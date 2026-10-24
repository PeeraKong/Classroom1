#!/usr/bin/env python3
# -*- coding: utf-8 -*-
u"""เพิ่มบทที่ 9 10 และ 11 ของวิชาหลักการตลาดลงในหน้าเว็บ

    python3 tools/mk-ch911.py            แทรกจริง
    python3 tools/mk-ch911.py --check    ตรวจอย่างเดียว ไม่เขียนไฟล์

ที่มาของเนื้อหา
  บทที่ 9   Chp 09 PRIN MKGT Price cut2 2569
  บทที่ 10  Chp 10 PRIN MKGT Place Mkt channel SCP 2569
  บทที่ 11  Chp 11 PRIN MKGT Retail_Wholesale 2569

สามบทนี้เป็นเนื้อหาหลังมิดเทอมต่อจากบทที่ 8 จึงวางต่อหลังเส้นคั่นในแถบแท็บ
และเติมข้อสอบเข้าทั้งคลังรวมและคลังหลังมิดเทอม

ต้องรัน tools/mk-postmid.py ให้เสร็จก่อน เพราะสคริปต์นี้ยึดจุดแทรกกับ
คอมเมนต์คร่อมที่สคริปต์นั้นวางไว้ ทั้งแถบแท็บ แถบข้าง แผง สคริปต์แผงเลือก
และคลังข้อสอบทั้งสองชุด

สคริปต์นี้รันซ้ำได้ไม่ซ้อน เพราะคร่อมของที่เพิ่มด้วยคอมเมนต์หัวท้าย
และตรวจให้หลังแทรกว่าหัวข้อครบ ลิงก์ในแถบข้างชี้ถูก แท็กสมดุล
คลังข้อสอบไม่มีช่องว่างในอาร์เรย์ และสคริปต์ของหน้ายังคอมไพล์ได้

ภาพในหน้านี้เป็นแผนภาพของตำรา (Figure 10.1 10.2 10.5 11.1 12.1 12.2 12.3
12.4 และ 13.1) ซึ่งเป็นแผนภาพเชิงแนวคิด ไม่ใช่งานโฆษณาของบุคคลที่สาม
ส่วนตารางจุดคุ้มทุน ตารางกลยุทธ์ปรับราคา และตาราง 13.2 พิมพ์ขึ้นใหม่
เป็นตารางเว็บพร้อมคำแปล ไม่ได้ฝังภาพสแกน
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
    return (u'<!-- ch911:%s:start -->' % key, u'<!-- ch911:%s:end -->' % key)


def jsmark(key):
    return (u'/* ch911:%s:start */' % key, u'/* ch911:%s:end */' % key)


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
        raise SystemExit(u'หาจุดยึดของ %s ไม่เจอ หรือเจอมากกว่าหนึ่งที่ (%d)'
                         % (key, html.count(anchor)))
    return (html.replace(anchor, body + anchor) if before
            else html.replace(anchor, anchor + body)), 1


CHAPTERS = (
    ('m9', u'9', u'การตั้งราคา', u'ราคา'),
    ('m10', u'10', u'ช่องทางการตลาด', u'ช่องทาง'),
    ('m11', u'11', u'การค้าปลีกและการค้าส่ง', u'ค้าปลีก ค้าส่ง'),
)


# ───────────────────────── ส่วนที่ 1 · แถบแท็บ ─────────────────────────

TABS = u"""
    <button class="tab" role="tab" id="t-m9" aria-controls="m9" aria-selected="false"><span class="tnum">09</span>การตั้งราคา</button>
    <button class="tab" role="tab" id="t-m10" aria-controls="m10" aria-selected="false"><span class="tnum">10</span>ช่องทางการตลาด</button>
    <button class="tab" role="tab" id="t-m11" aria-controls="m11" aria-selected="false"><span class="tnum">11</span>ค้าปลีกและค้าส่ง</button>
  """


def patch_tabs(html):
    return splice(html, 'tabs', TABS, u'<!-- postmid:tab-m8:end -->', before=False)


def patch_railjs(html):
    u"""ลงทะเบียนแถบข้างของสามแผงใหม่ในตาราง rails ของสคริปต์หน้า"""
    want = u"m9:'rail-m9', m10:'rail-m10', m11:'rail-m11', "
    return splice(html, 'rails', want, u'/* postmid:rails:end */',
                  comment=False, before=False)


def patch_rails(html):
    import mk9_data, mk10_data, mk11_data
    block = u'\n' + mk9_data.RAIL + mk10_data.RAIL + mk11_data.RAIL + u'    '
    return splice(html, 'rails', block, u'<!-- postmid:rails:end -->',
                  before=False)


def patch_panels(html):
    import mk9_data, mk10_data, mk11_data
    block = (u'\n' + mk9_data.PANEL + u'\n' + mk10_data.PANEL + u'\n'
             + mk11_data.PANEL + u'\n')
    return splice(html, 'panel', block, u'<!-- postmid:panel:end -->',
                  before=False)


def patch_stepjs(html):
    import mk9_data, mk10_data, mk11_data
    block = mk9_data.STEPJS + mk10_data.STEPJS + mk11_data.STEPJS
    return splice(html, 'stepjs', block, u'/* postmid:stepjs:end */',
                  comment=False, before=False)


# ───────────────────────── ส่วนที่ 2 · แบบทดสอบ ─────────────────────────

def append_bank(html, name, key, items):
    u"""เติมข้อสอบท้ายคลังที่ชื่อ name โดยคร่อมคอมเมนต์ให้รันซ้ำได้

    ข้อสุดท้ายของคลังเดิมไม่มีจุลภาคปิดท้าย จึงต้องเติมให้ก่อน แต่ต้องเติม
    ไว้ข้างในคอมเมนต์คร่อมของเรา ไม่ใช่ไปแก้ของเดิม เพราะ --strip ลบได้เฉพาะ
    สิ่งที่อยู่ในคอมเมนต์คร่อม ถ้าจุลภาคกับช่องว่างไปอยู่ข้างนอกจะค้างสะสมทุกรอบ
    จนหน้าเพี้ยนไปเรื่อย ๆ · ท้ายคลังมีคอมเมนต์ปิดของการแทรกรอบก่อนคั่นอยู่
    จึงต้องมองข้ามคอมเมนต์ด้วย trim_tail ก่อนดูว่ามีจุลภาคอยู่แล้วหรือไม่
    ไม่งั้นจะเติมซ้ำจนเกิดช่องว่างในอาร์เรย์ ซึ่ง forEach ข้ามให้เงียบ ๆ
    แต่ทำให้ bank.length เกินจริงและเลขข้อในหน้าเว็บกระโดด
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


LEDE1 = (u'TOT ข้อ ครอบคลุม<b>ทั้งสิบบท</b> ทั้งก่อนและหลังมิดเทอม '
         u'เน้นจุดที่นิยามใกล้เคียงกันจนสับสน · '
         u'<b>ลำดับตัวเลือกสลับใหม่ทุกครั้งที่เริ่มทำ</b> จึงจำตำแหน่งเฉลยไม่ได้ · '
         u'อยากซ้อมเฉพาะเนื้อหาหลังมิดเทอมให้ไปที่แท็บ <b>Q2</b>')

LEDE2 = (u'TOT ข้อ เฉพาะ<b>บทที่ 8 ถึง 11 ซึ่งเป็นเนื้อหาหลังมิดเทอม</b> · '
         u'ชุดนี้<b>ไม่ถามให้ท่องรายการ</b> แต่ให้สถานการณ์มาแล้วถามว่าอยู่ขั้นไหนของ'
         u'กระบวนการ เป็นกลยุทธ์ตัวใด หรือทำไมคำตอบที่ฟังดูถูกถึงผิด · '
         u'<b>ลำดับตัวเลือกสลับใหม่ทุกครั้งที่เริ่มทำ</b>')


def set_lede(html, top_id, want):
    pat = (r'(<div id="%s"></div>\s*<p class="lede">)(.*?)(</p>)' % top_id)
    m = re.search(pat, html, re.S)
    if not m:
        raise SystemExit(u'หาคำโปรยของ %s ไม่เจอ' % top_id)
    if m.group(2) == want:
        return html
    return html[:m.start(2)] + want + html[m.end(2):]


def patch_quiz(html, total, q2_total):
    import mkquiz911_data as Q
    before = html
    html, _ = append_bank(html, 'QS', 'quiz', Q.QUIZ)
    html, _ = append_bank(html, 'QS2', 'quiz2', Q.QUIZ2)

    html = set_lede(html, 'quiz-top', LEDE1.replace(u'TOT', u'%d' % total))
    html = set_lede(html, 'quiz2-top', LEDE2.replace(u'TOT', u'%d' % q2_total))
    html = re.sub(u'id="sc-of">0 จาก \\d+ ข้อ', u'id="sc-of">0 จาก %d ข้อ' % total, html)
    html = re.sub(u'id="sc2-of">0 จาก \\d+ ข้อ', u'id="sc2-of">0 จาก %d ข้อ' % q2_total, html)
    html = re.sub(u'<i>Q</i>\\d+ ข้อ', u'<i>Q</i>%d ข้อ' % total, html)
    html = re.sub(u'<i>Q2</i>\\d+ ข้อ', u'<i>Q2</i>%d ข้อ' % q2_total, html)
    return html, (0 if html == before else 1)


# ───────────────────── ส่วนที่ 3 · หัวเรื่องและท้ายหน้า ─────────────────────

EYEBROW = u'Principles of Marketing · Ch 1, 3–11'

MAST_NEW = (u'<b>ก่อนมิดเทอม</b> กระบวนการการตลาด 5 ขั้น · สภาพแวดล้อมทางการตลาดและ PESTLE · '
            u'ระบบสารสนเทศและการวิจัยตลาด · พฤติกรรมผู้บริโภค · กลยุทธ์ STP · ผลิตภัณฑ์และตราสินค้า · '
            u'<b>หลังมิดเทอม</b> การพัฒนาสินค้าใหม่และวงจรชีวิตผลิตภัณฑ์ · การตั้งราคา · '
            u'ช่องทางการตลาด · การค้าปลีกและการค้าส่ง')

FOOT_NEW = (u'<b>หลักการตลาด</b> — สรุปจากเอกสารประกอบการสอน 10 ชุด อ้างอิงตำรา Kotler &amp; Armstrong, '
            u'<i>Principles of Marketing</i> (Pearson Education) · '
            u'<b>บทที่ 1, 3, 4, 5, 6 และ 7 เป็นเนื้อหาสอบกลางภาค</b> · '
            u'<b>บทที่ 8, 9, 10 และ 11 เป็นเนื้อหาหลังมิดเทอม</b> ว่าด้วยการพัฒนาสินค้าใหม่และวงจรชีวิตผลิตภัณฑ์ '
            u'การตั้งราคา ช่องทางการตลาด และการค้าปลีกกับการค้าส่ง '
            u'แยกไว้หลังเส้นคั่นในแถบแท็บ และมีแบบทดสอบของตัวเองที่แท็บ <b>Q2</b> · '
            u'หัวข้อ <b>ชีทอาจารย์</b> ท้ายบทที่ 1, 3, 4, 5, 6 และ 7 สรุปจากชีทประกอบการสอนของ อ.กฤตินี (อ.เกด) · '
            u'บทที่ 7 ใส่เฉพาะส่วนผลิตภัณฑ์ · '
            u'เลขภาพและเลขตารางในบทที่ 9 ถึง 11 เป็นเลขของตำราคนละรุ่นกับเลขบท จึงไม่ตรงกัน')


def patch_mast(html):
    u"""เขียนทับคำโปรยใต้ชื่อวิชา บรรทัดหัว และย่อหน้าแรกของท้ายหน้าทั้งก้อน"""
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


def bank_len(html, name):
    u"""ให้ node ประเมินคลังข้อสอบจริง แล้วคืนความยาวกับจำนวนช่องว่าง

    เคยใช้ regex ดักจุลภาคซ้ำ แต่ /\\*.*?\\*/ แบบ DOTALL ขยายข้าม */ ตัวแรกได้
    เวลาถอยกลับ จึงจับข้ามคอมเมนต์หลายก้อนแล้วรายงานผิดว่ามีช่องว่าง
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
                        u'console.log(%s.length + " " + holes);\n'
                        % (name, name, name))
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


def verify(html, total, q2_total):
    import mk9_data, mk10_data, mk11_data
    bad = 0
    rails = {'m9': mk9_data.RAIL, 'm10': mk10_data.RAIL, 'm11': mk11_data.RAIL}
    panels = {'m9': mk9_data.PANEL, 'm10': mk10_data.PANEL, 'm11': mk11_data.PANEL}
    for cid, num, title, _short in CHAPTERS:
        want = re.findall(r'<section class="sec" id="(%s-\d+)">' % cid, panels[cid])
        panel = re.search(r'<div id="%s" class="hidden" role="tabpanel".*?\n  </div>'
                          % cid, html, re.S)
        if not panel:
            print(u'  %-4s หาแผงในหน้าไม่เจอ' % cid); bad += 1; continue
        got = re.findall(r'<section class="sec" id="(%s-\d+)">' % cid, panel.group(0))
        if got != want:
            print(u'  %-4s หัวข้อไม่ตรง · มี %d ควรมี %d' % (cid, len(got), len(want)))
            bad += 1
        for sid in want:
            if ('href="#%s"' % sid) not in html:
                print(u'  %-4s แถบข้างไม่มีลิงก์ไป %s' % (cid, sid)); bad += 1
        for need in ('id="rail-%s"' % cid, 'id="t-%s"' % cid,
                     "%s:'rail-%s'" % (cid, cid)):
            if need not in html:
                print(u'  %-4s ขาด %s' % (cid, need)); bad += 1
        nav = re.search(r'<nav id="rail-%s".*?</nav>' % cid, html, re.S)
        if nav and len(re.findall(r'<li>', nav.group(0))) != len(want):
            print(u'  %-4s จำนวนลิงก์ในแถบข้างไม่เท่าจำนวนหัวข้อ' % cid); bad += 1
        figs = len(re.findall(r'<figure class="fig">', panel.group(0)))
        print(u'  %-4s บทที่ %-3s %-28s %2d หัวข้อ · %d ภาพ'
              % (cid, num, title, len(got), figs))
        if len(re.findall(r'<img ', panel.group(0))) != figs:
            print(u'  %-4s จำนวนภาพไม่เท่าจำนวนกรอบภาพ' % cid); bad += 1
        if 'src="data:image/png;base64,' not in panel.group(0) and figs:
            print(u'  %-4s ภาพไม่ได้ฝังเป็น base64' % cid); bad += 1

    # ปุ่มเลือกของแผงต้องมีกล่องผลลัพธ์ที่สคริปต์เรียกหาครบ
    for attr, out in (('data-pr', 'pr-out'), ('data-vms', 'vms-out'),
                      ('data-cd', 'cd-out'), ('data-rm', 'rm-out')):
        if ('id="%s"' % out) not in html:
            print(u'  ไม่มีกล่องผลลัพธ์ %s' % out); bad += 1
        if ('.step[%s]' % attr) not in html:
            print(u'  สคริปต์ไม่ได้อ่านปุ่ม %s' % attr); bad += 1

    for name, want in (('QS', total), ('QS2', q2_total)):
        m = re.search(r'var %s = \[(.*?)\n  \];' % name, html, re.S)
        if not m:
            print(u'  หาคลัง %s ไม่เจอ' % name); bad += 1; continue
        n = m.group(1).count(u'{ch:')
        if n != want:
            print(u'  คลัง %s มี %d ข้อ แต่หน้าบอกว่า %d ข้อ' % (name, n, want)); bad += 1
        # จุลภาคซ้ำทำให้เกิดช่องว่างในอาร์เรย์ ซึ่ง forEach ข้ามให้เงียบ ๆ
        # หน้าเว็บจึงแสดงจำนวนข้อเกินจริงโดยไม่มีอะไรพัง ต้องถาม length ของจริง
        ln, holes = bank_len(html, name)
        if ln is None:
            print(u'  คลัง %-3s %d ข้อ · ไม่มี node จึงไม่ได้ตรวจความยาวจริง' % (name, n))
            continue
        if ln < 0:
            bad += 1
            continue
        if holes:
            print(u'  คลัง %s มีช่องว่างในอาร์เรย์ %d ช่อง' % (name, holes)); bad += 1
        if ln != want:
            print(u'  คลัง %s รันแล้วได้ %d ข้อ แต่หน้าบอกว่า %d ข้อ'
                  % (name, ln, want)); bad += 1
        if not holes and ln == want and n == want:
            print(u'  คลัง %-3s %d ข้อ · รันแล้วได้ %d ข้อ ไม่มีช่องว่าง' % (name, n, ln))

    for tag in ['section', 'figure', 'table', 'nav', 'button']:
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


def strip(html):
    u"""ลบทุกบล็อกที่สคริปต์นี้วางไว้ออก ให้หน้ากลับไปมีแค่ถึงบทที่ 8

    มีไว้ให้ build-marketing.py เรียกก่อนรัน mk-postmid.py ใหม่ เพราะสคริปต์นั้น
    เขียนทับคลังข้อสอบทั้งก้อน ถ้าของบทที่ 9 ถึง 11 ยังคาอยู่จะได้อาร์เรย์ที่
    ขาดจุลภาคคั่นแล้วสคริปต์ทั้งหน้าพัง · ลบด้วยคอมเมนต์คร่อมของตัวเองจึงแม่น
    ไม่ไปแตะของที่สคริปต์อื่นวางไว้
    """
    n = 0
    for pat in (r'<!-- ch911:[\w-]+:start -->.*?<!-- ch911:[\w-]+:end -->',
                r'/\* ch911:[\w-]+:start \*/.*?/\* ch911:[\w-]+:end \*/'):
        html, k = re.subn(pat, u'', html, flags=re.S)
        n += k
    return html, n


def main():
    ap = argparse.ArgumentParser(description=u'แทรกบทที่ 9 10 11 ของหลักการตลาด')
    ap.add_argument('--check', action='store_true', help=u'ตรวจอย่างเดียว ไม่เขียนไฟล์')
    ap.add_argument('--strip', action='store_true',
                    help=u'ลบบทที่ 9 ถึง 11 ออก ให้หน้ากลับไปมีแค่ถึงบทที่ 8')
    a = ap.parse_args()

    if a.strip:
        html = io.open(PAGE, encoding='utf-8').read()
        html, n = strip(html)
        if not n:
            print(u'ไม่มีบทที่ 9 ถึง 11 ในหน้าอยู่แล้ว ไม่ต้องลบ')
            return 0
        if a.check:
            print(u'จะลบ %d บล็อก · ยังไม่เขียนไฟล์เพราะสั่ง --check' % n)
            return 0
        io.open(PAGE, 'w', encoding='utf-8').write(html)
        print(u'ลบ %d บล็อกของบทที่ 9 ถึง 11 ออกจาก %s แล้ว'
              % (n, os.path.relpath(PAGE, ROOT)))
        return 0

    import mkpostmid_data as D8
    import mkquiz2_data as Q2
    import mkquiz911_data as Q

    total = D8.QUIZ_TOTAL + Q.QUIZ.count(u'{ch:')
    q2_total = Q2.TOTAL + Q.QUIZ2.count(u'{ch:')

    html = io.open(PAGE, encoding='utf-8').read()
    if u'<!-- postmid:tab-m8:end -->' not in html:
        raise SystemExit(u'หน้านี้ยังไม่มีบทที่ 8 · ต้องรัน tools/mk-postmid.py ก่อน')

    before = len(html)
    steps = 0
    for fn in (patch_tabs, patch_railjs, patch_rails, patch_panels,
               patch_stepjs, patch_mast):
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
