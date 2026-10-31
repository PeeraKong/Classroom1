"""ScreenTimeGuard - โปรแกรมจำกัดเวลาเล่นคอมพิวเตอร์สำหรับเด็ก

ความสามารถ
- กำหนดเวลาเล่นได้ต่อวัน แยกตามวันในสัปดาห์
- กำหนดช่วงเวลาที่อนุญาตให้ใช้เครื่อง (เช่น 07:00-21:00)
- มีนาฬิกานับถอยหลังเล็ก ๆ มุมจอ และเตือนก่อนหมดเวลา 10 / 5 / 1 นาที
- หมดเวลาแล้วขึ้นหน้าจอล็อกเต็มจอ ปิดไม่ได้ ต้องใช้รหัสผู้ปกครองถึงจะเล่นต่อได้
- เลือกได้ว่าหมดเวลาแล้วจะ ล็อกจออย่างเดียว / ออกจากระบบ / ปิดเครื่อง
- การตั้งค่าทั้งหมดต้องใช้รหัสผ่านผู้ปกครอง

วิธีเปิดหน้าตั้งค่า: ดับเบิลคลิกที่นาฬิกามุมจอ แล้วใส่รหัสผู้ปกครอง
"""

import ctypes
import datetime as dt
import hashlib
import hmac
import json
import os
import secrets
import socket
import subprocess
import sys
import time
import tkinter as tk
from tkinter import ttk

APP_NAME = "ScreenTimeGuard"
IS_WINDOWS = sys.platform == "win32"

TICK_MS = 1000
SAVE_EVERY = 15        # วินาที: บันทึกเวลาที่ใช้ไปลงไฟล์ทุก ๆ เท่านี้
SLEEP_GAP = 30         # วินาที: ถ้าห่างจากรอบก่อนเกินนี้ แปลว่าเครื่องเพิ่งตื่นจาก sleep ไม่นับเวลา
WARN_AT = (600, 300, 60)
INF = float("inf")

DAYS = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
DAY_TH = ["จันทร์", "อังคาร", "พุธ", "พฤหัสบดี", "ศุกร์", "เสาร์", "อาทิตย์"]
ACTIONS = {
    "lock": "ล็อกหน้าจออย่างเดียว",
    "logoff": "ออกจากระบบ (Sign out)",
    "shutdown": "ปิดเครื่อง",
}

FONT = "Leelawadee UI" if IS_WINDOWS else "TkDefaultFont"

DEFAULT_CONFIG = {
    "daily_minutes": {"mon": 60, "tue": 60, "wed": 60, "thu": 60, "fri": 90, "sat": 180, "sun": 180},
    "allowed_start": "07:00",
    "allowed_end": "21:00",
    "action": "lock",
    "action_delay_seconds": 60,
    "idle_minutes": 0,
    "salt": "",
    "password_hash": "",
}


# ---------------------------------------------------------------- ไฟล์ข้อมูล

def _data_dir():
    if IS_WINDOWS:
        base = os.environ.get("ProgramData", r"C:\ProgramData")
    else:
        base = os.path.expanduser("~/.local/share")
    path = os.path.join(base, APP_NAME)
    os.makedirs(path, exist_ok=True)
    return path


def _backup_dir():
    if IS_WINDOWS:
        base = os.environ.get("APPDATA", os.path.expanduser("~"))
    else:
        base = os.path.expanduser("~/.cache")
    path = os.path.join(base, APP_NAME)
    os.makedirs(path, exist_ok=True)
    return path


DATA_DIR = _data_dir()
CONFIG_PATH = os.path.join(DATA_DIR, "config.json")
USAGE_PATH = os.path.join(DATA_DIR, "usage.json")
USAGE_BACKUP_PATH = os.path.join(_backup_dir(), "usage.json")


def read_json(path):
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, dict) else None
    except (OSError, ValueError):
        return None


def write_json(path, data):
    # เขียนทับไฟล์เดิมตรง ๆ (ไม่ใช้ rename) เพราะโฟลเดอร์ข้อมูลตั้งสิทธิ์ไว้ไม่ให้เด็กลบไฟล์
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except OSError:
        pass


def load_config():
    cfg = json.loads(json.dumps(DEFAULT_CONFIG))
    saved = read_json(CONFIG_PATH) or {}
    for key, value in saved.items():
        if key == "daily_minutes" and isinstance(value, dict):
            cfg["daily_minutes"].update({d: int(value[d]) for d in DAYS if d in value})
        elif key in cfg:
            cfg[key] = value
    return cfg


def hash_password(password, salt):
    return hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), bytes.fromhex(salt), 200_000).hex()


def set_password(cfg, password):
    cfg["salt"] = secrets.token_hex(16)
    cfg["password_hash"] = hash_password(password, cfg["salt"])


def check_password(cfg, password):
    if not cfg.get("password_hash"):
        return False
    return hmac.compare_digest(hash_password(password, cfg["salt"]), cfg["password_hash"])


def new_usage(date):
    return {"date": date, "used": 0.0, "bonus": 0.0, "unlimited": False, "override_until": 0.0}


def load_usage(today):
    """อ่านเวลาที่ใช้ไปจากทั้งไฟล์หลักและไฟล์สำรอง แล้วเลือกตัวที่ใช้เวลาไปมากที่สุด
    (กันเด็กลบไฟล์ใดไฟล์หนึ่งเพื่อรีเซ็ตเวลา)"""
    best = None
    for path in (USAGE_PATH, USAGE_BACKUP_PATH):
        d = read_json(path)
        if not d or not isinstance(d.get("date"), str):
            continue
        d = {**new_usage(d["date"]), **d}
        if best is None or (d["date"], d["used"]) > (best["date"], best["used"]):
            best = d
    # วันที่ในไฟล์ใหม่กว่าวันนี้ = มีคนย้อนนาฬิกาเครื่อง ให้นับต่อจากของเดิม ไม่รีเซ็ต
    if best is None or best["date"] < today:
        best = new_usage(today)
    return best


def save_usage(usage):
    write_json(USAGE_PATH, usage)
    write_json(USAGE_BACKUP_PATH, usage)


def parse_hm(text):
    h, m = str(text).strip().split(":")
    h, m = int(h), int(m)
    if not (0 <= h <= 24 and 0 <= m < 60):
        raise ValueError(text)
    return h * 60 + m


def window_seconds_left(start, end, now):
    """วินาทีที่เหลือก่อนหมดช่วงเวลาที่อนุญาต (0 = อยู่นอกช่วง, INF = ไม่จำกัดช่วงเวลา)"""
    start, end = parse_hm(start), parse_hm(end)
    if start == end:
        return INF
    mins = now.hour * 60 + now.minute + now.second / 60
    if start < end:
        inside = start <= mins < end
    else:  # ช่วงข้ามเที่ยงคืน เช่น 20:00-02:00
        inside = mins >= start or mins < end
    return ((end - mins) % 1440) * 60 if inside else 0


def format_seconds(sec):
    if sec == INF:
        return "ไม่จำกัด"
    sec = max(0, int(sec))
    return f"{sec // 3600}:{sec % 3600 // 60:02d}:{sec % 60:02d}"


# ---------------------------------------------------------------- ระบบปฏิบัติการ

if IS_WINDOWS:
    class _LASTINPUTINFO(ctypes.Structure):
        _fields_ = [("cbSize", ctypes.c_uint), ("dwTime", ctypes.c_uint)]


def idle_seconds():
    if not IS_WINDOWS:
        return 0
    info = _LASTINPUTINFO()
    info.cbSize = ctypes.sizeof(info)
    if not ctypes.windll.user32.GetLastInputInfo(ctypes.byref(info)):
        return 0
    return ((ctypes.windll.kernel32.GetTickCount() - info.dwTime) & 0xFFFFFFFF) / 1000


def virtual_screen(root):
    """ตำแหน่งและขนาดของทุกจอรวมกัน เพื่อให้หน้าจอล็อกคลุมทุกจอ"""
    if IS_WINDOWS:
        gsm = ctypes.windll.user32.GetSystemMetrics
        return gsm(76), gsm(77), gsm(78), gsm(79)
    return 0, 0, root.winfo_screenwidth(), root.winfo_screenheight()


def do_system_action(action):
    if not IS_WINDOWS:
        print(f"[{APP_NAME}] system action: {action}")
        return
    flags = 0x08000000  # CREATE_NO_WINDOW
    if action == "logoff":
        subprocess.run(["shutdown", "/l"], creationflags=flags)
    elif action == "shutdown":
        subprocess.run(["shutdown", "/s", "/t", "0"], creationflags=flags)


_instance_handle = None


def acquire_single_instance():
    """เปิดได้ทีละหนึ่งตัวต่อผู้ใช้หนึ่งคน (ตัวที่ถูกสั่งเปิดซ้ำจาก Task Scheduler จะปิดตัวเองไป)"""
    global _instance_handle
    if IS_WINDOWS:
        _instance_handle = ctypes.windll.kernel32.CreateMutexW(None, False, f"Local\\{APP_NAME}")
        return ctypes.windll.kernel32.GetLastError() != 183  # ERROR_ALREADY_EXISTS
    _instance_handle = socket.socket()
    try:
        _instance_handle.bind(("127.0.0.1", 47613))
        return True
    except OSError:
        return False


# ---------------------------------------------------------------- หน้าต่าง

class PasswordDialog:
    def __init__(self, parent, title="รหัสผู้ปกครอง"):
        self.ok = False
        self.value = ""
        w = self.win = tk.Toplevel(parent)
        w.title(title)
        w.attributes("-topmost", True)
        w.resizable(False, False)
        tk.Label(w, text="ใส่รหัสผ่านผู้ปกครอง", font=(FONT, 11)).pack(padx=20, pady=(15, 5))
        self.entry = tk.Entry(w, show="•", font=(FONT, 12), width=22)
        self.entry.pack(padx=20)
        self.error = tk.Label(w, text="", fg="#c0392b", font=(FONT, 10))
        self.error.pack()
        row = tk.Frame(w)
        row.pack(pady=(0, 15))
        tk.Button(row, text="ตกลง", width=10, command=self.submit).pack(side="left", padx=5)
        tk.Button(row, text="ยกเลิก", width=10, command=w.destroy).pack(side="left", padx=5)
        self.entry.bind("<Return>", lambda e: self.submit())
        w.bind("<Escape>", lambda e: w.destroy())
        w.update_idletasks()
        w.geometry(f"+{(w.winfo_screenwidth() - w.winfo_width()) // 2}+{(w.winfo_screenheight() - w.winfo_height()) // 3}")
        w.focus_force()
        self.entry.focus_set()
        w.grab_set()

    def submit(self):
        self.value = self.entry.get()
        self.ok = True
        self.win.destroy()


class App:
    def __init__(self, setup_only=False):
        self.root = tk.Tk()
        self.root.withdraw()
        self.cfg = load_config()
        self.usage = load_usage(dt.date.today().isoformat())
        self.warned = set()
        self.lock_win = None
        self.settings_win = None

        if setup_only or not self.cfg["password_hash"]:
            self.open_settings(first_run=not self.cfg["password_hash"])
            self.root.wait_window(self.settings_win)
            if setup_only or not self.cfg["password_hash"]:
                self.root.destroy()
                raise SystemExit

        self.last_tick = time.monotonic()
        self.last_save = self.last_tick
        self.build_timer()
        self.root.after(TICK_MS, self.tick)
        self.root.after(500, self.keep_lock_on_top)

    # ---------- คำนวณเวลา

    def time_left(self):
        weekday = DAYS[dt.date.today().weekday()]
        return self.cfg["daily_minutes"][weekday] * 60 + self.usage["bonus"] - self.usage["used"]

    def window_left(self):
        try:
            left = window_seconds_left(self.cfg["allowed_start"], self.cfg["allowed_end"], dt.datetime.now())
        except ValueError:
            left = INF
        return max(left, self.usage["override_until"] - time.time(), 0)

    def status(self):
        """คืนค่า (วินาทีที่เหลือ, เหตุผลที่ต้องล็อก หรือ None)"""
        if self.usage["unlimited"]:
            return INF, None
        window = self.window_left()
        if window <= 0:
            return 0, "outside"
        left = self.time_left()
        if left <= 0:
            return 0, "timeup"
        return min(left, window), None

    def is_idle(self):
        limit = self.cfg.get("idle_minutes") or 0
        return limit > 0 and idle_seconds() >= limit * 60

    def grant(self, minutes):
        """ให้เล่นต่อได้อีก minutes นาที นับจากตอนนี้"""
        need = minutes * 60
        if self.time_left() < need:
            self.usage["bonus"] += need - self.time_left()
        self.usage["override_until"] = max(self.usage["override_until"], time.time() + need)
        self.warned.clear()
        save_usage(self.usage)

    # ---------- วงรอบหลัก

    def tick(self):
        now = time.monotonic()
        delta, self.last_tick = now - self.last_tick, now

        today = dt.date.today().isoformat()
        if today > self.usage["date"]:
            self.usage = new_usage(today)
            self.warned.clear()

        left, reason = self.status()
        if reason:
            self.show_lock(reason)
        else:
            self.hide_lock()
            if 0 < delta < SLEEP_GAP and not self.is_idle():
                self.usage["used"] += delta
                left -= delta
            for mark in WARN_AT:
                if left <= mark and mark not in self.warned:
                    self.warned.add(mark)
                    if left > 0:
                        self.toast(f"เหลือเวลาเล่นอีก {mark // 60} นาที\nเก็บงานให้เรียบร้อยนะ")

        if now - self.last_save >= SAVE_EVERY:
            save_usage(self.usage)
            self.last_save = now

        self.timer_label.config(text=format_seconds(left),
                                fg="#e74c3c" if left <= 300 else "#ffffff")
        self.root.after(TICK_MS, self.tick)

    # ---------- นาฬิกามุมจอ

    def build_timer(self):
        r = self.root
        r.overrideredirect(True)
        r.attributes("-topmost", True)
        try:
            r.attributes("-alpha", 0.85)
        except tk.TclError:
            pass
        r.configure(bg="#2c3e50")
        tk.Label(r, text="เวลาที่เหลือ", font=(FONT, 9), bg="#2c3e50", fg="#bdc3c7").pack(padx=12, pady=(6, 0))
        self.timer_label = tk.Label(r, text="--:--:--", font=(FONT, 18, "bold"), bg="#2c3e50", fg="#ffffff")
        self.timer_label.pack(padx=12, pady=(0, 6))
        r.update_idletasks()
        r.geometry(f"+{r.winfo_screenwidth() - r.winfo_width() - 20}+{r.winfo_screenheight() - r.winfo_height() - 70}")
        r.deiconify()

        for widget in (r, *r.winfo_children()):
            widget.bind("<ButtonPress-1>", self._drag_start)
            widget.bind("<B1-Motion>", self._drag_move)
            widget.bind("<Double-Button-1>", lambda e: self.ask_settings())

    def _drag_start(self, event):
        self._drag = (event.x_root - self.root.winfo_x(), event.y_root - self.root.winfo_y())

    def _drag_move(self, event):
        dx, dy = self._drag
        self.root.geometry(f"+{event.x_root - dx}+{event.y_root - dy}")

    def toast(self, message):
        t = tk.Toplevel(self.root)
        t.overrideredirect(True)
        t.attributes("-topmost", True)
        t.configure(bg="#f39c12")
        tk.Label(t, text=message, font=(FONT, 14, "bold"), bg="#f39c12", fg="#000000",
                 justify="center").pack(padx=30, pady=20)
        t.update_idletasks()
        t.geometry(f"+{(t.winfo_screenwidth() - t.winfo_width()) // 2}+60")
        t.bind("<Button-1>", lambda e: t.destroy())
        t.after(8000, t.destroy)

    # ---------- หน้าจอล็อก

    def show_lock(self, reason):
        if reason == "outside":
            text = (f"ตอนนี้อยู่นอกเวลาที่อนุญาตให้ใช้คอมพิวเตอร์\n"
                    f"(ใช้ได้ {self.cfg['allowed_start']} - {self.cfg['allowed_end']} น.)")
        else:
            text = "หมดเวลาเล่นคอมพิวเตอร์ของวันนี้แล้ว\nไปพักสายตา ออกไปวิ่งเล่นกันเถอะ!"

        if self.lock_win:
            self.lock_msg.config(text=text)
        else:
            self.build_lock()
            self.lock_msg.config(text=text)
            self.lock_started = time.monotonic()
            self.action_done = False
            save_usage(self.usage)

        action = self.cfg.get("action", "lock")
        if action != "lock" and not self.action_done:
            remain = self.cfg.get("action_delay_seconds", 60) - (time.monotonic() - self.lock_started)
            if remain <= 0:
                self.action_done = True
                do_system_action(action)
            else:
                verb = "ออกจากระบบ" if action == "logoff" else "ปิดเครื่อง"
                self.lock_countdown.config(text=f"เครื่องจะ{verb}อัตโนมัติใน {int(remain)} วินาที\n"
                                                f"กรุณาบันทึกงานให้เรียบร้อย")

    def build_lock(self):
        bg = "#1a252f"
        w = self.lock_win = tk.Toplevel(self.root)
        w.overrideredirect(True)
        x, y, width, height = virtual_screen(self.root)
        w.geometry(f"{width}x{height}+{x}+{y}")
        w.attributes("-topmost", True)
        w.configure(bg=bg, cursor="arrow")
        w.protocol("WM_DELETE_WINDOW", lambda: None)

        box = tk.Frame(w, bg=bg)
        box.place(relx=0.5, rely=0.5, anchor="center")
        tk.Label(box, text="⏰", font=(FONT, 72), bg=bg, fg="#f1c40f").pack()
        self.lock_msg = tk.Label(box, font=(FONT, 24, "bold"), bg=bg, fg="#ecf0f1", justify="center")
        self.lock_msg.pack(pady=10)
        self.lock_countdown = tk.Label(box, text="", font=(FONT, 14), bg=bg, fg="#e67e22", justify="center")
        self.lock_countdown.pack(pady=(0, 20))

        tk.Label(box, text="สำหรับผู้ปกครอง: ใส่รหัสผ่านแล้วเลือกเวลาที่จะให้เล่นต่อ",
                 font=(FONT, 12), bg=bg, fg="#95a5a6").pack()
        self.lock_entry = tk.Entry(box, show="•", font=(FONT, 16), width=20, justify="center")
        self.lock_entry.pack(pady=8)
        self.lock_error = tk.Label(box, text="", font=(FONT, 12), bg=bg, fg="#e74c3c")
        self.lock_error.pack()

        row = tk.Frame(box, bg=bg)
        row.pack(pady=8)
        for minutes in (15, 30, 60):
            tk.Button(row, text=f"+{minutes} นาที", font=(FONT, 12), width=10,
                      command=lambda m=minutes: self.unlock(m)).pack(side="left", padx=5)
        tk.Button(row, text="ไม่จำกัดวันนี้", font=(FONT, 12), width=12,
                  command=lambda: self.unlock(None)).pack(side="left", padx=5)

        # กันปุ่มลัดปิดหน้าต่าง
        for seq in ("<Alt-F4>", "<Escape>"):
            w.bind(seq, lambda e: "break")
        self.lock_entry.bind("<Return>", lambda e: self.unlock(15))
        w.focus_force()
        self.lock_entry.focus_set()
        try:
            w.grab_set()
        except tk.TclError:
            pass

    def unlock(self, minutes):
        if not check_password(self.cfg, self.lock_entry.get()):
            self.lock_entry.delete(0, "end")
            self.lock_error.config(text="รหัสผ่านไม่ถูกต้อง")
            return
        if minutes is None:
            self.usage["unlimited"] = True
            save_usage(self.usage)
        else:
            self.grant(minutes)
        self.hide_lock()

    def hide_lock(self):
        if self.lock_win:
            self.lock_win.destroy()
            self.lock_win = None

    def keep_lock_on_top(self):
        if self.lock_win:
            self.lock_win.lift()
            self.lock_win.attributes("-topmost", True)
            if self.lock_win.focus_get() is None:
                self.lock_win.focus_force()
                self.lock_entry.focus_set()
        else:
            self.root.lift()
        self.root.after(500, self.keep_lock_on_top)

    # ---------- หน้าตั้งค่า

    def ask_settings(self):
        if self.settings_win or self.lock_win:
            return
        dialog = PasswordDialog(self.root)
        self.root.wait_window(dialog.win)
        if not dialog.ok:
            return
        if check_password(self.cfg, dialog.value):
            self.open_settings()
        else:
            self.toast("รหัสผ่านไม่ถูกต้อง")

    def open_settings(self, first_run=False):
        cfg = self.cfg
        w = self.settings_win = tk.Toplevel(self.root)
        w.title(f"{APP_NAME} - ตั้งค่า")
        w.attributes("-topmost", True)
        w.resizable(False, False)
        pad = {"padx": 8, "pady": 3}

        frame = ttk.Frame(w, padding=15)
        frame.pack()
        if first_run:
            ttk.Label(frame, text="ยินดีต้อนรับ! กรุณาตั้งรหัสผ่านผู้ปกครองก่อนเริ่มใช้งาน",
                      font=(FONT, 11, "bold")).grid(row=0, column=0, columnspan=2, pady=(0, 10))

        days = ttk.LabelFrame(frame, text="เวลาเล่นต่อวัน (นาที)  —  0 = ห้ามเล่น, 1440 = ไม่จำกัด", padding=8)
        days.grid(row=1, column=0, columnspan=2, sticky="ew", pady=5)
        day_vars = {}
        for i, (key, name) in enumerate(zip(DAYS, DAY_TH)):
            ttk.Label(days, text=f"วัน{name}").grid(row=i // 2, column=(i % 2) * 2, sticky="w", **pad)
            var = tk.StringVar(value=str(cfg["daily_minutes"][key]))
            ttk.Spinbox(days, from_=0, to=1440, increment=15, width=7,
                        textvariable=var).grid(row=i // 2, column=(i % 2) * 2 + 1, **pad)
            day_vars[key] = var

        other = ttk.LabelFrame(frame, text="อื่น ๆ", padding=8)
        other.grid(row=2, column=0, columnspan=2, sticky="ew", pady=5)
        start_var = tk.StringVar(value=cfg["allowed_start"])
        end_var = tk.StringVar(value=cfg["allowed_end"])
        action_var = tk.StringVar(value=ACTIONS.get(cfg["action"], ACTIONS["lock"]))
        delay_var = tk.StringVar(value=str(cfg["action_delay_seconds"]))
        idle_var = tk.StringVar(value=str(cfg["idle_minutes"]))

        ttk.Label(other, text="ใช้เครื่องได้ตั้งแต่ (ชม:นาที)").grid(row=0, column=0, sticky="w", **pad)
        hours = ttk.Frame(other)
        hours.grid(row=0, column=1, sticky="w", **pad)
        ttk.Entry(hours, textvariable=start_var, width=6).pack(side="left")
        ttk.Label(hours, text=" ถึง ").pack(side="left")
        ttk.Entry(hours, textvariable=end_var, width=6).pack(side="left")
        ttk.Label(other, text="เมื่อหมดเวลา").grid(row=1, column=0, sticky="w", **pad)
        ttk.Combobox(other, textvariable=action_var, values=list(ACTIONS.values()),
                     state="readonly", width=24).grid(row=1, column=1, sticky="w", **pad)
        ttk.Label(other, text="รอก่อนออกจากระบบ/ปิดเครื่อง (วินาที)").grid(row=2, column=0, sticky="w", **pad)
        ttk.Entry(other, textvariable=delay_var, width=6).grid(row=2, column=1, sticky="w", **pad)
        ttk.Label(other, text="หยุดนับเมื่อไม่ได้แตะเครื่องเกิน (นาที, 0 = นับตลอด)").grid(row=3, column=0, sticky="w", **pad)
        ttk.Entry(other, textvariable=idle_var, width=6).grid(row=3, column=1, sticky="w", **pad)

        pw = ttk.LabelFrame(frame, text="รหัสผ่านผู้ปกครอง" + ("" if first_run else " (เว้นว่างถ้าไม่เปลี่ยน)"), padding=8)
        pw.grid(row=3, column=0, columnspan=2, sticky="ew", pady=5)
        pw1, pw2 = tk.StringVar(), tk.StringVar()
        ttk.Label(pw, text="รหัสใหม่").grid(row=0, column=0, sticky="w", **pad)
        ttk.Entry(pw, textvariable=pw1, show="•", width=22).grid(row=0, column=1, **pad)
        ttk.Label(pw, text="ยืนยันรหัส").grid(row=1, column=0, sticky="w", **pad)
        ttk.Entry(pw, textvariable=pw2, show="•", width=22).grid(row=1, column=1, **pad)

        error = ttk.Label(frame, text="", foreground="#c0392b")
        error.grid(row=4, column=0, columnspan=2)

        def save():
            try:
                daily = {k: int(v.get()) for k, v in day_vars.items()}
                if any(not 0 <= m <= 1440 for m in daily.values()):
                    raise ValueError
                parse_hm(start_var.get())
                parse_hm(end_var.get())
                delay = max(0, int(delay_var.get()))
                idle = max(0, int(idle_var.get()))
            except ValueError:
                error.config(text="ข้อมูลไม่ถูกต้อง: นาทีต้องเป็นตัวเลข 0-1440 และเวลาต้องเป็นรูปแบบ 07:00")
                return
            if pw1.get() != pw2.get():
                error.config(text="รหัสผ่านทั้งสองช่องไม่ตรงกัน")
                return
            if first_run and len(pw1.get()) < 4:
                error.config(text="รหัสผ่านต้องยาวอย่างน้อย 4 ตัวอักษร")
                return
            if pw1.get():
                if len(pw1.get()) < 4:
                    error.config(text="รหัสผ่านต้องยาวอย่างน้อย 4 ตัวอักษร")
                    return
                set_password(cfg, pw1.get())
            cfg["daily_minutes"] = daily
            cfg["allowed_start"] = start_var.get().strip()
            cfg["allowed_end"] = end_var.get().strip()
            cfg["action"] = next(k for k, v in ACTIONS.items() if v == action_var.get())
            cfg["action_delay_seconds"] = delay
            cfg["idle_minutes"] = idle
            write_json(CONFIG_PATH, cfg)
            self.warned.clear()
            close()

        def close():
            w.destroy()
            self.settings_win = None

        buttons = ttk.Frame(frame)
        buttons.grid(row=5, column=0, columnspan=2, pady=(10, 0))
        ttk.Button(buttons, text="บันทึก", command=save).pack(side="left", padx=4)
        if not first_run:
            def reset_today():
                self.usage = new_usage(dt.date.today().isoformat())
                self.warned.clear()
                save_usage(self.usage)
                used_label.config(text="วันนี้ใช้ไปแล้ว 0:00:00")

            def quit_app():
                save_usage(self.usage)
                self.root.destroy()

            ttk.Button(buttons, text="รีเซ็ตเวลาวันนี้", command=reset_today).pack(side="left", padx=4)
            ttk.Button(buttons, text="ปิดโปรแกรมชั่วคราว", command=quit_app).pack(side="left", padx=4)
            used_label = ttk.Label(frame, text=f"วันนี้ใช้ไปแล้ว {format_seconds(self.usage['used'])}")
            used_label.grid(row=6, column=0, columnspan=2, pady=(8, 0))
        ttk.Button(buttons, text="ยกเลิก", command=close).pack(side="left", padx=4)
        w.protocol("WM_DELETE_WINDOW", close)
        w.focus_force()


def main():
    if IS_WINDOWS:
        try:
            ctypes.windll.shcore.SetProcessDpiAwareness(1)
        except (AttributeError, OSError):
            pass
    setup_only = "--setup" in sys.argv
    if not setup_only and not acquire_single_instance():
        return
    try:
        app = App(setup_only=setup_only)
    except SystemExit:
        return
    app.root.mainloop()


if __name__ == "__main__":
    main()
