#!/usr/bin/env python3
# -*- coding: utf-8 -*-
u"""สร้างแท็บสรุปรวบยอดของวิชาการสอบบัญชี แล้ววางลงหน้าเว็บ

แท็บนี้ไม่ใช่เนื้อหาซ้ำกับบทเรียน แต่เป็นชีทอ่านก่อนสอบ คือบีบทั้งวิชาให้อยู่ใน
หน้าเดียวที่กวาดตาได้เร็ว เน้นตารางเทียบ กฎลัด และกับดักที่ตอบผิดบ่อย
ส่วนที่มีค่าที่สุดคือสองตารางท้าย ซึ่งไม่มีอยู่ที่อื่นในเว็บ

    python3 tools/audit-summary.py            วางลงหน้าเว็บ
    python3 tools/audit-summary.py --check    ตรวจอย่างเดียว
"""

import argparse
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGE = os.path.join(ROOT, 'audit', 'index.html')

TAB = (u'    <button class="tab" role="tab" id="t-sm" aria-controls="sm" aria-selected="false">'
       u'<span class="tnum">S</span>สรุปรวบยอด</button>\n')
TAB_ANCHOR = u'    <button class="tab" role="tab" id="t-quiz"'

RAIL = u'''    <nav id="rail-sm" class="hidden" aria-label="หัวข้อสรุปรวบยอด">
      <div class="rail-h">สรุปรวบยอด · 14 หัวข้อ</div>
      <ol>
        <li><a href="#sm-1"><i>1</i>เส้นเรื่องทั้งวิชา</a></li>
        <li><a href="#sm-2"><i>2</i>ข้อกำหนดของผู้บริหาร</a></li>
        <li><a href="#sm-3"><i>3</i>หลักการสามกลุ่ม</a></li>
        <li><a href="#sm-4"><i>4</i>หลักฐาน</a></li>
        <li><a href="#sm-5"><i>5</i>ความมีสาระสำคัญ</a></li>
        <li><a href="#sm-6"><i>6</i>แบบจำลองความเสี่ยง</a></li>
        <li><a href="#sm-7"><i>7</i>การทุจริต</a></li>
        <li><a href="#sm-8"><i>8</i>วิธีการตรวจสอบ</a></li>
        <li><a href="#sm-9"><i>9</i>เอกสารหลักฐาน</a></li>
        <li><a href="#sm-10"><i>10</i>สี่ประเภทงาน</a></li>
        <li><a href="#sm-11"><i>11</i>จรรยาบรรณ</a></li>
        <li><a href="#sm-12"><i>12</i>การเลือกตัวอย่าง</a></li>
        <li><a href="#sm-13"><i>13</i>กับดัก 24 ข้อ</a></li>
        <li><a href="#sm-14"><i>14</i>คู่คำที่สับสน</a></li>
      </ol>
    </nav>
'''
RAIL_ANCHOR = u'    <nav id="rail-quiz"'

CSS = u'''
/* แท็บสรุปรวบยอด · บีบให้แน่นกว่าแท็บบทเรียน เพราะใช้กวาดตาก่อนสอบ */
#sm .sec{padding-top:26px}
#sm .sec + .sec{padding-top:26px}
#sm .body > p{font-size:.9rem}
#sm table.tbl{font-size:.8rem}
#sm table.tbl td{padding:6px 11px}
#sm .note{font-size:.87rem; padding:10px 14px}
.sm-tools{display:flex; flex-wrap:wrap; gap:7px; margin-bottom:18px}
.sm-tools button{appearance:none; font:inherit; font-size:.79rem; font-weight:600; cursor:pointer;
  padding:5px 12px; border:1px solid var(--rule-strong); background:var(--surface);
  color:var(--ink-2); border-radius:3px}
.sm-tools button:hover{border-color:var(--accent); color:var(--accent)}

/* กฎลัดที่อยากให้จำเป็นประโยค วางเป็นแถบเดี่ยวให้สะดุดตา */
.sm-rule{border:1px solid var(--rule-strong); border-left:3px solid var(--teal);
  border-radius:0 4px 4px 0; background:var(--surface); padding:9px 14px;
  margin:10px 0; font-size:.88rem}
.sm-rule b{color:var(--ink)}
.sm-rule .k{font-family:"IBM Plex Mono",monospace; font-size:.68rem; letter-spacing:.1em;
  text-transform:uppercase; color:var(--teal); display:block; margin-bottom:2px}

/* เส้นเรื่องของวิชา · คำถามประจำบทเรียงต่อกัน */
.sm-spine{list-style:none; margin:14px 0 18px; padding:0; display:flex;
  flex-direction:column; gap:0}
.sm-spine li{display:flex; gap:12px; align-items:baseline; padding:9px 0;
  border-bottom:1px solid var(--rule); font-size:.89rem}
.sm-spine li:last-child{border-bottom:0}
.sm-spine .w{flex:0 0 96px; font-family:"IBM Plex Mono",monospace; font-size:.7rem;
  letter-spacing:.09em; text-transform:uppercase; color:var(--accent); font-weight:600}
.sm-spine .a{color:var(--ink-2)}
.sm-spine .a b{color:var(--ink)}

@media print{
  .sm-tools{display:none !important}
  #sm .sec{break-inside:auto; padding-top:18px}
  #sm .tw{break-inside:avoid; overflow:visible}
  #sm table.tbl{min-width:0; font-size:.72rem}
  #sm .card,#sm .note,#sm .sm-rule{break-inside:avoid}
}
'''
CSS_ANCHOR = u'\n/* slide figures'

SECTION = u'''  <div id="sm" class="hidden" role="tabpanel" aria-labelledby="t-sm">
    <p class="lede">แท็บนี้<b>ไม่ใช่เนื้อหาซ้ำกับบทเรียน</b> แต่เป็น<b>ชีทอ่านก่อนสอบ</b> คือบีบทั้งวิชาให้กวาดตาได้เร็ว เน้น<b>ตารางเทียบ กฎลัด และกับดักที่ตอบผิดบ่อย</b> · ถ้าอ่านแล้วสะดุดตรงไหน ให้กลับไปที่แท็บของบทนั้นเพื่อดูเหตุผลเต็ม ๆ</p>

    <div class="sm-tools">
      <button type="button" id="sm-print">พิมพ์เป็นชีทสรุป</button>
    </div>

    <div class="note key" style="margin-bottom:22px"><span class="nh">อ่านอย่างไรให้ได้ผลที่สุด</span>อ่าน<b>หัวข้อ 13 กับ 14 ก่อน</b> เพราะเป็นจุดที่คนเสียคะแนนมากที่สุด แล้วค่อยย้อนขึ้นมาอ่านหัวข้อ 1 ถึง 12 เพื่อเติมโครง · ระหว่างอ่านให้<b>ปิดคอลัมน์ขวาของตารางไว้</b>แล้วลองตอบเองก่อน ถ้าตอบได้ทุกแถวแปลว่าพร้อมแล้ว</div>

    <section class="sec" id="sm-1">
      <div class="sec-h"><span class="sec-n">1</span><h2>เส้นเรื่องของทั้งวิชา</h2></div>
      <div class="body">
        <p class="lede">ทุกบทตอบคำถามเดียวต่อกันเป็นลูกโซ่ ถ้าจำลำดับนี้ได้ จะรู้ว่าเนื้อหาแต่ละก้อนอยู่ตรงไหนของภาพใหญ่</p>
        <ul class="sm-spine">
          <li><span class="w">ทำไมต้องมี</span><span class="a">คนทำงบกับคนใช้งบเป็นคนละคน และคนทำมีแรงจูงใจ · ผู้สอบบัญชีเข้ามาลด<b>ความเสี่ยงของข้อมูล</b> ไม่ใช่ความเสี่ยงทางธุรกิจ</span></li>
          <li><span class="w">ทำตามอะไร</span><span class="a">มาตรฐานแตกเป็นสามกลุ่ม คือ<b>คนตรวจเป็นใคร · ตรวจอย่างไร · บอกผลอย่างไร</b></span></li>
          <li><span class="w">เริ่มอย่างไร</span><span class="a">รับงานหรือไม่ → เช็กความเป็นอิสระ → ทำหนังสือตอบรับ → ตั้ง<b>ความมีสาระสำคัญ</b></span></li>
          <li><span class="w">ตรวจหนักแค่ไหน</span><span class="a">ขึ้นกับความเสี่ยง · ฝั่งลูกค้าเปลี่ยนไม่ได้ เราปรับได้ตัวเดียวคือ<b>ความเสี่ยงที่จะตรวจไม่เจอ</b></span></li>
          <li><span class="w">ตรวจอะไร</span><span class="a">ทุกวิธีตรวจมีไว้พิสูจน์<b>ข้อกำหนดของผู้บริหาร</b>ข้อใดข้อหนึ่งเสมอ ถ้าตอบไม่ได้ว่ากำลังพิสูจน์ข้อไหน แปลว่ายังไม่เข้าใจว่าทำไปทำไม</span></li>
          <li><span class="w">ใช้อะไรตัดสิน</span><span class="a">หลักฐานที่<b>เพียงพอ</b>ในแง่ปริมาณ และ<b>เหมาะสม</b>ในแง่คุณภาพ · การถามอย่างเดียวไม่เคยพอ</span></li>
          <li><span class="w">จบอย่างไร</span><span class="a">แสดงความเห็นว่างบเป็นไปตาม<b>แม่บทที่ใช้</b>หรือไม่ หรือระบุว่าแสดงความเห็นไม่ได้ · จะเงียบไม่ได้</span></li>
        </ul>
        <div class="sm-rule"><span class="k">ประโยคเดียวที่สรุปทั้งวิชา</span>งานของผู้สอบบัญชีคือ<b>เปลี่ยนคำกล่าวอ้างให้กลายเป็นสิ่งที่พิสูจน์ได้</b> ภายใต้ต้นทุนและเวลาที่สมเหตุสมผล</div>
      </div>
    </section>

    <section class="sec" id="sm-2">
      <div class="sec-h"><span class="sec-n">2</span><h2>ข้อกำหนดของผู้บริหาร</h2></div>
      <div class="body">
        <p>ตัวเลขก้อนเดียวผิดได้หลายแบบ และแต่ละแบบต้องใช้วิธีตรวจคนละวิธี · คอลัมน์กลางคือ<b>คำถามที่ข้อกำหนดนั้นถาม</b> ซึ่งเป็นสิ่งที่ต้องตอบให้ได้ในห้องสอบ</p>
        <div class="tw">
          <table class="tbl">
            <thead><tr><th>ข้อกำหนด</th><th>ถามว่าอะไร</th><th>วิธีตรวจที่คู่กัน</th><th>กลุ่ม</th></tr></thead>
            <tbody>
              <tr><td class="asb">Occurrence</td><td class="q">ที่จดไว้ เกิดขึ้นจริงไหม</td><td>vouching · จากบัญชีไปหาเอกสาร</td><td>รายการค้า</td></tr>
              <tr><td class="asb">Existence</td><td class="q">ที่จดไว้ มีอยู่จริงไหม ณ วันสิ้นงวด</td><td>ตรวจนับ · ยืนยันยอด</td><td>ยอดคงเหลือ</td></tr>
              <tr><td class="asb">Completeness</td><td class="q">ที่มีจริง จดครบไหม</td><td>tracing · จากเอกสารไปหาบัญชี · อ่านรายงานการประชุม</td><td>ทั้งสองกลุ่ม</td></tr>
              <tr><td class="asb">Rights &amp; obligations</td><td class="q">เป็นของกิจการจริงไหม</td><td>ตรวจโฉนด สัญญา และภาระผูกพัน</td><td>ยอดคงเหลือ</td></tr>
              <tr><td class="asb">Accuracy</td><td class="q">จำนวนเงินถูกไหม</td><td>คำนวณใหม่ · ทานกับเอกสารต้นทาง</td><td>รายการค้า</td></tr>
              <tr><td class="asb">Valuation &amp; allocation</td><td class="q">ตีมูลค่าเหมาะสมไหม เก็บเงินได้จริงเท่าไร</td><td>คำนวณค่าเผื่อใหม่ · สอบทานประมาณการ</td><td>ยอดคงเหลือ</td></tr>
              <tr><td class="asb">Cutoff</td><td class="q">อยู่ในงวดที่ถูกไหม</td><td>ตรวจรายการคร่อมวันสิ้นงวด</td><td>รายการค้า</td></tr>
              <tr><td class="asb">Classification</td><td class="q">ลงบัญชีถูกช่องไหม</td><td>ทานผังบัญชีกับลักษณะของรายการ</td><td>รายการค้า</td></tr>
              <tr><td class="asb">Presentation</td><td class="q">คนอ่านได้รู้ครบไหม</td><td>ทานหมายเหตุประกอบกับสัญญา</td><td>การเปิดเผย</td></tr>
            </tbody>
          </table>
        </div>
        <div class="sm-rule"><span class="k">เทียบสองมาตรฐาน</span>กรอบ<b>ห้าข้อ</b>รวม <b>existence กับ occurrence</b> ไว้ด้วยกัน และรวม <b>classification กับ presentation</b> ไว้ด้วยกัน · กรอบที่<b>ละเอียดกว่า</b>แยกออกเป็นสองกลุ่ม คือ<b>รายการค้าที่เกิดระหว่างงวด</b> กับ<b>ยอดคงเหลือ ณ วันสิ้นงวด</b> · จับคำว่า<b>ระหว่างงวด</b>กับ<b>สิ้นงวด</b>ได้ ก็แยกสองกลุ่มออกแล้ว</div>
        <div class="sm-rule"><span class="k">ข้อที่ยากที่สุดเสมอ</span><b>Completeness</b> ยากกว่าข้ออื่นเพราะต้องค้นหา<b>สิ่งที่ไม่ปรากฏในบัญชี</b> จึงไม่มีจุดตั้งต้นในระบบของกิจการให้เริ่ม ต้องไปเริ่มจากนอกบัญชีเสมอ</div>
      </div>
    </section>

    <section class="sec" id="sm-3">
      <div class="sec-h"><span class="sec-n">3</span><h2>หลักการสามกลุ่ม</h2></div>
      <div class="body">
        <div class="tw">
          <table class="tbl">
            <thead><tr><th>กลุ่ม</th><th>ว่าด้วยอะไร</th><th>ประกอบด้วย</th></tr></thead>
            <tbody>
              <tr><td class="pc">Responsibilities</td><td>คนตรวจเป็นใคร · คลุมทั้งงานตั้งแต่ก่อนรับงาน</td><td>ความรู้ความสามารถ · <b>ความเป็นอิสระ</b> · ความระมัดระวัง · ความสงสัยและดุลยพินิจ</td></tr>
              <tr><td class="pc">Performance</td><td>ตรวจอย่างไร · คลุมตั้งแต่วางแผนถึงเก็บหลักฐาน</td><td>วางแผนและควบคุมงาน · <b>ความมีสาระสำคัญ</b> · ประเมินความเสี่ยง · หลักฐาน</td></tr>
              <tr><td class="pc">Reporting</td><td>บอกผลอย่างไร · คลุมเฉพาะขั้นสุดท้าย</td><td>แสดงความเห็นหรือระบุว่าแสดงไม่ได้ · เทียบกับแม่บทการรายงาน</td></tr>
            </tbody>
          </table>
        </div>
        <div class="grid g2">
          <div class="card">
            <span class="cn">independence</span>
            <div class="ct">ความเป็นอิสระสองด้าน ต้องมีครบทั้งคู่</div>
            <div class="cs"><b>ในข้อเท็จจริง</b> คือสภาพจิตใจที่เป็นกลาง อยู่ในใจ พิสูจน์ให้ใครดูไม่ได้<br><br><b>ในการปรากฏ</b> คือภาพที่คนนอกเห็น วัดจากว่า<b>นักลงทุนที่สมเหตุสมผลซึ่งรู้ข้อเท็จจริงทั้งหมด</b>จะสงสัยไหม<br><br>ขาดด้านใดด้านหนึ่ง<b>ก็ถือว่าขาดแล้ว</b></div>
          </div>
          <div class="card">
            <span class="cn">reasonable assurance</span>
            <div class="ct">ทำไมให้ได้แค่ความเชื่อมั่นอย่างสมเหตุสมผล</div>
            <div class="cs"><b>หนึ่ง</b> ตรวจทุกรายการมีต้นทุนสูงเกินประโยชน์<br><b>สอง</b> งบมีประมาณการที่<b>ไม่มีคำตอบเดียวที่ถูก</b> มีแต่ช่วงที่สมเหตุสมผล<br><b>สาม</b> การทุจริตที่มีการสมรู้ร่วมคิดออกแบบมาเพื่อหลบการตรวจโดยเฉพาะ<br><br>ช่องว่างระหว่างสิ่งที่สังคมคาดหวังกับสิ่งที่เรารับปาก เรียกว่า <b>expectation gap</b></div>
          </div>
        </div>
      </div>
    </section>

    <section class="sec" id="sm-4">
      <div class="sec-h"><span class="sec-n">4</span><h2>หลักฐานการสอบบัญชี</h2></div>
      <div class="body">
        <div class="sm-rule"><span class="k">สองคำที่ออกสอบแทบทุกครั้ง</span><b>เพียงพอ</b> คือเรื่อง<b>ปริมาณ</b> ขึ้นกับประสิทธิผลของการควบคุมภายใน · <b>เหมาะสม</b> คือเรื่อง<b>คุณภาพ</b> แตกเป็น<b>ความเกี่ยวข้อง</b> คือตอบตรงข้อกำหนดที่สนใจไหม และ<b>ความน่าเชื่อถือ</b> คือมาจากแหล่งไหน</div>
        <div class="tw">
          <table class="tbl">
            <thead><tr><th>ลำดับ</th><th>แหล่งที่มา</th><th>ตัวอย่าง</th><th>เงื่อนไขที่ทำให้ตกชั้น</th></tr></thead>
            <tbody>
              <tr><td class="pc">สูงสุด</td><td>ความรู้โดยตรงของผู้สอบบัญชี</td><td>ไปตรวจนับด้วยตาตัวเอง</td><td>—</td></tr>
              <tr><td class="pc">กลาง</td><td>เอกสารจากภายนอกกิจการ</td><td>หนังสือยืนยันยอดจากธนาคารหรือลูกหนี้</td><td><b>ตกลงมาเป็นระดับต่ำสุดทันทีถ้าผ่านมือลูกค้า</b></td></tr>
              <tr><td class="pc">ต่ำสุด</td><td>เอกสารภายในกิจการ</td><td>รายงานอายุลูกหนี้ที่ฝ่ายบัญชีพิมพ์ให้</td><td>—</td></tr>
            </tbody>
          </table>
        </div>
        <div class="sm-rule"><span class="k">กับดักเรื่องความเกี่ยวข้อง</span>หนังสือยืนยันยอดลูกหนี้<b>ดีสำหรับ existence</b> แต่<b>อ่อนสำหรับ valuation</b> เพราะลูกหนี้ที่ยืนยันว่าเป็นหนี้จริง อาจกำลังจะล้มละลาย · และ<b>ตอบ completeness ไม่ได้เลย</b> เพราะรายชื่อที่ใช้ส่งมาจากกิจการเอง</div>
      </div>
    </section>

    <section class="sec" id="sm-5">
      <div class="sec-h"><span class="sec-n">5</span><h2>ความมีสาระสำคัญ</h2></div>
      <div class="body">
        <div class="sm-rule"><span class="k">คำเดียวที่ตอบผิดกันมากที่สุด</span>นิยามอ้างอิงถึงการตัดสินใจของ<b>ผู้ใช้งบการเงิน</b> ไม่ใช่ผู้บริหาร และไม่ใช่ทีมสอบบัญชี</div>
        <div class="grid g2">
          <div class="card">
            <span class="cn">เชิงปริมาณ</span>
            <div class="ct">สามตัว</div>
            <div class="cs"><b>ขนาดสัมบูรณ์</b> จำนวนเงินล้วน ๆ<br><b>ขนาดสัมพัทธ์</b> เทียบกับฐาน เช่นกำไรก่อนภาษี รายได้ หรือสินทรัพย์รวม<br><b>ผลสะสม</b> ข้อผิดพลาดเล็ก ๆ หลายรายการรวมกัน<br><br>มาตรฐาน<b>ไม่เคยกำหนดเปอร์เซ็นต์ตายตัว</b> เพราะถ้ากำหนดเมื่อไร คนแต่งบัญชีก็รู้ทันทีว่าต้องแต่งไม่ให้เกินเท่าไร</div>
          </div>
          <div class="card">
            <span class="cn">เชิงคุณภาพ</span>
            <div class="ct">ทำให้เงินก้อนเล็กกลายเป็นเรื่องใหญ่ได้</div>
            <div class="cs">รายการที่<b>พลิกขาดทุนเป็นกำไร</b><br>รายการที่<b>ทำให้ผ่านเงื่อนไขสัญญาเงินกู้ได้พอดี</b><br><b>การทุจริตที่ผู้บริหารเป็นคนทำ มีสาระสำคัญเสมอ</b> ไม่ว่าเงินจะน้อยแค่ไหน เพราะสิ่งที่เสียคือความน่าเชื่อถือของคำกล่าวอ้างทั้งหมด</div>
          </div>
        </div>
        <div class="sm-rule"><span class="k">สองชั้นและทิศทางของมัน</span><b>เกณฑ์รวมของงบทั้งฉบับ</b> กระจายลงมาเป็น<b>เกณฑ์ระดับปฏิบัติงานของแต่ละกลุ่มรายการ</b> ซึ่ง<b>ตั้งต่ำกว่าโดยตั้งใจ</b> เพื่อเผื่อที่ให้ข้อผิดพลาดที่สุ่มไม่เจอ · <b>บัญชีเสี่ยงสูง ตั้งเกณฑ์ต่ำ</b> เพราะเกณฑ์ที่ต่ำทำให้รายการที่ต้องตรวจมีมากขึ้น</div>
      </div>
    </section>

    <section class="sec" id="sm-6">
      <div class="sec-h"><span class="sec-n">6</span><h2>แบบจำลองความเสี่ยง</h2></div>
      <div class="body">
        <div class="tw">
          <table class="tbl">
            <thead><tr><th>ตัว</th><th>คืออะไร</th><th>เป็นของใคร</th><th>เราทำอะไรกับมัน</th></tr></thead>
            <tbody>
              <tr><td class="pc">AR</td><td>เสี่ยงที่เราจะเซ็นรับรองงบที่มีปัญหา</td><td>เรา</td><td><b>ตั้งเอง</b> ไว้ต่ำ และไม่เปลี่ยนตามความยากของงาน</td></tr>
              <tr class="grp"><td class="pc">IR</td><td>เสี่ยงที่ความผิดพลาดจะเกิดตั้งแต่แรก โดยยังไม่คิดถึงระบบควบคุม</td><td>ลูกค้า</td><td><b>ประเมิน</b> เปลี่ยนไม่ได้</td></tr>
              <tr><td class="pc">CR</td><td>เสี่ยงที่ระบบควบคุมของลูกค้าจะจับไม่ได้</td><td>ลูกค้า</td><td><b>ประเมิน</b> เปลี่ยนไม่ได้</td></tr>
              <tr class="grp"><td class="pc">DR</td><td>เสี่ยงที่วิธีตรวจของเราเองจะไม่เจอ</td><td><b>เรา</b></td><td><b>คำนวณออกมา</b> และเป็นตัวเดียวที่คุมได้</td></tr>
            </tbody>
          </table>
        </div>
        <div class="sm-rule"><span class="k">สูตรและสิ่งที่มันบังคับ</span><b>AR = IR × CR × DR</b> · ย้ายข้างได้ว่า <b>DR = AR ÷ (IR × CR)</b> · <b>RMM = IR × CR</b> เป็นฝั่งลูกค้าทั้งหมด <b>ไม่มี DR อยู่ในนั้น</b> · ความเสี่ยงฝั่งลูกค้าสูงขึ้นเมื่อ AR คงที่ → <b>DR ต้องต่ำลง</b> → <b>เราต้องทำงานหนักขึ้น</b></div>
        <div class="tw">
          <table class="tbl">
            <thead><tr><th>มิติ</th><th>ถามว่าอะไร</th><th>DR ต่ำ · เสี่ยงสูง</th><th>DR สูง · เสี่ยงต่ำ</th></tr></thead>
            <tbody>
              <tr><td class="pc">ลักษณะ</td><td>ใช้วิธีไหน</td><td>วิธีที่มีประสิทธิผลมากขึ้น เช่นยืนยันยอดแทนการวิเคราะห์</td><td>วิธีที่เบาลง</td></tr>
              <tr><td class="pc">เวลา</td><td>ตรวจตอนไหน</td><td><b>ณ วันสิ้นงวด</b></td><td>ระหว่างงวดได้</td></tr>
              <tr><td class="pc">ขอบเขต</td><td>ตรวจกี่ราย</td><td>มากขึ้น</td><td>น้อยลง</td></tr>
            </tbody>
          </table>
        </div>
        <div class="sm-rule"><span class="k">ทำไมเสี่ยงสูงต้องตรวจสิ้นงวด</span>ถ้าไปตรวจแต่เนิ่น ๆ จะเหลือ<b>ช่องว่างช่วงท้ายปี</b>ที่ไม่ได้ดูเลย และนั่นคือช่วงที่ผู้บริหารรู้แล้วว่าทั้งปีจะเข้าเป้าหรือไม่ · ถ้าจะมีการปั้นตัวเลข มันมักเกิดตรงนั้นพอดี</div>
        <div class="sm-rule"><span class="k">ซอยย่อย DR อีกสองแบบ</span><b>จากการสุ่ม</b> คือตัวอย่างที่หยิบมาไม่เป็นตัวแทน <b>แก้ด้วยการเพิ่มขนาดตัวอย่าง</b> · <b>ไม่ได้เกิดจากการสุ่ม</b> คือเลือกวิธีผิดหรือตีความหลักฐานผิด <b>เพิ่มตัวอย่างไม่ช่วยเลย</b> ต้องแก้ด้วยการฝึกอบรมและการควบคุมดูแลงาน</div>
      </div>
    </section>

    <section class="sec" id="sm-7">
      <div class="sec-h"><span class="sec-n">7</span><h2>การทุจริต</h2></div>
      <div class="body">
        <div class="sm-rule"><span class="k">สิ่งเดียวที่แยกข้อผิดพลาดจากการทุจริต</span><b>เจตนา</b> · ตัวเลขผิดเท่ากันเป๊ะ แต่กดคีย์ผิดคือข้อผิดพลาด ตั้งใจแต่งคือทุจริต · ในทางปฏิบัติดูจาก<b>ทิศทาง</b> ข้อผิดพลาดที่ไม่ตั้งใจกระจายทั้งสองทาง ส่วนความเอนเอียงที่เป็นระบบคือร่องรอยของเจตนา</div>
        <div class="grid g3">
          <div class="card">
            <span class="cn">สามเหลี่ยม</span>
            <div class="ct">เงื่อนไขที่มักมีครบพร้อมกัน</div>
            <div class="cs"><b>แรงกดดัน</b> หนี้ส่วนตัว เป้ากำไรที่ผูกกับโบนัส เงื่อนไขเงินกู้ที่กำลังจะผิด<br><br><b>โอกาส</b> คนเดียวคุมทั้งรับเงินและลงบัญชี ผู้บริหารสั่งข้ามระบบได้<br><br><b>การหาเหตุผลเข้าข้างตัวเอง</b> แค่ยืมไว้ก่อน บริษัทเอาเปรียบเรามาตลอด</div>
          </div>
          <div class="card">
            <span class="cn">สองประเภท</span>
            <div class="ct">แยกด้วยคำถามว่าใครเจ็บ</div>
            <div class="cs"><b>รายงานการเงินที่เป็นเท็จ</b><br>ผู้บริหารทำ · ผู้ลงทุนและเจ้าหนี้เจ็บ · เงินก้อนใหญ่<br><br><b>การยักยอกสินทรัพย์</b><br>พนักงานทำ · บริษัทเจ็บ · เงินไม่ใหญ่แต่เกิดถี่และยาวนาน</div>
          </div>
          <div class="card">
            <span class="cn">สองคำที่สับสน</span>
            <div class="ct">เส้นแบ่งคือการได้รับมอบหมายให้ดูแล</div>
            <div class="cs"><b>Embezzlement</b> ยักยอกของที่ตนดูแลอยู่แล้ว เช่นแคชเชียร์เอาเงินในลิ้นชักตัวเอง · มี<b>การทรยศความไว้วางใจ</b>เพิ่มอีกชั้น<br><br><b>Larceny</b> ลักทรัพย์ที่ไม่ได้อยู่ในความดูแลของตน</div>
          </div>
        </div>
        <div class="sm-rule"><span class="k">ข้อสันนิษฐานสองข้อที่มีในทุกงาน</span><b>การรับรู้รายได้ที่ไม่เหมาะสมเป็นความเสี่ยงจากการทุจริต</b> ถือว่ามีตั้งแต่ต้น ถ้าจะสรุปว่าไม่มี<b>ต้องเขียนเหตุผลไว้</b> · <b>การล้มล้างการควบคุมโดยผู้บริหาร</b> มีเสมอไม่ว่าระบบจะดีแค่ไหน เพราะคนที่ออกแบบระบบและสั่งยกเว้นได้ ย่อมอยู่เหนือระบบ <b>ห้ามสรุปว่าไม่มี</b></div>
        <div class="sm-rule"><span class="k">วิธีรับมือการล้มล้างการควบคุม</span><b>ตรวจรายการในสมุดรายวันทั่วไปและรายการปรับปรุง</b> · สอบทานความเอนเอียงของประมาณการ · ประเมินเหตุผลทางธุรกิจของรายการผิดปกติ · สิ่งที่มองหาคือรายการลงวันสิ้นปีตอนดึก ตัวเลขกลม ๆ คำอธิบายว่างเปล่า หรือคีย์โดยคนที่ปกติไม่มีหน้าที่คีย์</div>
        <div class="sm-rule"><span class="k">เมื่อเจอทุจริต</span>รายงานไปที่<b>ระดับสูงกว่าผู้เกี่ยวข้องอย่างน้อยหนึ่งระดับ</b> · ถ้าคนทำคือผู้บริหาร <b>ถือว่ามีสาระสำคัญเสมอ</b>และรายงานต่อคณะกรรมการตรวจสอบ · ในกระดาษทำการ<b>เขียนข้อเท็จจริงที่พบ ไม่เขียนว่าใครทุจริต</b> เพราะนั่นเป็นข้อสรุปทางกฎหมาย</div>
      </div>
    </section>

    <section class="sec" id="sm-8">
      <div class="sec-h"><span class="sec-n">8</span><h2>วิธีการตรวจสอบ</h2></div>
      <div class="body">
        <div class="tw">
          <table class="tbl">
            <thead><tr><th>กลุ่ม</th><th>ถามว่าอะไร</th><th>ตัวอย่าง</th></tr></thead>
            <tbody>
              <tr><td class="pc">ประเมินความเสี่ยง</td><td>กิจการนี้เป็นอย่างไร เสี่ยงตรงไหน</td><td>ถามขั้นตอนการอนุมัติวงเงินแล้วจดไว้ว่าระบบออกแบบมาแบบไหน</td></tr>
              <tr><td class="pc">ทดสอบการควบคุม</td><td><b>ระบบทำงานจริงไหม</b></td><td>หยิบใบเปิดบัญชีลูกค้าใหม่มาดูว่ามีลายเซ็นอนุมัติครบไหม</td></tr>
              <tr><td class="pc">ตรวจเนื้อหาสาระ</td><td><b>ตัวเลขถูกไหม</b></td><td>ยืนยันยอดลูกหนี้ · แตกเป็นทดสอบรายละเอียด กับวิธีวิเคราะห์เปรียบเทียบ</td></tr>
            </tbody>
          </table>
        </div>
        <div class="sm-rule"><span class="k">คู่ที่สับสนที่สุด ต่างกันแค่ทิศทาง</span><b>Vouching</b> เริ่มจากบัญชี ย้อนไปหาเอกสาร ถามว่า<b>ที่จดไว้เกิดจริงไหม</b> → จับ<b>ของเกิน</b>ในบัญชี → ทดสอบ occurrence · <b>Tracing</b> เริ่มจากเอกสาร ตามเข้าไปในบัญชี ถามว่า<b>ที่เกิดจริงจดครบไหม</b> → จับ<b>ของขาด</b>จากบัญชี → ทดสอบ completeness · <b>ทำอย่างเดียวไม่มีวันครบ</b></div>
        <div class="sm-rule"><span class="k">วิธีวิเคราะห์เปรียบเทียบ</span>หัวใจคือ<b>สร้างความคาดหวังก่อน แล้วค่อยดูตัวเลขจริง</b> ถ้าทำกลับลำดับ เราจะหาเหตุผลมาอธิบายได้เสมอ ซึ่งไม่ใช่การตรวจสอบ · <b>บังคับสองจุด คือตอนวางแผนกับตอนสอบทานภาพรวมตอนจบงาน</b> ส่วนตอนทดสอบเนื้อหาสาระใช้ได้แต่ไม่บังคับ · แบบที่ทรงพลังที่สุดคือ<b>เทียบกับข้อมูลที่ไม่ใช่ตัวเงิน</b> เพราะอยู่นอกระบบที่คนจะไปปั้นตัวเลข</div>
      </div>
    </section>

    <section class="sec" id="sm-9">
      <div class="sec-h"><span class="sec-n">9</span><h2>เอกสารหลักฐาน</h2></div>
      <div class="body">
        <div class="sm-rule"><span class="k">เกณฑ์ความละเอียด</span>ต้องละเอียดพอที่<b>ผู้สอบบัญชีที่มีประสบการณ์ซึ่งไม่เคยยุ่งกับงานนี้มาก่อน</b> อ่านแล้วเข้าใจได้ว่า<b>ทำอะไร ทำเมื่อไร ผลเป็นอย่างไร ใครทำ ใครสอบทาน วันไหน</b> · เขียนว่า ตรวจแล้วไม่พบข้อผิดพลาด เฉย ๆ <b>ใช้ไม่ได้</b></div>
        <div class="tw">
          <table class="tbl">
            <thead><tr><th>ประเภทกิจการ</th><th>เก็บนานเท่าไร</th><th>ปิดแฟ้มภายใน</th></tr></thead>
            <tbody>
              <tr><td>กิจการทั่วไป</td><td class="pc">5 ปี</td><td class="pc">60 วัน</td></tr>
              <tr><td>บริษัทมหาชน</td><td class="pc">7 ปี</td><td class="pc">14 วัน</td></tr>
            </tbody>
          </table>
        </div>
        <div class="sm-rule"><span class="k">สองจุดที่มักถาม</span>ตัวเลข <b>14 วัน</b> เป็นของใหม่ ของเดิมคือ 45 วัน ถ้าเจอหนังสือเก่าเขียน 45 ให้ยึดตัวเลขใหม่ · หลังวันปิดแฟ้ม <b>เพิ่มได้แต่ต้องระบุว่าใครเพิ่ม เมื่อไร เพราะอะไร</b> ส่วนการ<b>ลบของเดิมห้าม</b>จนกว่าจะพ้นระยะเวลาเก็บรักษา</div>
      </div>
    </section>

    <section class="sec" id="sm-10">
      <div class="sec-h"><span class="sec-n">10</span><h2>สี่ประเภทงานและระดับความเชื่อมั่น</h2></div>
      <div class="body">
        <div class="tw">
          <table class="tbl">
            <thead><tr><th>งาน</th><th>ความเชื่อมั่น</th><th>ผลลัพธ์</th><th>ต้องเป็นอิสระ</th></tr></thead>
            <tbody>
              <tr><td class="pc">ตรวจสอบ</td><td>อย่างสมเหตุสมผล · ระดับสูง</td><td><b>ความเห็น</b> เขียนในรูปบวก บอกตรง ๆ ว่างบถูกต้อง</td><td>ใช่</td></tr>
              <tr><td class="pc">สอบทาน</td><td>อย่างจำกัด</td><td><b>ข้อสรุป</b> เขียนในรูปลบ ว่าไม่พบสิ่งที่ทำให้เชื่อว่าไม่ถูกต้อง</td><td>ใช่</td></tr>
              <tr><td class="pc">วิธีที่ตกลงร่วมกัน</td><td><b>ไม่ให้เลย</b></td><td>สิ่งที่พบตามข้อเท็จจริง <b>ห้ามตีความ ห้ามสรุป</b> ผู้อ่านสรุปเอง</td><td><b>ใช่</b></td></tr>
              <tr><td class="pc">รวบรวมข้อมูล</td><td><b>ไม่ให้เลย</b></td><td>จัดรูปข้อมูลที่ผู้บริหารให้มา</td><td><b>ไม่</b></td></tr>
            </tbody>
          </table>
        </div>
        <div class="sm-rule"><span class="k">จุดที่ตอบผิดมากที่สุดของหัวข้อนี้</span>ความเป็นอิสระ<b>กับ</b>การให้ความเชื่อมั่น เป็น<b>คนละเรื่องกัน</b> · <b>วิธีที่ตกลงร่วมกัน ไม่ให้ความเชื่อมั่น แต่ต้องเป็นอิสระ</b> · <b>การรวบรวมข้อมูล ไม่ให้ความเชื่อมั่น และไม่ต้องเป็นอิสระ</b> แต่<b>ยังต้องมีจรรยาบรรณครบทุกข้ออื่น</b></div>
        <div class="sm-rule"><span class="k">ฟังจากรูปประโยคก็รู้ระดับ</span>ประโยค<b>บอกเล่าตรง ๆ</b> ว่างบถูกต้อง คือความเชื่อมั่นอย่างสมเหตุสมผล · ประโยค<b>ปฏิเสธซ้อน</b> ว่าไม่พบสิ่งที่ทำให้เชื่อว่าไม่ถูกต้อง คือความเชื่อมั่นอย่างจำกัด · ภาษาที่อ้อมกว่าสะท้อนความเชื่อมั่นที่ต่ำกว่าโดยตรง</div>
        <div class="sm-rule"><span class="k">งานสอบทานไม่มีอะไร</span>ไม่มี<b>การยืนยันยอดลูกหนี้</b> และไม่มี<b>การตรวจนับสินค้าคงเหลือ</b> เพราะสองอย่างนั้นเป็นวิธีตรวจเนื้อหาสาระของงานตรวจสอบ · ข้อสอบชอบเอามาใส่แล้วถามว่าข้อใดไม่ใช่</div>
      </div>
    </section>

    <section class="sec" id="sm-11">
      <div class="sec-h"><span class="sec-n">11</span><h2>จรรยาบรรณ</h2></div>
      <div class="body">
        <p>รูปแบบข้อสอบคือ<b>ให้สถานการณ์มาแล้วถามว่าเป็นภัยคุกคามประเภทใด</b> คอลัมน์ขวาคือคำใบ้ที่มักโผล่ในโจทย์</p>
        <div class="tw">
          <table class="tbl">
            <thead><tr><th>ภัยคุกคาม</th><th>คืออะไร</th><th>คำใบ้ในโจทย์</th></tr></thead>
            <tbody>
              <tr><td class="asb">ผลประโยชน์ส่วนตน</td><td>มีความสัมพันธ์ทางการเงินกับลูกค้า</td><td>ถือหุ้น · เงินกู้ · ลงทุนร่วม · <b>ตัดราคาค่าธรรมเนียมจนทำงานตามมาตรฐานไม่ได้</b></td></tr>
              <tr><td class="asb">สอบทานงานตนเอง</td><td>ตรวจงานที่ตัวเองเป็นคนทำ</td><td>เคยทำบัญชีให้ · เคยออกแบบระบบให้ · เคยประเมินมูลค่าให้</td></tr>
              <tr><td class="asb">เป็นผู้สนับสนุน</td><td>ไปยืนข้างลูกค้า แต่<b>ยังไม่ตัดสินใจแทน</b></td><td>ช่วยโปรโมตหุ้น · เป็นปากเสียงในการเจรจา · ล็อบบี้แทน</td></tr>
              <tr><td class="asb">ร่วมบริหาร</td><td><b>เข้าไปตัดสินใจแทน</b>ลูกค้า</td><td>อนุมัติรายการ · คัดเลือกพนักงาน · ทำหน้าที่บริหาร</td></tr>
              <tr><td class="asb">ความคุ้นเคย</td><td>เห็นใจลูกค้ามากเกินไปจากความสัมพันธ์</td><td>ตรวจมานาน · ญาติทำงานที่ลูกค้า → แก้ด้วย<b>การหมุนเวียน</b></td></tr>
              <tr><td class="asb">ถูกข่มขู่</td><td>ถูกกดดันจากภายนอกพร้อมผลเสียถ้าไม่ทำตาม</td><td>ขู่เปลี่ยนผู้สอบบัญชี · ขู่ไม่จ่ายค่าธรรมเนียม · ขู่ฟ้อง</td></tr>
              <tr><td class="asb">ผลประโยชน์ขัดแย้ง</td><td>อยู่ในฐานะเป็นปฏิปักษ์กับลูกค้า</td><td>ฟ้องร้องกัน · ข้อพิพาท · เรียกค่าเสียหาย</td></tr>
            </tbody>
          </table>
        </div>
        <div class="sm-rule"><span class="k">กฎส่วนได้เสียทางการเงิน · ออกสอบบ่อยที่สุด</span><b>โดยตรง ห้ามทุกจำนวน</b> ถือหุ้นเดียวก็ขาดความเป็นอิสระ ไม่มีข้อยกเว้นเรื่องมูลค่า · <b>โดยอ้อม ห้ามเฉพาะเมื่อมีสาระสำคัญ</b> เช่นถือหน่วยลงทุนของกองทุนที่บังเอิญมีหุ้นลูกค้าอยู่นิดเดียว · <b>คำว่ามีสาระสำคัญปรากฏหรือไม่ในโจทย์ คือกุญแจของข้อสอบประเภทนี้</b></div>
        <div class="sm-rule"><span class="k">สองจุดที่มักตอบผิด</span><b>ความเป็นอิสระไม่ใช่หลักการพื้นฐาน</b> แต่เป็นข้อกำหนดแยกต่างหากที่ใช้กับงานให้ความเชื่อมั่น · <b>หน้าที่รักษาความลับไม่สิ้นสุด</b> แม้ความสัมพันธ์จบไปแล้ว และ<b>แม้ข้อมูลจะกลายเป็นข่าวสาธารณะไปแล้ว</b></div>
        <div class="sm-rule"><span class="k">เครื่องมือตัดสิน</span>ถามตัวเองว่า <b>บุคคลอื่นที่สมเหตุสมผลซึ่งรู้ข้อเท็จจริงทั้งหมด จะได้ข้อสรุปเดียวกับเราไหม</b> · เป็นการทดสอบทางความคิด ไม่ใช่การเรียกคนจริงมาตรวจ และคือเวอร์ชันที่ใช้จริงได้ของความเป็นอิสระในสายตาคนนอก</div>
      </div>
    </section>

    <section class="sec" id="sm-12">
      <div class="sec-h"><span class="sec-n">12</span><h2>การเลือกตัวอย่าง</h2></div>
      <div class="body">
        <div class="sm-rule"><span class="k">ท่องสองบรรทัดนี้พอ</span><b>Attribute = ใช่หรือไม่ใช่</b> ประมาณ<b>อัตราการเบี่ยงเบน</b> คู่กับ<b>การทดสอบการควบคุม</b> · <b>Variable = เท่าไร</b> ประมาณ<b>จำนวนเงิน</b> คู่กับ<b>การตรวจเนื้อหาสาระ</b></div>
        <div class="tw">
          <table class="tbl">
            <thead><tr><th>ความเสี่ยง</th><th>เกิดเมื่อ</th><th>ผลที่ตามมา</th><th>ตกกับใคร</th></tr></thead>
            <tbody>
              <tr><td class="asb">เชื่อถือมากเกินไป</td><td>ตัวอย่างบอกว่าการควบคุมได้ผล แต่จริง ๆ ไม่ได้ผล</td><td>ตรวจน้อยเกินไป <b>เสียประสิทธิผล</b> อาจออกความเห็นผิด</td><td><b>ผู้ลงทุน ซึ่งไม่มีทางรู้ตัว</b></td></tr>
              <tr><td class="asb">เชื่อถือน้อยเกินไป</td><td>ตัวอย่างบอกว่าไม่ได้ผล แต่จริง ๆ ได้ผล</td><td>ตรวจมากเกินไป <b>เสียประสิทธิภาพ</b> แต่ความเห็นยังถูก</td><td>เราเอง</td></tr>
            </tbody>
          </table>
        </div>
        <div class="sm-rule"><span class="k">อันไหนร้ายแรงกว่า</span><b>เชื่อถือมากเกินไป</b> เพราะในงานสอบบัญชี<b>ประสิทธิผลสำคัญกว่าประสิทธิภาพ</b> · จำที่คำต้น <b>over</b> คือเชื่อมากไป จึงตรวจน้อยไป</div>
        <div class="sm-rule"><span class="k">วิธีเลือกที่ใช้กับสถิติได้</span>มีสองวิธี คือ<b>สุ่มแบบไม่จำกัด</b>กับ<b>สุ่มอย่างเป็นระบบ</b> · ส่วน<b>เลือกเป็นกลุ่มก้อน</b>กับ<b>หยิบแบบไร้ระบบ</b>ใช้ไม่ได้ · <b>haphazard ไม่เท่ากับ random</b> เพราะยังมีอคติของผู้หยิบแฝงอยู่ คนเรามักหยิบแฟ้มด้านหน้าหรือเล่มที่หนาสะดุดตา</div>
        <div class="sm-rule"><span class="k">อย่าดูแค่จำนวน</span>การเบี่ยงเบน<b>หนึ่งรายการที่มีเจตนา ร้ายแรงกว่าสิบรายการที่เกิดจากความเข้าใจผิด</b> เพราะเจตนาบ่งชี้ถึงการทุจริต · และ<b>ประชากรต้องครอบคลุมทั้งงวด</b> การสุ่มเฉพาะเดือนที่เอกสารพร้อม มักเป็นการตัดเดือนที่เสี่ยงที่สุดออกไปพอดี</div>
      </div>
    </section>

    <section class="sec" id="sm-13">
      <div class="sec-h"><span class="sec-n">13</span><h2>กับดัก 24 ข้อที่เสียคะแนนบ่อยที่สุด</h2></div>
      <div class="body">
        <p class="lede">ตารางนี้คือส่วนที่มีค่าที่สุดของชีท · ลองปิดคอลัมน์ขวาแล้วตอบเองก่อน</p>
        <div class="tw">
          <table class="tbl">
            <thead><tr><th>โจทย์ถามว่า</th><th>คนมักตอบผิดว่า</th><th>คำตอบที่ถูก</th></tr></thead>
            <tbody>
              <tr><td>ผู้สอบบัญชีลดความเสี่ยงตัวไหน</td><td class="q">ความเสี่ยงทางธุรกิจ</td><td><b>ความเสี่ยงของข้อมูล</b></td></tr>
              <tr><td>ตามรอยจากเอกสารเข้าบัญชี ทดสอบอะไร</td><td class="q">occurrence</td><td><b>completeness</b></td></tr>
              <tr><td>บันทึกผิดงวด ผิดข้อกำหนดใด</td><td class="q">occurrence</td><td><b>cutoff</b></td></tr>
              <tr><td>ขายลูกหนี้ไปแล้วแต่ยังแสดงในงบ</td><td class="q">existence</td><td><b>rights and obligations</b></td></tr>
              <tr><td>ซื้อสินทรัพย์แต่ลงเป็นค่าใช้จ่าย</td><td class="q">accuracy</td><td><b>classification</b></td></tr>
              <tr><td>ความมีสาระสำคัญอ้างอิงถึงใคร</td><td class="q">ผู้บริหาร หรือทีมสอบบัญชี</td><td><b>ผู้ใช้งบการเงิน</b></td></tr>
              <tr><td>บัญชีเสี่ยงสูง ตั้งเกณฑ์อย่างไร</td><td class="q">สูงขึ้น</td><td><b>ต่ำลง เพื่อให้ตรวจมากขึ้น</b></td></tr>
              <tr><td>RMM ประกอบด้วยอะไร</td><td class="q">ใส่ DR เข้าไปด้วย</td><td><b>IR × CR เท่านั้น</b></td></tr>
              <tr><td>ความเสี่ยงฝั่งลูกค้าสูงขึ้น DR เป็นอย่างไร</td><td class="q">สูงขึ้นตาม</td><td><b>ต่ำลง งานหนักขึ้น</b></td></tr>
              <tr><td>ตัวไหนที่ผู้สอบบัญชีควบคุมได้</td><td class="q">ความเสี่ยงจากการควบคุม</td><td><b>ความเสี่ยงที่จะตรวจไม่เจอ</b></td></tr>
              <tr><td>ตรวจไม่เจอเพราะใช้วิธีผิด เป็นความเสี่ยงแบบใด</td><td class="q">จากการสุ่ม</td><td><b>ไม่ได้เกิดจากการสุ่ม · เพิ่มตัวอย่างไม่ช่วย</b></td></tr>
              <tr><td>เหตุผลที่ต้องการข้อมูลเชื่อถือได้มากขึ้น</td><td class="q">ต้นทุนการจัดทำงบสูงขึ้น</td><td><b>ไม่ใช่ข้อนี้</b> · ที่ถูกคือซับซ้อนขึ้น ผู้ใช้อยู่ไกล ต้องการเร็วขึ้น ผลกระทบกว้าง</td></tr>
              <tr><td>ถามผู้บริหารแล้วได้คำตอบที่ฟังขึ้น พอไหม</td><td class="q">พอ ถ้าผู้บริหารน่าเชื่อถือ</td><td><b>ไม่พอ ต้องมีหลักฐานพิสูจน์เสมอ</b></td></tr>
              <tr><td>ลูกค้าอาสาเอาแบบยืนยันยอดไปให้ธนาคารเซ็น</td><td class="q">ใช้ได้ เพราะต้นทางเป็นธนาคาร</td><td><b>ตกชั้นเป็นเอกสารภายในทันที</b></td></tr>
              <tr><td>ใครติดต่อผู้สอบบัญชีคนเดิม</td><td class="q">คนเดิมติดต่อมาหาคนใหม่</td><td><b>คนใหม่เป็นฝ่ายพยายามติดต่อ หลังขออนุญาตลูกค้า</b></td></tr>
              <tr><td>ต้องถามคนเดิมเรื่องอะไร</td><td class="q">ค่าธรรมเนียมที่เคยเก็บ</td><td><b>ไม่ใช่ข้อนี้</b> · ที่ถูกคือความซื่อสัตย์ ข้อขัดแย้ง และเหตุที่เปลี่ยน</td></tr>
              <tr><td>ใครรับผิดชอบจัดทำงบการเงิน</td><td class="q">ผู้สอบบัญชี</td><td><b>ผู้บริหาร</b></td></tr>
              <tr><td>วิธีวิเคราะห์เปรียบเทียบบังคับตอนไหน</td><td class="q">ตอนทดสอบเนื้อหาสาระ</td><td><b>ตอนวางแผน และตอนสอบทานภาพรวมตอนจบงาน</b></td></tr>
              <tr><td>ผู้บริหารเบิกเท็จหกพันบาท มีสาระสำคัญไหม</td><td class="q">ไม่มี เพราะเงินน้อย</td><td><b>มีเสมอ เพราะกระทบความน่าเชื่อถือของคำกล่าวอ้างทั้งหมด</b></td></tr>
              <tr><td>งานวิธีที่ตกลงร่วมกัน ต้องเป็นอิสระไหม</td><td class="q">ไม่ต้อง เพราะไม่ให้ความเชื่อมั่น</td><td><b>ต้องเป็นอิสระ</b></td></tr>
              <tr><td>งานรวบรวมข้อมูลไม่ต้องเป็นอิสระ แปลว่าไม่ต้องมีจรรยาบรรณ</td><td class="q">ใช่</td><td><b>ไม่ใช่ ยังต้องครบทุกข้ออื่น</b></td></tr>
              <tr><td>ข้อใดไม่ใช่หลักการพื้นฐานทางจรรยาบรรณ</td><td class="q">การรักษาความลับ</td><td><b>ความเป็นอิสระ</b> ซึ่งแยกเป็นข้อกำหนดต่างหาก</td></tr>
              <tr><td>ถือหุ้นลูกค้าโดยตรงจำนวนน้อยมาก</td><td class="q">ยังเป็นอิสระ เพราะไม่มีสาระสำคัญ</td><td><b>ขาดความเป็นอิสระ · โดยตรงห้ามทุกจำนวน</b></td></tr>
              <tr><td>overreliance กับ underreliance อันไหนร้ายแรงกว่า</td><td class="q">underreliance เพราะเสียเงินเสียเวลา</td><td><b>overreliance เพราะอาจออกความเห็นผิด</b></td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <section class="sec" id="sm-14">
      <div class="sec-h"><span class="sec-n">14</span><h2>คู่คำที่สับสน</h2></div>
      <div class="body">
        <div class="tw">
          <table class="tbl">
            <thead><tr><th>คู่คำ</th><th>ตัวแรก</th><th>ตัวที่สอง</th><th>เส้นแบ่ง</th></tr></thead>
            <tbody>
              <tr><td class="asb">business ↔ information risk</td><td>ธุรกิจทำไม่ได้ตามเป้า</td><td>ตัวเลขที่ประกาศไม่ถูกต้อง</td><td>เราลดตัวหลัง แต่ตัวแรกดันตัวหลังให้สูงขึ้น</td></tr>
              <tr><td class="asb">vouching ↔ tracing</td><td>บัญชี → เอกสาร · occurrence</td><td>เอกสาร → บัญชี · completeness</td><td><b>ทิศทาง</b></td></tr>
              <tr><td class="asb">sufficient ↔ appropriate</td><td>ปริมาณ</td><td>คุณภาพ</td><td>มากพอไหม เทียบกับ ดีพอไหม</td></tr>
              <tr><td class="asb">relevance ↔ reliability</td><td>ตอบตรงข้อกำหนดไหม</td><td>มาจากแหล่งไหน</td><td>ทั้งคู่อยู่ใต้คำว่าเหมาะสม</td></tr>
              <tr><td class="asb">in fact ↔ in appearance</td><td>สภาพจิตใจ มองไม่เห็น</td><td>ภาพที่คนนอกเห็น</td><td>ต้องมีครบทั้งคู่</td></tr>
              <tr><td class="asb">self-interest ↔ self-review</td><td>เรื่องเงิน</td><td>ตรวจงานตัวเอง</td><td>ขึ้นต้นเหมือนกันแต่คนละเรื่อง</td></tr>
              <tr><td class="asb">advocacy ↔ management participation</td><td>ยืนข้างลูกค้า</td><td>ตัดสินใจแทนลูกค้า</td><td>ยังไม่ตัดสินใจ เทียบกับ ตัดสินใจแล้ว</td></tr>
              <tr><td class="asb">embezzlement ↔ larceny</td><td>ยักยอกของที่ตนดูแล</td><td>ลักทรัพย์ที่ไม่ได้ดูแล</td><td><b>ได้รับมอบหมายให้ดูแลหรือไม่</b></td></tr>
              <tr><td class="asb">error ↔ fraud</td><td>ไม่ตั้งใจ กระจายสองทิศทาง</td><td>ตั้งใจ เอียงทางเดียว</td><td><b>เจตนา</b></td></tr>
              <tr><td class="asb">attributes ↔ variables</td><td>ใช่หรือไม่ใช่ · คู่กับทดสอบการควบคุม</td><td>เท่าไร · คู่กับตรวจเนื้อหาสาระ</td><td>สิ่งที่ต้องการประมาณ</td></tr>
              <tr><td class="asb">haphazard ↔ random</td><td>หยิบมั่ว ยังมีอคติแฝง</td><td>ทุกหน่วยมีโอกาสเท่ากัน</td><td>คำนวณความน่าจะเป็นได้หรือไม่</td></tr>
              <tr><td class="asb">reasonable ↔ limited assurance</td><td>ประโยคบอกเล่า · ความเห็น</td><td>ประโยคปฏิเสธซ้อน · ข้อสรุป</td><td>ฟังจากรูปประโยค</td></tr>
              <tr><td class="asb">direct ↔ indirect effect</td><td>ผูกกับบัญชีตรง ๆ เช่นภาษี <b>ต้องออกแบบวิธีไปหา</b></td><td>กระทบผ่านขั้นกลาง เช่นกฎสิ่งแวดล้อม <b>แค่ติดตามเมื่อสงสัย</b></td><td>ผูกกับตัวเลขในงบได้ตรงหรือไม่</td></tr>
            </tbody>
          </table>
        </div>
        <div class="note src" style="margin-top:18px"><span class="nh">ชีทนี้ไม่ใช่ตัวแทนของบทเรียน</span>ทุกบรรทัดในหน้านี้ตัดเหตุผลออกไปหมดแล้วเหลือแต่ข้อสรุป · ถ้าตรงไหนอ่านแล้วรู้สึกว่า<b>จำได้แต่ไม่เข้าใจว่าทำไม</b> ให้กลับไปที่แท็บของบทนั้น เพราะข้อสอบที่ให้สถานการณ์มาแล้วถามว่าจะทำอย่างไร ตอบด้วยการท่องไม่ได้</div>
      </div>
    </section>
  </div>

'''
SECTION_ANCHOR = u'  <div id="quiz" class="hidden" role="tabpanel"'


def apply(html):
    steps = [
        (u'ปุ่มแท็บ', TAB_ANCHOR, TAB, 'before'),
        (u'สารบัญข้าง', RAIL_ANCHOR, RAIL, 'before'),
        (u'เนื้อหาแท็บ', SECTION_ANCHOR, SECTION, 'before'),
        (u'สไตล์', CSS_ANCHOR, CSS, 'before'),
    ]
    for label, anchor, payload, _ in steps:
        if payload.strip() in html:
            print(u'  %s มีอยู่แล้ว ข้าม' % label)
            continue
        at = html.find(anchor)
        if at < 0:
            raise SystemExit(u'หาจุดวาง %s ไม่เจอ' % label)
        html = html[:at] + payload + html[at:]
        print(u'  วาง%sแล้ว · %d ตัวอักษร' % (label, len(payload)))

    # ผูกแท็บใหม่เข้ากับสารบัญข้าง มิฉะนั้นกดแล้วสารบัญเดิมจะค้างอยู่
    old = u"var rails = {ch1:'rail-ch1'"
    if u"sm:'rail-sm'" not in html:
        html = html.replace(old + u", ch2:", u"var rails = {ch1:'rail-ch1', sm:'rail-sm', ch2:")
        print(u'  ผูกแท็บเข้ากับสารบัญข้างแล้ว')

    # ปุ่มพิมพ์ชีท
    hook = u"    document.getElementById('qz-print')"
    if u"'sm-print'" not in html:
        add = (u"    var smPrint = document.getElementById('sm-print');\n"
               u"    if (smPrint) smPrint.addEventListener('click', function(){ window.print(); });\n")
        at = html.find(hook)
        if at < 0:
            raise SystemExit(u'หาจุดวางปุ่มพิมพ์ไม่เจอ')
        html = html[:at] + add + html[at:]
        print(u'  ต่อปุ่มพิมพ์ชีทแล้ว')
    return html


def main():
    ap = argparse.ArgumentParser(description=u'วางแท็บสรุปรวบยอดลงหน้าวิชาการสอบบัญชี')
    ap.add_argument('--check', action='store_true', help=u'ดูผลอย่างเดียว ไม่เขียนไฟล์')
    a = ap.parse_args()

    html = io.open(PAGE, encoding='utf-8').read()
    before = len(html)
    html = apply(html)
    print(u'\nหน้าเว็บ %d → %d ตัวอักษร' % (before, len(html)))

    # ตรวจว่าทุก id ที่สารบัญชี้ไป มีอยู่จริงในเนื้อหา
    bad = 0
    for ref in re.findall(r'href="#(sm-\d+)"', RAIL):
        if ('id="%s"' % ref) not in html:
            print(u'สารบัญชี้ไปยัง %s ซึ่งไม่มีในเนื้อหา' % ref)
            bad += 1
    print(u'ตรวจลิงก์สารบัญ %d รายการ · พบปัญหา %d จุด'
          % (len(re.findall(r'href="#(sm-\d+)"', RAIL)), bad))
    if bad:
        return 1

    if not a.check:
        io.open(PAGE, 'w', encoding='utf-8').write(html)
        print(u'เขียน audit/index.html แล้ว')
    return 0


if __name__ == '__main__':
    sys.exit(main())
