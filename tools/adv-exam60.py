#!/usr/bin/env python3
# -*- coding: utf-8 -*-
u"""เพิ่มแท็บข้อสอบจำลอง 20 ข้อ 60 นาที ของเอกสาร Ch4_3

    python3 tools/adv-exam60.py            แทรกจริง
    python3 tools/adv-exam60.py --check    ตรวจอย่างเดียว ไม่เขียนไฟล์

ต่างจากสามแท็บที่มีอยู่แล้วตรงที่ชุดนี้เป็น โหมดสอบ ไม่ใช่โหมดฝึก
  Q   แบบทดสอบรวมทุกบท        เฉลยทันทีที่เลือกคำตอบ
  Q2  เน้นแนวคิดหลังมิดเทอม    เฉลยทันที
  Q3  ควิซชีท 4_3 ไล่ระดับ     เฉลยทันที
  Q4  ข้อสอบจำลอง 60 นาที      ปิดเฉลยไว้จนกว่าจะส่งคำตอบ

เหตุผลที่ปิดเฉลยไว้ เพราะถ้าเฉลยโผล่ทันทีจะวัดไม่ได้ว่าทำทันเวลาไหม
และผู้สอบจะเรียนรู้คำตอบระหว่างทางจนคะแนนไม่สะท้อนความพร้อมจริง

เครื่องเล่นของแท็บนี้แยกจาก mountQuiz เพราะพฤติกรรมต่างกันคนละเรื่อง
มีนาฬิกานับถอยหลัง เปลี่ยนคำตอบได้จนกว่าจะส่ง ตรวจทีเดียวตอนจบ
และหมดเวลาแล้วส่งให้อัตโนมัติ

รันซ้ำได้ไม่ซ้อน เพราะคร่อมของที่เพิ่มด้วยคอมเมนต์หัวท้าย
"""

import argparse
import io
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGE = os.path.join(ROOT, 'adv-acctg-1', 'index.html')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def mark(k):
    return (u'<!-- exam60:%s:start -->' % k, u'<!-- exam60:%s:end -->' % k)


def jsmark(k):
    return (u'/* exam60:%s:start */' % k, u'/* exam60:%s:end */' % k)


def splice(html, key, block, anchor, comment=True, before=True):
    u"""วางบล็อกคร่อมคอมเมนต์หัวท้าย ถ้ามีอยู่แล้วให้แทนที่ของเดิม ไม่ใช่ข้ามไป"""
    s, e = (mark(key) if comment else jsmark(key))
    body = s + block + e
    old = re.search(re.escape(s) + r'.*?' + re.escape(e), html, re.S)
    if old:
        if old.group(0) == body:
            return html, 0
        return html[:old.start()] + body + html[old.end():], 1
    if html.count(anchor) != 1:
        raise SystemExit(u'หาจุดยึดของ %s ไม่เจอ หรือเจอมากกว่าหนึ่งที่ (%d)'
                         % (key, html.count(anchor)))
    return (html.replace(anchor, body + anchor) if before
            else html.replace(anchor, anchor + body)), 1


# ───────────────────────── ส่วนที่ 1 · CSS ─────────────────────────

CSS = u"""
/* แถบนาฬิกาของข้อสอบจำลอง เกาะอยู่ใต้แถบแท็บ */
.exbar{position:sticky; top:53px; z-index:30; background:var(--surface-2); border:1px solid var(--rule);
  border-radius:10px; padding:12px 18px; margin-bottom:18px; display:flex; flex-wrap:wrap;
  gap:12px 20px; align-items:center; justify-content:space-between}
.exclock{font-family:"IBM Plex Mono",monospace; font-size:1.5rem; font-weight:600;
  font-variant-numeric:tabular-nums; letter-spacing:.02em}
.exclock.warn{color:var(--amber)}
.exclock.danger{color:var(--red)}
.exbar .exinfo{font-size:.85rem; color:var(--ink-2)}
.exbar .exinfo b{color:var(--ink)}
.exbtns{display:flex; flex-wrap:wrap; gap:8px}
.exbtns button{appearance:none; font:inherit; font-size:.85rem; font-weight:600; cursor:pointer;
  padding:8px 18px; border-radius:999px; border:1px solid var(--rule-strong);
  background:var(--paper); color:var(--ink-2)}
.exbtns button:hover:not(:disabled){border-color:var(--accent); color:var(--accent)}
.exbtns button:disabled{opacity:.45; cursor:default}
.exbtns button.go{background:var(--accent); border-color:var(--accent); color:var(--paper)}
.exbtns button.go:hover:not(:disabled){filter:brightness(1.08); color:var(--paper)}
/* ตัวเลือกระหว่างทำข้อสอบ ยังไม่บอกถูกผิด บอกแค่ว่าเลือกไว้แล้ว */
.opt.picked{border-color:var(--accent); background:var(--accent-soft); color:var(--ink); font-weight:600}
/* กล่องสรุปคะแนนหลังส่งคำตอบ */
.exresult{border:1px solid var(--rule-strong); border-radius:10px; background:var(--surface);
  padding:20px 22px; margin-bottom:20px}
.exresult .rbig{font-family:"IBM Plex Mono",monospace; font-size:2rem; font-weight:600;
  font-variant-numeric:tabular-nums; color:var(--accent)}
.exresult .rline{font-size:.9rem; color:var(--ink-2); margin-top:6px}
.exresult .rline b{color:var(--ink)}
.exbreak{display:flex; flex-wrap:wrap; gap:8px; margin-top:14px}
.exbreak span{font-size:.8rem; padding:4px 12px; border-radius:999px;
  background:var(--sunk); border:1px solid var(--rule); color:var(--ink-2)}
/* ซ่อนข้อสอบไว้จนกว่าจะกดเริ่ม จะได้ไม่เผลออ่านโจทย์ก่อนจับเวลา */
#ex60-list[data-state="idle"]{display:none}
.exintro{border-left:3px solid var(--accent); background:var(--accent-soft); padding:14px 18px;
  border-radius:0 6px 6px 0; margin-bottom:18px; font-size:.9rem; color:var(--ink-2); max-width:72ch}
.exintro b{color:var(--ink)}
@media (max-width:560px){ .exbar{top:49px; padding:11px 14px} .exclock{font-size:1.3rem} }"""


def patch_css(html):
    anchor = u'.expl{'
    i = html.find(anchor)
    if i < 0:
        raise SystemExit(u'หาจุดยึดของ CSS ไม่เจอ')
    s, e = jsmark('css')
    body = s + CSS + u'\n' + e
    old = re.search(re.escape(s) + r'.*?' + re.escape(e), html, re.S)
    if old:
        return (html, 0) if old.group(0) == body else (html[:old.start()] + body + html[old.end():], 1)
    return html[:i] + body + u'\n' + html[i:], 1


# ───────────────────── ส่วนที่ 2 · แท็บ แถบข้าง แผง ─────────────────────

TAB = (u'\n    <button class="tab" role="tab" id="t-ex60" aria-controls="ex60" '
       u'aria-selected="false"><span class="tnum">Q4</span>ข้อสอบจำลอง 60 นาที</button>')

RAIL = u"""
    <nav id="rail-ex60" class="hidden" aria-label="ข้อสอบจำลอง 60 นาที">
      <div class="rail-h">ข้อสอบจำลอง</div>
      <ol>
        <li><a href="#ex60-top"><i>Q4</i>%d ข้อ · %d นาที</a></li>
      </ol>
    </nav>
"""

PANEL = u"""
  <div id="ex60" class="hidden" role="tabpanel" aria-labelledby="t-ex60">
    <div id="ex60-top"></div>
    <p class="lede"><b>ข้อสอบจำลอง %d ข้อ %d นาที</b> เฉพาะเนื้อหาจากเอกสาร <b>Ch4_3</b> คือ
      บทที่ 6, 8, 9 และ 10 · เฉลี่ย<b>ข้อละ 3 นาที</b> จึงเป็นโจทย์ที่ต้องคำนวณหลายขั้น
      หรือผสมกฎสองข้อเข้าด้วยกันแทบทุกข้อ ยากกว่าระดับขั้นสูงในแท็บ <b>Q3</b></p>
    <div class="exintro">
      <b>ชุดนี้เป็นโหมดสอบ ไม่ใช่โหมดฝึก</b> — <b>เฉลยจะยังไม่แสดงจนกว่าจะกดส่งคำตอบ</b>
      เปลี่ยนคำตอบได้ตลอดเวลาที่ยังไม่ส่ง · นาฬิกาเริ่มนับเมื่อกด<b>เริ่มทำข้อสอบ</b>
      และเมื่อหมดเวลาระบบจะ<b>ส่งคำตอบให้อัตโนมัติ</b> ·
      ข้อที่ยังไม่ได้ตอบนับเป็นผิด เหมือนข้อสอบจริง · ลำดับตัวเลือกสลับใหม่ทุกครั้งที่เริ่ม
    </div>
    <div class="exbar">
      <div>
        <div class="exclock" id="ex60-clock">%02d:00</div>
        <div class="exinfo" id="ex60-info">ยังไม่เริ่ม · กดปุ่มเพื่อเริ่มจับเวลา</div>
      </div>
      <div class="exbtns">
        <button type="button" class="go" id="ex60-start">เริ่มทำข้อสอบ</button>
        <button type="button" id="ex60-submit" disabled>ส่งคำตอบ</button>
      </div>
    </div>
    <div id="ex60-result"></div>
    <div id="ex60-list" data-state="idle"></div>
  </div>
"""


def patch_tab(html):
    return splice(html, 'tab', TAB, u'<!-- quiz3:tab:end -->', before=False)


def patch_rail(html, total, minutes):
    m = re.search(r'<nav id="rail-quiz3" class="hidden".*?</nav>\n', html, re.S)
    if not m:
        raise SystemExit(u'หาแถบข้างของควิซชีท 4_3 ไม่เจอ')
    return splice(html, 'rail', RAIL % (total, minutes), m.group(0), before=False)


def patch_railjs(html):
    s, e = jsmark('rails')
    want = s + u" ex60:'rail-ex60'," + e
    old = re.search(re.escape(s) + r'.*?' + re.escape(e), html, re.S)
    if old:
        return (html, 0) if old.group(0) == want else (html[:old.start()] + want + html[old.end():], 1)
    anchor = u"quiz3:'rail-quiz3',"
    if html.count(anchor) != 1:
        raise SystemExit(u'หาตาราง rails ใน JS ไม่เจอ')
    return html.replace(anchor, anchor + want), 1


def patch_panel(html, total, minutes):
    return splice(html, 'panel', PANEL % (total, minutes, minutes),
                  u'<!-- quiz3:panel:end -->', before=False)


def patch_bank(html, bank_js):
    s, e = jsmark('bank')
    body = s + u'\n  var EX60 = [\n' + bank_js + u'\n  ];\n  ' + e
    old = re.search(re.escape(s) + r'.*?' + re.escape(e), html, re.S)
    if old:
        return (html, 0) if old.group(0) == body else (html[:old.start()] + body + html[old.end():], 1)
    anchor = u'/* quiz3:bank:end */'
    if html.count(anchor) != 1:
        raise SystemExit(u'หาท้ายคลังข้อสอบชุดที่สามไม่เจอ')
    return html.replace(anchor, anchor + u'\n  ' + body), 1


# ───────────────────── ส่วนที่ 3 · เครื่องเล่นโหมดสอบ ─────────────────────

MOUNT = u"""
  /* โหมดสอบ แยกจาก mountQuiz เพราะต้องปิดเฉลยไว้ จับเวลา และตรวจทีเดียวตอนจบ */
  (function(){
    var LIMIT = %d * 60;                 // วินาที
    var listEl = document.getElementById('ex60-list');
    if (!listEl) return;
    var clockEl  = document.getElementById('ex60-clock');
    var infoEl   = document.getElementById('ex60-info');
    var startBtn = document.getElementById('ex60-start');
    var subBtn   = document.getElementById('ex60-submit');
    var resEl    = document.getElementById('ex60-result');
    var picked = [], order = [], left = LIMIT, timer = null, done = false;

    function mmss(s){
      if (s < 0) s = 0;
      var m = Math.floor(s / 60);
      return (m < 10 ? '0' : '') + m + ':' + (s %% 60 < 10 ? '0' : '') + (s %% 60);
    }
    function paintClock(){
      clockEl.textContent = mmss(left);
      clockEl.classList.toggle('warn', left <= 600 && left > 300);
      clockEl.classList.toggle('danger', left <= 300);
    }
    function answered(){
      return picked.reduce(function(n, p){ return n + (p === null ? 0 : 1); }, 0);
    }
    function paintInfo(){
      if (done) return;
      infoEl.textContent = 'ตอบแล้ว ' + answered() + ' จาก ' + EX60.length + ' ข้อ' +
        (left <= 300 ? ' · เหลือเวลาไม่ถึงห้านาที' : '');
    }

    function build(){
      listEl.innerHTML = '';
      picked = EX60.map(function(){ return null; });
      order = [];
      EX60.forEach(function(item, i){
        var wrap = document.createElement('div');
        wrap.className = 'q';
        var n = document.createElement('div');
        n.className = 'q-n';
        n.textContent = 'ข้อ ' + (i + 1) + ' · บทที่ ' + item.ch;
        var t = document.createElement('div');
        t.className = 'q-t';
        t.textContent = item.q;
        var opts = document.createElement('div');
        opts.className = 'opts';
        var expl = document.createElement('div');
        expl.className = 'expl hidden';
        expl.textContent = item.e;

        // สลับลำดับตัวเลือกทุกครั้งที่เริ่มทำ กันการจำตำแหน่งเฉลยแทนการเข้าใจเนื้อหา
        var ord = item.o.map(function(_, k){ return k; });
        for (var x = ord.length - 1; x > 0; x--){
          var y = Math.floor(Math.random() * (x + 1));
          var tmp = ord[x]; ord[x] = ord[y]; ord[y] = tmp;
        }
        order.push(ord);

        ord.forEach(function(srcIdx, j){
          var b = document.createElement('button');
          b.type = 'button';
          b.className = 'opt';
          b.textContent = item.o[srcIdx];
          b.addEventListener('click', function(){
            if (done) return;
            picked[i] = j;                        // เก็บตำแหน่งที่เลือกในลำดับที่สลับแล้ว
            Array.prototype.forEach.call(opts.querySelectorAll('.opt'), function(o, k){
              o.classList.toggle('picked', k === j);
            });
            paintInfo();
          });
          opts.appendChild(b);
        });
        wrap.appendChild(n); wrap.appendChild(t); wrap.appendChild(opts); wrap.appendChild(expl);
        listEl.appendChild(wrap);
      });
    }

    function grade(reason){
      if (done) return;
      done = true;
      clearInterval(timer);
      var correct = 0, blank = 0;
      var byCh = {};
      var wraps = listEl.querySelectorAll('.q');
      EX60.forEach(function(item, i){
        var at = order[i].indexOf(item.a);       // ตำแหน่งของเฉลยหลังสลับ
        var opts = wraps[i].querySelectorAll('.opt');
        Array.prototype.forEach.call(opts, function(o, k){
          o.disabled = true;
          o.classList.remove('picked');
          if (k === at) o.classList.add('ok');
          else if (k === picked[i]) o.classList.add('no');
        });
        wraps[i].querySelector('.expl').classList.remove('hidden');
        if (picked[i] === null) blank++;
        byCh[item.ch] = byCh[item.ch] || [0, 0];
        byCh[item.ch][1]++;
        if (picked[i] === at){ correct++; byCh[item.ch][0]++; }
      });
      var used = LIMIT - left;
      var pct = Math.round(correct * 1000 / EX60.length) / 10;
      var parts = Object.keys(byCh).sort(function(a, b){ return a - b; }).map(function(c){
        return '<span>บทที่ ' + c + ' ' + byCh[c][0] + ' จาก ' + byCh[c][1] + '</span>';
      }).join('');
      resEl.innerHTML =
        '<div class="exresult">' +
          '<div class="rbig">' + correct + ' / ' + EX60.length + '</div>' +
          '<div class="rline">คิดเป็น <b>' + pct + ' เปอร์เซ็นต์</b> · ใช้เวลา <b>' + mmss(used) + '</b>' +
            ' จาก ' + mmss(LIMIT) + (blank ? ' · ไม่ได้ตอบ <b>' + blank + ' ข้อ</b> ซึ่งนับเป็นผิด' : '') + '</div>' +
          '<div class="rline">' + (reason === 'timeout'
            ? 'หมดเวลา ระบบส่งคำตอบให้อัตโนมัติ'
            : 'ส่งคำตอบแล้ว') + ' · เลื่อนลงไปดูเฉลยและคำอธิบายของทุกข้อได้เลย</div>' +
          '<div class="exbreak">' + parts + '</div>' +
        '</div>';
      infoEl.textContent = 'ส่งคำตอบแล้ว · กดเริ่มใหม่เพื่อทำอีกครั้ง';
      clockEl.classList.remove('warn', 'danger');
      startBtn.textContent = 'เริ่มใหม่';
      startBtn.disabled = false;
      subBtn.disabled = true;
    }

    function start(){
      done = false;
      left = LIMIT;
      resEl.innerHTML = '';
      build();
      listEl.dataset.state = 'run';
      paintClock(); paintInfo();
      startBtn.disabled = true;
      startBtn.textContent = 'เริ่มทำข้อสอบ';
      subBtn.disabled = false;
      clearInterval(timer);
      timer = setInterval(function(){
        left--;
        paintClock();
        if (left === 300 || left === 60) paintInfo();
        if (left <= 0) grade('timeout');
      }, 1000);
    }

    startBtn.addEventListener('click', start);
    subBtn.addEventListener('click', function(){
      var miss = EX60.length - answered();
      if (miss > 0 && !window.confirm('ยังไม่ได้ตอบ ' + miss + ' ข้อ ซึ่งจะนับเป็นผิด ส่งคำตอบเลยหรือไม่')) return;
      grade('submit');
    });
  })();
"""


def patch_mount(html, minutes):
    return splice(html, 'mount', MOUNT % minutes, u'/* quiz3:mount:end */',
                  comment=False, before=False)


# ───────────────────────── ตรวจหลังแทรก ─────────────────────────

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


def verify(html, data):
    bad = 0
    for need in ('id="t-ex60"', 'id="ex60"', 'id="rail-ex60"', 'id="ex60-list"',
                 'id="ex60-clock"', 'id="ex60-start"', 'id="ex60-submit"', 'id="ex60-result"',
                 'var EX60 = [', "ex60:'rail-ex60'"):
        if need not in html:
            print(u'  ขาด %s' % need); bad += 1

    m = re.search(r'var EX60 = \[(.*?)\n  \];', html, re.S)
    if not m:
        print(u'  หาคลังข้อสอบจำลองไม่เจอ'); bad += 1
        return bad
    body = m.group(1)
    if re.search(r',(?:\s|/\*.*?\*/)*,', body, flags=re.S):
        print(u'  คลังข้อสอบจำลองมีจุลภาคซ้ำจนเกิดช่องว่างในอาร์เรย์'); bad += 1
    n = body.count(u'{ch:')
    if n != data.TOTAL:
        print(u'  คลังมี %d ข้อ แต่ข้อมูลบอกว่า %d ข้อ' % (n, data.TOTAL)); bad += 1
    else:
        print(u'  ข้อสอบจำลอง %d ข้อ · %d นาที' % (n, data.MINUTES))
    for ch in sorted(data.BY_CH):
        got = body.count(u'{ch:%d,' % ch)
        if got != data.BY_CH[ch]:
            print(u'  บทที่ %d มี %d ข้อ แต่ข้อมูลบอกว่า %d' % (ch, got, data.BY_CH[ch])); bad += 1
        else:
            print(u'  บทที่ %-2d %d ข้อ' % (ch, got))
    # ทุกข้อต้องมีสี่ตัวเลือก ไม่งั้นโจทย์ไม่สมบูรณ์
    opts = re.findall(r"o:\[(.*?)\], a:", body, re.S)
    if len(opts) != n:
        print(u'  มีข้อที่รูปแบบตัวเลือกไม่ตรงแบบ เจอ %d จาก %d' % (len(opts), n)); bad += 1
    short = [i + 1 for i, o in enumerate(opts) if o.count(u"','") != 3]
    if short:
        print(u'  ข้อที่ตัวเลือกไม่ครบสี่ตัว %s' % short); bad += 1
    # เครื่องเล่นใช้ textContent ถ้ามีแท็กหลุดมาจะโผล่เป็นตัวหนังสือ
    tags = re.findall(r'<[a-zA-Z/][^>]*>', body)
    if tags:
        print(u'  มีแท็ก HTML หลุดอยู่ในคลัง เช่น %s' % tags[0]); bad += 1

    # สามคลังเดิมต้องไม่ถูกกระทบ
    for name, pat, want in ((u'คลังรวม', r'var QS = \[(.*?)\n  \];', 78),
                            (u'คลังหลังมิดเทอม', r'var QS2 = \[(.*?)\n  \];', 50),
                            (u'ควิซชีท 4_3', r'var QS3 = \[(.*?)\n  \];', 65)):
        mm = re.search(pat, html, re.S)
        got = mm.group(1).count(u'{ch:') if mm else 0
        if got != want:
            print(u'  %s เปลี่ยนไปเป็น %d ข้อ จากเดิม %d' % (name, got, want)); bad += 1
        else:
            print(u'  %-14s คงเดิม %d ข้อ' % (name, got))

    for tag in ('nav', 'section'):
        o = len(re.findall(r'<%s[\s>]' % tag, html))
        c = len(re.findall(r'</%s>' % tag, html))
        if o != c:
            print(u'  แท็ก %s ไม่สมดุล เปิด %d ปิด %d' % (tag, o, c)); bad += 1
    od = len(re.findall(r'<div[\s>]', html))
    cd = len(re.findall(r'</div>', html))
    if od != cd:
        print(u'  แท็ก div ไม่สมดุล เปิด %d ปิด %d' % (od, cd)); bad += 1
    bad += check_js(html)
    return bad


def main():
    ap = argparse.ArgumentParser(description=u'เพิ่มข้อสอบจำลอง 20 ข้อ 60 นาที')
    ap.add_argument('--check', action='store_true', help=u'ตรวจอย่างเดียว ไม่เขียนไฟล์')
    a = ap.parse_args()

    import advexam_data as D

    html = io.open(PAGE, encoding='utf-8').read()
    before = len(html)
    steps = 0
    for fn in (patch_css, patch_tab, patch_railjs):
        html, n = fn(html)
        steps += n
    html, n = patch_rail(html, D.TOTAL, D.MINUTES); steps += n
    html, n = patch_panel(html, D.TOTAL, D.MINUTES); steps += n
    html, n = patch_bank(html, D.EXAM); steps += n
    html, n = patch_mount(html, D.MINUTES); steps += n

    print(u'ปรับ %d ชิ้น · %d → %d อักษร' % (steps, before, len(html)))
    bad = verify(html, D)
    if bad:
        print(u'\nตรวจพบปัญหา %d จุด จึงยังไม่เขียนไฟล์' % bad)
        return 1
    if a.check:
        print(u'\nตรวจผ่าน · ยังไม่เขียนไฟล์เพราะสั่ง --check')
        return 0
    io.open(PAGE, 'w', encoding='utf-8').write(html)
    print(u'\nเขียน %s แล้ว' % os.path.relpath(PAGE, ROOT))
    return 0


if __name__ == '__main__':
    sys.exit(main())
