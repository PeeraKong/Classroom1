#!/usr/bin/env python3
# -*- coding: utf-8 -*-
u"""ฝังเนื้อหาหลังมิดเทอมของวิชาการสอบบัญชีลงหน้าเว็บ

    python3 tools/audit-postmid.py            ตรวจแล้วฝัง
    python3 tools/audit-postmid.py --check    ตรวจอย่างเดียว ไม่เขียนไฟล์
    python3 tools/audit-postmid.py --strip    ถอนของที่ฝังไว้ออกให้หมด

หน้า audit/index.html เดิมเขียนมือทั้งหน้า ไม่มีเครื่องหมายคั่นให้ฝังซ้ำได้
ตัวนี้จึงเป็นตัวแรกที่วางเครื่องหมาย <!-- pm:...:start --> ลงหน้านั้น

ทำไมรวมทุกหน่วยไว้ในตัวสร้างตัวเดียว
  หน้านี้จะมีหน่วยหลังมิดเทอมหลายหน่วย ถ้าแยกเป็นตัวสร้างหน่วยละตัว
  แต่ละตัวต้องรู้ว่าตัวเองต่อท้ายใคร แล้วลำดับการรันจะกลายเป็นกับดัก
  คือรันสลับลำดับแล้วเนื้อหาของตัวที่รันก่อนถูกทับหาย
  (เคยเจอมาแล้วกับหน้า marketing จนต้องมีตัวประสานงานแยกอีกตัว)
  ตัวนี้ถือรายการหน่วยทั้งหมดไว้เอง เพิ่มหน่วยใหม่คือเพิ่มบรรทัดใน UNITS
  แล้วรันตัวเดิมซ้ำ ลำดับจึงถูกเสมอและรันกี่ครั้งก็ได้ผลเท่ากัน

เนื้อหาของแต่ละหน่วยอยู่ในไฟล์ข้อมูลแยก ซึ่งต้องมีตัวแปรสองตัว
    RAIL   แถบนำทางด้านซ้าย  <nav id="rail-<รหัส>" ...>
    PANEL  เนื้อหาของแท็บ    <div id="<รหัส>" ...role="tabpanel"...>
"""

import argparse
import importlib.util
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PAGE = os.path.join(ROOT, 'audit', 'index.html')

# หน่วยเนื้อหาหลังมิดเทอม เรียงตามลำดับที่อยากให้แท็บเรียงในหน้า
# เพิ่มหน่วยใหม่ที่นี่ได้เลย แล้วรันสคริปต์ซ้ำ
UNITS = [
    {'mod': 'audit_tc_data', 'id': 'tc', 'num': u'TC', 'label': u'วงจรการค้า',
     'aria': u'หัวข้อวงจรการค้า'},
    {'mod': 'audit_oc_data', 'id': 'oc', 'num': u'OC', 'label': u'วงจรอื่น',
     'aria': u'หัวข้อการตรวจสอบวงจรอื่น'},
]

DIV_LABEL = u'หลังมิดเทอม'

# ---- จุดวางของแต่ละก้อน ต้องมีอยู่จริงในหน้า ไม่งั้นหยุดทันที ----
A_CSS = u'.tab .tnum{font-family:"IBM Plex Mono",monospace; font-size:.75rem; opacity:.65; margin-right:7px}\n'
A_TAB = u'    <button class="tab" role="tab" id="t-quiz" aria-controls="quiz"'
A_RAIL = u'    <nav id="rail-quiz" class="hidden" aria-label="แบบทดสอบ">'
A_PANEL = u'  <div id="quiz" class="hidden" role="tabpanel" aria-labelledby="t-quiz">'
A_RAILJS = u"  var rails = {"

CSS = u"""
/* ---- เนื้อหาหลังมิดเทอม ---- */
/* เส้นคั่นกลางแถบแท็บ บอกว่าจากตรงนี้ไปเป็นเนื้อหาหลังมิดเทอม */
.tab-div{display:flex; align-items:center; gap:7px; padding:0 12px; white-space:nowrap;
  font-size:.7rem; font-weight:700; letter-spacing:.09em; text-transform:uppercase; color:var(--ink-3)}
.tab-div::before{content:""; width:1px; height:18px; background:var(--rule)}
@media (max-width:640px){.tab-div{padding:0 8px; font-size:.62rem}}

/* กล่องเตือน ใช้สีเดียวกับกล่องปกติแต่ขอบหนากว่า จึงดังกว่าโดยไม่เพิ่มสีใหม่
   หน้านี้เรียก class="note warn" อยู่ก่อนแล้วหลายจุด แต่ไม่เคยมีกฎรองรับ
   จึงตกไปใช้หน้าตาของ .note เฉย ๆ บรรทัดนี้ปิดช่องว่างนั้นด้วย */
.note.warn{border-left-width:5px; background:var(--accent-soft)}
.note.warn .nh{color:var(--accent)}

/* ช่องตารางสองแบบที่หน่วยหลังมิดเทอมใช้บ่อย
   td.k คือช่องหัวแถว ส่วน td.m คือช่องรหัสสั้น ๆ เช่นตัวย่อข้อกำหนด
   ผูกไว้กับ table.tbl เพื่อไม่ให้ไปชนกับ .sm-rule .k ที่มีอยู่เดิม */
table.tbl td.k{font-weight:600; color:var(--ink)}

/* ตัวย่อข้อกำหนดอย่าง E, C, R/O ที่แทรกกลางประโยคหรือวางไว้ทั้งช่อง
   ต้องมีกฎที่ไม่ผูกกับตาราง ไม่งั้นที่แทรกกลางประโยคจะไม่ได้หน้าตาอะไรเลย */
.m{font-family:"IBM Plex Mono",monospace; font-size:.85em;
  color:var(--accent); white-space:nowrap}
table.tbl td.m{font-size:.79rem}
"""

# ข้อความหัวหน้าเว็บ ปรับให้บอกว่ามีเนื้อหาหลังมิดเทอมแล้ว
EYEBROW_OLD = u'Auditing &amp; Assurance Services · Chapters 1, 3, 4'
EYEBROW_NEW = u'Auditing &amp; Assurance Services · Chapters 1, 3, 4 · วงจรรายการค้า'
SUB_TAIL = (u' · วงจรรายการค้าครบทั้งห้าวงจร ตั้งแต่วงจรรายได้และวงจรรายจ่าย'
            u' จนถึงวงจรการผลิต ค่าจ้างแรงงาน การจัดหาเงิน และการลงทุน')
META_TAIL = (u' และวงจรรายการค้าครบทั้งห้าวงจร ทั้งวงจรรายได้ วงจรรายจ่าย'
             u' วงจรการผลิต วงจรค่าจ้างแรงงาน วงจรการจัดหาเงิน และวงจรการลงทุน')

# คำบอกขอบเขตของแบบทดสอบ ส่วนจำนวนข้อ tools/make-quiz.py เป็นคนเขียนให้
QZ_OLD = u'ครอบคลุมทั้งสี่บท สองโมดูล และงานให้ความเชื่อมั่น'
QZ_NEW = u'ครอบคลุมทั้งสี่บท สองโมดูล งานให้ความเชื่อมั่น และวงจรรายการค้าหลังมิดเทอม'


def mark(key):
    return u'<!-- pm:%s:start -->' % key, u'<!-- pm:%s:end -->' % key


def jsmark(key):
    return u'/* pm:%s:start */' % key, u'/* pm:%s:end */' % key


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
    u"""ตำแหน่งหน้าจุดยึด ใช้เมื่อยังไม่เคยฝัง"""
    at = html.find(anchor)
    if at < 0:
        raise SystemExit(u'หาจุดวาง %s ในหน้าไม่เจอ · %s' % (key, anchor[:70]))
    return at


def after(html, key, anchor):
    u"""ตำแหน่งถัดจากจุดยึด ใช้เมื่อต้องวางต่อท้ายข้อความที่มีอยู่"""
    return before(html, key, anchor) + len(anchor)


def in_code(html, i):
    u"""จริงเมื่อตำแหน่ง i อยู่ข้างใน style หรือ script

    ใช้กันพลาดเรื่องชนิดของเครื่องหมายคั่น เคยพลาดมาแล้วตอนวางเครื่องหมาย
    แบบ HTML ลงกลางบล็อก style ซึ่งดูเผิน ๆ ไม่มีอะไร แต่ตัวอ่าน CSS
    มองเห็น -->.layout{...} เป็นกฎเดียวกันทั้งก้อน แล้วกลืนกฎที่อยู่ถัดไปหายไป
    หน้าเลยเสียเลย์เอาต์สองคอลัมน์ทิ้งโดยไม่มีข้อความเตือนอะไรเลย
    """
    for tag in ('style', 'script'):
        for m in re.finditer(r'<%s[^>]*>(.*?)</%s>' % (tag, tag), html, re.S):
            if m.start(1) <= i <= m.end(1):
                return True
    return False


def splice(html, key, body, at, js=False):
    u"""วางก้อน body ไว้ในเครื่องหมายของ key ถ้ามีอยู่แล้วให้แทนที่ของเดิม

    at คือตำแหน่งที่จะวางเมื่อยังไม่เคยฝัง ส่งเป็นฟังก์ชันมาเพื่อให้หาจุดยึด
    เฉพาะตอนที่จำเป็น เพราะพอฝังแล้วข้อความรอบ ๆ จุดยึดอาจขยับไปแล้ว

    คืนค่า (html, เปลี่ยนไปหรือไม่) เพื่อให้รู้ว่ารันรอบนี้มีอะไรขยับจริงไหม
    """
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
    out = [u'\n    <span class="tab-div">%s</span>' % DIV_LABEL]
    for u_ in UNITS:
        out.append(u'\n    <button class="tab" role="tab" id="t-%s" aria-controls="%s"'
                   u' aria-selected="false"><span class="tnum">%s</span>%s</button>'
                   % (u_['id'], u_['id'], u_['num'], u_['label']))
    return u''.join(out) + u'\n'


def patch_mast(html):
    u"""ปรับคำโฆษณาหัวหน้าเว็บและ meta ให้ครอบเนื้อหาใหม่

    ไม่ได้ใช้เครื่องหมายคั่น เพราะเป็นการแก้ข้อความในที่เดิม
    จึงเช็กก่อนว่าแก้ไปแล้วหรือยัง แล้วค่อยแก้ เพื่อให้รันซ้ำได้
    """
    n = 0
    if EYEBROW_NEW not in html:
        if EYEBROW_OLD not in html:
            raise SystemExit(u'หาข้อความ eyebrow เดิมไม่เจอ')
        html = html.replace(EYEBROW_OLD, EYEBROW_NEW)
        n += 1
    if SUB_TAIL not in html:
        m = re.search(r'(<p class="mast-sub">)(.*?)(</p>)', html, re.S)
        if not m:
            raise SystemExit(u'หา mast-sub ไม่เจอ')
        html = html[:m.end(2)] + SUB_TAIL + html[m.end(2):]
        n += 1
    if META_TAIL not in html:
        # คำบรรยายหน้าอยู่สองที่ คือ meta description และ og:description
        before = html
        html = re.sub(r'(content="สื่อประกอบการเรียนวิชาการสอบบัญชี[^"]*?)(")',
                      lambda m: m.group(1) + META_TAIL + m.group(2), html)
        if html != before:
            n += 1
    if QZ_NEW not in html:
        if QZ_OLD not in html:
            raise SystemExit(u'หาคำบอกขอบเขตของแบบทดสอบไม่เจอ')
        html = html.replace(QZ_OLD, QZ_NEW)
        n += 1
    return html, n


def insert(html):
    moved = 0
    html, ch = splice(html, 'css', CSS,
                      lambda h, k: after(h, k, A_CSS), js=True); moved += ch

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

    html, n = patch_mast(html); moved += n
    return html, moved


def strip(html):
    html = re.sub(r'<!-- pm:\w+:start -->.*?<!-- pm:\w+:end -->', u'', html, flags=re.S)
    html = re.sub(r'/\* pm:\w+:start \*/.*?/\* pm:\w+:end \*/', u'', html, flags=re.S)
    html = html.replace(EYEBROW_NEW, EYEBROW_OLD)
    html = html.replace(SUB_TAIL, u'')
    html = html.replace(META_TAIL, u'')
    html = html.replace(QZ_NEW, QZ_OLD)
    return html


# ---------------------------------------------------------------- ตรวจ

def check_data():
    u"""ตรวจไฟล์ข้อมูลของทุกหน่วยก่อนเอาไปฝัง"""
    bad = 0
    for u_ in UNITS:
        cid = u_['id']
        mod = load(u_['mod'])
        rail, panel = mod.RAIL, mod.PANEL

        # รหัสหัวข้อในแถบนำทางต้องตรงกับหัวข้อในเนื้อหา ทั้งชุดและลำดับ
        links = re.findall(r'href="#([^"]+)"', rail)
        secs = re.findall(r'<section class="sec" id="([^"]+)">', panel)
        if links != secs:
            print(u'  %-4s แถบนำทางกับหัวข้อไม่ตรงกัน · นำทาง %d · หัวข้อ %d'
                  % (cid, len(links), len(secs)))
            for a in set(links) - set(secs):
                print(u'       นำทางชี้ไป %s ซึ่งไม่มีหัวข้อ' % a)
            for a in set(secs) - set(links):
                print(u'       หัวข้อ %s ไม่มีในแถบนำทาง' % a)
            bad += 1

        pre = re.compile(r'^%s-\d+$' % re.escape(cid))
        off = [s for s in secs if not pre.match(s)]
        if off:
            print(u'  %-4s รหัสหัวข้อไม่ขึ้นต้นด้วย %s- · %s' % (cid, cid, ' '.join(off)))
            bad += 1

        if (u'<nav id="rail-%s"' % cid) not in rail:
            print(u'  %-4s RAIL ไม่มี nav id ที่ตรงกับรหัสหน่วย' % cid)
            bad += 1
        if (u'<div id="%s" class="hidden" role="tabpanel" aria-labelledby="t-%s">' % (cid, cid)) not in panel:
            print(u'  %-4s PANEL เปิดแท็กไม่ตรงแบบที่หน้านี้ใช้' % cid)
            bad += 1

        # จำนวนหัวข้อต้องเท่ากับจำนวน h2 ไม่งั้นมีหัวข้อที่ลืมใส่ชื่อ
        h2 = len(re.findall(r'<h2>', panel))
        if h2 != len(secs):
            print(u'  %-4s มี %d หัวข้อ แต่มี h2 %d อัน' % (cid, len(secs), h2))
            bad += 1

        # แท็กต้องปิดครบ นับเฉพาะแท็กที่ต้องมีคู่
        for tag in ('div', 'section', 'table', 'thead', 'tbody', 'tr', 'td', 'th',
                    'p', 'ol', 'ul', 'li', 'span', 'h2', 'h3', 'b', 'i'):
            o = len(re.findall(r'<%s[ >]' % tag, panel))
            c = len(re.findall(r'</%s>' % tag, panel))
            if o != c:
                print(u'  %-4s แท็ก %s เปิด %d ปิด %d' % (cid, tag, o, c))
                bad += 1

        # ตัวแทนรูปที่ลืมแทนค่า จะโผล่เป็นข้อความ FIG ค้างอยู่
        for m in re.finditer(r'"(FIG\w*)"', panel):
            print(u'  %-4s มีตัวแทนรูป %s ที่ยังไม่ได้แทนค่า' % (cid, m.group(1)))
            bad += 1

        print(u'%-4s %-24s %2d หัวข้อ · %2d ตาราง · %6d อักษร'
              % (cid, u_['label'], len(secs),
                 len(re.findall(r'<table', panel)), len(panel)))
    return bad


def verify(html):
    u"""ตรวจหน้าที่ฝังเสร็จแล้ว ว่าแท็บ แผง และแถบนำทางยังตรงกันครบ"""
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

    # รหัสทั้งหน้า อ่านจากแท็กเปิดเท่านั้น
    # ถ้าไล่หา id="..." ทั้งไฟล์จะไปเจอที่เขียนไว้ในคำอธิบายของสคริปต์ด้วย
    # แล้วรายงานว่ารหัสซ้ำทั้งที่ไม่ได้ซ้ำ
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
    ap = argparse.ArgumentParser(description=u'ฝังเนื้อหาหลังมิดเทอมของวิชาการสอบบัญชี')
    ap.add_argument('--check', action='store_true', help=u'ตรวจอย่างเดียว ไม่เขียนไฟล์')
    ap.add_argument('--strip', action='store_true', help=u'ถอนของที่ฝังไว้ออก')
    a = ap.parse_args()

    html = io.open(PAGE, encoding='utf-8').read()

    if a.strip:
        out = strip(html)
        io.open(PAGE, 'w', encoding='utf-8').write(out)
        print(u'ถอนเนื้อหาหลังมิดเทอมออกแล้ว · %d → %d อักษร' % (len(html), len(out)))
        return 0

    bad = check_data()
    if bad:
        print(u'\nตรวจพบปัญหา %d จุด จึงยังไม่ฝังให้' % bad)
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
    print(u'\nฝังลง audit/index.html แล้ว · %d → %d อักษร · เปลี่ยน %d จุด'
          % (len(html), len(out), moved))
    return 0


if __name__ == '__main__':
    sys.exit(main())
