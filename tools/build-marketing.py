#!/usr/bin/env python3
# -*- coding: utf-8 -*-
u"""สร้างเนื้อหาหลังมิดเทอมของหน้าหลักการตลาดทั้งหมดตามลำดับที่ถูกต้อง

    python3 tools/build-marketing.py            สร้างใหม่ทั้งชุด
    python3 tools/build-marketing.py --check    ตรวจอย่างเดียว ไม่เขียนไฟล์

ลำดับสำคัญ เพราะ mk-ch911.py ยึดจุดแทรกกับคอมเมนต์คร่อมที่ mk-postmid.py วางไว้
และข้อสอบของบทที่ 9 ถึง 11 ถูกเติมเข้าไปในคลังที่ mk-postmid.py เขียนทับทั้งก้อน
ถ้ารัน mk-postmid.py ทับของที่มีอยู่ คลังข้อสอบจะขาดจุลภาคคั่นแล้วสคริปต์ทั้งหน้าพัง
mk-postmid.py จึงปฏิเสธการรันตัวเดียวเมื่อเห็นว่าหน้ามีบทเหล่านั้นอยู่แล้ว

ชุดนี้จึงเริ่มด้วยการลบบทที่ 9 ถึง 11 ออกก่อน ให้หน้ากลับไปมีแค่ถึงบทที่ 8
แล้วจึงรัน mk-postmid.py และ mk-ch911.py ตามลำดับ ผลที่ได้จึงเหมือนกันทุกครั้ง
ไม่ว่าหน้าจะอยู่ในสภาพใดก่อนรัน

โหมด --check ไม่เขียนไฟล์ จึงลบของเดิมออกไม่ได้ และรันทั้งชุดไม่ได้
โหมดนี้จึงตรวจเฉพาะ mk-ch911.py กับหน้าที่มีอยู่ตอนนี้ และบอกตรง ๆ ว่าตรวจแค่นั้น
"""

import argparse
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

STEPS = (
    ('mk-ch911.py', (u'--strip',), u'ลบบทที่ 9 ถึง 11 ออกก่อน'),
    ('mk-postmid.py', (u'--alone',), u'บทที่ 8 · สินค้าใหม่และวงจรชีวิต'),
    ('mk-ch911.py', (), u'บทที่ 9 ถึง 11 · ราคา ช่องทาง ค้าปลีกค้าส่ง'),
)


def run(script, extra, title):
    print(u'\n── %s · %s ──' % (script, title))
    cmd = [sys.executable, os.path.join(HERE, script)]
    cmd.extend(extra)
    return subprocess.run(cmd).returncode


def main():
    ap = argparse.ArgumentParser(description=u'สร้างเนื้อหาหลังมิดเทอมของหลักการตลาด')
    ap.add_argument('--check', action='store_true', help=u'ตรวจอย่างเดียว ไม่เขียนไฟล์')
    a = ap.parse_args()

    if a.check:
        print(u'โหมดตรวจ · ตรวจเฉพาะ mk-ch911.py กับหน้าที่มีอยู่ตอนนี้')
        print(u'ตรวจทั้งชุดไม่ได้ เพราะแต่ละตัวต้องอ่านผลที่ตัวก่อนหน้าเขียนลงไฟล์')
        return run('mk-ch911.py', (u'--check',), u'ตรวจบทที่ 9 ถึง 11')

    for script, extra, title in STEPS:
        rc = run(script, extra, title)
        if rc:
            print(u'\n%s ล้มเหลว จึงหยุดทั้งชุด' % script)
            return rc
    print(u'\nเสร็จทั้งชุด')
    return 0


if __name__ == '__main__':
    sys.exit(main())
