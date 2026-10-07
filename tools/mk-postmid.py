#!/usr/bin/env python3
# -*- coding: utf-8 -*-
u"""เพิ่มเนื้อหาส่วนหลังมิดเทอมของวิชาหลักการตลาดลงในหน้าเว็บ

    python3 tools/mk-postmid.py            แทรกจริง
    python3 tools/mk-postmid.py --check    ตรวจอย่างเดียว ไม่เขียนไฟล์

ที่มาของเนื้อหา  เอกสารประกอบการสอน Chp 08 PRIN MKGT NPD PLC V2 cut 2569
  หน้า  5-6   สองทางที่จะได้สินค้าใหม่ และสาเหตุที่สินค้าใหม่ล้มเหลว
  หน้า  7-24  กระบวนการพัฒนาสินค้าใหม่แปดขั้น
  หน้า 25-28  การบริหารกระบวนการพัฒนาสินค้าใหม่สามแบบ
  หน้า 29-47  วงจรชีวิตผลิตภัณฑ์และกลยุทธ์ในแต่ละขั้น รวมตาราง 9.2
  หน้า 48-49  ความรับผิดชอบต่อสังคม และการตลาดระหว่างประเทศ

บทนี้เป็นเนื้อหาหลังมิดเทอม จึงแยกออกจากหกบทเดิมด้วยเส้นคั่นในแถบแท็บ
ทำแบบเดียวกับที่ทำไว้ในวิชาการบัญชีขั้นสูง 1 และเพิ่มแบบทดสอบชุดที่สอง
ที่เน้นแนวคิดของเนื้อหาหลังมิดเทอมโดยเฉพาะ แยกจากคลังรวมที่มีอยู่เดิม

สคริปต์นี้รันซ้ำได้ไม่ซ้อน เพราะคร่อมของที่เพิ่มด้วยคอมเมนต์หัวท้าย
และตรวจให้หลังแทรกว่าหัวข้อครบ ลิงก์ในแถบข้างชี้ถูก แท็กสมดุล
และสคริปต์ของหน้ายังคอมไพล์ได้

ภาพโฆษณาของแบรนด์ในสไลด์ไม่ได้ฝังลงในหน้า เพราะเป็นงานโฆษณาของบุคคลที่สาม
หน้านี้เล่าใจความเป็นภาษาไทยขึ้นใหม่พร้อมระบุที่มาแทน
ส่วนตาราง 9.2 พิมพ์ขึ้นใหม่เป็นตารางเว็บพร้อมคำแปล ไม่ได้ฝังภาพสแกน
"""

import argparse
import io
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGE = os.path.join(ROOT, 'marketing', 'index.html')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def mark(key):
    return (u'<!-- postmid:%s:start -->' % key, u'<!-- postmid:%s:end -->' % key)


def jsmark(key):
    return (u'/* postmid:%s:start */' % key, u'/* postmid:%s:end */' % key)


def trim_tail(s):
    u"""ตัดช่องว่างและคอมเมนต์ท้ายข้อความออกทีละก้อน

    ต้องไล่ตัดเองทีละก้อน ใช้ regex ตัวเดียวไม่ได้ เพราะ /\\*.*?\\*/ แบบ DOTALL
    ย้อนกลับไปจับ /* ตัวแรกของทั้งไฟล์ได้ แล้วกินเนื้อหาหายไปทั้งก้อน
    """
    while True:
        t = s.rstrip()
        if not t.endswith(u'*/'):
            return t
        k = t.rfind(u'/*')
        if k < 0:
            return t
        s = t[:k]


def splice(html, key, block, anchor, comment=True, before=True):
    u"""วางบล็อกคร่อมคอมเมนต์หัวท้าย ถ้ามีอยู่แล้วให้แทนที่ของเดิม ไม่ใช่ข้ามไป

    ทำแบบนี้เพื่อให้แก้เนื้อหาแล้วรันซ้ำได้ ไม่ต้องย้อนไฟล์กลับก่อนทุกครั้ง
    """
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
# หน้านี้ใช้สีเดียวทั้งหน้าอยู่แล้ว จึงไม่ต้องเพิ่มตัวแปรสี เพิ่มแค่เส้นคั่น

CSS_RULES = u"""
/* เส้นคั่นกลางแถบแท็บ บอกว่าจากตรงนี้ไปเป็นเนื้อหาหลังมิดเทอม */
.tab-div{display:flex; align-items:center; gap:7px; padding:0 12px; white-space:nowrap;
  font-size:.7rem; font-weight:700; letter-spacing:.09em; text-transform:uppercase; color:var(--ink-3)}
.tab-div::before{content:""; width:1px; height:18px; background:var(--rule)}
@media (max-width:640px){.tab-div{padding:0 8px; font-size:.62rem}}"""


def patch_css(html):
    # อยู่ใน <style> จึงต้องคร่อมด้วยคอมเมนต์แบบ CSS ไม่ใช่คอมเมนต์ HTML
    anchor = (u'.tab .tnum{font-family:"IBM Plex Mono",monospace; '
              u'font-size:.75rem; opacity:.65; margin-right:7px}')
    return splice(html, 'css', CSS_RULES, anchor, comment=False, before=False)


# ───────────────────────── ส่วนที่ 2 · แถบแท็บ ─────────────────────────
TAB_M8 = u"""
    <span class="tab-div">หลังมิดเทอม</span>
    <button class="tab" role="tab" id="t-m8" aria-controls="m8" aria-selected="false"><span class="tnum">08</span>สินค้าใหม่และวงจรชีวิต</button>
  """

TAB_Q2 = u"""
    <button class="tab" role="tab" id="t-quiz2" aria-controls="quiz2" aria-selected="false"><span class="tnum">Q2</span>แบบทดสอบหลังมิดเทอม</button>"""

QUIZ_TAB = (u'<button class="tab" role="tab" id="t-quiz" aria-controls="quiz" '
            u'aria-selected="false"><span class="tnum">Q</span>แบบทดสอบ</button>')


def patch_tabs(html):
    html, a = splice(html, 'tab-m8', TAB_M8, u'  ' + QUIZ_TAB)
    html, b = splice(html, 'tab-q2', TAB_Q2, QUIZ_TAB, before=False)
    return html, a + b


def patch_railjs(html):
    u"""ลงทะเบียนแถบข้างของแผงใหม่ในตาราง rails ของสคริปต์หน้า"""
    before = html
    s, e = jsmark('rails')
    want = s + u"m8:'rail-m8', " + e
    old = re.search(re.escape(s) + r'.*?' + re.escape(e), html, re.S)
    if old:
        html = html if old.group(0) == want else html[:old.start()] + want + html[old.end():]
    else:
        anchor = u"quiz:'rail-quiz'}"
        if html.count(anchor) != 1:
            raise SystemExit(u'หาตาราง rails ใน JS ไม่เจอ')
        html = html.replace(anchor, want + anchor)

    s2, e2 = jsmark('rails2')
    want2 = s2 + u", quiz2:'rail-quiz2'" + e2
    old2 = re.search(re.escape(s2) + r'.*?' + re.escape(e2), html, re.S)
    if old2:
        html = html if old2.group(0) == want2 else html[:old2.start()] + want2 + html[old2.end():]
    else:
        anchor = u"quiz:'rail-quiz'"
        html = html.replace(anchor, anchor + want2, 1)
    return html, (0 if html == before else 1)


RAIL_Q2 = u"""
    <nav id="rail-quiz2" class="hidden" aria-label="แบบทดสอบหลังมิดเทอม">
      <div class="rail-h">หลังมิดเทอม</div>
      <ol><li><a href="#quiz2-top"><i>Q2</i>QTOT ข้อ · เน้นแนวคิด</a></li></ol>
    </nav>"""


def patch_rails(html, rails_html, q2_total):
    html, a = splice(html, 'rails', u'\n' + rails_html + u'    ',
                     u'    <nav id="rail-quiz" class="hidden" aria-label="แบบทดสอบ">')
    m = re.search(r'<nav id="rail-quiz" class="hidden".*?</nav>', html, re.S)
    if not m:
        raise SystemExit(u'หาแถบข้างของแบบทดสอบเดิมไม่เจอ')
    html, b = splice(html, 'rail-q2', RAIL_Q2.replace(u'QTOT', u'%d' % q2_total),
                     m.group(0), before=False)
    return html, a + b


QUIZ2_PANEL = u"""
  <div id="quiz2" class="hidden" role="tabpanel" aria-labelledby="t-quiz2">
    <div id="quiz2-top"></div>
    <p class="lede">QTOT ข้อ เฉพาะ<b>บทที่ 8 ซึ่งเป็นเนื้อหาหลังมิดเทอม</b> · ชุดนี้<b>ไม่ถามให้ท่องรายการ</b> แต่ให้สถานการณ์มาแล้วถามว่าอยู่ขั้นไหนของกระบวนการ เป็นกลยุทธ์ตัวใด หรือทำไมคำตอบที่ฟังดูถูกถึงผิด · <b>ลำดับตัวเลือกสลับใหม่ทุกครั้งที่เริ่มทำ</b></p>
    <div class="score">
      <span>ตอบถูก <span class="sv" id="sc2-val">0</span> ข้อ · ตอบแล้ว <span class="sv" id="sc2-of">0 จาก QTOT ข้อ</span></span>
      <button type="button" id="sc2-reset">เริ่มใหม่</button>
    </div>
    <div id="quiz2-list"></div>
  </div>
"""


def patch_panels(html, panel_html, q2_total):
    html, a = splice(html, 'panel', u'\n' + panel_html + u'\n',
                     u'  <div id="quiz" class="hidden" role="tabpanel" aria-labelledby="t-quiz">')
    html, b = splice(html, 'panel-q2', QUIZ2_PANEL.replace(u'QTOT', u'%d' % q2_total),
                     u'  </main>')
    return html, a + b


# ───────────────── ส่วนที่ 3 · สคริปต์ของแผงเลือกขั้นตอน ─────────────────

def patch_stepjs(html, step_js):
    return splice(html, 'stepjs', u'\n' + step_js, u'  /* ---- แบบทดสอบ ---- */',
                  comment=False)


# ───────────────────────── ส่วนที่ 4 · แบบทดสอบ ─────────────────────────

OLD_BUILDER = u"""  var listEl = document.getElementById('quiz-list');
  var scVal = document.getElementById('sc-val'), scOf = document.getElementById('sc-of');
  var answered = 0, correct = 0;
  function updateScore(){
    scVal.textContent = String(correct);
    scOf.textContent = answered + ' จาก ' + QS.length + ' ข้อ';
  }
  function buildQuiz(){
    listEl.innerHTML = '';
    answered = 0; correct = 0; updateScore();
    QS.forEach(function(item, i){"""

NEW_BUILDER = u"""  /* คลังข้อสอบมีสองชุด จึงทำตัวสร้างให้รับคลังและรหัสกล่องเป็นพารามิเตอร์
     ชุดแรกคือคลังรวมทั้งเจ็ดบท ชุดที่สองคือชุดเน้นแนวคิดของบทหลังมิดเทอม */
  function mountQuiz(bank, elId, valId, ofId, resetId){
  var listEl = document.getElementById(elId);
  if (!listEl) return;
  var scVal = document.getElementById(valId), scOf = document.getElementById(ofId);
  var answered = 0, correct = 0;
  function updateScore(){
    scVal.textContent = String(correct);
    scOf.textContent = answered + ' จาก ' + bank.length + ' ข้อ';
  }
  function buildQuiz(){
    listEl.innerHTML = '';
    answered = 0; correct = 0; updateScore();
    bank.forEach(function(item, i){"""

OLD_TAIL = u"""  buildQuiz();
  document.getElementById('sc-reset').addEventListener('click', buildQuiz);"""

NEW_TAIL = u"""  buildQuiz();
  var rb = document.getElementById(resetId);
  if (rb) rb.addEventListener('click', buildQuiz);
  }
  mountQuiz(QS,  'quiz-list',  'sc-val',  'sc-of',  'sc-reset');
  mountQuiz(QS2, 'quiz2-list', 'sc2-val', 'sc2-of', 'sc2-reset');"""


def patch_builder(html):
    u"""เปลี่ยนตัวสร้างแบบทดสอบตัวเดียวให้เป็นฟังก์ชันที่เรียกซ้ำกับคลังที่สองได้"""
    before = html
    if 'function mountQuiz(' not in html:
        for old, new in ((OLD_BUILDER, NEW_BUILDER), (OLD_TAIL, NEW_TAIL)):
            if html.count(old) != 1:
                raise SystemExit(u'โค้ดตัวสร้างแบบทดสอบไม่ตรงกับที่คาด (%d ที่)' % html.count(old))
            html = html.replace(old, new)
    return html, (0 if html == before else 1)


LEDE1 = (u'TOT ข้อ ครอบคลุม<b>ทั้งเจ็ดบท</b> ทั้งก่อนและหลังมิดเทอม '
         u'เน้นจุดที่นิยามใกล้เคียงกันจนสับสน · '
         u'<b>ลำดับตัวเลือกสลับใหม่ทุกครั้งที่เริ่มทำ</b> จึงจำตำแหน่งเฉลยไม่ได้ · '
         u'อยากซ้อมเฉพาะเนื้อหาหลังมิดเทอมให้ไปที่แท็บ <b>Q2</b>')


def patch_quiz(html, quiz_js, total, quiz2_js):
    before = html

    # ข้อที่เติมเข้าคลังรวม
    s, e = jsmark('quiz')
    body = s + u'\n' + quiz_js + u'\n    ' + e
    old = re.search(re.escape(s) + r'.*?' + re.escape(e), html, re.S)
    if old:
        html = html if old.group(0) == body else html[:old.start()] + body + html[old.end():]
    else:
        i = html.rindex(u'var QS = [')
        j = html.index(u'\n  ];', i)
        head = html[:j]
        # ข้อสุดท้ายของคลังเดิมอาจไม่มีจุลภาคปิดท้าย ต้องเติมก่อน ไม่งั้นสคริปต์ทั้งหน้าพัง
        # แต่ท้ายคลังมีคอมเมนต์ปิดของการแทรกรอบก่อนคั่นอยู่ ต้องมองข้ามคอมเมนต์ก่อน
        # ไม่งั้นจะเติมจุลภาคซ้ำจนกลายเป็นช่องว่างในอาร์เรย์ ซึ่ง forEach ข้ามให้เงียบ ๆ
        # แต่ทำให้ bank.length เกินจริงไปหนึ่ง และเลขข้อในหน้าเว็บกระโดด
        bare = trim_tail(head)
        if not bare.endswith(u','):
            head = bare + u',' + head[len(bare):]
        html = head + u'\n    ' + body + html[j:]

    # คลังชุดที่สอง วางต่อท้ายคลังรวม
    s2, e2 = jsmark('quiz2')
    body2 = s2 + u'\n  var QS2 = [\n' + quiz2_js + u'\n  ];\n  ' + e2
    old2 = re.search(re.escape(s2) + r'.*?' + re.escape(e2), html, re.S)
    if old2:
        html = html if old2.group(0) == body2 else html[:old2.start()] + body2 + html[old2.end():]
    else:
        i = html.rindex(u'var QS = [')
        j = html.index(u'\n  ];', i) + len(u'\n  ];')
        html = html[:j] + u'\n\n  ' + body2 + html[j:]

    # ข้อความบอกจำนวนข้อของคลังรวมต้องตามไปด้วย ไม่งั้นตัวเลขไม่ตรงของจริง
    # เขียนทับทั้งย่อหน้าแทนการจับคู่ของเดิม เพราะเคยแก้มาหลายรอบแล้ว
    m = re.search(r'(<div id="quiz-top"></div>\s*<p class="lede">)(.*?)(</p>)', html, re.S)
    if not m:
        raise SystemExit(u'หาคำโปรยของแบบทดสอบรวมไม่เจอ')
    want = LEDE1.replace(u'TOT', u'%d' % total)
    if m.group(2) != want:
        html = html[:m.start(2)] + want + html[m.end(2):]
    html = re.sub(u'id="sc-of">0 จาก \\d+ ข้อ', u'id="sc-of">0 จาก %d ข้อ' % total, html)
    html = re.sub(u'<i>Q</i>\\d+ ข้อ', u'<i>Q</i>%d ข้อ' % total, html)
    return html, (0 if html == before else 1)


# ───────────────────── ส่วนที่ 5 · หัวเรื่องและท้ายหน้า ─────────────────────

EYEBROW = u'Principles of Marketing · Ch 1, 3–8'

MAST_NEW = (u'<b>ก่อนมิดเทอม</b> กระบวนการการตลาด 5 ขั้น · สภาพแวดล้อมทางการตลาดและ PESTLE · '
            u'ระบบสารสนเทศและการวิจัยตลาด · พฤติกรรมผู้บริโภค · กลยุทธ์ STP · ผลิตภัณฑ์และตราสินค้า · '
            u'<b>หลังมิดเทอม</b> การพัฒนาสินค้าใหม่แปดขั้นและวงจรชีวิตผลิตภัณฑ์')

FOOT_NEW = (u'<b>หลักการตลาด</b> — สรุปจากเอกสารประกอบการสอน 7 ชุด อ้างอิงตำรา Kotler &amp; Armstrong, '
            u'<i>Principles of Marketing</i> (Pearson Education) · '
            u'<b>บทที่ 1, 3, 4, 5, 6 และ 7 เป็นเนื้อหาสอบกลางภาค</b> · '
            u'<b>บทที่ 8 เป็นเนื้อหาหลังมิดเทอม</b> ว่าด้วยการพัฒนาสินค้าใหม่และวงจรชีวิตผลิตภัณฑ์ '
            u'แยกไว้หลังเส้นคั่นในแถบแท็บ และมีแบบทดสอบของตัวเองที่แท็บ <b>Q2</b> · '
            u'หัวข้อ <b>ชีทอาจารย์</b> ท้ายบทที่ 1, 3, 4, 5, 6 และ 7 สรุปจากชีทประกอบการสอนของ อ.กฤตินี (อ.เกด) · '
            u'บทที่ 7 ใส่เฉพาะส่วนผลิตภัณฑ์')


def patch_mast(html):
    u"""เขียนทับคำโปรยใต้ชื่อวิชาและบรรทัดหัวทั้งก้อน

    เขียนทับทั้งก้อนแทนการจับคู่ข้อความเดิม เพราะคำโปรยถูกแก้มาหลายรอบแล้ว
    การไล่จับคู่ของเก่าทุกรุ่นจะพังทันทีที่ลืมรุ่นใดรุ่นหนึ่ง
    """
    before = html
    for pat, new in ((r'(<div class="eyebrow">)(.*?)(</div>)', EYEBROW),
                     (r'(<p class="mast-sub">)(.*?)(</p>)', MAST_NEW)):
        m = re.search(pat, html, re.S)
        if not m:
            raise SystemExit(u'หาหัวเรื่องของหน้าไม่เจอ · %s' % pat)
        if m.group(2) != new:
            html = html[:m.start(2)] + new + html[m.end(2):]
    m = re.search(r'(<footer>\s*<div class="shell">\s*<p>)(.*?)(</p>)', html, re.S)
    if not m:
        raise SystemExit(u'หาย่อหน้าแรกของท้ายหน้าไม่เจอ')
    if m.group(2) != FOOT_NEW:
        html = html[:m.start(2)] + FOOT_NEW + html[m.end(2):]
    return html, (0 if html == before else 1)


# ───────────────────────── ตรวจหลังแทรก ─────────────────────────

def check_js(html):
    u"""ดึงสคริปต์ของหน้าออกมาให้ node ตรวจไวยากรณ์"""
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


def verify(html, chapters, total, q2_total):
    bad = 0
    for ch, title, secs in chapters:
        panel = re.search(r'<div id="%s"[^>]*role="tabpanel".*?(?=\n  <div id="[\w-]+"[^>]*role="tabpanel"|\n  </main>)'
                          % ch, html, re.S)
        if not panel:
            print(u'  %-4s หาแผงในหน้าไม่เจอ' % ch); bad += 1; continue
        got = re.findall(r'<section class="sec" id="(%s-\d+)">' % ch, panel.group(0))
        want = [u'%s-%d' % (ch, i + 1) for i in range(len(secs))]
        if got != want:
            print(u'  %-4s หัวข้อไม่ตรง · มี %s' % (ch, ' '.join(got))); bad += 1
        for sid in want:
            if ('href="#%s"' % sid) not in html:
                print(u'  %-4s แถบข้างไม่มีลิงก์ไป %s' % (ch, sid)); bad += 1
        if ('id="rail-%s"' % ch) not in html:
            print(u'  %-4s ไม่มีแถบข้าง' % ch); bad += 1
        if ('id="t-%s"' % ch) not in html:
            print(u'  %-4s ไม่มีปุ่มแท็บ' % ch); bad += 1
        n = len(re.findall(r'<section class="sec"', panel.group(0)))
        print(u'  %-4s %-44s %2d หัวข้อ' % (ch, title, n))

    # แบบทดสอบสองชุดต้องมีครบทุกชิ้นส่วน และตัวเลขต้องตรงกับคลังจริง
    for need in ('id="t-quiz2"', 'id="quiz2"', 'id="rail-quiz2"', 'id="quiz2-list"',
                 'id="sc2-val"', 'id="sc2-of"', 'id="sc2-reset"', 'var QS2 = ['):
        if need not in html:
            print(u'  แบบทดสอบชุดที่สองขาด %s' % need); bad += 1
    qs = re.search(r'var QS = \[(.*?)\n  \];', html, re.S)
    qs2 = re.search(r'var QS2 = \[(.*?)\n  \];', html, re.S)
    for name, m, want in ((u'คลังรวม', qs, total), (u'คลังหลังมิดเทอม', qs2, q2_total)):
        if not m:
            print(u'  หา%sไม่เจอ' % name); bad += 1; continue
        # จุลภาคสองตัวติดกันทำให้เกิดช่องว่างในอาร์เรย์ ซึ่ง forEach ข้ามให้เงียบ ๆ
        # หน้าเว็บจึงแสดงจำนวนข้อเกินจริงโดยไม่มีอะไรพัง ต้องดักตรงนี้
        if re.search(r',(?:\s|/\*.*?\*/)*,', m.group(1), flags=re.S):
            print(u'  %s มีจุลภาคซ้ำจนเกิดช่องว่างในอาร์เรย์' % name); bad += 1
        n = m.group(1).count(u'{ch:')
        if n != want:
            print(u'  %s มี %d ข้อ แต่หน้าบอกว่า %d ข้อ' % (name, n, want)); bad += 1
        else:
            print(u'  %-10s %d ข้อ' % (name, n))

    for tag in ['section', 'figure', 'table', 'nav']:
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
    ap = argparse.ArgumentParser(description=u'แทรกเนื้อหาหลังมิดเทอมของหลักการตลาด')
    ap.add_argument('--check', action='store_true', help=u'ตรวจอย่างเดียว ไม่เขียนไฟล์')
    a = ap.parse_args()

    import mkpostmid_data as D
    import mkquiz2_data as Q2

    html = io.open(PAGE, encoding='utf-8').read()
    before = len(html)
    steps = 0
    for fn in (patch_css, patch_tabs, patch_railjs, patch_builder, patch_mast):
        html, n = fn(html)
        steps += n
    html, n = patch_rails(html, D.RAILS, Q2.TOTAL); steps += n
    html, n = patch_panels(html, D.PANEL, Q2.TOTAL); steps += n
    html, n = patch_stepjs(html, D.STEPJS); steps += n
    html, n = patch_quiz(html, D.QUIZ, D.QUIZ_TOTAL, Q2.QUIZ2); steps += n

    print(u'ปรับ %d ชิ้น · %d → %d อักษร' % (steps, before, len(html)))
    bad = verify(html, D.CHAPTERS, D.QUIZ_TOTAL, Q2.TOTAL)
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
