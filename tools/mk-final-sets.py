#!/usr/bin/env python3
# -*- coding: utf-8 -*-
u"""สร้างหน้า oral-eng/final-sets.html · ข้อสอบเสมือนจริงปลายภาคเก้าชุดเต็ม

ข้อสอบชุดแรกอยู่ที่ oral-eng/final.html มาแต่เดิม หน้านี้เพิ่มอีกเก้าชุด
ครบโครงเดียวกันคือ Part 1 สิบคะแนน Part 2 สิบคะแนน Part 3 ยี่สิบคะแนน

ต่างจากชุดแรกตรงที่ Part 3 ของหน้านี้ใช้ไฟล์เสียง mp3 จริง
ไม่ได้ใช้เสียงอ่านของเบราว์เซอร์ซึ่งคุณภาพต่างกันไปตามเครื่องและไม่มีจังหวะพูด

    python3 tools/mk-final-sets.py            สร้างหน้าใหม่ทั้งหน้า
    python3 tools/mk-final-sets.py --check    ตรวจข้อมูลอย่างเดียว ไม่เขียน

ข้อมูลมาจากสองไฟล์
    tools/final-sets-data.py        Part 1 กับ Part 2 ของทั้งเก้าชุด
    tools/final-listening-data.py   บทฟังของ Part 3 สิบแปดบท

── เรื่องสำคัญเรื่องลำดับการสั่ง ──
หน้านี้ถูกเขียนใหม่ทั้งหน้าทุกครั้งที่สั่ง แต่บล็อก fl-data กับ fl-audio
เป็นของ tools/make-listening.py ซึ่งเขียนลงหน้าเดียวกัน
ตัวนี้จึงดึงสองบล็อกนั้นเก็บไว้ก่อนเขียน แล้วใส่คืนให้เหมือนเดิม
สั่งสองตัวนี้ลำดับไหนก่อนก็ได้ ผลลัพธ์เท่ากัน
"""

import argparse
import importlib.util
import io
import json
import os
import re
import sys

sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PAGE = os.path.join(ROOT, 'oral-eng', 'final-sets.html')

# บล็อกของ tools/make-listening.py ที่ต้องรักษาไว้เมื่อเขียนหน้าใหม่
KEEP_RE = re.compile(
    r'\n*<script type="application/json" id="fl-(?:data|audio)">.*?</script>', re.S)

# หมุดที่บล็อกบทฟังต้องไปอยู่ข้างหน้า ต้องตรงกับ EXAMS['final']['anchor']
# ใน tools/make-listening.py ไม่งั้นสั่งสองตัวสลับลำดับแล้วได้ผลไม่เหมือนกัน
ANCHOR = u'\n<!-- fl:blocks -->'


def load(name, attr):
    spec = importlib.util.spec_from_file_location(re.sub(r'\W', '_', name),
                                                  os.path.join(HERE, name))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return getattr(mod, attr)


SETS2 = load('final-sets-data.py', 'SETS2')
LSETS = load('final-listening-data.py', 'SETS')


# ────────────────────────────── ตรวจข้อมูลก่อนเขียน ──────────────────────────────

def check_data():
    u"""ตรวจทุกอย่างที่เครื่องตรวจได้ ก่อนจะเขียนหน้าเว็บ

    ข้อสอบที่ช่องว่างขาดไปข้อหนึ่ง หรือคำตอบไม่อยู่ในคลังคำ
    จะทำให้นิสิตเสียคะแนนโดยไม่ใช่ความผิดของเขา จึงตรวจให้หมดทุกข้อ
    """
    bad = 0

    def fail(tag, msg):
        nonlocal bad
        bad += 1
        print(u'  %-8s %s' % (tag, msg))

    if len(SETS2) != 9:
        fail('sets', u'มี %d ชุด ต้องเป็น 9 ชุด' % len(SETS2))

    lmap = {st['id']: st for st in LSETS}
    seen = set()

    for st in SETS2:
        sid = st['id']
        if sid in seen:
            fail(sid, u'รหัสชุดซ้ำ')
        seen.add(sid)

        # ทุกชุดต้องมีบทฟังของตัวเองสองบท ไม่งั้น Part 3 จะว่าง
        ls = lmap.get(sid)
        if not ls:
            fail(sid, u'ไม่มีบทฟังของชุดนี้ใน final-listening-data.py')
        elif len(ls['parts']) != 2:
            fail(sid, u'บทฟังมี %d บท ต้องเป็น 2 บท' % len(ls['parts']))
        elif sum(len(p['questions']) for p in ls['parts']) != 20:
            fail(sid, u'คำถาม Part 3 ไม่ครบ 20 ข้อ')
        elif ls['title'] != st['title']:
            fail(sid, u'ชื่อชุดไม่ตรงกับไฟล์บทฟัง · %s กับ %s' % (st['title'], ls['title']))

        for key, label in (('p1', 'Part 1'), ('p2', 'Part 2')):
            P = st.get(key)
            tag = '%s %s' % (sid, key)
            if not P:
                fail(tag, u'ไม่มีข้อมูล %s' % label)
                continue

            text = ' '.join(b['t'] for b in P['blocks'])
            gaps = [int(x) for x in re.findall(r'\[\[(\d+)\]\]', text)]
            if sorted(gaps) != list(range(1, 11)):
                fail(tag, u'ช่องว่างต้องเป็น 1 ถึง 10 ครบและไม่ซ้ำ · พบ %s' % sorted(gaps))

            if len(P['box']) != len(set(P['box'])):
                fail(tag, u'คลังคำมีคำซ้ำ')
            if len(P['box']) < 13:
                fail(tag, u'คลังคำมี %d คำ ควรมีอย่างน้อย 13 คำ' % len(P['box']))

            answers = [P['ans'].get(n) for n in range(1, 11)]
            for n, a in zip(range(1, 11), answers):
                if a is None:
                    fail(tag, u'ไม่มีคำตอบของช่อง %d' % n)
                elif a not in P['box']:
                    fail(tag, u'คำตอบช่อง %d คือ %s ซึ่งไม่อยู่ในคลังคำ' % (n, a))
                if not (P['exp'].get(n) or u'').strip():
                    fail(tag, u'ไม่มีคำอธิบายของช่อง %d' % n)

            # คำลวงคือสิ่งที่ทำให้ข้อสอบวัดอะไรได้ ถ้าคลังคำมีเท่าจำนวนช่องพอดี
            # นิสิตจะกาถูกช่องท้าย ๆ ด้วยการตัดตัวเลือกออกไปเรื่อย ๆ ไม่ใช่ด้วยความรู้
            extras = [w for w in P['box'] if w not in answers]
            if len(extras) < 3:
                fail(tag, u'มีคำลวงเพียง %d คำ ต้องมีอย่างน้อย 3 คำ' % len(extras))

            # คำตอบที่โผล่อยู่ในบทอยู่แล้ว ทำให้เดาได้จากการกวาดตาหาคำซ้ำ
            for n, a in zip(range(1, 11), answers):
                if not a:
                    continue
                stripped = re.sub(r'\[\[\d+\]\]', ' ', text)
                if re.search(r'(?<![a-z-])%s(?![a-z-])' % re.escape(a), stripped, re.I):
                    fail(tag, u'คำตอบช่อง %d คือ %s ปรากฏในบทอยู่แล้ว' % (n, a))
    return bad


# ───────────────────────────────── ชิ้นส่วนของหน้า ─────────────────────────────────

HEAD = u'''<!doctype html>
<html lang="th">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="ข้อสอบเสมือนจริงปลายภาค 5500313 Bus Eng Oral Comm อีก 9 ชุด ชุดละ 40 คะแนน: Vocabulary, Language Points และ Listening พร้อมไฟล์เสียงจริง เฉลยภาษาไทยทุกข้อ">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://peerakong.github.io/Classroom1/oral-eng/final-sets.html">
<meta property="og:type" content="website">
<meta property="og:locale" content="th_TH">
<meta property="og:title" content="ข้อสอบเสมือนจริงปลายภาค 9 ชุด · Oral Comm">
<meta property="og:description" content="อีก 9 ชุด ชุดละ 40 คะแนน พร้อม Listening ที่เป็นไฟล์เสียงจริง 18 บท">
<meta property="og:url" content="https://peerakong.github.io/Classroom1/oral-eng/final-sets.html">
<title>ข้อสอบเสมือนจริงปลายภาค 9 ชุด · Oral Comm</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&amp;family=IBM+Plex+Sans+Thai:wght@400;500;600;700&amp;family=Noto+Serif+Thai:wght@600;700&amp;display=swap">
'''

STYLE = u'''<style>
:root{
  --bg:#fbfcfa; --paper:#f4f2f1; --ink:#1e1917; --muted:#7a6e6a; --line:#dcd2ce;
  --accent:#6b3560; --accent-soft:#f0e2ee; --ok:#1f6b5e; --ok-soft:#dcebe7; --bad:#a3341f; --bad-soft:#f7e4de; --hl:#f6ecd6;
  --f-body:"IBM Plex Sans Thai","IBM Plex Sans",system-ui,-apple-system,sans-serif;
  --f-display:"Noto Serif Thai",Georgia,serif;
  --f-mono:"IBM Plex Mono",ui-monospace,Menlo,monospace;
}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){
  --bg:#15110f; --paper:#1c1715; --ink:#eee7e4; --muted:#8d7f7a; --line:#352c29;
  --accent:#d09ac4; --accent-soft:#2c1a29; --ok:#68c2b0; --ok-soft:#152825; --bad:#eda386; --bad-soft:#32201a; --hl:#2b2413; color-scheme:dark}}
:root[data-theme="dark"]{
  --bg:#15110f; --paper:#1c1715; --ink:#eee7e4; --muted:#8d7f7a; --line:#352c29;
  --accent:#d09ac4; --accent-soft:#2c1a29; --ok:#68c2b0; --ok-soft:#152825; --bad:#eda386; --bad-soft:#32201a; --hl:#2b2413; color-scheme:dark}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--f-body);font-size:16px;line-height:1.65}
body::before{content:"";position:fixed;inset:0 0 auto;height:env(safe-area-inset-top,0px);z-index:10;background:var(--paper)}
.back{display:inline-block;font-family:var(--f-mono);font-size:.72rem;letter-spacing:.11em;color:var(--muted);text-decoration:none}
.back:hover{color:var(--accent)}
.wrap{max-width:820px;margin:0 auto;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:28px 64px;display:flex;flex-direction:column;gap:28px}
header.top{display:flex;flex-direction:column;gap:6px}
.eyebrow{font-family:var(--f-mono);font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
h1{font-family:var(--f-display);font-weight:600;font-size:clamp(26px,5vw,36px);line-height:1.2;margin:0;text-wrap:balance}
h2{font-family:var(--f-display);font-weight:600;font-size:22px;margin:0;text-wrap:balance}
h3{font-size:17px;margin:0;font-weight:600}
p{margin:0}
.muted{color:var(--muted)}
.lede{font-size:17px;display:flex;flex-direction:column;gap:10px}
.note{background:var(--paper);border:1px solid var(--line);border-radius:10px;padding:14px 16px;font-size:15px;display:flex;flex-direction:column;gap:8px}
.picker{display:flex;flex-direction:column;gap:10px}
.picker .row{display:flex;flex-wrap:wrap;gap:8px}
.setbtn{font:inherit;font-size:14px;font-weight:600;border-radius:999px;padding:7px 15px;cursor:pointer;border:1px solid var(--line);background:var(--paper);color:var(--ink)}
.setbtn[aria-pressed="true"]{border-color:var(--accent);background:var(--accent);color:var(--bg)}
.setbtn .dot{font-family:var(--f-mono);font-size:11px;opacity:.75;margin-left:6px}
.bar{position:sticky;top:env(safe-area-inset-top,0px);z-index:5;background:var(--paper);border:1px solid var(--line);border-radius:10px;padding:10px 14px;display:flex;flex-wrap:wrap;gap:10px 18px;align-items:center;justify-content:space-between}
.bar .scores{display:flex;flex-wrap:wrap;gap:6px 16px;font-size:14px;font-variant-numeric:tabular-nums}
.bar .scores b{font-family:var(--f-mono)}
.btns{display:flex;flex-wrap:wrap;gap:8px}
button{font:inherit;font-size:14px;font-weight:600;border-radius:8px;padding:8px 14px;cursor:pointer;border:1px solid var(--accent);background:var(--accent);color:var(--bg)}
button.ghost{background:transparent;color:var(--accent)}
button.small{font-size:13px;padding:5px 11px}
button:focus-visible,select:focus-visible,input:focus-visible,a:focus-visible{outline:3px solid var(--accent);outline-offset:2px}
button:disabled{opacity:.5;cursor:default}
section.part{background:var(--paper);border:1px solid var(--line);border-radius:12px;padding:22px clamp(16px,4vw,28px);display:flex;flex-direction:column;gap:16px}
.part-head{display:flex;flex-wrap:wrap;align-items:baseline;justify-content:space-between;gap:6px 12px;border-bottom:1px solid var(--line);padding-bottom:12px}
.pts{font-family:var(--f-mono);font-size:13px;color:var(--muted)}
.instr{background:var(--accent-soft);border-radius:8px;padding:10px 14px;font-size:15px}
.box{border:1.5px dashed var(--accent);border-radius:8px;padding:12px;display:flex;flex-wrap:wrap;gap:8px}
.chip{font-size:14px;padding:3px 10px;border-radius:999px;border:1px solid var(--line);background:var(--bg)}
.chip.used{text-decoration:line-through;color:var(--muted)}
.passage{display:flex;flex-direction:column;gap:12px;line-height:2.1}
.passage .who{font-weight:600;font-size:14px;color:var(--muted);text-transform:uppercase;letter-spacing:.05em;line-height:1.4}
.blank{display:inline-flex;align-items:center;gap:4px;white-space:nowrap}
.blank .n{font-family:var(--f-mono);font-size:12px;color:var(--accent)}
select{font:inherit;font-size:15px;padding:2px 6px;border-radius:6px;border:1px solid var(--line);background:var(--paper);color:var(--ink);max-width:180px}
select.ok{border-color:var(--ok);background:var(--ok-soft)}
select.bad{border-color:var(--bad);background:var(--bad-soft)}
.clip{display:flex;flex-direction:column;gap:12px;border-top:1px solid var(--line);padding-top:16px}
.clip:first-of-type{border-top:0;padding-top:0}
.clip-head{display:flex;flex-wrap:wrap;align-items:baseline;gap:4px 10px}
.ctx{font-size:15px;color:var(--muted)}
.audio{display:flex;flex-wrap:wrap;align-items:center;gap:10px;border:1px solid var(--line);border-radius:10px;padding:12px 14px;background:var(--bg)}
.audio audio{width:100%;max-width:520px}
.audio .status{font-size:14px;color:var(--muted)}
.audio .warn{font-size:14px;color:var(--bad)}
.q{display:flex;flex-direction:column;gap:8px;padding:12px 0;border-top:1px solid var(--line)}
.q:first-of-type{border-top:0}
.q .stem{font-weight:500}
.q .stem .n{font-family:var(--f-mono);color:var(--accent);margin-right:6px}
.opts{display:flex;flex-direction:column;gap:4px}
.opts label{display:flex;gap:10px;align-items:flex-start;padding:6px 10px;border-radius:8px;cursor:pointer;border:1px solid transparent}
.opts label:hover{background:var(--bg)}
.opts input{margin-top:6px;accent-color:var(--accent)}
.opts label.ok{background:var(--ok-soft);border-color:var(--ok)}
.opts label.bad{background:var(--bad-soft);border-color:var(--bad)}
.exp{font-size:14px;background:var(--hl);border-radius:8px;padding:8px 12px}
.key{display:flex;flex-direction:column;gap:6px;font-size:14px}
.key .row{display:grid;grid-template-columns:auto 1fr;gap:10px;align-items:baseline}
.key .row .n{font-family:var(--f-mono);color:var(--accent)}
details.tr{border:1px solid var(--line);border-radius:10px;padding:10px 14px;background:var(--bg)}
details.tr summary{cursor:pointer;font-weight:600}
details.tr .tx{margin-top:10px;display:flex;flex-direction:column;gap:10px;font-size:15px}
.tx .sp{font-weight:600;color:var(--accent)}
.tag{font-family:var(--f-mono);font-size:11px;padding:1px 6px;border-radius:4px;background:var(--accent-soft);color:var(--accent);margin-right:4px;white-space:nowrap}
.result{border:2px solid var(--accent);border-radius:12px;padding:16px 18px;display:flex;flex-direction:column;gap:8px;background:var(--paper)}
.result .big{font-family:var(--f-display);font-size:30px;font-weight:600;font-variant-numeric:tabular-nums}
.result .rows{display:flex;flex-direction:column;gap:4px;font-size:15px;font-variant-numeric:tabular-nums}
.result .rows .r{display:grid;grid-template-columns:1fr auto;gap:12px}
footer{font-size:13px;color:var(--muted);display:flex;flex-direction:column;gap:6px}
@media (prefers-reduced-motion:reduce){*{scroll-behavior:auto!important}}
</style>
'''


def body():
    return u'''<div class="wrap">

<a class="back" href="index.html">&larr; กลับหน้าวิชา</a>

<header class="top">
  <div class="eyebrow">5500313 Bus Eng Oral Comm · Final · 9 ชุด</div>
  <h1>ข้อสอบเสมือนจริงปลายภาค อีกเก้าชุด</h1>
  <div class="lede">
    <p>เก้าชุดนี้ครบทั้งสามพาร์ตเหมือนข้อสอบจริง ชุดละ <b>40 คะแนน</b>
       รวมกับ<a href="final.html">ชุดที่ 1</a>ที่มีอยู่แล้ว เป็น 10 ชุด</p>
    <p class="muted">Part 3 ของหน้านี้เป็น<b>ไฟล์เสียง mp3 จริง</b>
       ผู้พูดแต่ละคนใช้เสียงคนละเสียง และมีจังหวะหยุดตอนเปลี่ยนคนพูด
       ฟังกี่ครั้งก็ได้ ส่วนบทอ่านจะเปิดให้ดูหลังกดตรวจคำตอบแล้ว</p>
  </div>
</header>

<div class="note">
  <h3>โครงข้อสอบของแต่ละชุด</h3>
  <div class="rows" style="display:flex;flex-direction:column;gap:4px;font-size:15px">
    <div><span class="tag">Part 1</span> Vocabulary · เติมคำลงช่องว่าง 10 ช่อง · 10 คะแนน</div>
    <div><span class="tag">Part 2</span> Language Points · เติมคำลงช่องว่าง 10 ช่อง · 10 คะแนน</div>
    <div><span class="tag">Part 3</span> Listening · สองบท บทละ 10 ข้อ · 20 คะแนน</div>
  </div>
  <p class="muted">ทุกชุดมีบทหนึ่งเป็น<b>การนำเสนอ</b> และอีกบทเป็น<b>การสัมภาษณ์งาน</b>
     ตามแนวข้อสอบจริง · ทุกกิจการและทุกตัวละครสมมุติขึ้นทั้งหมด</p>
</div>

<div class="picker">
  <h3>เลือกชุด</h3>
  <div class="row" id="picker" role="group" aria-label="เลือกชุดข้อสอบ"></div>
  <p class="muted" id="theme"></p>
</div>

<div class="bar">
  <div class="scores">
    <span>Part 1 <b id="s1">–</b>/10</span>
    <span>Part 2 <b id="s2">–</b>/10</span>
    <span>Part 3 <b id="s3">–</b>/20</span>
    <span>รวม <b id="st">–</b>/40</span>
  </div>
  <div class="btns">
    <button id="grade">ตรวจคำตอบ</button>
    <button id="reset" class="ghost">เริ่มใหม่</button>
  </div>
</div>

<div id="result" hidden></div>

<section class="part">
  <div class="part-head">
    <h2>Part 1 · Vocabulary</h2>
    <span class="pts">10 คะแนน</span>
  </div>
  <p class="instr">เติมคำลงช่องว่างที่ (1) ถึง (10)
     ด้วยคำจากคลังคำข้างล่าง · <b>มีคำเกินมาหลายคำ ใช้ไม่ครบทุกคำ</b></p>
  <div class="box" id="box1"></div>
  <div class="passage" id="pass1"></div>
</section>

<section class="part">
  <div class="part-head">
    <h2>Part 2 · Language Points</h2>
    <span class="pts">10 คะแนน</span>
  </div>
  <p class="instr">เติมคำลงช่องว่างที่ (1) ถึง (10)
     ด้วยคำจากคลังคำข้างล่าง · สังเกตรูปคำกริยาและคำที่ตามมาเป็นสำคัญ</p>
  <div class="box" id="box2"></div>
  <div class="passage" id="pass2"></div>
</section>

<section class="part">
  <div class="part-head">
    <h2>Part 3 · Listening</h2>
    <span class="pts">20 คะแนน</span>
  </div>
  <p class="instr">ฟังแต่ละบท แล้วตอบคำถาม 10 ข้อของบทนั้น
     · บทอ่านจะเปิดให้หลังตรวจคำตอบแล้ว</p>
  <div id="clips"></div>
</section>

<footer>
  <p>เอกสารประกอบการสอน รายวิชา 5500313 Business English Oral Communication
     · คณะพาณิชย์และการบัญชี จุฬาลงกรณ์มหาวิทยาลัย</p>
  <p>ทุกกิจการ ทุกชื่อบุคคล และทุกตัวเลขในหน้านี้<b>สมมุติขึ้นเพื่อใช้ฝึก</b>
     ไม่ได้อ้างอิงกิจการหรือบุคคลใด</p>
</footer>

</div>
'''


JS = u'''<!-- fl:blocks -->
<script>
"use strict";
const $ = s => document.querySelector(s);
const esc = s => String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;");

function readJSON(id){
  const el = document.getElementById(id);
  if(!el) return null;
  try { return JSON.parse(el.textContent); } catch(e){ return null; }
}

/* บล็อก JSON ของบทฟังถูกเขียนลงท้ายไฟล์โดย tools/make-listening.py
   ซึ่งอยู่หลังสคริปต์นี้ จึงต้องรออ่านตอน DOMContentLoaded
   ถ้าอ่านทันทีตอนแปลงหน้า บล็อกเหล่านั้นยังไม่เกิด แล้ว Part 3 จะว่างเปล่า */
let SETS = [], LDATA = [], LAUD = {}, LMAP = {};

let cur = 0, graded = false;

/* ─────────────── ตัวเลือกชุด ─────────────── */
function renderPicker(){
  $("#picker").innerHTML = SETS.map((s,i) =>
    `<button class="setbtn" type="button" data-i="${i}" aria-pressed="${i===cur}">${esc(s.title)}</button>`
  ).join("");
  $("#picker").querySelectorAll(".setbtn").forEach(b => {
    b.addEventListener("click", () => { cur = +b.dataset.i; render(); });
  });
  $("#theme").textContent = SETS[cur] ? SETS[cur].theme : "";
}

/* ─────────────── Part 1 และ Part 2 เติมคำ ─────────────── */
function renderGap(P, boxId, passId, prefix){
  $(boxId).innerHTML = P.box.map(w => `<span class="chip" data-w="${esc(w)}">${esc(w)}</span>`).join("");
  const opts = ['<option value="">—</option>']
    .concat([...P.box].sort().map(w => `<option>${esc(w)}</option>`)).join("");
  $(passId).innerHTML = P.blocks.map(b => {
    const html = esc(b.t).replace(/\\[\\[(\\d+)\\]\\]/g, (m,n) =>
      `<span class="blank"><span class="n">(${n})</span><select id="${prefix}-${n}" data-n="${n}" aria-label="Blank ${n}">${opts}</select></span>`);
    return `<div><div class="who">${esc(b.who)}</div><p>${html}</p></div>`;
  }).join("") + `<div class="key" id="${prefix}-key" hidden></div>`;
  $(passId).addEventListener("change", () => markUsed(P, boxId, passId));
}

function markUsed(P, boxId, passId){
  const used = new Set([...document.querySelectorAll(passId+" select")].map(s => s.value).filter(Boolean));
  document.querySelectorAll(boxId+" .chip").forEach(c => c.classList.toggle("used", used.has(c.dataset.w)));
}

function gradeGap(P, prefix){
  let sc = 0; const rows = [];
  for(let n = 1; n <= 10; n++){
    const sel = $("#"+prefix+"-"+n);
    const want = P.ans[n];
    const ok = sel.value === want;
    sel.classList.toggle("ok", ok);
    sel.classList.toggle("bad", !ok);
    if(ok) sc++;
    const mine = (!ok && sel.value) ? ` <span class="muted">(คุณตอบ: ${esc(sel.value)})</span>` : "";
    rows.push(`<div class="row"><span class="n">(${n})</span><span>${ok?"✓":"✗"} <b>${esc(want)}</b>${mine} — ${P.exp[n]}</span></div>`);
  }
  const key = $("#"+prefix+"-key");
  key.innerHTML = "<h3>เฉลย</h3>" + rows.join("");
  key.hidden = false;
  return sc;
}

/* ─────────────── Part 3 ฟังจากไฟล์เสียงจริง ─────────────── */
function renderClips(){
  const ls = LMAP[SETS[cur].id];
  if(!ls){
    $("#clips").innerHTML = `<p class="warn">ยังไม่มีบทฟังของชุดนี้</p>`;
    return;
  }
  $("#clips").innerHTML = ls.parts.map((p, pi) => {
    const clip = LAUD[p.id];
    const kind = p.kind === "interview"
      ? "Job interview"
      : (p.kind === "presentation" ? "Presentation" : "Talk");
    /* ลายเซ็นของบทกับของไฟล์เสียงต้องตรงกัน ไม่งั้นคลิปยังพูดบทเก่า
       หน้าเว็บจึงเตือนเองโดยไม่ต้องรอให้คนมาสังเกต */
    const stale = clip && clip.sig && p.sig && clip.sig !== p.sig;
    let player;
    if(clip && !stale){
      player = `<div class="audio">
          <audio controls preload="none" src="${esc(clip.src)}"></audio>
          <span class="status">${fmt(clip.dur)} · ${p.turns.length} ช่วงพูด</span>
        </div>`;
    } else {
      player = `<div class="audio"><span class="warn">${stale
        ? "ไฟล์เสียงยังเป็นบทเก่า รอสร้างใหม่"
        : "ยังไม่มีไฟล์เสียงของบทนี้"
      }</span><button class="ghost small" type="button" data-show="${pi}">เปิดบทอ่านแทน</button></div>`;
    }
    const qs = p.questions.map((q, i) => {
      const nn = pi * 10 + i + 1;
      return `<div class="q" id="l3-${pi}-q${i}">
        <div class="stem"><span class="n">${nn}.</span>${esc(q.q)}</div>
        <div class="opts">${q.o.map((o,j) =>
          `<label><input type="radio" name="l3-${pi}-${i}" value="${j}"><span><b>${"ABCD"[j]}.</b> ${esc(o)}</span></label>`
        ).join("")}</div>
        <div class="exp" hidden></div>
      </div>`;
    }).join("");
    return `<div class="clip">
      <div class="clip-head"><span class="tag">${kind}</span><h3>${esc(p.title)}</h3></div>
      <p class="ctx">${esc(p.context)}</p>
      ${player}
      <details class="tr" id="tr-${pi}" ${clip && !stale ? "" : "open"}>
        <summary>บทอ่าน · transcript</summary>
        <div class="tx">${p.turns.map(t =>
          `<div><span class="sp">${esc(t[0])}:</span> ${esc(t[1])}</div>`).join("")}</div>
      </details>
      ${qs}
    </div>`;
  }).join("");

  /* ก่อนตรวจคำตอบ บทอ่านต้องปิดไว้ ไม่งั้นก็ไม่ได้วัดการฟัง */
  ls.parts.forEach((p, pi) => {
    const clip = LAUD[p.id];
    const stale = clip && clip.sig && p.sig && clip.sig !== p.sig;
    const d = $("#tr-"+pi);
    if(d && clip && !stale) d.open = false;
  });
  $("#clips").querySelectorAll("[data-show]").forEach(b => {
    b.addEventListener("click", () => { const d = $("#tr-"+b.dataset.show); if(d) d.open = true; });
  });
}

function fmt(sec){
  sec = Math.round(sec || 0);
  return Math.floor(sec/60) + ":" + String(sec%60).padStart(2,"0");
}

function gradeClips(){
  const ls = LMAP[SETS[cur].id];
  if(!ls) return 0;
  let sc = 0;
  ls.parts.forEach((p, pi) => {
    p.questions.forEach((q, i) => {
      const chosen = document.querySelector(`input[name="l3-${pi}-${i}"]:checked`);
      const labels = document.querySelectorAll(`#l3-${pi}-q${i} label`);
      labels.forEach(l => l.classList.remove("ok","bad"));
      labels[q.a].classList.add("ok");
      const ok = chosen && +chosen.value === q.a;
      if(chosen && !ok) labels[+chosen.value].classList.add("bad");
      if(ok) sc++;
      const ex = document.querySelector(`#l3-${pi}-q${i} .exp`);
      ex.innerHTML = q.e;
      ex.hidden = false;
    });
    const d = $("#tr-"+pi);
    if(d) d.open = true;
  });
  return sc;
}

/* ─────────────── ประกอบหน้า ─────────────── */
function render(){
  graded = false;
  const S = SETS[cur];
  renderPicker();
  renderGap(S.p1, "#box1", "#pass1", "p1");
  renderGap(S.p2, "#box2", "#pass2", "p2");
  renderClips();
  ["#s1","#s2","#s3","#st"].forEach(id => $(id).textContent = "–");
  $("#result").hidden = true;
  $("#grade").disabled = false;
  window.scrollTo({top:0, behavior:"instant"});
}

function grade(){
  if(graded) return;
  graded = true;
  const S = SETS[cur];
  const a = gradeGap(S.p1, "p1");
  const b = gradeGap(S.p2, "p2");
  const c = gradeClips();
  const tot = a + b + c;
  $("#s1").textContent = a;
  $("#s2").textContent = b;
  $("#s3").textContent = c;
  $("#st").textContent = tot;
  const pct = Math.round(tot / 40 * 100);
  let word;
  if(pct >= 85)      word = "ดีมาก พร้อมสอบ";
  else if(pct >= 70) word = "ใช้ได้ ทวนส่วนที่พลาดอีกรอบ";
  else if(pct >= 50) word = "พอใช้ ควรกลับไปอ่านบทเรียนอีกครั้ง";
  else               word = "ยังต้องทบอีกมาก";
  $("#result").innerHTML = `<div class="result">
    <div class="big">${tot} / 40 <span class="muted" style="font-size:18px">(${pct}%)</span></div>
    <div class="rows">
      <div class="r"><span>Part 1 · Vocabulary</span><span>${a} / 10</span></div>
      <div class="r"><span>Part 2 · Language Points</span><span>${b} / 10</span></div>
      <div class="r"><span>Part 3 · Listening</span><span>${c} / 20</span></div>
    </div>
    <p>${word}</p>
    <p class="muted">เฉลยของทุกข้ออยู่ใต้แต่ละพาร์ตแล้ว · บทอ่านของ Part 3 เปิดให้แล้วเช่นกัน</p>
  </div>`;
  $("#result").hidden = false;
  $("#grade").disabled = true;
}

function boot(){
  SETS  = readJSON("fx-sets") || [];
  LDATA = readJSON("fl-data") || [];
  LAUD  = readJSON("fl-audio") || {};
  LMAP  = {};
  LDATA.forEach(s => LMAP[s.id] = s);
  if(!SETS.length){
    $("#picker").innerHTML = `<p class="warn">ยังไม่มีข้อสอบในหน้านี้</p>`;
    return;
  }
  $("#grade").addEventListener("click", grade);
  $("#reset").addEventListener("click", render);
  render();
}

if(document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot);
else boot();
</script>
'''


def write_page():
    u"""เขียนหน้าใหม่ทั้งหน้า แต่รักษาบล็อกของ make-listening.py ไว้"""
    keep = u''
    if os.path.exists(PAGE):
        old = io.open(PAGE, encoding='utf-8').read()
        keep = u''.join(KEEP_RE.findall(old))

    data = [{'id': st['id'], 'title': st['title'], 'theme': st['theme'],
             'p1': {'box': list(st['p1']['box']),
                    'blocks': [{'who': b['who'], 't': b['t']} for b in st['p1']['blocks']],
                    'ans': {str(k): v for k, v in st['p1']['ans'].items()},
                    'exp': {str(k): v for k, v in st['p1']['exp'].items()}},
             'p2': {'box': list(st['p2']['box']),
                    'blocks': [{'who': b['who'], 't': b['t']} for b in st['p2']['blocks']],
                    'ans': {str(k): v for k, v in st['p2']['ans'].items()},
                    'exp': {str(k): v for k, v in st['p2']['exp'].items()}}}
            for st in SETS2]

    block = (u'\n<script type="application/json" id="fx-sets">\n'
             + json.dumps(data, ensure_ascii=False, separators=(',', ':'))
             + u'\n</script>\n')

    html = HEAD + STYLE + body() + block + JS

    # บล็อกบทฟังต้องอยู่หน้าสคริปต์ จึงใส่คืนตรงหมุดเดียวกับที่ make-listening.py ใช้
    # keep ยังมีขึ้นบรรทัดนำหน้าที่ make-listening.py ใส่ไว้ จึงไม่ตัดออก
    # ไม่งั้นสั่งสองตัวสลับลำดับแล้วไฟล์ต่างกันที่ช่องว่าง ซึ่งทำให้ diff รกเปล่า ๆ
    if keep:
        at = html.find(ANCHOR)
        keep = keep.rstrip(u'\n')
        html = (html[:at] + keep + html[at:]) if at > 0 else (html + keep + u'\n')

    io.open(PAGE, 'w', encoding='utf-8').write(html.rstrip(u'\n') + u'\n')
    print(u'  เขียน %s · %.0f KB'
          % (os.path.relpath(PAGE, ROOT), os.path.getsize(PAGE) / 1024.0))
    if keep:
        print(u'  รักษาบล็อก fl-data กับ fl-audio เดิมไว้')
    else:
        print(u'  ยังไม่มีบทฟังในหน้า '
              u'· สั่ง python3 tools/make-listening.py --exam final --page-only')


HUB = os.path.join(ROOT, 'oral-eng', 'index.html')

# ลิงก์เข้าหน้านี้จากหน้าวิชา เป็นของตัวสร้างนี้เจ้าเดียว
# ใช้หมุดคร่อมไว้ สั่งซ้ำกี่ครั้งก็ได้ลิงก์เดียวไม่งอก
HUB_START = u'<!-- sets:link:start -->'
HUB_END = u'<!-- sets:link:end -->'
HUB_RE = re.compile(re.escape(HUB_START) + r'.*?' + re.escape(HUB_END), re.S)
HUB_ANCHOR = u'      <a class="final-link" href="final-prep.html">'


def patch_hub():
    u"""เพิ่มลิงก์เข้าหน้าข้อสอบเก้าชุด ไว้ที่หัวหน้าวิชาข้างลิงก์ชุดแรก"""
    if not os.path.exists(HUB):
        print(u'  ไม่พบ oral-eng/index.html จึงยังไม่ได้ใส่ลิงก์')
        return
    html = io.open(HUB, encoding='utf-8').read()
    link = (HUB_START
            + u'\n      <a class="final-link" href="final-sets.html">'
            + u'ข้อสอบเสมือนจริงปลายภาค อีก 9 ชุด '
            + u'· ฟังจากไฟล์เสียงจริง →</a>\n'
            + HUB_END)

    if HUB_RE.search(html):
        new = HUB_RE.sub(lambda m: link, html)
    else:
        at = html.find(HUB_ANCHOR)
        if at < 0:
            print(u'  หาจุดใส่ลิงก์ในหน้าวิชาไม่เจอ')
            return
        end = html.find(u'\n', at) + 1
        new = html[:end] + u'      ' + link + u'\n' + html[end:]

    if new == html:
        print(u'  ลิงก์ที่หน้าวิชาเหมือนเดิม')
        return
    io.open(HUB, 'w', encoding='utf-8').write(new)
    print(u'  ใส่ลิงก์เข้าหน้านี้ที่ oral-eng/index.html แล้ว')


def verify():
    u"""ตรวจหน้าที่เขียนเสร็จ ว่าข้อมูลที่ฝังไปตรงกับไฟล์ข้อมูลจริง"""
    html = io.open(PAGE, encoding='utf-8').read()
    m = re.search(r'id="fx-sets">(.*?)</script>', html, re.S)
    if not m:
        print(u'  ตรวจแล้วไม่พบข้อสอบในหน้า')
        return 1
    page = json.loads(m.group(1))
    bad = 0
    if len(page) != len(SETS2):
        print(u'  จำนวนชุดไม่ตรง'); bad += 1
    for a, st in zip(page, SETS2):
        for key in ('p1', 'p2'):
            if [b['t'] for b in a[key]['blocks']] != [b['t'] for b in st[key]['blocks']]:
                print(u'  %s %s บทไม่ตรง' % (st['id'], key)); bad += 1
            if a[key]['ans'] != {str(k): v for k, v in st[key]['ans'].items()}:
                print(u'  %s %s คำตอบไม่ตรง' % (st['id'], key)); bad += 1

    opens = html.count('<div') + html.count('<section') + html.count('<details')
    closes = html.count('</div>') + html.count('</section>') + html.count('</details>')
    print(u'  ตรวจข้อมูลในหน้าเทียบกับไฟล์ข้อมูล '
          u'· พบไม่ตรง %d จุด' % bad)
    return bad


def main():
    ap = argparse.ArgumentParser(description=u'สร้างหน้าข้อสอบปลายภาคเก้าชุด')
    ap.add_argument('--check', action='store_true', help=u'ตรวจข้อมูลอย่างเดียว ไม่เขียนหน้า')
    a = ap.parse_args()

    print(u'\nตรวจข้อมูล')
    bad = check_data()
    print(u'  พบปัญหา %d จุด' % bad)
    if bad:
        print(u'\nข้อมูลมีปัญหา ยังไม่เขียนหน้าให้')
        return 1
    if a.check:
        print(u'\nข้อมูลครบถ้วน พร้อมสร้างหน้า')
        return 0

    print(u'\nเขียนหน้า')
    write_page()
    patch_hub()
    return verify()


if __name__ == '__main__':
    sys.exit(main())
