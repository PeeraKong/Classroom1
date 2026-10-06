#!/usr/bin/env python3
# -*- coding: utf-8 -*-
u"""เพิ่มเนื้อหาส่วนหลังมิดเทอมของวิชาการบัญชีขั้นสูง 1 ลงในหน้าเว็บ

    python3 tools/adv-postmid.py            แทรกจริง
    python3 tools/adv-postmid.py --check    ตรวจอย่างเดียว ไม่เขียนไฟล์

ที่มาของเนื้อหา  เอกสารประกอบการสอน Ch4_3_2568 ของอาจารย์ แบ่งเป็นสี่ชุดสไลด์
  หน้า  1-14  งบการเงินรวมและเงินลงทุนในบริษัทร่วม กรณีขาดทุน
  หน้า 15-48  การด้อยค่าของค่าความนิยม TAS 36
  หน้า 50-58  กิจการร่วมค้า TFRS 11
  หน้า 59-83  บุคคลหรือกิจการที่เกี่ยวข้องกัน TAS 24

ทั้งสี่เรื่องเป็นเนื้อหาหลังมิดเทอม จึงแยกออกจากสี่บทเดิมด้วยเส้นคั่นในแถบแท็บ

สคริปต์นี้รันซ้ำได้ไม่ซ้อน เพราะคร่อมของที่เพิ่มด้วยคอมเมนต์หัวท้าย
และตรวจให้หลังแทรกว่าหัวข้อครบ ลิงก์ในแถบข้างชี้ถูก แท็กสมดุล
และสคริปต์ของหน้ายังคอมไพล์ได้

หน้าตัวอย่างจริงในสไลด์เป็นภาพสแกนของงบการเงินที่เผยแพร่ต่อสาธารณะ
หน้านี้ไม่ได้ฝังภาพนั้น แต่พิมพ์ตัวเลขขึ้นใหม่เป็นตารางพร้อมระบุที่มา
จะได้ค้นหาได้ อ่านบนจอเล็กได้ และเข้ากับธีมมืดสว่างเหมือนส่วนอื่นของหน้า
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

# โหลดชิ้นส่วนเนื้อหาจากไฟล์ข้างเคียง เพื่อไม่ให้ไฟล์เดียวยาวเกินอ่าน
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def mark(key):
    return (u'<!-- postmid:%s:start -->' % key, u'<!-- postmid:%s:end -->' % key)


def jsmark(key):
    return (u'/* postmid:%s:start */' % key, u'/* postmid:%s:end */' % key)


# ───────────────────────── ส่วนที่ 1 · CSS ─────────────────────────
# สองสีใหม่สำหรับบทที่ 7 กับ 8 ของกลุ่มหลังมิดเทอม และเส้นคั่นในแถบแท็บ
CSS_LIGHT = u"""
--teal:#1d6a6a; --teal-soft:#d8ebe9;
--clay:#8a5a24; --clay-soft:#f4e8d6;"""

CSS_DARK = u"""
--teal:#63c3bd; --teal-soft:#132b2a;
--clay:#d9a765; --clay-soft:#2d2415;"""

CSS_RULES = u"""
.tab[aria-controls="ch5"], #rail-ch5{--accent:var(--green); --accent-soft:var(--green-soft)}
.tab[aria-controls="ch6"], #rail-ch6{--accent:var(--red); --accent-soft:var(--red-soft)}
.tab[aria-controls="ch7"], #rail-ch7{--accent:var(--teal); --accent-soft:var(--teal-soft)}
.tab[aria-controls="ch8"], #rail-ch8{--accent:var(--clay); --accent-soft:var(--clay-soft)}
/* เส้นคั่นกลางแถบแท็บ บอกว่าจากตรงนี้ไปเป็นเนื้อหาหลังมิดเทอม */
.tab-div{display:flex; align-items:center; gap:7px; padding:0 12px; white-space:nowrap;
  font-size:.7rem; font-weight:700; letter-spacing:.09em; text-transform:uppercase; color:var(--ink-3)}
.tab-div::before{content:""; width:1px; height:18px; background:var(--rule)}
@media (max-width:640px){.tab-div{padding:0 8px; font-size:.62rem}}
/* ตารางเทียบค่าความนิยมของบริษัทใหญ่กับส่วนได้เสียที่ไม่มีอำนาจควบคุม */
.gw-split{display:grid; grid-template-columns:1fr 1fr; gap:10px; margin:14px 0}
.gw-split>div{border:1px solid var(--rule); border-radius:10px; padding:12px 14px; background:var(--surface)}
.gw-split .gl{display:block; font-size:.72rem; font-weight:700; letter-spacing:.07em;
  text-transform:uppercase; color:var(--ink-3); margin-bottom:5px}
.gw-split .gv{font-variant-numeric:tabular-nums; font-weight:700; font-size:1.18rem; color:var(--accent)}
@media (max-width:560px){.gw-split{grid-template-columns:1fr}}"""


def patch_css(html):
    u"""เพิ่มตัวแปรสีสองคู่เข้าไปในทั้งสามบล็อกธีม แล้วต่อกฎของแท็บใหม่"""
    s, e = mark('css')
    if s in html:
        return html, 0

    # บล็อกธีม ตัวแปร --plum-soft เป็นตัวสุดท้ายของชุดสี จึงเกาะไว้ตรงนั้น
    hits = [m for m in re.finditer(r'--plum-soft:\s*#[0-9a-fA-F]{3,8};', html)]
    if len(hits) != 3:
        raise SystemExit(u'หาบล็อกธีมไม่ครบสามบล็อก เจอ %d' % len(hits))
    out, last = [], 0
    for i, m in enumerate(hits):
        add = CSS_LIGHT if i == 0 else CSS_DARK
        out.append(html[last:m.end()])
        out.append(add)
        last = m.end()
    out.append(html[last:])
    html = ''.join(out)

    anchor = u'.tab[aria-controls="ch4"], #rail-ch4{--accent:var(--plum); --accent-soft:var(--plum-soft)}'
    if html.count(anchor) != 1:
        raise SystemExit(u'หาแถวสีของแท็บบทที่ 4 ไม่เจอ')
    html = html.replace(anchor, anchor + u'\n' + s + CSS_RULES + u'\n' + e)
    return html, 1


# ───────────────────────── ส่วนที่ 2 · แถบแท็บ ─────────────────────────
TABS = u"""
    <span class="tab-div">หลังมิดเทอม</span>
    <button class="tab" role="tab" id="t-ch5" aria-controls="ch5" aria-selected="false"><span class="tnum">06</span>งบรวม · กรณีขาดทุน</button>
    <button class="tab" role="tab" id="t-ch6" aria-controls="ch6" aria-selected="false"><span class="tnum">07</span>การด้อยค่าของค่าความนิยม</button>
    <button class="tab" role="tab" id="t-ch7" aria-controls="ch7" aria-selected="false"><span class="tnum">08</span>กิจการร่วมค้า</button>
    <button class="tab" role="tab" id="t-ch8" aria-controls="ch8" aria-selected="false"><span class="tnum">09</span>บุคคลที่เกี่ยวข้องกัน</button>"""


def patch_tabs(html):
    s, e = mark('tabs')
    if s in html:
        return html, 0
    anchor = (u'    <button class="tab" role="tab" id="t-ex" aria-controls="ex" '
              u'aria-selected="false"><span class="tnum">E</span>แบบฝึกเขียนตอบ</button>')
    if html.count(anchor) != 1:
        raise SystemExit(u'หาแท็บแบบฝึกเขียนตอบไม่เจอ')
    block = u'    ' + s + TABS + u'\n    ' + e + u'\n' + anchor
    return html.replace(anchor, block), 1


def patch_railjs(html):
    s, e = jsmark('rails')
    if s in html:
        return html, 0
    old = (u"var rails = {ch1:'rail-ch1', ch2:'rail-ch2', ch3:'rail-ch3', ch4:'rail-ch4', "
           u"c4x:'rail-c4x', ex:'rail-ex', quiz:'rail-quiz'};")
    if html.count(old) != 1:
        raise SystemExit(u'หาตาราง rails ใน JS ไม่เจอ')
    new = (u"var rails = {ch1:'rail-ch1', ch2:'rail-ch2', ch3:'rail-ch3', ch4:'rail-ch4', "
           u"c4x:'rail-c4x', " + s +
           u" ch5:'rail-ch5', ch6:'rail-ch6', ch7:'rail-ch7', ch8:'rail-ch8', " + e +
           u" ex:'rail-ex', quiz:'rail-quiz'};")
    return html.replace(old, new), 1


def patch_rails(html, rails_html):
    s, e = mark('rails')
    if s in html:
        return html, 0
    anchor = u'    <nav id="rail-ex" class="hidden" aria-label="แบบฝึกเขียนตอบ">'
    if html.count(anchor) != 1:
        raise SystemExit(u'หาแถบข้างของแบบฝึกเขียนตอบไม่เจอ')
    return html.replace(anchor, u'    ' + s + u'\n' + rails_html + u'    ' + e + u'\n' + anchor), 1


def patch_panels(html, panels_html):
    s, e = mark('panels')
    if s in html:
        return html, 0
    anchor = u'  <div id="ex" class="hidden" role="tabpanel" aria-labelledby="t-ex">'
    if html.count(anchor) != 1:
        raise SystemExit(u'หาแผงแบบฝึกเขียนตอบไม่เจอ')
    return html.replace(anchor, u'  ' + s + u'\n' + panels_html + u'  ' + e + u'\n\n' + anchor), 1


def patch_quiz(html, quiz_js, total):
    s, e = jsmark('quiz')
    if s in html:
        return html, 0
    i = html.rindex(u'var QS = [')
    j = html.index(u'\n  ];', i)
    head = html[:j]
    # ข้อสุดท้ายของคลังเดิมไม่มีจุลภาคปิดท้าย ต้องเติมก่อน ไม่งั้นสคริปต์ทั้งหน้าพัง
    if not head.rstrip().endswith(','):
        head = head.rstrip() + u','
    html = head + u'\n    ' + s + u'\n' + quiz_js + u'    ' + e + html[j:]

    # ข้อความบอกจำนวนข้อสองแห่งต้องตามไปด้วย ไม่งั้นตัวเลขไม่ตรงของจริง
    for old, new in [(u'46 ข้อ ครอบคลุมทั้งสี่บทและตัวอย่างครบวงจร',
                      u'%d ข้อ ครอบคลุมทั้งแปดบทและตัวอย่างครบวงจร' % total),
                     (u'0 จาก 46 ข้อ', u'0 จาก %d ข้อ' % total)]:
        if html.count(old) != 1:
            raise SystemExit(u'หาข้อความจำนวนข้อสอบไม่เจอ · %s' % old)
        html = html.replace(old, new)
    # ตัวนับใน JS ก็ตรึงเลข 46 ไว้เหมือนกัน
    html = html.replace(u"' จาก 46 ข้อ'", u"' จาก %d ข้อ'" % total)
    return html, 1


MAST_OLD = (u'สื่อประกอบการเรียน 4 บท · บัญชีสำนักงานใหญ่และสาขา · การรวมธุรกิจตาม TFRS 3 · '
            u'งบการเงินรวม ณ วันซื้อหุ้น · งบการเงินรวมภายหลังวันซื้อหุ้น '
            u'พร้อมสมุดรายวันคู่ กระดาษทำการ เครื่องมือคำนวณ และแบบทดสอบ')
MAST_NEW = (u'สื่อประกอบการเรียน 8 บท · <b>ก่อนมิดเทอม</b> บัญชีสำนักงานใหญ่และสาขา · การรวมธุรกิจตาม TFRS 3 · '
            u'งบการเงินรวม ณ วันซื้อหุ้นและภายหลังวันซื้อหุ้น · <b>หลังมิดเทอม</b> งบรวมกรณีขาดทุน · '
            u'การด้อยค่าของค่าความนิยมตาม TAS 36 · กิจการร่วมค้าตาม TFRS 11 · '
            u'บุคคลหรือกิจการที่เกี่ยวข้องกันตาม TAS 24 '
            u'พร้อมสมุดรายวันคู่ กระดาษทำการ เครื่องมือคำนวณ และแบบทดสอบ')


def patch_mast(html):
    if MAST_NEW in html:
        return html, 0
    if html.count(MAST_OLD) != 1:
        raise SystemExit(u'หาคำโปรยบนหัวหน้าไม่เจอ')
    return html.replace(MAST_OLD, MAST_NEW), 1


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


def verify(html, chapters):
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
        print(u'  %-4s %-38s %2d หัวข้อ' % (ch, title, n))

    for tag in ['section', 'figure']:
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
    ap = argparse.ArgumentParser(description=u'แทรกเนื้อหาหลังมิดเทอมของการบัญชีขั้นสูง 1')
    ap.add_argument('--check', action='store_true', help=u'ตรวจอย่างเดียว ไม่เขียนไฟล์')
    a = ap.parse_args()

    import advpostmid_data as D

    html = io.open(PAGE, encoding='utf-8').read()
    before = len(html)
    steps = 0
    for fn in (patch_css, patch_tabs, patch_railjs, patch_mast):
        html, n = fn(html)
        steps += n
    html, n = patch_rails(html, D.RAILS); steps += n
    html, n = patch_panels(html, D.PANELS); steps += n
    html, n = patch_quiz(html, D.QUIZ, D.QUIZ_TOTAL); steps += n

    print(u'แทรก %d จาก 7 ชิ้น · %d → %d อักษร' % (steps, before, len(html)))
    bad = verify(html, D.CHAPTERS)
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
