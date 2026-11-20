#!/usr/bin/env python3
# -*- coding: utf-8 -*-
u"""สร้างหน้าข้อสอบปลายภาควิชาหลักการตลาด  marketing/final.html

    python3 tools/mk-final.py            เขียนไฟล์จริง
    python3 tools/mk-final.py --check    ตรวจอย่างเดียว ไม่เขียนไฟล์

ต่างจากตัวสร้างบทเรียนตัวอื่นตรงที่<สคริปต์นี้เขียนทั้งไฟล์ใหม่ทุกครั้ง>
จึงไม่ต้องใช้คอมเมนต์คร่อมและไม่มีโหมด --strip
เหตุผลคือหน้านี้เป็นหน้าใหม่ที่ไม่มีใครอื่นมาแก้ ไม่ใช่การแทรกเข้าไปในหน้าที่มีอยู่

ข้อสอบ 300 ข้ออยู่ใน tools/final_q1.py ถึง tools/final_q6.py
เป็นข้อสอบชุดใหม่ทั้งหมด ไม่ซ้ำกับคลัง QS และ QS2 ในหน้า marketing/index.html

หน้านี้ตรวจตัวเองหลังสร้างว่า
  จำนวนข้อตรงกับที่ไฟล์ข้อมูลประกาศไว้ และไม่มีช่องว่างในอาร์เรย์
  ทุกข้อมีรูปร่างครบ คือมี ch t q o a e และ a ชี้ไปยังตัวเลือกที่มีอยู่จริง
  ค่า a เป็น 0 ทุกข้อ เพราะหน้าสลับลำดับตัวเลือกเอง
  ไม่มีโจทย์ซ้ำกัน และไม่มีข้อใดซ้ำกับคลังในหน้า marketing/index.html
  แท็กสมดุล และสคริปต์ของหน้าคอมไพล์ได้
"""

import argparse
import io
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGE = os.path.join(ROOT, 'marketing', 'final.html')
INDEX = os.path.join(ROOT, 'marketing', 'index.html')

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

MODULES = ['final_q%d' % i for i in range(1, 7)]

# ชื่อบทสำหรับป้ายกำกับและตัวกรอง  0 คือข้อข้ามบท
CHAPTERS = [
    (0, u'ข้ามบท', u'เชื่อมสองบทขึ้นไป'),
    (1, u'บทที่ 1', u'การตลาดคืออะไร'),
    (2, u'บทที่ 2', u'กลยุทธ์องค์กรและการตลาด'),
    (3, u'บทที่ 3', u'สภาพแวดล้อมทางการตลาด'),
    (4, u'บทที่ 4', u'สารสนเทศและการวิจัยตลาด'),
    (5, u'บทที่ 5', u'พฤติกรรมผู้บริโภค'),
    (6, u'บทที่ 6', u'กลยุทธ์ STP'),
    (7, u'บทที่ 7', u'ผลิตภัณฑ์และตราสินค้า'),
    (8, u'บทที่ 8', u'สินค้าใหม่และวงจรชีวิต'),
    (9, u'บทที่ 9', u'การตั้งราคา'),
    (10, u'บทที่ 10', u'ช่องทางการตลาด'),
    (11, u'บทที่ 11', u'ค้าปลีกและค้าส่ง'),
    (12, u'บทที่ 12', u'โฆษณาและประชาสัมพันธ์'),
    (13, u'บทที่ 13-14', u'ขายตรงและส่งเสริมการขาย'),
]

PRE = set([1, 2, 3, 4, 5, 6, 7])    # บทก่อนมิดเทอม
POST = set([8, 9, 10, 11, 12, 13])  # บทหลังมิดเทอม


def load_bank():
    u"""รวมข้อสอบจากทุกโมดูลเป็นสตริงเดียว พร้อมคืนยอดที่แต่ละไฟล์ประกาศไว้"""
    parts, want = [], 0
    for name in MODULES:
        mod = __import__(name)
        body = mod.QUIZ.strip()
        n = body.count(u'{ch:')
        if n != mod.TOTAL:
            raise SystemExit(u'%s ประกาศ TOTAL = %d แต่มีจริง %d ข้อ'
                             % (name, mod.TOTAL, n))
        parts.append(u'    /* %s */\n' % name + body)
        want += n
    return u',\n'.join(parts), want


HEAD = u"""<!doctype html>
<html lang="th">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>ข้อสอบปลายภาค · หลักการตลาด</title>
<meta name="description" content="ข้อสอบปลายภาควิชาหลักการตลาด NNN ข้อ ครอบคลุมบทที่ 1 ถึง 14 เลือกซ้อมทีละบทหรือจับเวลาทั้งชุดได้">
<style>
  :root{
    --bg:#fbfaf7; --fg:#1d1b17; --mut:#6d6a62; --line:#e2ded4;
    --card:#fff; --accent:#1f6f54; --accent-s:#e8f2ed;
    --warn:#9a5b1d; --warn-s:#fbf1e4; --bad:#9b2f2f; --bad-s:#fbeeee;
    --shadow:0 1px 2px rgba(0,0,0,.05),0 4px 14px rgba(0,0,0,.04);
  }
  @media (prefers-color-scheme:dark){
    :root:not([data-theme="light"]){
      --bg:#14150f; --fg:#eceadf; --mut:#9d9a8e; --line:#2f3128;
      --card:#1b1c15; --accent:#6cc39c; --accent-s:#16281f;
      --warn:#d8a05c; --warn-s:#2b2113; --bad:#e08c8c; --bad-s:#2d1818;
      --shadow:0 1px 2px rgba(0,0,0,.3),0 4px 14px rgba(0,0,0,.25);
    }
  }
  :root[data-theme="dark"]{
    --bg:#14150f; --fg:#eceadf; --mut:#9d9a8e; --line:#2f3128;
    --card:#1b1c15; --accent:#6cc39c; --accent-s:#16281f;
    --warn:#d8a05c; --warn-s:#2b2113; --bad:#e08c8c; --bad-s:#2d1818;
    --shadow:0 1px 2px rgba(0,0,0,.3),0 4px 14px rgba(0,0,0,.25);
  }
  *{box-sizing:border-box}
  html{-webkit-text-size-adjust:100%}
  body{
    margin:0; background:var(--bg); color:var(--fg);
    font-family:"IBM Plex Sans Thai","Noto Sans Thai",-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
    font-size:17px; line-height:1.75;
  }
  .wrap{max-width:860px; margin:0 auto; padding:0 16px 64px}
  header{padding:30px 0 18px; border-bottom:1px solid var(--line); margin-bottom:22px}
  .eyebrow{font-size:13px; letter-spacing:.09em; text-transform:uppercase; color:var(--mut)}
  h1{font-size:clamp(25px,5vw,36px); line-height:1.25; margin:.3em 0 .35em; letter-spacing:-.01em}
  .mast{color:var(--mut); font-size:15px; margin:0}
  .back{display:inline-block; margin-top:14px; font-size:15px; color:var(--accent); text-decoration:none}
  .back:hover{text-decoration:underline}
  .panel{
    background:var(--card); border:1px solid var(--line); border-radius:14px;
    padding:18px; margin:18px 0; box-shadow:var(--shadow);
  }
  .panel h2{font-size:18px; margin:0 0 10px}
  .lede{color:var(--mut); font-size:15px; margin:0 0 14px}
  .lede b{color:var(--fg)}
  .grp{margin-bottom:14px}
  .grp-h{font-size:13px; letter-spacing:.06em; text-transform:uppercase; color:var(--mut); margin-bottom:7px}
  .chips{display:flex; flex-wrap:wrap; gap:7px}
  .chip{
    appearance:none; cursor:pointer; font:inherit; font-size:14px; line-height:1.3;
    background:var(--bg); color:var(--fg); border:1px solid var(--line);
    border-radius:999px; padding:7px 13px; transition:background .12s,border-color .12s;
  }
  .chip:hover{border-color:var(--accent)}
  .chip[aria-pressed="true"]{background:var(--accent-s); border-color:var(--accent); color:var(--accent); font-weight:600}
  .chip .cnt{color:var(--mut); font-weight:400; margin-inline-start:5px; font-size:13px}
  .chip[aria-pressed="true"] .cnt{color:var(--accent)}
  .row{display:flex; flex-wrap:wrap; gap:10px; align-items:center; margin-top:4px}
  .btn{
    appearance:none; cursor:pointer; font:inherit; font-weight:600;
    background:var(--accent); color:#fff; border:1px solid var(--accent);
    border-radius:10px; padding:11px 20px;
  }
  .btn:hover{filter:brightness(1.07)}
  .btn.ghost{background:transparent; color:var(--accent)}
  .btn[disabled]{opacity:.45; cursor:not-allowed; filter:none}
  .selnote{font-size:14px; color:var(--mut)}
  .selnote b{color:var(--fg)}
  .bar{
    position:sticky; top:0; z-index:5; background:var(--bg);
    border-bottom:1px solid var(--line); padding:10px 0; margin-bottom:16px;
    display:flex; flex-wrap:wrap; gap:12px; align-items:center; font-size:15px;
  }
  .bar .sp{flex:1 1 auto}
  .meter{height:5px; background:var(--line); border-radius:999px; overflow:hidden; flex:1 1 120px; min-width:90px}
  .meter i{display:block; height:100%; background:var(--accent); width:0; transition:width .2s}
  .qn{font-size:13px; letter-spacing:.06em; text-transform:uppercase; color:var(--mut)}
  .qtag{
    display:inline-block; font-size:13px; color:var(--accent); background:var(--accent-s);
    border-radius:999px; padding:2px 11px; margin-bottom:10px;
  }
  .q{font-size:19px; line-height:1.6; margin:0 0 16px; font-weight:600}
  .q b{font-weight:700}
  .opts{display:grid; gap:9px; margin-bottom:16px}
  .opt{
    appearance:none; cursor:pointer; font:inherit; text-align:start; line-height:1.6;
    background:var(--card); color:var(--fg); border:1px solid var(--line);
    border-radius:11px; padding:13px 15px; display:flex; gap:11px; align-items:flex-start;
    transition:border-color .12s,background .12s;
  }
  .opt:hover:not([disabled]){border-color:var(--accent)}
  .opt .k{
    flex:0 0 auto; width:25px; height:25px; border-radius:50%; border:1px solid var(--line);
    display:grid; place-items:center; font-size:13px; font-weight:600; color:var(--mut);
  }
  .opt[data-state="right"]{border-color:var(--accent); background:var(--accent-s)}
  .opt[data-state="right"] .k{border-color:var(--accent); background:var(--accent); color:#fff}
  .opt[data-state="wrong"]{border-color:var(--bad); background:var(--bad-s)}
  .opt[data-state="wrong"] .k{border-color:var(--bad); background:var(--bad); color:#fff}
  .opt[disabled]{cursor:default}
  .exp{
    border:1px solid var(--line); border-inline-start:3px solid var(--accent);
    background:var(--accent-s); border-radius:10px; padding:13px 15px; font-size:15.5px; line-height:1.72;
  }
  .exp.miss{border-inline-start-color:var(--warn); background:var(--warn-s)}
  .exp .eh{display:block; font-size:13px; letter-spacing:.05em; text-transform:uppercase; color:var(--mut); margin-bottom:5px}
  .exp .en{color:var(--mut); font-size:14px}
  .nav{display:flex; gap:10px; margin-top:16px; flex-wrap:wrap}
  .score{text-align:center; padding:12px 0 4px}
  .score .big{font-size:48px; font-weight:700; line-height:1.1; letter-spacing:-.02em}
  .score .sub{color:var(--mut); font-size:15px}
  .tbl{width:100%; border-collapse:collapse; font-size:15px; margin-top:14px}
  .tbl th,.tbl td{border:1px solid var(--line); padding:8px 11px; text-align:start; vertical-align:top}
  .tbl th{background:var(--accent-s); font-weight:600}
  .tbl td.n{text-align:end; white-space:nowrap; font-variant-numeric:tabular-nums}
  .tw{overflow-x:auto; -webkit-overflow-scrolling:touch}
  .hidden{display:none !important}
  footer{margin-top:40px; padding-top:18px; border-top:1px solid var(--line); color:var(--mut); font-size:14px}
  footer a{color:var(--accent)}
  .en{font-style:normal; color:var(--mut)}
</style>
</head>
<body>
<div class="wrap">
<header>
  <div class="eyebrow">Principles of Marketing &middot; Final Exam</div>
  <h1>ข้อสอบปลายภาค · หลักการตลาด</h1>
  <p class="mast">NNN ข้อ ครอบคลุม<b>บทที่ 1 ถึง 14</b> ทั้งก่อนและหลังมิดเทอม &middot; เป็น<b>ชุดใหม่ทั้งหมด ไม่ซ้ำกับแบบทดสอบท้ายหน้าบทเรียน</b> &middot; เลือกซ้อมทีละบท หรือจับเวลาทั้งชุดก็ได้</p>
  <a class="back" href="index.html">&larr; กลับไปหน้าบทเรียน</a>
</header>
"""

SETUP = u"""
<div id="setup">
  <div class="panel">
    <h2>เลือกขอบเขตที่จะทำ</h2>
    <p class="lede">กดเลือกบทที่ต้องการ กดซ้ำเพื่อเอาออก &middot; <b>ลำดับข้อและลำดับตัวเลือกสลับใหม่ทุกครั้งที่เริ่มทำ</b> จึงจำตำแหน่งเฉลยไม่ได้</p>
    <div class="grp">
      <div class="grp-h">เลือกเร็ว</div>
      <div class="chips" role="group" aria-label="เลือกขอบเขตแบบรวดเร็ว">
        <button type="button" class="chip" data-quick="all" aria-pressed="false">ทั้งหมด</button>
        <button type="button" class="chip" data-quick="pre" aria-pressed="false">เฉพาะก่อนมิดเทอม</button>
        <button type="button" class="chip" data-quick="post" aria-pressed="false">เฉพาะหลังมิดเทอม</button>
        <button type="button" class="chip" data-quick="none" aria-pressed="false">ล้างที่เลือก</button>
      </div>
    </div>
    <div class="grp">
      <div class="grp-h">เลือกทีละบท</div>
      <div class="chips" id="chapchips" role="group" aria-label="เลือกบท"></div>
    </div>
    <div class="grp">
      <div class="grp-h">จำนวนข้อ</div>
      <div class="chips" role="group" aria-label="เลือกจำนวนข้อ">
        <button type="button" class="chip" data-size="20" aria-pressed="false">20 ข้อ</button>
        <button type="button" class="chip" data-size="40" aria-pressed="true">40 ข้อ</button>
        <button type="button" class="chip" data-size="60" aria-pressed="false">60 ข้อ</button>
        <button type="button" class="chip" data-size="0" aria-pressed="false">ทุกข้อที่เลือก</button>
      </div>
    </div>
    <div class="grp">
      <div class="grp-h">รูปแบบ</div>
      <div class="chips" role="group" aria-label="เลือกรูปแบบการทำ">
        <button type="button" class="chip" data-mode="learn" aria-pressed="true">เฉลยทันทีทีละข้อ</button>
        <button type="button" class="chip" data-mode="exam" aria-pressed="false">จับเวลา เฉลยตอนจบ</button>
      </div>
    </div>
    <div class="row">
      <button type="button" class="btn" id="start">เริ่มทำข้อสอบ</button>
      <span class="selnote" id="selnote"></span>
    </div>
  </div>

  <div class="panel">
    <h2>สัดส่วนข้อสอบแต่ละบท</h2>
    <p class="lede">บทหลังมิดเทอมมีสัดส่วนมากกว่า เพราะข้อสอบปลายภาคเน้นช่วงหลังเป็นหลัก</p>
    <div class="tw"><table class="tbl">
      <thead><tr><th>บท</th><th>หัวข้อ</th><th class="n">จำนวนข้อ</th></tr></thead>
      <tbody id="mixrows"></tbody>
    </table></div>
  </div>
</div>

<div id="run" class="hidden">
  <div class="bar">
    <span class="qn" id="pos">ข้อที่ 1</span>
    <div class="meter"><i id="meter"></i></div>
    <span class="qn" id="clock"></span>
    <span class="sp"></span>
    <button type="button" class="btn ghost" id="quit">ออก</button>
  </div>
  <div class="panel">
    <span class="qtag" id="qtag"></span>
    <p class="q" id="qtext"></p>
    <div class="opts" id="opts"></div>
    <div id="expwrap"></div>
    <div class="nav">
      <button type="button" class="btn ghost" id="prev">ข้อก่อนหน้า</button>
      <button type="button" class="btn" id="next">ข้อถัดไป</button>
    </div>
  </div>
</div>

<div id="done" class="hidden">
  <div class="panel">
    <div class="score">
      <div class="big" id="sc">0</div>
      <div class="sub" id="scsub"></div>
    </div>
    <div class="row" style="justify-content:center">
      <button type="button" class="btn" id="again">ทำชุดใหม่</button>
      <button type="button" class="btn ghost" id="review">ดูเฉลยทุกข้อ</button>
    </div>
  </div>
  <div class="panel">
    <h2>ผลแยกตามบท</h2>
    <div class="tw"><table class="tbl">
      <thead><tr><th>บท</th><th class="n">ถูก</th><th class="n">ทำไป</th><th class="n">ร้อยละ</th></tr></thead>
      <tbody id="byrows"></tbody>
    </table></div>
  </div>
  <div id="reviewwrap"></div>
</div>

<footer>
  <p><b>ข้อสอบปลายภาค หลักการตลาด</b> &mdash; NNN ข้อ เขียนขึ้นจากเนื้อหาในหน้าบทเรียนของวิชานี้ อ้างอิงตำรา Kotler &amp; Armstrong, <i>Principles of Marketing</i> (Pearson Education) &middot; ชุดนี้เป็น<b>ข้อสอบคนละชุดกับแบบทดสอบท้ายหน้าบทเรียน</b> จึงใช้ซ้อมต่อจากกันได้โดยไม่เจอข้อซ้ำ &middot; <b>เฉลยทุกข้อมีคำอธิบายกำกับ</b> ว่าทำไมตัวเลือกนั้นถูกและตัวเลือกอื่นผิดตรงไหน</p>
  <p>ข้อสอบชุดนี้เป็น<b>แบบฝึกหัดที่จัดทำขึ้นเพื่อการทบทวน</b> ไม่ใช่ข้อสอบจริงของรายวิชา และไม่ได้มาจากคลังข้อสอบของผู้สอน &middot; <a href="index.html">กลับไปหน้าบทเรียน</a></p>
</footer>
</div>
"""

SCRIPT_TAIL = u"""
<script>
(function(){
  var CH = CHAPDATA;
  var LAB = {}, SUB = {};
  CH.forEach(function(c){ LAB[c[0]] = c[1]; SUB[c[0]] = c[2]; });

  var picked = {}, size = 40, mode = 'learn';
  var order = [], cur = 0, answers = [], t0 = 0, timer = null;

  function $(id){ return document.getElementById(id); }
  function esc(s){ return String(s); }

  /* ---- หน้าตั้งค่า ---- */
  var chipbox = $('chapchips'), rows = $('mixrows');
  CH.forEach(function(c){
    var n = BANK.filter(function(it){ return it.ch === c[0]; }).length;
    if (!n) return;
    var b = document.createElement('button');
    b.type = 'button'; b.className = 'chip'; b.setAttribute('aria-pressed','false');
    b.dataset.ch = c[0];
    b.innerHTML = c[1] + '<span class="cnt">' + n + '</span>';
    b.addEventListener('click', function(){
      if (picked[c[0]]) { delete picked[c[0]]; } else { picked[c[0]] = 1; }
      paint();
    });
    chipbox.appendChild(b);
    var tr = document.createElement('tr');
    tr.innerHTML = '<td><b>' + c[1] + '</b></td><td>' + c[2] + '</td><td class="n">' + n + '</td>';
    rows.appendChild(tr);
  });

  function pool(){
    return BANK.filter(function(it){ return picked[it.ch]; });
  }
  function paint(){
    Array.prototype.forEach.call(chipbox.children, function(b){
      b.setAttribute('aria-pressed', picked[+b.dataset.ch] ? 'true' : 'false');
    });
    var n = pool().length;
    var take = size ? Math.min(size, n) : n;
    $('selnote').innerHTML = n
      ? 'เลือกไว้ <b>' + n + '</b> ข้อ จะสุ่มมา <b>' + take + '</b> ข้อ'
      : 'ยังไม่ได้เลือกบท';
    $('start').disabled = !n;
  }
  document.querySelectorAll('[data-quick]').forEach(function(b){
    b.addEventListener('click', function(){
      var k = b.dataset.quick;
      picked = {};
      CH.forEach(function(c){
        var id = c[0];
        if (k === 'all') picked[id] = 1;
        else if (k === 'pre' && PRE.indexOf(id) >= 0) picked[id] = 1;
        else if (k === 'post' && POST.indexOf(id) >= 0) picked[id] = 1;
      });
      paint();
    });
  });
  document.querySelectorAll('[data-size]').forEach(function(b){
    b.addEventListener('click', function(){
      size = +b.dataset.size;
      document.querySelectorAll('[data-size]').forEach(function(o){
        o.setAttribute('aria-pressed', o === b ? 'true' : 'false');
      });
      paint();
    });
  });
  document.querySelectorAll('[data-mode]').forEach(function(b){
    b.addEventListener('click', function(){
      mode = b.dataset.mode;
      document.querySelectorAll('[data-mode]').forEach(function(o){
        o.setAttribute('aria-pressed', o === b ? 'true' : 'false');
      });
    });
  });

  /* ---- สุ่ม ---- */
  function shuffle(a){
    for (var i = a.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var t = a[i]; a[i] = a[j]; a[j] = t;
    }
    return a;
  }

  /* ---- เริ่มทำ ---- */
  $('start').addEventListener('click', function(){
    var p = shuffle(pool().slice());
    if (size) p = p.slice(0, size);
    order = p.map(function(it){
      var idx = it.o.map(function(_, i){ return i; });
      shuffle(idx);
      return { it: it, idx: idx, pick: -1 };
    });
    cur = 0; answers = [];
    $('setup').classList.add('hidden');
    $('done').classList.add('hidden');
    $('run').classList.remove('hidden');
    t0 = Date.now();
    if (timer) clearInterval(timer);
    timer = setInterval(tick, 1000);
    tick();
    show();
    window.scrollTo(0, 0);
  });
  function tick(){
    var s = Math.floor((Date.now() - t0) / 1000);
    var m = Math.floor(s / 60);
    $('clock').textContent = m + ':' + (s % 60 < 10 ? '0' : '') + (s % 60);
  }

  function show(){
    var row = order[cur], it = row.it;
    $('pos').textContent = 'ข้อที่ ' + (cur + 1) + ' จาก ' + order.length;
    $('meter').style.width = ((cur) / order.length * 100) + '%';
    $('qtag').textContent = LAB[it.ch] + ' · ' + it.t;
    $('qtext').innerHTML = it.q;
    var box = $('opts'); box.innerHTML = '';
    var keys = 'กขคง จฉชญ';
    row.idx.forEach(function(oi, slot){
      var b = document.createElement('button');
      b.type = 'button'; b.className = 'opt';
      b.innerHTML = '<span class="k">' + keys.charAt(slot) + '</span><span>' + it.o[oi] + '</span>';
      if (row.pick >= 0) {
        b.disabled = true;
        if (mode === 'learn') {
          if (oi === it.a) b.dataset.state = 'right';
          else if (slot === row.pick) b.dataset.state = 'wrong';
        } else if (slot === row.pick) {
          b.dataset.state = 'right';
        }
      }
      b.addEventListener('click', function(){ answer(slot, oi); });
      box.appendChild(b);
    });
    var w = $('expwrap'); w.innerHTML = '';
    if (row.pick >= 0 && mode === 'learn') explain(w, row);
    $('prev').disabled = cur === 0;
    $('next').textContent = cur === order.length - 1 ? 'ส่งคำตอบ' : 'ข้อถัดไป';
  }
  function explain(w, row){
    var ok = row.idx[row.pick] === row.it.a;
    var d = document.createElement('div');
    d.className = 'exp' + (ok ? '' : ' miss');
    d.innerHTML = '<span class="eh">' + (ok ? 'ถูกต้อง' : 'ยังไม่ใช่') + '</span>' + row.it.e;
    w.appendChild(d);
  }
  function answer(slot, oi){
    var row = order[cur];
    if (row.pick >= 0) return;
    row.pick = slot;
    show();
    if (mode === 'exam' && cur < order.length - 1) {
      setTimeout(function(){ cur++; show(); window.scrollTo(0, 0); }, 160);
    }
  }
  $('prev').addEventListener('click', function(){
    if (cur > 0) { cur--; show(); window.scrollTo(0, 0); }
  });
  $('next').addEventListener('click', function(){
    if (cur < order.length - 1) { cur++; show(); window.scrollTo(0, 0); }
    else finish();
  });
  $('quit').addEventListener('click', function(){
    if (timer) clearInterval(timer);
    $('run').classList.add('hidden');
    $('setup').classList.remove('hidden');
    window.scrollTo(0, 0);
  });

  /* ---- สรุปผล ---- */
  function finish(){
    if (timer) clearInterval(timer);
    var right = 0, by = {};
    order.forEach(function(row){
      var ch = row.it.ch;
      by[ch] = by[ch] || { r: 0, n: 0 };
      by[ch].n++;
      if (row.pick >= 0 && row.idx[row.pick] === row.it.a) { right++; by[ch].r++; }
    });
    var pct = Math.round(right / order.length * 100);
    $('sc').textContent = right + ' / ' + order.length;
    var s = Math.floor((Date.now() - t0) / 1000);
    $('scsub').innerHTML = 'คิดเป็น <b>' + pct + '%</b> · ใช้เวลา <b>'
      + Math.floor(s / 60) + ' นาที ' + (s % 60) + ' วินาที</b>';
    var tb = $('byrows'); tb.innerHTML = '';
    CH.forEach(function(c){
      var b = by[c[0]];
      if (!b) return;
      var tr = document.createElement('tr');
      tr.innerHTML = '<td><b>' + c[1] + '</b></td><td class="n">' + b.r
        + '</td><td class="n">' + b.n + '</td><td class="n">'
        + Math.round(b.r / b.n * 100) + '%</td>';
      tb.appendChild(tr);
    });
    $('reviewwrap').innerHTML = '';
    $('run').classList.add('hidden');
    $('done').classList.remove('hidden');
    window.scrollTo(0, 0);
  }
  $('again').addEventListener('click', function(){
    $('done').classList.add('hidden');
    $('setup').classList.remove('hidden');
    window.scrollTo(0, 0);
  });
  $('review').addEventListener('click', function(){
    var w = $('reviewwrap');
    if (w.innerHTML) { w.innerHTML = ''; return; }
    order.forEach(function(row, i){
      var ok = row.pick >= 0 && row.idx[row.pick] === row.it.a;
      var p = document.createElement('div');
      p.className = 'panel';
      var mine = row.pick >= 0 ? row.it.o[row.idx[row.pick]] : 'ไม่ได้ตอบ';
      p.innerHTML = '<span class="qtag">ข้อ ' + (i + 1) + ' · ' + LAB[row.it.ch]
        + ' · ' + row.it.t + '</span><p class="q">' + row.it.q + '</p>'
        + '<div class="exp' + (ok ? '' : ' miss') + '">'
        + '<span class="eh">' + (ok ? 'ตอบถูก' : 'ตอบผิด') + '</span>'
        + '<div class="en">คำตอบของคุณ · ' + mine + '</div>'
        + '<div class="en">คำตอบที่ถูก · ' + row.it.o[row.it.a] + '</div><br>'
        + row.it.e + '</div>';
      w.appendChild(p);
    });
    w.scrollIntoView({ behavior: 'smooth' });
  });

  paint();
})();
</script>
</body>
</html>
"""


def build():
    bank, want = load_bank()
    chapdata = u'[' + u','.join(
        u'[%d,%s,%s]' % (n, js(a), js(b)) for n, a, b in CHAPTERS) + u']'
    pre = u'[' + u','.join(str(i) for i in sorted(PRE)) + u']'
    post = u'[' + u','.join(str(i) for i in sorted(POST)) + u']'

    html = HEAD + SETUP
    html += (u'<script>\n  var BANK = [\n' + bank + u'\n  ];\n'
             u'  var CHAPDATA = ' + chapdata + u';\n'
             u'  var PRE = ' + pre + u';\n'
             u'  var POST = ' + post + u';\n</script>\n')
    html += SCRIPT_TAIL.replace(u'CHAPDATA', u'CHAPDATA')
    html = html.replace(u'NNN', u'%d' % want)
    return html, want


def js(s):
    return u"'" + s.replace(u"'", u"&rsquo;") + u"'"


def bank_shape(html, want):
    u"""ให้ node ประเมินคลังข้อสอบจริง แล้วคืนความยาว ช่องว่าง และข้อที่รูปร่างผิด"""
    node = '/opt/node22/bin/node'
    if not os.path.exists(node):
        return None
    m = re.search(r'(var BANK = \[.*?\n  \];)', html, re.S)
    if not m:
        print(u'  หาคลัง BANK ไม่เจอ')
        return -1
    src = m.group(1) + u"""
var holes = 0, bad = [], seen = {}, dup = [];
for (var i = 0; i < BANK.length; i++) {
  var it = BANK[i];
  if (it === undefined) { holes++; continue; }
  var why = [];
  if (typeof it.q !== 'string' || !it.q) why.push('q');
  if (typeof it.e !== 'string' || !it.e) why.push('e');
  if (typeof it.t !== 'string' || !it.t) why.push('t');
  if (typeof it.ch !== 'number') why.push('ch');
  if (!Array.isArray(it.o) || it.o.length < 2) why.push('o');
  else if (it.a !== 0) why.push('a-ไม่ใช่ศูนย์');
  else if (it.o.some(function (x) { return typeof x !== 'string' || !x; })) why.push('o-ว่าง');
  else if (new Set(it.o).size !== it.o.length) why.push('o-ซ้ำ');
  if (why.length) bad.push((i + 1) + ':' + why.join('/'));
  var k = it.q.replace(/<[^>]+>/g, '').trim();
  if (seen[k]) dup.push((i + 1) + ' ซ้ำกับ ' + seen[k]); else seen[k] = i + 1;
}
console.log(JSON.stringify({n: BANK.length, holes: holes, bad: bad, dup: dup}));
"""
    with tempfile.NamedTemporaryFile('w', suffix='.js', delete=False, encoding='utf-8') as f:
        f.write(src)
        path = f.name
    r = subprocess.run([node, path], capture_output=True, text=True)
    os.unlink(path)
    if r.returncode:
        print(u'  คลัง BANK รันไม่ผ่าน · %s' % r.stderr.strip().split('\n')[0])
        return -1
    import json
    d = json.loads(r.stdout)
    bad = 0
    if d['holes']:
        print(u'  คลังมีช่องว่างในอาร์เรย์ %d ช่อง' % d['holes']); bad += 1
    if d['bad']:
        print(u'  ข้อที่รูปร่างผิด · %s' % u' '.join(d['bad'][:8])); bad += 1
    if d['dup']:
        print(u'  โจทย์ซ้ำกันเอง · %s' % u' '.join(d['dup'][:8])); bad += 1
    if d['n'] != want:
        print(u'  คลังมี %d ข้อ แต่ไฟล์ข้อมูลรวมได้ %d ข้อ' % (d['n'], want)); bad += 1
    if not bad:
        print(u'  คลัง %d ข้อ · รันแล้วได้ %d ข้อ ไม่มีช่องว่าง ไม่มีข้อซ้ำ รูปร่างครบทุกข้อ'
              % (want, d['n']))
    return bad


def check_dup_with_index(html):
    u"""ข้อในหน้านี้ต้องไม่ซ้ำกับคลัง QS และ QS2 ของหน้าบทเรียน"""
    if not os.path.exists(INDEX):
        print(u'  ไม่พบ marketing/index.html จึงข้ามการเทียบข้อซ้ำ')
        return 0

    def stems(text):
        out = set()
        for m in re.finditer(r"\{ch:[^,]+,(?:\s*t:'[^']*',)?\s*q:'(.*?)',\s*\n", text, re.S):
            s = re.sub(r'<[^>]+>', u'', m.group(1))
            s = re.sub(r'&[a-z]+;', u'"', s).strip()
            if s:
                out.add(s)
        return out

    idx = io.open(INDEX, encoding='utf-8').read()
    old = set()
    for name in ('QS', 'QS2'):
        m = re.search(r'var %s = \[(.*?)\n  \];' % name, idx, re.S)
        if m:
            old |= stems(m.group(1))
    m = re.search(r'var BANK = \[(.*?)\n  \];', html, re.S)
    mine = stems(m.group(1)) if m else set()
    hit = sorted(old & mine)
    if hit:
        print(u'  มี %d ข้อที่ซ้ำกับคลังในหน้าบทเรียน · %s' % (len(hit), hit[0][:60]))
        return 1
    print(u'  เทียบกับคลังเดิม %d ข้อในหน้าบทเรียนแล้ว ไม่มีข้อซ้ำ' % len(old))
    return 0


def check_js(html):
    blocks = [m.group(1) for m in re.finditer(r'<script>(.*?)</script>', html, re.S)]
    node = '/opt/node22/bin/node'
    if not os.path.exists(node):
        print(u'  ไม่มี node ในเครื่อง ข้ามการตรวจไวยากรณ์สคริปต์')
        return 0
    bad = 0
    for i, b in enumerate(blocks):
        with tempfile.NamedTemporaryFile('w', suffix='.js', delete=False, encoding='utf-8') as f:
            f.write(b)
            path = f.name
        r = subprocess.run([node, '--check', path], capture_output=True, text=True)
        os.unlink(path)
        if r.returncode:
            print(u'  สคริปต์ก้อนที่ %d พัง · %s' % (i + 1, r.stderr.strip().split('\n')[0]))
            bad += 1
    return bad


def verify(html, want):
    bad = 0

    # ตัวยึดที่สคริปต์ของหน้าเรียกหา ต้องมีอยู่จริงทุกตัว
    need = ['chapchips', 'mixrows', 'selnote', 'start', 'setup', 'run', 'done',
            'pos', 'meter', 'clock', 'quit', 'qtag', 'qtext', 'opts', 'expwrap',
            'prev', 'next', 'sc', 'scsub', 'byrows', 'again', 'review', 'reviewwrap']
    for i in need:
        if ('id="%s"' % i) not in html:
            print(u'  ไม่มีอิลิเมนต์ id="%s" ที่สคริปต์เรียกหา' % i); bad += 1

    if u'NNN' in html:
        print(u'  ยังมีที่วางตัวเลขที่ไม่ได้แทนค่า NNN ค้างอยู่'); bad += 1

    for tag in ['table', 'tbody', 'thead', 'header', 'footer', 'style', 'script']:
        o = len(re.findall(r'<%s[\s>]' % tag, html))
        c = len(re.findall(r'</%s>' % tag, html))
        if o != c:
            print(u'  แท็ก %s ไม่สมดุล เปิด %d ปิด %d' % (tag, o, c)); bad += 1
    od = len(re.findall(r'<div[\s>]', html))
    cd = len(re.findall(r'</div>', html))
    if od != cd:
        print(u'  แท็ก div ไม่สมดุล เปิด %d ปิด %d' % (od, cd)); bad += 1

    n = bank_shape(html, want)
    if n:
        bad += (1 if n > 0 else 1)
    bad += check_dup_with_index(html)
    bad += check_js(html)

    import collections
    cnt = collections.Counter(int(x) for x in re.findall(r'\{ch:(\d+),', html))
    print(u'  ต่อบท · ' + u' · '.join(
        u'%s %d' % (dict((c[0], c[1]) for c in CHAPTERS)[k], cnt[k]) for k in sorted(cnt)))
    return bad


# ลิงก์จากหน้าบทเรียนมาหน้านี้ สคริปต์นี้เป็นเจ้าของ เพราะเป็นเจ้าของหน้าปลายทาง
# คร่อมด้วยคอมเมนต์เพื่อให้รันซ้ำได้ไม่ซ้อน และให้เห็นชัดว่าใครเป็นคนวาง
LINK_ANCHOR = u'      Pearson Education\n'


def link_block(want):
    return (u'<!-- final:link:start -->      <br><a href="final.html"><b>'
            u'ข้อสอบปลายภาค %d ข้อ &rarr;</b></a>\n<!-- final:link:end -->' % want)


def patch_index(want):
    u"""วางลิงก์ไปหน้าข้อสอบปลายภาคไว้ใต้ชื่อตำราในหัวของหน้าบทเรียน"""
    if not os.path.exists(INDEX):
        print(u'  ไม่พบ marketing/index.html จึงไม่ได้วางลิงก์')
        return 0
    html = io.open(INDEX, encoding='utf-8').read()
    body = link_block(want)
    old = re.search(r'<!-- final:link:start -->.*?<!-- final:link:end -->', html, re.S)
    if old:
        if old.group(0) == body:
            print(u'  ลิงก์ในหน้าบทเรียนตรงอยู่แล้ว ไม่ต้องแก้')
            return 0
        html = html[:old.start()] + body + html[old.end():]
    else:
        if html.count(LINK_ANCHOR) != 1:
            raise SystemExit(u'หาจุดยึดของลิงก์ในหน้าบทเรียนไม่เจอ หรือเจอมากกว่าหนึ่งที่ (%d)'
                             % html.count(LINK_ANCHOR))
        html = html.replace(LINK_ANCHOR, LINK_ANCHOR + body)
    if u'href="final.html"' not in html:
        raise SystemExit(u'วางลิงก์แล้วแต่หาไม่เจอในหน้า')
    io.open(INDEX, 'w', encoding='utf-8').write(html)
    print(u'  วางลิงก์ไปหน้าข้อสอบปลายภาคในหน้าบทเรียนแล้ว')
    return 1


def main():
    ap = argparse.ArgumentParser(description=u'สร้างหน้าข้อสอบปลายภาควิชาหลักการตลาด')
    ap.add_argument('--check', action='store_true', help=u'ตรวจอย่างเดียว ไม่เขียนไฟล์')
    a = ap.parse_args()

    html, want = build()
    print(u'สร้างหน้า %d ข้อ · %d อักษร' % (want, len(html)))
    bad = verify(html, want)
    if bad:
        print(u'\nตรวจพบปัญหา %d จุด จึงยังไม่เขียนไฟล์' % bad)
        return 1
    if a.check:
        print(u'\nตรวจผ่าน · ยังไม่เขียนไฟล์เพราะสั่ง --check')
        return 0
    io.open(PAGE, 'w', encoding='utf-8').write(html)
    print(u'\nเขียน %s แล้ว' % os.path.relpath(PAGE, ROOT))
    patch_index(want)
    return 0


if __name__ == '__main__':
    sys.exit(main())
