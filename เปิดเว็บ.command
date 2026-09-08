#!/bin/bash
# ---------------------------------------------------------------
# ดับเบิลคลิกไฟล์นี้ใน Finder เพื่อเปิดเว็บผ่าน http://localhost
# จำเป็นเพราะการเปิดไฟล์แบบ file:// ทำให้ Safari ไม่ยอมโหลดไฟล์เสียง
# ---------------------------------------------------------------

cd "$(dirname "$0")" || exit 1

PORT=8765

echo ""
echo "  ┌────────────────────────────────────────────┐"
echo "  │   เปิดเว็บสื่อการสอน · ผ่าน localhost       │"
echo "  └────────────────────────────────────────────┘"
echo ""
echo "  โฟลเดอร์  $(pwd)"

if [ ! -f "index.html" ]; then
  echo ""
  echo "  ไม่พบ index.html ในโฟลเดอร์นี้"
  echo "  ไฟล์นี้ต้องอยู่ในโฟลเดอร์โปรเจกต์ Classroom1 เท่านั้น"
  echo ""
  echo "  กด Enter เพื่อปิดหน้าต่าง"
  read -r _
  exit 1
fi

PY=""
for c in python3 /usr/bin/python3 /opt/homebrew/bin/python3 /usr/local/bin/python3 python; do
  if command -v "$c" >/dev/null 2>&1 && "$c" -c 'import sys; sys.exit(0 if sys.version_info >= (3, 8) else 1)' 2>/dev/null; then
    PY="$c"
    break
  fi
done

if [ -z "$PY" ]; then
  echo ""
  echo "  ไม่พบ Python 3 ในเครื่อง ติดตั้งได้จาก https://www.python.org/downloads/"
  echo ""
  echo "  กด Enter เพื่อปิดหน้าต่าง"
  read -r _
  exit 1
fi

# ถ้าพอร์ตนี้ถูกใช้อยู่แล้ว ให้ขยับไปพอร์ตว่างถัดไป
while "$PY" - "$PORT" <<'EOF' 2>/dev/null
import socket, sys
s = socket.socket()
try:
    s.bind(('127.0.0.1', int(sys.argv[1])))
except OSError:
    sys.exit(0)     # พอร์ตไม่ว่าง
finally:
    s.close()
sys.exit(1)         # พอร์ตว่าง
EOF
do
  PORT=$((PORT + 1))
  if [ "$PORT" -gt 8800 ]; then
    echo "  หาพอร์ตว่างไม่ได้ ลองปิดหน้าต่าง Terminal เก่าที่ยังเปิดเว็บอยู่ก่อน"
    read -r _
    exit 1
  fi
done

URL="http://localhost:$PORT/"
echo "  ที่อยู่    $URL"
echo ""
echo "  กำลังเปิดเบราว์เซอร์ให้..."
echo "  อย่าปิดหน้าต่างนี้ระหว่างใช้งาน ถ้าปิดแล้วเว็บจะเข้าไม่ได้"
echo "  ใช้เสร็จแล้วกด Control + C เพื่อหยุด"
echo ""

# รอให้เซิร์ฟเวอร์พร้อมก่อนแล้วค่อยเปิดเบราว์เซอร์
( sleep 1; command -v open >/dev/null 2>&1 && open "$URL" ) &

"$PY" -m http.server "$PORT" --bind 127.0.0.1

echo ""
echo "  หยุดเรียบร้อย กด Enter เพื่อปิดหน้าต่าง"
read -r _
