# -*- coding: utf-8 -*-
u"""เนื้อหาหลังมิดเทอมของวิชาหลักการตลาด · ใช้คู่กับ tools/mk-postmid.py

หนึ่งบท ยกมาจากเอกสารประกอบการสอน Chp 08 PRIN MKGT NPD PLC V2 cut 2569
  m8  การพัฒนาสินค้าใหม่และการบริหารวงจรชีวิตผลิตภัณฑ์
      Kotler & Armstrong, Principles of Marketing บทที่ 8 (เลขภาพในสไลด์เป็น 9.x)

โครงของบทตามสไลด์
  หน้า  5-6   สองทางที่จะได้สินค้าใหม่ และสาเหตุที่สินค้าใหม่ล้มเหลว
  หน้า  7-24  กระบวนการพัฒนาสินค้าใหม่แปดขั้น
  หน้า 25-28  การบริหารกระบวนการพัฒนาสินค้าใหม่สามแบบ
  หน้า 29-47  วงจรชีวิตผลิตภัณฑ์และกลยุทธ์ในแต่ละขั้น รวมตาราง 9.2
  หน้า 48-49  ความรับผิดชอบต่อสังคม และการตลาดระหว่างประเทศ

ภาพโฆษณาของแบรนด์ในสไลด์หน้า 40 43 44 ไม่ได้ฝังลงในหน้านี้
เพราะเป็นงานโฆษณาของบุคคลที่สามและมีภาพพรีเซนเตอร์อยู่ด้วย
หน้านี้เล่าใจความเป็นภาษาไทยขึ้นใหม่พร้อมระบุที่มาแทน
ส่วนภาพสามภาพที่ฝังไว้เป็นแผนภาพจากตำราซึ่งเป็นแกนของบท
"""

from mk8_figs import F1, F2, F3


# ───────────────────────────── แถบข้าง ─────────────────────────────

RAILS = u"""    <nav id="rail-m8" class="hidden" aria-label="หัวข้อบทที่ 8">
      <div class="rail-h">บทที่ 8 · สินค้าใหม่และวงจรชีวิต</div>
      <ol>
        <li><a href="#m8-1"><i>1</i>สองทางที่จะได้สินค้าใหม่</a></li>
        <li><a href="#m8-2"><i>2</i>ทำไมสินค้าใหม่ถึงล้มเหลว</a></li>
        <li><a href="#m8-3"><i>3</i>แปดขั้นของการพัฒนา</a></li>
        <li><a href="#m8-4"><i>4</i>ขั้น 1 สร้างความคิด</a></li>
        <li><a href="#m8-5"><i>5</i>ขั้น 2 กลั่นกรองความคิด</a></li>
        <li><a href="#m8-6"><i>6</i>ขั้น 3 แนวคิดสินค้า</a></li>
        <li><a href="#m8-7"><i>7</i>ขั้น 4 กลยุทธ์การตลาด</a></li>
        <li><a href="#m8-8"><i>8</i>ขั้น 5 วิเคราะห์ธุรกิจ</a></li>
        <li><a href="#m8-9"><i>9</i>ขั้น 6 พัฒนาสินค้า</a></li>
        <li><a href="#m8-10"><i>10</i>ขั้น 7 ทดสอบตลาด</a></li>
        <li><a href="#m8-11"><i>11</i>ขั้น 8 ออกสู่ตลาดจริง</a></li>
        <li><a href="#m8-12"><i>12</i>บริหารกระบวนการสามแบบ</a></li>
        <li><a href="#m8-13"><i>13</i>วงจรชีวิตผลิตภัณฑ์</a></li>
        <li><a href="#m8-14"><i>14</i>ใช้ PLC กับอะไรได้บ้าง</a></li>
        <li><a href="#m8-15"><i>15</i>สไตล์ แฟชัน แฟด</a></li>
        <li><a href="#m8-16"><i>16</i>ขั้นแนะนำและขั้นเติบโต</a></li>
        <li><a href="#m8-17"><i>17</i>ขั้นเติบโตเต็มที่</a></li>
        <li><a href="#m8-18"><i>18</i>ตัวอย่างการปรับในตลาดไทย</a></li>
        <li><a href="#m8-19"><i>19</i>ขั้นถดถอย</a></li>
        <li><a href="#m8-20"><i>20</i>ตาราง 9.2 สรุปทั้งวงจร</a></li>
        <li><a href="#m8-21"><i>21</i>สองประเด็นเพิ่มเติม</a></li>
      </ol>
    </nav>
"""


CHAPTERS = [
    ('m8', u'การพัฒนาสินค้าใหม่และวงจรชีวิตผลิตภัณฑ์', list(range(21))),
]


# ───────────────────────── แผงเนื้อหาบทที่ 8 ─────────────────────────

PANEL = u"""  <div id="m8" class="hidden" role="tabpanel" aria-labelledby="t-m8">
    <p class="lede">บทนี้ตอบคำถามที่ต่อจากบทที่ 7 โดยตรง — บทที่ 7 บอกว่า<b>สินค้าคืออะไรและตัดสินใจอะไรกับมันบ้าง</b> บทนี้ถามว่า<b>สินค้านั้นเกิดขึ้นมาได้อย่างไร</b> และ<b>เมื่อเกิดแล้วจะต้องเปลี่ยนกลยุทธ์ตามไปอย่างไรตลอดอายุของมัน</b> · ครึ่งแรกคือ<b>กระบวนการพัฒนาสินค้าใหม่แปดขั้น</b> ครึ่งหลังคือ<b>วงจรชีวิตผลิตภัณฑ์</b> และข้อสอบมักให้สถานการณ์มาแล้วถามว่าอยู่ขั้นไหนและควรทำอะไร</p>

    <div class="note">
      <span class="nh">วัตถุประสงค์การเรียนรู้ของบทที่ 8</span>
      <b>8.1</b> อธิบายว่าบริษัทหาและพัฒนาความคิดเรื่องสินค้าใหม่ได้อย่างไร<br>
      <b>8.2</b> ระบุและนิยามขั้นตอนในกระบวนการพัฒนาสินค้าใหม่ และข้อพิจารณาสำคัญในการบริหารกระบวนการนี้<br>
      <b>8.3</b> อธิบายขั้นต่าง ๆ ของวงจรชีวิตผลิตภัณฑ์ และกลยุทธ์การตลาดที่เปลี่ยนไปในแต่ละขั้น<br>
      <b>8.4</b> อภิปรายสองประเด็นเพิ่มเติม คือการตัดสินใจเรื่องสินค้าอย่างรับผิดชอบต่อสังคม และการตลาดสินค้าและบริการระหว่างประเทศ
    </div>

    <section class="sec" id="m8-1">
      <div class="sec-h"><span class="sec-n">1</span><h2>สองทางที่จะได้สินค้าใหม่มา</h2></div>
      <div class="body">
        <p class="lede">บริษัทได้สินค้าใหม่มาได้สองทางเท่านั้น และสองทางนี้<b>ต่างกันที่ว่าสินค้าเกิดจากข้างในบริษัทหรือซื้อมาจากข้างนอก</b></p>
        <div class="grid g2">
          <div class="card">
            <span class="cn">ทางที่ 1</span>
            <div class="ct">การซื้อกิจการ <span class="en">Acquisition</span></div>
            <div class="cs">การ<b>ซื้อทั้งบริษัท ซื้อสิทธิบัตร หรือซื้อใบอนุญาต</b>เพื่อผลิตสินค้าของคนอื่น · สินค้าไม่ได้เกิดจากการวิจัยและพัฒนาของบริษัทเอง แต่<b>ได้กรรมสิทธิ์หรือสิทธิในการผลิตมา</b></div>
          </div>
          <div class="card">
            <span class="cn">ทางที่ 2</span>
            <div class="ct">การพัฒนาสินค้าใหม่ <span class="en">New product development</span></div>
            <div class="cs">การพัฒนา<b>สินค้าต้นฉบับ (original products) · การปรับปรุงสินค้า (product improvements) · การดัดแปลงสินค้า (product modifications)</b> และ<b>ตราสินค้าใหม่</b> ที่เกิดจาก<b>ความพยายามพัฒนาสินค้าหรืองานวิจัยและพัฒนาของบริษัทเอง</b></div>
          </div>
        </div>
        <div class="note key">
          <span class="nh">เส้นแบ่งที่ข้อสอบชอบถาม</span>
          คำว่า <b>สินค้าใหม่</b> ในบทนี้หมายถึงเฉพาะทางที่ 2 เท่านั้น · ถ้าโจทย์บอกว่าบริษัทไป<b>ซื้อแบรนด์หนึ่งมา</b>หรือ<b>ซื้อใบอนุญาตมาผลิต</b> นั่นคือ <b>acquisition</b> ไม่ใช่ new product development · และ<b>สี่อย่างที่นับเป็น NPD</b>คือ ของใหม่แท้ · ของเดิมที่ปรับปรุง · ของเดิมที่ดัดแปลง · ตราใหม่
        </div>
        <p>ทั้งบทนี้ตั้งแต่หัวข้อถัดไปเป็นต้นไปพูดถึงทางที่ 2 ล้วน ๆ เพราะทางที่ 1 เป็นเรื่องของการเงินและกฎหมายมากกว่าการตลาด</p>
      </div>
    </section>

    <section class="sec" id="m8-2">
      <div class="sec-h"><span class="sec-n">2</span><h2>ทำไมสินค้าใหม่ถึงล้มเหลว</h2></div>
      <div class="body">
        <p class="lede">สินค้าใหม่ส่วนใหญ่ล้มเหลว และ<b>ความล้มเหลวทุกครั้งคือเงินและความหวังที่สูญไป</b> <span class="en">each product failure represents squandered dollars and hopes</span> · ตำราให้ห้าสาเหตุหลัก และทั้งห้าข้อเป็นเหตุผลว่าทำไมจึงต้องมีกระบวนการแปดขั้นในหัวข้อถัดไป</p>
        <div class="grid g3">
          <div class="card">
            <span class="cn">สาเหตุที่ 1</span>
            <div class="ct">ประเมินขนาดตลาดสูงเกินจริง</div>
            <div class="cs"><span class="en">Overestimation of market size</span><br>คิดว่ามีคนอยากได้มากกว่าความเป็นจริง · เป็นข้อที่<b>ขั้นวิเคราะห์ทางธุรกิจ</b>มีหน้าที่จับให้ได้</div>
          </div>
          <div class="card">
            <span class="cn">สาเหตุที่ 2</span>
            <div class="ct">ปัญหาด้านการออกแบบ</div>
            <div class="cs"><span class="en">Design problems</span><br>ตัวสินค้าใช้ไม่ได้จริงอย่างที่คิด · เป็นข้อที่<b>ขั้นพัฒนาสินค้าและการทดสอบกับผู้บริโภค</b>มีหน้าที่จับให้ได้</div>
          </div>
          <div class="card">
            <span class="cn">สาเหตุที่ 3</span>
            <div class="ct">ตั้งราคาหรือวางตำแหน่งผิด</div>
            <div class="cs"><span class="en">Incorrect pricing or positioning</span><br>ของดีแต่บอกไม่ถูกว่าเพื่อใครและคุ้มอย่างไร · เป็นข้อที่<b>ขั้นพัฒนากลยุทธ์การตลาด</b>มีหน้าที่จับให้ได้</div>
          </div>
          <div class="card">
            <span class="cn">สาเหตุที่ 4</span>
            <div class="ct">ต้นทุนการพัฒนาสูงเกินไป</div>
            <div class="cs"><span class="en">High development costs</span><br>กว่าจะทำเสร็จก็แพงจนขายไม่คุ้ม</div>
          </div>
          <div class="card">
            <span class="cn">สาเหตุที่ 5</span>
            <div class="ct">การตอบโต้ของคู่แข่ง</div>
            <div class="cs"><span class="en">Competitor reaction</span><br>คู่แข่งลดราคา ออกของเลียนแบบ หรือเร่งโฆษณาสวนทันที</div>
          </div>
        </div>
        <div class="note warn">
          <span class="nh">อ่านห้าข้อนี้ให้เป็นแผนที่</span>
          สี่ในห้าข้อเป็นเรื่องที่<b>รู้ได้ก่อนลงทุนจริง ถ้ามีขั้นตอนตรวจ</b> · นี่คือเหตุผลทั้งหมดที่ตำราวางกระบวนการแปดขั้นไว้ และเป็นเหตุผลว่าทำไมแต่ละขั้นจึงต้อง<b>คัดความคิดออกให้มากขึ้นเรื่อย ๆ</b> ไม่ใช่เดินหน้าอย่างเดียว
        </div>
      </div>
    </section>

    <section class="sec" id="m8-3">
      <div class="sec-h"><span class="sec-n">3</span><h2>กระบวนการพัฒนาสินค้าใหม่แปดขั้น</h2></div>
      <div class="body">
        <p class="lede">นี่คือ<b>แกนกลางของทั้งบท</b> · ต้องจำได้ทั้งแปดขั้นเรียงตามลำดับ และต้องแยกออกว่าขั้นไหนทำอะไร เพราะข้อสอบจะให้สถานการณ์มาแล้วถามว่าอยู่ขั้นใด</p>
        <figure class="fig">
          <div class="plate"><img loading="lazy" alt="Figure 9.1 Major Stages in New Product Development" src="FIG1"></div>
          <figcaption><b>Figure 9.1</b> Major Stages in New Product Development — แปดขั้นเรียงจากซ้ายบนไปขวาแล้ววกลงมาแถวล่าง · กล่องคำอธิบายซ้ายบนยกตัวอย่าง <b>AT&amp;T</b> ที่โครงการ <b>The Innovation Pipeline (TIP)</b> ซึ่งเป็นการระดมความคิดจากพนักงาน เก็บความคิดเรื่องนวัตกรรมได้<b>มากกว่า 40,000 ความคิด</b>จากสมาชิกใน 50 รัฐและ 54 ประเทศ · กล่องขวาล่างบอกผลลัพธ์ปลายทางว่า จากความคิดทั้ง 40,000 นั้น<b>มีเพียง 80 โครงการที่ได้รับเงินสนับสนุน</b></figcaption>
        </figure>
        <div class="note key">
          <span class="nh">รูปทรงของกระบวนการ</span>
          <b>ขั้นที่ 1 สร้างความคิด = ยิ่งมากยิ่งดี</b> · <b>ขั้นที่ 2 ถึง 8 = ลดจำนวนความคิดลงเรื่อย ๆ และพัฒนาเฉพาะตัวที่ดีที่สุดให้กลายเป็นสินค้าที่ทำกำไร</b> <span class="en">the remaining steps reduce the number of ideas and develop only the best ones into profitable products</span><br>
          ตัวเลขของ AT&amp;T อ่านได้ตรง ๆ ว่า <b>40,000 ความคิด เหลือ 80 โครงการ</b> คือเหลือราวสองในหมื่น นั่นคือรูปทรงของกรวยที่บทนี้พูดถึง
        </div>
        <h3>กดเลือกดูทีละขั้น</h3>
        <div class="step-wrap">
          <div class="steps" role="group" aria-label="เลือกขั้นตอนของการพัฒนาสินค้าใหม่">
            <button type="button" class="step" data-npd="1" aria-pressed="true"><span class="sn">ขั้นที่ 1</span><span class="st">สร้างความคิด</span></button>
            <button type="button" class="step" data-npd="2" aria-pressed="false"><span class="sn">ขั้นที่ 2</span><span class="st">กลั่นกรองความคิด</span></button>
            <button type="button" class="step" data-npd="3" aria-pressed="false"><span class="sn">ขั้นที่ 3</span><span class="st">พัฒนาและทดสอบแนวคิด</span></button>
            <button type="button" class="step" data-npd="4" aria-pressed="false"><span class="sn">ขั้นที่ 4</span><span class="st">พัฒนากลยุทธ์การตลาด</span></button>
            <button type="button" class="step" data-npd="5" aria-pressed="false"><span class="sn">ขั้นที่ 5</span><span class="st">วิเคราะห์ทางธุรกิจ</span></button>
            <button type="button" class="step" data-npd="6" aria-pressed="false"><span class="sn">ขั้นที่ 6</span><span class="st">พัฒนาสินค้า</span></button>
            <button type="button" class="step" data-npd="7" aria-pressed="false"><span class="sn">ขั้นที่ 7</span><span class="st">ทดสอบตลาด</span></button>
            <button type="button" class="step" data-npd="8" aria-pressed="false"><span class="sn">ขั้นที่ 8</span><span class="st">นำออกสู่ตลาด</span></button>
          </div>
          <div class="step-out" id="npd-out"></div>
        </div>
        <div class="note">
          <span class="nh">เทคนิคจำลำดับ</span>
          สังเกตว่าลำดับเดินจาก<b>นามธรรมไปหารูปธรรม</b>ตลอด — ความคิดลอย ๆ (1) → ความคิดที่ผ่านการคัด (2) → แนวคิดที่เขียนเป็นภาษาผู้บริโภค (3) → แผนการตลาด (4) → ตัวเลข (5) → ของจริงที่จับต้องได้ (6) → ของจริงที่วางขายในตลาดจำลอง (7) → ของจริงที่วางขายในตลาดจริง (8)
        </div>
      </div>
    </section>

    <section class="sec" id="m8-4">
      <div class="sec-h"><span class="sec-n">4</span><h2>ขั้นที่ 1 · การสร้างความคิด <span class="en">Idea generation</span></h2></div>
      <div class="body">
        <div class="note key">
          <span class="nh">นิยามที่ต้องจำ</span>
          <b>Idea generation is the systematic search for new product ideas.</b><br>
          การสร้างความคิดคือ<b>การค้นหาความคิดเรื่องสินค้าใหม่อย่างเป็นระบบ</b> · คำสำคัญคือ <b>systematic</b> — ไม่ใช่รอให้ความคิดดี ๆ โผล่มาเอง แต่ต้องมีกลไกไล่เก็บ
        </div>
        <p class="lede">แหล่งที่มาของความคิดแบ่งเป็นสองกลุ่มใหญ่ และต้องแยกให้ขาดว่าอะไรอยู่กลุ่มไหน</p>
        <div class="grid g2">
          <div class="card">
            <span class="cn">แหล่งภายใน</span>
            <div class="ct">Internal sources</div>
            <div class="cs">หมายถึง<b>งานวิจัยและพัฒนาที่เป็นทางการของบริษัทเอง ผู้บริหารและพนักงาน และโครงการผู้ประกอบการภายใน</b>
              <ul class="list">
                <li>กระบวนการ <b>R&amp;D</b> แบบดั้งเดิม</li>
                <li><b>Intrapreneurs</b> คือพนักงานที่ทำตัวเป็นผู้ประกอบการอยู่ภายในบริษัท</li>
                <li>ตัวอย่าง <b>Facebook</b> ใช้ <b>hackathon</b> เพื่อดึงความคิดเรื่องนวัตกรรมออกมาจากสมองของพนักงานตัวเอง</li>
              </ul>
            </div>
          </div>
          <div class="card">
            <span class="cn">แหล่งภายนอก</span>
            <div class="ct">External sources</div>
            <div class="cs">หมายถึงแหล่งที่อยู่<b>นอกบริษัท</b> เช่น ลูกค้า คู่แข่ง ผู้จัดจำหน่าย ผู้จัดหาวัตถุดิบ และบริษัทออกแบบภายนอก
              <ul class="list">
                <li><b>Distributors and suppliers</b> ผู้จัดจำหน่ายและผู้จัดหาวัตถุดิบ</li>
                <li><b>Competitors and their products</b> คู่แข่งและสินค้าของคู่แข่ง</li>
                <li><b>Trade magazines and shows</b> นิตยสารและงานแสดงสินค้าของอุตสาหกรรม</li>
                <li><b>Customers</b> ลูกค้า</li>
                <li><b>Crowdsourcing</b> การระดมความคิดจากฝูงชน</li>
              </ul>
            </div>
          </div>
        </div>
        <h3>เจาะลึกสองแหล่งที่สไลด์ให้ตัวอย่างไว้</h3>
        <div class="note">
          <span class="nh">ลูกค้า · กรณี 3M</span>
          วิธีดึงความคิดจากลูกค้ามีสองทางที่ตำราเน้น คือ <b>วิเคราะห์คำถามและคำร้องเรียนของลูกค้า</b>เพื่อหาสินค้าที่แก้ปัญหาของผู้บริโภคได้ดีกว่าเดิม และ <b>เชิญลูกค้าเข้ามาแบ่งปันข้อเสนอแนะและความคิด</b><br>
          <b>3M</b> เปิด <b>customer innovation centers</b> ขึ้นมาเพื่อการนี้โดยเฉพาะ · ศูนย์นี้ทำสองหน้าที่พร้อมกัน คือ<b>ผลิตความคิดเรื่องสินค้าใหม่ที่มาจากลูกค้า</b> และ<b>ช่วยให้ 3M สร้างความสัมพันธ์ระยะยาวกับลูกค้า</b>ไปด้วยในตัว
        </div>
        <div class="note">
          <span class="nh">Crowdsourcing · กรณี Tupperware</span>
          <b>Crowdsourcing</b> คือการ<b>เชิญชุมชนคนกว้าง ๆ</b> ทั้งลูกค้า พนักงาน นักวิทยาศาสตร์และนักวิจัยอิสระ และแม้แต่<b>สาธารณชนทั่วไป</b> เข้ามาร่วมในกระบวนการสร้างนวัตกรรมสินค้าใหม่<br>
          <b>Tupperware</b> ซึ่งเป็นยักษ์ใหญ่ด้านภาชนะบรรจุอาหาร จัดการประกวด <b>Clever Container Challenge</b> เพื่อหาความคิดในการ<b>ผสานเทคโนโลยี Internet of Things เข้ากับภาชนะอาหารสำหรับครัวอัจฉริยะในอนาคต</b>
        </div>
        <div class="note warn">
          <span class="nh">จุดที่สับสนบ่อย</span>
          <b>Crowdsourcing ไม่เท่ากับ external source ทั้งหมด</b> · crowdsourcing เป็น<b>หนึ่งในวิธีของแหล่งภายนอก</b> จุดต่างคือมันเปิดกว้างถึงขั้น<b>คนนอกที่ไม่ใช่ลูกค้า</b>ก็ส่งความคิดเข้ามาได้ · ส่วน hackathon ของ Facebook เป็น<b>แหล่งภายใน</b> เพราะดึงจาก<b>พนักงานของตัวเอง</b> ไม่ใช่คนนอก
        </div>
      </div>
    </section>

    <section class="sec" id="m8-5">
      <div class="sec-h"><span class="sec-n">5</span><h2>ขั้นที่ 2 · การกลั่นกรองความคิด <span class="en">Idea screening</span></h2></div>
      <div class="body">
        <div class="note key">
          <span class="nh">นิยามที่ต้องจำ</span>
          <b>Screening new-product ideas to spot good ideas and drop poor ones as soon as possible.</b><br>
          การกลั่นกรองความคิดเรื่องสินค้าใหม่ เพื่อ<b>จับความคิดที่ดีให้เจอ</b>และ<b>ทิ้งความคิดที่แย่ให้เร็วที่สุด</b>
        </div>
        <p>คำว่า <b>as soon as possible</b> คือหัวใจของขั้นนี้ · เหตุผลตรงไปตรงมา — ยิ่งปล่อยความคิดที่แย่เดินไปไกลในกระบวนการเท่าไร ต้นทุนที่เสียไปก็ยิ่งสูงขึ้นเท่านั้น และกลับมาไม่ได้</p>
        <h3>กรอบ R-W-W</h3>
        <p class="lede">ตำราให้เครื่องมือกลั่นกรองหนึ่งชุด เรียกว่า <b>R-W-W screening framework</b> ซึ่งเป็นสามคำถามที่ต้องตอบว่าใช่ให้ครบทั้งสามข้อ</p>
        <div class="grid g3">
          <div class="card">
            <span class="cn">R</span>
            <div class="ct">Is it real?</div>
            <div class="cs">มันจริงหรือเปล่า — <b>มีความต้องการอยู่จริงไหม</b> และ<b>ทำสินค้านี้ขึ้นมาได้จริงไหม</b></div>
          </div>
          <div class="card">
            <span class="cn">W</span>
            <div class="ct">Can we win?</div>
            <div class="cs">เราชนะได้ไหม — <b>บริษัทมีความได้เปรียบที่ยั่งยืนพอจะเอาชนะคู่แข่งในตลาดนี้หรือไม่</b></div>
          </div>
          <div class="card">
            <span class="cn">W</span>
            <div class="ct">Is it worth doing?</div>
            <div class="cs">คุ้มที่จะทำไหม — <b>ผลตอบแทนคุ้มกับความเสี่ยงและทรัพยากรที่ต้องลงไปหรือไม่</b></div>
          </div>
        </div>
        <div class="note warn">
          <span class="nh">ข้อควรระวัง</span>
          ขั้นนี้เป็นด่าน<b>ลดจำนวน</b>ด่านแรก ตรงข้ามกับขั้นที่ 1 ซึ่งเป็นด่าน<b>เพิ่มจำนวน</b> · ความผิดพลาดที่ตำราเตือนมีสองแบบ คือ <b>drop-error</b> ทิ้งความคิดที่จริง ๆ แล้วดี กับ <b>go-error</b> ปล่อยความคิดที่แย่ผ่านไป · R-W-W ถูกออกแบบมาเพื่อลดทั้งสองแบบพร้อมกัน
        </div>
      </div>
    </section>

    <section class="sec" id="m8-6">
      <div class="sec-h"><span class="sec-n">6</span><h2>ขั้นที่ 3 · การพัฒนาและทดสอบแนวคิดสินค้า <span class="en">Concept development and testing</span></h2></div>
      <div class="body">
        <p class="lede">ขั้นนี้มีสามคำที่หน้าตาคล้ายกันมากจน<b>ข้อสอบชอบเอามาสลับกัน</b> ต้องแยกให้ขาด</p>
        <div class="tw"><table class="tbl">
          <thead><tr><th>คำ</th><th>นิยามตามตำรา</th><th>อยู่ในหัวใคร</th></tr></thead>
          <tbody>
            <tr><td class="k">Product idea<br>ความคิดเรื่องสินค้า</td><td>ความคิดเกี่ยวกับสินค้าที่<b>เป็นไปได้</b> ซึ่งบริษัทมองเห็นว่าตัวเองจะนำเสนอออกสู่ตลาดได้</td><td><b>บริษัท</b> — ยังเป็นความคิดดิบ ๆ</td></tr>
            <tr><td class="k">Product concept<br>แนวคิดสินค้า</td><td><b>ฉบับที่ลงรายละเอียดแล้ว</b>ของความคิดเรื่องสินค้าใหม่ ซึ่ง<b>เขียนด้วยถ้อยคำที่มีความหมายต่อผู้บริโภค</b></td><td><b>บริษัท</b> — แต่เขียนด้วยภาษาของลูกค้า</td></tr>
            <tr><td class="k">Product image<br>ภาพลักษณ์สินค้า</td><td><b>วิธีที่ผู้บริโภครับรู้</b>ต่อสินค้าที่มีอยู่จริงหรือสินค้าที่อาจจะมี</td><td><b>ผู้บริโภค</b> — เป็นการรับรู้ ไม่ใช่สิ่งที่บริษัทเขียน</td></tr>
          </tbody>
        </table></div>
        <div class="note key">
          <span class="nh">วิธีจำสามคำนี้</span>
          <b>idea → concept → image</b> คือการเดินจาก<b>ของบริษัท</b>ไปสู่<b>ของลูกค้า</b> · idea กับ concept ยังอยู่ฝั่งบริษัท ต่างกันแค่<b>ละเอียดแค่ไหนและเขียนด้วยภาษาใคร</b> · ส่วน image ข้ามไปอยู่ฝั่งลูกค้าแล้ว เป็น<b>การรับรู้</b> ซึ่งบริษัทสั่งไม่ได้โดยตรง
        </div>
        <h3>การทดสอบแนวคิด <span class="en">Concept testing</span></h3>
        <p>คือการ<b>ทดสอบแนวคิดสินค้าใหม่กับกลุ่มผู้บริโภคเป้าหมาย เพื่อดูว่าแนวคิดนั้นดึงดูดผู้บริโภคได้แรงหรือไม่</b></p>
        <ul class="list">
          <li>ใช้<b>คำบรรยาย ภาพ หรือแบบจำลอง</b>ของสินค้า <span class="en">a description, picture or model</span> — ยังไม่ต้องมีของจริง</li>
          <li>แล้ว<b>ถามผู้บริโภคถึงปฏิกิริยาของเขา</b></li>
        </ul>
        <div class="note">
          <span class="nh">งานสามอย่างของขั้นนี้</span>
          <b>1</b> พัฒนาสินค้าใหม่ออกมาเป็น<b>แนวคิดสินค้าทางเลือกหลาย ๆ แบบ</b> · <b>2</b> หาว่าแต่ละแนวคิด<b>ดึงดูดลูกค้าได้มากแค่ไหน</b> · <b>3</b> <b>เลือกแนวคิดที่ดีที่สุด</b>มาหนึ่งอัน<br>
          สังเกตว่าหนึ่ง product idea สามารถแตกออกเป็น<b>หลาย product concept</b>ได้ และขั้นนี้คือการเลือกว่าจะเดินต่อด้วยอันไหน
        </div>
        <div class="note">
          <span class="nh">ตัวอย่างในสไลด์ · รถยนต์ไฟฟ้าล้วน</span>
          สไลด์ยกรถเก๋งขนาดใหญ่ไฟฟ้าล้วนรุ่นแรกของ <b>Tesla</b> เป็นตัวอย่างของแนวคิดสินค้าที่ต้องทดสอบว่าผู้บริโภคเอาด้วยไหม · และบอกต่อว่ารุ่น <b>Model 3</b> ซึ่งเป็นรุ่นคอมแพกต์ที่ออกมาทีหลัง<b>วิ่งได้ถึง 310 ไมล์ต่อการชาร์จหนึ่งครั้ง</b> และ<b>มีต้นทุนการใช้งานระดับเศษสตางค์ต่อไมล์</b><br>
          <span class="en">ที่มา สไลด์ประกอบการสอนบทที่ 8 อ้างอิง Kotler &amp; Armstrong</span>
        </div>
      </div>
    </section>

    <section class="sec" id="m8-7">
      <div class="sec-h"><span class="sec-n">7</span><h2>ขั้นที่ 4 · การพัฒนากลยุทธ์การตลาด <span class="en">Marketing strategy development</span></h2></div>
      <div class="body">
        <div class="note key">
          <span class="nh">นิยามที่ต้องจำ</span>
          <b>Marketing strategy development is designing an initial marketing strategy for a new product based on the product concept.</b><br>
          คือการ<b>ออกแบบกลยุทธ์การตลาดเริ่มต้น</b>สำหรับสินค้าใหม่ <b>โดยอิงจากแนวคิดสินค้า</b>ที่เลือกมาจากขั้นที่ 3
        </div>
        <p class="lede">ผลลัพธ์ของขั้นนี้คือเอกสารหนึ่งชิ้นชื่อ <b>marketing strategy statement</b> ซึ่งต้องมีองค์ประกอบครบตามรายการข้างล่าง</p>
        <ul class="list">
          <li><b>คำบรรยายตลาดเป้าหมาย</b> <span class="en">target market description</span> — ต่อยอดโดยตรงจากบทที่ 6 เรื่อง segmentation และ targeting</li>
          <li><b>ข้อเสนอคุณค่าที่วางแผนไว้</b> <span class="en">value proposition planned</span> — ต่อยอดจากบทที่ 6 เรื่อง differentiation และ positioning</li>
          <li><b>เป้าหมายยอดขาย ส่วนแบ่งตลาด และกำไร</b> <span class="en">sales, market-share, profit goals</span></li>
          <li><b>โครงร่างของราคา ช่องทางจัดจำหน่าย และงบประมาณการตลาด</b>ที่วางแผนไว้</li>
          <li><b>เป้าหมายยอดขายและกำไรระยะยาว</b> <span class="en">planned long-run sales and profit goals</span></li>
          <li><b>กลยุทธ์ส่วนประสมการตลาด 4Ps</b> <span class="en">marketing mix strategy</span></li>
        </ul>
        <div class="note">
          <span class="nh">สองช่วงเวลาในเอกสารเดียว</span>
          สังเกตว่ารายการนี้พูดถึง<b>ทั้งช่วงสั้นและช่วงยาว</b> — เป้าหมายยอดขายและส่วนแบ่งตลาดกับงบประมาณคือ<b>ปีแรก ๆ</b> ส่วน <b>long-run sales and profit goals</b> คือ<b>ระยะยาว</b> · ข้อสอบชอบถามว่าอะไรอยู่ใน marketing strategy statement บ้าง และ<b>คำตอบรวมทั้งสองช่วง</b>
        </div>
        <div class="note warn">
          <span class="nh">อย่าสลับขั้นที่ 4 กับขั้นที่ 5</span>
          ขั้นที่ 4 คือการ<b>ออกแบบแผน</b> ซึ่งรวมการตั้งเป้าหมายและโครงร่างงบประมาณ · ขั้นที่ 5 คือการ<b>เอาแผนนั้นมาตรวจด้วยตัวเลข</b>ว่าคุ้มหรือไม่ · ลำดับนี้กลับกันไม่ได้ เพราะยังไม่มีแผนก็ไม่มีอะไรให้ประมาณการ
        </div>
      </div>
    </section>

    <section class="sec" id="m8-8">
      <div class="sec-h"><span class="sec-n">8</span><h2>ขั้นที่ 5 · การวิเคราะห์ทางธุรกิจ <span class="en">Business analysis</span></h2></div>
      <div class="body">
        <div class="note key">
          <span class="nh">นิยามที่ต้องจำ</span>
          <b>Business analysis is a review of the sales, costs, and profit projections for a new product to find out whether these factors satisfy the company's objectives.</b><br>
          คือการ<b>ทบทวนประมาณการยอดขาย ต้นทุน และกำไร</b>ของสินค้าใหม่ เพื่อดูว่าปัจจัยเหล่านี้<b>ตอบวัตถุประสงค์ของบริษัทได้หรือไม่</b>
        </div>
        <p>ขั้นนี้สั้นที่สุดในแปดขั้น แต่เป็น<b>ประตูบานสุดท้ายก่อนที่เงินก้อนใหญ่จะถูกใช้</b> เพราะขั้นที่ 6 คือการสร้างของจริงซึ่งแพง</p>
        <div class="grid g3">
          <div class="card"><span class="cn">ตัวที่ 1</span><div class="ct">Sales projections</div><div class="cs">ประมาณการ<b>ยอดขาย</b> · เชื่อมโดยตรงกับสาเหตุความล้มเหลวข้อที่ 1 คือประเมินขนาดตลาดสูงเกินจริง</div></div>
          <div class="card"><span class="cn">ตัวที่ 2</span><div class="ct">Cost projections</div><div class="cs">ประมาณการ<b>ต้นทุน</b> · เชื่อมกับสาเหตุความล้มเหลวข้อที่ 4 คือต้นทุนการพัฒนาสูงเกินไป</div></div>
          <div class="card"><span class="cn">ตัวที่ 3</span><div class="ct">Profit projections</div><div class="cs">ประมาณการ<b>กำไร</b> · ตัวตัดสินว่าจะไปต่อหรือหยุด เพราะต้องเทียบกับ<b>วัตถุประสงค์ของบริษัท</b></div></div>
        </div>
        <div class="note">
          <span class="nh">เกณฑ์ตัดสินไม่ใช่ตัวเลขลอย ๆ</span>
          คำว่า <b>satisfy the company's objectives</b> แปลว่าเกณฑ์คือ<b>วัตถุประสงค์ของบริษัทเอง</b> ไม่ใช่ตัวเลขมาตรฐานของอุตสาหกรรม · สินค้าตัวเดียวกันจึงอาจผ่านที่บริษัทหนึ่งและไม่ผ่านที่อีกบริษัทหนึ่งได้
        </div>
      </div>
    </section>

    <section class="sec" id="m8-9">
      <div class="sec-h"><span class="sec-n">9</span><h2>ขั้นที่ 6 · การพัฒนาสินค้า <span class="en">Product development</span></h2></div>
      <div class="body">
        <div class="note key">
          <span class="nh">นิยามที่ต้องจำ</span>
          <b>Product development is developing the product concept into a physical product to ensure that the product idea can be turned into a workable market offering.</b><br>
          คือการ<b>พัฒนาแนวคิดสินค้าให้กลายเป็นสินค้าที่มีตัวตนจริง</b> เพื่อให้มั่นใจว่าความคิดเรื่องสินค้านั้น<b>แปลงเป็นข้อเสนอที่ใช้งานได้จริงในตลาด</b>
        </div>
        <p class="lede">ขั้นนี้คือจุดที่<b>แนวคิดบนกระดาษกลายเป็นของที่จับต้องได้</b> และมีสองกิจกรรมหลัก</p>
        <ul class="list">
          <li><b>สร้างต้นแบบ</b> <span class="en">prototypes are made</span></li>
          <li><b>ทดสอบกับผู้บริโภค</b> <span class="en">consumer tests are conducted</span></li>
        </ul>
        <div class="note">
          <span class="nh">ตัวอย่างในสไลด์ · Brooks</span>
          <b>Brooks</b> ผู้ผลิตรองเท้าวิ่ง รวบรวมผู้ใช้จำนวนมากเข้ามาเป็นกองทัพทดสอบสินค้า โดยเรียกพวกเขาว่า <b>Lab Rats</b> และ <b>Wear Testers</b> · ข้อความที่แบรนด์สื่อกับคนกลุ่มนี้คือ <b>&ldquo;ผลตอบรับของคุณคือสิ่งที่กำหนดความพอดี การใช้งาน และการออกแบบของสินค้าทุกตัวของเราในอนาคต&rdquo;</b><br>
          นี่คือตัวอย่างของ <b>consumer tests</b> ในขั้นที่ 6 ไม่ใช่ concept testing ในขั้นที่ 3 — เพราะคนกลุ่มนี้ได้<b>รองเท้าจริงไปใส่วิ่งจริง</b> ไม่ใช่ดูภาพหรือคำบรรยาย
        </div>
        <div class="note warn">
          <span class="nh">เส้นแบ่งที่ออกสอบบ่อย · ขั้นที่ 3 เทียบขั้นที่ 6 เทียบขั้นที่ 7</span>
          <b>ขั้นที่ 3 concept testing</b> ผู้บริโภคเห็นแค่<b>คำบรรยาย ภาพ หรือแบบจำลอง</b><br>
          <b>ขั้นที่ 6 consumer tests</b> ผู้บริโภคได้<b>ของจริงหรือต้นแบบไปใช้</b> แต่ยัง<b>ไม่มีโปรแกรมการตลาด</b>มาด้วย<br>
          <b>ขั้นที่ 7 test marketing</b> ผู้บริโภคเจอ<b>ทั้งสินค้าและโปรแกรมการตลาดทั้งชุด</b>ในสภาพตลาดที่สมจริง
        </div>
      </div>
    </section>

    <section class="sec" id="m8-10">
      <div class="sec-h"><span class="sec-n">10</span><h2>ขั้นที่ 7 · การทดสอบตลาด <span class="en">Test marketing</span></h2></div>
      <div class="body">
        <div class="note key">
          <span class="nh">นิยามที่ต้องจำ</span>
          <b>Test marketing is the stage of new product development in which the product and its proposed marketing program are tested in realistic market settings.</b><br>
          คือขั้นที่<b>ทั้งตัวสินค้าและโปรแกรมการตลาดที่เสนอไว้</b>ถูกนำไป<b>ทดสอบในสภาพตลาดที่สมจริง</b> · คำสำคัญคือ <b>และ</b> — ทดสอบสองอย่างพร้อมกัน ไม่ใช่แค่สินค้า
        </div>
        <h3>สามรูปแบบของการทดสอบตลาด</h3>
        <div class="grid g3">
          <div class="card">
            <span class="cn">แบบที่ 1</span>
            <div class="ct">Standard test markets</div>
            <div class="cs">ทดสอบในตลาดจริงเต็มรูปแบบ · ตำราระบุว่า<b>มักกินขอบเขตกว้างและมีค่าใช้จ่ายสูง</b> <span class="en">extensive and costly to use</span></div>
          </div>
          <div class="card">
            <span class="cn">แบบที่ 2</span>
            <div class="ct">Simulated test markets</div>
            <div class="cs">นักวิจัย<b>วัดการตอบสนองของผู้บริโภคในร้านค้าจำลองในห้องปฏิบัติการ หรือในสภาพแวดล้อมการช็อปปิงออนไลน์จำลอง</b></div>
          </div>
          <div class="card">
            <span class="cn">แบบที่ 3</span>
            <div class="ct">Controlled test markets</div>
            <div class="cs">ทดสอบสินค้าใหม่และกลยุทธ์<b>กับกลุ่มผู้ซื้อและร้านค้าที่ถูกควบคุมไว้</b> <span class="en">controlled panels of shoppers and stores</span></div>
          </div>
        </div>
        <h3>เมื่อไรควรทดสอบตลาด และเมื่อไรไม่ต้อง</h3>
        <div class="tw"><table class="tbl">
          <thead><tr><th>มักจะทดสอบตลาด <span class="en">likely</span></th><th>มักจะไม่ทดสอบตลาด <span class="en">unlikely</span></th></tr></thead>
          <tbody>
            <tr><td><b>สินค้าใหม่ที่ต้องลงทุนสูง</b><br><span class="en">new product with large investment</span></td><td><b>การต่อสายผลิตภัณฑ์แบบง่าย ๆ</b><br><span class="en">simple line extension</span></td></tr>
            <tr><td><b>ยังไม่แน่ใจในตัวสินค้าหรือโปรแกรมการตลาด</b><br><span class="en">uncertainty about product or marketing program</span></td><td><b>เป็นการลอกสินค้าของคู่แข่ง</b><br><span class="en">copy of competitor product</span></td></tr>
            <tr><td></td><td><b>ต้นทุนต่ำ</b> <span class="en">low costs</span></td></tr>
            <tr><td></td><td><b>ผู้บริหารมั่นใจอยู่แล้ว</b> <span class="en">management confidence</span></td></tr>
          </tbody>
        </table></div>
        <div class="note">
          <span class="nh">ตัวอย่างในสไลด์ · Starbucks</span>
          บางครั้งบริษัท<b>ย่นหรือข้ามการทดสอบตลาดไปเลย เพื่อฉวยจังหวะที่ตลาดกำลังเปลี่ยนเร็ว</b> · <b>Starbucks</b> ทำแบบนั้นกับ<b>แอปพลิเคชันชำระเงินผ่านมือถือ</b>ของตัวเอง และกลายเป็นความสำเร็จอย่างสูง<br>
          อ่านตัวอย่างนี้คู่กับตารางข้างบน — การข้ามทดสอบตลาดไม่ได้แปลว่าประมาท แต่แปลว่า<b>ต้นทุนของการช้าสูงกว่าต้นทุนของการพลาด</b>
        </div>
      </div>
    </section>

    <section class="sec" id="m8-11">
      <div class="sec-h"><span class="sec-n">11</span><h2>ขั้นที่ 8 · การนำออกสู่ตลาดเชิงพาณิชย์ <span class="en">Commercialization</span></h2></div>
      <div class="body">
        <div class="note key">
          <span class="nh">นิยามที่ต้องจำ</span>
          <b>Commercialization involves introducing a new product into the market.</b><br>
          คือการ<b>นำสินค้าใหม่เข้าสู่ตลาดจริง</b> · เป็นขั้นสุดท้ายและเป็นขั้นที่<b>ใช้เงินมากที่สุด</b>
        </div>
        <p class="lede">ขั้นนี้ตอบสามคำถาม</p>
        <div class="grid g3">
          <div class="card">
            <span class="cn">คำถามที่ 1</span>
            <div class="ct">เปิดตัวเมื่อไร <span class="en">When to launch?</span></div>
            <div class="cs">จังหวะเวลา · เร็วไปอาจชนสินค้าเดิมของตัวเอง ช้าไปอาจเสียตลาดให้คู่แข่ง</div>
          </div>
          <div class="card">
            <span class="cn">คำถามที่ 2</span>
            <div class="ct">เปิดตัวที่ไหน <span class="en">Where to launch?</span></div>
            <div class="cs">ทำเลเดียว · ทั้งรัฐหรือจังหวัด · ทั้งภูมิภาค · ทั้งประเทศ · หรือระดับนานาชาติ <span class="en">single location, state, region, nationally, internationally</span></div>
          </div>
          <div class="card">
            <span class="cn">คำถามที่ 3</span>
            <div class="ct">ทยอยออกอย่างไร <span class="en">Planned market rollout?</span></div>
            <div class="cs">แผนการกระจายออกสู่ตลาดตามลำดับที่วางไว้ ไม่ใช่เปิดพร้อมกันทุกที่เสมอไป</div>
          </div>
        </div>
        <div class="note">
          <span class="nh">ความเชื่อมโยงกับบทถัดไปของวิชา</span>
          คำตอบของคำถามที่ 2 และ 3 คือจุดที่บทนี้ส่งต่อไปยังเรื่อง<b>ช่องทางการจัดจำหน่าย</b> · และคำตอบของคำถามที่ 1 คือจุดที่ส่งต่อไปยังเรื่อง<b>กลยุทธ์ขั้นแนะนำของวงจรชีวิตผลิตภัณฑ์</b> ซึ่งอยู่ในครึ่งหลังของบทนี้เอง
        </div>
      </div>
    </section>

    <section class="sec" id="m8-12">
      <div class="sec-h"><span class="sec-n">12</span><h2>การบริหารกระบวนการพัฒนาสินค้าใหม่</h2></div>
      <div class="body">
        <p class="lede">รู้แปดขั้นแล้วยังไม่พอ · ตำราบอกว่าบริษัทต้อง<b>มองการพัฒนาสินค้าใหม่แบบองค์รวม</b> <span class="en">holistic approach</span> และการพัฒนาสินค้าใหม่ที่สำเร็จต้องมีคุณสมบัติสามอย่างพร้อมกัน</p>
        <div class="grid g3">
          <div class="card">
            <span class="cn">แบบที่ 1</span>
            <div class="ct">ยึดลูกค้าเป็นศูนย์กลาง<br><span class="en">Customer-centered NPD</span></div>
            <div class="cs"><b>มุ่งหาวิธีใหม่ ๆ ในการแก้ปัญหาของลูกค้า และสร้างประสบการณ์ที่ทำให้ลูกค้าพอใจมากขึ้น</b><br>ตัวอย่าง <b>LEGO</b> รับฟังลูกค้าและ<b>ดึงความคิดเรื่องสินค้าใหม่จากชุมชนผู้ใช้ของตัวเองอย่างจริงจัง</b> จนมีผู้สังเกตการณ์เรียกว่า <b>&ldquo;the Apple of Toys&rdquo;</b></div>
          </div>
          <div class="card">
            <span class="cn">แบบที่ 2</span>
            <div class="ct">ทำงานเป็นทีม<br><span class="en">Team-based NPD</span></div>
            <div class="cs"><b>ให้หลายแผนกของบริษัททำงานร่วมกันอย่างใกล้ชิด โดยทำขั้นตอนต่าง ๆ คาบเกี่ยวกัน</b>เพื่อประหยัดเวลาและเพิ่มประสิทธิผล<br>· <b>ทีมข้ามสายงาน</b> <span class="en">cross-functional teams</span> ทำให้การพัฒนา<b>เร็วและยืดหยุ่น</b><br>· แต่<b>ก่อให้เกิดความตึงเครียดและความสับสนในองค์กรมากกว่าวิธีทำทีละขั้นตามลำดับ</b></div>
          </div>
          <div class="card">
            <span class="cn">แบบที่ 3</span>
            <div class="ct">เป็นระบบ<br><span class="en">Systematic NPD</span></div>
            <div class="cs">กระบวนการพัฒนาสินค้าใหม่ควร<b>เป็นองค์รวมและเป็นระบบ</b><br><b>ระบบบริหารจัดการนวัตกรรม</b> <span class="en">innovation management system</span> ช่วยให้บริษัท<b>รวบรวม ทบทวน ประเมิน และบริหารความคิดเรื่องสินค้าใหม่</b> ซึ่งให้ผลสองอย่าง คือ<b>สร้างวัฒนธรรมองค์กรที่มุ่งนวัตกรรม</b> และ<b>ได้ความคิดเรื่องสินค้าใหม่จำนวนมาก</b></div>
          </div>
        </div>
        <div class="note warn">
          <span class="nh">จุดที่ข้อสอบชอบดัก · ข้อเสียของทีมข้ามสายงาน</span>
          หลายคนจำแต่ข้อดีว่า<b>เร็วและยืดหยุ่น</b> แล้วตอบผิดเวลาถูกถามถึงข้อเสีย · ตำราระบุข้อเสียไว้ชัดว่า<b>ก่อให้เกิดความตึงเครียดและความสับสนในองค์กรมากกว่าแบบเรียงลำดับ</b> <span class="en">more organizational tension and confusion than the sequential approach</span> · ข้อแลกเปลี่ยนคือ<b>แลกความเป็นระเบียบกับความเร็ว</b>
        </div>
        <div class="note">
          <span class="nh">สามแบบนี้ไม่ใช่ตัวเลือกที่เลือกอย่างใดอย่างหนึ่ง</span>
          ตำราใช้คำว่า <b>should be</b> กับทั้งสามข้อ แปลว่าการพัฒนาสินค้าใหม่ที่ดี<b>ต้องมีครบทั้งสามพร้อมกัน</b> — ยึดลูกค้า ทำเป็นทีม และเป็นระบบ · ไม่ใช่เลือกหนึ่งในสาม
        </div>
      </div>
    </section>

    <section class="sec" id="m8-13">
      <div class="sec-h"><span class="sec-n">13</span><h2>วงจรชีวิตผลิตภัณฑ์ · ห้าขั้น</h2></div>
      <div class="body">
        <div class="note key">
          <span class="nh">นิยามที่ต้องจำ</span>
          <b>Product life cycle: The course of a product's sales and profits over its lifetime.</b><br>
          วงจรชีวิตผลิตภัณฑ์คือ<b>เส้นทางของยอดขายและกำไรของสินค้าตลอดอายุของมัน</b> · สังเกตว่านิยามพูดถึง<b>สองเส้นพร้อมกัน</b> คือยอดขายและกำไร และสองเส้นนี้<b>ไม่ขึ้นลงพร้อมกัน</b>
        </div>
        <figure class="fig">
          <div class="plate"><img loading="lazy" alt="Figure 9.2 Sales and Profits over the Product's Life from Inception to Decline" src="FIG2"></div>
          <figcaption><b>Figure 9.2</b> Sales and Profits over the Product&rsquo;s Life from Inception to Decline — เส้นสีเขียวน้ำทะเลคือ<b>ยอดขาย</b> เส้นสีแดงคือ<b>กำไร</b> · แกนตั้งเหนือศูนย์คือยอดขายและกำไร ใต้ศูนย์คือ<b>ขาดทุนหรือเงินลงทุน</b> · กล่องคำอธิบายซ้ายมือยกตัวอย่าง <b>Crayola Crayons</b> ที่อยู่มา<b>กว่า 115 ปี</b> และรักษาความสดของตราไว้ด้วยการเติมสินค้าใหม่เข้ามาต่อเนื่อง เช่น <b>Color Alive</b> ที่ให้เด็กระบายสีการ์ตูน สแกน แล้วดูแอปทำให้ภาพเคลื่อนไหว</figcaption>
        </figure>
        <h3>กดเลือกดูทีละขั้น</h3>
        <div class="step-wrap">
          <div class="steps" role="group" aria-label="เลือกขั้นของวงจรชีวิตผลิตภัณฑ์">
            <button type="button" class="step" data-plc="1" aria-pressed="true"><span class="sn">ขั้นที่ 1</span><span class="st">พัฒนาสินค้า</span></button>
            <button type="button" class="step" data-plc="2" aria-pressed="false"><span class="sn">ขั้นที่ 2</span><span class="st">แนะนำ</span></button>
            <button type="button" class="step" data-plc="3" aria-pressed="false"><span class="sn">ขั้นที่ 3</span><span class="st">เติบโต</span></button>
            <button type="button" class="step" data-plc="4" aria-pressed="false"><span class="sn">ขั้นที่ 4</span><span class="st">เติบโตเต็มที่</span></button>
            <button type="button" class="step" data-plc="5" aria-pressed="false"><span class="sn">ขั้นที่ 5</span><span class="st">ถดถอย</span></button>
          </div>
          <div class="step-out" id="plc-out"></div>
        </div>
        <div class="note warn">
          <span class="nh">สองจุดที่เส้นกำไรทำให้คนตอบผิด</span>
          <b>จุดที่หนึ่ง</b> ในขั้นพัฒนาสินค้า <b>ยอดขายเป็นศูนย์</b> แต่<b>ต้นทุนการลงทุนเพิ่มขึ้นเรื่อย ๆ</b> กำไรจึง<b>ติดลบ</b> และนี่คือช่วงที่เส้นสีแดงจมอยู่ใต้ศูนย์<br>
          <b>จุดที่สอง</b> <b>กำไรขึ้นถึงจุดสูงสุดก่อนยอดขาย</b> · ดูในภาพจะเห็นว่ายอดกำไรเริ่มลดลงตั้งแต่ปลายขั้นเติบโตเต็มที่ ขณะที่ยอดขายยังสูงอยู่ · เหตุผลคือการแข่งขันที่ดุขึ้นบังคับให้ลดราคาและเพิ่มงบส่งเสริมการตลาด
        </div>
      </div>
    </section>

    <section class="sec" id="m8-14">
      <div class="sec-h"><span class="sec-n">14</span><h2>ใช้แนวคิดวงจรชีวิตผลิตภัณฑ์กับอะไรได้บ้าง</h2></div>
      <div class="body">
        <div class="note warn">
          <span class="nh">ข้อเตือนที่สำคัญที่สุดของหัวข้อนี้</span>
          <b>สินค้าทุกตัวไม่ได้เดินครบทั้งห้าขั้นของ PLC</b> <span class="en">all products do not follow all five stages of the PLC</span><br>
          นักการตลาดใช้ PLC ได้ในฐานะ<b>กรอบสำหรับอธิบายว่าสินค้าและตลาดทำงานอย่างไร</b> <span class="en">a framework for describing how products and markets work</span> — ไม่ใช่กฎที่ทำนายอนาคตได้แม่นยำ · บางสินค้า<b>ตายเร็วมาก</b> ขณะที่บางสินค้า<b>อยู่ในขั้นเติบโตเต็มที่นานมาก</b> เช่นซอส <b>TABASCO&reg;</b>
        </div>
        <p class="lede">แนวคิด PLC ใช้อธิบายได้สามระดับ และ<b>สามระดับนี้มีอายุวงจรต่างกันชัดเจน</b></p>
        <div class="grid g3">
          <div class="card">
            <span class="cn">ระดับที่ 1</span>
            <div class="ct">ประเภทสินค้า <span class="en">Product class</span></div>
            <div class="cs"><b>มีวงจรชีวิตยาวที่สุด</b> <span class="en">has the longest life cycle</span><br>ตัวอย่างระดับนี้คือ <b>รถยนต์</b> หรือ <b>ยาสีฟัน</b> ซึ่งอยู่ในขั้นเติบโตเต็มที่มานานมาก</div>
          </div>
          <div class="card">
            <span class="cn">ระดับที่ 2</span>
            <div class="ct">รูปแบบสินค้า <span class="en">Product form</span></div>
            <div class="cs"><b>มีแนวโน้มเป็นรูปทรง PLC มาตรฐาน</b> <span class="en">tends to the standard PLC shape</span><br>คือขึ้น ๆ แล้วลงตามรูประฆังของ Figure 9.2 ชัดกว่าสองระดับที่เหลือ</div>
          </div>
          <div class="card">
            <span class="cn">ระดับที่ 3</span>
            <div class="ct">ตราสินค้า <span class="en">Brand</span></div>
            <div class="cs"><b>เปลี่ยนแปลงได้เร็ว</b> <span class="en">can change quickly</span> เพราะ<b>การโจมตีและการตอบโต้ของคู่แข่งที่เปลี่ยนไปเรื่อย ๆ</b> <span class="en">changing competitive attacks and responses</span></div>
          </div>
        </div>
        <div class="note key">
          <span class="nh">เรียงลำดับความยาวให้ถูก</span>
          <b>Product class ยาวที่สุด &gt; product form รูปทรงมาตรฐาน &gt; brand สั้นและผันผวนที่สุด</b><br>
          ตรรกะคือ ยิ่งเป็น<b>หมวดใหญ่</b>ยิ่งทนทานต่อการแข่งขัน เพราะคู่แข่งที่ออกของใหม่มาก็ยัง<b>อยู่ในหมวดเดียวกัน</b> · แต่ถ้าพูดถึง<b>ตราหนึ่งตรา</b> คู่แข่งแย่งลูกค้าไปได้โดยตรง วงจรจึงสั้นและกระชาก
        </div>
        <p>นอกจากสามระดับนี้ แนวคิด PLC ยังนำไปใช้กับสิ่งที่เรียกว่า <b>styles, fashions และ fads</b> ได้ด้วย ซึ่งอยู่ในหัวข้อถัดไป</p>
      </div>
    </section>

    <section class="sec" id="m8-15">
      <div class="sec-h"><span class="sec-n">15</span><h2>สไตล์ แฟชัน และแฟด</h2></div>
      <div class="body">
        <p class="lede">สามคำนี้<b>ต่างกันที่รูปทรงของเส้นยอดขาย</b> ไม่ใช่ที่ประเภทของสินค้า · ข้อสอบจะให้สถานการณ์มาแล้วถามว่าเป็นอะไร ให้ดูที่<b>เส้นขึ้นเร็วแค่ไหนและลงแบบไหน</b></p>
        <div class="grid g3">
          <div class="card">
            <span class="cn">แบบที่ 1</span>
            <div class="ct">สไตล์ <span class="en">Style</span></div>
            <div class="cs"><b>รูปแบบการแสดงออกที่เป็นพื้นฐานและมีเอกลักษณ์</b> <span class="en">a basic and distinctive mode of expression</span><br>เส้นยอดขาย<b>ขึ้นแล้วอยู่ยาว มีขึ้นมีลงเป็นลูกคลื่น และกลับมาได้อีก</b> เพราะสไตล์ไม่เคยหายไปจริง ๆ แค่หมุนเวียนความนิยม</div>
          </div>
          <div class="card">
            <span class="cn">แบบที่ 2</span>
            <div class="ct">แฟชัน <span class="en">Fashion</span></div>
            <div class="cs"><b>สไตล์ที่กำลังได้รับการยอมรับหรือเป็นที่นิยมอยู่ในขณะนั้นในวงการใดวงการหนึ่ง</b> <span class="en">a currently accepted or popular style in a given field</span><br>เส้นยอดขาย<b>ค่อย ๆ ขึ้น ถึงจุดสูงสุด แล้วค่อย ๆ ลง</b> เป็นโค้งนุ่ม ๆ ลูกเดียว</div>
          </div>
          <div class="card">
            <span class="cn">แบบที่ 3</span>
            <div class="ct">แฟด <span class="en">Fad</span></div>
            <div class="cs"><b>ช่วงเวลาสั้น ๆ ที่ยอดขายสูงผิดปกติ ขับเคลื่อนด้วยความคลั่งไคล้ของผู้บริโภคและความนิยมเฉพาะหน้าในตัวสินค้าหรือตรา</b><br>เส้นยอดขาย<b>พุ่งขึ้นชัน แหลม แล้วทรุดลงเร็วพอ ๆ กัน</b></div>
          </div>
        </div>
        <figure class="fig">
          <div class="plate"><img loading="lazy" alt="Figure 8.3 Styles, Fashions, and Fads" src="FIG3"></div>
          <figcaption><b>Figure 8.3</b> Styles, Fashions, and Fads — ทั้งสามกราฟมีแกนเดียวกันคือ <b>Sales</b> กับ <b>Time</b> แต่รูปทรงต่างกันสิ้นเชิง · <b>Style</b> เส้นเขียวขึ้นแล้วเป็นลูกคลื่นวนกลับขึ้นได้อีก · <b>Fashion</b> เส้นดำเป็นโค้งลูกเดียว ขึ้นช้าลงช้า · <b>Fad</b> เส้นแดงเป็นยอดแหลมสูงแล้วดิ่งลงเกือบเป็นเส้นตรง</figcaption>
        </figure>
        <div class="note key">
          <span class="nh">วิธีแยกให้เร็วในห้องสอบ</span>
          ถามตัวเองสองคำถาม — <b>มันกลับมาได้ไหม</b> ถ้าได้คือ <b>style</b> · ถ้าไม่ได้ ถามต่อว่า<b>มันลงเร็วพอ ๆ กับที่ขึ้นหรือเปล่า</b> ถ้าใช่คือ <b>fad</b> ถ้าค่อย ๆ ลงคือ <b>fashion</b><br>
          สังเกตจากนิยามด้วยว่า <b>fashion คือ style ที่กำลังนิยม</b> แปลว่าสองคำนี้<b>ซ้อนกันอยู่</b> ไม่ได้แยกขาดจากกัน
        </div>
      </div>
    </section>

    <section class="sec" id="m8-16">
      <div class="sec-h"><span class="sec-n">16</span><h2>ขั้นแนะนำและขั้นเติบโต</h2></div>
      <div class="body">
        <div class="grid g2">
          <div class="card">
            <span class="cn">ขั้นที่ 2 ของ PLC</span>
            <div class="ct">ขั้นแนะนำ <span class="en">Introduction stage</span></div>
            <div class="cs">
              <ul class="list">
                <li><b>ยอดขายเติบโตช้า</b> <span class="en">slow sales growth</span></li>
                <li><b>กำไรน้อยมากหรือไม่มีเลย</b> <span class="en">little or no profit</span></li>
                <li><b>ค่าใช้จ่ายด้านการจัดจำหน่ายและการส่งเสริมการตลาดสูง</b> <span class="en">high distribution and promotion expenses</span></li>
              </ul>
              เหตุผลที่กำไรยังไม่มา ไม่ใช่เพราะสินค้าไม่ดี แต่เพราะ<b>ต้องใช้เงินมากเพื่อผลักสินค้าเข้าช่องทางและให้คนรู้จัก</b> ขณะที่ยอดขายยังน้อย
            </div>
          </div>
          <div class="card">
            <span class="cn">ขั้นที่ 3 ของ PLC</span>
            <div class="ct">ขั้นเติบโต <span class="en">Growth stage</span></div>
            <div class="cs">
              <ul class="list">
                <li><b>ยอดขายเพิ่มขึ้น</b> <span class="en">sales increase</span></li>
                <li><b>คู่แข่งรายใหม่เข้าสู่ตลาด</b> <span class="en">new competitors enter the market</span></li>
                <li><b>กำไรเพิ่มขึ้น</b> <span class="en">profits increase</span></li>
                <li><b>เกิดการประหยัดจากขนาด</b> <span class="en">economies of scale</span></li>
                <li><b>ให้ความรู้แก่ผู้บริโภค</b> <span class="en">consumer education</span></li>
                <li><b>ลดราคาลงเพื่อดึงผู้ซื้อเพิ่ม</b> <span class="en">lowering prices to attract more buyers</span></li>
              </ul>
            </div>
          </div>
        </div>
        <div class="note">
          <span class="nh">เหตุผลที่กำไรเพิ่มในขั้นเติบโตทั้งที่ลดราคา</span>
          ดูสองข้อนี้คู่กัน — <b>ลดราคา</b> กับ <b>economies of scale</b> · ราคาต่อหน่วยลดลงก็จริง แต่<b>ต้นทุนต่อหน่วยลดลงเร็วกว่า</b>เพราะผลิตเยอะขึ้นมาก และ<b>ค่าส่งเสริมการตลาดถูกเฉลี่ยลงบนยอดขายที่ใหญ่ขึ้น</b> กำไรรวมจึงยังเพิ่ม
        </div>
        <div class="note warn">
          <span class="nh">ทางแยกที่บริษัทต้องเลือกในขั้นเติบโต</span>
          บริษัทต้องเลือกระหว่าง<b>ส่วนแบ่งตลาดสูง</b>กับ<b>กำไรปัจจุบันสูง</b> · การทุ่มเงินกับการปรับปรุงสินค้า การส่งเสริมการตลาด และการจัดจำหน่าย จะ<b>ยึดตำแหน่งที่เหนือกว่าไว้ได้</b> แต่ต้อง<b>ยอมสละกำไรสูงสุดในตอนนี้</b>เพื่อแลกกับกำไรที่มากกว่าในขั้นถัดไป · ตาราง 9.2 ในหัวข้อที่ 20 สรุปไว้ว่าวัตถุประสงค์ของขั้นเติบโตคือ <b>maximize market share</b> ไม่ใช่ maximize profit
        </div>
      </div>
    </section>

    <section class="sec" id="m8-17">
      <div class="sec-h"><span class="sec-n">17</span><h2>ขั้นเติบโตเต็มที่ · สามกลยุทธ์การปรับ</h2></div>
      <div class="body">
        <p class="lede">ขั้นนี้<b>ยาวที่สุดในวงจร</b> และเป็นขั้นที่สินค้าส่วนใหญ่ในตลาดอยู่กัน ดังนั้นงานของนักการตลาดส่วนใหญ่จึงเป็น<b>งานของขั้นนี้</b></p>
        <h3>ลักษณะของขั้นเติบโตเต็มที่ <span class="en">Maturity stage</span></h3>
        <ul class="list">
          <li><b>ยอดขายชะลอตัว</b> <span class="en">slowdown in sales</span></li>
          <li><b>มีสินค้าทดแทนเข้ามา</b> <span class="en">substitute products</span></li>
          <li><b>ต้องเพิ่มการส่งเสริมการตลาดและงานวิจัยและพัฒนาเพื่อประคองยอดขายและกำไร</b> <span class="en">increased promotion and R&amp;D to support sales and profits</span></li>
        </ul>
        <div class="note">
          <span class="nh">ตัวอย่างในสไลด์ · Quaker</span>
          ตราอายุ <b>140 ปี</b> อย่าง <b>Quaker</b> ทำตัว<b>ไม่สมวัยเลย</b> · ผ่านสิ่งที่แบรนด์เรียกว่า <b>&ldquo;oatsperiments&rdquo;</b> แบรนด์ได้<b>เติมสินค้าใหม่ร่วมสมัยเข้ามาเต็มตู้ครัว</b> พร้อมกับ<b>วิธีการตลาดสมัยใหม่อีกชุดใหญ่</b> · นี่คือภาพของการบริหารวงจรชีวิตผลิตภัณฑ์ในขั้นเติบโตเต็มที่
        </div>
        <h3>สามกลยุทธ์การปรับ <span class="en">Modification strategies</span></h3>
        <p class="lede">เมื่อยอดขายชะลอ มีสามทางเลือก และ<b>ทั้งสามทางมีคำว่า modify เหมือนกัน ต่างกันที่ปรับอะไร</b></p>
        <div class="grid g3">
          <div class="card">
            <span class="cn">กลยุทธ์ที่ 1</span>
            <div class="ct">ปรับตลาด <span class="en">Modify the market</span></div>
            <div class="cs"><b>เป้าหมาย</b> เพิ่มการบริโภคสินค้าตัวเดิม <span class="en">increase the consumption of the current product</span>
              <ul class="list">
                <li><b>หาผู้ใช้กลุ่มใหม่และส่วนตลาดใหม่</b></li>
                <li><b>วางตำแหน่งตราใหม่</b>ให้ดึงดูดส่วนตลาดที่ใหญ่กว่าหรือโตเร็วกว่า</li>
                <li><b>หาวิธีเพิ่มอัตราการใช้ในกลุ่มลูกค้าปัจจุบัน</b></li>
              </ul>
              <b>ตัวสินค้าไม่เปลี่ยน · คนที่ใช้หรือวิธีใช้เปลี่ยน</b>
            </div>
          </div>
          <div class="card">
            <span class="cn">กลยุทธ์ที่ 2</span>
            <div class="ct">ปรับสินค้า <span class="en">Modify the product</span></div>
            <div class="cs"><b>เป้าหมาย</b> เปลี่ยนคุณลักษณะเช่น <b>คุณภาพ คุณสมบัติ รูปแบบ หรือบรรจุภัณฑ์</b> เพื่อดึงผู้ใช้ใหม่และกระตุ้นให้ใช้มากขึ้น
              <ul class="list">
                <li><b>ปรับปรุงความทนทาน ความน่าเชื่อถือ ความเร็ว รสชาติ</b></li>
                <li><b>ปรับปรุงรูปลักษณ์ให้น่าดึงดูดขึ้น</b></li>
                <li><b>เพิ่มคุณสมบัติใหม่</b></li>
              </ul>
              <b>ตัวสินค้าเปลี่ยน · ส่วนประสมการตลาดที่เหลือยังเหมือนเดิม</b>
            </div>
          </div>
          <div class="card">
            <span class="cn">กลยุทธ์ที่ 3</span>
            <div class="ct">ปรับส่วนประสมการตลาด <span class="en">Modify the marketing mix</span></div>
            <div class="cs"><b>เป้าหมาย</b> เพิ่มยอดขายด้วยการ<b>เปลี่ยนองค์ประกอบของส่วนประสมการตลาดหนึ่งตัวหรือมากกว่า</b>
              <ul class="list">
                <li><b>เสนอบริการใหม่หรือบริการที่ดีขึ้น</b></li>
                <li><b>ลดราคา</b></li>
                <li><b>ทำแคมเปญโฆษณาที่ดีกว่าเดิม</b></li>
                <li><b>เข้าสู่ช่องทางตลาดใหม่</b></li>
              </ul>
              <b>ตัวสินค้าไม่เปลี่ยน · ราคา ช่องทาง หรือการส่งเสริมการตลาดเปลี่ยน</b>
            </div>
          </div>
        </div>
        <div class="note warn">
          <span class="nh">เส้นแบ่งที่ต้องชัด · modify the market เทียบ modify the marketing mix</span>
          สองตัวนี้ชื่อคล้ายกันจนสับสนบ่อยที่สุดในบทนี้<br>
          <b>Modify the market</b> คำถามคือ <b>ใครใช้ และใช้บ่อยแค่ไหน</b> — เปลี่ยน<b>กลุ่มเป้าหมายหรือพฤติกรรมการใช้</b><br>
          <b>Modify the marketing mix</b> คำถามคือ <b>เราใช้เครื่องมือ 4Ps อย่างไร</b> — เปลี่ยน<b>ราคา ช่องทาง โฆษณา หรือบริการ</b><br>
          ตัวอย่างชี้ขาด การบอกให้ลูกค้าเดิม<b>แปรงฟันวันละสามครั้งแทนสองครั้ง</b> คือ modify the market · การ<b>ลดราคายาสีฟันลง 20%</b> คือ modify the marketing mix
        </div>
      </div>
    </section>

    <section class="sec" id="m8-18">
      <div class="sec-h"><span class="sec-n">18</span><h2>ตัวอย่างการปรับในตลาดไทย</h2></div>
      <div class="body">
        <p class="lede">สไลด์ยกตัวอย่างแบรนด์ไทยสามกรณีประกบสามกลยุทธ์ข้างต้น · หน้านี้<b>เล่าใจความขึ้นใหม่เป็นภาษาไทยพร้อมระบุที่มา</b> ไม่ได้นำภาพโฆษณาต้นฉบับมาลง</p>
        <div class="grid g2">
          <div class="card">
            <span class="cn">กรณีที่ 1</span>
            <div class="ct">Dentiste&rsquo; · ยาสีฟัน</div>
            <div class="cs">สไลด์เทียบแคมเปญของแบรนด์เดียวกันสองยุค<br>
              <b>ยุคแรก</b> ตัวสินค้าหลักคือ <b>Dentiste&rsquo; Plus White Nighttime</b> วางตำแหน่งว่าเป็นยาสีฟันสำหรับ<b>แก้ปัญหากลิ่นปากยามเช้าให้คู่รัก</b> สื่อสารด้วยแฮชแท็ก <b>#HealthyRelationship</b> โดยชูว่าลดแบคทีเรียในช่องปากด้วยสารสกัดจาก<b>สมุนไพร 14 ชนิด</b><br>
              <b>ยุคหลัง</b> แบรนด์ออก <b>Dentiste&rsquo; Anticavity Max Fluoride</b> พร้อมเปลี่ยนไปใช้พรีเซนเตอร์ระดับสากลและเปลี่ยนสารที่สื่อเป็น<b>ฟันขาว ยิ้มสวย มั่นใจ</b><br>
              <b>อ่านเป็นกลยุทธ์อะไร</b> นี่คือตัวอย่างของการ<b>วางตำแหน่งตราใหม่ให้จับส่วนตลาดที่ใหญ่กว่า</b> ซึ่งอยู่ใต้ <b>modify the market</b> และมี<b>การปรับตัวสินค้า</b>เข้ามาประกอบด้วย<br>
              <span class="en">ที่มาที่สไลด์อ้าง central.co.th และคลิปโฆษณาของแบรนด์บน YouTube</span></div>
          </div>
          <div class="card">
            <span class="cn">กรณีที่ 2</span>
            <div class="ct">Sappe &times; ตราตะขาบ · มิถุนายน 2564 ถึง 2565</div>
            <div class="cs"><b>เซ็ปเป้</b> ร่วมมือกับ<b>ยาอมตราตะขาบ</b> ออกเครื่องดื่มรสใหม่ที่ผสม<b>หล่อฮังก๊วย ชะเอมเทศ มะนาว และมะขามป้อม</b> ชู <b>วิตามินซี 100%</b> และสื่อสารด้วยแฮชแท็ก <b>#ระคายคอCALLตะขาบ</b><br>
              <b>อ่านเป็นกลยุทธ์อะไร</b> เป็นการ<b>ปรับตัวสินค้า</b> <span class="en">modify the product</span> โดยเพิ่ม<b>รสชาติและส่วนผสมใหม่</b> พร้อมกับการ<b>ร่วมแบรนด์</b>ซึ่งยืมภาพจำเรื่องการดูแลลำคอจากอีกแบรนด์มาใช้<br>
              <span class="en">ที่มาที่สไลด์อ้าง sappe.com ข่าวประชาสัมพันธ์เดือนกรกฎาคม 2564</span></div>
          </div>
          <div class="card">
            <span class="cn">กรณีที่ 3</span>
            <div class="ct">ปีโป้ &times; M-150 · กรกฎาคม 2564</div>
            <div class="cs"><b>เยลลี่ปีโป้</b> ของ EURO จับมือกับเครื่องดื่ม <b>M-150</b> ออก<b>รุ่นจำกัด กลิ่น M-150</b> บรรจุกล่องละ <b>50 ถ้วย</b> โดยสื่อสารว่าสองแบรนด์ที่<b>อยู่คู่คนไทยมากว่า 30 ปี</b>มาร่วมมือกัน<br>
              <b>อ่านเป็นกลยุทธ์อะไร</b> เป็นการ<b>ปรับตัวสินค้า</b>ด้วย<b>รสชาติใหม่และบรรจุภัณฑ์ใหม่</b> พร้อมใช้ความเป็น<b>รุ่นจำกัด</b>สร้างเหตุผลให้ลูกค้าเดิมกลับมาซื้ออีกครั้ง ซึ่งเข้ากับเป้าหมาย<b>เพิ่มอัตราการใช้ในกลุ่มลูกค้าปัจจุบัน</b><br>
              <span class="en">ที่มาที่สไลด์อ้าง brandbuffet.in.th ข่าวเดือนกรกฎาคม 2564</span></div>
          </div>
        </div>
        <div class="note key">
          <span class="nh">สิ่งที่สามกรณีนี้มีร่วมกัน</span>
          ทั้งสามแบรนด์<b>ไม่ใช่สินค้าใหม่</b> แต่เป็นสินค้าที่อยู่ในขั้น<b>เติบโตเต็มที่</b>มานาน · สิ่งที่ทำจึงไม่ใช่การเปิดตลาดใหม่ แต่คือ<b>การหาเหตุผลใหม่ให้คนซื้อของเดิม</b> ซึ่งเป็นสาระทั้งหมดของสามกลยุทธ์การปรับ
        </div>
      </div>
    </section>

    <section class="sec" id="m8-19">
      <div class="sec-h"><span class="sec-n">19</span><h2>ขั้นถดถอย · สามทางเลือก</h2></div>
      <div class="body">
        <p class="lede">เมื่อยอดขายตกและกำไรลดลง บริษัทมี<b>สามทางเลือก</b>เท่านั้น และทั้งสามทางเป็นการตัดสินใจที่ถูกต้องได้ทั้งหมด ขึ้นกับสถานการณ์</p>
        <div class="grid g3">
          <div class="card">
            <span class="cn">ทางเลือกที่ 1</span>
            <div class="ct">คงสินค้าไว้ <span class="en">Maintain</span></div>
            <div class="cs">เก็บสินค้าไว้<b>ด้วยความหวังว่าจะดันมันกลับขึ้นไปสู่ขั้นเติบโตของวงจรชีวิตได้อีกครั้ง</b> <span class="en">hopes of moving it back into the growth stage of the PLC</span><br>เป็นทางเลือกที่<b>ลงทุนต่อ</b> จึงเสี่ยงที่สุด</div>
          </div>
          <div class="card">
            <span class="cn">ทางเลือกที่ 2</span>
            <div class="ct">รีดกำไร <span class="en">Harvest</span></div>
            <div class="cs"><b>ลดต้นทุนต่าง ๆ ลง</b> แล้ว<b>หวังว่ายอดขายจะยังทรงอยู่ได้</b> <span class="en">reducing various costs, hoping that sales hold up</span><br>เป็นการ<b>เก็บกำไรก้อนสุดท้าย</b>จากสินค้าที่ยังมีลูกค้าเหลืออยู่ โดยไม่ลงทุนเพิ่ม</div>
          </div>
          <div class="card">
            <span class="cn">ทางเลือกที่ 3</span>
            <div class="ct">เลิกสินค้า <span class="en">Drop</span></div>
            <div class="cs"><b>ถอดสินค้าออกจากสายผลิตภัณฑ์</b><br>ทำได้ทั้งการ<b>ขายให้บริษัทอื่น</b>หรือ<b>เลิกผลิตไปเลย</b> · เชื่อมกับการตัดสินใจเรื่อง<b>ความยาวของสายผลิตภัณฑ์</b>ในบทที่ 7</div>
          </div>
        </div>
        <div class="note">
          <span class="nh">ทำไมบริษัทถึงลังเลที่จะเลิกสินค้า</span>
          สินค้าที่อ่อนแรงมัก<b>กินเวลาผู้บริหารมากเกินสัดส่วนของยอดขาย</b> ต้องปรับราคาและสต็อกบ่อย ต้องใช้งบโฆษณาและพนักงานขายที่เอาไปใช้กับสินค้าที่ทำกำไรได้มากกว่า และ<b>ทำให้ภาพลักษณ์ของบริษัทเสีย</b> · ตาราง 9.2 ในหัวข้อถัดไปจึงระบุวัตถุประสงค์ของขั้นนี้ไว้ว่า <b>ลดค่าใช้จ่ายและรีดเอาประโยชน์จากตราให้หมด</b> <span class="en">reduce expenditure and milk the brand</span>
        </div>
      </div>
    </section>

    <section class="sec" id="m8-20">
      <div class="sec-h"><span class="sec-n">20</span><h2>ตาราง 9.2 · สรุปทั้งวงจรในหน้าเดียว</h2></div>
      <div class="body">
        <p class="lede">ตารางนี้คือ<b>ตัวที่ออกสอบมากที่สุดของครึ่งหลัง</b> เพราะรวมทั้งลักษณะ วัตถุประสงค์ และกลยุทธ์ 4Ps ของทั้งสี่ขั้นไว้ในที่เดียว · อ่านแบบ<b>ไล่ตามแถว</b>จะเห็นตรรกะได้ชัดกว่าไล่ตามคอลัมน์</p>
        <h3>ส่วนที่หนึ่ง · ลักษณะ <span class="en">Characteristics</span></h3>
        <div class="tw"><table class="tbl">
          <thead><tr><th></th><th>Introduction<br>ขั้นแนะนำ</th><th>Growth<br>ขั้นเติบโต</th><th>Maturity<br>ขั้นเติบโตเต็มที่</th><th>Decline<br>ขั้นถดถอย</th></tr></thead>
          <tbody>
            <tr><td class="k">Sales<br>ยอดขาย</td><td>ยอดขายต่ำ<br><span class="en">low sales</span></td><td>ยอดขายเพิ่มอย่างรวดเร็ว<br><span class="en">rapidly rising</span></td><td>ยอดขายถึงจุดสูงสุด<br><span class="en">peak sales</span></td><td>ยอดขายลดลง<br><span class="en">declining sales</span></td></tr>
            <tr><td class="k">Costs<br>ต้นทุน</td><td>ต้นทุนต่อลูกค้าสูง<br><span class="en">high cost per customer</span></td><td>ต้นทุนต่อลูกค้าปานกลาง<br><span class="en">average</span></td><td>ต้นทุนต่อลูกค้าต่ำ<br><span class="en">low</span></td><td>ต้นทุนต่อลูกค้าต่ำ<br><span class="en">low</span></td></tr>
            <tr><td class="k">Profits<br>กำไร</td><td>ติดลบหรือต่ำ<br><span class="en">negative or low</span></td><td>กำไรเพิ่มขึ้น<br><span class="en">rising profits</span></td><td>กำไรสูง<br><span class="en">high profits</span></td><td>กำไรลดลง<br><span class="en">declining profits</span></td></tr>
            <tr><td class="k">Customers<br>ลูกค้า</td><td>Innovators</td><td>Early adopters</td><td>Mainstream adopters</td><td>Lagging adopters</td></tr>
            <tr><td class="k">Competitors<br>คู่แข่ง</td><td>มีน้อยราย<br><span class="en">few</span></td><td>จำนวนเพิ่มขึ้น<br><span class="en">growing number</span></td><td>จำนวนคงที่และเริ่มลดลง<br><span class="en">stable number beginning to decline</span></td><td>จำนวนลดลง<br><span class="en">declining number</span></td></tr>
          </tbody>
        </table></div>
        <h3>ส่วนที่สอง · วัตถุประสงค์ทางการตลาด <span class="en">Marketing objectives</span></h3>
        <div class="tw"><table class="tbl">
          <thead><tr><th>Introduction</th><th>Growth</th><th>Maturity</th><th>Decline</th></tr></thead>
          <tbody>
            <tr><td><b>สร้างความผูกพันกับสินค้าและทำให้เกิดการทดลองใช้</b><br><span class="en">create product engagement and trial</span></td><td><b>เพิ่มส่วนแบ่งตลาดให้มากที่สุด</b><br><span class="en">maximize market share</span></td><td><b>เพิ่มกำไรให้มากที่สุดพร้อมกับปกป้องส่วนแบ่งตลาด</b><br><span class="en">maximize profit while defending market share</span></td><td><b>ลดค่าใช้จ่ายและรีดเอาประโยชน์จากตรา</b><br><span class="en">reduce expenditure and milk the brand</span></td></tr>
          </tbody>
        </table></div>
        <div class="note key">
          <span class="nh">แถวนี้คือหัวใจของตารางทั้งตาราง</span>
          <b>ขั้นเติบโตเน้นส่วนแบ่งตลาด · ขั้นเติบโตเต็มที่จึงค่อยเน้นกำไร</b> · ถ้าสลับสองคำนี้ผิด คำตอบของคำถามเรื่องกลยุทธ์ 4Ps ในส่วนที่สามจะผิดตามไปทั้งแถว
        </div>
        <h3>ส่วนที่สาม · กลยุทธ์ <span class="en">Strategies</span></h3>
        <div class="tw"><table class="tbl">
          <thead><tr><th></th><th>Introduction</th><th>Growth</th><th>Maturity</th><th>Decline</th></tr></thead>
          <tbody>
            <tr><td class="k">Product<br>ผลิตภัณฑ์</td><td>เสนอสินค้าพื้นฐาน<br><span class="en">offer a basic product</span></td><td>เสนอส่วนต่อขยายของสินค้า บริการ และการรับประกัน<br><span class="en">product extensions, service, and warranty</span></td><td>แตกตราและรุ่นให้หลากหลาย<br><span class="en">diversify brand and models</span></td><td>ทยอยเลิกรายการที่อ่อนแรง<br><span class="en">phase out weak items</span></td></tr>
            <tr><td class="k">Price<br>ราคา</td><td>ใช้ต้นทุนบวกกำไร<br><span class="en">use cost-plus</span></td><td>ตั้งราคาเพื่อเจาะตลาด<br><span class="en">price to penetrate market</span></td><td>ตั้งราคาให้เท่าหรือต่ำกว่าคู่แข่ง<br><span class="en">price to match or beat competitors</span></td><td>ลดราคา<br><span class="en">cut price</span></td></tr>
            <tr><td class="k">Distribution<br>การจัดจำหน่าย</td><td>สร้างการจัดจำหน่ายแบบเลือกสรร<br><span class="en">build selective distribution</span></td><td>สร้างการจัดจำหน่ายแบบทั่วถึง<br><span class="en">build intensive distribution</span></td><td>สร้างการจัดจำหน่ายให้ทั่วถึงยิ่งขึ้น<br><span class="en">build more intensive distribution</span></td><td>กลับไปเลือกสรร ทยอยตัดร้านที่ไม่ทำกำไร<br><span class="en">go selective, phase out unprofitable outlets</span></td></tr>
            <tr><td class="k">Advertising<br>การโฆษณา</td><td>สร้างการรับรู้ในสินค้าในกลุ่มผู้รับนวัตกรรมช่วงต้นและตัวแทนจำหน่าย<br><span class="en">build product awareness among early adopters and dealers</span></td><td>สร้างความผูกพัน ความสนใจ และการรับรู้ในตลาดมวลชน<br><span class="en">build engagement and interest in the mass market</span></td><td>เน้นความแตกต่างและประโยชน์ของตรา<br><span class="en">stress brand differences and benefits</span></td><td>ลดลงเหลือเท่าที่จำเป็นเพื่อรักษาลูกค้าที่ภักดีอย่างแรงกล้า<br><span class="en">reduce to level needed to retain hardcore loyals</span></td></tr>
            <tr><td class="k">Sales promotion<br>การส่งเสริมการขาย</td><td>ใช้การส่งเสริมการขายอย่างหนักเพื่อล่อให้ทดลองใช้<br><span class="en">use heavy sales promotion to entice trial</span></td><td>ลดลง เพื่อฉวยประโยชน์จากอุปสงค์ที่แรงอยู่แล้ว<br><span class="en">reduce to take advantage of heavy consumer demand</span></td><td>เพิ่มขึ้น เพื่อกระตุ้นให้เปลี่ยนตรา<br><span class="en">increase to encourage brand switching</span></td><td>ลดลงเหลือระดับต่ำสุด<br><span class="en">reduce to minimal level</span></td></tr>
          </tbody>
        </table></div>
        <p class="cap">ที่มา <b>Table 9.2</b> Summary of Product Life-Cycle Characteristics, Objectives, and Strategies · อ้างอิง Philip Kotler และ Kevin Lane Keller, <i>Marketing Management</i>, ฉบับพิมพ์ครั้งที่ 15 (Hoboken, NJ: Pearson Education, 2016), หน้า 358 · ตารางนี้พิมพ์ขึ้นใหม่เป็นตารางเว็บพร้อมคำแปลไทย ไม่ได้ฝังภาพสแกน จะได้ค้นหาได้และอ่านบนจอเล็กได้</p>
        <div class="note warn">
          <span class="nh">สามจุดในตารางที่ตอบผิดบ่อยที่สุด</span>
          <b>หนึ่ง · การส่งเสริมการขายในขั้นเติบโต &ldquo;ลดลง&rdquo;</b> ไม่ใช่เพิ่มขึ้น เพราะอุปสงค์แรงอยู่แล้วไม่ต้องล่อ · แล้ว<b>กลับมาเพิ่มอีกครั้งในขั้นเติบโตเต็มที่</b>เพื่อแย่งลูกค้าจากคู่แข่ง<br>
          <b>สอง · ต้นทุนต่อลูกค้าในขั้นแนะนำ &ldquo;สูง&rdquo;</b> ทั้งที่ยอดขายต่ำ เพราะต้นทุนคงที่ถูกหารด้วยจำนวนลูกค้าที่น้อยมาก<br>
          <b>สาม · คู่แข่งในขั้นเติบโตเต็มที่คือ &ldquo;คงที่และเริ่มลดลง&rdquo;</b> ไม่ใช่มากที่สุด · จุดที่คู่แข่งเพิ่มเร็วที่สุดคือ<b>ขั้นเติบโต</b>
        </div>
      </div>
    </section>

    <section class="sec" id="m8-21">
      <div class="sec-h"><span class="sec-n">21</span><h2>สองประเด็นเพิ่มเติม</h2></div>
      <div class="body">
        <p class="lede">ปิดท้ายบทด้วยสองเรื่องที่ตำราเรียกว่า <b>additional product and service considerations</b> ซึ่งเป็นวัตถุประสงค์การเรียนรู้ข้อ 8.4</p>
        <h3>ประเด็นที่หนึ่ง · การตัดสินใจเรื่องสินค้ากับความรับผิดชอบต่อสังคม</h3>
        <p>บริษัทต้องพิจารณาสี่เรื่องต่อไปนี้</p>
        <ul class="list">
          <li><b>ประเด็นด้านนโยบายสาธารณะ</b> <span class="en">public policy issues</span></li>
          <li><b>กฎระเบียบเกี่ยวกับการพัฒนา การได้มา หรือการเลิกสินค้า</b> <span class="en">regulations regarding developing, acquiring or dropping products</span></li>
          <li><b>การคุ้มครองสิทธิบัตร</b> <span class="en">patent protection</span></li>
          <li><b>คุณภาพ ความปลอดภัย และการรับประกันสินค้า</b> <span class="en">product quality, safety, and product warranties</span></li>
        </ul>
        <div class="note">
          <span class="nh">สังเกตว่าข้อสองครอบคลุมทั้งบท</span>
          คำว่า <b>developing, acquiring or dropping</b> ตรงกับสามเรื่องที่บทนี้สอนพอดี — <b>developing</b> คือกระบวนการแปดขั้น · <b>acquiring</b> คือทางที่ 1 ในหัวข้อแรก · <b>dropping</b> คือทางเลือกที่ 3 ของขั้นถดถอย · ทั้งสามเรื่องมีกฎหมายกำกับอยู่ ไม่ใช่เรื่องที่บริษัทตัดสินใจได้ตามใจล้วน ๆ
        </div>
        <h3>ประเด็นที่สอง · การตลาดสินค้าและบริการระหว่างประเทศ</h3>
        <ul class="list">
          <li><b>ตัดสินใจว่าจะนำสินค้าและบริการใดเข้าสู่ประเทศใด</b> <span class="en">what products and services to introduce in which countries</span></li>
          <li><b>มาตรฐานเดียวกันทั้งโลก หรือปรับให้เข้ากับแต่ละที่</b> <span class="en">standardization versus customization</span></li>
          <li><b>บรรจุภัณฑ์และฉลาก</b> <span class="en">packaging and labeling</span></li>
          <li><b>ขนบธรรมเนียม ค่านิยม และกฎหมาย</b> <span class="en">customs, values, laws</span></li>
        </ul>
        <div class="note key">
          <span class="nh">ตัวอย่างในสไลด์ · McDonald&rsquo;s ในฝรั่งเศส</span>
          ด้วยการ<b>ปรับเมนูและการดำเนินงานให้เข้ากับความต้องการ ความชอบ และวัฒนธรรมของผู้บริโภคชาวฝรั่งเศส</b> McDonald&rsquo;s ทำให้ฝรั่งเศสกลายเป็น<b>ตลาดที่ทำกำไรสูงเป็นอันดับสองของโลก</b>ของบริษัท<br>
          นี่คือตัวอย่างของการเลือก <b>customization</b> แทน <b>standardization</b> และเป็นคำตอบว่าทำไมประเด็นที่สองนี้ถึงไม่ใช่แค่เรื่องโลจิสติกส์ แต่เป็น<b>การตัดสินใจเชิงกลยุทธ์</b>
        </div>
        <div class="note">
          <span class="nh">ปิดบท</span>
          บทที่ 7 ตอบว่า<b>สินค้าคืออะไรและตัดสินใจอะไรกับมัน</b> · บทที่ 8 ตอบว่า<b>สินค้าเกิดขึ้นมาอย่างไรและต้องดูแลมันอย่างไรตลอดชีวิตของมัน</b> · สองบทนี้รวมกันคือ <b>P ตัวแรกของ 4Ps</b> ทั้งตัว และเป็นขั้นที่ 3 ของกระบวนการการตลาดห้าขั้นในบทที่ 1
        </div>
      </div>
    </section>
  </div>
"""

PANEL = PANEL.replace(u'src="FIG1"', u'src="%s"' % F1) \
             .replace(u'src="FIG2"', u'src="%s"' % F2) \
             .replace(u'src="FIG3"', u'src="%s"' % F3)


# ───────────────────── สคริปต์ของแผงเลือกขั้นตอน ─────────────────────

STEPJS = u"""
  /* บทที่ 8 · แปดขั้นของการพัฒนาสินค้าใหม่ */
  var NPD = {
    '1': {th:'การสร้างความคิด', en:'Idea generation',
      items:['การ<b>ค้นหาความคิดเรื่องสินค้าใหม่อย่างเป็นระบบ</b>',
             '<b>แหล่งภายใน</b> งานวิจัยและพัฒนา ผู้บริหารและพนักงาน และ intrapreneurs เช่น hackathon ของ Facebook',
             '<b>แหล่งภายนอก</b> ผู้จัดจำหน่าย ผู้จัดหาวัตถุดิบ คู่แข่ง นิตยสารและงานแสดงสินค้า ลูกค้า และ crowdsourcing',
             'ขั้นเดียวในแปดขั้นที่<b>ยิ่งได้มากยิ่งดี</b>']},
    '2': {th:'การกลั่นกรองความคิด', en:'Idea screening',
      items:['<b>จับความคิดที่ดีให้เจอ และทิ้งความคิดที่แย่ให้เร็วที่สุด</b>',
             'ใช้กรอบ <b>R-W-W</b> คือ <b>Is it real? Can we win? Is it worth doing?</b>',
             'ด่าน<b>ลดจำนวน</b>ด่านแรกของกระบวนการ']},
    '3': {th:'การพัฒนาและทดสอบแนวคิดสินค้า', en:'Concept development and testing',
      items:['แยกสามคำให้ขาด <b>product idea</b> ความคิดดิบ · <b>product concept</b> ฉบับละเอียดที่เขียนด้วยภาษาผู้บริโภค · <b>product image</b> การรับรู้ของผู้บริโภค',
             '<b>Concept testing</b> คือทดสอบแนวคิดกับกลุ่มผู้บริโภคเป้าหมาย ด้วย<b>คำบรรยาย ภาพ หรือแบบจำลอง</b> แล้วถามปฏิกิริยา',
             'ผลลัพธ์คือ<b>เลือกแนวคิดที่ดีที่สุดมาหนึ่งอัน</b>จากหลายแนวคิดทางเลือก']},
    '4': {th:'การพัฒนากลยุทธ์การตลาด', en:'Marketing strategy development',
      items:['ออกแบบ<b>กลยุทธ์การตลาดเริ่มต้นโดยอิงจากแนวคิดสินค้า</b>',
             'ผลลัพธ์คือ <b>marketing strategy statement</b>',
             'ต้องมี<b>ตลาดเป้าหมาย · ข้อเสนอคุณค่า · เป้าหมายยอดขาย ส่วนแบ่งตลาด และกำไร · โครงร่างราคา ช่องทาง และงบประมาณ · เป้าหมายระยะยาว · กลยุทธ์ 4Ps</b>']},
    '5': {th:'การวิเคราะห์ทางธุรกิจ', en:'Business analysis',
      items:['ทบทวน<b>ประมาณการยอดขาย ต้นทุน และกำไร</b>',
             'เกณฑ์ตัดสินคือ<b>ตอบวัตถุประสงค์ของบริษัทได้หรือไม่</b>',
             'เป็น<b>ประตูบานสุดท้ายก่อนใช้เงินก้อนใหญ่</b>ในขั้นถัดไป']},
    '6': {th:'การพัฒนาสินค้า', en:'Product development',
      items:['เปลี่ยน<b>แนวคิดสินค้าให้เป็นสินค้าที่มีตัวตนจริง</b>',
             '<b>สร้างต้นแบบ</b> และ<b>ทดสอบกับผู้บริโภค</b>',
             'ตัวอย่าง Brooks ใช้กองทัพผู้ทดสอบที่เรียกว่า <b>Lab Rats และ Wear Testers</b>']},
    '7': {th:'การทดสอบตลาด', en:'Test marketing',
      items:['ทดสอบ<b>ทั้งตัวสินค้าและโปรแกรมการตลาด</b>ในสภาพตลาดที่สมจริง',
             'สามรูปแบบ <b>standard · simulated · controlled</b>',
             '<b>มักทดสอบ</b>เมื่อลงทุนสูงหรือยังไม่แน่ใจ · <b>มักไม่ทดสอบ</b>เมื่อเป็นการต่อสายผลิตภัณฑ์ง่าย ๆ ลอกคู่แข่ง ต้นทุนต่ำ หรือผู้บริหารมั่นใจแล้ว',
             'ตัวอย่าง Starbucks ข้ามขั้นนี้ไปกับแอปชำระเงินผ่านมือถือ เพื่อฉวยจังหวะตลาด']},
    '8': {th:'การนำออกสู่ตลาดเชิงพาณิชย์', en:'Commercialization',
      items:['<b>นำสินค้าใหม่เข้าสู่ตลาดจริง</b> และเป็นขั้นที่ใช้เงินมากที่สุด',
             'ตอบสามคำถาม <b>เปิดตัวเมื่อไร · เปิดตัวที่ไหน · ทยอยออกสู่ตลาดอย่างไร</b>',
             'ทำเลมีตั้งแต่<b>แห่งเดียว จังหวัด ภูมิภาค ทั้งประเทศ จนถึงระดับนานาชาติ</b>']}
  };
  var npdBtns = Array.prototype.slice.call(document.querySelectorAll('.step[data-npd]'));
  var npdOut = document.getElementById('npd-out');
  function showNpd(n){
    var s = NPD[n];
    if (!s || !npdOut) return;
    npdBtns.forEach(function(b){ b.setAttribute('aria-pressed', b.dataset.npd === n ? 'true' : 'false'); });
    npdOut.innerHTML = '<div class="oh">ขั้นที่ ' + n + ' · ' + s.th + '</div>' +
      '<div class="oe">' + s.en + '</div><ul>' +
      s.items.map(function(i){ return '<li>' + i + '</li>'; }).join('') + '</ul>';
  }
  npdBtns.forEach(function(b){ b.addEventListener('click', function(){ showNpd(b.dataset.npd); }); });
  if (npdOut) showNpd('1');

  /* บทที่ 8 · ห้าขั้นของวงจรชีวิตผลิตภัณฑ์ */
  var PLC = {
    '1': {th:'ขั้นพัฒนาสินค้า', en:'Product development',
      items:['<b>ยอดขายเป็นศูนย์</b> เพราะยังไม่มีอะไรวางขาย',
             '<b>ต้นทุนการลงทุนเพิ่มขึ้นเรื่อย ๆ</b>',
             'กำไรจึง<b>ติดลบ</b> และเป็นช่วงที่เส้นกำไรจมอยู่ใต้ศูนย์ในภาพ',
             'ขั้นนี้คือกระบวนการแปดขั้นในครึ่งแรกของบททั้งหมด']},
    '2': {th:'ขั้นแนะนำ', en:'Introduction',
      items:['<b>ยอดขายเติบโตช้า</b>',
             '<b>กำไรน้อยมากหรือไม่มีเลย</b>',
             '<b>ค่าใช้จ่ายด้านการจัดจำหน่ายและการส่งเสริมการตลาดสูง</b>',
             'ลูกค้าคือ <b>innovators</b> และคู่แข่ง<b>มีน้อยราย</b>',
             'วัตถุประสงค์คือ<b>สร้างความผูกพันกับสินค้าและทำให้เกิดการทดลองใช้</b>']},
    '3': {th:'ขั้นเติบโต', en:'Growth',
      items:['<b>ยอดขายเพิ่มขึ้น</b> และ<b>คู่แข่งรายใหม่เข้าสู่ตลาด</b>',
             '<b>กำไรเพิ่มขึ้น</b> เพราะเกิด<b>การประหยัดจากขนาด</b>',
             'มี<b>การให้ความรู้แก่ผู้บริโภค</b> และ<b>ลดราคาเพื่อดึงผู้ซื้อเพิ่ม</b>',
             'ลูกค้าคือ <b>early adopters</b>',
             'วัตถุประสงค์คือ<b>เพิ่มส่วนแบ่งตลาดให้มากที่สุด</b> ไม่ใช่กำไรสูงสุด']},
    '4': {th:'ขั้นเติบโตเต็มที่', en:'Maturity',
      items:['<b>ยอดขายชะลอตัว</b> และมี<b>สินค้าทดแทน</b>เข้ามา',
             'ต้อง<b>เพิ่มการส่งเสริมการตลาดและงานวิจัยและพัฒนา</b>เพื่อประคองยอดขายและกำไร',
             'มีสามทางเลือก <b>ปรับตลาด · ปรับสินค้า · ปรับส่วนประสมการตลาด</b>',
             'ลูกค้าคือ <b>mainstream adopters</b> และคู่แข่ง<b>คงที่และเริ่มลดลง</b>',
             'วัตถุประสงค์คือ<b>เพิ่มกำไรให้มากที่สุดพร้อมกับปกป้องส่วนแบ่งตลาด</b>',
             '<b>เป็นขั้นที่ยาวที่สุด</b>']},
    '5': {th:'ขั้นถดถอย', en:'Decline',
      items:['<b>ยอดขายตกลง</b> และ<b>กำไรลดลง</b>',
             'มีสามทางเลือก <b>คงสินค้าไว้ · รีดกำไร · เลิกสินค้า</b>',
             'ลูกค้าคือ <b>lagging adopters</b> และคู่แข่ง<b>จำนวนลดลง</b>',
             'วัตถุประสงค์คือ<b>ลดค่าใช้จ่ายและรีดเอาประโยชน์จากตรา</b>']}
  };
  var plcBtns = Array.prototype.slice.call(document.querySelectorAll('.step[data-plc]'));
  var plcOut = document.getElementById('plc-out');
  function showPlc(n){
    var s = PLC[n];
    if (!s || !plcOut) return;
    plcBtns.forEach(function(b){ b.setAttribute('aria-pressed', b.dataset.plc === n ? 'true' : 'false'); });
    plcOut.innerHTML = '<div class="oh">ขั้นที่ ' + n + ' · ' + s.th + '</div>' +
      '<div class="oe">' + s.en + '</div><ul>' +
      s.items.map(function(i){ return '<li>' + i + '</li>'; }).join('') + '</ul>';
  }
  plcBtns.forEach(function(b){ b.addEventListener('click', function(){ showPlc(b.dataset.plc); }); });
  if (plcOut) showPlc('1');
"""


# ───────────────────── ข้อสอบที่เติมเข้าคลังรวม ─────────────────────
# ต่อท้ายคลัง QS เดิมของหน้า จึงต้องขึ้นต้นด้วยจุลภาคของข้อก่อนหน้าเสมอ
# สลับตัวเลือกตอนแสดงผล เฉลยจึงเป็น a:0 ได้ทุกข้อ

QUIZ = u"""    {ch:8, q:'บริษัทแห่งหนึ่งซื้อสิทธิบัตรจากนักประดิษฐ์อิสระมาผลิตสินค้าออกขาย การได้สินค้ามาแบบนี้เรียกว่าอะไร',
     o:['การซื้อกิจการ <span class="en">acquisition</span>','การพัฒนาสินค้าใหม่ <span class="en">new product development</span>','การดัดแปลงสินค้า <span class="en">product modification</span>','การต่อสายผลิตภัณฑ์ <span class="en">line extension</span>'], a:0,
     e:'<b>Acquisition</b> คือการซื้อ<b>ทั้งบริษัท สิทธิบัตร หรือใบอนุญาต</b>เพื่อผลิตสินค้าของคนอื่น · ส่วน <b>new product development</b> ต้องเกิดจาก<b>ความพยายามพัฒนาสินค้าหรืองานวิจัยและพัฒนาของบริษัทเอง</b> คำว่าซื้อสิทธิบัตรจึงตัดออกจากกลุ่มหลังทันที'},
    {ch:8, q:'ข้อใด<b>ไม่ใช่</b>สาเหตุความล้มเหลวของสินค้าใหม่ตามที่ตำราระบุ',
     o:['พนักงานขายมีจำนวนไม่พอ','ประเมินขนาดตลาดสูงเกินจริง','ตั้งราคาหรือวางตำแหน่งผิด','การตอบโต้ของคู่แข่ง'], a:0,
     e:'ห้าสาเหตุตามตำราคือ <b>ประเมินขนาดตลาดสูงเกินจริง · ปัญหาด้านการออกแบบ · ตั้งราคาหรือวางตำแหน่งผิด · ต้นทุนการพัฒนาสูงเกินไป · การตอบโต้ของคู่แข่ง</b> · จำนวนพนักงานขายไม่อยู่ในชุดนี้'},
    {ch:8, q:'Facebook ใช้ hackathon เพื่อดึงความคิดเรื่องนวัตกรรมจากพนักงานของตัวเอง จัดเป็นแหล่งความคิดแบบใด',
     o:['แหล่งภายใน <span class="en">internal source</span>','แหล่งภายนอก <span class="en">external source</span>','Crowdsourcing','การซื้อกิจการ'], a:0,
     e:'คำชี้ขาดคือ <b>พนักงานของตัวเอง</b> · แหล่งภายในหมายถึง<b>งานวิจัยและพัฒนาของบริษัท ผู้บริหารและพนักงาน และโครงการผู้ประกอบการภายใน</b> · ส่วน crowdsourcing เปิดกว้างถึง<b>คนนอกและสาธารณชน</b> จึงอยู่กลุ่มแหล่งภายนอก'},
    {ch:8, q:'Tupperware จัดประกวด Clever Container Challenge เพื่อหาความคิดเรื่องภาชนะอาหารอัจฉริยะ ตรงกับวิธีใด',
     o:['Crowdsourcing','Concept testing','Test marketing','Business analysis'], a:0,
     e:'<b>Crowdsourcing</b> คือการเชิญ<b>ชุมชนคนกว้าง ๆ</b> ทั้งลูกค้า พนักงาน นักวิจัยอิสระ และสาธารณชนทั่วไป เข้ามาร่วมในกระบวนการสร้างนวัตกรรม · การเปิดประกวดให้ใครก็ได้ส่งความคิดเข้ามาคือรูปแบบที่ชัดที่สุดของวิธีนี้ และยังอยู่ใน<b>ขั้นที่ 1 สร้างความคิด</b>'},
    {ch:8, q:'กรอบ R-W-W ที่ใช้ในขั้นกลั่นกรองความคิด ประกอบด้วยคำถามข้อใด',
     o:['Is it real? · Can we win? · Is it worth doing?','Is it ready? · Is it wanted? · Is it workable?','Is it right? · Who wins? · What is the risk?','Is it real? · Who pays? · When to launch?'], a:0,
     e:'สามคำถามคือ <b>มันจริงไหม</b> มีความต้องการอยู่จริงและทำได้จริง · <b>เราชนะได้ไหม</b> มีความได้เปรียบที่ยั่งยืนพอหรือไม่ · <b>คุ้มที่จะทำไหม</b> ผลตอบแทนคุ้มความเสี่ยงหรือไม่'},
    {ch:8, q:'ข้อใดคือนิยามของ product concept',
     o:['ฉบับที่ลงรายละเอียดแล้วของความคิดเรื่องสินค้าใหม่ ซึ่งเขียนด้วยถ้อยคำที่มีความหมายต่อผู้บริโภค','ความคิดเกี่ยวกับสินค้าที่เป็นไปได้ซึ่งบริษัทมองว่าตัวเองจะนำเสนอออกสู่ตลาดได้','วิธีที่ผู้บริโภครับรู้ต่อสินค้าที่มีอยู่จริงหรือที่อาจจะมี','ชุดของคุณประโยชน์ที่ตราสินค้าสัญญาว่าจะส่งมอบ'], a:0,
     e:'ตัวเลือกที่สองคือ <b>product idea</b> ตัวเลือกที่สามคือ <b>product image</b> · จุดต่างของ <b>product concept</b> คือ<b>ลงรายละเอียดแล้ว</b>และ<b>เขียนด้วยภาษาที่มีความหมายต่อผู้บริโภค</b> ไม่ใช่ภาษาเทคนิคของบริษัท'},
    {ch:8, q:'นักวิจัยนำภาพวาดและคำบรรยายของรถยนต์ไฟฟ้ารุ่นใหม่ไปให้กลุ่มผู้บริโภคเป้าหมายดูแล้วถามปฏิกิริยา กิจกรรมนี้อยู่ในขั้นใด',
     o:['ขั้นที่ 3 การพัฒนาและทดสอบแนวคิดสินค้า','ขั้นที่ 6 การพัฒนาสินค้า','ขั้นที่ 7 การทดสอบตลาด','ขั้นที่ 2 การกลั่นกรองความคิด'], a:0,
     e:'<b>Concept testing</b> ใช้เพียง<b>คำบรรยาย ภาพ หรือแบบจำลอง</b> ยังไม่มีของจริง · ถ้าผู้บริโภคได้<b>ของจริงไปใช้</b>คือขั้นที่ 6 · ถ้าเจอ<b>ทั้งสินค้าและโปรแกรมการตลาดในตลาดที่สมจริง</b>คือขั้นที่ 7'},
    {ch:8, q:'ข้อใด<b>ไม่ได้</b>อยู่ใน marketing strategy statement',
     o:['รายชื่อผู้จัดหาวัตถุดิบที่คัดเลือกไว้','คำบรรยายตลาดเป้าหมาย','เป้าหมายยอดขาย ส่วนแบ่งตลาด และกำไร','โครงร่างของราคา ช่องทางจัดจำหน่าย และงบประมาณการตลาด'], a:0,
     e:'องค์ประกอบตามตำราคือ <b>ตลาดเป้าหมาย · ข้อเสนอคุณค่า · เป้าหมายยอดขาย ส่วนแบ่งตลาด และกำไร · โครงร่างราคา ช่องทาง และงบประมาณ · เป้าหมายยอดขายและกำไรระยะยาว · กลยุทธ์ 4Ps</b> · รายชื่อซัพพลายเออร์เป็นเรื่องของการจัดหา ไม่อยู่ในเอกสารนี้'},
    {ch:8, q:'การทบทวนประมาณการยอดขาย ต้นทุน และกำไร เพื่อดูว่าตอบวัตถุประสงค์ของบริษัทหรือไม่ คือขั้นใด',
     o:['ขั้นที่ 5 การวิเคราะห์ทางธุรกิจ','ขั้นที่ 4 การพัฒนากลยุทธ์การตลาด','ขั้นที่ 2 การกลั่นกรองความคิด','ขั้นที่ 8 การนำออกสู่ตลาด'], a:0,
     e:'<b>Business analysis</b> คือขั้นที่เอาตัวเลขมาตรวจ · สังเกตเกณฑ์ตัดสินว่าเป็น<b>วัตถุประสงค์ของบริษัทเอง</b> ไม่ใช่มาตรฐานอุตสาหกรรม · ขั้นที่ 4 เป็นการ<b>ออกแบบแผน</b> ส่วนขั้นที่ 5 เป็นการ<b>ตรวจแผนด้วยตัวเลข</b>'},
    {ch:8, q:'Brooks ใช้กลุ่มผู้ใช้ที่เรียกว่า Lab Rats และ Wear Testers ทดสอบรองเท้าวิ่งของจริง กิจกรรมนี้คือขั้นใด',
     o:['ขั้นที่ 6 การพัฒนาสินค้า','ขั้นที่ 3 การพัฒนาและทดสอบแนวคิดสินค้า','ขั้นที่ 7 การทดสอบตลาด','ขั้นที่ 1 การสร้างความคิด'], a:0,
     e:'ขั้นที่ 6 มีสองกิจกรรมคือ<b>สร้างต้นแบบ</b>และ<b>ทดสอบกับผู้บริโภค</b> · กรณีนี้ผู้ทดสอบได้<b>รองเท้าจริงไปใส่วิ่ง</b> จึงเป็น consumer test ของขั้นที่ 6 ไม่ใช่ concept testing · และยัง<b>ไม่มีโปรแกรมการตลาดครบชุด</b> จึงไม่ใช่ขั้นที่ 7'},
    {ch:8, q:'ข้อใด<b>ไม่ใช่</b>รูปแบบของการทดสอบตลาดตามตำรา',
     o:['Sequential test markets','Standard test markets','Simulated test markets','Controlled test markets'], a:0,
     e:'สามรูปแบบคือ <b>standard</b> ตลาดจริงเต็มรูปแบบซึ่งกว้างและแพง · <b>simulated</b> ร้านจำลองในห้องปฏิบัติการหรือร้านออนไลน์จำลอง · <b>controlled</b> กลุ่มผู้ซื้อและร้านค้าที่ถูกควบคุม · คำว่า sequential เป็นคำที่ใช้กับ<b>วิธีพัฒนาแบบเรียงลำดับ</b> คนละเรื่องกัน'},
    {ch:8, q:'สถานการณ์ใดที่บริษัท<b>มักจะไม่</b>ทดสอบตลาด',
     o:['เป็นการต่อสายผลิตภัณฑ์แบบง่าย ๆ และต้นทุนต่ำ','สินค้าใหม่ที่ต้องลงทุนสูงมาก','ยังไม่แน่ใจในตัวสินค้า','ยังไม่แน่ใจในโปรแกรมการตลาด'], a:0,
     e:'ตำราให้สี่กรณีที่มักไม่ทดสอบ คือ <b>การต่อสายผลิตภัณฑ์แบบง่าย ๆ · ลอกสินค้าของคู่แข่ง · ต้นทุนต่ำ · ผู้บริหารมั่นใจอยู่แล้ว</b> · ส่วนสองกรณีที่มักทดสอบคือ<b>ลงทุนสูง</b>และ<b>ยังไม่แน่ใจ</b>'},
    {ch:8, q:'การตัดสินใจว่าจะเปิดตัวเมื่อไร ที่ไหน และจะทยอยออกสู่ตลาดอย่างไร อยู่ในขั้นใด',
     o:['ขั้นที่ 8 การนำออกสู่ตลาดเชิงพาณิชย์','ขั้นที่ 7 การทดสอบตลาด','ขั้นที่ 4 การพัฒนากลยุทธ์การตลาด','ขั้นที่ 5 การวิเคราะห์ทางธุรกิจ'], a:0,
     e:'<b>Commercialization</b> คือการนำสินค้าใหม่เข้าสู่ตลาดจริง และตอบสามคำถามคือ <b>when to launch · where to launch · planned market rollout</b> · เป็นขั้นสุดท้ายและใช้เงินมากที่สุด'},
    {ch:8, q:'ข้อใดเป็น<b>ข้อเสีย</b>ของการพัฒนาสินค้าใหม่แบบทีมข้ามสายงาน',
     o:['ก่อให้เกิดความตึงเครียดและความสับสนในองค์กรมากกว่าวิธีทำทีละขั้นตามลำดับ','ทำให้การพัฒนาช้าลงกว่าวิธีเรียงลำดับ','ทำให้ต้นทุนการวิจัยและพัฒนาสูงขึ้นเสมอ','ทำให้บริษัทต้องพึ่งความคิดจากลูกค้ามากเกินไป'], a:0,
     e:'ตำราระบุข้อดีว่า<b>เร็วและยืดหยุ่น</b> และระบุข้อเสียไว้ตรง ๆ ว่า<b>ก่อให้เกิดความตึงเครียดและความสับสนในองค์กรมากกว่าแบบ sequential</b> · ข้อแลกเปลี่ยนคือแลกความเป็นระเบียบกับความเร็ว จึงไม่ใช่ว่าช้าลง'},
    {ch:8, q:'LEGO รับฟังลูกค้าและดึงความคิดจากชุมชนผู้ใช้ของตัวเองจนถูกเรียกว่า the Apple of Toys เป็นตัวอย่างของอะไร',
     o:['การพัฒนาสินค้าใหม่ที่ยึดลูกค้าเป็นศูนย์กลาง','การพัฒนาสินค้าใหม่แบบทีม','การพัฒนาสินค้าใหม่อย่างเป็นระบบ','การซื้อกิจการ'], a:0,
     e:'<b>Customer-centered NPD</b> คือการ<b>มุ่งหาวิธีใหม่ในการแก้ปัญหาของลูกค้าและสร้างประสบการณ์ที่ทำให้ลูกค้าพอใจมากขึ้น</b> · ส่วน team-based พูดถึง<b>แผนกภายในบริษัท</b> และ systematic พูดถึง<b>ระบบบริหารจัดการนวัตกรรม</b>'},
    {ch:8, q:'ในขั้นพัฒนาสินค้าของวงจรชีวิตผลิตภัณฑ์ ยอดขายและกำไรเป็นอย่างไร',
     o:['ยอดขายเป็นศูนย์ ต้นทุนการลงทุนเพิ่มขึ้น กำไรจึงติดลบ','ยอดขายต่ำแต่เริ่มมีกำไรเล็กน้อย','ยอดขายเติบโตช้าและกำไรคงที่','ยอดขายเป็นศูนย์และไม่มีต้นทุนใด ๆ'], a:0,
     e:'ตำราระบุว่าขั้นนี้ <b>zero sales and increasing investment costs</b> · ยังไม่มีอะไรวางขายจึงยอดขายเป็นศูนย์ แต่เงินลงทุนไหลออกเรื่อย ๆ กำไรจึงติดลบ เป็นช่วงที่เส้นกำไรอยู่ใต้ศูนย์ใน Figure 9.2'},
    {ch:8, q:'ระดับใดของแนวคิดวงจรชีวิตผลิตภัณฑ์มีวงจรชีวิต<b>ยาวที่สุด</b>',
     o:['ประเภทสินค้า <span class="en">product class</span>','รูปแบบสินค้า <span class="en">product form</span>','ตราสินค้า <span class="en">brand</span>','แฟชัน <span class="en">fashion</span>'], a:0,
     e:'ตำราระบุว่า <b>product class has the longest life cycle</b> · <b>product form</b> มีแนวโน้มเป็นรูปทรง PLC มาตรฐาน ส่วน <b>brand</b> เปลี่ยนได้เร็วเพราะการโจมตีและการตอบโต้ของคู่แข่ง'},
    {ch:8, q:'ยอดขายของสินค้าชนิดหนึ่งพุ่งขึ้นสูงมากในเวลาอันสั้นแล้วทรุดลงเร็วพอ ๆ กัน ตรงกับคำใด',
     o:['Fad','Fashion','Style','Product form'], a:0,
     e:'<b>Fad</b> คือ<b>ช่วงเวลาสั้น ๆ ที่ยอดขายสูงผิดปกติ ขับเคลื่อนด้วยความคลั่งไคล้ของผู้บริโภค</b> กราฟจึงเป็นยอดแหลมแล้วดิ่ง · <b>fashion</b> ขึ้นช้าลงช้าเป็นโค้งลูกเดียว · <b>style</b> เป็นลูกคลื่นที่กลับมาได้อีก'},
    {ch:8, q:'ข้อใดคือนิยามของ fashion ตามตำรา',
     o:['สไตล์ที่กำลังได้รับการยอมรับหรือเป็นที่นิยมอยู่ในขณะนั้นในวงการใดวงการหนึ่ง','รูปแบบการแสดงออกที่เป็นพื้นฐานและมีเอกลักษณ์','ช่วงเวลาสั้น ๆ ที่ยอดขายสูงผิดปกติจากความคลั่งไคล้','สินค้าที่อยู่ในขั้นเติบโตของวงจรชีวิต'], a:0,
     e:'นิยามคือ <b>a currently accepted or popular style in a given field</b> · สังเกตว่า fashion ถูกนิยามโดยใช้คำว่า style อยู่ในตัว แปลว่า<b>สองคำนี้ซ้อนกัน</b> fashion คือ style ที่กำลังนิยม ไม่ใช่สิ่งที่แยกขาดจากกัน'},
    {ch:8, q:'ขั้นใดของวงจรชีวิตผลิตภัณฑ์ที่มี<b>ค่าใช้จ่ายด้านการจัดจำหน่ายและการส่งเสริมการตลาดสูง</b> แต่<b>กำไรน้อยมากหรือไม่มีเลย</b>',
     o:['ขั้นแนะนำ','ขั้นเติบโต','ขั้นเติบโตเต็มที่','ขั้นถดถอย'], a:0,
     e:'ลักษณะสามข้อของ <b>introduction stage</b> คือ<b>ยอดขายเติบโตช้า · กำไรน้อยหรือไม่มี · ค่าใช้จ่ายด้านการจัดจำหน่ายและการส่งเสริมการตลาดสูง</b> · กำไรยังไม่มาเพราะต้องใช้เงินมากผลักสินค้าเข้าช่องทางและให้คนรู้จัก ขณะที่ยอดขายยังน้อย'},
    {ch:8, q:'ยาสีฟันยี่ห้อหนึ่งยอดขายนิ่งมาหลายปี จึงออกแคมเปญชวนให้ลูกค้าเดิมแปรงฟันวันละสามครั้งแทนสองครั้ง นี่คือกลยุทธ์ใด',
     o:['ปรับตลาด <span class="en">modify the market</span>','ปรับสินค้า <span class="en">modify the product</span>','ปรับส่วนประสมการตลาด <span class="en">modify the marketing mix</span>','รีดกำไร <span class="en">harvest</span>'], a:0,
     e:'เป้าหมายของ <b>modify the market</b> คือ<b>เพิ่มการบริโภคสินค้าตัวเดิม</b> ซึ่งทำได้สามทาง คือหาผู้ใช้กลุ่มใหม่ วางตำแหน่งใหม่ และ<b>เพิ่มอัตราการใช้ในกลุ่มลูกค้าปัจจุบัน</b> · ตัวสินค้าไม่เปลี่ยน เครื่องมือ 4Ps ก็ไม่เปลี่ยน สิ่งที่เปลี่ยนคือ<b>พฤติกรรมการใช้</b>'},
    {ch:8, q:'บริษัทเดียวกันนั้นตัดสินใจลดราคายาสีฟันลง 20% และเพิ่มช่องทางขายบนแพลตฟอร์มออนไลน์ นี่คือกลยุทธ์ใด',
     o:['ปรับส่วนประสมการตลาด <span class="en">modify the marketing mix</span>','ปรับตลาด <span class="en">modify the market</span>','ปรับสินค้า <span class="en">modify the product</span>','เลิกสินค้า <span class="en">drop</span>'], a:0,
     e:'<b>Modify the marketing mix</b> คือการ<b>เปลี่ยนองค์ประกอบของส่วนประสมการตลาดหนึ่งตัวหรือมากกว่า</b> เช่น ลดราคา เสนอบริการใหม่ ทำแคมเปญโฆษณาที่ดีกว่าเดิม หรือเข้าสู่ช่องทางใหม่ · ทั้งลดราคาและเพิ่มช่องทางอยู่ในชุดนี้ทั้งคู่'},
    {ch:8, q:'ในขั้นถดถอย ทางเลือกที่เรียกว่า harvest หมายถึงอะไร',
     o:['ลดต้นทุนต่าง ๆ ลงแล้วหวังว่ายอดขายจะยังทรงอยู่ได้','เก็บสินค้าไว้โดยหวังว่าจะดันกลับไปสู่ขั้นเติบโตได้อีก','ถอดสินค้าออกจากสายผลิตภัณฑ์','เร่งงบโฆษณาเพื่อยืดอายุสินค้า'], a:0,
     e:'<b>Harvest</b> คือ<b>ลดต้นทุนลงแล้วหวังว่ายอดขายจะยังทรงอยู่</b> เป็นการเก็บกำไรก้อนสุดท้ายโดยไม่ลงทุนเพิ่ม · ตัวเลือกที่สองคือ <b>maintain</b> และตัวเลือกที่สามคือ <b>drop</b>'},
    {ch:8, q:'ตามตาราง 9.2 วัตถุประสงค์ทางการตลาดของ<b>ขั้นเติบโต</b>คือข้อใด',
     o:['เพิ่มส่วนแบ่งตลาดให้มากที่สุด','เพิ่มกำไรให้มากที่สุดพร้อมกับปกป้องส่วนแบ่งตลาด','สร้างความผูกพันกับสินค้าและทำให้เกิดการทดลองใช้','ลดค่าใช้จ่ายและรีดเอาประโยชน์จากตรา'], a:0,
     e:'ขั้นเติบโตคือ <b>maximize market share</b> · ส่วน <b>maximize profit while defending market share</b> เป็นของขั้นเติบโตเต็มที่ · <b>create product engagement and trial</b> เป็นของขั้นแนะนำ และ <b>reduce expenditure and milk the brand</b> เป็นของขั้นถดถอย'},
    {ch:8, q:'ตามตาราง 9.2 กลยุทธ์การส่งเสริมการขายใน<b>ขั้นเติบโต</b>คือข้อใด',
     o:['ลดลง เพื่อฉวยประโยชน์จากอุปสงค์ที่แรงอยู่แล้ว','ใช้อย่างหนักเพื่อล่อให้ทดลองใช้','เพิ่มขึ้นเพื่อกระตุ้นให้เปลี่ยนตรา','ลดลงเหลือระดับต่ำสุด'], a:0,
     e:'ข้อนี้คนตอบผิดบ่อยที่สุดในตาราง · ขั้นเติบโต<b>ลดการส่งเสริมการขาย</b>เพราะอุปสงค์แรงอยู่แล้วไม่ต้องล่อ · การ<b>ใช้อย่างหนักเพื่อล่อให้ทดลองใช้</b>เป็นของขั้นแนะนำ และการ<b>เพิ่มเพื่อกระตุ้นให้เปลี่ยนตรา</b>เป็นของขั้นเติบโตเต็มที่'},
    {ch:8, q:'ตามตาราง 9.2 จำนวนคู่แข่งใน<b>ขั้นเติบโตเต็มที่</b>เป็นอย่างไร',
     o:['คงที่และเริ่มลดลง','เพิ่มขึ้นเรื่อย ๆ','มีน้อยราย','ลดลงอย่างรวดเร็ว'], a:0,
     e:'ตารางระบุว่า <b>stable number beginning to decline</b> · จุดที่คู่แข่ง<b>เพิ่มเร็วที่สุด</b>คือ<b>ขั้นเติบโต</b> ไม่ใช่ขั้นเติบโตเต็มที่ · และจำนวนที่ลดลงชัดเจนเป็นของขั้นถดถอย'},
    {ch:8, q:'McDonald&rsquo;s ปรับเมนูและการดำเนินงานให้เข้ากับวัฒนธรรมผู้บริโภคฝรั่งเศสจนฝรั่งเศสเป็นตลาดที่ทำกำไรสูงอันดับสองของบริษัท เป็นตัวอย่างของอะไร',
     o:['การเลือก customization แทน standardization ในการตลาดระหว่างประเทศ','การปรับส่วนประสมการตลาดในขั้นถดถอย','การทดสอบตลาดแบบ controlled test market','การพัฒนาสินค้าใหม่แบบ crowdsourcing'], a:0,
     e:'ประเด็นการตลาดสินค้าและบริการระหว่างประเทศมีสี่ข้อ คือ<b>จะนำสินค้าใดเข้าประเทศใด · standardization versus customization · บรรจุภัณฑ์และฉลาก · ขนบธรรมเนียม ค่านิยม และกฎหมาย</b> · กรณีนี้คือการเลือก<b>ปรับให้เข้ากับท้องถิ่น</b>'}"""

QUIZ_TOTAL = 85 + QUIZ.count(u'{ch:')
