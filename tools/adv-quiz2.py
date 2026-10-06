#!/usr/bin/env python3
# -*- coding: utf-8 -*-
u"""แยกแบบทดสอบหลังมิดเทอมออกเป็นแท็บของตัวเอง และเน้นคำถามเชิงแนวคิด

    python3 tools/adv-quiz2.py            แก้จริง
    python3 tools/adv-quiz2.py --check    ตรวจอย่างเดียว

สิ่งที่ทำ
  ย้ายข้อสอบบทที่ 6 ถึง 10 ออกจากคลังเดิม คลังเดิมจึงกลับไปเป็นก่อนมิดเทอมล้วน
  เพิ่มคลังใหม่ QS2 ที่เน้นแนวคิด ไม่เน้นคิดเลข
  เพิ่มแท็บและแถบข้างของแบบทดสอบหลังมิดเทอม
  แปลงตัวสร้างข้อสอบให้รับคลังกับชุดรหัสหน้าจอเป็นพารามิเตอร์ จะได้ใช้ซ้ำสองที่

คำถามในคลังใหม่เขียนแบบวัดว่าเข้าใจหลักหรือไม่ เช่น ทำไมถึงทำแบบนั้น
อันไหนต่างจากอันไหน ถ้าเปลี่ยนเงื่อนไขแล้วคำตอบเปลี่ยนไหม
ไม่ใช่การแทนค่าในสูตร ส่วนข้อที่ต้องคำนวณยังอยู่ในคลังเดิมของแต่ละบท
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


def mark(k):
    return (u'<!-- quiz2:%s:start -->' % k, u'<!-- quiz2:%s:end -->' % k)


def jsmark(k):
    return (u'/* quiz2:%s:start */' % k, u'/* quiz2:%s:end */' % k)


def splice(html, key, block, anchor, comment=True, before=True):
    s, e = (mark(key) if comment else jsmark(key))
    body = s + block + e
    old = re.search(re.escape(s) + r'.*?' + re.escape(e), html, re.S)
    if old:
        return (html, 0) if old.group(0) == body else (html[:old.start()] + body + html[old.end():], 1)
    if html.count(anchor) != 1:
        raise SystemExit(u'หาจุดยึดของ %s ไม่เจอ หรือเจอมากกว่าหนึ่งที่' % key)
    return (html.replace(anchor, body + anchor) if before
            else html.replace(anchor, anchor + body)), 1


# ─────────────────── ย้ายข้อสอบหลังมิดเทอมออกจากคลังเดิม ───────────────────

# ชุดรวมยังเก็บข้อสอบของทุกบทไว้เหมือนเดิม รวมถึงข้อที่ต้องคำนวณของบทหลังมิดเทอม
# แท็บใหม่เป็นชุดเสริมที่เน้นแนวคิดล้วน ไม่ได้มาแทนที่ชุดรวม จะได้ไม่เสียของเดิม


# ─────────────────────────── แท็บและแถบข้าง ───────────────────────────

TAB = (u'\n    <button class="tab" role="tab" id="t-quiz2" aria-controls="quiz2" '
       u'aria-selected="false"><span class="tnum">Q2</span>แบบทดสอบหลังมิดเทอม</button>')

RAIL = u"""
    <nav id="rail-quiz2" class="hidden" aria-label="แบบทดสอบหลังมิดเทอม">
      <div class="rail-h">หลังมิดเทอม</div>
      <ol>
        <li><a href="#quiz2-top"><i>Q2</i>%d ข้อ · เน้นแนวคิด</a></li>
      </ol>
    </nav>
"""

PANEL = u"""
  <div id="quiz2" class="hidden" role="tabpanel" aria-labelledby="t-quiz2">
    <div id="quiz2-top"></div>
    <p class="lede"><b>%d ข้อ เน้นแนวคิด</b> ครอบคลุมบทที่ 6 ถึง 10 ซึ่งเป็นเนื้อหาหลังมิดเทอมทั้งหมด ·
      ข้อสอบชุดนี้<b>แทบไม่มีการคิดเลข</b> แต่ถามว่าเข้าใจหลักหรือไม่ เช่น ทำไมมาตรฐานถึงกำหนดแบบนั้น
      เรื่องไหนต่างจากเรื่องไหน และถ้าเปลี่ยนเงื่อนไขแล้วคำตอบเปลี่ยนหรือไม่ ·
      ส่วนข้อที่ต้องคำนวณของบทเหล่านี้อยู่ในแท็บ <b>แบบทดสอบรวม</b> ซึ่งยังครอบคลุมทุกบทตามเดิม · เลือกคำตอบเพื่อดูเฉลยและคำอธิบายทันที ลำดับตัวเลือกสลับใหม่ทุกครั้ง</p>
    <div class="score">
      <span>ตอบถูก <span class="sv" id="sc2-val">0</span> ข้อ · ตอบแล้ว <span class="sv" id="sc2-of">0 จาก %d ข้อ</span></span>
      <button type="button" id="sc2-reset">เริ่มใหม่</button>
    </div>
    <div id="quiz2-list"></div>
  </div>
"""

# ─────────────────────── แปลงตัวสร้างข้อสอบให้ใช้ซ้ำได้ ───────────────────────

OLD_HEAD = u"""  var listEl = document.getElementById('quiz-list');
  var scVal = document.getElementById('sc-val');
  var answered = 0, correct = 0;"""
NEW_HEAD = u"""  var listEl = document.getElementById('quiz-list');"""


def rewire(html, bank_js, total2):
    u"""เปลี่ยนตัวสร้างข้อสอบจากของตายตัวชุดเดียว เป็นฟังก์ชันที่รับคลังมา"""
    i = html.index(u'  function updateScore(){')
    j = html.index(u"    document.getElementById('sc-reset').addEventListener('click', buildQuiz);\n  }", i)
    j = html.index(u'\n  }', j) + len(u'\n  }')
    old = html[i:j]

    body = re.search(r'QS\.forEach\(function\(item, i\)\{(.*)\n    \}\);\n  \}', old, re.S)
    if not body:
        raise SystemExit(u'อ่านตัวสร้างข้อสอบเดิมไม่ออก')
    inner = body.group(1)
    # ตัวสร้างเดิมอ้างชื่อ QS กับ listEl ตรง ๆ ต้องเปลี่ยนเป็นตัวแปรที่ส่งเข้ามา
    inner = inner.replace(u'listEl.appendChild(wrap);', u'el.appendChild(wrap);')

    new = (u"""  /* quiz2:mount:start */
  /* ตัวสร้างข้อสอบใช้ซ้ำได้ รับคลังข้อสอบกับรหัสของช่องบนหน้าจอเข้ามา
     ทำแบบนี้เพราะหน้านี้มีแบบทดสอบสองชุด คือชุดรวม กับชุดหลังมิดเทอมที่เน้นแนวคิด */
  function mountQuiz(bank, elId, valId, ofId, resetId){
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
      bank.forEach(function(item, i){""" + inner + u"""
      });
    }
    build();
    var rb = document.getElementById(resetId);
    if (rb) rb.addEventListener('click', build);
  }
  mountQuiz(QS, 'quiz-list', 'sc-val', 'sc-of', 'sc-reset');
  mountQuiz(QS2, 'quiz2-list', 'sc2-val', 'sc2-of', 'sc2-reset');
  /* quiz2:mount:end */""")

    html = html[:i] + new + html[j:]
    html = html.replace(OLD_HEAD, NEW_HEAD)

    # คลังข้อสอบชุดใหม่ วางต่อท้ายคลังเดิม
    anchor = u'\n  var listEl = document.getElementById(\'quiz-list\');'
    html, _ = splice(html, 'bank', u'\n  var QS2 = [\n' + bank_js + u'  ];\n',
                     anchor, comment=False)
    return html


LEDE1 = (u'<p class="lede">%d ข้อ ครอบคลุมทั้งสิบบทและตัวอย่างครบวงจร '
         u'มีทั้งข้อที่ต้องคำนวณและข้อที่วัดแนวคิด · '
         u'ถ้าต้องการเฉพาะแนวคิดของเนื้อหาหลังมิดเทอม ดูแท็บ <b>แบบทดสอบหลังมิดเทอม</b> · '
         u'เลือกคำตอบเพื่อดูเฉลยและคำอธิบายทันที ลำดับตัวเลือกสลับใหม่ทุกครั้งที่เริ่มทำ</p>')


def patch_counts(html, total1):
    u"""ปรับข้อความของแท็บแบบทดสอบรวมให้ตรงกับจำนวนข้อจริง

    เขียนทับทั้งย่อหน้าแทนการแก้ทีละวลี เพราะการแก้ทีละวลีทำให้รันซ้ำแล้วข้อความงอก
    """
    i = html.index(u'<div id="quiz-top"></div>')
    j = html.index(u'</p>', i) + len(u'</p>')
    k = html.index(u'<p class="lede">', i)
    html = html[:k] + (LEDE1 % total1) + html[j:]
    html = re.sub(u'0 จาก \\d+ ข้อ</span>', u'0 จาก %d ข้อ</span>' % total1, html, count=1)
    html = re.sub(u'<li><a href="#quiz-top"><i>Q</i>[^<]*</a></li>',
                  u'<li><a href="#quiz-top"><i>Q</i>%d ข้อ · ทุกบท</a></li>' % total1, html, count=1)
    return html


def check_js(html):
    node = '/opt/node22/bin/node'
    if not os.path.exists(node):
        print(u'  ไม่มี node ข้ามการตรวจไวยากรณ์'); return 0
    bad = 0
    for i, b in enumerate(re.findall(r'<script>(.*?)</script>', html, re.S)):
        with tempfile.NamedTemporaryFile('w', suffix='.js', delete=False, encoding='utf-8') as f:
            f.write(b); path = f.name
        r = subprocess.run([node, '--check', path], capture_output=True, text=True)
        os.unlink(path)
        if r.returncode:
            print(u'  สคริปต์ก้อนที่ %d พัง · %s' % (i + 1, r.stderr.strip().split('\n')[0])); bad += 1
    return bad


def main():
    ap = argparse.ArgumentParser(description=u'แยกแบบทดสอบหลังมิดเทอม')
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()

    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import advquiz2_data as D

    html = io.open(PAGE, encoding='utf-8').read()
    before = len(html)

    html = html.replace(u'<span class="tnum">Q</span>แบบทดสอบ</button>',
                        u'<span class="tnum">Q</span>แบบทดสอบรวม</button>')
    html, _ = splice(html, 'tab', TAB,
                     u'<span class="tnum">Q</span>แบบทดสอบรวม</button>', before=False)
    rail_anchor = re.search(r'<nav id="rail-quiz" class="hidden".*?</nav>\n', html, re.S)
    if not rail_anchor:
        raise SystemExit(u'หาแถบข้างของแบบทดสอบไม่เจอ')
    html, _ = splice(html, 'rail', RAIL % D.TOTAL, rail_anchor.group(0), before=False)
    html, _ = splice(html, 'panel', PANEL % (D.TOTAL, D.TOTAL),
                     u'    <div id="quiz-list"></div>\n  </div>', before=False)

    old = (u"c4x:'rail-c4x', /* postmid:rails:start */ ch5:'rail-ch5', ch9:'rail-ch9', "
           u"ch6:'rail-ch6', ch7:'rail-ch7', ch8:'rail-ch8', /* postmid:rails:end */ ex:'rail-ex', ")
    if old in html and u"quiz2:'rail-quiz2'" not in html:
        html = html.replace(old, old + u"quiz2:'rail-quiz2', ")
    elif u"quiz2:'rail-quiz2'" not in html:
        raise SystemExit(u'หาตาราง rails ใน JS ไม่เจอ')

    if u'/* quiz2:mount:start */' not in html:
        html = rewire(html, D.QUIZ2, D.TOTAL)

    n1 = len(re.findall(r'\{ch:\d', html[html.rindex('var QS = ['):html.rindex('var QS2 = [')]))
    html = patch_counts(html, n1)

    print(u'ชุดรวม %d ข้อ · ชุดหลังมิดเทอมเน้นแนวคิด %d ข้อ · %d → %d อักษร'
          % (n1, D.TOTAL, before, len(html)))

    bad = check_js(html)
    for tag, want in [('quiz2-list', 1), ('sc2-reset', 1), ('t-quiz2', 1), ('rail-quiz2', 2)]:
        if html.count(tag) < want:
            print(u'  ไม่พบ %s ในหน้า' % tag); bad += 1
    if bad:
        print(u'\nตรวจพบปัญหา %d จุด จึงยังไม่เขียนไฟล์' % bad)
        return 1
    if a.check:
        print(u'\nตรวจผ่าน · ยังไม่เขียนไฟล์เพราะสั่ง --check')
        return 0
    io.open(PAGE, 'w', encoding='utf-8').write(html)
    print(u'\nเขียน adv-acctg-1/index.html แล้ว')
    return 0


if __name__ == '__main__':
    sys.exit(main())
