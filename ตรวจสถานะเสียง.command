#!/bin/bash
# ---------------------------------------------------------------
# ดับเบิลคลิกเพื่อดูว่าบทไหนยังไม่มีไฟล์เสียง โดยไม่สร้างอะไรจริง
# ไม่ต้องพิมพ์คำสั่งใด ๆ
# ---------------------------------------------------------------

cd "$(dirname "$0")" || exit 1

echo ""
echo "  ┌────────────────────────────────────────────┐"
echo "  │   ตรวจสถานะไฟล์เสียง · ไม่สร้างอะไรจริง     │"
echo "  └────────────────────────────────────────────┘"
echo ""

if [ ! -f "tools/make-audio.py" ]; then
  echo "  ไม่พบไฟล์ tools/make-audio.py ในโฟลเดอร์นี้"
  echo "  ให้รัน  git pull origin claude/educational-media-c9pinv  ก่อน"
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
  echo "  ไม่พบ Python 3 ในเครื่อง ติดตั้งได้จาก https://www.python.org/downloads/"
  echo ""
  echo "  กด Enter เพื่อปิดหน้าต่าง"
  read -r _
  exit 1
fi

"$PY" tools/make-audio.py --check

echo ""
echo "  ถ้ามีบทที่ยังขาด ให้ปิดหน้าต่างนี้แล้วดับเบิลคลิก  สร้างไฟล์เสียง.command"
echo ""
echo "  กด Enter เพื่อปิดหน้าต่าง"
read -r _
