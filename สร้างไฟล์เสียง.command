#!/bin/bash
# ---------------------------------------------------------------
# ดับเบิลคลิกไฟล์นี้ใน Finder เพื่อสร้างไฟล์เสียงบรรยายเสียงผู้ชาย
# ไม่ต้องเปิด Terminal เอง ไม่ต้อง cd ไปไหน
# ---------------------------------------------------------------

# ย้ายไปยังโฟลเดอร์ที่ไฟล์นี้อยู่ ซึ่งก็คือโฟลเดอร์โปรเจกต์เสมอ
cd "$(dirname "$0")" || exit 1

echo ""
echo "  ┌────────────────────────────────────────────┐"
echo "  │   สร้างไฟล์เสียงบรรยาย · เสียงผู้ชาย Niwat   │"
echo "  └────────────────────────────────────────────┘"
echo ""
echo "  โฟลเดอร์  $(pwd)"

if [ ! -f "tools/make-audio.py" ]; then
  echo ""
  echo "  ไม่พบไฟล์ tools/make-audio.py ในโฟลเดอร์นี้"
  echo "  แปลว่ายังไม่ได้ดึงโค้ดรุ่นล่าสุดมา ให้รันคำสั่งนี้ก่อน"
  echo ""
  echo "      git pull origin claude/educational-media-c9pinv"
  echo ""
  echo "  กด Enter เพื่อปิดหน้าต่าง"
  read -r _
  exit 1
fi

# หา Python ที่ใช้ได้ ไล่จากตัวที่พบบ่อยที่สุดบน macOS
PY=""
for c in python3 /usr/bin/python3 /opt/homebrew/bin/python3 /usr/local/bin/python3 python; do
  if command -v "$c" >/dev/null 2>&1 && "$c" -c 'import sys; sys.exit(0 if sys.version_info >= (3, 8) else 1)' 2>/dev/null; then
    PY="$c"
    break
  fi
done

if [ -z "$PY" ]; then
  echo ""
  echo "  ไม่พบ Python 3 ในเครื่อง"
  echo "  ติดตั้งได้จาก https://www.python.org/downloads/ แล้วดับเบิลคลิกไฟล์นี้ใหม่"
  echo ""
  echo "  กด Enter เพื่อปิดหน้าต่าง"
  read -r _
  exit 1
fi

echo "  Python    $("$PY" -c 'import sys; print(sys.executable)')"
echo ""

# ติดตั้ง edge-tts ให้ Python ตัวเดียวกับที่จะใช้รัน กันปัญหา pip คนละตัว
if ! "$PY" -c 'import edge_tts' 2>/dev/null; then
  echo "  ยังไม่มี edge-tts กำลังติดตั้งให้ รอสักครู่..."
  echo ""
  "$PY" -m pip install --quiet --upgrade edge-tts 2>/dev/null ||
    "$PY" -m pip install --quiet --user --upgrade edge-tts ||
    "$PY" -m pip install --quiet --user --break-system-packages --upgrade edge-tts
  if ! "$PY" -c 'import edge_tts' 2>/dev/null; then
    echo ""
    echo "  ติดตั้ง edge-tts ไม่สำเร็จ ลองรันคำสั่งนี้ใน Terminal ด้วยตัวเองดูครับ"
    echo ""
    echo "      \"$PY\" -m pip install --user edge-tts"
    echo ""
    echo "  กด Enter เพื่อปิดหน้าต่าง"
    read -r _
    exit 1
  fi
  echo "  ติดตั้ง edge-tts เรียบร้อย"
  echo ""
fi

# โหมดตรวจสถานะไม่ได้สร้างไฟล์อะไร จึงไม่ต้องขึ้นข้อความรอยาว
CHECK_ONLY=0
for a in "$@"; do
  if [ "$a" = "--check" ]; then CHECK_ONLY=1; fi
done

if [ $CHECK_ONLY -eq 0 ]; then
  echo "  เริ่มสร้างไฟล์เสียง ใช้เวลาราว 15 ถึง 25 นาที"
  echo "  ปล่อยหน้าต่างนี้ไว้ได้เลย ไม่ต้องทำอะไรต่อ"
  echo ""
fi

"$PY" tools/make-audio.py "$@"
STATUS=$?

echo ""
if [ $CHECK_ONLY -eq 1 ]; then
  : # โหมดตรวจสถานะพิมพ์ผลของตัวเองไปแล้ว
elif [ $STATUS -eq 0 ]; then
  echo "  เสร็จเรียบร้อย เปิดหน้าเว็บวิชาไหนก็ได้แล้วกดปุ่ม ฟังสรุปบท"
  echo "  ถ้าหน้าเว็บเปิดค้างอยู่ ให้กดรีเฟรชหนึ่งครั้ง"
  echo ""
  echo "  อย่าลืมเก็บไฟล์เสียงเข้า git ด้วย"
  echo "      git add -A && git commit -m \"เพิ่มไฟล์เสียงบรรยาย\""
else
  echo "  ทำไม่สำเร็จ ดูข้อความด้านบนว่าติดตรงไหน"
  echo "  ถ้าเป็นเรื่องเน็ต ให้ดับเบิลคลิกไฟล์นี้ใหม่ ระบบจะทำต่อจากบทที่ค้างไว้เอง"
fi

echo ""
echo "  กด Enter เพื่อปิดหน้าต่าง"
read -r _
