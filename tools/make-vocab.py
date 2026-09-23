#!/usr/bin/env python3
# -*- coding: utf-8 -*-
u"""ฝังคลังคำศัพท์ลงหน้าวิชาภาษาอังกฤษ พร้อมตรวจกติกาก่อนฝังทุกครั้ง

    python3 tools/make-vocab.py --check   ตรวจอย่างเดียว
    python3 tools/make-vocab.py           ตรวจแล้วฝัง

กติกาที่บังคับ
  ทุกคำต้องมีครบห้าช่อง คือ คำศัพท์ คำแปล คำอธิบาย ตัวอย่างประโยค และคำแปลของตัวอย่าง
  ตัวอย่างประโยคต้องมีคำศัพท์นั้นอยู่จริง ไม่ใช่ประโยคที่ไม่เกี่ยวกัน
  คำอธิบายต้องไม่ใช่การแปลซ้ำ จึงบังคับให้ยาวกว่าคำแปลพอสมควร
  ไม่ใช้ชื่อกิจการจริง ให้สอดคล้องกับข้อสอบส่วนอื่นของวิชา

หลังฝังเสร็จจะอ่านหน้าเว็บกลับมาตรวจว่าตรงกับไฟล์ต้นทางจริง
เพราะเคยมีกรณีที่เครื่องมือเขียนกลับไม่ครบแล้วไม่มีอะไรจับได้
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
WANT = 129

SOURCES = ['vocab-1.py', 'vocab-2.py']

BLOCK_RE = re.compile(r'\n*<script type="application/json" id="vc-data">.*?</script>', re.S)
# ต้องวางก่อนแท็ก script ตัวแรก ไม่ใช่ก่อน cn-data ซึ่งอยู่ท้ายไฟล์
# เพราะสคริปต์ที่อ่านบล็อกนี้อยู่กลางหน้า ถ้าข้อมูลอยู่หลังมัน
# getElementById จะคืนค่าว่างและแท็บคำศัพท์จะไม่ขึ้นเลย
ANCHOR = '</footer>\n'

REAL_CO = re.compile(r'Kraft|Cadbury|Disney|Pixar|Nestl|Toyota|Panasonic|Exxon|Mobil|'
                     r'Vodafone|Unilever|Tesco|L’Or')

# คำที่ไม่ต้องหาในตัวอย่างประโยค เพราะเป็นคำไวยากรณ์ ไม่ใช่ตัวคำศัพท์
SKIP = {'a', 'an', 'the', 'in', 'for', 'with', 'of', 'to', 'up', 'out', 'over'}

# คำแทนที่ในรูปแบบของศัพท์ ซึ่งตัวอย่างจริงมักเปลี่ยนเป็นคำอื่น
# เช่น introduce a product ตัวอย่างเขียนว่า introduced a low-sugar version
PLACEHOLDER = {'product', 'company', 'firm', 'goods'}

# กริยาอปกติที่เทียบด้วยตัวอักษรต้นคำไม่ได้
IRREGULAR = {
    'take': ('took', 'taken', 'takes', 'taking'),
    'make': ('made', 'makes', 'making'),
    'sell': ('sold', 'sells', 'selling'),
    'bring': ('brought', 'brings', 'bringing'),
    'buy': ('bought', 'buys', 'buying'),
    'hold': ('held', 'holds', 'holding'),
    'build': ('built', 'builds', 'building'),
    'set': ('sets', 'setting'),
    'withdraw': ('withdrew', 'withdrawn', 'withdraws'),
    'rise': ('rose', 'risen', 'rises', 'rising'),
}


def load():
    groups = []
    for name in SOURCES:
        path = os.path.join(HERE, name)
        spec = importlib.util.spec_from_file_location(name[:-3].replace('-', '_'), path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        groups.extend(mod.GROUPS)
    return groups


def in_example(term, example):
    """ตัวอย่างประโยคมีคำศัพท์นั้นอยู่ไหม โดยยอมให้ผันรูปและเปลี่ยนคำแทนที่ได้

    ศัพท์หลายตัวเป็นรูปแบบ ไม่ใช่ข้อความตายตัว เช่น introduce a product
    ซึ่งตัวอย่างจริงเขียนว่า introduced a low-sugar version จึงต้องยอมให้
    คำแทนที่อย่าง product หรือ company ถูกเปลี่ยนเป็นคำอื่นได้
    และต้องเผื่อกริยาอปกติอย่าง take กับ took ซึ่งเทียบด้วยตัวอักษรต้นคำไม่ได้

    เกณฑ์คือ ต้องเจออย่างน้อยครึ่งหนึ่งของคำที่มีความหมาย และอย่างน้อยหนึ่งคำเสมอ
    """
    tokens = set(re.findall(r'[a-z0-9]+', example.lower()))

    def hit(word):
        w = word.lower()
        if w in SKIP or w in PLACEHOLDER:
            return True
        if w in tokens:
            return True
        for form in IRREGULAR.get(w, ()):
            if form in tokens:
                return True
        stem = w[:4] if len(w) > 4 else w
        return any(t.startswith(stem) for t in tokens)

    best = False
    for alt in term.split(u'\u00b7'):
        words = [w for w in re.findall(r'[A-Za-z0-9]+', alt) if w.lower() not in SKIP]
        if not words:
            continue
        found = sum(1 for w in words if hit(w))
        if found and found * 2 >= len(words):
            best = True
    return best


def check(groups):
    bad = 0
    total = 0

    def fail(term, msg):
        nonlocal bad
        bad += 1
        print(u'  %-34s %s' % (term[:34], msg))

    seen = {}
    for g in groups:
        for it in g['items']:
            total += 1
            if len(it) != 5:
                fail(str(it[0]), u'มี %d ช่อง ต้องเป็น 5 ช่อง' % len(it))
                continue
            w, th, note, ex, exth = it
            if w in seen:
                fail(w, u'คำซ้ำกับหมวด %s' % seen[w])
            seen[w] = g['code']

            if not th.strip():
                fail(w, u'ไม่มีคำแปล')
            if not note.strip():
                fail(w, u'ไม่มีคำอธิบาย')
            elif len(note) < len(th) + 10:
                fail(w, u'คำอธิบายสั้นเกินไป ดูเหมือนแปลซ้ำมากกว่าอธิบาย')
            if not ex.strip():
                fail(w, u'ไม่มีตัวอย่างประโยค')
            elif not ex.rstrip().endswith(('.', '?', '!')):
                fail(w, u'ตัวอย่างประโยคไม่จบประโยค')
            elif not in_example(w, ex):
                fail(w, u'ตัวอย่างประโยคไม่มีคำศัพท์นี้อยู่ · %s' % ex[:48])
            if not exth.strip():
                fail(w, u'ไม่มีคำแปลของตัวอย่างประโยค')
            m = REAL_CO.search(ex)
            if m:
                fail(w, u'ตัวอย่างประโยคมีชื่อกิจการจริง %s' % m.group(0))

    print('')
    for g in groups:
        print(u'%-10s %-28s %-9s %2d คำ' % (g['code'], g['name'], g['unit'], len(g['items'])))
    print(u'\nรวม %d คำ · %d หมวด' % (total, len(groups)))
    if total != WANT:
        print(u'ต้องการ %d คำ แต่มี %d คำ' % (WANT, total))
        bad += 1
    print(u'ตรวจพบปัญหา %d จุด' % bad)
    return bad


def write(groups):
    data = [{'code': g['code'], 'name': g['name'], 'unit': g['unit'],
             'items': [list(it) for it in g['items']]} for g in groups]
    html = io.open(PAGE, encoding='utf-8').read()
    block = ('\n\n<script type="application/json" id="vc-data">\n' +
             json.dumps(data, ensure_ascii=False, separators=(',', ':')) + '\n</script>')
    html = BLOCK_RE.sub('', html)
    at = html.find(ANCHOR)
    if at < 0:
        print(u'หาจุดวางบล็อกในหน้าไม่เจอ')
        return 1
    at += len(ANCHOR)
    html = html[:at] + block.lstrip('\n') + '\n' + html[at:]
    io.open(PAGE, 'w', encoding='utf-8').write(html.rstrip('\n') + '\n')
    print(u'\nฝังคลังคำศัพท์ลง oral-eng/index.html แล้ว · %.1f KB' % (len(block) / 1024.0))
    return verify(groups)


def verify(groups):
    """อ่านหน้าเว็บกลับมาตรวจว่าตรงกับไฟล์ต้นทางจริง และอยู่ถูกที่"""
    html = io.open(PAGE, encoding='utf-8').read()
    at_data = html.find('id="vc-data"')
    at_script = html.find('\n<script>\n')
    if at_data < 0 or at_script < 0 or at_data > at_script:
        print(u'  บล็อกคำศัพท์อยู่หลังสคริปต์ที่อ่านมัน แท็บจะขึ้นว่างเปล่า')
        return 1
    m = BLOCK_RE.search(html)
    got = json.loads(re.search(r'>(.*?)</script>', m.group(0), re.S).group(1)) if m else []
    page = {it[0]: it for g in got for it in g['items']}
    bad = 0
    for g in groups:
        for it in g['items']:
            a = page.get(it[0])
            if not a:
                print(u'  %s ไม่มีในหน้าเว็บ' % it[0]); bad += 1
            elif list(a) != list(it):
                print(u'  %s ในหน้าเว็บไม่ตรงกับไฟล์ต้นทาง' % it[0]); bad += 1
    print(u'ตรวจคำในหน้าเว็บเทียบกับไฟล์ต้นทาง · พบไม่ตรง %d จุด' % bad)
    return bad


def main():
    ap = argparse.ArgumentParser(description=u'ฝังคลังคำศัพท์ลงหน้าวิชาภาษาอังกฤษ')
    ap.add_argument('--check', action='store_true', help=u'ตรวจอย่างเดียว ไม่เขียนไฟล์')
    a = ap.parse_args()

    groups = load()
    if check(groups):
        print(u'\nยังไม่ฝังให้ เพราะต้องแก้ข้อมูลก่อน')
        return 1
    if a.check:
        return 0
    return 1 if write(groups) else 0


if __name__ == '__main__':
    sys.exit(main())
