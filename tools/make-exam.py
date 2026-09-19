#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ย้ายข้อสอบ Part I และ Part II จาก tools/exam-data.py เข้าไปในหน้าเว็บ

เก็บโจทย์ไว้เป็นไฟล์ Python เพราะแก้ง่ายกว่าการไปนั่งแก้ JSON ยาว ๆ ในหน้า HTML
แล้วให้สคริปต์นี้แปลงเป็นบล็อก JSON id="mx-data" ฝังกลับเข้า oral-eng/index.html

    python3 tools/make-exam.py

ใช้ --check เพื่อดูว่าข้อมูลครบถ้วนไหม โดยไม่แตะไฟล์
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
PAGE = os.path.join(ROOT, 'oral-eng', 'index.html')

_spec = importlib.util.spec_from_file_location('exam_data', os.path.join(HERE, 'exam-data.py'))
_ed = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_ed)

_lspec = importlib.util.spec_from_file_location('ldata', os.path.join(HERE, 'listening-data.py'))
_ld = importlib.util.module_from_spec(_lspec)
_lspec.loader.exec_module(_ld)

BLOCK_RE = re.compile(r'\n*<script type="application/json" id="mx-data">.*?</script>', re.S)
ANCHOR = '\n<script type="application/json" id="vc-data">'


def build():
    """รวมสี่ส่วนเข้าเป็นชุดละก้อน ให้ตรงกับชุดของ Part III ที่มีอยู่แล้ว"""
    sets = []
    for i, st in enumerate(_ld.SETS):
        sets.append({
            'id': st['id'],
            'title': st['title'],
            'p1a': {'box': _ed.P1A[i]['box'],
                    'items': [list(x) for x in _ed.P1A[i]['items']]},
            'p1b': {'box': _ed.P1B[i]['box'],
                    'items': [list(x) for x in _ed.P1B[i]['items']]},
            'p2a': [list(x) for x in _ed.P2A[i]],
            'p2b': [[s, list(o), e] for s, o, e in _ed.P2B[i]],
        })
    return sets


def check(sets):
    """ตรวจให้แน่ใจก่อนฝังว่าทุกข้อใช้ได้จริง ไม่ใช่ไปเจอตอนเปิดหน้าเว็บ"""
    bad = 0

    def fail(msg):
        nonlocal bad
        bad += 1
        print(u'  ผิด · %s' % msg)

    for s in sets:
        print(u'%s' % s['title'])
        for key in ('p1a', 'p1b'):
            part = s[key]
            if len(part['box']) < len(part['items']):
                fail(u'%s %s กล่องคำมีน้อยกว่าจำนวนข้อ' % (s['id'], key))
            # หน้าเว็บทำดัชนีกล่องคำด้วยตัวพิมพ์เล็ก วลีซ้ำจะทำให้ขีดฆ่าผิดตัว
            low = [b.lower() for b in part['box']]
            if len(set(low)) != len(low):
                fail(u'%s %s กล่องคำมีวลีซ้ำกัน' % (s['id'], key))
            if len(set(a.lower() for _, a, _ in part['items'])) != len(part['items']):
                fail(u'%s %s คำตอบซ้ำกันภายในชุดเดียว' % (s['id'], key))
            for sent, ans, exp in part['items']:
                if u'…' not in sent:
                    fail(u'%s %s ไม่มีช่องว่าง · %s' % (s['id'], key, sent[:40]))
                # เทียบแบบไม่สนตัวพิมพ์ เพราะคำตอบต้นประโยคขึ้นต้นด้วยตัวใหญ่
                if ans.lower() not in [b.lower() for b in part['box']]:
                    fail(u'%s %s คำตอบ %s ไม่อยู่ในกล่องคำ' % (s['id'], key, ans))
                if not exp.strip():
                    fail(u'%s %s ไม่มีคำอธิบาย' % (s['id'], key))
        for phrase, ok, fix, exp in s['p2a']:
            if not ok and not fix.strip():
                fail(u'%s p2a ข้อผิดแต่ไม่ได้ให้รูปที่ถูก · %s' % (s['id'], phrase))
            if ok and fix.strip():
                fail(u'%s p2a ข้อถูกแต่ดันมีรูปแก้มาด้วย · %s' % (s['id'], phrase))
            if not exp.strip():
                fail(u'%s p2a ไม่มีคำอธิบาย' % s['id'])
        for sent, opts, exp in s['p2b']:
            if len(opts) != 4:
                fail(u'%s p2b มี %d ตัวเลือก ต้องเป็น 4' % (s['id'], len(opts)))
            if len(set(opts)) != len(opts):
                fail(u'%s p2b ตัวเลือกซ้ำกัน · %s' % (s['id'], sent[:40]))
            if u'…' not in sent:
                fail(u'%s p2b ไม่มีช่องว่าง · %s' % (s['id'], sent[:40]))
            if not exp.strip():
                fail(u'%s p2b ไม่มีคำอธิบาย' % s['id'])
        n = len(s['p1a']['items']) + len(s['p1b']['items']) + len(s['p2a']) + len(s['p2b'])
        print(u'  Part I %d + %d ข้อ · Part II %d + %d ข้อ · รวม %d คะแนน'
              % (len(s['p1a']['items']), len(s['p1b']['items']),
                 len(s['p2a']), len(s['p2b']), n))
        if n != 20:
            fail(u'%s รวมได้ %d ข้อ ต้องเป็น 20' % (s['id'], n))

    # ถ้าทุกชุดมีข้อถูกเท่ากันหมด เดาว่า "เรียงถูกแล้ว" ทุกข้อก็ได้คะแนนฟรีเท่าเดิมทุกชุด
    balance = [sum(1 for x in s['p2a'] if x[1]) for s in sets]
    print(u'\nPart II A · จำนวนข้อที่เรียงถูกในแต่ละชุด %s'
          % ' '.join(str(b) for b in balance))
    if len(set(balance)) == 1:
        fail(u'ทุกชุดมีข้อถูกเท่ากันหมด ควรกระจายให้เดาไม่ได้')

    total = sum(len(s['p1a']['items']) + len(s['p1b']['items']) +
                len(s['p2a']) + len(s['p2b']) for s in sets)
    print(u'\nรวม %d ชุด %d ข้อ · ข้อละ 1 คะแนน · ตรวจพบปัญหา %d จุด'
          % (len(sets), total, bad))
    return bad


def write(sets):
    html = io.open(PAGE, encoding='utf-8').read()
    block = ('\n\n<script type="application/json" id="mx-data">\n' +
             json.dumps(sets, ensure_ascii=False, separators=(',', ':')) + '\n</script>')
    html = BLOCK_RE.sub('', html).rstrip('\n')
    at = html.find(ANCHOR)
    html = (html[:at] + block + html[at:]) if at > 0 else (html + block + '\n')
    io.open(PAGE, 'w', encoding='utf-8').write(html.rstrip('\n') + '\n')
    print(u'\nฝังบล็อก mx-data ลง oral-eng/index.html แล้ว · %.1f KB'
          % (len(block) / 1024.0))


def main():
    ap = argparse.ArgumentParser(description=u'ฝังข้อสอบ Part I และ Part II ลงหน้าเว็บ')
    ap.add_argument('--check', action='store_true', help=u'ตรวจอย่างเดียว ไม่เขียนไฟล์')
    a = ap.parse_args()

    sets = build()
    bad = check(sets)
    if bad:
        print(u'\nยังไม่ฝังให้ เพราะต้องแก้ข้อมูลก่อน')
        return 1
    if not a.check:
        write(sets)
    return 0


if __name__ == '__main__':
    sys.exit(main())
