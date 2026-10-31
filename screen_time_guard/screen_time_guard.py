"""ScreenTimeGuard - โปรแกรมจำกัดเวลาเล่นคอมพิวเตอร์สำหรับเด็ก

ความสามารถ
- กำหนดเวลาเล่นได้ต่อวัน แยกตามวันในสัปดาห์
- กำหนดช่วงเวลาที่อนุญาตให้ใช้เครื่อง (เช่น 07:00-21:00)
- มีนาฬิกานับถอยหลังเล็ก ๆ มุมจอ และเตือนก่อนหมดเวลา 10 / 5 / 1 นาที
- หมดเวลาแล้วขึ้นหน้าจอล็อกเต็มจอ ปิดไม่ได้ ต้องใช้รหัสผู้ปกครองถึงจะเล่นต่อได้
- เลือกได้ว่าหมดเวลาแล้วจะ ล็อกจออย่างเดียว / ออกจากระบบ / ปิดเครื่อง
- การตั้งค่าทั้งหมดต้องใช้รหัสผ่านผู้ปกครอง
- สั่งงานจากมือถือผ่าน Telegram ได้: ดูสถานะ ให้เวลาเพิ่ม ล็อก/ปลดล็อกเครื่อง และรับแจ้งเตือน

วิธีเปิดหน้าตั้งค่า: ดับเบิลคลิกที่นาฬิกามุมจอ แล้วใส่รหัสผู้ปกครอง

โหมดการรัน
  (ไม่ใส่อะไร)   ถ้าเป็นไฟล์ .exe ที่ยังไม่ได้ติดตั้ง = เปิดหน้าติดตั้ง, นอกนั้น = เริ่มจำกัดเวลา
  --install       เปิดหน้าติดตั้ง (จะขอสิทธิ์ Administrator เอง)
  --run           เริ่มจำกัดเวลา (Task Scheduler เรียกแบบนี้)
  --setup         เปิดหน้าตั้งค่าอย่างเดียว
"""

import ctypes
import datetime as dt
import hashlib
import hmac
import json
import os
import queue
import secrets
import shutil
import socket
import subprocess
import sys
import threading
import base64
import time
import urllib.request
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
    "telegram_token": "",
    "telegram_chat_ids": [],
    "limit_admins": False,
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
    return {"date": date, "used": 0.0, "bonus": 0.0, "unlimited": False, "override_until": 0.0,
            "forced_lock": False, "last_seen": 0.0}


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


def is_admin_account():
    """บัญชีนี้เป็น Administrator หรือไม่ (นับด้วยแม้ตอนนี้ UAC ยังไม่ได้ยกสิทธิ์)
    ปกติไม่จำกัดเวลาบัญชีผู้ดูแล จะได้ไม่ไปล็อกเครื่องตอนพ่อแม่ใช้"""
    if not IS_WINDOWS:
        return False
    try:
        out = subprocess.run(["whoami", "/groups"], capture_output=True, text=True,
                             creationflags=0x08000000).stdout
    except OSError:
        return False
    return "S-1-5-32-544" in out


def is_elevated():
    return IS_WINDOWS and bool(ctypes.windll.shell32.IsUserAnAdmin())


def relaunch_elevated(args):
    """เปิดตัวเองใหม่ด้วยสิทธิ์ Administrator (Windows จะถามยืนยันผ่าน UAC)"""
    if getattr(sys, "frozen", False):
        params = args
    else:
        params = f'"{os.path.abspath(__file__)}" {args}'
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)


# ---------------------------------------------------------------- ติดตั้ง / ถอนการติดตั้ง

INSTALL_DIR = os.path.join(os.environ.get("ProgramFiles", r"C:\Program Files"), APP_NAME)
EXE_NAME = f"{APP_NAME}.exe"


def run_powershell(script):
    encoded = base64.b64encode(script.encode("utf-16-le")).decode("ascii")
    return subprocess.run(["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-EncodedCommand", encoded],
                          capture_output=True, text=True, creationflags=0x08000000)


def ps_quote(text):
    return "'" + str(text).replace("'", "''") + "'"


def is_installed():
    return IS_WINDOWS and run_powershell(
        f"if (Get-ScheduledTask -TaskName {ps_quote(APP_NAME)} -ErrorAction SilentlyContinue) {{ 'yes' }}"
    ).stdout.strip() == "yes"


def stop_running_copies():
    run_powershell(
        "Get-CimInstance Win32_Process | Where-Object { $_.ProcessId -ne $PID -and $_.ProcessId -ne "
        f"{os.getpid()} -and ($_.ExecutablePath -like {ps_quote(os.path.join(INSTALL_DIR, '*'))} -or "
        "$_.CommandLine -like '*screen_time_guard.py*--run*') } | "
        "ForEach-Object { Stop-Process -Id $_.ProcessId -Force }")


def install_files():
    """คัดลอกโปรแกรมไป Program Files, ตั้งสิทธิ์โฟลเดอร์ข้อมูล และตั้ง Task Scheduler (ต้องเป็น Administrator)"""
    stop_running_copies()
    os.makedirs(INSTALL_DIR, exist_ok=True)
    if getattr(sys, "frozen", False):
        target = os.path.join(INSTALL_DIR, EXE_NAME)
        if os.path.normcase(os.path.abspath(sys.executable)) != os.path.normcase(target):
            shutil.copy2(sys.executable, target)
        execute, argument = target, "--run"
    else:
        target = os.path.join(INSTALL_DIR, "screen_time_guard.py")
        shutil.copy2(os.path.abspath(__file__), target)
        execute = os.path.join(os.path.dirname(sys.executable), "pythonw.exe")
        argument = f'"{target}" --run'

    for path in (CONFIG_PATH, USAGE_PATH):
        if not os.path.exists(path):
            write_json(path, {})
    # ผู้ใช้ทั่วไป (Users) อ่าน/เขียนไฟล์ได้ แต่ลบไม่ได้, Administrators และ SYSTEM ทำได้ทุกอย่าง
    subprocess.run(["icacls", DATA_DIR, "/inheritance:r", "/grant:r", "*S-1-5-32-544:(OI)(CI)F",
                    "*S-1-5-18:(OI)(CI)F", "*S-1-5-32-545:(OI)(CI)(RX,W)", "/T"],
                   capture_output=True, creationflags=0x08000000)

    # เปิดเองตอนล็อกอิน และเปิดซ้ำทุก 1 นาทีถ้าโดนปิด
    result = run_powershell(f"""
$ErrorActionPreference = 'Stop'
$action = New-ScheduledTaskAction -Execute {ps_quote(execute)} -Argument {ps_quote(argument)}
$atLogon = New-ScheduledTaskTrigger -AtLogOn
$repeat = New-ScheduledTaskTrigger -Once -At (Get-Date) -RepetitionInterval (New-TimeSpan -Minutes 1) -RepetitionDuration (New-TimeSpan -Days 3650)
$principal = New-ScheduledTaskPrincipal -GroupId 'S-1-5-32-545' -RunLevel Limited
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -ExecutionTimeLimit (New-TimeSpan -Seconds 0) -MultipleInstances IgnoreNew -StartWhenAvailable
Register-ScheduledTask -TaskName {ps_quote(APP_NAME)} -Action $action -Trigger $atLogon, $repeat -Principal $principal -Settings $settings -Force | Out-Null
""")
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "ตั้ง Task Scheduler ไม่สำเร็จ")


def start_installed():
    run_powershell(f"Start-ScheduledTask -TaskName {ps_quote(APP_NAME)}")


def uninstall_files():
    run_powershell(f"Unregister-ScheduledTask -TaskName {ps_quote(APP_NAME)} -Confirm:$false -ErrorAction SilentlyContinue")
    stop_running_copies()
    shutil.rmtree(DATA_DIR, ignore_errors=True)
    shutil.rmtree(INSTALL_DIR, ignore_errors=True)
    if os.path.exists(INSTALL_DIR):  # ลบไฟล์ที่กำลังเปิดอยู่ไม่ได้ ให้ลบตามหลังตอนปิดโปรแกรมแล้ว
        subprocess.Popen(f'cmd /c ping -n 4 127.0.0.1 >nul & rmdir /s /q "{INSTALL_DIR}"',
                         creationflags=0x08000000)


# ---------------------------------------------------------------- Telegram

PC_NAME = f"{os.environ.get('USERNAME') or os.environ.get('USER', '?')}@{socket.gethostname()}"
BUTTONS = {
    "📊 สถานะ": "/status",
    "➕ 15 นาที": "/add 15",
    "➕ 30 นาที": "/add 30",
    "➕ 60 นาที": "/add 60",
    "🔒 ล็อกเลย": "/lock",
    "🔓 ปลดล็อก": "/unlock",
    "♾️ ไม่จำกัดวันนี้": "/unlimited",
    "⚙️ ตั้งค่า": "/settings",
    "❓ วิธีใช้": "/help",
}
KEYBOARD = {"keyboard": [[{"text": t} for t in row] for row in (
    list(BUTTONS)[0:1], list(BUTTONS)[1:4], list(BUTTONS)[4:6], list(BUTTONS)[6:9])],
    "resize_keyboard": True, "is_persistent": True}
HELP_TEXT = (
    "คำสั่งที่ใช้ได้\n"
    "/status – ดูเวลาที่ใช้ไปและเวลาที่เหลือ\n"
    "/add 30 – ให้เล่นต่ออีก 30 นาที (ใส่ตัวเลขกี่นาทีก็ได้)\n"
    "/lock – ล็อกเครื่องทันทีจนกว่าจะสั่ง /unlock\n"
    "/unlock – ยกเลิกการล็อกที่สั่งไว้\n"
    "/unlimited – ไม่จำกัดเวลาเฉพาะวันนี้\n"
    "/reset – รีเซ็ตเวลาที่ใช้ไปของวันนี้\n"
    "\n"
    "ตั้งค่า\n"
    "/settings – ดูการตั้งค่าทั้งหมด\n"
    "/limit all 60 – ทุกวันเล่นได้ 60 นาที\n"
    "/limit weekday 60 – วันจันทร์-ศุกร์\n"
    "/limit weekend 180 – วันเสาร์-อาทิตย์\n"
    "/limit sat 120 – เฉพาะวัน (mon tue wed thu fri sat sun)\n"
    "/hours 07:00 21:00 – ช่วงเวลาที่ใช้เครื่องได้ (/hours off = ทั้งวัน)\n"
    "/action lock – หมดเวลาแล้ว lock=ล็อกจอ, logoff=ออกจากระบบ, shutdown=ปิดเครื่อง\n"
    "/idle 10 – ไม่นับเวลาถ้าไม่แตะเครื่องเกิน 10 นาที (0 = นับตลอด)\n"
    "/password 1234 – ตั้งรหัสปลดล็อกที่หน้าจอคอม\n"
    "\n"
    "หรือกดปุ่มด้านล่างได้เลย"
)
DAY_ALIASES = {
    "all": DAYS, "ทุกวัน": DAYS,
    "weekday": DAYS[:5], "weekdays": DAYS[:5], "วันธรรมดา": DAYS[:5],
    "weekend": DAYS[5:], "weekends": DAYS[5:], "เสาร์อาทิตย์": DAYS[5:],
    **{d: [d] for d in DAYS}, **{name: [d] for d, name in zip(DAYS, DAY_TH)},
}


class TelegramRemote:
    """คุยกับ Telegram Bot API ในเธรดแยก ข้อความที่เข้ามาจะถูกส่งต่อให้เธรดหลักผ่าน incoming
    (เธรดนี้ไม่แตะหน้าต่าง tkinter เลย)"""

    def __init__(self, cfg):
        self.cfg = cfg
        self.incoming = queue.Queue()
        self.outgoing = queue.Queue()
        self.offset = None
        self.stopped = False
        threading.Thread(target=self._poll_loop, daemon=True).start()
        threading.Thread(target=self._send_loop, daemon=True).start()

    def _call(self, method, payload, timeout=15):
        url = f"https://api.telegram.org/bot{self.cfg['telegram_token']}/{method}"
        req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"),
                                     headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))

    def get_me(self):
        """ตรวจ token และคืนชื่อบอท (@username) หรือ None ถ้า token ใช้ไม่ได้"""
        try:
            data = self._call("getMe", {}, timeout=15)
        except Exception:
            return None
        return data.get("result", {}).get("username") if data.get("ok") else None

    def ack(self):
        """บอก Telegram ว่าอ่านข้อความที่ได้มาแล้ว (จะได้ไม่ส่งซ้ำให้โปรแกรมตัวถัดไป)"""
        if self.offset is not None:
            try:
                self._call("getUpdates", {"offset": self.offset, "timeout": 0}, timeout=15)
            except Exception:
                pass

    def _poll_loop(self):
        token = None
        while not self.stopped:
            if not self.cfg.get("telegram_token"):
                time.sleep(5)
                continue
            if token != self.cfg["telegram_token"]:
                self.offset, token = None, self.cfg["telegram_token"]
            try:
                data = self._call("getUpdates", {"offset": self.offset, "timeout": 25,
                                                 "allowed_updates": ["message"]}, timeout=35)
            except Exception:
                time.sleep(10)  # ไม่มีเน็ต หรือ token ผิด ลองใหม่ทีหลัง
                continue
            for update in data.get("result", []):
                self.offset = update["update_id"] + 1
                msg = update.get("message") or {}
                # ไม่ทำตามคำสั่งเก่าที่ค้างไว้นานตอนเครื่องปิดอยู่
                if msg.get("text") and time.time() - msg.get("date", 0) < 600 and not self.stopped:
                    self.incoming.put((msg["chat"]["id"], msg["message_id"], msg["text"]))

    def _send_loop(self):
        while True:
            method, payload = self.outgoing.get()
            for _ in range(3):
                try:
                    self._call(method, payload)
                    break
                except Exception:
                    if method == "deleteMessage":
                        break
                    time.sleep(5)

    def send(self, chat_id, text):
        if self.cfg.get("telegram_token"):
            self.outgoing.put(("sendMessage", {"chat_id": chat_id, "text": text, "reply_markup": KEYBOARD}))

    def delete(self, chat_id, message_id):
        if self.cfg.get("telegram_token"):
            self.outgoing.put(("deleteMessage", {"chat_id": chat_id, "message_id": message_id}))

    def notify(self, text):
        for chat_id in self.cfg.get("telegram_chat_ids", []):
            self.send(chat_id, f"[{PC_NAME}]\n{text}")


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
        self.pair_code, self.pair_expires = None, 0

        configured = self.cfg["password_hash"] or self.cfg["telegram_chat_ids"]
        if setup_only or not configured:
            self.open_settings(first_run=not self.cfg["password_hash"])
            self.root.wait_window(self.settings_win)
            if setup_only or not self.cfg["password_hash"]:
                self.root.destroy()
                raise SystemExit

        self.last_tick = time.monotonic()
        self.last_save = self.last_tick
        self.remote = TelegramRemote(self.cfg)
        if time.time() - self.usage["last_seen"] < 180:
            self.remote.notify("⚠️ โปรแกรมถูกปิดแล้วเปิดขึ้นมาใหม่ (อาจมีคนพยายามปิดโปรแกรม)")
        else:
            self.remote.notify("💻 มีการเข้าใช้งานคอมพิวเตอร์\n" + self.status_text())
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
        if self.usage["forced_lock"]:
            return 0, "parent"
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

    def reset_today(self):
        forced = self.usage["forced_lock"]
        self.usage = new_usage(dt.date.today().isoformat())
        self.usage["forced_lock"] = forced
        self.warned.clear()
        save_usage(self.usage)

    def status_text(self):
        left, reason = self.status()
        weekday = dt.date.today().weekday()
        state = {
            None: "🟢 กำลังใช้งานได้",
            "timeup": "🔴 ล็อกอยู่ (หมดเวลาของวันนี้)",
            "outside": "🔴 ล็อกอยู่ (นอกช่วงเวลาที่อนุญาต)",
            "parent": "🔴 ล็อกอยู่ (ผู้ปกครองสั่งล็อก)",
        }[reason]
        return (f"{state}\n"
                f"ใช้ไปแล้ววันนี้: {format_seconds(self.usage['used'])}\n"
                f"เหลือเวลา: {format_seconds(left)}\n"
                f"โควตาวัน{DAY_TH[weekday]}: {self.cfg['daily_minutes'][DAYS[weekday]]} นาที\n"
                f"ช่วงเวลาที่ใช้ได้: {self.cfg['allowed_start']} - {self.cfg['allowed_end']} น.")

    # ---------- สั่งงานจาก Telegram

    def process_remote(self):
        while True:
            try:
                chat_id, message_id, text = self.remote.incoming.get_nowait()
            except queue.Empty:
                return
            if text.strip().lower().startswith("/password"):
                self.remote.delete(chat_id, message_id)  # ไม่ให้รหัสค้างอยู่ในแชต
            reply = self.handle_remote(chat_id, text)
            if reply:
                self.remote.send(chat_id, reply)

    def handle_remote(self, chat_id, text):
        text = BUTTONS.get(text.strip(), text.strip())
        cmd, _, arg = text.partition(" ")
        cmd, arg = cmd.split("@")[0].lower(), arg.strip()

        if cmd == "/pair":
            if self.pair_code and time.time() < self.pair_expires and hmac.compare_digest(arg.encode(), self.pair_code.encode()):
                if chat_id not in self.cfg["telegram_chat_ids"]:
                    self.cfg["telegram_chat_ids"].append(chat_id)
                    write_json(CONFIG_PATH, self.cfg)
                self.pair_code = None
                return f"✅ จับคู่กับเครื่อง {PC_NAME} เรียบร้อย\n\n{HELP_TEXT}"
            return "❌ รหัสจับคู่ไม่ถูกต้องหรือหมดอายุ\nสร้างรหัสใหม่ได้ที่หน้าตั้งค่าของโปรแกรมบนคอม"
        if chat_id not in self.cfg["telegram_chat_ids"]:
            return ("ยังไม่ได้จับคู่กับเครื่องนี้\n"
                    "ที่คอม: ดับเบิลคลิกนาฬิกา → ตั้งค่า → สร้างรหัสจับคู่ แล้วส่ง /pair ตามด้วยรหัสมาที่นี่")

        if cmd in ("/start", "/help"):
            return HELP_TEXT
        if cmd == "/status":
            return self.status_text()
        if cmd == "/add":
            try:
                minutes = int(arg or 30)
                if not 1 <= minutes <= 1440:
                    raise ValueError
            except ValueError:
                return "ใส่จำนวนนาทีเป็นตัวเลข 1-1440 เช่น /add 30"
            self.grant(minutes)
            note = "\n(ยังล็อกอยู่เพราะผู้ปกครองสั่งล็อก ส่ง /unlock เพื่อปลดล็อก)" if self.usage["forced_lock"] else ""
            return f"✅ ให้เล่นต่ออีก {minutes} นาทีแล้ว{note}\n\n{self.status_text()}"
        if cmd == "/lock":
            self.usage["forced_lock"] = True
            save_usage(self.usage)
            return "🔒 ล็อกเครื่องแล้ว ส่ง /unlock เมื่อต้องการปลดล็อก"
        if cmd == "/unlock":
            self.usage["forced_lock"] = False
            save_usage(self.usage)
            return "🔓 ยกเลิกการล็อกแล้ว\n\n" + self.status_text()
        if cmd == "/unlimited":
            self.usage["unlimited"] = True
            save_usage(self.usage)
            return "♾️ ไม่จำกัดเวลาเฉพาะวันนี้แล้ว"
        if cmd == "/reset":
            self.reset_today()
            return "🔄 รีเซ็ตเวลาของวันนี้แล้ว\n\n" + self.status_text()

        reply = self.handle_setting(cmd, arg.split())
        if reply:
            self.warned.clear()
            write_json(CONFIG_PATH, self.cfg)
            return reply
        return "ไม่รู้จักคำสั่งนี้\n\n" + HELP_TEXT

    def settings_text(self):
        cfg = self.cfg
        days = "\n".join(f"  {name}: {cfg['daily_minutes'][d]} นาที" for d, name in zip(DAYS, DAY_TH))
        start, end = cfg["allowed_start"], cfg["allowed_end"]
        idle = f"เกิน {cfg['idle_minutes']} นาที" if cfg["idle_minutes"] else "ไม่หยุด (นับตลอด)"
        return (f"⚙️ การตั้งค่า\nเวลาเล่นต่อวัน\n{days}\n"
                f"ช่วงเวลาที่ใช้ได้: {'ทั้งวัน' if start == end else f'{start} - {end} น.'}\n"
                f"เมื่อหมดเวลา: {ACTIONS.get(cfg['action'], cfg['action'])}\n"
                f"หยุดนับเมื่อไม่แตะเครื่อง: {idle}\n"
                f"รหัสปลดล็อกที่หน้าจอ: {'ตั้งแล้ว' if cfg['password_hash'] else 'ยังไม่ได้ตั้ง (/password 1234)'}")

    def handle_setting(self, cmd, args):
        """คำสั่งตั้งค่าจาก Telegram คืนข้อความตอบกลับ หรือ None ถ้าไม่ใช่คำสั่งตั้งค่า"""
        cfg = self.cfg
        if cmd == "/settings":
            return self.settings_text()
        if cmd == "/limit":
            try:
                days = DAY_ALIASES[args[0].lower()] if len(args) == 2 else DAYS
                minutes = int(args[-1])
                if not 0 <= minutes <= 1440:
                    raise ValueError
            except (KeyError, IndexError, ValueError):
                return "ใช้แบบนี้: /limit all 60 หรือ /limit weekend 180 หรือ /limit sat 120 (0-1440 นาที)"
            for d in days:
                cfg["daily_minutes"][d] = minutes
            return "✅ บันทึกแล้ว\n\n" + self.settings_text()
        if cmd == "/hours":
            if args and args[0].lower() in ("off", "ปิด"):
                args = ["00:00", "00:00"]
            try:
                parse_hm(args[0])
                parse_hm(args[1])
            except (IndexError, ValueError):
                return "ใช้แบบนี้: /hours 07:00 21:00 หรือ /hours off"
            cfg["allowed_start"], cfg["allowed_end"] = args[0], args[1]
            return "✅ บันทึกแล้ว\n\n" + self.settings_text()
        if cmd == "/action":
            if not args or args[0].lower() not in ACTIONS:
                return "ใช้แบบนี้: /action lock หรือ /action logoff หรือ /action shutdown"
            cfg["action"] = args[0].lower()
            return "✅ บันทึกแล้ว\n\n" + self.settings_text()
        if cmd == "/idle":
            try:
                cfg["idle_minutes"] = max(0, int(args[0]))
            except (IndexError, ValueError):
                return "ใช้แบบนี้: /idle 10 (0 = นับเวลาตลอด)"
            return "✅ บันทึกแล้ว\n\n" + self.settings_text()
        if cmd == "/password":
            if len(args) != 1 or len(args[0]) < 4:
                return "ใช้แบบนี้: /password 1234 (อย่างน้อย 4 ตัว ห้ามมีช่องว่าง)"
            set_password(cfg, args[0])
            return "✅ ตั้งรหัสปลดล็อกที่หน้าจอคอมแล้ว (ลบข้อความที่มีรหัสออกจากแชตให้แล้ว)"
        return None

    # ---------- วงรอบหลัก

    def tick(self):
        now = time.monotonic()
        delta, self.last_tick = now - self.last_tick, now

        self.process_remote()

        today = dt.date.today().isoformat()
        if today > self.usage["date"]:
            self.reset_today()

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
            self.usage["last_seen"] = time.time()
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
        elif reason == "parent":
            text = "ผู้ปกครองสั่งล็อกเครื่องไว้\nพักก่อนนะ!"
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
            if reason != "parent":
                self.remote.notify(f"🔒 ล็อกเครื่องแล้ว: {text.splitlines()[0]}\n"
                                   f"ใช้ไปวันนี้ {format_seconds(self.usage['used'])}\n"
                                   "ส่ง /add 30 ถ้าจะให้เล่นต่อ")

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

        hint = ("สำหรับผู้ปกครอง: ใส่รหัสผ่านแล้วเลือกเวลาที่จะให้เล่นต่อ" if self.cfg["password_hash"]
                else "ผู้ปกครองปลดล็อกได้ทาง Telegram (หรือตั้งรหัสปลดล็อกที่หน้าจอด้วย /password)")
        tk.Label(box, text=hint,
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
        self.usage["forced_lock"] = False
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
        if not self.cfg["password_hash"]:
            self.toast("ตั้งค่าผ่าน Telegram ได้เลย\nหรือตั้งรหัสด้วยคำสั่ง /password")
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

        tg = ttk.LabelFrame(frame, text="สั่งงานจากมือถือผ่าน Telegram (ไม่บังคับ)", padding=8)
        tg.grid(row=4, column=0, columnspan=2, sticky="ew", pady=5)
        token_var = tk.StringVar(value=cfg["telegram_token"])
        ttk.Label(tg, text="Bot token").grid(row=0, column=0, sticky="w", **pad)
        ttk.Entry(tg, textvariable=token_var, width=40, show="•").grid(row=0, column=1, columnspan=2, **pad)
        pair_label = ttk.Label(tg, text=f"จับคู่กับมือถือแล้ว {len(cfg['telegram_chat_ids'])} เครื่อง", justify="left")
        pair_label.grid(row=2, column=0, columnspan=3, sticky="w", **pad)
        if first_run:
            ttk.Label(tg, text="จับคู่มือถือได้หลังติดตั้งเสร็จ: ดับเบิลคลิกนาฬิกามุมจอ → ตั้งค่า",
                      foreground="#7f8c8d").grid(row=1, column=0, columnspan=3, sticky="w", **pad)
        else:
            def make_pair_code():
                cfg["telegram_token"] = token_var.get().strip()
                if not cfg["telegram_token"]:
                    pair_label.config(text="กรุณาใส่ Bot token ก่อน")
                    return
                write_json(CONFIG_PATH, cfg)
                self.pair_code = f"{secrets.randbelow(10 ** 6):06d}"
                self.pair_expires = time.time() + 600
                pair_label.config(text=f"ส่งข้อความนี้ไปที่บอทใน Telegram ภายใน 10 นาที:\n/pair {self.pair_code}")

            def unpair_all():
                cfg["telegram_chat_ids"] = []
                write_json(CONFIG_PATH, cfg)
                pair_label.config(text="ยกเลิกการจับคู่ทั้งหมดแล้ว")

            ttk.Button(tg, text="สร้างรหัสจับคู่", command=make_pair_code).grid(row=1, column=1, sticky="w", **pad)
            ttk.Button(tg, text="ยกเลิกการจับคู่ทั้งหมด", command=unpair_all).grid(row=1, column=2, sticky="w", **pad)

        error = ttk.Label(frame, text="", foreground="#c0392b")
        error.grid(row=5, column=0, columnspan=2)

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
            cfg["telegram_token"] = token_var.get().strip()
            write_json(CONFIG_PATH, cfg)
            self.warned.clear()
            close()

        def close():
            w.destroy()
            self.settings_win = None

        buttons = ttk.Frame(frame)
        buttons.grid(row=6, column=0, columnspan=2, pady=(10, 0))
        ttk.Button(buttons, text="บันทึก", command=save).pack(side="left", padx=4)
        if not first_run:
            def reset_today():
                self.reset_today()
                used_label.config(text="วันนี้ใช้ไปแล้ว 0:00:00")

            def quit_app():
                self.remote.notify("⏸️ ผู้ปกครองปิดโปรแกรมชั่วคราวจากหน้าตั้งค่า (จะเปิดกลับมาเองใน 1 นาที)")
                self.usage["last_seen"] = 0
                save_usage(self.usage)
                w.withdraw()
                self.root.after(3000, self.root.destroy)  # รอส่งข้อความแจ้งเตือนให้เสร็จก่อน

            ttk.Button(buttons, text="รีเซ็ตเวลาวันนี้", command=reset_today).pack(side="left", padx=4)
            ttk.Button(buttons, text="ปิดโปรแกรมชั่วคราว", command=quit_app).pack(side="left", padx=4)
            used_label = ttk.Label(frame, text=f"วันนี้ใช้ไปแล้ว {format_seconds(self.usage['used'])}")
            used_label.grid(row=7, column=0, columnspan=2, pady=(8, 0))
        ttk.Button(buttons, text="ยกเลิก", command=close).pack(side="left", padx=4)
        w.protocol("WM_DELETE_WINDOW", close)
        w.focus_force()


class Installer:
    """หน้าติดตั้ง: ผู้ปกครองวาง token ของบอท กดติดตั้ง แล้วกด Start ในแชตบอท เท่านี้ก็เสร็จ"""

    def __init__(self):
        self.root = tk.Tk()
        self.root.title(f"ติดตั้ง {APP_NAME}")
        self.root.resizable(False, False)
        self.cfg = load_config()
        self.remote = None

        f = self.frame = ttk.Frame(self.root, padding=20)
        f.pack()
        ttk.Label(f, text="⏰ ScreenTimeGuard", font=(FONT, 16, "bold")).pack(anchor="w")
        ttk.Label(f, text="จำกัดเวลาเล่นคอมของลูก และสั่งงานจากมือถือผ่าน Telegram",
                  font=(FONT, 10)).pack(anchor="w", pady=(0, 12))
        ttk.Label(f, text="1. ใน Telegram ทักหา @BotFather ส่ง /newbot แล้วตั้งชื่อบอท\n"
                          "2. คัดลอก token ที่ได้ (หน้าตาแบบ 123456789:AAF...) มาวางช่องนี้",
                  font=(FONT, 10), justify="left").pack(anchor="w")
        self.token_var = tk.StringVar(value=self.cfg["telegram_token"])
        ttk.Entry(f, textvariable=self.token_var, width=55).pack(fill="x", pady=8)
        self.admins_var = tk.BooleanVar(value=self.cfg.get("limit_admins", True) if os.path.exists(CONFIG_PATH) else True)
        ttk.Checkbutton(f, variable=self.admins_var,
                        text="จำกัดเวลาบัญชีที่เป็น Administrator ด้วย\n"
                             "(ติ๊กไว้ถ้าบัญชีของลูกเป็น Administrator · เอาติ๊กออกถ้าพ่อแม่ใช้เครื่องนี้ด้วยบัญชีผู้ดูแลแยกต่างหาก)"
                        ).pack(anchor="w", pady=(0, 6))
        self.status = ttk.Label(f, text="", font=(FONT, 11), justify="left", wraplength=460)
        self.status.pack(anchor="w", pady=(4, 8))
        self.buttons = ttk.Frame(f)
        self.buttons.pack(anchor="w")
        ttk.Button(self.buttons, text="ติดตั้ง", command=self.install).pack(side="left", padx=(0, 6))
        ttk.Button(self.buttons, text="ติดตั้งแบบไม่ใช้ Telegram", command=self.install_offline).pack(side="left", padx=6)
        if is_installed():
            ttk.Button(self.buttons, text="ถอนการติดตั้ง", command=self.uninstall).pack(side="left", padx=6)
            self.say("ติดตั้งไว้แล้ว กดติดตั้งอีกครั้งเพื่ออัปเดต (การตั้งค่าเดิมยังอยู่)")

    def say(self, text):
        self.status.config(text=text)
        self.root.update()

    def install(self):
        token = self.token_var.get().strip()
        self.cfg["telegram_token"] = token
        self.remote = TelegramRemote(self.cfg)
        self.say("กำลังตรวจสอบ token...")
        bot = self.remote.get_me()
        if not bot:
            self.remote.stopped = True
            self.say("❌ token ใช้ไม่ได้ หรือเครื่องยังไม่ได้ต่ออินเทอร์เน็ต ลองตรวจดูอีกครั้ง")
            return
        if not self.do_install():
            return
        for child in self.buttons.winfo_children():
            child.config(state="disabled")
        if self.cfg["telegram_chat_ids"]:
            self.finish("✅ อัปเดตเรียบร้อย มือถือที่จับคู่ไว้ยังใช้งานได้เหมือนเดิม")
            return
        self.say(f"3. เปิด Telegram ไปที่บอท @{bot} แล้วกด Start (หรือส่ง /start)\n\nกำลังรอ...")
        self.root.after(500, self.wait_for_parent)

    def wait_for_parent(self):
        try:
            chat_id, _, _ = self.remote.incoming.get_nowait()
        except queue.Empty:
            self.root.after(500, self.wait_for_parent)
            return
        # คนแรกที่ทักบอทระหว่างติดตั้ง = ผู้ปกครอง
        self.cfg["telegram_chat_ids"] = [chat_id]
        write_json(CONFIG_PATH, self.cfg)
        self.remote.stopped = True
        self.remote.send(chat_id, f"✅ เชื่อมต่อกับคอม {socket.gethostname()} เรียบร้อย!\n"
                                  "ตอนนี้เริ่มจำกัดเวลาแล้ว ตั้งค่าทั้งหมดผ่านแชตนี้ได้เลย\n\n"
                                  "แนะนำ: ตั้งรหัสสำหรับปลดล็อกที่หน้าจอคอมด้วย /password 1234\n\n" + HELP_TEXT)
        self.remote.ack()
        self.finish("✅ ติดตั้งเสร็จแล้ว! ดูข้อความต้อนรับในแชตบอทได้เลย")

    def install_offline(self):
        if not self.do_install():
            return
        self.say("ตั้งรหัสผ่านผู้ปกครองในหน้าต่างที่ขึ้นมา...")
        args = ["--setup"] if getattr(sys, "frozen", False) else [os.path.abspath(__file__), "--setup"]
        subprocess.run([sys.executable, *args])
        self.cfg = load_config()
        if not self.cfg["password_hash"]:
            self.say("ยังไม่ได้ตั้งรหัสผ่าน กด 'ติดตั้งแบบไม่ใช้ Telegram' อีกครั้ง")
            return
        self.finish("✅ ติดตั้งเสร็จแล้ว!")

    def do_install(self):
        self.say("กำลังติดตั้ง...")
        self.cfg["limit_admins"] = self.admins_var.get()
        try:
            write_json(CONFIG_PATH, self.cfg)
            install_files()
            write_json(CONFIG_PATH, self.cfg)
        except Exception as exc:
            self.say(f"❌ ติดตั้งไม่สำเร็จ: {exc}")
            return False
        return True

    def finish(self, text):
        start_installed()
        self.say(text + "\nหน้าต่างนี้จะปิดเองใน 5 วินาที")
        self.root.after(5000, self.root.destroy)

    def uninstall(self):
        self.say("กำลังถอนการติดตั้ง...")
        if self.cfg["telegram_chat_ids"] and self.cfg["telegram_token"]:
            remote = TelegramRemote(self.cfg)
            remote.stopped = True
            remote.notify("🗑️ ถอนการติดตั้ง ScreenTimeGuard ออกจากเครื่องนี้แล้ว")
            time.sleep(2)
        uninstall_files()
        self.say("ถอนการติดตั้งเรียบร้อย")
        self.root.after(3000, self.root.destroy)


def main():
    if IS_WINDOWS:
        try:
            ctypes.windll.shcore.SetProcessDpiAwareness(1)
        except (AttributeError, OSError):
            pass
    args = sys.argv[1:]
    frozen = getattr(sys, "frozen", False)
    installed_copy = os.path.normcase(os.path.dirname(os.path.abspath(sys.executable))) == os.path.normcase(INSTALL_DIR)
    if "--install" in args or (frozen and not args and not installed_copy):
        if IS_WINDOWS and not is_elevated():
            relaunch_elevated("--install")
            return
        Installer().root.mainloop()
        return

    setup_only = "--setup" in args
    if not setup_only:
        if not acquire_single_instance():
            return
        if is_admin_account() and not load_config().get("limit_admins"):
            return  # ไม่จำกัดเวลาบัญชีผู้ดูแล (ผู้ปกครอง)
    try:
        app = App(setup_only=setup_only)
    except SystemExit:
        return
    app.root.mainloop()


if __name__ == "__main__":
    main()
