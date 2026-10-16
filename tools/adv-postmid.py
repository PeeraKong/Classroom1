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
.tab[aria-controls="ch9"], #rail-ch9{--accent:var(--indigo); --accent-soft:var(--indigo-soft)}
/* สีประจำบทของสี่เรื่องในชีท 4_3 ย้ายมาอยู่ที่หัวกลุ่มและรายการในแถบข้าง
   เพราะทั้งสี่บทอยู่ในแท็บเดียวกันแล้ว จะผูกสีไว้กับปุ่มแท็บเหมือนเดิมไม่ได้ */
#rail-s43 .r-ch5{--accent:var(--green); --accent-soft:var(--green-soft)}
#rail-s43 .r-ch6{--accent:var(--red); --accent-soft:var(--red-soft)}
#rail-s43 .r-ch7{--accent:var(--teal); --accent-soft:var(--teal-soft)}
#rail-s43 .r-ch8{--accent:var(--clay); --accent-soft:var(--clay-soft)}
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
@media (max-width:560px){.gw-split{grid-template-columns:1fr}}
/* หัวคั่นของแต่ละบทในแท็บรวมของชีท 4_3 */
.grp + .grp{margin-top:34px}
.grp-h{display:flex; flex-wrap:wrap; gap:4px 12px; align-items:baseline; padding:14px 18px;
  border-left:4px solid var(--accent); background:var(--accent-soft);
  border-radius:0 8px 8px 0; margin:0 0 6px}
.grp-n{font-family:"IBM Plex Mono",monospace; font-size:.74rem; letter-spacing:.12em;
  text-transform:uppercase; color:var(--accent); font-weight:700}
.grp-t{font-family:"Noto Serif Thai",Georgia,serif; font-weight:700; font-size:1.18rem; color:var(--ink)}
.grp-s{font-family:"IBM Plex Mono",monospace; font-size:.72rem; color:var(--ink-3); margin-left:auto}
.grp > .sec:first-of-type{border-top:0; padding-top:14px}
@media (max-width:560px){.grp-s{margin-left:0; width:100%}}
/* หัวกลุ่มที่สองเป็นต้นไปในแถบข้างรวม ต้องมีระยะห่างจากรายการของกลุ่มก่อนหน้า */
.rail-h2{margin-top:18px; padding-top:14px; border-top:1px solid var(--rule)}"""


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
# ─────────────── สี่เรื่องที่มาจากเอกสาร Ch4_3 รวมอยู่ในแท็บเดียว ───────────────
# บทที่ 7 รายการระหว่างบริษัทในเครือ มาจากเอกสารคนละชุด จึงแยกเป็นแท็บของตัวเองต่อไป
SHEET43 = [
    ('ch5', u'บทที่ 6', u'งบการเงินรวม กรณีขาดทุน', u'TFRS 10 ย่อหน้า ข94 · TAS 28 ย่อหน้า 38-39'),
    ('ch6', u'บทที่ 8', u'การด้อยค่าของค่าความนิยม', u'TAS 36'),
    ('ch7', u'บทที่ 9', u'กิจการร่วมค้า', u'TFRS 11 · TAS 28'),
    ('ch8', u'บทที่ 10', u'บุคคลหรือกิจการที่เกี่ยวข้องกัน', u'TAS 24'),
]

S43_LEDE = (u'    <p class="lede">สี่เรื่องนี้มาจากเอกสารประกอบการสอน <b>Ch4_3</b> ฉบับเดียวกัน '
            u'จึงรวมไว้ในแท็บเดียวเพื่อให้อ่านรวดเดียวจบและค้นข้ามเรื่องได้ · '
            u'แถบข้างทางซ้ายแบ่งหัวข้อตามบทไว้ให้แล้ว · '
            u'<b>บทที่ 7 รายการระหว่างบริษัทในเครือ ไม่ได้อยู่ในเอกสารฉบับนี้</b> '
            u'จึงยังแยกเป็นแท็บของตัวเองตามเดิม · '
            u'ต้องการฉบับย่อที่ค้นได้ทั้งหน้าให้ดู <a href="sheet-4-3.html">สรุปชีท 4_3</a></p>\n')

TABS = u"""
    <span class="tab-div">หลังมิดเทอม</span>
    <button class="tab" role="tab" id="t-s43" aria-controls="s43" aria-selected="false" data-nar="ch5"><span class="tnum">ชีท</span>ชีท 4_3 · สี่เรื่องรวม</button>
    <button class="tab" role="tab" id="t-ch9" aria-controls="ch9" aria-selected="false"><span class="tnum">07</span>รายการระหว่างบริษัทในเครือ</button>"""


def strip_panel(block, cid):
    u"""ตัดเปลือก div ของแผงออก เหลือเฉพาะเนื้อข้างใน

    ใช้ตอนยุบสี่แผงให้เหลือแผงเดียว เนื้อหาและรหัสหัวข้อข้างในไม่ถูกแตะเลย
    ลิงก์ในแถบข้าง การเลื่อนตามหัวข้อ และบทบรรยายจึงยังชี้ถูกที่เหมือนเดิม
    """
    m = re.match(r'\s*<div id="%s"[^>]*>\n(.*)\n  </div>\s*$' % cid, block, re.S)
    if not m:
        raise SystemExit(u'รูปแบบของแผง %s ไม่ตรงกับที่คาด' % cid)
    return m.group(1)


def accent_of(block, cid):
    u"""ดึงชุดสีประจำบทออกมาจากแผงเดิม จะได้คงสีเดิมไว้ตอนยุบรวม"""
    m = re.search(r'<div id="%s"[^>]*style="([^"]*)"' % cid, block)
    return m.group(1) if m else u''


def build_s43(data):
    u"""ประกอบสี่เรื่องของชีท 4_3 ให้เป็นแผงเดียว โดยคั่นหัวเรื่องของแต่ละบท"""
    out = [u'  <div id="s43" class="hidden" role="tabpanel" aria-labelledby="t-s43">\n',
           S43_LEDE]
    for cid, num, title, std in SHEET43:
        block = getattr(data, cid.upper())
        out.append(u'    <div class="grp" id="grp-%s" style="%s">\n' % (cid, accent_of(block, cid)))
        out.append(u'      <div class="grp-h"><span class="grp-n">%s</span>'
                   u'<span class="grp-t">%s</span><span class="grp-s">%s</span></div>\n'
                   % (num, title, std))
        out.append(strip_panel(block, cid))
        out.append(u'\n    </div>\n')
    out.append(u'  </div>\n\n')
    return u''.join(out)


def rail_of(rails, cid):
    u"""ดึงรายการหัวข้อของบทหนึ่งออกมาจากก้อนแถบข้างเดิม"""
    m = re.search(r'<nav id="rail-%s"[^>]*>\s*<div class="rail-h">(.*?)</div>\s*(<ol>.*?</ol>)'
                  % cid, rails, re.S)
    if not m:
        raise SystemExit(u'หาแถบข้างของ %s ไม่เจอ' % cid)
    return m.group(1).strip(), m.group(2)


def build_rails(data):
    u"""แถบข้างรวมของชีท 4_3 หนึ่งก้อน และแถบข้างของบทที่ 7 แยกไว้ตามเดิม"""
    out = [u'    <nav id="rail-s43" class="hidden" aria-label="หัวข้อชีท 4_3">\n']
    for i, (cid, num, title, _) in enumerate(SHEET43):
        _, items = rail_of(data.RAILS, cid)
        out.append(u'      <div class="r-%s">\n' % cid)
        out.append(u'        <div class="rail-h%s">%s · %s</div>\n'
                   % (u' rail-h2' if i else u'', num, title))
        out.append(u'        ' + items + u'\n      </div>\n')
    out.append(u'    </nav>\n')
    head, items = rail_of(data.RAILS, 'ch9')
    out.append(u'    <nav id="rail-ch9" class="hidden" aria-label="หัวข้อรายการระหว่างบริษัทในเครือ">\n'
               u'      <div class="rail-h">%s</div>\n      %s\n    </nav>\n' % (head, items))
    return u''.join(out)


def patch_tabs(html):
    return splice(html, 'tabs', u'\n    ' + TABS + u'\n    ',
                  u'    <button class="tab" role="tab" id="t-ex" aria-controls="ex" '
                  u'aria-selected="false"><span class="tnum">E</span>แบบฝึกเขียนตอบ</button>')


def patch_railjs(html):
    s, e = jsmark('rails')
    want = s + u" s43:'rail-s43', ch9:'rail-ch9', " + e
    old = re.search(re.escape(s) + r'.*?' + re.escape(e), html, re.S)
    if old:
        return (html, 0) if old.group(0) == want else (html[:old.start()] + want + html[old.end():], 1)
    anchor = u"c4x:'rail-c4x', "
    if html.count(anchor) != 1:
        raise SystemExit(u'หาตาราง rails ใน JS ไม่เจอ')
    return html.replace(anchor, anchor + want + u' '), 1


# เครื่องเล่นเสียงจับคู่แท็บกับบทบรรยายด้วย aria-controls ซึ่งแท็บรวมไม่มีบทของตัวเอง
# จึงให้แท็บบอกเองได้ว่าจะให้เครื่องเล่นเปิดบทไหน ผ่าน data-nar
OLD_SYNC = u"""      var k = t.getAttribute('aria-controls');
      if (playing || !DATA[k] || k === cur) return;"""

NEW_SYNC = u"""      var k = t.getAttribute('data-nar') || t.getAttribute('aria-controls');
      if (playing || !DATA[k] || k === cur) return;"""


def patch_narsync(html):
    before = html
    if NEW_SYNC in html:
        return html, 0
    if html.count(OLD_SYNC) != 1:
        raise SystemExit(u'โค้ดจับคู่แท็บกับเครื่องเล่นไม่ตรงกับที่คาด')
    html = html.replace(OLD_SYNC, NEW_SYNC)
    return html, (0 if html == before else 1)


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


MAST_NEW = (u'สื่อประกอบการเรียน 10 บท · <b>ก่อนมิดเทอม</b> บัญชีสำนักงานใหญ่และสาขา · '
            u'การรวมธุรกิจตาม TFRS 3 · งบการเงินรวม ณ วันซื้อหุ้นและภายหลังวันซื้อหุ้น · '
            u'<b>หลังมิดเทอม</b> งบรวมกรณีขาดทุน · รายการระหว่างบริษัทในเครือ · '
            u'การด้อยค่าของค่าความนิยมตาม TAS 36 · กิจการร่วมค้าตาม TFRS 11 · '
            u'บุคคลหรือกิจการที่เกี่ยวข้องกันตาม TAS 24 '
            u'พร้อมสมุดรายวันคู่ กระดาษทำการ เครื่องมือคำนวณ และแบบทดสอบ')


def patch_mast(html):
    u"""เขียนทับคำโปรยใต้ชื่อวิชาทั้งย่อหน้า

    เขียนทับทั้งก้อนแทนการจับคู่ข้อความเดิม เพราะคำโปรยถูกแก้มาหลายรอบแล้ว
    การไล่จับคู่ของเก่าทุกรุ่นจะพังทันทีที่ลืมรุ่นใดรุ่นหนึ่ง
    """
    m = re.search(r'(<p class="mast-sub">)(.*?)(</p>)', html, re.S)
    if not m:
        raise SystemExit(u'หาคำโปรยใต้ชื่อวิชาไม่เจอ')
    if m.group(2) == MAST_NEW:
        return html, 0
    return html[:m.start(2)] + MAST_NEW + html[m.end(2):], 1


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


PANEL_RE = (r'<div id="%s"[^>]*role="tabpanel".*?'
            r'(?=\n  <div id="[\w-]+"[^>]*role="tabpanel"|\n  </main>)')

# แท็บไหนเป็นที่อยู่ของบทไหน หลังยุบสี่เรื่องของชีท 4_3 เข้าแท็บเดียว
HOME = dict([(cid, 's43') for cid, _, _, _ in SHEET43] + [('ch9', 'ch9')])


def verify(html, chapters):
    bad = 0
    panels = {}
    for pid in sorted(set(HOME.values())):
        m = re.search(PANEL_RE % pid, html, re.S)
        if not m:
            print(u'  หาแผง %s ในหน้าไม่เจอ' % pid); bad += 1
        panels[pid] = m.group(0) if m else u''

    for ch, title, secs in chapters:
        pid = HOME[ch]
        panel = panels.get(pid, u'')
        got = re.findall(r'<section class="sec" id="(%s-\d+)">' % ch, panel)
        want = [u'%s-%d' % (ch, i + 1) for i in range(len(secs))]
        if got != want:
            print(u'  %-4s หัวข้อไม่ตรง หรือไม่ได้อยู่ในแผง %s · มี %s'
                  % (ch, pid, ' '.join(got))); bad += 1
        for sid in want:
            if ('href="#%s"' % sid) not in html:
                print(u'  %-4s แถบข้างไม่มีลิงก์ไป %s' % (ch, sid)); bad += 1
        print(u'  %-4s %-38s %2d หัวข้อ · อยู่ในแท็บ %s' % (ch, title, len(got), pid))

    # แท็บและแถบข้างต้องมีครบเท่าที่ใช้จริง และบทที่ยุบรวมต้องไม่เหลือของเดิมค้าง
    for pid in sorted(set(HOME.values())):
        for need in (u'id="t-%s"' % pid, u'id="rail-%s"' % pid, u"%s:'rail-%s'" % (pid, pid)):
            if need not in html:
                print(u'  ขาด %s' % need); bad += 1
    for cid, _, _, _ in SHEET43:
        for stale in (u'id="t-%s"' % cid, u'id="rail-%s"' % cid, u'aria-controls="%s"' % cid):
            if stale in html:
                print(u'  ยังมีของเดิมของ %s ค้างอยู่ · %s' % (cid, stale)); bad += 1
    if 'data-nar="ch5"' not in html:
        print(u'  แท็บรวมไม่ได้บอกเครื่องเล่นว่าให้เปิดบทไหน'); bad += 1
    if "t.getAttribute('data-nar')" not in html:
        print(u'  เครื่องเล่นยังไม่รู้จัก data-nar'); bad += 1

    # บทบรรยายยังต้องมีครบห้าบท เพราะไฟล์เสียงผูกกับรหัสบท ไม่ได้ผูกกับแท็บ
    m = re.search(r'id="cn-data">\n(.*?)\n</script>', html, re.S)
    if m:
        import json
        data = json.loads(m.group(1))
        for ch, _, _ in chapters:
            if ch not in data:
                print(u'  บทบรรยายของ %s หายไป' % ch); bad += 1

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
    for fn in (patch_css, patch_tabs, patch_railjs, patch_mast, patch_narsync):
        html, n = fn(html)
        steps += n
    html, n = patch_rails(html, build_rails(D)); steps += n
    # สี่เรื่องของชีท 4_3 ยุบเป็นแผงเดียว ส่วนบทที่ 7 ซึ่งมาจากเอกสารคนละชุดยังแยกอยู่
    html, n = patch_panels(html, build_s43(D) + D.CH9); steps += n
    html, n = patch_quiz(html, D.QUIZ, D.QUIZ_TOTAL); steps += n

    print(u'ปรับ %d ชิ้น · %d → %d อักษร' % (steps, before, len(html)))
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
