#!/usr/bin/env python3
# -*- coding: utf-8 -*-
u"""ฝังคลังข้อสอบวิชาการสอบบัญชีลงหน้าเว็บ พร้อมตรวจกติกาก่อนฝังทุกครั้ง

    python3 tools/make-quiz.py            ตรวจแล้วฝัง
    python3 tools/make-quiz.py --check    ตรวจอย่างเดียว

กติกาที่สคริปต์บังคับ
  จำนวนข้อต้องครบตามที่ตั้งไว้ และแต่ละข้อมีสี่ตัวเลือกที่ไม่ซ้ำกัน
  ห้ามมีเลขมาตรฐานในโจทย์หรือตัวเลือก เพราะข้อสอบชุดนี้วัดความเข้าใจ ไม่ใช่การท่องเลข
  ห้ามอ้างถึงสไลด์ เพราะโจทย์ต้องยืนได้ด้วยตัวเองโดยไม่ต้องเปิดเอกสารต้นทาง
  ทุกข้อต้องมีคำอธิบาย และต้องมีทั้งข้อภาษาไทยและภาษาอังกฤษในทุกหมวด
"""

import argparse
import importlib.util
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PAGE = os.path.join(ROOT, 'audit', 'index.html')
WANT = 120

SOURCES = ['audit-quiz-1.py', 'audit-quiz-2.py']

# ชื่อหมวดที่ใช้เป็นปุ่มกรองในหน้าเว็บ เรียงตามลำดับที่อยากให้แสดง
CATS = [
    ('as', u'ข้อกำหนดของผู้บริหาร'),
    ('wy', u'ทำไมต้องมีการสอบบัญชี'),
    ('ga', u'หลักการสามกลุ่ม'),
    ('ev', u'หลักฐานการสอบบัญชี'),
    ('rp', u'การรายงานและคุณภาพงาน'),
    ('ac', u'การตอบรับงาน'),
    ('ma', u'ความมีสาระสำคัญ'),
    ('pr', u'วิธีการตรวจสอบ'),
    ('dc', u'เอกสารหลักฐาน'),
    ('rk', u'แบบจำลองความเสี่ยง'),
    ('fr', u'การทุจริต'),
    ('ai', u'งานให้ความเชื่อมั่น'),
    ('et', u'จรรยาบรรณ'),
    ('sa', u'การเลือกตัวอย่าง'),
]

# เลขมาตรฐานมักมาในรูปตัวย่อพิมพ์ใหญ่ตามด้วยตัวเลข หรือคำว่ากฎหรือภาคผนวกตามด้วยเลขข้อ
STD_NUM = re.compile(r'\b[A-Z][A-Za-z\-]{1,6}\s?\d{3,4}\b|\bRule\s*\d|\bExhibit\s*[A-Z]', re.U)
SLIDE = re.compile(u'สไลด์|เอกสารประกอบการสอน|ในบทเรียน')
BLOCK_RE = re.compile(r'\n*<script type="application/json" id="qz-data">.*?</script>', re.S)

# ต้องวางก่อนแท็ก script ตัวแรก ไม่ใช่ท้ายไฟล์
# เพราะสคริปต์ในเนื้อหน้าทำงานทันทีที่ถูกอ่านเจอ ถ้าข้อมูลอยู่หลังมัน
# getElementById จะคืนค่าว่างและแบบทดสอบจะไม่ขึ้นเลย
ANCHOR = '</footer>\n'


def load():
    out = []
    for name in SOURCES:
        path = os.path.join(HERE, name)
        spec = importlib.util.spec_from_file_location(name.replace('-', '_')[:-3], path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        out.extend(mod.Q)
    return out


def check(rows):
    bad = 0
    cats = dict(CATS)

    def fail(i, msg):
        nonlocal bad
        bad += 1
        print(u'  ข้อ %-3d %s' % (i + 1, msg))

    seen = {}
    for i, row in enumerate(rows):
        if len(row) != 5:
            fail(i, u'โครงสร้างไม่ครบห้าช่อง')
            continue
        cat, lang, q, opts, exp = row
        if cat not in cats:
            fail(i, u'หมวด %s ไม่อยู่ในรายการ' % cat)
        if lang not in ('th', 'en'):
            fail(i, u'ภาษา %s ไม่ถูกต้อง' % lang)
        if len(opts) != 4:
            fail(i, u'มี %d ตัวเลือก ต้องเป็น 4' % len(opts))
        if len(set(opts)) != len(opts):
            fail(i, u'ตัวเลือกซ้ำกัน')
        if not exp.strip():
            fail(i, u'ไม่มีคำอธิบาย')
        if q.strip() in seen:
            fail(i, u'โจทย์ซ้ำกับข้อ %d' % (seen[q.strip()] + 1))
        seen[q.strip()] = i

        # เลขมาตรฐานและการอ้างถึงสไลด์ ห้ามอยู่ในโจทย์หรือตัวเลือก
        for text in [q] + list(opts):
            m = STD_NUM.search(text)
            if m:
                fail(i, u'มีเลขมาตรฐาน %s อยู่ในโจทย์หรือตัวเลือก' % m.group(0))
            if SLIDE.search(text):
                fail(i, u'โจทย์อ้างถึงสไลด์ ซึ่งต้องยืนได้ด้วยตัวเอง')
        if SLIDE.search(exp):
            fail(i, u'คำอธิบายอ้างถึงสไลด์')

    print('')
    n_th = sum(1 for r in rows if r[1] == 'th')
    for key, label in CATS:
        rs = [r for r in rows if r[0] == key]
        th = sum(1 for r in rs if r[1] == 'th')
        if not rs:
            print(u'%-4s %-28s ไม่มีข้อเลย' % (key, label))
            bad += 1
            continue
        if th == 0 or th == len(rs):
            print(u'%-4s %-28s %2d ข้อ · มีภาษาเดียว ควรมีทั้งสองภาษา' % (key, label, len(rs)))
            bad += 1
        else:
            print(u'%-4s %-28s %2d ข้อ · ไทย %2d · อังกฤษ %2d'
                  % (key, label, len(rs), th, len(rs) - th))

    print(u'\nรวม %d ข้อ · ไทย %d ข้อ · อังกฤษ %d ข้อ' % (len(rows), n_th, len(rows) - n_th))
    if len(rows) != WANT:
        print(u'ต้องการ %d ข้อ แต่มี %d ข้อ' % (WANT, len(rows)))
        bad += 1
    print(u'ตรวจพบปัญหา %d จุด' % bad)
    return bad


def write(rows):
    data = {
        'cats': [{'k': k, 'n': n} for k, n in CATS],
        'qs': [{'c': c, 'l': l, 'q': q, 'o': list(o), 'e': e} for c, l, q, o, e in rows],
    }
    html = io.open(PAGE, encoding='utf-8').read()
    block = ('\n\n<script type="application/json" id="qz-data">\n' +
             json.dumps(data, ensure_ascii=False, separators=(',', ':')) + '\n</script>')
    html = BLOCK_RE.sub('', html)
    at = html.find(ANCHOR)
    if at < 0:
        print(u'หาจุดวางบล็อกในหน้าไม่เจอ')
        return 1
    at += len(ANCHOR)
    html = html[:at] + block.lstrip('\n') + '\n' + html[at:]
    io.open(PAGE, 'w', encoding='utf-8').write(html.rstrip('\n') + '\n')
    print(u'\nฝังบล็อก qz-data ลง audit/index.html แล้ว · %.1f KB' % (len(block) / 1024.0))


def main():
    ap = argparse.ArgumentParser(description=u'ฝังคลังข้อสอบวิชาการสอบบัญชี')
    ap.add_argument('--check', action='store_true', help=u'ตรวจอย่างเดียว ไม่เขียนไฟล์')
    a = ap.parse_args()

    rows = load()
    if check(rows):
        print(u'\nยังไม่ฝังให้ เพราะต้องแก้ข้อมูลก่อน')
        return 1
    if not a.check:
        write(rows)
    return 0


if __name__ == '__main__':
    sys.exit(main())
