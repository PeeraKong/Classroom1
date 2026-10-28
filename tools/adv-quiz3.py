#!/usr/bin/env python3
# -*- coding: utf-8 -*-
u"""เพิ่มแท็บควิซของเอกสารประกอบการสอน Ch4_3_2568 ที่ไล่ระดับความยาก

    python3 tools/adv-quiz3.py            แทรกจริง
    python3 tools/adv-quiz3.py --check    ตรวจอย่างเดียว ไม่เขียนไฟล์

ต่างจากสองแท็บที่มีอยู่แล้ว
  แท็บ Q   แบบทดสอบรวม ครอบคลุมทุกบทของทั้งวิชา
  แท็บ Q2  เน้นแนวคิดของเนื้อหาหลังมิดเทอม แทบไม่มีการคิดเลข
  แท็บ Q3  เฉพาะสี่บทที่มาจากชีท Ch4_3 และ ไล่ระดับจากพื้นฐานไปขั้นสูง
           มีทั้งข้อท่องนิยาม ข้อแยกแยะ และข้อคำนวณหลายขั้น

สคริปต์นี้ขยายตัวสร้างแบบทดสอบ mountQuiz ที่มีอยู่แล้วให้
  แสดงป้ายระดับความยากต่อท้ายเลขข้อ เมื่อข้อนั้นมีคีย์ lv
  รับปุ่มกรองระดับมาเป็นพารามิเตอร์เพิ่มได้
ทั้งสองอย่างเป็นการเพิ่มแบบไม่กระทบของเดิม เพราะข้อในคลัง Q และ Q2 ไม่มีคีย์ lv
และสองแท็บนั้นไม่ได้ส่งรหัสปุ่มกรองเข้ามา

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
    return (u'<!-- quiz3:%s:start -->' % k, u'<!-- quiz3:%s:end -->' % k)


def jsmark(k):
    return (u'/* quiz3:%s:start */' % k, u'/* quiz3:%s:end */' % k)


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
/* แถบเลือกระดับความยากของแท็บ Q3 */
.lvbar{display:flex; flex-wrap:wrap; gap:7px; align-items:center; margin:0 0 14px}
.lvbar .lvlabel{font-size:.78rem; color:var(--ink-3); margin-right:4px}
.lvbar button{appearance:none; font:inherit; font-size:.82rem; font-weight:600; cursor:pointer;
  padding:6px 14px; border:1px solid var(--rule-strong); background:var(--surface);
  color:var(--ink-2); border-radius:999px}
.lvbar button:hover{border-color:var(--accent); color:var(--accent)}
.lvbar button[aria-pressed="true"]{background:var(--accent); border-color:var(--accent); color:var(--paper)}
/* ป้ายระดับความยากต่อท้ายเลขข้อ */
.q-n .lvtag{display:inline-block; margin-left:8px; padding:1px 8px; border-radius:999px;
  font-size:.68rem; font-weight:700; letter-spacing:.04em; vertical-align:1px}
.q-n .lv1{background:var(--green-soft); color:var(--green)}
.q-n .lv2{background:var(--amber-soft); color:var(--amber)}
.q-n .lv3{background:var(--red-soft); color:var(--red)}"""


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


# ───────────────────────── ส่วนที่ 2 · แท็บ แถบข้าง แผง ─────────────────────────

TAB = (u'\n    <button class="tab" role="tab" id="t-quiz3" aria-controls="quiz3" '
       u'aria-selected="false"><span class="tnum">Q3</span>ควิซชีท 4_3</button>')

RAIL = u"""
    <nav id="rail-quiz3" class="hidden" aria-label="ควิซชีท 4_3">
      <div class="rail-h">ควิซชีท 4_3</div>
      <ol>
        <li><a href="#quiz3-top"><i>Q3</i>%d ข้อ · ไล่ระดับ</a></li>
      </ol>
    </nav>
"""

PANEL = u"""
  <div id="quiz3" class="hidden" role="tabpanel" aria-labelledby="t-quiz3">
    <div id="quiz3-top"></div>
    <p class="lede"><b>%d ข้อ จากชีท Ch4_3 โดยเฉพาะ</b> ครอบคลุมสี่บทที่มาจากเอกสารฉบับนั้น คือ
      <b>บทที่ 6</b> งบการเงินรวมกรณีขาดทุน · <b>บทที่ 8</b> การด้อยค่าของค่าความนิยม ·
      <b>บทที่ 9</b> กิจการร่วมค้า · <b>บทที่ 10</b> บุคคลหรือกิจการที่เกี่ยวข้องกัน ·
      <b>บทที่ 7 รายการระหว่างบริษัทในเครือ ไม่ได้อยู่ในชีทฉบับนี้</b> จึงไม่มีในชุดนี้</p>
    <p class="lede">เรียงจาก<b>ง่ายไปยาก</b> แบ่งเป็นสามระดับ ·
      <b>พื้นฐาน %d ข้อ</b> ท่องนิยามและข้อความตามมาตรฐานให้ได้ ·
      <b>ปานกลาง %d ข้อ</b> แยกแยะของที่คล้ายกันและคำนวณขั้นเดียว ·
      <b>ขั้นสูง %d ข้อ</b> คำนวณหลายขั้นและกับดักที่ซ่อนในโจทย์ ·
      กดปุ่มด้านล่างเพื่อซ้อมเฉพาะระดับที่ต้องการได้</p>
    <div class="lvbar" id="lv3-bar" role="group" aria-label="เลือกระดับความยาก">
      <span class="lvlabel">ระดับ</span>
      <button type="button" data-lv="all" aria-pressed="true">ทั้งหมด</button>
      <button type="button" data-lv="1" aria-pressed="false">พื้นฐาน</button>
      <button type="button" data-lv="2" aria-pressed="false">ปานกลาง</button>
      <button type="button" data-lv="3" aria-pressed="false">ขั้นสูง</button>
    </div>
    <div class="score">
      <span>ตอบถูก <span class="sv" id="sc3-val">0</span> ข้อ · ตอบแล้ว <span class="sv" id="sc3-of">0 จาก %d ข้อ</span></span>
      <button type="button" id="sc3-reset">เริ่มใหม่</button>
    </div>
    <div id="quiz3-list"></div>
  </div>
"""


def patch_tab(html):
    return splice(html, 'tab', TAB, u'<!-- quiz2:tab:end -->', before=False)


def patch_rail(html, total):
    m = re.search(r'<nav id="rail-quiz2" class="hidden".*?</nav>\n', html, re.S)
    if not m:
        raise SystemExit(u'หาแถบข้างของแบบทดสอบหลังมิดเทอมไม่เจอ')
    return splice(html, 'rail', RAIL % total, m.group(0), before=False)


def patch_railjs(html):
    s, e = jsmark('rails')
    want = s + u" quiz3:'rail-quiz3'," + e
    old = re.search(re.escape(s) + r'.*?' + re.escape(e), html, re.S)
    if old:
        return (html, 0) if old.group(0) == want else (html[:old.start()] + want + html[old.end():], 1)
    anchor = u"quiz2:'rail-quiz2',"
    if html.count(anchor) != 1:
        raise SystemExit(u'หาตาราง rails ใน JS ไม่เจอ')
    return html.replace(anchor, anchor + want), 1


def patch_panel(html, total, by_level):
    block = PANEL % (total, by_level[1], by_level[2], by_level[3], total)
    return splice(html, 'panel', block, u'<!-- quiz2:panel:end -->', before=False)


def patch_bank(html, bank_js):
    s, e = jsmark('bank')
    body = s + u'\n  var QS3 = [\n' + bank_js + u'\n  ];\n  ' + e
    old = re.search(re.escape(s) + r'.*?' + re.escape(e), html, re.S)
    if old:
        return (html, 0) if old.group(0) == body else (html[:old.start()] + body + html[old.end():], 1)
    anchor = u'/* quiz2:bank:end */'
    if html.count(anchor) != 1:
        raise SystemExit(u'หาท้ายคลังข้อสอบชุดที่สองไม่เจอ')
    return html.replace(anchor, anchor + u'\n  ' + body), 1


# ───────────── ส่วนที่ 3 · ขยายตัวสร้างแบบทดสอบให้รู้จักระดับความยาก ─────────────
# แก้สามจุดเล็ก ๆ ในฟังก์ชันเดิม แล้วต่อการเรียกใช้ของคลังชุดที่สาม
# ทั้งหมดเป็นการเพิ่ม ไม่ได้เปลี่ยนพฤติกรรมของสองคลังเดิมที่ไม่มีคีย์ lv

OLD_SIG = u"""  function mountQuiz(bank, elId, valId, ofId, resetId){
    var el = document.getElementById(elId);
    if (!el) return;
    var sv = document.getElementById(valId);
    var so = document.getElementById(ofId);
    var answered = 0, correct = 0;
    function updateScore(){
      if (sv) sv.textContent = String(correct);
      if (so) so.textContent = answered + ' จาก ' + bank.length + ' ข้อ';
    }
    function build(){
      el.innerHTML = '';
      answered = 0; correct = 0; updateScore();
      bank.forEach(function(item, i){"""

NEW_SIG = u"""  /* ป้ายระดับความยาก ใช้เฉพาะคลังที่ข้อมีคีย์ lv */
  var LVNAME = {1:'พื้นฐาน', 2:'ปานกลาง', 3:'ขั้นสูง'};
  function mountQuiz(bank, elId, valId, ofId, resetId, barId){
    var el = document.getElementById(elId);
    if (!el) return;
    var sv = document.getElementById(valId);
    var so = document.getElementById(ofId);
    var answered = 0, correct = 0, level = 'all';
    // กรองตามระดับที่เลือก ถ้ายังไม่เคยเลือกก็คืนคลังทั้งก้อนตามเดิม
    function pick(){
      if (level === 'all') return bank;
      return bank.filter(function(q){ return String(q.lv) === level; });
    }
    function updateScore(){
      if (sv) sv.textContent = String(correct);
      if (so) so.textContent = answered + ' จาก ' + pick().length + ' ข้อ';
    }
    function build(){
      el.innerHTML = '';
      answered = 0; correct = 0; updateScore();
      pick().forEach(function(item, i){"""

OLD_NUM = u"""      n.textContent = 'ข้อ ' + (i+1) + ' · บทที่ ' + item.ch;"""

NEW_NUM = u"""      n.textContent = 'ข้อ ' + (i+1) + ' · บทที่ ' + item.ch;
      if (item.lv){
        // ใช้ span ต่างหากแทนการต่อสตริง จะได้ระบายสีป้ายตามระดับได้
        var lt = document.createElement('span');
        lt.className = 'lvtag lv' + item.lv;
        lt.textContent = LVNAME[item.lv] || '';
        n.appendChild(lt);
      }"""

OLD_TAIL = u"""    build();
    var rb = document.getElementById(resetId);
    if (rb) rb.addEventListener('click', build);
  }
  mountQuiz(QS, 'quiz-list', 'sc-val', 'sc-of', 'sc-reset');
  mountQuiz(QS2, 'quiz2-list', 'sc2-val', 'sc2-of', 'sc2-reset');"""

NEW_TAIL = u"""    build();
    var rb = document.getElementById(resetId);
    if (rb) rb.addEventListener('click', build);
    var bar = barId && document.getElementById(barId);
    if (bar){
      var btns = Array.prototype.slice.call(bar.querySelectorAll('button[data-lv]'));
      btns.forEach(function(b){
        b.addEventListener('click', function(){
          level = b.getAttribute('data-lv');
          btns.forEach(function(x){
            x.setAttribute('aria-pressed', x === b ? 'true' : 'false');
          });
          build();   // เปลี่ยนระดับแล้วเริ่มนับคะแนนใหม่ เพราะจำนวนข้อเปลี่ยนไป
        });
      });
    }
  }
  mountQuiz(QS, 'quiz-list', 'sc-val', 'sc-of', 'sc-reset');
  mountQuiz(QS2, 'quiz2-list', 'sc2-val', 'sc2-of', 'sc2-reset');
  /* quiz3:mount:start */
  mountQuiz(QS3, 'quiz3-list', 'sc3-val', 'sc3-of', 'sc3-reset', 'lv3-bar');
  /* quiz3:mount:end */"""

PAIRS = [(OLD_SIG, NEW_SIG), (OLD_NUM, NEW_NUM), (OLD_TAIL, NEW_TAIL)]


def patch_mount(html):
    u"""ขยาย mountQuiz ให้รู้จักระดับความยากและปุ่มกรอง"""
    before = html
    if 'quiz3:mount:start' in html:
        return html, 0
    for old, new in PAIRS:
        if html.count(old) != 1:
            raise SystemExit(u'โค้ด mountQuiz ไม่ตรงกับที่คาด เจอ %d ที่' % html.count(old))
        html = html.replace(old, new)
    return html, (0 if html == before else 1)


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
    for need in ('id="t-quiz3"', 'id="quiz3"', 'id="rail-quiz3"', 'id="quiz3-list"',
                 'id="sc3-val"', 'id="sc3-of"', 'id="sc3-reset"', 'id="lv3-bar"',
                 'var QS3 = [', "quiz3:'rail-quiz3'"):
        if need not in html:
            print(u'  ขาด %s' % need); bad += 1

    m = re.search(r'var QS3 = \[(.*?)\n  \];', html, re.S)
    if not m:
        print(u'  หาคลังข้อสอบชุดที่สามไม่เจอ'); bad += 1
        return bad
    body = m.group(1)
    # จุลภาคสองตัวติดกันทำให้เกิดช่องว่างในอาร์เรย์ ซึ่ง forEach ข้ามให้เงียบ ๆ
    if re.search(r',(?:\s|/\*.*?\*/)*,', body, flags=re.S):
        print(u'  คลังชุดที่สามมีจุลภาคซ้ำจนเกิดช่องว่างในอาร์เรย์'); bad += 1
    n = body.count(u'{ch:')
    if n != data.TOTAL:
        print(u'  คลังมี %d ข้อ แต่ข้อมูลบอกว่า %d ข้อ' % (n, data.TOTAL)); bad += 1
    for lv, name in data.LEVELS:
        got = body.count(u'lv:%d,' % lv)
        if got != data.BY_LEVEL[lv]:
            print(u'  ระดับ%s มี %d ข้อ แต่ข้อมูลบอกว่า %d ข้อ'
                  % (name, got, data.BY_LEVEL[lv])); bad += 1
        else:
            print(u'  %-8s %2d ข้อ' % (name, got))
    # ทุกข้อต้องมีระดับกำกับ ไม่งั้นปุ่มกรองจะทำให้ข้อนั้นหายไปเลย
    if n != sum(data.BY_LEVEL.values()):
        print(u'  มีข้อที่ไม่ได้ระบุระดับความยาก'); bad += 1
    for ch in (6, 8, 9, 10):
        print(u'  บทที่ %-2d %2d ข้อ' % (ch, body.count(u'{ch:%d,' % ch)))
    # เครื่องเล่นใช้ textContent ถ้ามีแท็กหลุดมาจะโผล่เป็นตัวหนังสือให้ผู้เรียนเห็น
    tags = re.findall(r'<[a-zA-Z/][^>]*>', body)
    if tags:
        print(u'  มีแท็ก HTML หลุดอยู่ในคลัง เช่น %s' % tags[0]); bad += 1

    # สองคลังเดิมต้องไม่ถูกกระทบ
    # ยอดคลังหลังมิดเทอมขยับจาก 50 เป็น 69 ตอนเพิ่มบทที่ 6 กรณีต่างๆ ของงบรวม
    # ด้วย tools/adv-ch6.py ถ้าเพิ่มข้อสอบของบทไหนอีก ต้องมาขยับเลขตรงนี้ด้วย
    for name, pat, want in ((u'คลังรวม', r'var QS = \[(.*?)\n  \];', 78),
                            (u'คลังหลังมิดเทอม', r'var QS2 = \[(.*?)\n  \];', 69)):
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
    ap = argparse.ArgumentParser(description=u'เพิ่มควิซชีท 4_3 ที่ไล่ระดับความยาก')
    ap.add_argument('--check', action='store_true', help=u'ตรวจอย่างเดียว ไม่เขียนไฟล์')
    a = ap.parse_args()

    import advquiz3_data as D

    html = io.open(PAGE, encoding='utf-8').read()
    before = len(html)
    steps = 0
    for fn in (patch_css, patch_tab, patch_railjs, patch_mount):
        html, n = fn(html)
        steps += n
    html, n = patch_rail(html, D.TOTAL); steps += n
    html, n = patch_panel(html, D.TOTAL, D.BY_LEVEL); steps += n
    html, n = patch_bank(html, D.QUIZ3); steps += n

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
