#!/usr/bin/env python3
# -*- coding: utf-8 -*-
u"""เพิ่มบทที่ 2 ของวิชาหลักการตลาดลงในหน้าเว็บ

    python3 tools/mk-ch2.py            แทรกจริง
    python3 tools/mk-ch2.py --check    ตรวจอย่างเดียว ไม่เขียนไฟล์
    python3 tools/mk-ch2.py --strip    ลบของที่สคริปต์นี้วางไว้ออกให้หมด

ที่มาของเนื้อหา  Chp 02 PRIN MKGT Strategic Mar V2 2569 · 47 หน้า

บทนี้เป็นเนื้อหา<ก่อนมิดเทอม> จึงแทรกไว้<ระหว่างบทที่ 1 กับบทที่ 3>
ไม่ใช่ต่อท้ายบทที่ 11 และข้อสอบเข้าเฉพาะ<คลังรวม QS> ไม่เข้าคลังหลังมิดเทอม QS2

จุดยึดของแท็บ แถบข้าง และแผง คือตัวบทที่ 3 เอง เพราะบทที่ 1 กับ 3
เป็นของที่หน้านี้มีมาแต่เดิม ไม่ได้ถูกคร่อมด้วยคอมเมนต์ของสคริปต์ไหน
ส่วนสคริปต์แผงเลือกกับคลังข้อสอบยึดกับคอมเมนต์ปิดท้ายของ tools/mk-ch911.py
จึงต้องรัน mk-postmid.py และ mk-ch911.py ให้เสร็จก่อน

สคริปต์นี้รันซ้ำได้ไม่ซ้อน เพราะคร่อมของที่เพิ่มด้วยคอมเมนต์หัวท้าย
และตรวจให้หลังแทรกว่าหัวข้อครบ ลิงก์ในแถบข้างชี้ถูก แท็กสมดุล
คลังข้อสอบไม่มีช่องว่างในอาร์เรย์ รูปร่างของข้อสอบครบทุกข้อ
และสคริปต์ของหน้ายังคอมไพล์ได้

ภาพแปดรูปที่ฝังไว้เป็นแผนภาพเชิงแนวคิดของตำรา Kotler และ Armstrong
คือ Figure 2.1 ถึง 2.8 ไม่ใช่งานโฆษณาหรือภาพถ่ายของบุคคลที่สาม
ส่วนสไลด์ที่เป็นโลโก้แบรนด์และภาพนิ่งจากคลิปวิดีโอ ไม่ได้ฝังเลย
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

CH = 'm2'
NSEC = 15
PRE = 'ch2'


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

TAB = (u'<button class="tab" role="tab" id="t-m2" aria-controls="m2" '
       u'aria-selected="false"><span class="tnum">02</span>กลยุทธ์องค์กรและการตลาด</button>\n    ')

TAB_ANCHOR = u'<button class="tab" role="tab" id="t-m3"'
RAILJS_ANCHOR = u"m3:'rail-m3', "
RAIL_ANCHOR = u'    <nav id="rail-m3"'
PANEL_ANCHOR = u'  <div id="m3" class="hidden" role="tabpanel"'
STEPJS_ANCHOR = u'/* ch911:stepjs:end */'


def patch_tab(html):
    return splice(html, 'tab', TAB, TAB_ANCHOR)


def patch_railjs(html):
    return splice(html, 'rails', u"m2:'rail-m2', ", RAILJS_ANCHOR,
                  comment=False, before=True)


def patch_rail(html):
    import mk2_data as D
    return splice(html, 'rail', u'\n' + D.RAIL, RAIL_ANCHOR)


def patch_panel(html):
    import mk2_data as D
    return splice(html, 'panel', u'\n' + D.PANEL + u'\n', PANEL_ANCHOR)


def patch_stepjs(html):
    import mk2_data as D
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


def patch_quiz(html, total):
    import mkquizch2_data as Q
    before = html
    html, _ = append_bank(html, 'QS', 'quiz', Q.QUIZ)
    # คำโปรยของคลังรวมมีเจ้าของคือ tools/mk-ch911.py จึงแก้เฉพาะตัวเลข
    # ด้วยรูปแบบที่จับทั้งประโยคไม่ได้ แต่จับเฉพาะเลขจำนวนข้อ
    html = re.sub(u'id="sc-of">0 จาก \\d+ ข้อ', u'id="sc-of">0 จาก %d ข้อ' % total, html)
    html = re.sub(u'<i>Q</i>\\d+ ข้อ', u'<i>Q</i>%d ข้อ' % total, html)
    html = re.sub(u'(<div id="quiz-top"></div>\\s*<p class="lede">)\\d+( ข้อ)',
                  u'\\g<1>%d\\g<2>' % total, html, flags=re.S)
    return html, (0 if html == before else 1)


def quiz_total(html):
    u"""จำนวนข้อของคลังรวม นับจากของเดิมในหน้าบวกของบทนี้

    นับจากหน้าก่อนแทรก เพื่อไม่ต้องรู้ว่าบทไหนใส่ไปกี่ข้อ
    """
    import mkquizch2_data as Q
    s, e = jsmark('quiz')
    m = re.search(r'var QS = \[(.*?)\n  \];', html, re.S)
    body = m.group(1)
    mine = re.search(re.escape(s) + r'.*?' + re.escape(e), body, re.S)
    if mine:
        body = body[:mine.start()] + body[mine.end():]
    return len(re.findall(r'\{ch:', body)) + Q.TOTAL


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


def verify(html, total):
    bad = 0

    panel = re.search(r'<div id="%s" class="hidden" role="tabpanel".*?\n  </div>' % CH,
                      html, re.S)
    if not panel:
        print(u'  หาแผงของบทที่ 2 ไม่เจอ'); return bad + 1
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

    # ลำดับแท็บ ต้องอยู่หลังบทที่ 1 และก่อนบทที่ 3
    order = re.findall(r'id="t-([\w-]+)"', html)
    for a, b in (('m1', CH), (CH, 'm3')):
        if a in order and b in order and order.index(a) > order.index(b):
            print(u'  ลำดับแท็บผิด · %s ควรอยู่ก่อน %s' % (a, b)); bad += 1

    # ปุ่มของแผงเลือกต้องมีคู่กับตัวแปรในสคริปต์ ไม่งั้นกดแล้วเงียบ
    for attr, out in (('data-bcg', 'bcg-out'), ('data-pmg', 'pmg-out')):
        n = len(re.findall(r'%s="\d+"' % attr, panel.group(0)))
        if n != 4:
            print(u'  ปุ่ม %s มี %d ปุ่ม ควรมี 4' % (attr, n)); bad += 1
        if ('id="%s"' % out) not in panel.group(0):
            print(u'  ไม่มีกล่องผลลัพธ์ %s' % out); bad += 1
        if ("getElementById('%s')" % out) not in html:
            print(u'  สคริปต์ไม่ได้ผูกกับกล่อง %s' % out); bad += 1

    # ภาพต้องฝังจริง ไม่ใช่เหลือ placeholder ค้างไว้
    left = re.findall(r'src="FIG\w+"', panel.group(0))
    if left:
        print(u'  ยังมีที่วางภาพที่ไม่ได้แทนค่า · %s' % u' '.join(sorted(set(left)))); bad += 1
    nimg = len(re.findall(r'<img loading="lazy"', panel.group(0)))
    if nimg != 8:
        print(u'  ภาพในแผงมี %d รูป ควรมี 8 รูป' % nimg); bad += 1

    tabs = re.findall(r'<button class="tab"[^>]*id="t-([\w-]+)"', html)
    pans = re.findall(r'<div id="([\w-]+)"[^>]*role="tabpanel"', html)
    navs = re.findall(r'<nav id="rail-([\w-]+)"', html)
    print(u'  แท็บ %d · แผง %d · แถบข้าง %d' % (len(tabs), len(pans), len(navs)))
    print(u'  %-4s บทที่ 2 กลยุทธ์องค์กรและการตลาด  %2d หัวข้อ · %d ตาราง · %d ภาพ'
          % (CH, len(got), len(re.findall(r'<table class="tbl">', panel.group(0))), nimg))

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

    n = len(re.findall(r'\{ch:', re.search(r'var QS = \[(.*?)\n  \];', html, re.S).group(1)))
    ln, holes, shape = bank_shape(html, 'QS')
    if ln is None:
        print(u'  คลัง QS %d ข้อ · ไม่มี node จึงไม่ได้ตรวจความยาวจริง' % n)
    elif ln < 0:
        bad += 1
    else:
        if holes:
            print(u'  คลัง QS มีช่องว่างในอาร์เรย์ %d ช่อง' % holes); bad += 1
        if shape:
            print(u'  คลัง QS มีข้อที่รูปร่างผิด · %s' % shape); bad += 1
        if ln != total or n != total:
            print(u'  คลัง QS มี %d ข้อ รันแล้วได้ %d ข้อ แต่หน้าบอกว่า %d ข้อ'
                  % (n, ln, total)); bad += 1
        elif not holes and not shape:
            print(u'  คลัง QS %d ข้อ · รันแล้วได้ %d ข้อ ไม่มีช่องว่าง รูปร่างครบทุกข้อ'
                  % (n, ln))

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
    ap = argparse.ArgumentParser(description=u'แทรกบทที่ 2 ของวิชาหลักการตลาด')
    ap.add_argument('--check', action='store_true', help=u'ตรวจอย่างเดียว ไม่เขียนไฟล์')
    ap.add_argument('--strip', action='store_true', help=u'ลบของที่สคริปต์นี้วางไว้ออก')
    a = ap.parse_args()

    html = io.open(PAGE, encoding='utf-8').read()

    if a.strip:
        html, n = strip(html)
        if not n:
            print(u'ไม่มีบทที่ 2 ในหน้าอยู่แล้ว ไม่ต้องลบ')
            return 0
        if a.check:
            print(u'จะลบ %d บล็อก · ยังไม่เขียนไฟล์เพราะสั่ง --check' % n)
            return 0
        io.open(PAGE, 'w', encoding='utf-8').write(html)
        print(u'ลบ %d บล็อกของบทที่ 2 แล้ว' % n)
        return 0

    total = quiz_total(html)

    before = len(html)
    steps = 0
    for fn in (patch_tab, patch_railjs, patch_rail, patch_panel, patch_stepjs):
        html, n = fn(html)
        steps += n
    html, n = patch_quiz(html, total); steps += n

    print(u'ปรับ %d ชิ้น · %d → %d อักษร' % (steps, before, len(html)))
    bad = verify(html, total)
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
