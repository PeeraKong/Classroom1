#!/usr/bin/env python3
# -*- coding: utf-8 -*-
u"""สร้างหน้า oral-eng/drills.html · แบบฝึกตามรูปแบบข้อสอบจริง

    python3 tools/mk-drills.py            ตรวจแล้วเขียนหน้า
    python3 tools/mk-drills.py --check    ตรวจอย่างเดียว

ข้อมูลอยู่ที่ tools/oral-drills-data.py
หน้านี้เขียนใหม่ทั้งหน้าทุกครั้ง ไม่มีเครื่องมืออื่นเขียนลงไฟล์เดียวกัน
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
PAGE = os.path.join(ROOT, 'oral-eng', 'drills.html')
HUB = os.path.join(ROOT, 'oral-eng', 'index.html')

_spec = importlib.util.spec_from_file_location('odd', os.path.join(HERE, 'oral-drills-data.py'))
_m = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_m)
DRILLS, GROUPS = _m.DRILLS, _m.GROUPS

SARL = [u'Situation (S)', u'Action (A)', u'Result (R)', u'Lesson (L)']
THREE = [u'SUCCESS', u'STRENGTH', u'SITUATION']


def check_data():
    u"""ตรวจทุกอย่างที่เครื่องตรวจได้ ก่อนเขียนหน้า"""
    bad = 0

    def fail(tag, msg):
        nonlocal bad
        bad += 1
        print(u'  %-6s %s' % (tag, msg))

    known = set(g[0] for g in GROUPS)
    seen = set()
    for d in DRILLS:
        tag = d['id']
        if tag in seen:
            fail(tag, u'รหัสซ้ำ')
        seen.add(tag)
        if d['group'] not in known:
            fail(tag, u'ไม่รู้จักกลุ่ม %s' % d['group'])

        text = ' '.join(b['t'] for b in d['blocks'])
        gaps = [int(x) for x in re.findall(r'\[\[(\d+)\]\]', text)]
        n = len(d['box'])
        if sorted(gaps) != list(range(1, n + 1)):
            fail(tag, u'ช่องว่างต้องเป็น 1 ถึง %d ครบและไม่ซ้ำ · พบ %s' % (n, sorted(gaps)))

        if len(d['box']) != len(set(d['box'])):
            fail(tag, u'คลังคำมีรายการซ้ำ')

        answers = [d['ans'].get(i) for i in range(1, n + 1)]
        for i, a in zip(range(1, n + 1), answers):
            if a is None:
                fail(tag, u'ไม่มีคำตอบของช่อง %d' % i)
            elif a not in d['box']:
                fail(tag, u'คำตอบช่อง %d คือ %s ซึ่งไม่อยู่ในคลังคำ' % (i, a))
            if not (d['exp'].get(i) or u'').strip():
                fail(tag, u'ไม่มีคำอธิบายของช่อง %d' % i)

        # คลังคำมีจำนวนเท่าช่องว่างพอดี ทุกคำจึงต้องถูกใช้คำละครั้ง
        # ถ้ามีคำไหนไม่ถูกใช้ แปลว่ามีอีกคำถูกใช้สองครั้ง ซึ่งขัดกับรูปแบบของข้อสอบจริง
        unused = [w for w in d['box'] if w not in answers]
        if unused:
            fail(tag, u'มีรายการในคลังคำที่ไม่ได้เป็นคำตอบของช่องใดเลย · %s' % ' / '.join(unused))

        labels = [b['label'] for b in d['blocks']]
        if d['group'] == 'sarl' and labels != SARL:
            fail(tag, u'โครง SAR+L ต้องมีสี่ช่องตามลำดับ · พบ %s' % ' '.join(labels))
        if d['group'] == 'three' and labels != THREE:
            fail(tag, u"โครง Three S's ต้องมีสามช่องตามลำดับ · พบ %s" % ' '.join(labels))

        # คำตอบที่โผล่อยู่ในบทอยู่แล้ว ทำให้เดาได้จากการกวาดตา
        # ตรวจเฉพาะกลุ่มที่คำตอบเป็นวลียาว เพราะคำเดี่ยวอย่าง of หรือ to
        # ย่อมปรากฏซ้ำในที่อื่นของบทอยู่แล้วโดยเลี่ยงไม่ได้
        if d['group'] in ('sarl', 'three'):
            stripped = re.sub(r'\[\[\d+\]\]', ' ', text).lower()
            for i, a in zip(range(1, n + 1), answers):
                if a and a.lower() in stripped:
                    fail(tag, u'คำตอบช่อง %d ปรากฏในบทอยู่แล้ว · %s' % (i, a))
    return bad


HEAD = u'''<!doctype html>
<html lang="th">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="แบบฝึกตามรูปแบบข้อสอบจริง วิชาภาษาอังกฤษเพื่อการสื่อสาร · เติมคำภาษาการนำเสนอและคำบุพบท · เติมวลีลงโครง SAR+L และโครง Three S's พร้อมเฉลยภาษาไทยทุกช่อง">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://peerakong.github.io/Classroom1/oral-eng/drills.html">
<meta property="og:type" content="website">
<meta property="og:locale" content="th_TH">
<meta property="og:title" content="แบบฝึกตามรูปแบบข้อสอบจริง · Oral Comm">
<meta property="og:description" content="เติมคำจากกล่อง · โครง SAR+L · โครง Three S's พร้อมเฉลยภาษาไทยทุกช่อง">
<meta property="og:url" content="https://peerakong.github.io/Classroom1/oral-eng/drills.html">
<title>แบบฝึกตามรูปแบบข้อสอบจริง · Oral Comm</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&amp;family=IBM+Plex+Sans+Thai:wght@400;500;600;700&amp;family=Noto+Serif+Thai:wght@600;700&amp;display=swap">
<style>
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
.wrap{max-width:820px;margin:0 auto;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:28px 64px;display:flex;flex-direction:column;gap:26px}
header.top{display:flex;flex-direction:column;gap:6px}
.eyebrow{font-family:var(--f-mono);font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
h1{font-family:var(--f-display);font-weight:600;font-size:clamp(26px,5vw,36px);line-height:1.2;margin:0;text-wrap:balance}
h2{font-family:var(--f-display);font-weight:600;font-size:21px;margin:0;text-wrap:balance}
p{margin:0}
.muted{color:var(--muted)}
.lede{font-size:17px;display:flex;flex-direction:column;gap:10px}
.note{background:var(--paper);border:1px solid var(--line);border-radius:10px;padding:14px 16px;font-size:15px;display:flex;flex-direction:column;gap:8px}
.tabs{display:flex;flex-wrap:wrap;gap:8px}
.tabs button{font:inherit;font-size:14px;font-weight:600;border-radius:999px;padding:7px 15px;cursor:pointer;border:1px solid var(--line);background:var(--paper);color:var(--ink)}
.tabs button[aria-pressed="true"]{border-color:var(--accent);background:var(--accent);color:var(--bg)}
.gdesc{font-size:15px;color:var(--muted)}
button{font:inherit;font-size:14px;font-weight:600;border-radius:8px;padding:8px 14px;cursor:pointer;border:1px solid var(--accent);background:var(--accent);color:var(--bg)}
button.ghost{background:transparent;color:var(--accent)}
button.small{font-size:13px;padding:5px 11px}
button:focus-visible,select:focus-visible,a:focus-visible{outline:3px solid var(--accent);outline-offset:2px}
button:disabled{opacity:.5;cursor:default}
section.ex{background:var(--paper);border:1px solid var(--line);border-radius:12px;padding:20px clamp(15px,4vw,26px);display:flex;flex-direction:column;gap:14px}
.ex-head{display:flex;flex-wrap:wrap;align-items:baseline;justify-content:space-between;gap:6px 12px;border-bottom:1px solid var(--line);padding-bottom:10px}
.pts{font-family:var(--f-mono);font-size:13px;color:var(--muted)}
.box{border:1.5px dashed var(--accent);border-radius:8px;padding:12px;display:flex;flex-wrap:wrap;gap:8px}
.chip{font-size:14px;padding:3px 10px;border-radius:999px;border:1px solid var(--line);background:var(--bg)}
.chip.used{text-decoration:line-through;color:var(--muted)}
.blk{display:flex;flex-direction:column;gap:5px;line-height:2.15}
.blk .lb{font-weight:600;font-size:13px;color:var(--accent);text-transform:uppercase;letter-spacing:.06em;line-height:1.4;font-family:var(--f-mono)}
.frame .blk{border-left:3px solid var(--accent);padding:8px 0 8px 13px;background:var(--bg);border-radius:0 6px 6px 0}
.body{display:flex;flex-direction:column;gap:11px}
.blank{display:inline-flex;align-items:center;gap:4px}
.blank .n{font-family:var(--f-mono);font-size:12px;color:var(--accent)}
select{font:inherit;font-size:15px;padding:2px 6px;border-radius:6px;border:1px solid var(--line);background:var(--paper);color:var(--ink);max-width:min(330px,74vw)}
select.ok{border-color:var(--ok);background:var(--ok-soft)}
select.bad{border-color:var(--bad);background:var(--bad-soft)}
.row-btns{display:flex;flex-wrap:wrap;gap:8px;align-items:center}
.sc{font-family:var(--f-mono);font-size:14px;color:var(--muted);font-variant-numeric:tabular-nums}
.key{display:none;flex-direction:column;gap:6px;font-size:14px;background:var(--hl);border-radius:8px;padding:11px 14px}
.key.on{display:flex}
.key .r{display:grid;grid-template-columns:auto 1fr;gap:10px;align-items:baseline}
.key .r .n{font-family:var(--f-mono);color:var(--accent)}
footer{font-size:13px;color:var(--muted);display:flex;flex-direction:column;gap:6px}
@media (prefers-reduced-motion:reduce){*{scroll-behavior:auto!important}}
</style>
'''


BODY = u'''<div class="wrap">

<a class="back" href="index.html">&larr; กลับหน้าวิชา</a>

<header class="top">
  <div class="eyebrow">5500313 Bus Eng Oral Comm · แบบฝึกตามรูปแบบข้อสอบ</div>
  <h1>แบบฝึกตามรูปแบบข้อสอบจริง</h1>
  <div class="lede">
    <p>สามรูปแบบที่ข้อสอบใช้จริง · <b>เติมคำจากกล่อง</b> · <b>เติมวลีลงโครง SAR+L</b> ·
       และ <b>เติมวลีลงโครง Three S&rsquo;s</b></p>
    <p class="muted">ทุกชุด<b>คลังคำมีจำนวนเท่าช่องว่างพอดี</b> ใช้ครบทุกรายการ รายการละครั้ง
       เหมือนแบบฝึกของรายวิชา · กดตรวจได้ทีละชุด และมีคำอธิบายภาษาไทยทุกช่อง</p>
  </div>
</header>

<div class="note">
  <h2>ทำไมสองรูปแบบหลังถึงต่างจากแบบฝึกเติมคำ</h2>
  <p>แบบเติมคำวัดว่ารู้ศัพท์และรู้บุพบทไหม · แต่แบบ <b>SAR+L</b> กับ <b>Three S&rsquo;s</b>
     วัดอีกอย่างหนึ่ง คือ<b>รู้ไหมว่าคำตอบที่ดีวางอะไรไว้ตรงไหน</b></p>
  <p>เวลาทำสองแบบหลัง ให้ดูที่<b>ตำแหน่ง</b>ของช่องว่างก่อนดูที่ตัวเลือก ·
     ช่องที่อยู่ต้น Situation มักเป็นการบอกบทบาทของตัวเอง · ช่องต้น Action
     มักเป็นสิ่งที่ตัดสินใจทำ · ช่องใน Lesson มักขึ้นต้นด้วย what I learned
     แล้วปิดด้วยการโยงไปที่งานที่สมัคร</p>
</div>

<div class="tabs" id="tabs" role="group" aria-label="เลือกกลุ่มแบบฝึก"></div>
<p class="gdesc" id="gdesc"></p>

<div id="list"></div>

<footer>
  <p>เอกสารประกอบการสอน รายวิชา 5500313 Business English Oral Communication
     · คณะพาณิชยศาสตร์และการบัญชี จุฬาลงกรณ์มหาวิทยาลัย</p>
  <p>ทุกกิจการ ทุกชื่อบุคคล และทุกตัวเลขในหน้านี้<b>สมมุติขึ้นเพื่อใช้ฝึก</b>
     ไม่ได้อ้างอิงกิจการหรือบุคคลใด</p>
</footer>

</div>
'''


JS = u'''<!-- dr:data -->
<script>
"use strict";
const $ = s => document.querySelector(s);
const esc = s => String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;");

let DRILLS = [], GROUPS = [], cur = 0;

function boot(){
  const el = document.getElementById("dr-data");
  if(!el){ $("#list").innerHTML = '<p class="muted">ยังไม่มีข้อมูลแบบฝึกในหน้านี้</p>'; return; }
  const d = JSON.parse(el.textContent);
  DRILLS = d.drills; GROUPS = d.groups;
  $("#tabs").innerHTML = GROUPS.map((g,i) =>
    `<button type="button" data-i="${i}" aria-pressed="${i===cur}">${esc(g.title)}</button>`).join("");
  $("#tabs").querySelectorAll("button").forEach(b =>
    b.addEventListener("click", () => { cur = +b.dataset.i; render(); }));
  render();
}

function render(){
  $("#tabs").querySelectorAll("button").forEach(b =>
    b.setAttribute("aria-pressed", String(+b.dataset.i === cur)));
  const g = GROUPS[cur];
  $("#gdesc").textContent = g.desc;
  const items = DRILLS.filter(d => d.group === g.id);
  const framed = (g.id === "sarl" || g.id === "three");

  $("#list").innerHTML = items.map(d => {
    const n = d.box.length;
    const opts = ['<option value="">\\u2014</option>']
      .concat([...d.box].sort((a,b)=>a.localeCompare(b)).map(w => `<option>${esc(w)}</option>`)).join("");
    const blocks = d.blocks.map(b => {
      const html = esc(b.t).replace(/\\[\\[(\\d+)\\]\\]/g, (m,k) =>
        `<span class="blank"><span class="n">(${k})</span><select id="${d.id}-${k}" aria-label="ช่องที่ ${k}">${opts}</select></span>`);
      return `<div class="blk">${b.label ? `<div class="lb">${esc(b.label)}</div>` : ""}<div>${html}</div></div>`;
    }).join("");
    return `<section class="ex" id="ex-${d.id}">
      <div class="ex-head"><h2>${esc(d.title)}</h2><span class="pts">${n} ช่อง</span></div>
      <div class="box" id="box-${d.id}">${d.box.map(w =>
        `<span class="chip" data-w="${esc(w)}">${esc(w)}</span>`).join("")}</div>
      <div class="body ${framed ? "frame" : ""}" id="bd-${d.id}">${blocks}</div>
      <div class="row-btns">
        <button type="button" class="small" data-grade="${d.id}">ตรวจคำตอบ</button>
        <button type="button" class="small ghost" data-clear="${d.id}">ล้างคำตอบ</button>
        <span class="sc" id="sc-${d.id}">\\u2013 / ${n}</span>
      </div>
      <div class="key" id="key-${d.id}"></div>
    </section>`;
  }).join("");

  items.forEach(d => {
    const bd = document.getElementById("bd-" + d.id);
    bd.addEventListener("change", () => markUsed(d));
  });
  $("#list").querySelectorAll("[data-grade]").forEach(b =>
    b.addEventListener("click", () => grade(items.find(x => x.id === b.dataset.grade))));
  $("#list").querySelectorAll("[data-clear]").forEach(b =>
    b.addEventListener("click", () => clear(items.find(x => x.id === b.dataset.clear))));
  window.scrollTo({top:0, behavior:"instant"});
}

function markUsed(d){
  const used = new Set();
  for(let i=1;i<=d.box.length;i++){
    const v = document.getElementById(d.id+"-"+i).value;
    if(v) used.add(v);
  }
  document.querySelectorAll("#box-"+d.id+" .chip").forEach(c =>
    c.classList.toggle("used", used.has(c.dataset.w)));
}

function grade(d){
  let sc = 0; const rows = [];
  for(let i=1;i<=d.box.length;i++){
    const sel = document.getElementById(d.id+"-"+i);
    const want = d.ans[String(i)];
    const ok = sel.value === want;
    sel.classList.toggle("ok", ok);
    sel.classList.toggle("bad", !ok);
    if(ok) sc++;
    const mine = (!ok && sel.value) ? ` <span class="muted">(คุณตอบ: ${esc(sel.value)})</span>` : "";
    rows.push(`<div class="r"><span class="n">(${i})</span><span>${ok?"\\u2713":"\\u2717"} <b>${esc(want)}</b>${mine} \\u2014 ${d.exp[String(i)]}</span></div>`);
  }
  document.getElementById("sc-"+d.id).textContent = sc + " / " + d.box.length;
  const key = document.getElementById("key-"+d.id);
  key.innerHTML = rows.join("");
  key.classList.add("on");
}

function clear(d){
  for(let i=1;i<=d.box.length;i++){
    const sel = document.getElementById(d.id+"-"+i);
    sel.value = ""; sel.classList.remove("ok","bad");
  }
  document.getElementById("sc-"+d.id).textContent = "\\u2013 / " + d.box.length;
  document.getElementById("key-"+d.id).classList.remove("on");
  markUsed(d);
}

if(document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot);
else boot();
</script>
'''


HUB_START = u'<!-- drills:link:start -->'
HUB_END = u'<!-- drills:link:end -->'
HUB_RE = re.compile(re.escape(HUB_START) + r'.*?' + re.escape(HUB_END), re.S)
HUB_ANCHOR = u'<!-- sets:link:end -->'


def patch_hub():
    if not os.path.exists(HUB):
        print(u'  ไม่พบ oral-eng/index.html จึงยังไม่ได้ใส่ลิงก์')
        return
    html = io.open(HUB, encoding='utf-8').read()
    link = (HUB_START + u'\n      <a class="final-link" href="drills.html">'
            u'แบบฝึกตามรูปแบบข้อสอบ · เติมคำ · SAR+L · Three S&rsquo;s &rarr;</a>\n' + HUB_END)
    if HUB_RE.search(html):
        new = HUB_RE.sub(lambda m: link, html)
    else:
        at = html.find(HUB_ANCHOR)
        if at < 0:
            print(u'  หาจุดใส่ลิงก์ในหน้าวิชาไม่เจอ')
            return
        end = at + len(HUB_ANCHOR)
        new = html[:end] + u'\n      ' + link + html[end:]
    if new == html:
        print(u'  ลิงก์ที่หน้าวิชาเหมือนเดิม')
        return
    io.open(HUB, 'w', encoding='utf-8').write(new)
    print(u'  ใส่ลิงก์เข้าหน้านี้ที่ oral-eng/index.html แล้ว')


def payload():
    u"""ข้อมูลชุดเดียวที่ทั้งหน้าเว็บและไฟล์ Word ใช้ร่วมกัน"""
    return {
        'groups': [{'id': g[0], 'title': g[1], 'desc': g[2]} for g in GROUPS],
        'drills': [{'id': d['id'], 'group': d['group'], 'title': d['title'],
                    'box': list(d['box']),
                    'blocks': [{'label': b['label'], 't': b['t']} for b in d['blocks']],
                    'ans': {str(k): v for k, v in d['ans'].items()},
                    'exp': {str(k): v for k, v in d['exp'].items()}} for d in DRILLS],
    }


def write_page():
    data = payload()
    block = (u'\n<script type="application/json" id="dr-data">\n'
             + json.dumps(data, ensure_ascii=False, separators=(',', ':')) + u'\n</script>\n')
    html = HEAD + BODY + block + JS
    io.open(PAGE, 'w', encoding='utf-8').write(html.rstrip(u'\n') + u'\n')
    print(u'  เขียน %s · %.0f KB' % (os.path.relpath(PAGE, ROOT), os.path.getsize(PAGE) / 1024.0))


def verify():
    html = io.open(PAGE, encoding='utf-8').read()
    m = re.search(r'id="dr-data">(.*?)</script>', html, re.S)
    if not m:
        print(u'  ตรวจแล้วไม่พบข้อมูลในหน้า')
        return 1
    page = json.loads(m.group(1))
    bad = 0
    if len(page['drills']) != len(DRILLS):
        print(u'  จำนวนแบบฝึกไม่ตรง'); bad += 1
    for a, d in zip(page['drills'], DRILLS):
        if [b['t'] for b in a['blocks']] != [b['t'] for b in d['blocks']]:
            print(u'  %s บทไม่ตรง' % d['id']); bad += 1
        if a['ans'] != {str(k): v for k, v in d['ans'].items()}:
            print(u'  %s คำตอบไม่ตรง' % d['id']); bad += 1
    gaps = sum(len(d['box']) for d in DRILLS)
    print(u'  ตรวจข้อมูลในหน้าเทียบกับไฟล์ข้อมูล · พบไม่ตรง %d จุด' % bad)
    print(u'  แบบฝึก %d ชุด · ช่องว่างรวม %d ช่อง' % (len(DRILLS), gaps))
    return bad


def main():
    ap = argparse.ArgumentParser(description=u'สร้างหน้าแบบฝึกตามรูปแบบข้อสอบ')
    ap.add_argument('--check', action='store_true', help=u'ตรวจข้อมูลอย่างเดียว')
    ap.add_argument('--json', metavar='PATH',
                    help=u'เขียนข้อมูลออกเป็น JSON ให้ tools/mk-drills-doc.js ใช้ทำไฟล์ Word')
    a = ap.parse_args()

    print(u'\nตรวจข้อมูล')
    for gid, gtitle, _ in GROUPS:
        items = [d for d in DRILLS if d['group'] == gid]
        print(u'  %-9s %-34s %d ชุด · %d ช่อง'
              % (gid, gtitle, len(items), sum(len(d['box']) for d in items)))
    bad = check_data()
    print(u'  พบปัญหา %d จุด' % bad)
    if bad:
        print(u'\nข้อมูลมีปัญหา ยังไม่เขียนหน้าให้')
        return 1
    if a.json:
        io.open(a.json, 'w', encoding='utf-8').write(
            json.dumps(payload(), ensure_ascii=False))
        print(u'\nเขียนข้อมูลเป็น JSON ที่ %s แล้ว' % a.json)
        return 0
    if a.check:
        print(u'\nข้อมูลครบถ้วน พร้อมสร้างหน้า')
        return 0

    print(u'\nเขียนหน้า')
    write_page()
    patch_hub()
    return verify()


if __name__ == '__main__':
    sys.exit(main())
