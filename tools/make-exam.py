#!/usr/bin/env python3
# -*- coding: utf-8 -*-
u"""ย้ายข้อสอบ Part I และ Part II จาก tools/exam-data*.py เข้าไปในหน้าเว็บ

เก็บโจทย์ไว้เป็นไฟล์ Python เพราะแก้ง่ายกว่าการไปนั่งแก้ JSON ยาว ๆ ในหน้า HTML
แล้วให้สคริปต์นี้แปลงเป็นบล็อก JSON id="mx-data" ฝังกลับเข้า oral-eng/index.html

    python3 tools/make-exam.py

ใช้ --check เพื่อดูว่าข้อมูลครบถ้วนไหม โดยไม่แตะไฟล์

ชุดที่ 1 ถึง 5 อยู่ใน exam-data.py และมี Part III เป็นไฟล์เสียงให้ทำต่อ
จึงใช้รหัสชุดเดียวกับแท็บฝึกฟัง เพื่อให้ปุ่มข้ามไป Part III ยังชี้ถูกที่
ชุดที่ 6 เป็นต้นไปอยู่ใน exam-data-2.py เป็นแบบฝึกล้วน ไม่มี Part III
สคริปต์จึงติดธง p3 ไว้ให้หน้าเว็บรู้ว่าชุดไหนควรมีปุ่มข้ามไปฝึกฟัง
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

SOURCES = ['exam-data.py', 'exam-data-2.py']


def _load(name):
    path = os.path.join(HERE, name)
    spec = importlib.util.spec_from_file_location(name[:-3].replace('-', '_'), path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ต่อชุดจากทุกไฟล์เข้าด้วยกันตามลำดับ ชุดที่ 1 ถึง 5 มาจากไฟล์แรกเสมอ
_MODS = [_load(n) for n in SOURCES]
P1A = [s for m in _MODS for s in m.P1A]
P1B = [s for m in _MODS for s in m.P1B]
P2A = [s for m in _MODS for s in m.P2A]
P2B = [s for m in _MODS for s in m.P2B]

_ld = _load('listening-data.py')

BLOCK_RE = re.compile(r'\n*<script type="application/json" id="mx-data">.*?</script>', re.S)
ANCHOR = '\n<script type="application/json" id="vc-data">'


def build():
    """รวมสี่ส่วนเข้าเป็นชุดละก้อน

    ชุดแรก ๆ ยืมรหัสกับชื่อมาจากแท็บฝึกฟัง เพราะเป็นชุดเดียวกันกับ Part III
    ที่เหลือเป็นแบบฝึกล้วน ตั้งรหัสของตัวเองว่า X6 เป็นต้นไป
    ให้ไม่ชนกับรหัสของคลิปเสียงไม่ว่าจะเพิ่มคลิปอีกกี่ชุด
    """
    n = len(P1A)
    if not (len(P1B) == len(P2A) == len(P2B) == n):
        raise SystemExit(u'จำนวนชุดในสี่ส่วนไม่เท่ากัน · P1A %d · P1B %d · P2A %d · P2B %d'
                         % (n, len(P1B), len(P2A), len(P2B)))

    sets = []
    for i in range(n):
        st = _ld.SETS[i] if i < len(_ld.SETS) else None
        sets.append({
            'id': st['id'] if st else 'X%d' % (i + 1),
            'title': st['title'] if st else u'ชุดที่ %d' % (i + 1),
            'p3': bool(st),
            'p1a': {'box': P1A[i]['box'],
                    'items': [list(x) for x in P1A[i]['items']]},
            'p1b': {'box': P1B[i]['box'],
                    'items': [list(x) for x in P1B[i]['items']]},
            'p2a': [list(x) for x in P2A[i]],
            'p2b': [[s, list(o), e] for s, o, e in P2B[i]],
        })
    return sets


def check(sets):
    """ตรวจให้แน่ใจก่อนฝังว่าทุกข้อใช้ได้จริง ไม่ใช่ไปเจอตอนเปิดหน้าเว็บ"""
    bad = 0

    def fail(msg):
        nonlocal bad
        bad += 1
        print(u'  ผิด · %s' % msg)

    # ข้อสอบภาษาไม่ควรวัดว่าจำกรณีศึกษาจริงได้ไหม ทุกสถานการณ์จึงต้องสมมติขึ้น
    real = re.compile(r'Kraft|Cadbury|Disney|Pixar|Nestl|Toyota|Panasonic|Vodafone|'
                      r'Mannesmann|L’Or|Bank of England|Unilever|Tesco')

    for s in sets:
        print(u'%s' % s['title'])
        texts = ([x[0] for x in s['p1a']['items']] + [x[0] for x in s['p1b']['items']] +
                 [x[0] for x in s['p2a']] + [x[0] for x in s['p2b']])
        for t in texts:
            m = real.search(t)
            if m:
                fail(u'%s มีชื่อกิจการจริง %s อยู่ในโจทย์ · %s' % (s['id'], m.group(0), t[:50]))
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

    # รหัสชุดซ้ำจะทำให้ลิงก์ในแถบข้างและ querySelector ชี้ไปผิดชุด
    ids = [s['id'] for s in sets]
    if len(set(ids)) != len(ids):
        fail(u'รหัสชุดซ้ำกัน · %s' % ' '.join(ids))

    # โจทย์ซ้ำข้ามชุดทำให้แบบฝึกชุดหลังไม่ได้วัดอะไรใหม่ ต้องจับตั้งแต่ตอนนี้
    seen = {}
    for s in sets:
        for t in ([x[0] for x in s['p1a']['items']] + [x[0] for x in s['p1b']['items']] +
                  [x[0] for x in s['p2a']] + [x[0] for x in s['p2b']]):
            k = t.strip().lower()
            if k in seen:
                fail(u'โจทย์ซ้ำระหว่างชุด %s กับ %s · %s' % (seen[k], s['id'], t[:46]))
            seen[k] = s['id']

    # ถ้าทุกชุดมีข้อถูกเท่ากันหมด เดาว่า "เรียงถูกแล้ว" ทุกข้อก็ได้คะแนนฟรีเท่าเดิมทุกชุด
    balance = [sum(1 for x in s['p2a'] if x[1]) for s in sets]
    print(u'\nPart II A · จำนวนข้อที่เรียงถูกในแต่ละชุด %s'
          % ' '.join(str(b) for b in balance))
    if len(set(balance)) < 3:
        fail(u'จำนวนข้อที่เรียงถูกกระจายน้อยเกินไป เดาทางได้ง่าย')

    withp3 = sum(1 for s in sets if s['p3'])
    total = sum(len(s['p1a']['items']) + len(s['p1b']['items']) +
                len(s['p2a']) + len(s['p2b']) for s in sets)
    print(u'\nรวม %d ชุด %d ข้อ · ข้อละ 1 คะแนน · มี Part III ต่อให้ %d ชุด'
          % (len(sets), total, withp3))
    print(u'ตรวจพบปัญหา %d จุด' % bad)
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
    return verify(sets)


def verify(sets):
    u"""อ่านหน้าเว็บกลับมาตรวจว่าตรงกับไฟล์ต้นทางจริง และอยู่ก่อนสคริปต์ที่อ่านมัน

    เคยมีกรณีที่เครื่องมือเขียนกลับไม่ครบแล้วไม่มีอะไรจับได้ หน้าเว็บจึงยังโชว์ของเก่า
    และถ้าบล็อกไปอยู่หลังสคริปต์ getElementById จะคืนค่าว่าง แท็บจะขึ้นเปล่า
    """
    html = io.open(PAGE, encoding='utf-8').read()
    at_data = html.find('id="mx-data"')
    at_script = html.find('\n<script>\n')
    if at_data < 0 or at_script < 0 or at_data > at_script:
        print(u'  บล็อกข้อสอบอยู่หลังสคริปต์ที่อ่านมัน แท็บจะขึ้นว่างเปล่า')
        return 1
    m = BLOCK_RE.search(html)
    got = json.loads(re.search(r'>(.*?)</script>', m.group(0), re.S).group(1)) if m else []
    bad = 0
    if len(got) != len(sets):
        print(u'  หน้าเว็บมี %d ชุด แต่ไฟล์ต้นทางมี %d ชุด' % (len(got), len(sets)))
        bad += 1
    for a, b in zip(got, sets):
        if json.dumps(a, sort_keys=True, ensure_ascii=False) != \
           json.dumps(b, sort_keys=True, ensure_ascii=False):
            print(u'  ชุด %s ในหน้าเว็บไม่ตรงกับไฟล์ต้นทาง' % b['id'])
            bad += 1
    print(u'ตรวจชุดในหน้าเว็บเทียบกับไฟล์ต้นทาง · พบไม่ตรง %d จุด' % bad)
    return bad


def main():
    ap = argparse.ArgumentParser(description=u'ฝังข้อสอบ Part I และ Part II ลงหน้าเว็บ')
    ap.add_argument('--check', action='store_true', help=u'ตรวจอย่างเดียว ไม่เขียนไฟล์')
    a = ap.parse_args()

    sets = build()
    bad = check(sets)
    if bad:
        print(u'\nยังไม่ฝังให้ เพราะต้องแก้ข้อมูลก่อน')
        return 1
    if a.check:
        return 0
    return 1 if write(sets) else 0


if __name__ == '__main__':
    sys.exit(main())
