#!/usr/bin/env python3
# -*- coding: utf-8 -*-
u"""เพิ่มบทที่ 9 เงินตราต่างประเทศ TAS 21 ลงหน้าการบัญชีขั้นสูง 1

    python3 tools/adv-ch9fx.py            แทรกจริง
    python3 tools/adv-ch9fx.py --check    ตรวจอย่างเดียว ไม่เขียนไฟล์
    python3 tools/adv-ch9fx.py --strip    ลบของที่สคริปต์นี้วางไว้ออกให้หมด

ที่มาของเนื้อหา  เอกสารประกอบการสอน Ch9_2568

แท็บใหม่ใช้ id ว่า fx ไม่ใช่ ch9 เพราะหน้านี้มีแท็บ ch9 อยู่แล้ว
ซึ่งเป็นเรื่องรายการระหว่างบริษัทในเครือ จากเอกสารคนละฉบับที่เรียกตัวเองว่าบทที่ 9 เหมือนกัน

จุดยึดของทุกบล็อกในสคริปต์นี้ คือคอมเมนต์ปิดท้ายของ tools/adv-ch8.py
ไม่ใช่จุดยึดเดียวกับที่ adv-ch8.py ใช้ เหตุผลคือถ้าสองสคริปต์ยึดจุดเดียวกัน
ลำดับของแท็บจะขึ้นกับว่ารันตัวไหนก่อน ซึ่งเป็นกับดักที่ไม่ควรมี
การยึดกับคอมเมนต์ของบทที่ 8 ทำให้บทที่ 9 ต่อท้ายบทที่ 8 เสมอ ไม่ว่าจะรันกี่รอบในลำดับใด

สคริปต์นี้รันซ้ำได้ไม่ซ้อน เพราะคร่อมของที่เพิ่มด้วยคอมเมนต์หัวท้าย
และตรวจให้หลังแทรกว่าหัวข้อครบ ลิงก์ในแถบข้างชี้ถูก แท็กสมดุล
คลังข้อสอบไม่มีช่องว่าง และสคริปต์ของหน้ายังคอมไพล์ได้
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

# ห้ามเขียนไบต์โค้ดลง __pycache__ เพราะ Python ถือว่าไฟล์ต้นทางไม่เปลี่ยน
# เมื่อ mtime กับขนาดเท่าเดิม ตอนแก้ไฟล์ข้อมูลแล้วรันซ้ำภายในวินาทีเดียวกัน
# ถ้าการแก้นั้นไม่ทำให้ขนาดเปลี่ยน เช่น เปลี่ยนชื่อคีย์จาก c เป็น o ซึ่งยาวเท่ากัน
# สคริปต์จะหยิบของเก่าจากแคชมาใช้แบบเงียบ ๆ แล้วผลที่ได้จะไม่ตรงกับไฟล์บนดิสก์
# สคริปต์พวกนี้รันครั้งเดียวจบ แคชไบต์โค้ดจึงไม่ได้ช่วยอะไรอยู่แล้ว
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

CH = 'fx'
NSEC = 18
PRE = 'ch9fx'


def mark(key):
    return (u'<!-- %s:%s:start -->' % (PRE, key), u'<!-- %s:%s:end -->' % (PRE, key))


def jsmark(key):
    return (u'/* %s:%s:start */' % (PRE, key), u'/* %s:%s:end */' % (PRE, key))


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
        raise SystemExit(
            u'หาจุดยึดของ %s ไม่เจอ หรือเจอมากกว่าหนึ่งที่ (%d)\n'
            u'  จุดยึดที่หา  %s\n'
            u'  จุดยึดของบทนี้เป็นคอมเมนต์ที่ tools/adv-ch8.py วางไว้\n'
            u'  ถ้ายังไม่ได้รัน adv-ch8.py ให้รันตัวนั้นก่อน แล้วค่อยรันตัวนี้'
            % (key, html.count(anchor), anchor))
    return (html.replace(anchor, body + anchor) if before
            else html.replace(anchor, anchor + body)), 1


# ───────────────────────── แถบแท็บ ─────────────────────────

TAB = (u'<button class="tab" role="tab" id="t-fx" aria-controls="fx" '
       u'aria-selected="false"><span class="tnum">09</span>เงินตราต่างประเทศ</button>\n    ')

TAB_ANCHOR = u'<!-- ch8:tab:end -->'
RAIL_ANCHOR = u'<!-- ch8:rail:end -->'
PANEL_ANCHOR = u'<!-- ch8:panel:end -->'
RAILJS_ANCHOR = u'/* ch8:rails:end */'
QUIZ_ANCHOR = u'/* ch8:quiz:end */'


def patch_tab(html):
    return splice(html, 'tab', u'\n    ' + TAB.rstrip() + u'\n    ',
                  TAB_ANCHOR, before=False)


def patch_railjs(html):
    return splice(html, 'rails', u" fx:'rail-fx',", RAILJS_ANCHOR,
                  comment=False, before=False)


def patch_rail(html):
    import acct9fx_data as D
    return splice(html, 'rail', u'\n' + D.RAIL + u'    ', RAIL_ANCHOR, before=False)


def patch_panel(html):
    import acct9fx_data as D
    return splice(html, 'panel', u'\n' + D.PANEL + u'\n', PANEL_ANCHOR, before=False)


# ───────────────────────── แบบทดสอบ ─────────────────────────

def patch_quiz(html):
    u"""เติมข้อสอบของบทนี้ต่อท้ายก้อนของบทที่ 8 ในคลัง QS2

    จุลภาคที่คั่นข้อสุดท้ายของบทที่ 8 กับข้อแรกของบทนี้ ต้องอยู่<ข้างใน>
    คอมเมนต์คร่อมของเรา ไม่ใช่ไปแก้ของเดิม เพราะ --strip ลบได้เฉพาะสิ่งที่อยู่
    ในคอมเมนต์คร่อม ถ้าจุลภาคค้างอยู่ข้างนอกจะเหลือช่องว่างในอาร์เรย์
    """
    import advquiz9fx_data as Q
    return splice(html, 'quiz', u',\n' + Q.QUIZ9FX + u'\n  ', QUIZ_ANCHOR,
                  comment=False, before=False)


def bank_len(html, name):
    u"""ให้ node ประเมินคลังข้อสอบจริง แล้วคืนความยาว ช่องว่าง และข้อที่รูปร่างผิด

    การตรวจรูปร่างสำคัญพอ ๆ กับการนับจำนวน เพราะตัวสร้างข้อสอบของหน้านี้
    ใช้คีย์ชื่อ o สำหรับตัวเลือก ไม่ใช่ c ถ้าเขียนผิดคีย์ อาร์เรย์ยังยาวเท่าเดิม
    จำนวนข้อยังตรง แต่หน้าเว็บจะพังตอนโหลดด้วย Cannot read properties of undefined
    ซึ่งจับได้เฉพาะตอนเปิดเบราว์เซอร์จริงเท่านั้น จึงย้ายมาตรวจตั้งแต่ตอนแทรก
    """
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


def patch_quiz_lede(html, total):
    u"""ปรับจำนวนข้อในคำโปรยและในแถบแท็บให้ตรงกับคลังจริง

    ข้อความก้อนนี้มีเจ้าของร่วมกับ tools/adv-ch8.py ซึ่งเขียนตัวเลขเดียวกัน
    เพราะทั้งสองสคริปต์คิดยอดจากโมดูลข้อสอบชุดเดียวกันทั้งหมด
    ผลจึงไม่ขึ้นกับลำดับการรัน ถ้าแก้สูตรที่หนึ่ง ต้องแก้อีกที่ด้วยเสมอ
    """
    before = html
    html = re.sub(u'<b>\\d+ ข้อ เน้นแนวคิด</b>', u'<b>%d ข้อ เน้นแนวคิด</b>' % total, html)
    html = re.sub(u'<i>Q2</i>\\d+ ข้อ', u'<i>Q2</i>%d ข้อ' % total, html)
    return html, (0 if html == before else 1)


def quiz_total():
    import advquiz6_data as Q6
    import advquiz8_data as Q8
    import advquiz9fx_data as Q9
    # 50 ข้อเดิมของชุดหลังมิดเทอม บวกของบทที่ 6 บทที่ 8 และบทที่ 9 ที่ต่อท้ายเข้าไป
    return 50 + Q6.TOTAL + Q8.TOTAL + Q9.TOTAL


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
    bad = 0

    panel = re.search(r'<div id="%s" class="hidden" role="tabpanel".*?\n  </div>' % CH,
                      html, re.S)
    if not panel:
        print(u'  หาแผงของบทเงินตราต่างประเทศไม่เจอ'); return bad + 1
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

    # ลำดับแท็บ ต้องอยู่หลังบทที่ 8 และก่อนแท็บแบบฝึกเขียนตอบ
    order = re.findall(r'id="t-([\w-]+)"', html)
    if 'c8' in order and order.index(CH) < order.index('c8'):
        print(u'  ลำดับแท็บผิด · บทที่ 9 ควรอยู่หลังบทที่ 8'); bad += 1
    if 'ex' in order and order.index(CH) > order.index('ex'):
        print(u'  ลำดับแท็บผิด · บทที่ 9 ควรอยู่ก่อนแท็บแบบฝึกเขียนตอบ'); bad += 1

    # คลาสที่ใช้ในเนื้อหาต้องมีจริงใน CSS ของหน้า ไม่งั้นจะแสดงผลเพี้ยนแบบเงียบ ๆ
    style = re.search(r'<style>(.*?)</style>', html, re.S)
    if style:
        used = set(re.findall(r'class="([^"]+)"', panel.group(0)))
        names = set()
        for u_ in used:
            names.update(u_.split())
        known = set(re.findall(r'\.([a-zA-Z][\w-]*)', style.group(1)))
        # คลาสที่หน้านี้ใช้อยู่แล้วแม้ไม่มีกฎ CSS ของตัวเอง ถือว่าไม่ใช่ของใหม่
        ok_extra = {'key', 'm', 'head-row', 'tot', 'tot2', 'txt'}
        miss = sorted(n for n in names if n not in known and n not in ok_extra)
        if miss:
            print(u'  ใช้คลาสที่ไม่มีใน CSS ของหน้า · %s' % u' '.join(miss)); bad += 1

    tabs = re.findall(r'<button class="tab"[^>]*id="t-([\w-]+)"', html)
    pans = re.findall(r'<div id="([\w-]+)"[^>]*role="tabpanel"', html)
    navs = re.findall(r'<nav id="rail-([\w-]+)"', html)
    print(u'  แท็บ %d · แผง %d · แถบข้าง %d' % (len(tabs), len(pans), len(navs)))
    print(u'  %-4s บทที่ 9 เงินตราต่างประเทศ   %2d หัวข้อ · %d ตาราง'
          % (CH, len(got), len(re.findall(r'<table class="tbl">', panel.group(0)))))

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

    n = len(re.findall(r'\{ch:', re.search(r'var QS2 = \[(.*?)\n  \];', html, re.S).group(1)))
    ln, holes, shape = bank_len(html, 'QS2')
    if ln is None:
        print(u'  คลัง QS2 %d ข้อ · ไม่มี node จึงไม่ได้ตรวจความยาวจริง' % n)
    elif ln < 0:
        bad += 1
    else:
        if holes:
            print(u'  คลัง QS2 มีช่องว่างในอาร์เรย์ %d ช่อง' % holes); bad += 1
        if shape:
            print(u'  คลัง QS2 มีข้อที่รูปร่างผิด · %s' % shape)
            print(u'    อ่านว่า เลขข้อ ตามด้วยคีย์ที่ขาดหรือผิด'
                  u' · ตัวเลือกต้องใช้คีย์ o ไม่ใช่ c')
            bad += 1
        if ln != q2_total or n != q2_total:
            print(u'  คลัง QS2 มี %d ข้อ รันแล้วได้ %d ข้อ แต่หน้าบอกว่า %d ข้อ'
                  % (n, ln, q2_total)); bad += 1
        elif not holes and not shape:
            print(u'  คลัง QS2 %d ข้อ · รันแล้วได้ %d ข้อ ไม่มีช่องว่าง รูปร่างครบทุกข้อ'
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
    ap = argparse.ArgumentParser(description=u'แทรกบทที่ 9 เงินตราต่างประเทศ')
    ap.add_argument('--check', action='store_true', help=u'ตรวจอย่างเดียว ไม่เขียนไฟล์')
    ap.add_argument('--strip', action='store_true', help=u'ลบของที่สคริปต์นี้วางไว้ออก')
    a = ap.parse_args()

    html = io.open(PAGE, encoding='utf-8').read()

    if a.strip:
        html, n = strip(html)
        if not n:
            print(u'ไม่มีบทเงินตราต่างประเทศในหน้าอยู่แล้ว ไม่ต้องลบ')
            return 0
        if a.check:
            print(u'จะลบ %d บล็อก · ยังไม่เขียนไฟล์เพราะสั่ง --check' % n)
            return 0
        io.open(PAGE, 'w', encoding='utf-8').write(html)
        print(u'ลบ %d บล็อกของบทเงินตราต่างประเทศแล้ว' % n)
        return 0

    q2_total = quiz_total()

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
