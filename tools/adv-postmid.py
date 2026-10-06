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
        raise SystemExit(u'หาจุดยึดของ %s ไม่เจอ หรือเจอมากกว่าหนึ่งที่' % key)
    return (html.replace(anchor, body + anchor) if before
            else html.replace(anchor, anchor + body)), 1


# ───────────────────────── ส่วนที่ 1 · CSS ─────────────────────────
# สองสีใหม่สำหรับบทที่ 7 กับ 8 ของกลุ่มหลังมิดเทอม และเส้นคั่นในแถบแท็บ
CSS_LIGHT = u"""
--teal:#1d6a6a; --teal-soft:#d8ebe9;
--clay:#8a5a24; --clay-soft:#f4e8d6;
--indigo:#3d4a8c; --indigo-soft:#e2e4f3;"""

CSS_DARK = u"""
--teal:#63c3bd; --teal-soft:#132b2a;
--clay:#d9a765; --clay-soft:#2d2415;
--indigo:#9aa6e0; --indigo-soft:#1d2038;"""

CSS_RULES = u"""
.tab[aria-controls="ch5"], #rail-ch5{--accent:var(--green); --accent-soft:var(--green-soft)}
.tab[aria-controls="ch6"], #rail-ch6{--accent:var(--red); --accent-soft:var(--red-soft)}
.tab[aria-controls="ch7"], #rail-ch7{--accent:var(--teal); --accent-soft:var(--teal-soft)}
.tab[aria-controls="ch8"], #rail-ch8{--accent:var(--clay); --accent-soft:var(--clay-soft)}
.tab[aria-controls="ch9"], #rail-ch9{--accent:var(--indigo); --accent-soft:var(--indigo-soft)}
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
    u"""เพิ่มตัวแปรสีเข้าไปในทั้งสามบล็อกธีม แล้วต่อกฎของแท็บใหม่

    วิธีคือรื้อของเก่าออกให้หมดก่อนแล้วค่อยวางใหม่ จะได้แก้ชุดสีแล้วรันซ้ำได้
    ไม่ใช่ข้ามไปเฉย ๆ ซึ่งเคยทำให้เพิ่มสีใหม่แล้วตัวแปรไม่เข้าไปในหน้า
    และกันไม่ให้ซ้อนกันเองเวลารันหลายรอบ
    """
    before = html

    # ขั้นที่ 1 · รื้อบล็อกตัวแปรสีที่เคยวางไว้ออกให้หมด
    html = re.sub(r'/\* postmid:vars\d+:start \*/.*?/\* postmid:vars\d+:end \*/', '', html, flags=re.S)
    # ขั้นที่ 2 · รุ่นแรกสุดวางตัวแปรไว้โดยไม่มีคอมเมนต์คร่อม ต้องเก็บกวาดด้วย
    for legacy in (u'\n--teal:#1d6a6a; --teal-soft:#d8ebe9;\n--clay:#8a5a24; --clay-soft:#f4e8d6;',
                   u'\n--teal:#63c3bd; --teal-soft:#132b2a;\n--clay:#d9a765; --clay-soft:#2d2415;'):
        html = html.replace(legacy, u'')

    # ขั้นที่ 3 · วางใหม่ · --plum-soft เป็นตัวสุดท้ายของชุดสีเดิมในแต่ละบล็อกธีม
    hits = [m for m in re.finditer(r'--plum-soft:\s*#[0-9a-fA-F]{3,8};', html)]
    if len(hits) != 3:
        raise SystemExit(u'หาบล็อกธีมไม่ครบสามบล็อก เจอ %d' % len(hits))
    out, last = [], 0
    for i, m in enumerate(hits):
        out.append(html[last:m.end()])
        out.append(u'/* postmid:vars%d:start */' % (i + 1) +
                   (CSS_LIGHT if i == 0 else CSS_DARK) +
                   u'/* postmid:vars%d:end */' % (i + 1))
        last = m.end()
    out.append(html[last:])
    html = ''.join(out)

    anchor = (u'.tab[aria-controls="ch4"], #rail-ch4'
              u'{--accent:var(--plum); --accent-soft:var(--plum-soft)}')
    html, _ = splice(html, 'css', CSS_RULES + u'\n', anchor, before=False)
    return html, (0 if html == before else 1)


# ───────────────────────── ส่วนที่ 2 · แถบแท็บ ─────────────────────────
TABS = u"""
    <span class="tab-div">หลังมิดเทอม</span>
    <button class="tab" role="tab" id="t-ch5" aria-controls="ch5" aria-selected="false"><span class="tnum">06</span>งบรวม · กรณีขาดทุน</button>
    <button class="tab" role="tab" id="t-ch9" aria-controls="ch9" aria-selected="false"><span class="tnum">07</span>รายการระหว่างบริษัทในเครือ</button>
    <button class="tab" role="tab" id="t-ch6" aria-controls="ch6" aria-selected="false"><span class="tnum">08</span>การด้อยค่าของค่าความนิยม</button>
    <button class="tab" role="tab" id="t-ch7" aria-controls="ch7" aria-selected="false"><span class="tnum">09</span>กิจการร่วมค้า</button>
    <button class="tab" role="tab" id="t-ch8" aria-controls="ch8" aria-selected="false"><span class="tnum">10</span>บุคคลที่เกี่ยวข้องกัน</button>"""


def patch_tabs(html):
    return splice(html, 'tabs', u'\n    ' + TABS + u'\n    ',
                  u'    <button class="tab" role="tab" id="t-ex" aria-controls="ex" '
                  u'aria-selected="false"><span class="tnum">E</span>แบบฝึกเขียนตอบ</button>')


def patch_railjs(html):
    s, e = jsmark('rails')
    want = (s + u" ch5:'rail-ch5', ch9:'rail-ch9', ch6:'rail-ch6', "
            u"ch7:'rail-ch7', ch8:'rail-ch8', " + e)
    old = re.search(re.escape(s) + r'.*?' + re.escape(e), html, re.S)
    if old:
        return (html, 0) if old.group(0) == want else (html[:old.start()] + want + html[old.end():], 1)
    anchor = u"c4x:'rail-c4x', "
    if html.count(anchor) != 1:
        raise SystemExit(u'หาตาราง rails ใน JS ไม่เจอ')
    return html.replace(anchor, anchor + want + u' '), 1


def patch_rails(html, rails_html):
    return splice(html, 'rails', u'\n' + rails_html + u'    ',
                  u'    <nav id="rail-ex" class="hidden" aria-label="แบบฝึกเขียนตอบ">')


def patch_panels(html, panels_html):
    return splice(html, 'panels', u'\n' + panels_html + u'  ',
                  u'  <div id="ex" class="hidden" role="tabpanel" aria-labelledby="t-ex">')


def patch_quiz(html, quiz_js, total):
    before = html
    s, e = jsmark('quiz')
    body = s + u'\n' + quiz_js + u'    ' + e
    old = re.search(re.escape(s) + r'.*?' + re.escape(e), html, re.S)
    if old:
        html = html if old.group(0) == body else html[:old.start()] + body + html[old.end():]
    else:
        i = html.rindex(u'var QS = [')
        j = html.index(u'\n  ];', i)
        head = html[:j]
        # ข้อสุดท้ายของคลังเดิมไม่มีจุลภาคปิดท้าย ต้องเติมก่อน ไม่งั้นสคริปต์ทั้งหน้าพัง
        if not head.rstrip().endswith(','):
            head = head.rstrip() + u','
        html = head + u'\n    ' + body + html[j:]

    # ข้อความบอกจำนวนข้อต้องตามไปด้วย ไม่งั้นตัวเลขไม่ตรงของจริง
    html = re.sub(u'\\d+ ข้อ ครอบคลุมทั้ง\\S+บทและตัวอย่างครบวงจร',
                  u'%d ข้อ ครอบคลุมทั้งเก้าบทและตัวอย่างครบวงจร' % total, html)
    html = re.sub(u'0 จาก \\d+ ข้อ', u'0 จาก %d ข้อ' % total, html)
    html = re.sub(u"' จาก \\d+ ข้อ'", u"' จาก %d ข้อ'" % total, html)
    return html, (0 if html == before else 1)


MAST_OLD = (u'สื่อประกอบการเรียน 4 บท · บัญชีสำนักงานใหญ่และสาขา · การรวมธุรกิจตาม TFRS 3 · '
            u'งบการเงินรวม ณ วันซื้อหุ้น · งบการเงินรวมภายหลังวันซื้อหุ้น '
            u'พร้อมสมุดรายวันคู่ กระดาษทำการ เครื่องมือคำนวณ และแบบทดสอบ')
MAST_NEW = (u'สื่อประกอบการเรียน 9 บท · <b>ก่อนมิดเทอม</b> บัญชีสำนักงานใหญ่และสาขา · การรวมธุรกิจตาม TFRS 3 · '
            u'งบการเงินรวม ณ วันซื้อหุ้นและภายหลังวันซื้อหุ้น · <b>หลังมิดเทอม</b> งบรวมกรณีขาดทุน · '
            u'การด้อยค่าของค่าความนิยมตาม TAS 36 · กิจการร่วมค้าตาม TFRS 11 · '
            u'บุคคลหรือกิจการที่เกี่ยวข้องกันตาม TAS 24 '
            u'พร้อมสมุดรายวันคู่ กระดาษทำการ เครื่องมือคำนวณ และแบบทดสอบ')


MAST_PREV = MAST_NEW.replace(u'9 บท', u'8 บท').replace(
    u'งบรวมกรณีขาดทุน · รายการระหว่างบริษัทในเครือ · ', u'งบรวมกรณีขาดทุน · ')


def patch_mast(html):
    if MAST_NEW in html:
        return html, 0
    for old in (MAST_OLD, MAST_PREV):
        if html.count(old) == 1:
            return html.replace(old, MAST_NEW), 1
    if True:
        raise SystemExit(u'หาคำโปรยบนหัวหน้าไม่เจอ')


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

    print(u'ปรับ %d จาก 7 ชิ้น · %d → %d อักษร' % (steps, before, len(html)))
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
