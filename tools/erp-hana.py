#!/usr/bin/env python3
# -*- coding: utf-8 -*-
u"""ฝังเนื้อหาฐานข้อมูลของ SAP กับ HANA และ S4HANA ลงหน้าวิชา ERP

    python3 tools/erp-hana.py            ตรวจแล้วฝัง
    python3 tools/erp-hana.py --check    ตรวจอย่างเดียว ไม่เขียนไฟล์
    python3 tools/erp-hana.py --strip    ถอนของที่ฝังไว้ออกให้หมด

หน้า erp/index.html เดิมเขียนมือทั้งหน้า ไม่มีเครื่องหมายคั่นให้ฝังซ้ำได้
ตัวนี้จึงเป็นตัวแรกที่วางเครื่องหมาย <!-- hn:...:start --> ลงหน้านั้น

รวมทุกหน่วยไว้ในตัวสร้างตัวเดียวด้วยเหตุผลเดียวกับ tools/audit-postmid.py
คือถ้าแยกเป็นตัวสร้างหน่วยละตัว แต่ละตัวต้องรู้ว่าตัวเองต่อท้ายใคร
แล้วลำดับการรันจะกลายเป็นกับดัก เพิ่มหน่วยใหม่คือเพิ่มบรรทัดใน UNITS

หน่วยทั้งสองไม่ต้องเพิ่ม CSS เลย เพราะหน้านี้มีคลาสที่ต้องใช้ครบอยู่แล้ว
ได้แก่ note กับ note key กับ note src · tbl กับ td.pc · card · flow · grid
list · ol.tl ที่มี ty กับ tt กับ td · mono · en · cap
"""

import argparse
import importlib.util
import io
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PAGE = os.path.join(ROOT, 'erp', 'index.html')
NODE = '/opt/node22/bin/node' if os.path.exists('/opt/node22/bin/node') else 'node'

# หน่วยเนื้อหาใหม่ เรียงตามลำดับที่อยากให้แท็บเรียงในหน้า
UNITS = [
    {'mod': 'erp_db_data', 'id': 'db', 'num': u'04', 'label': u'ฐานข้อมูลของ SAP'},
    {'mod': 'erp_hana_data', 'id': 'hana', 'num': u'05', 'label': u'HANA และ S/4HANA'},
]

# ---- จุดวางของแต่ละก้อน ต้องมีอยู่จริงในหน้า ไม่งั้นหยุดทันที ----
A_TAB = u'    <button class="tab" role="tab" id="t-tcode" aria-controls="tcode"'
A_RAIL = u'    <nav id="rail-tcode" class="hidden" aria-label="รวม T-Code">'
A_PANEL = u'  <div id="tcode" class="hidden" role="tabpanel" aria-labelledby="t-tcode">'
A_RAILJS = u'  var rails = {'
A_QUIZ_HEAD = u'  var QS = ['
A_QUIZ_TAIL = u'\n  ];'

# ข้อความหัวหน้าเว็บ ปรับให้บอกว่ามีเนื้อหาใหม่แล้ว
EYEBROW_OLD = u'Enterprise Resource Planning · SAP'
SUB_TAIL = (u' · ฐานข้อมูลของระบบ SAP ตั้งแต่ AnyDB จนถึง SAP HANA'
            u' และ SAP S/4HANA รุ่นที่สี่ของ Business Suite')
META_TAIL = (u' รวมถึงฐานข้อมูลของระบบ SAP ทั้ง AnyDB และ SAP HANA'
             u' และ SAP S/4HANA')
FOOT_OLD = u'<i>SAP ERP Implementation Project</i> (24 หน้า)'
FOOT_NEW = (u'<i>SAP ERP Implementation Project</i> (24 หน้า) · '
            u'<i>Traditional RDBMS in SAP System AnyDB</i> (12 หน้า) · '
            u'<i>SAP Business Suite 7</i> (13 หน้า) · '
            u'<i>SAP HANA Overview</i> (32 หน้า) · '
            u'<i>SAP S/4HANA Overview</i> (39 หน้า)')


def mark(key):
    return u'<!-- hn:%s:start -->' % key, u'<!-- hn:%s:end -->' % key


def jsmark(key):
    return u'/* hn:%s:start */' % key, u'/* hn:%s:end */' % key


def load(name):
    path = os.path.join(HERE, name + '.py')
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    for attr in ('RAIL', 'PANEL'):
        if not getattr(mod, attr, None):
            raise SystemExit(u'ไฟล์ %s ไม่มีตัวแปร %s' % (name, attr))
    return mod


def before(html, key, anchor):
    at = html.find(anchor)
    if at < 0:
        raise SystemExit(u'หาจุดวาง %s ในหน้าไม่เจอ · %s' % (key, anchor[:70]))
    return at


def after(html, key, anchor):
    return before(html, key, anchor) + len(anchor)


def in_code(html, i):
    u"""จริงเมื่อตำแหน่ง i อยู่ข้างใน style หรือ script

    ใช้กันพลาดเรื่องชนิดของเครื่องหมายคั่น · เคยพลาดมาแล้วตอนวางเครื่องหมาย
    แบบ HTML ลงกลางบล็อก style ซึ่งตัวอ่าน CSS มองเห็น -->.layout{...}
    เป็นกฎเดียวกันทั้งก้อน แล้วกลืนกฎถัดไปหายไปโดยไม่มีข้อความเตือนอะไรเลย
    """
    for tag in ('style', 'script'):
        for m in re.finditer(r'<%s[^>]*>(.*?)</%s>' % (tag, tag), html, re.S):
            if m.start(1) <= i <= m.end(1):
                return True
    return False


def splice(html, key, body, at, js=False):
    u"""วางก้อน body ไว้ในเครื่องหมายของ key ถ้ามีอยู่แล้วให้แทนที่ของเดิม"""
    s, e = (jsmark if js else mark)(key)
    block = s + body + e
    old = re.search(re.escape(s) + r'.*?' + re.escape(e), html, re.S)
    if old:
        return ((html, False) if old.group(0) == block
                else (html[:old.start()] + block + html[old.end():], True))
    i = at(html, key)
    if in_code(html, i) != js:
        raise SystemExit(
            u'เครื่องหมายคั่นของ %s ผิดชนิด · จุดวางอยู่%sบล็อก style หรือ script '
            u'แต่ใช้เครื่องหมายแบบ%s' % (key, u'ใน' if not js else u'นอก',
                                        u'HTML' if not js else u'CSS หรือ JS'))
    return html[:i] + block + html[i:], True


def build_tabs():
    out = []
    for u_ in UNITS:
        out.append(u'\n    <button class="tab" role="tab" id="t-%s" aria-controls="%s"'
                   u' aria-selected="false"><span class="tnum">%s</span>%s</button>'
                   % (u_['id'], u_['id'], u_['num'], u_['label']))
    return u''.join(out) + u'\n'


def patch_text(html):
    u"""ปรับคำโปรยหัวหน้าเว็บ meta และท้ายหน้า ให้ครอบเนื้อหาใหม่

    ไม่ได้ใช้เครื่องหมายคั่น เพราะเป็นการแก้ข้อความในที่เดิม
    จึงเช็กก่อนว่าแก้ไปแล้วหรือยัง แล้วค่อยแก้ เพื่อให้รันซ้ำได้
    """
    n = 0
    if SUB_TAIL not in html:
        m = re.search(r'(<p class="mast-sub">)(.*?)(</p>)', html, re.S)
        if not m:
            raise SystemExit(u'หา mast-sub ไม่เจอ')
        html = html[:m.end(2)] + SUB_TAIL + html[m.end(2):]
        n += 1
    if META_TAIL not in html:
        before_ = html
        html = re.sub(r'(content="สื่อประกอบการเรียนระบบวางแผนทรัพยากรองค์กร[^"]*?)(")',
                      lambda m: m.group(1) + META_TAIL + m.group(2), html)
        if html != before_:
            n += 1
        else:
            print(u'เตือน · หาคำบรรยายหน้าใน meta ไม่เจอ จึงไม่ได้แก้')
    if FOOT_NEW not in html:
        if FOOT_OLD not in html:
            raise SystemExit(u'หารายชื่อเอกสารท้ายหน้าไม่เจอ')
        html = html.replace(FOOT_OLD, FOOT_NEW)
        n += 1
    return html, n


def insert(html):
    moved = 0
    html, ch = splice(html, 'tabs', build_tabs(),
                      lambda h, k: before(h, k, A_TAB)); moved += ch

    rails = u'\n' + u''.join(load(u_['mod']).RAIL for u_ in UNITS)
    html, ch = splice(html, 'rail', rails,
                      lambda h, k: before(h, k, A_RAIL)); moved += ch

    panels = u'\n' + u'\n'.join(load(u_['mod']).PANEL for u_ in UNITS)
    html, ch = splice(html, 'panel', panels,
                      lambda h, k: before(h, k, A_PANEL)); moved += ch

    # แผนที่บอกว่าแท็บไหนใช้แถบนำทางอันไหน ต้องเพิ่มชื่อหน่วยใหม่เข้าไปด้วย
    # ไม่งั้นกดแท็บแล้วแถบซ้ายจะว่างเปล่า
    js = u''.join(u"%s:'rail-%s', " % (u_['id'], u_['id']) for u_ in UNITS)
    html, ch = splice(html, 'railjs', js,
                      lambda h, k: after(h, k, A_RAILJS), js=True); moved += ch

    # ต่อข้อสอบเข้าไปท้ายอาร์เรย์ QS ที่มีอยู่แล้วในหน้า
    # เครื่องหมายคั่นอยู่ข้างในอาร์เรย์ ทั้งจุลภาคที่คั่นจากข้อสุดท้ายของเดิม
    # จึงถอนออกแล้วหน้ากลับไปเหมือนเดิมเป๊ะ ไม่เหลือจุลภาคค้าง
    quiz = __import__('erp_hana_quiz')
    html, ch = splice(html, 'quiz', u',' + quiz.QUIZ,
                      lambda h, k: before(h, k, A_QUIZ_TAIL), js=True); moved += ch

    html, n = patch_text(html); moved += n
    html, n = retally(html, quiz_len(html)); moved += n
    return html, moved


# จำนวนข้อสอบถูกเขียนเป็นตัวเลขไว้ในหน้าสองจุด
# ถ้าปล่อยให้แก้มือ พอเพิ่มข้อสอบทีไรตัวเลขจะค้างอยู่ที่ของเดิมทุกที
TALLY = [
    (r'<p class="lede">\d+ ข้อ ', u'<p class="lede">{n} ข้อ '),
    (r'<span class="sv" id="sc-of">0 จาก \d+ ข้อ</span>',
     u'<span class="sv" id="sc-of">0 จาก {n} ข้อ</span>'),
]


def retally(html, n):
    u"""เขียนจำนวนข้อสอบลงในหน้า และนับเฉพาะจุดที่ค่าเปลี่ยนจริง

    ต้องเทียบข้อความก่อนและหลัง ไม่ใช่นับจำนวนครั้งที่ regex เจอ
    ไม่งั้นรันซ้ำทีไรก็รายงานว่าเปลี่ยนทุกครั้ง ทั้งที่เขียนทับด้วยเลขเดิม
    """
    hit = 0
    for pat, tpl in TALLY:
        out, k = re.subn(pat, tpl.format(n=n), html)
        if not k:
            print(u'เตือน · หาที่เขียนจำนวนข้อสอบไม่เจอ · %s' % pat)
        elif out != html:
            hit += 1
        html = out
    return html, hit


def quiz_len(html):
    u"""นับจำนวนข้อสอบจริงด้วยการให้ node รันอาร์เรย์นั้นจริง ๆ

    ไม่ได้นับด้วย regex เพราะถ้าอาร์เรย์มีรูโหว่จากจุลภาคซ้อน
    regex จะนับได้เท่าเดิมแต่หน้าเว็บจะพัง · การรันจริงจับได้ทั้งสองอย่าง
    """
    i = html.index(A_QUIZ_HEAD)
    j = html.index(A_QUIZ_TAIL, i) + len(A_QUIZ_TAIL)
    src = html[i:j].replace(u'var QS =', u'var QS =', 1)
    tmp = os.path.join(HERE, '_qs_check.js')
    io.open(tmp, 'w', encoding='utf-8').write(
        src + u'\nvar holes = QS.filter(function(x){return !x || !x.q;}).length;'
              u'\nconsole.log(QS.length + " " + holes);\n')
    try:
        out = subprocess.run([NODE, tmp], capture_output=True, text=True)
    finally:
        os.remove(tmp)
    if out.returncode != 0:
        raise SystemExit(u'คลังข้อสอบรันไม่ผ่าน · %s' % out.stderr.strip()[:400])
    n, holes = out.stdout.split()
    if int(holes):
        raise SystemExit(u'คลังข้อสอบมีรูโหว่ %s ช่อง · น่าจะมีจุลภาคซ้อนกัน' % holes)
    return int(n)


def strip(html):
    html = re.sub(r'<!-- hn:\w+:start -->.*?<!-- hn:\w+:end -->', u'', html, flags=re.S)
    html = re.sub(r'/\* hn:\w+:start \*/.*?/\* hn:\w+:end \*/', u'', html, flags=re.S)
    html = html.replace(SUB_TAIL, u'')
    html = html.replace(META_TAIL, u'')
    html = html.replace(FOOT_NEW, FOOT_OLD)
    # จำนวนข้อสอบต้องเขียนกลับตามคลังที่เหลือจริงหลังถอนของใหม่ออกแล้ว
    # ไม่งั้นหน้าจะค้างเลขของตอนที่ยังมีข้อสอบชุดใหม่อยู่
    html, _ = retally(html, quiz_len(html))
    return html


# ---------------------------------------------------------------- ตรวจ

# คลาสที่หน้านี้มีอยู่แล้ว หน่วยใหม่ใช้ได้เฉพาะในรายการนี้
# เพราะตัวสร้างไม่ได้เพิ่ม CSS ให้เลย ใช้คลาสนอกรายการแล้วจะไม่มีหน้าตา
OK_CLASSES = set(u"""
 sec sec-h sec-n body lede note key src nh list cap en mono rail-h
 tw tbl pc grp dim hit card cn ct cs grid g2 g3 flow fstep fn ft fd
 tl tt td ty hidden fig plate switch reveal rc
""".split())


def check_data():
    bad = 0
    for u_ in UNITS:
        cid = u_['id']
        mod = load(u_['mod'])
        rail, panel = mod.RAIL, mod.PANEL

        links = re.findall(r'href="#([^"]+)"', rail)
        secs = re.findall(r'<section class="sec" id="([^"]+)">', panel)
        if links != secs:
            print(u'  %-5s แถบนำทางกับหัวข้อไม่ตรงกัน · นำทาง %d · หัวข้อ %d'
                  % (cid, len(links), len(secs)))
            for a in set(links) - set(secs):
                print(u'        นำทางชี้ไป %s ซึ่งไม่มีหัวข้อ' % a)
            for a in set(secs) - set(links):
                print(u'        หัวข้อ %s ไม่มีในแถบนำทาง' % a)
            bad += 1

        pre = re.compile(r'^%s-\d+$' % re.escape(cid))
        off = [s for s in secs if not pre.match(s)]
        if off:
            print(u'  %-5s รหัสหัวข้อไม่ขึ้นต้นด้วย %s- · %s' % (cid, cid, ' '.join(off)))
            bad += 1

        if (u'<nav id="rail-%s"' % cid) not in rail:
            print(u'  %-5s RAIL ไม่มี nav id ที่ตรงกับรหัสหน่วย' % cid)
            bad += 1
        if (u'<div id="%s" class="hidden" role="tabpanel" aria-labelledby="t-%s">'
                % (cid, cid)) not in panel:
            print(u'  %-5s PANEL เปิดแท็กไม่ตรงแบบที่หน้านี้ใช้' % cid)
            bad += 1

        h2 = len(re.findall(r'<h2>', panel))
        if h2 != len(secs):
            print(u'  %-5s มี %d หัวข้อ แต่มี h2 %d อัน' % (cid, len(secs), h2))
            bad += 1

        for tag in ('div', 'section', 'table', 'thead', 'tbody', 'tr', 'td', 'th',
                    'p', 'ol', 'ul', 'li', 'span', 'h2', 'h3', 'b', 'i', 'figure'):
            o = len(re.findall(r'<%s[ >]' % tag, panel))
            c = len(re.findall(r'</%s>' % tag, panel))
            if o != c:
                print(u'  %-5s แท็ก %s เปิด %d ปิด %d' % (cid, tag, o, c))
                bad += 1

        # ใช้คลาสที่หน้านี้ไม่มี จะไม่มีหน้าตาอะไรเลยและไม่มีใครเตือน
        used = set()
        for m in re.finditer(r'class="([^"]+)"', rail + panel):
            used.update(m.group(1).split())
        unknown = sorted(used - OK_CLASSES)
        if unknown:
            print(u'  %-5s ใช้คลาสที่หน้านี้ไม่มี · %s' % (cid, ' '.join(unknown)))
            bad += 1

        print(u'%-5s %-22s %2d หัวข้อ · %2d ตาราง · %6d อักษร'
              % (cid, u_['label'], len(secs),
                 len(re.findall(r'<table', panel)), len(panel)))
    return bad


def verify(html):
    bad = 0
    tabs = re.findall(r'<button class="tab" role="tab" id="t-([\w-]+)" aria-controls="([\w-]+)"', html)
    panels = re.findall(r'<div id="([\w-]+)"[^>]*role="tabpanel" aria-labelledby="t-([\w-]+)">', html)
    tab_ids = [a for _t, a in tabs]
    panel_ids = [a for a, _t in panels]
    if len(tabs) != len(panels):
        print(u'  แท็บ %d อัน แต่แผง %d อัน' % (len(tabs), len(panels)))
        bad += 1
    for t, a in tabs:
        if t != a:
            print(u'  แท็บ t-%s ชี้ไปแผง %s ซึ่งชื่อไม่ตรงกัน' % (t, a))
            bad += 1
        if a not in panel_ids:
            print(u'  แท็บ t-%s ชี้ไปแผง %s ที่ไม่มีในหน้า' % (t, a))
            bad += 1
    for a in panel_ids:
        if a not in tab_ids:
            print(u'  แผง %s ไม่มีแท็บไหนชี้มาถึง' % a)
            bad += 1

    m = re.search(r'var rails = \{(.*?)\};', html, re.S)
    if not m:
        print(u'  หาแผนที่ rails ไม่เจอ')
        return bad + 1
    mapped = dict(re.findall(r"([\w-]+):'([\w-]+)'", m.group(1)))
    for a in panel_ids:
        if a not in mapped:
            print(u'  แผง %s ไม่มีชื่อในแผนที่ rails · กดแท็บแล้วแถบซ้ายจะว่าง' % a)
            bad += 1
        elif (u'<nav id="%s"' % mapped[a]) not in html:
            print(u'  แผนที่ rails ชี้ไป %s ซึ่งไม่มีในหน้า' % mapped[a])
            bad += 1

    tagged = re.findall(r'<[a-zA-Z][^<>]*\sid="([\w-]+)"', html)
    ids = set(tagged)
    rail_part = html[html.index(u'<aside class="rail">'):html.index(u'</aside>')]
    for a in re.findall(r'href="#([\w-]+)"', rail_part):
        if a not in ids:
            print(u'  ลิงก์ในแถบนำทางชี้ไป %s ซึ่งไม่มีอะไรรองรับ' % a)
            bad += 1

    dup = sorted(i for i in ids if tagged.count(i) > 1)
    if dup:
        print(u'  รหัสซ้ำในหน้า · %s' % ' '.join(dup))
        bad += 1

    secs = len(re.findall(r'<section class="sec" id="[\w-]+">', html))
    print(u'\nแท็บ %d อัน · แผง %d อัน · หัวข้อรวม %d อัน' % (len(tabs), len(panels), secs))
    return bad


def main():
    ap = argparse.ArgumentParser(description=u'ฝังเนื้อหาฐานข้อมูลและ HANA ลงหน้าวิชา ERP')
    ap.add_argument('--check', action='store_true', help=u'ตรวจอย่างเดียว ไม่เขียนไฟล์')
    ap.add_argument('--strip', action='store_true', help=u'ถอนของที่ฝังไว้ออก')
    a = ap.parse_args()

    html = io.open(PAGE, encoding='utf-8').read()

    if a.strip:
        out = strip(html)
        io.open(PAGE, 'w', encoding='utf-8').write(out)
        print(u'ถอนเนื้อหาฐานข้อมูลและ HANA ออกแล้ว · %d → %d อักษร' % (len(html), len(out)))
        return 0

    if check_data():
        print(u'\nตรวจพบปัญหา จึงยังไม่ฝังให้')
        return 1

    out, moved = insert(html)
    if verify(out):
        print(u'\nผลลัพธ์ยังไม่ผ่านการตรวจ จึงไม่เขียนไฟล์')
        return 1
    if a.check:
        print(u'ตรวจผ่าน · ถ้าฝังจริงจะมี %d จุดที่เปลี่ยน' % moved)
        return 0
    if not moved:
        print(u'หน้าตรงกับข้อมูลอยู่แล้ว ไม่มีอะไรต้องเขียน')
        return 0
    io.open(PAGE, 'w', encoding='utf-8').write(out)
    print(u'\nฝังลง erp/index.html แล้ว · %d → %d อักษร · เปลี่ยน %d จุด'
          % (len(html), len(out), moved))
    return 0


if __name__ == '__main__':
    sys.exit(main())
