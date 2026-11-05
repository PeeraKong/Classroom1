#!/usr/bin/env python3
# -*- coding: utf-8 -*-
u"""เพิ่มบทที่ 8 งบกระแสเงินสดรวม ลงหน้าการบัญชีขั้นสูง 1

    python3 tools/adv-ch8.py            แทรกจริง
    python3 tools/adv-ch8.py --check    ตรวจอย่างเดียว ไม่เขียนไฟล์
    python3 tools/adv-ch8.py --strip    ลบของที่สคริปต์นี้วางไว้ออกให้หมด

ที่มาของเนื้อหา  เอกสารประกอบการสอน Ch8_2568

แท็บใหม่วางไว้<b>หลังเส้นคั่น หลังมิดเทอม และก่อนแท็บ ชีท 4_3</b>
เพราะเลขบทเรียงเป็น 06 แล้วจึงเป็น ชีท แล้วจึง 07 ตามที่หน้าเรียงอยู่เดิม

หน้านี้มีบทที่ 8 อยู่แล้วส่วนหนึ่ง คือ งบการเงินรวม กรณีขาดทุน ซึ่งมาจาก
เอกสารชีท 4_3 คนละฉบับกัน จึงไม่ได้เขียนทับของเดิม แต่โยงถึงกันในคำโปรยแทน

สคริปต์นี้รันซ้ำได้ไม่ซ้อน เพราะคร่อมของที่เพิ่มด้วยคอมเมนต์หัวท้าย
และตรวจให้หลังแทรกว่าหัวข้อครบ ลิงก์ในแถบข้างชี้ถูก แท็กสมดุล
และสคริปต์ของหน้ายังคอมไพล์ได้
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

CH = 'c8'
NSEC = 16


def mark(key):
    return (u'<!-- ch8:%s:start -->' % key, u'<!-- ch8:%s:end -->' % key)


def jsmark(key):
    return (u'/* ch8:%s:start */' % key, u'/* ch8:%s:end */' % key)


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


# ───────────────────────── แถบแท็บ ─────────────────────────

TAB = (u'<button class="tab" role="tab" id="t-c8" aria-controls="c8" '
       u'aria-selected="false"><span class="tnum">08</span>งบกระแสเงินสดรวม</button>\n    ')

# วางไว้ก่อนแท็บแบบฝึกเขียนตอบ จึงอยู่ต่อจากแท็บ 07 รายการระหว่างบริษัทในเครือ
# ซึ่งตรงกับลำดับเลขบทที่หน้านี้เรียงอยู่เดิม
TAB_ANCHOR = u'<button class="tab" role="tab" id="t-ex"'


def patch_tab(html):
    return splice(html, 'tab', TAB, TAB_ANCHOR)


def patch_railjs(html):
    return splice(html, 'rails', u" c8:'rail-c8',", u'/* postmid:rails:end */',
                  comment=False, before=False)


def patch_rail(html):
    import acct8_data as D
    return splice(html, 'rail', u'\n' + D.RAIL + u'    ',
                  u'    <nav id="rail-ex" class="hidden"', before=True)


def patch_panel(html):
    import acct8_data as D
    return splice(html, 'panel', u'\n' + D.PANEL + u'\n',
                  u'  <div id="ex" class="hidden" role="tabpanel"', before=True)


# ───────────────────────── แบบทดสอบ ─────────────────────────

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


def patch_quiz(html):
    u"""เติมข้อสอบของบทนี้ท้ายคลังชุดหลังมิดเทอม QS2

    จุลภาคคั่นข้อสุดท้ายของคลังเดิมต้องเติมไว้<ข้างใน>คอมเมนต์คร่อมของเรา
    ไม่ใช่ไปแก้ของเดิม เพราะ --strip ลบได้เฉพาะสิ่งที่อยู่ในคอมเมนต์คร่อม
    ถ้าจุลภาคไปค้างอยู่ข้างนอกจะสะสมทุกรอบจนอาร์เรย์มีช่องว่าง
    """
    import advquiz8_data as Q
    s, e = jsmark('quiz')
    i = html.find(u'var QS2 = [')
    if i < 0:
        raise SystemExit(u'หาคลัง QS2 ไม่เจอ')
    j = html.index(u'\n  ];', i)

    old = re.search(re.escape(s) + r'.*?' + re.escape(e), html, re.S)
    head = html[:old.start()] if old else html[:j]
    lead = u'' if trim_tail(head).endswith(u',') else u','
    body = s + lead + u'\n' + Q.QUIZ8 + u'\n  ' + e

    if old:
        if old.group(0) == body:
            return html, 0
        return html[:old.start()] + body + html[old.end():], 1
    return head + body + html[j:], 1


def bank_len(html, name):
    u"""ให้ node ประเมินคลังข้อสอบจริง แล้วคืนความยาวกับจำนวนช่องว่าง

    ดักด้วย regex ไม่ได้ เพราะจุลภาคซ้ำที่ซ่อนอยู่หลังคอมเมนต์จับยาก
    วิธีที่เถียงไม่ได้คือรันอาร์เรย์นั้นจริงแล้วถาม length กับจำนวนช่องที่ว่าง
    """
    node = '/opt/node22/bin/node'
    if not os.path.exists(node):
        return None, None
    m = re.search(r'(var %s = \[.*?\n  \];)' % name, html, re.S)
    if not m:
        return None, None
    src = m.group(1) + (u'\nvar holes = 0;\nfor (var i = 0; i < %s.length; i++)'
                        u' if (%s[i] === undefined) holes++;\n'
                        u'console.log(%s.length + " " + holes);\n' % (name, name, name))
    with tempfile.NamedTemporaryFile('w', suffix='.js', delete=False, encoding='utf-8') as f:
        f.write(src)
        path = f.name
    r = subprocess.run([node, path], capture_output=True, text=True)
    os.unlink(path)
    if r.returncode:
        print(u'  คลัง %s รันไม่ผ่าน · %s' % (name, r.stderr.strip().split('\n')[0]))
        return -1, -1
    a, b = r.stdout.split()
    return int(a), int(b)


LEDE2_OLD = u'<b>50 ข้อ เน้นแนวคิด</b> ครอบคลุมบทที่ 8 ถึง 10'


def patch_quiz_lede(html, total):
    u"""ปรับจำนวนข้อในคำโปรยและในแถบข้างให้ตรงกับคลังจริง"""
    before = html
    html = re.sub(u'<b>\\d+ ข้อ เน้นแนวคิด</b>', u'<b>%d ข้อ เน้นแนวคิด</b>' % total, html)
    html = re.sub(u'<i>Q2</i>\\d+ ข้อ', u'<i>Q2</i>%d ข้อ' % total, html)
    return html, (0 if html == before else 1)


# ───────────────────── หัวเรื่องและท้ายหน้า ─────────────────────

# คำโปรยใต้ชื่อวิชาไม่ได้แก้ที่นี่ เพราะ tools/adv-ch6.py เป็นเจ้าของข้อความก้อนนั้น
# ถ้าสองสคริปต์เขียนทับกันเอง ผลจะขึ้นกับลำดับการรัน ซึ่งเป็นกับดักที่ไม่ควรมี


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


def verify(html, q2_total):
    import acct8_data as D
    bad = 0

    panel = re.search(r'<div id="%s" class="hidden" role="tabpanel".*?\n  </div>' % CH,
                      html, re.S)
    if not panel:
        print(u'  หาแผงของบทที่ 8 ไม่เจอ'); return bad + 1
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

    # ลำดับแท็บ ต้องอยู่หลังเส้นคั่นหลังมิดเทอม และก่อนแท็บ ชีท 4_3
    order = re.findall(r'id="t-([\w-]+)"', html)
    if 'c8' in order and 'ch9' in order and order.index('c8') < order.index('ch9'):
        print(u'  ลำดับแท็บผิด · บทที่ 8 ควรอยู่หลังแท็บ 07'); bad += 1
    if 'c8' in order and 'ex' in order and order.index('c8') > order.index('ex'):
        print(u'  ลำดับแท็บผิด · บทที่ 8 ควรอยู่ก่อนแท็บแบบฝึกเขียนตอบ'); bad += 1

    # นับจากแท็กจริงเท่านั้น ไม่ใช่นับคำว่า role="tabpanel" ดิบ ๆ
    # เพราะสคริปต์ของหน้าก็มีสตริงนั้นอยู่ด้วย ทำให้ยอดแผงเกินจริงไปหนึ่ง
    tabs = re.findall(r'<button class="tab"[^>]*id="t-([\w-]+)"', html)
    pans = re.findall(r'<div id="([\w-]+)"[^>]*role="tabpanel"', html)
    navs = re.findall(r'<nav id="rail-([\w-]+)"', html)
    print(u'  แท็บ %d · แผง %d · แถบข้าง %d' % (len(tabs), len(pans), len(navs)))
    print(u'  %-4s บทที่ 8 งบกระแสเงินสดรวม   %2d หัวข้อ · %d ตาราง'
          % (CH, len(got), len(re.findall(r'<table class="tbl">', panel.group(0)))))

    # แท็บกับแผงต้องจับคู่กันครบทั้งสองทาง ไม่ใช่แค่ทางเดียว
    for tid in tabs:
        if tid not in pans:
            print(u'  แท็บ %s ไม่มีแผง' % tid); bad += 1
    for pid in pans:
        if pid not in tabs:
            print(u'  แผง %s ไม่มีแท็บ' % pid); bad += 1

    for tag in ['section', 'nav', 'table', 'tbody', 'thead']:
        o = len(re.findall(r'<%s[\s>]' % tag, html))
        c = len(re.findall(r'</%s>' % tag, html))
        if o != c:
            print(u'  แท็ก %s ไม่สมดุล เปิด %d ปิด %d' % (tag, o, c)); bad += 1
    od = len(re.findall(r'<div[\s>]', html))
    cd = len(re.findall(r'</div>', html))
    if od != cd:
        print(u'  แท็ก div ไม่สมดุล เปิด %d ปิด %d' % (od, cd)); bad += 1

    # คลังข้อสอบต้องยาวตรงกับที่หน้าบอก และต้องไม่มีช่องว่างในอาร์เรย์
    # ซึ่ง forEach ข้ามให้เงียบ ๆ ทำให้จำนวนข้อเกินจริงโดยไม่มีอะไรพัง
    n = len(re.findall(r'\{ch:', re.search(r'var QS2 = \[(.*?)\n  \];', html, re.S).group(1)))
    ln, holes = bank_len(html, 'QS2')
    if ln is None:
        print(u'  คลัง QS2 %d ข้อ · ไม่มี node จึงไม่ได้ตรวจความยาวจริง' % n)
    elif ln < 0:
        bad += 1
    else:
        if holes:
            print(u'  คลัง QS2 มีช่องว่างในอาร์เรย์ %d ช่อง' % holes); bad += 1
        if ln != q2_total or n != q2_total:
            print(u'  คลัง QS2 มี %d ข้อ รันแล้วได้ %d ข้อ แต่หน้าบอกว่า %d ข้อ'
                  % (n, ln, q2_total)); bad += 1
        else:
            print(u'  คลัง QS2 %d ข้อ · รันแล้วได้ %d ข้อ ไม่มีช่องว่าง' % (n, ln))

    bad += check_js(html)
    return bad


def strip(html):
    u"""ลบทุกบล็อกที่สคริปต์นี้วางไว้ออก"""
    n = 0
    for pat in (r'<!-- ch8:[\w-]+:start -->.*?<!-- ch8:[\w-]+:end -->',
                r'/\* ch8:[\w-]+:start \*/.*?/\* ch8:[\w-]+:end \*/'):
        html, k = re.subn(pat, u'', html, flags=re.S)
        n += k
    return html, n


def main():
    ap = argparse.ArgumentParser(description=u'แทรกบทที่ 8 ของการบัญชีขั้นสูง 1')
    ap.add_argument('--check', action='store_true', help=u'ตรวจอย่างเดียว ไม่เขียนไฟล์')
    ap.add_argument('--strip', action='store_true', help=u'ลบของที่สคริปต์นี้วางไว้ออก')
    a = ap.parse_args()

    html = io.open(PAGE, encoding='utf-8').read()

    if a.strip:
        html, n = strip(html)
        if not n:
            print(u'ไม่มีบทที่ 8 ในหน้าอยู่แล้ว ไม่ต้องลบ')
            return 0
        if a.check:
            print(u'จะลบ %d บล็อก · ยังไม่เขียนไฟล์เพราะสั่ง --check' % n)
            return 0
        io.open(PAGE, 'w', encoding='utf-8').write(html)
        print(u'ลบ %d บล็อกของบทที่ 8 แล้ว' % n)
        return 0

    import advquiz6_data as Q6
    import advquiz8_data as Q
    # 50 ข้อเดิมของชุดหลังมิดเทอม บวกของบทที่ 6 และบทที่ 8 ที่ต่อท้ายเข้าไป
    q2_total = 50 + Q6.TOTAL + Q.TOTAL

    before = len(html)
    steps = 0
    for fn in (patch_tab, patch_railjs, patch_rail, patch_panel, patch_quiz):
        html, n = fn(html)
        steps += n
    html, n = patch_quiz_lede(html, q2_total); steps += n

    print(u'ปรับ %d ชิ้น · %d → %d อักษร' % (steps, before, len(html)))
    bad = verify(html, q2_total)
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
