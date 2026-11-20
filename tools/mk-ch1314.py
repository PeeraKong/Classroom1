#!/usr/bin/env python3
# -*- coding: utf-8 -*-
u"""เพิ่มบทที่ 13-14 ของวิชาหลักการตลาดลงในหน้าเว็บ

    python3 tools/mk-ch1314.py            แทรกจริง
    python3 tools/mk-ch1314.py --check    ตรวจอย่างเดียว ไม่เขียนไฟล์
    python3 tools/mk-ch1314.py --strip    ลบของที่สคริปต์นี้วางไว้ออกให้หมด

ที่มาของเนื้อหา  Final Chp 13 14 PRIN MKGT IMC Per Sell Sales Pro Direct Mar V2 cut 2569 · 63 หน้า

บทนี้เป็นเนื้อหา<หลังมิดเทอม> จึงต่อท้ายบทที่ 12 และข้อสอบเข้า<ทั้งสองคลัง>
คือคลังรวม QS และคลังหลังมิดเทอม QS2

จุดยึดทุกจุดคือคอมเมนต์ปิดท้ายของ tools/mk-ch12.py จึงต้องรัน mk-ch12.py ก่อน
ที่ยึดกับบทที่ 12 ไม่ใช่กับ mk-ch911.py เพราะถ้ายึดจุดเดียวกับบทที่ 12
แล้วรันสลับลำดับ บทที่ 13-14 จะไปแทรกอยู่หน้าบทที่ 12 ซึ่งผิดลำดับบท

สคริปต์นี้รันซ้ำได้ไม่ซ้อน เพราะคร่อมของที่เพิ่มด้วยคอมเมนต์หัวท้าย
และตรวจให้หลังแทรกว่าหัวข้อครบ ลิงก์ในแถบข้างชี้ถูก แท็กสมดุล
คลังข้อสอบทั้งสองคลังไม่มีช่องว่างในอาร์เรย์ รูปร่างของข้อสอบครบทุกข้อ
คลาสที่ใช้มีจริงในสไตล์ของหน้า และสคริปต์ของหน้ายังคอมไพล์ได้

ภาพสามรูปที่ฝังไว้เป็นแผนภาพเชิงแนวคิดของตำรา Kotler และ Armstrong
คือ Figure 14.1 ซึ่งใช้ซ้ำจากบทที่ 12  Figure 16.2 และ Figure 17.1
สไลด์ที่เป็นงานโฆษณาของแบรนด์ ภาพถ่ายบุคคล และภาพนิ่งจากคลิป ไม่ได้ฝังเลย
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

# ห้ามเขียนไบต์โค้ดลง __pycache__ เพราะ Python ถือว่าไฟล์ต้นทางไม่เปลี่ยน
# เมื่อ mtime กับขนาดเท่าเดิม ตอนแก้ไฟล์ข้อมูลแล้วรันซ้ำภายในวินาทีเดียวกัน
# ถ้าการแก้นั้นไม่ทำให้ขนาดเปลี่ยน สคริปต์จะหยิบของเก่าจากแคชมาใช้แบบเงียบ ๆ
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

CH = 'm1314'
NSEC = 18
PRE = 'ch1314'
NIMG = 3
TITLE = u'บทที่ 13-14 ขายโดยบุคคล ส่งเสริมการขาย ตลาดทางตรง'

# ปุ่มของแผงเลือก กับกล่องผลลัพธ์ที่ต้องมีคู่กัน ไม่งั้นกดแล้วเงียบ
WIDGETS = (('data-sell', 'sell-out', 7), ('data-spp', 'spp-out', 5))


def mark(key):
    return (u'<!-- %s:%s:start -->' % (PRE, key), u'<!-- %s:%s:end -->' % (PRE, key))


def jsmark(key):
    return (u'/* %s:%s:start */' % (PRE, key), u'/* %s:%s:end */' % (PRE, key))


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
    u"""วางบล็อกคร่อมคอมเมนต์หัวท้าย ถ้ามีอยู่แล้วให้แทนที่ของเดิม ไม่ใช่ข้ามไป"""
    s, e = (mark(key) if comment else jsmark(key))
    body = s + block + e
    old = re.search(re.escape(s) + r'.*?' + re.escape(e), html, re.S)
    if old:
        if old.group(0) == body:
            return html, 0
        return html[:old.start()] + body + html[old.end():], 1
    if html.count(anchor) != 1:
        raise SystemExit(u'หาจุดยึดของ %s ไม่เจอ หรือเจอมากกว่าหนึ่งที่ (%d)\n  จุดยึด  %s'
                         % (key, html.count(anchor), anchor))
    return (html.replace(anchor, body + anchor) if before
            else html.replace(anchor, anchor + body)), 1


# ───────────────────────── ส่วนที่ 1 · โครงหน้า ─────────────────────────

TAB = (u'<button class="tab" role="tab" id="t-m1314" aria-controls="m1314" '
       u'aria-selected="false"><span class="tnum">13-14</span>ขายตรงและส่งเสริมการขาย</button>\n  ')

# ทุกจุดยึดเป็นคอมเมนต์ปิดท้ายของ tools/mk-ch12.py และแทรก<หลัง>จุดยึด
TAB_ANCHOR = u'<!-- ch12:tab:end -->'
RAILJS_ANCHOR = u'/* ch12:rails:end */'
RAIL_ANCHOR = u'<!-- ch12:rail:end -->'
PANEL_ANCHOR = u'<!-- ch12:panel:end -->'
STEPJS_ANCHOR = u'/* ch12:stepjs:end */'


def patch_tab(html):
    return splice(html, 'tab', TAB, TAB_ANCHOR, before=False)


def patch_railjs(html):
    return splice(html, 'rails', u"m1314:'rail-m1314', ", RAILJS_ANCHOR,
                  comment=False, before=False)


def patch_rail(html):
    import mk1314_data as D
    return splice(html, 'rail', u'\n' + D.RAIL, RAIL_ANCHOR, before=False)


def patch_panel(html):
    import mk1314_data as D
    return splice(html, 'panel', u'\n' + D.PANEL + u'\n', PANEL_ANCHOR, before=False)


def patch_stepjs(html):
    import mk1314_data as D
    return splice(html, 'stepjs', D.STEPJS, STEPJS_ANCHOR,
                  comment=False, before=False)


# ───────────────────────── ส่วนที่ 2 · แบบทดสอบ ─────────────────────────

def append_bank(html, name, key, items):
    u"""เติมข้อสอบท้ายคลังที่ชื่อ name โดยคร่อมคอมเมนต์ให้รันซ้ำได้

    จุลภาคที่คั่นข้อสุดท้ายของคลังเดิมกับข้อแรกของเรา ต้องอยู่<ข้างใน>
    คอมเมนต์คร่อมของเรา ไม่ใช่ไปแก้ของเดิม เพราะ --strip ลบได้เฉพาะสิ่งที่อยู่
    ในคอมเมนต์คร่อม ถ้าจุลภาคค้างอยู่ข้างนอกจะเหลือช่องว่างในอาร์เรย์
    """
    s, e = jsmark(key)
    i = html.find(u'var %s = [' % name)
    if i < 0:
        raise SystemExit(u'หาคลัง %s ไม่เจอ' % name)
    j = html.index(u'\n  ];', i)

    old = re.search(re.escape(s) + r'.*?' + re.escape(e), html, re.S)
    head = html[:old.start()] if old else html[:j]
    lead = u'' if trim_tail(head).endswith(u',') else u','
    body = s + lead + u'\n' + items + u'\n  ' + e

    if old:
        if old.group(0) == body:
            return html, 0
        return html[:old.start()] + body + html[old.end():], 1
    return head + body + html[j:], 1


def patch_quiz(html, total, q2_total):
    import mkquiz1314_data as Q
    before = html
    html, _ = append_bank(html, 'QS', 'quiz', Q.QUIZ)
    html, _ = append_bank(html, 'QS2', 'quiz2', Q.QUIZ2)
    # คำโปรยของทั้งสองคลังมีเจ้าของคือ tools/mk-ch911.py จึงแก้เฉพาะตัวเลข
    # ด้วยรูปแบบที่จับทั้งประโยคไม่ได้ แต่จับเฉพาะเลขจำนวนข้อ
    html = re.sub(u'id="sc-of">0 จาก \\d+ ข้อ', u'id="sc-of">0 จาก %d ข้อ' % total, html)
    html = re.sub(u'id="sc2-of">0 จาก \\d+ ข้อ', u'id="sc2-of">0 จาก %d ข้อ' % q2_total, html)
    html = re.sub(u'<i>Q</i>\\d+ ข้อ', u'<i>Q</i>%d ข้อ' % total, html)
    html = re.sub(u'<i>Q2</i>\\d+ ข้อ', u'<i>Q2</i>%d ข้อ' % q2_total, html)
    html = re.sub(u'(<div id="quiz-top"></div>\\s*<p class="lede">)\\d+( ข้อ)',
                  u'\\g<1>%d\\g<2>' % total, html, flags=re.S)
    html = re.sub(u'(<div id="quiz2-top"></div>\\s*<p class="lede">)\\d+( ข้อ)',
                  u'\\g<1>%d\\g<2>' % q2_total, html, flags=re.S)
    return html, (0 if html == before else 1)


def bank_total(html, name, key, mine):
    u"""จำนวนข้อของคลังหนึ่ง นับจากของเดิมในหน้าบวกของบทนี้

    นับจากหน้าก่อนแทรก เพื่อไม่ต้องรู้ว่าบทไหนใส่ไปกี่ข้อ
    """
    s, e = jsmark(key)
    m = re.search(r'var %s = \[(.*?)\n  \];' % name, html, re.S)
    if not m:
        raise SystemExit(u'หาคลัง %s ไม่เจอ' % name)
    body = m.group(1)
    got = re.search(re.escape(s) + r'.*?' + re.escape(e), body, re.S)
    if got:
        body = body[:got.start()] + body[got.end():]
    return len(re.findall(r'\{ch:', body)) + mine


# ───────────────────────── ส่วนที่ 3 · ตรวจหลังแทรก ─────────────────────────

def bank_shape(html, name):
    u"""ให้ node ประเมินคลังข้อสอบจริง แล้วคืนความยาว ช่องว่าง และข้อที่รูปร่างผิด"""
    node = '/opt/node22/bin/node'
    if not os.path.exists(node):
        return None, None, None
    m = re.search(r'(var %s = \[.*?\n  \];)' % name, html, re.S)
    if not m:
        return None, None, None
    src = m.group(1) + (u"""
var holes = 0, bad = [];
for (var i = 0; i < %(n)s.length; i++) {
  var it = %(n)s[i];
  if (it === undefined) { holes++; continue; }
  var why = [];
  if (typeof it.q !== 'string' || !it.q) why.push('q');
  if (typeof it.e !== 'string' || !it.e) why.push('e');
  if (it.ch === undefined || it.ch === null || it.ch === '') why.push('ch');
  if (!Array.isArray(it.o) || it.o.length < 2) why.push('o');
  else if (typeof it.a !== 'number' || it.a < 0 || it.a >= it.o.length) why.push('a');
  else if (it.o.some(function (x) { return typeof x !== 'string' || !x; })) why.push('o-ว่าง');
  if (why.length) bad.push((i + 1) + ':' + why.join('/'));
}
console.log(%(n)s.length + ' ' + holes + ' ' + (bad.join(',') || '-'));
""" % {'n': name})
    with tempfile.NamedTemporaryFile('w', suffix='.js', delete=False, encoding='utf-8') as f:
        f.write(src)
        path = f.name
    r = subprocess.run([node, path], capture_output=True, text=True)
    os.unlink(path)
    if r.returncode:
        print(u'  คลัง %s รันไม่ผ่าน · %s' % (name, r.stderr.strip().split('\n')[0]))
        return -1, -1, None
    a, b, c = r.stdout.split(None, 2)
    c = c.strip()
    return int(a), int(b), (None if c == '-' else c)


def check_bank(html, name, want):
    bad = 0
    m = re.search(r'var %s = \[(.*?)\n  \];' % name, html, re.S)
    if not m:
        print(u'  หาคลัง %s ไม่เจอ' % name)
        return bad + 1
    n = len(re.findall(r'\{ch:', m.group(1)))
    ln, holes, shape = bank_shape(html, name)
    if ln is None:
        print(u'  คลัง %s %d ข้อ · ไม่มี node จึงไม่ได้ตรวจความยาวจริง' % (name, n))
        return bad
    if ln < 0:
        return bad + 1
    if holes:
        print(u'  คลัง %s มีช่องว่างในอาร์เรย์ %d ช่อง' % (name, holes)); bad += 1
    if shape:
        print(u'  คลัง %s มีข้อที่รูปร่างผิด · %s' % (name, shape)); bad += 1
    if ln != want or n != want:
        print(u'  คลัง %s มี %d ข้อ รันแล้วได้ %d ข้อ แต่หน้าบอกว่า %d ข้อ'
              % (name, n, ln, want)); bad += 1
    elif not holes and not shape:
        print(u'  คลัง %s %d ข้อ · รันแล้วได้ %d ข้อ ไม่มีช่องว่าง รูปร่างครบทุกข้อ'
              % (name, n, ln))
    return bad


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


def verify(html, total, q2_total):
    bad = 0

    panel = re.search(r'<div id="%s" class="hidden" role="tabpanel".*?\n  </div>' % CH,
                      html, re.S)
    if not panel:
        print(u'  หาแผงของบทที่ 13-14 ไม่เจอ'); return bad + 1
    got = re.findall(r'<section class="sec" id="(%s-\d+)">' % CH, panel.group(0))
    want = [u'%s-%d' % (CH, i + 1) for i in range(NSEC)]
    if got != want:
        print(u'  หัวข้อไม่ตรง · มี %d ควรมี %d' % (len(got), NSEC)); bad += 1
    for sid in want:
        if ('href="#%s"' % sid) not in html:
            print(u'  แถบข้างไม่มีลิงก์ไป %s' % sid); bad += 1

    for need in ('id="rail-%s"' % CH, 'id="t-%s"' % CH, "%s:'rail-%s'" % (CH, CH)):
        if need not in html:
            print(u'  ขาด %s' % need); bad += 1

    nav = re.search(r'<nav id="rail-%s".*?</nav>' % CH, html, re.S)
    if nav and len(re.findall(r'<li>', nav.group(0))) != NSEC:
        print(u'  จำนวนลิงก์ในแถบข้างไม่เท่าจำนวนหัวข้อ'); bad += 1

    # ลำดับแท็บ ต้องอยู่หลังบทที่ 12 และก่อนแท็บแบบทดสอบ
    order = re.findall(r'id="t-([\w-]+)"', html)
    for a, b in (('m12', CH), (CH, 'quiz')):
        if a in order and b in order and order.index(a) > order.index(b):
            print(u'  ลำดับแท็บผิด · %s ควรอยู่ก่อน %s' % (a, b)); bad += 1

    # ปุ่มของแผงเลือกต้องมีคู่กับตัวแปรในสคริปต์ ไม่งั้นกดแล้วเงียบ
    for attr, out, cnt in WIDGETS:
        n = len(re.findall(r'%s="\d+"' % attr, panel.group(0)))
        if n != cnt:
            print(u'  ปุ่ม %s มี %d ปุ่ม ควรมี %d' % (attr, n, cnt)); bad += 1
        if ('id="%s"' % out) not in panel.group(0):
            print(u'  ไม่มีกล่องผลลัพธ์ %s' % out); bad += 1
        if ("getElementById('%s')" % out) not in html:
            print(u'  สคริปต์ไม่ได้ผูกกับกล่อง %s' % out); bad += 1

    # ภาพต้องฝังจริง ไม่ใช่เหลือ placeholder ค้างไว้
    left = re.findall(r'src="FIG\w+"', panel.group(0))
    if left:
        print(u'  ยังมีที่วางภาพที่ไม่ได้แทนค่า · %s' % u' '.join(sorted(set(left)))); bad += 1
    nimg = len(re.findall(r'<img loading="lazy"', panel.group(0)))
    if nimg != NIMG:
        print(u'  ภาพในแผงมี %d รูป ควรมี %d รูป' % (nimg, NIMG)); bad += 1

    # คลาสที่ใช้ต้องมีจริงในสไตล์ของหน้า ไม่งั้นกล่องจะกลายเป็นข้อความเปล่า
    css = re.search(r'<style>(.*?)</style>', html, re.S)
    if css:
        for cls in sorted(set(re.findall(r'class="([\w\- ]+)"', panel.group(0)))):
            for one in cls.split():
                if one in ('hidden',):
                    continue
                if (u'.%s' % one) not in css.group(1):
                    print(u'  คลาส %s ไม่มีในสไตล์ของหน้า' % one); bad += 1

    tabs = re.findall(r'<button class="tab"[^>]*id="t-([\w-]+)"', html)
    pans = re.findall(r'<div id="([\w-]+)"[^>]*role="tabpanel"', html)
    navs = re.findall(r'<nav id="rail-([\w-]+)"', html)
    print(u'  แท็บ %d · แผง %d · แถบข้าง %d' % (len(tabs), len(pans), len(navs)))
    print(u'  %-6s %s  %2d หัวข้อ · %d ตาราง · %d ภาพ'
          % (CH, TITLE, len(got),
             len(re.findall(r'<table class="tbl">', panel.group(0))), nimg))

    for tid in tabs:
        if tid not in pans:
            print(u'  แท็บ %s ไม่มีแผง' % tid); bad += 1
    for pid in pans:
        if pid not in tabs:
            print(u'  แผง %s ไม่มีแท็บ' % pid); bad += 1

    for tag in ['section', 'nav', 'table', 'tbody', 'thead', 'figure', 'figcaption']:
        o = len(re.findall(r'<%s[\s>]' % tag, html))
        c = len(re.findall(r'</%s>' % tag, html))
        if o != c:
            print(u'  แท็ก %s ไม่สมดุล เปิด %d ปิด %d' % (tag, o, c)); bad += 1
    od = len(re.findall(r'<div[\s>]', html))
    cd = len(re.findall(r'</div>', html))
    if od != cd:
        print(u'  แท็ก div ไม่สมดุล เปิด %d ปิด %d' % (od, cd)); bad += 1

    bad += check_bank(html, 'QS', total)
    bad += check_bank(html, 'QS2', q2_total)
    bad += check_js(html)
    return bad


def strip(html):
    n = 0
    for pat in (r'<!-- %s:[\w-]+:start -->.*?<!-- %s:[\w-]+:end -->' % (PRE, PRE),
                r'/\* %s:[\w-]+:start \*/.*?/\* %s:[\w-]+:end \*/' % (PRE, PRE)):
        html, k = re.subn(pat, u'', html, flags=re.S)
        n += k
    return html, n


def main():
    ap = argparse.ArgumentParser(description=u'แทรกบทที่ 13-14 ของวิชาหลักการตลาด')
    ap.add_argument('--check', action='store_true', help=u'ตรวจอย่างเดียว ไม่เขียนไฟล์')
    ap.add_argument('--strip', action='store_true', help=u'ลบของที่สคริปต์นี้วางไว้ออก')
    a = ap.parse_args()

    html = io.open(PAGE, encoding='utf-8').read()

    if a.strip:
        html, n = strip(html)
        if not n:
            print(u'ไม่มีบทที่ 13-14 ในหน้าอยู่แล้ว ไม่ต้องลบ')
            return 0
        if a.check:
            print(u'จะลบ %d บล็อก · ยังไม่เขียนไฟล์เพราะสั่ง --check' % n)
            return 0
        io.open(PAGE, 'w', encoding='utf-8').write(html)
        print(u'ลบ %d บล็อกของบทที่ 13-14 แล้ว' % n)
        return 0

    import mkquiz1314_data as Q
    total = bank_total(html, 'QS', 'quiz', Q.TOTAL)
    q2_total = bank_total(html, 'QS2', 'quiz2', Q.TOTAL2)

    before = len(html)
    steps = 0
    for fn in (patch_tab, patch_railjs, patch_rail, patch_panel, patch_stepjs):
        html, n = fn(html)
        steps += n
    html, n = patch_quiz(html, total, q2_total); steps += n

    print(u'ปรับ %d ชิ้น · %d → %d อักษร' % (steps, before, len(html)))
    bad = verify(html, total, q2_total)
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
