# -*- coding: utf-8 -*-
u"""เนื้อหาบทที่ 6 ของวิชาการบัญชีขั้นสูง 1 · กรณีต่างๆ เกี่ยวกับการจัดทำงบการเงินรวม

ที่มา เอกสารประกอบการสอน Ch6_2568
  สไลด์  2      ห้ากรณีที่บทนี้ครอบคลุม
  สไลด์  3-8    บริษัทย่อยมีหุ้นบุริมสิทธิ
  สไลด์  9-16   การซื้อหุ้นบริษัทย่อยในระหว่างงวดบัญชี
  สไลด์ 17      บริษัทย่อยจ่ายหุ้นปันผล
  สไลด์ 19-22   การเปลี่ยนแปลงสัดส่วนการถือหุ้น กรณีซื้อเพิ่ม
  สไลด์ 23      ตัวอย่างที่ 6.5 การขายหุ้นสามัญบางส่วน มีแต่หน้าชื่อเรื่อง

สองหัวข้อที่สไลด์ไม่ได้ลงเนื้อหา คือการขายหุ้นบางส่วนกับการสูญเสียการควบคุม
เขียนจากมาตรฐานและตำราแทน และกำกับไว้ในหน้าให้ชัดว่าส่วนนั้นไม่ได้มาจากสไลด์

ตารางและกระดาษทำการในสไลด์พิมพ์ขึ้นใหม่เป็นตารางเว็บทั้งหมด ไม่ได้ฝังภาพสแกน
เพราะกระดาษทำการมีตัวเลขหนาแน่น อ่านจากภาพบนมือถือไม่ไหว

บทที่ 6 อีกส่วนหนึ่งคือ งบการเงินรวม กรณีขาดทุน อยู่ในแท็บ ชีท 4_3 อยู่แล้ว
หน้านี้จึงโยงไปหากันแทนการเขียนซ้ำ
"""

RAIL = u"""    <nav id="rail-c6s" class="hidden" aria-label="หัวข้อบทที่ 6">
      <div class="rail-h">บทที่ 6 · กรณีต่างๆ</div>
      <ol>
        <li><a href="#c6s-1"><i>1</i>ห้ากรณีของบทนี้</a></li>
        <li><a href="#c6s-2"><i>2</i>หุ้นบุริมสิทธิคืออะไร</a></li>
        <li><a href="#c6s-3"><i>3</i>ค่าความนิยมเมื่อมีหุ้นบุริมสิทธิ</a></li>
        <li><a href="#c6s-4"><i>4</i>ถือหุ้นสามัญเท่านั้น</a></li>
        <li><a href="#c6s-5"><i>5</i>ถือทั้งสามัญและบุริมสิทธิ</a></li>
        <li><a href="#c6s-6"><i>6</i>ซื้อระหว่างงวด · หลักการ</a></li>
        <li><a href="#c6s-7"><i>7</i>ซื้อระหว่างงวด · ตัวอย่าง</a></li>
        <li><a href="#c6s-8"><i>8</i>วิธีส่วนได้เสียและงบกำไรขาดทุน</a></li>
        <li><a href="#c6s-9"><i>9</i>กระดาษทำการงบฐานะการเงิน</a></li>
        <li><a href="#c6s-10"><i>10</i>เปลี่ยนสัดส่วน · วัดค่าความนิยมเมื่อใด</a></li>
        <li><a href="#c6s-11"><i>11</i>ตัวอย่างที่ 6.4 ซื้อเป็นขั้น</a></li>
        <li><a href="#c6s-12"><i>12</i>ซื้อเพิ่มโดยไม่เสียการควบคุม</a></li>
        <li><a href="#c6s-13"><i>13</i>ขายบางส่วนโดยไม่เสียการควบคุม</a></li>
        <li><a href="#c6s-14"><i>14</i>การสูญเสียการควบคุม</a></li>
        <li><a href="#c6s-15"><i>15</i>บริษัทย่อยจ่ายหุ้นปันผล</a></li>
        <li><a href="#c6s-16"><i>16</i>สรุปและจุดที่ข้อสอบชอบถาม</a></li>
      </ol>
    </nav>
"""

PANEL = u"""  <div id="c6s" class="hidden" role="tabpanel" aria-labelledby="t-c6s">
    <p class="lede">สี่บทแรกสร้างงบการเงินรวมในสถานการณ์<b>มาตรฐานที่สุด</b> คือบริษัทย่อยมีแต่หุ้นสามัญ ซื้อกันวันต้นปี และสัดส่วนการถือหุ้นไม่เคยขยับ · บทนี้ยก<b>ข้อสมมติเหล่านั้นออกทีละข้อ</b> แล้วถามว่าต้องแก้วิธีทำอย่างไร · ทั้งห้ากรณีใช้หลักเดิมทั้งหมด เปลี่ยนแค่<b>ฐานที่ใช้คำนวณ</b>กับ<b>จังหวะเวลาที่วัดมูลค่า</b></p>

    <div class="note rule">
      <span class="nh">บทที่ 6 อีกส่วนหนึ่งอยู่คนละแท็บ</span>
      หัวข้อ <b>งบการเงินรวม กรณีขาดทุน</b> ตาม TFRS 10 ย่อหน้า ข94 ก็เป็นเนื้อหาของบทที่ 6 เหมือนกัน แต่มาจากเอกสาร <b>ชีท 4_3</b> คนละฉบับกับสไลด์ชุดนี้ จึงอยู่ในแท็บ <b>ชีท 4_3 · สี่เรื่องรวม</b> ตามเดิม · อ่านคู่กันทั้งสองแท็บจึงจะครบทั้งบท
    </div>

    <section class="sec" id="c6s-1">
      <div class="sec-h"><span class="sec-n">1</span><h2>ห้ากรณีที่บทนี้ครอบคลุม</h2></div>
      <div class="body">
        <p>สไลด์หน้าแรกของบทวางหัวข้อไว้ห้าข้อ ผมอยากให้มองว่าแต่ละข้อคือ<b>ข้อสมมติหนึ่งข้อที่ถูกยกออก</b> ไม่ใช่เรื่องใหม่ห้าเรื่องที่ไม่เกี่ยวกัน</p>
        <div class="tw"><table class="tbl">
          <thead><tr><th>กรณี</th><th>ข้อสมมติเดิมที่ถูกยกออก</th><th>สิ่งที่ต้องเปลี่ยน</th></tr></thead>
          <tbody>
            <tr><td class="k">1 · บริษัทย่อยมีหุ้นบุริมสิทธิ</td>
                <td>บริษัทย่อยมีแต่<b>หุ้นสามัญ</b></td>
                <td><b>ฐานที่ใช้แบ่งส่วนของเจ้าของและกำไร</b> ต้องกันส่วนของหุ้นบุริมสิทธิออกก่อน</td></tr>
            <tr><td class="k">2 · ซื้อหุ้นระหว่างงวดบัญชี</td>
                <td>ซื้อหุ้น<b>วันต้นงวด</b>พอดี</td>
                <td><b>จังหวะที่วัดมูลค่ายุติธรรม</b> ย้ายมาเป็นวันที่ซื้อจริง และต้องแยกกำไรก่อนซื้อออก</td></tr>
            <tr><td class="k">3 · เปลี่ยนสัดส่วนโดย<b>ไม่</b>เสียการควบคุม</td>
                <td>สัดส่วนการถือหุ้น<b>คงที่</b></td>
                <td>ถือเป็น<b>รายการในส่วนของเจ้าของ</b> ไม่เกิดค่าความนิยมใหม่ ไม่เกิดกำไรขาดทุน</td></tr>
            <tr><td class="k">4 · การสูญเสียการควบคุม</td>
                <td>ยัง<b>ควบคุม</b>อยู่ตลอด</td>
                <td>เลิกจัดทำงบรวม <b>รับรู้กำไรขาดทุนในกำไรหรือขาดทุน</b> และวัดส่วนที่เหลือด้วยมูลค่ายุติธรรม</td></tr>
            <tr><td class="k">5 · บริษัทย่อยจ่ายหุ้นปันผล</td>
                <td>บริษัทย่อยจ่าย<b>เงินปันผลเป็นเงินสด</b></td>
                <td>แทบไม่ต้องเปลี่ยนอะไร เพราะ<b>ส่วนของผู้ถือหุ้นรวมไม่เปลี่ยน</b> แต่ต้องย้ายยอดให้ถูกบัญชี</td></tr>
          </tbody>
        </table></div>
        <div class="note warn">
          <span class="nh">สองหัวข้อที่สไลด์ไม่ได้ลงเนื้อหา</span>
          สไลด์ชุดนี้<b>ไม่มีหน้าเนื้อหาของกรณีที่ 4 การสูญเสียการควบคุม</b> และ<b>ตัวอย่างที่ 6.5 การขายหุ้นสามัญบางส่วน มีแต่หน้าชื่อเรื่องเปล่า</b> · หัวข้อที่ 13 และ 14 ของหน้านี้จึงเขียนขึ้นจาก<b>มาตรฐานและตำรา ไม่ได้มาจากสไลด์</b> และกำกับไว้ในหัวข้อนั้นแล้ว · สไลด์หน้าสุดท้ายของชุดก็เขียนไว้ว่า <b>โปรดนำหนังสือเรียนมาด้วย</b> ซึ่งสอดคล้องกัน
        </div>
      </div>
    </section>

    <section class="sec" id="c6s-2">
      <div class="sec-h"><span class="sec-n">2</span><h2>หุ้นบุริมสิทธิคืออะไร และทำไมจึงกวนงบรวม</h2></div>
      <div class="body">
        <p class="lede">ตราสารทุนของบริษัทย่อยมีสองชนิด คือ<b>หุ้นสามัญ</b>กับ<b>หุ้นบุริมสิทธิ</b> และความต่างข้อเดียวที่ทำให้ทั้งหัวข้อนี้เกิดขึ้น คือ<b>สิทธิออกเสียง</b></p>
        <div class="grid g2">
          <div class="card">
            <span class="cn">หุ้นสามัญ</span>
            <div class="ct">Common stock</div>
            <div class="cs"><b>มีสิทธิออกเสียง</b>ในที่ประชุมผู้ถือหุ้น · เป็นตัวที่ใช้ตัดสินว่าใคร<b>ควบคุม</b>บริษัทย่อย · ได้ส่วนแบ่งกำไรเป็น<b>ส่วนที่เหลือ</b>หลังหักส่วนของหุ้นบุริมสิทธิแล้ว</div>
          </div>
          <div class="card">
            <span class="cn">หุ้นบุริมสิทธิ</span>
            <div class="ct">Preferred stock</div>
            <div class="cs">มี<b>สิทธิพิเศษเหนือผู้ถือหุ้นสามัญ</b> แต่<b>ไม่มีสิทธิออกเสียง</b>ในที่ประชุมผู้ถือหุ้น · กำหนด<b>อัตราเงินปันผลเป็นร้อยละของราคาตราไว้</b> เช่น หุ้นบุริมสิทธิ 3 เปอร์เซ็นต์</div>
          </div>
        </div>
        <div class="note key">
          <span class="nh">ประโยคเดียวที่คุมทั้งหัวข้อ</span>
          เมื่อหุ้นบุริมสิทธิ<b>ไม่มีสิทธิออกเสียง</b> ผู้ถือหุ้นบุริมสิทธิจึง<b>ไม่มีทางเป็นผู้ควบคุม</b>ได้เลย · ดังนั้นส่วนของผู้ถือหุ้นบุริมสิทธิที่บริษัทใหญ่ไม่ได้ถือ จะกลายเป็น<b>ส่วนได้เสียที่ไม่มีอำนาจควบคุม</b> <span class="mono">NCI</span> ทั้งก้อนเสมอ ไม่ว่าบริษัทใหญ่จะคุมบริษัทย่อยแน่นแค่ไหนก็ตาม
        </div>
        <h3>สามประเด็นที่สไลด์บอกว่าต้องพิจารณา</h3>
        <ul class="list">
          <li><b>การคำนวณค่าความนิยม</b> — ฐานที่ใช้เทียบเปลี่ยนไป เพราะต้องกันส่วนของหุ้นบุริมสิทธิออกจากฐานของหุ้นสามัญ</li>
          <li><b>กรณีบริษัทใหญ่ถือหุ้นสามัญของบริษัทย่อยเท่านั้น</b></li>
          <li><b>กรณีบริษัทใหญ่ถือทั้งหุ้นสามัญและหุ้นบุริมสิทธิของบริษัทย่อย</b></li>
        </ul>
      </div>
    </section>

    <section class="sec" id="c6s-3">
      <div class="sec-h"><span class="sec-n">3</span><h2>ตัวอย่าง · คำนวณค่าความนิยมเมื่อบริษัทย่อยมีหุ้นบุริมสิทธิ</h2></div>
      <div class="body">
        <div class="note">
          <span class="nh">โจทย์ตามสไลด์</span>
          บริษัทใหญ่ซื้อ<b>หุ้นสามัญ</b>ของบริษัทย่อยจำนวน <b>80 เปอร์เซ็นต์</b> ในราคา <b>63,000 บาท</b> · สินทรัพย์และหนี้สินของบริษัทย่อยแสดงตามมูลค่ายุติธรรมแล้ว · แต่บริษัทย่อยมี<b>สิทธิบัตรที่ไม่ได้บันทึกบัญชี 15,000 บาท</b> อายุการให้ประโยชน์อีก 10 ปี
        </div>
        <h3>ส่วนของผู้ถือหุ้นของบริษัทย่อย</h3>
        <div class="tw"><table class="tbl">
          <tbody>
            <tr><td class="k">ทุน-หุ้นบุริมสิทธิ 3 เปอร์เซ็นต์</td><td class="m">20,000</td></tr>
            <tr><td class="k">ทุน-หุ้นสามัญ</td><td class="m">20,000</td></tr>
            <tr><td class="k">ส่วนเกินมูลค่าหุ้นสามัญ</td><td class="m">10,000</td></tr>
            <tr><td class="k">กำไรสะสม</td><td class="m">30,000</td></tr>
            <tr class="tot2"><td class="k">รวม</td><td class="m">80,000</td></tr>
          </tbody>
        </table></div>
        <div class="note key">
          <span class="nh">ขั้นที่ต้องทำก่อนทุกอย่าง · แยกสองก้อนออกจากกัน</span>
          <b>ก้อนของหุ้นบุริมสิทธิ</b> = 20,000 บาท<br>
          <b>ก้อนของหุ้นสามัญ</b> = ทุนหุ้นสามัญ 20,000 + ส่วนเกินมูลค่า 10,000 + กำไรสะสม 30,000 = <b>60,000 บาท</b><br>
          ถ้าเผลอเอา 80,000 ทั้งก้อนไปคูณ 80 เปอร์เซ็นต์ คำตอบจะผิดทันที เพราะบริษัทใหญ่ซื้อแต่หุ้นสามัญ
        </div>
        <h3>การคำนวณค่าความนิยม</h3>
        <div class="tw"><table class="tbl">
          <tbody>
            <tr><td class="k">สิ่งตอบแทนโอนให้</td><td class="m"></td><td class="m">63,000</td></tr>
            <tr><td class="k">มูลค่าของส่วนได้เสียที่ไม่มีอำนาจควบคุม</td><td class="m"></td><td class="m"></td></tr>
            <tr><td>&nbsp;&nbsp;&nbsp;หุ้นบุริมสิทธิ <span class="mono">ทั้งก้อน</span></td><td class="m">20,000</td><td class="m"></td></tr>
            <tr><td>&nbsp;&nbsp;&nbsp;หุ้นสามัญ <span class="mono">20% &times; 75,000</span></td><td class="m">15,000</td><td class="m">35,000</td></tr>
            <tr class="tot"><td class="k">รวม</td><td class="m"></td><td class="m">98,000</td></tr>
            <tr><td class="k">มูลค่ายุติธรรมของสินทรัพย์สุทธิที่ระบุได้ของบริษัทย่อย</td><td class="m"></td><td class="m"></td></tr>
            <tr><td>&nbsp;&nbsp;&nbsp;<span class="mono">(20,000 + 60,000) + 15,000</span></td><td class="m"></td><td class="m">95,000</td></tr>
            <tr class="tot2"><td class="k">ค่าความนิยม</td><td class="m"></td><td class="m">3,000</td></tr>
          </tbody>
        </table></div>
        <div class="note warn">
          <span class="nh">ตัวเลข 75,000 มาจากไหน · จุดที่พลาดกันมากที่สุด</span>
          <b>75,000 = ส่วนของหุ้นสามัญ 60,000 + สิทธิบัตร 15,000</b> · สังเกตว่า<b>ไม่รวมหุ้นบุริมสิทธิ 20,000</b> เข้ามาด้วย<br>
          เหตุผลคือ สิทธิบัตรที่ยังไม่ได้บันทึกเป็น<b>มูลค่าส่วนเพิ่มที่ตกเป็นของผู้ถือหุ้นสามัญ</b> ส่วนผู้ถือหุ้นบุริมสิทธิได้แค่สิทธิตามที่ตราไว้ ไม่ได้ส่วนแบ่งในมูลค่าเพิ่มของกิจการ · ฐานของ NCI ฝั่งหุ้นสามัญจึงเป็น 75,000 ไม่ใช่ 95,000
        </div>
        <div class="note">
          <span class="nh">ทำไม NCI ฝั่งหุ้นบุริมสิทธิจึงเป็น 20,000 เต็มจำนวน</span>
          เพราะโจทย์บอกว่าบริษัทใหญ่ซื้อ<b>หุ้นสามัญ</b> 80 เปอร์เซ็นต์เท่านั้น ไม่ได้ซื้อหุ้นบุริมสิทธิเลยแม้แต่หุ้นเดียว · หุ้นบุริมสิทธิทั้งหมดจึงอยู่ในมือคนนอก และเข้า NCI ทั้งก้อน 100 เปอร์เซ็นต์
        </div>
      </div>
    </section>

    <section class="sec" id="c6s-4">
      <div class="sec-h"><span class="sec-n">4</span><h2>กรณีบริษัทใหญ่ถือหุ้นสามัญของบริษัทย่อยเท่านั้น</h2></div>
      <div class="body">
        <p class="lede">กรณีนี้คือกรณีปกติ และหลักมีอยู่ข้อเดียวคือ<b>ผู้ถือหุ้นบุริมสิทธิได้ก่อน ที่เหลือจึงเป็นของผู้ถือหุ้นสามัญ</b></p>
        <h3>ลำดับการแบ่งกำไรสุทธิของบริษัทย่อย</h3>
        <div class="tw"><table class="tbl">
          <thead><tr><th>ขั้น</th><th>แบ่งให้ใคร</th><th>คิดอย่างไร</th></tr></thead>
          <tbody>
            <tr><td class="m">1</td><td class="k">ผู้ถือหุ้นบุริมสิทธิ</td>
                <td>คิด<b>ก่อน</b>เสมอ ตาม<b>อัตราที่ตราไว้คูณราคาตราไว้</b> เช่น หุ้นบุริมสิทธิ 3 เปอร์เซ็นต์ ทุน 20,000 ก็ได้ส่วนแบ่ง 600 บาทต่อปี</td></tr>
            <tr><td class="m">2</td><td class="k">ผู้ถือหุ้นสามัญ</td>
                <td><b>ส่วนที่เหลือทั้งหมด</b> แล้วจึงแบ่งต่อระหว่าง<b>บริษัทใหญ่</b>กับ <b>NCI</b> ตามสัดส่วนการถือหุ้นสามัญ</td></tr>
          </tbody>
        </table></div>
        <div class="note key">
          <span class="nh">สิ่งที่ต้องทำในงบฐานะการเงินรวม</span>
          <b>โอนส่วนของผู้ถือหุ้นบุริมสิทธิไปแสดงที่ส่วนได้เสียที่ไม่มีอำนาจควบคุม</b> · เพราะบริษัทใหญ่ไม่ได้ถือหุ้นบุริมสิทธิเลย ส่วนนั้นจึงเป็นของคนนอกทั้งหมด
        </div>
        <h3>แผนภาพการไหลของกำไร</h3>
        <div class="tw"><table class="tbl">
          <tbody>
            <tr><td class="k">กำไรสุทธิของบริษัทย่อย</td><td class="m">XXX</td></tr>
            <tr><td>&nbsp;&nbsp;<b>ลบ</b> ส่วนแบ่งของผู้ถือหุ้นบุริมสิทธิ</td><td class="m el">(XX)</td></tr>
            <tr class="tot"><td class="k">ส่วนที่เหลือ · ของผู้ถือหุ้นสามัญ</td><td class="m">XXX</td></tr>
            <tr><td>&nbsp;&nbsp;แบ่งให้<b>บริษัทใหญ่</b> ตามสัดส่วนหุ้นสามัญ เช่น 80 เปอร์เซ็นต์</td><td class="m hi">XX</td></tr>
            <tr><td>&nbsp;&nbsp;แบ่งให้ <b>NCI</b> ส่วนที่เหลือ เช่น 20 เปอร์เซ็นต์</td><td class="m hi">XX</td></tr>
          </tbody>
        </table></div>
        <div class="note warn">
          <span class="nh">อย่าลืมว่า NCI มีสองก้อน</span>
          ในงบฐานะการเงินรวม ยอด NCI ของกรณีนี้ประกอบด้วย<b>ส่วนของผู้ถือหุ้นบุริมสิทธิทั้งก้อน</b> บวกกับ<b>ส่วนแบ่งของผู้ถือหุ้นสามัญที่เป็นของคนนอก</b> · เวลาทำข้อสอบให้เขียนแยกสองบรรทัดเสมอ แล้วค่อยรวม จะไม่หล่นก้อนใดก้อนหนึ่ง
        </div>
      </div>
    </section>

    <section class="sec" id="c6s-5">
      <div class="sec-h"><span class="sec-n">5</span><h2>กรณีบริษัทใหญ่ถือทั้งหุ้นสามัญและหุ้นบุริมสิทธิ</h2></div>
      <div class="body">
        <p class="lede">พอบริษัทใหญ่ถือหุ้นบุริมสิทธิด้วย ก้อนของหุ้นบุริมสิทธิก็<b>ไม่ได้เป็นของคนนอกทั้งหมดอีกต่อไป</b> ต้องแบ่งกันอีกชั้นหนึ่ง</p>
        <ul class="list">
          <li>เนื่องจากบริษัทใหญ่ถือหุ้นบุริมสิทธิด้วย จึง<b>ได้ส่วนแบ่งจากกำไรของผู้ถือหุ้นบุริมสิทธิตามสัดส่วนที่ถืออยู่</b></li>
          <li><b>กำไรสุทธิส่วนที่เหลือ</b>จึงถูกแบ่งให้ผู้ถือหุ้นสามัญเหมือนเดิม</li>
          <li>ในงบฐานะการเงินรวม ต้อง<b>ตัดบัญชีเงินลงทุนในหุ้นบุริมสิทธิกับส่วนของผู้ถือหุ้นบุริมสิทธิ</b> แล้ว<b>ตั้งส่วนที่เหลือไว้ในส่วนได้เสียที่ไม่มีอำนาจควบคุม</b></li>
        </ul>
        <div class="note key">
          <span class="nh">รายการตัดบัญชีของก้อนหุ้นบุริมสิทธิ</span>
          สมมติบริษัทใหญ่ถือหุ้นบุริมสิทธิ 60 เปอร์เซ็นต์ ส่วนที่เหลือ 40 เปอร์เซ็นต์อยู่กับคนนอก
        </div>
        <div class="je je-solo">
          <div class="je-side"><div class="je-head">รายการตัดบัญชี · ก้อนหุ้นบุริมสิทธิ</div><div class="je-body">
            <table class="je-t">
              <tr><td class="dr">Dr. ทุน-หุ้นบุริมสิทธิ <span class="mono">100%</span></td><td class="amt">XXX</td></tr>
              <tr><td class="cr">Cr. เงินลงทุนในหุ้นบุริมสิทธิ <span class="mono">60%</span></td><td class="amt">XX</td></tr>
              <tr><td class="cr">Cr. ส่วนได้เสียที่ไม่มีอำนาจควบคุม <span class="mono">40%</span></td><td class="amt">XX</td></tr>
            </table>
            <p class="je-note">ตัดทุนหุ้นบุริมสิทธิออกเต็มจำนวน แล้วโยนกลับเป็นสองทาง คือส่วนที่บริษัทใหญ่ถือไปล้างกับเงินลงทุน และส่วนที่คนนอกถือไปตั้งเป็น NCI</p>
          </div></div>
        </div>
        <h3>หน้าตาของกระดาษทำการงบฐานะการเงิน</h3>
        <p>สไลด์วางผังไว้แบบนี้ · ตัวอักษร <span class="mono">B</span> คือรายการตัดก้อน<b>หุ้นบุริมสิทธิ</b> และ <span class="mono">D</span> คือรายการตัดก้อน<b>หุ้นสามัญ</b>ตามปกติ</p>
        <div class="tw"><table class="tbl">
          <thead><tr><th>31/12/25x1 · งบฐานะการเงิน</th><th>P</th><th>S</th><th>ตัดบัญชี Dr.</th><th>ตัดบัญชี Cr.</th><th>งบรวม</th></tr></thead>
          <tbody>
            <tr><td class="k">Investment in subsidiary</td><td class="m">COST</td><td class="m"></td><td class="m"></td><td class="m el">D&nbsp;&nbsp;yy</td><td class="m">0</td></tr>
            <tr><td class="k">Investment in preferred s.</td><td class="m">COST</td><td class="m"></td><td class="m"></td><td class="m el">B&nbsp;&nbsp;xx</td><td class="m">0</td></tr>
            <tr><td class="k">Common stock &ndash; P</td><td class="m">XXX</td><td class="m"></td><td class="m"></td><td class="m"></td><td class="m">XXX</td></tr>
            <tr><td class="k">R/E &ndash; P</td><td class="m">XXX</td><td class="m"></td><td class="m"></td><td class="m"></td><td class="m">XXX</td></tr>
            <tr><td class="k">Preferred stock &ndash; S</td><td class="m"></td><td class="m">XXX</td><td class="m el">B&nbsp;&nbsp;xx</td><td class="m"></td><td class="m">&ndash;</td></tr>
            <tr><td class="k">Common stock &ndash; S</td><td class="m"></td><td class="m">XXX</td><td class="m el">D&nbsp;&nbsp;yy</td><td class="m"></td><td class="m">&ndash;</td></tr>
            <tr><td class="k">R/E &ndash; S</td><td class="m"></td><td class="m">XXX</td><td class="m el">D&nbsp;&nbsp;yy</td><td class="m"></td><td class="m">&ndash;</td></tr>
            <tr><td class="k">Net profit &ndash; S</td><td class="m"></td><td class="m">XXX</td><td class="m el">D&nbsp;&nbsp;yy</td><td class="m"></td><td class="m">&ndash;</td></tr>
            <tr><td class="k">Dividends payment &ndash; S</td><td class="m"></td><td class="m">(XX)</td><td class="m"></td><td class="m el">D&nbsp;&nbsp;yy</td><td class="m">&ndash;</td></tr>
            <tr class="tot"><td class="k">ส่วนได้เสียที่ไม่มีอำนาจควบคุม</td><td class="m"></td><td class="m"></td><td class="m"></td><td class="m el">B&nbsp;&nbsp;xx<br>D&nbsp;&nbsp;yy</td><td class="m hi">XXX</td></tr>
          </tbody>
        </table></div>
        <div class="note">
          <span class="nh">อ่านผังนี้ให้ออก</span>
          สังเกตว่ายอด <b>NCI</b> บรรทัดล่างสุดรับของมาจาก<b>สองรายการ</b> คือ <span class="mono">B</span> ที่มาจากก้อนหุ้นบุริมสิทธิ และ <span class="mono">D</span> ที่มาจากก้อนหุ้นสามัญ · นี่คือภาพเดียวกับที่หัวข้อ 4 เตือนไว้ว่า NCI มีสองก้อนเสมอเมื่อบริษัทย่อยมีหุ้นบุริมสิทธิ
        </div>
      </div>
    </section>

    <section class="sec" id="c6s-6">
      <div class="sec-h"><span class="sec-n">6</span><h2>การซื้อหุ้นบริษัทย่อยระหว่างงวดบัญชี · หลักการ</h2></div>
      <div class="body">
        <div class="note key">
          <span class="nh">ประโยคที่ต้องขีดเส้นใต้</span>
          มูลค่ายุติธรรมของ<b>สินทรัพย์ที่ได้มาที่ระบุได้</b>และ<b>หนี้สินที่รับมา</b> วัดค่า <b>ณ วันที่ซื้อ</b> ซึ่งเป็นวันระหว่างงวดบัญชี <b>ไม่ใช่วันต้นปี</b>
        </div>
        <p>ฟังดูเป็นเรื่องเล็ก แต่มีผลสองชั้น ชั้นแรกคือ<b>ฐานที่ใช้คำนวณค่าความนิยมเปลี่ยน</b> เพราะส่วนของผู้ถือหุ้นของบริษัทย่อย ณ วันที่ซื้อ ไม่เท่ากับ ณ วันต้นปี · ชั้นที่สองคือ<b>กำไรของบริษัทย่อยช่วงต้นปีถึงวันซื้อไม่ใช่ของกลุ่ม</b></p>
        <h3>สองวิธีแสดงงบกำไรขาดทุนรวม</h3>
        <div class="grid g2">
          <div class="card">
            <span class="cn">วิธีที่ 1</span>
            <div class="ct">แสดงเฉพาะช่วงหลังซื้อ</div>
            <div class="cs">แสดง<b>ผลการดำเนินงานของบริษัทใหญ่ตลอดทั้งปี</b> รวมกับ<b>ผลการดำเนินงานของบริษัทย่อยนับจากวันซื้อหุ้น</b> · ตรงไปตรงมา ไม่ต้องมีบรรทัดหักอะไร</div>
          </div>
          <div class="card">
            <span class="cn">วิธีที่ 2</span>
            <div class="ct">แสดงเต็มปีแล้วหักออก</div>
            <div class="cs">แสดงผลการดำเนินงานของ<b>บริษัทใหญ่และบริษัทย่อยตลอดทั้งปี</b> แล้วแสดง<b>กำไรก่อนการซื้อหุ้น</b> <span class="mono">Preacquisition Income</span> เป็นรายการหักออกมาบรรทัดหนึ่ง</div>
          </div>
        </div>
        <h3>ตัวเลขเปรียบเทียบสองวิธีจากสไลด์</h3>
        <p>บริษัทใหญ่ถือ 80 เปอร์เซ็นต์ ซื้อเมื่อ <b>1 เมษายน 25x1</b> จึงรวมผลการดำเนินงานของบริษัทย่อยเพียง <b>9 เดือน</b> หรือ <span class="mono">3/4</span> ของปี</p>
        <div class="tw"><table class="tbl">
          <thead><tr><th></th><th>P<br><span class="mono">ทั้งปี</span></th><th>S<br><span class="mono">ทั้งปี</span></th><th>S<br><span class="mono">3/4 ปี</span></th><th>วิธีที่ 1</th><th>วิธีที่ 2</th></tr></thead>
          <tbody>
            <tr><td class="k">ขาย</td><td class="m">500</td><td class="m">400</td><td class="m">300</td><td class="m">800</td><td class="m">900</td></tr>
            <tr class="tot"><td class="k">ค่าใช้จ่าย</td><td class="m">180</td><td class="m">160</td><td class="m">120</td><td class="m">300</td><td class="m">340</td></tr>
            <tr><td class="k">กำไรสุทธิ</td><td class="m">320</td><td class="m">240</td><td class="m">180</td><td class="m">500</td><td class="m">560</td></tr>
            <tr><td class="k">หัก กำไรก่อนการซื้อหุ้น</td><td class="m"></td><td class="m"></td><td class="m"></td><td class="m">&ndash;</td><td class="m el">(60)</td></tr>
            <tr class="tot2"><td class="k">กำไรสุทธิรวม</td><td class="m"></td><td class="m"></td><td class="m"></td><td class="m hi">500</td><td class="m hi">500</td></tr>
          </tbody>
        </table></div>
        <div class="note">
          <span class="nh">ตรวจตัวเลขให้เห็นว่าสองวิธีลงเอยเท่ากัน</span>
          <b>กำไรก่อนซื้อ</b> = กำไรทั้งปีของบริษัทย่อย <span class="mono">(400 &minus; 160) &times; 3/12 = 60</span> ซึ่งคือกำไรของไตรมาสแรกที่ยังไม่ได้เป็นของกลุ่ม<br>
          วิธีที่ 1 ได้ <span class="mono">320 + 180 = 500</span> · วิธีที่ 2 ได้ <span class="mono">560 &minus; 60 = 500</span> · <b>เท่ากันเสมอ</b> ต่างกันแค่หน้าตาการนำเสนอ ไม่ใช่ต่างกันที่คำตอบ
        </div>
        <div class="note warn">
          <span class="nh">ข้อสมมติที่ซ่อนอยู่</span>
          การเอากำไรทั้งปีมาคูณเศษส่วนของเดือนแบบนี้ ใช้ได้ก็ต่อเมื่อสมมติว่า<b>รายได้และค่าใช้จ่ายเกิดสม่ำเสมอตลอดทั้งปี</b> · ถ้าโจทย์ให้กำไรแยกช่วงมาให้แล้ว ต้องใช้ตัวเลขที่โจทย์ให้ ห้ามเฉลี่ยเอง
        </div>
      </div>
    </section>

    <section class="sec" id="c6s-7">
      <div class="sec-h"><span class="sec-n">7</span><h2>ตัวอย่าง · ซื้อหุ้น 80 เปอร์เซ็นต์ เมื่อ 1 ตุลาคม</h2></div>
      <div class="body">
        <div class="note">
          <span class="nh">โจทย์ตามสไลด์</span>
          บริษัทใหญ่ซื้อหุ้นบริษัทย่อย <b>80 เปอร์เซ็นต์</b> เมื่อวันที่ <b>1 ตุลาคม 25x1</b> โดยจ่ายเงินสด <b>330,000 บาท</b><br>
          ส่วนของผู้ถือหุ้นของบริษัทย่อย<b>ต้นงวด</b>ประกอบด้วยทุนหุ้นสามัญ 100,000 บาท และกำไรสะสม 200,000 บาท<br>
          ณ วันที่ซื้อ บริษัทย่อยมี<b>สิทธิบัตรที่ไม่ได้บันทึกบัญชี</b> มูลค่ายุติธรรม <b>40,000 บาท</b> อายุให้ประโยชน์ <b>10 ปี</b><br>
          ในปี 25x1 บริษัทย่อยมีกำไรสุทธิ <b>9 เดือนแรก 80,000 บาท</b> และ<b>ตลอดทั้งปี 120,000 บาท</b><br>
          จ่ายเงินปันผลครั้งแรก <b>20,000 บาท สิ้นเดือนพฤษภาคม</b> และครั้งที่สอง <b>10,000 บาท สิ้นเดือนตุลาคม</b>
        </div>
        <h3>ขั้นที่ 1 · ส่วนของผู้ถือหุ้นของบริษัทย่อย ณ วันที่ซื้อ</h3>
        <div class="tw"><table class="tbl">
          <tbody>
            <tr><td class="k">ส่วนของผู้ถือหุ้น 1 มกราคม 25x1</td><td class="m"></td><td class="m"></td></tr>
            <tr><td>&nbsp;&nbsp;&nbsp;ทุนหุ้นสามัญ</td><td class="m">100,000</td><td class="m"></td></tr>
            <tr><td>&nbsp;&nbsp;&nbsp;กำไรสะสม</td><td class="m">200,000</td><td class="m">300,000</td></tr>
            <tr><td class="k">บวก กำไรสุทธิ 9 เดือนแรก</td><td class="m"></td><td class="m">80,000</td></tr>
            <tr><td class="k">หัก เงินปันผลจ่าย 31 พฤษภาคม 25x1</td><td class="m"></td><td class="m el">(20,000)</td></tr>
            <tr class="tot2"><td class="k">ส่วนของผู้ถือหุ้น 1 ตุลาคม 25x1</td><td class="m"></td><td class="m hi">360,000</td></tr>
          </tbody>
        </table></div>
        <div class="note warn">
          <span class="nh">ทำไมหักแค่เงินปันผลก้อนแรก</span>
          เพราะเงินปันผลก้อนที่สอง <b>10,000 บาท จ่ายสิ้นเดือนตุลาคม ซึ่งอยู่หลังวันซื้อ</b> จึงยังไม่กระทบส่วนของผู้ถือหุ้น ณ วันที่ 1 ตุลาคม · ก้อนที่สองจะไปโผล่อีกทีตอนทำกระดาษทำการ ในฐานะเงินปันผลรับของบริษัทใหญ่
        </div>
        <h3>ขั้นที่ 2 · คำนวณค่าความนิยม ณ 1 ตุลาคม 25x1</h3>
        <div class="tw"><table class="tbl">
          <tbody>
            <tr><td class="k">สิ่งตอบแทนโอนให้</td><td class="m">330,000</td></tr>
            <tr><td class="k">ส่วนได้เสียที่ไม่มีอำนาจควบคุม <span class="mono">20% &times; (360,000 + 40,000)</span></td><td class="m">80,000</td></tr>
            <tr class="tot"><td class="k">รวม</td><td class="m">410,000</td></tr>
            <tr><td class="k">มูลค่ายุติธรรมของสินทรัพย์สุทธิที่ระบุได้ของบริษัทย่อย</td><td class="m">400,000</td></tr>
            <tr class="tot2"><td class="k">ค่าความนิยม</td><td class="m hi">10,000</td></tr>
          </tbody>
        </table></div>
        <div class="note key">
          <span class="nh">เลข 400,000 มาจากไหน</span>
          <b>400,000 = ส่วนของผู้ถือหุ้น ณ วันซื้อ 360,000 + สิทธิบัตรที่ยังไม่ได้บันทึก 40,000</b><br>
          สิทธิบัตรเป็น<b>สินทรัพย์ที่ระบุได้ซึ่งบริษัทย่อยไม่เคยบันทึก</b> แต่กลุ่มต้องรับรู้ ณ วันซื้อ เพราะมาตรฐานให้วัดสินทรัพย์ที่ระบุได้ทุกตัวด้วยมูลค่ายุติธรรม ไม่ว่าบริษัทย่อยจะเคยบันทึกหรือไม่
        </div>
      </div>
    </section>

    <section class="sec" id="c6s-8">
      <div class="sec-h"><span class="sec-n">8</span><h2>วิธีส่วนได้เสียและกระดาษทำการงบกำไรขาดทุน</h2></div>
      <div class="body">
        <h3>ขั้นที่ 3 · บัญชีเงินลงทุนตามวิธีส่วนได้เสีย ณ สิ้นปี</h3>
        <div class="tw"><table class="tbl">
          <tbody>
            <tr><td class="k">ส่วนของผู้ถือหุ้นของบริษัทย่อย ณ 31/12/25x1</td>
                <td class="m"><span class="mono">300,000 + 120,000 &minus; (20,000 + 10,000)</span></td><td class="m">390,000</td></tr>
            <tr><td class="k">เงินลงทุนในบริษัทย่อย ณ 31/12/25x1</td>
                <td class="m"><span class="mono">80%(390,000) + 80%(40,000 &minus; 1,000) + 10,000</span></td><td class="m hi">353,200</td></tr>
            <tr class="tot2"><td class="k">ผลต่างจากเงินลงทุนที่เพิ่มขึ้น</td>
                <td class="m"><span class="mono">353,200 &minus; 330,000</span></td><td class="m hi">23,200</td></tr>
          </tbody>
        </table></div>
        <div class="note">
          <span class="nh">แกะสูตรเงินลงทุนทีละก้อน</span>
          <b>80%(390,000) = 312,000</b> คือส่วนแบ่งในส่วนของผู้ถือหุ้นตามบัญชีของบริษัทย่อย<br>
          <b>80%(40,000 &minus; 1,000) = 31,200</b> คือส่วนแบ่งในสิทธิบัตรที่ตัดจำหน่ายไปแล้ว 3 เดือน · ค่าตัดจำหน่าย <span class="mono">40,000 &divide; 10 &times; 3/12 = 1,000</span><br>
          <b>+ 10,000</b> คือค่าความนิยมซึ่งไม่ตัดจำหน่าย<br>
          รวม <span class="mono">312,000 + 31,200 + 10,000 = 353,200</span>
        </div>
        <div class="note warn">
          <span class="nh">ทำไมตัดจำหน่ายแค่ 3 เดือน</span>
          เพราะสิทธิบัตรถูกรับรู้<b>ณ วันที่ซื้อคือ 1 ตุลาคม</b> ไม่ใช่ต้นปี · ปีแรกจึงตัดจำหน่ายเพียง<b>ตุลาคมถึงธันวาคม</b> · ข้อสอบชอบดักตรงนี้ด้วยการให้ตัดเต็มปีเป็นตัวลวง
        </div>
        <h3>กระดาษทำการงบกำไรขาดทุน ณ 31/12/25x1</h3>
        <div class="tw"><table class="tbl">
          <thead><tr><th>งบกำไรขาดทุน</th><th>P</th><th>S<br><span class="mono">เฉพาะหลังซื้อ</span></th><th>ตัดบัญชี Dr.</th><th>ตัดบัญชี Cr.</th><th>งบรวม</th></tr></thead>
          <tbody>
            <tr><td class="k">เงินปันผลรับ</td><td class="m">8,000</td><td class="m"></td><td class="m el">B&nbsp;&nbsp;8,000</td><td class="m"></td><td class="m">&ndash;</td></tr>
            <tr><td class="k">ค่าใช้จ่าย · ค่าตัดจำหน่ายสิทธิบัตร</td><td class="m"></td><td class="m"></td><td class="m el">A&nbsp;&nbsp;1,000</td><td class="m"></td><td class="m">1,000</td></tr>
            <tr><td class="k">กำไรสุทธิ &ndash; P</td><td class="m"></td><td class="m"></td><td class="m el">C&nbsp;&nbsp;31,200</td><td class="m el">B&nbsp;&nbsp;8,000</td><td class="m hi">X + 23,200</td></tr>
            <tr><td class="k">กำไรสุทธิ &ndash; S</td><td class="m"></td><td class="m">40,000</td><td class="m"></td><td class="m el">A&nbsp;&nbsp;1,000<br>C&nbsp;&nbsp;39,000</td><td class="m">&ndash;</td></tr>
            <tr class="tot2"><td class="k">กำไรสุทธิ &ndash; NCI</td><td class="m"></td><td class="m"></td><td class="m el">C&nbsp;&nbsp;7,800</td><td class="m"></td><td class="m hi">7,800</td></tr>
          </tbody>
        </table></div>
        <div class="note key">
          <span class="nh">ที่มาของตัวเลขทุกตัวในกระดาษทำการ</span>
          <b>เงินปันผลรับ 8,000</b> = <span class="mono">10,000 &times; 80%</span> · <b>เฉพาะก้อนที่สอง</b>ที่จ่ายหลังวันซื้อเท่านั้น ก้อนแรกเดือนพฤษภาคมบริษัทใหญ่ยังไม่ได้ถือหุ้น<br>
          <b>กำไรสุทธิ S 40,000</b> = <span class="mono">120,000 &minus; 80,000</span> คือกำไรไตรมาสสุดท้ายซึ่งเป็นช่วงหลังซื้อ<br>
          <b>C 39,000</b> = <span class="mono">40,000 &minus; 1,000</span> คือกำไรหลังซื้อหลังปรับค่าตัดจำหน่ายสิทธิบัตรแล้ว<br>
          <b>C 31,200</b> = <span class="mono">80% &times; 39,000</span> ส่วนของบริษัทใหญ่ · <b>C 7,800</b> = <span class="mono">20% &times; 39,000</span> ส่วนของ NCI<br>
          ตรวจยอด <span class="mono">31,200 + 7,800 = 39,000</span> ลงตัวพอดี
        </div>
      </div>
    </section>

    <section class="sec" id="c6s-9">
      <div class="sec-h"><span class="sec-n">9</span><h2>กระดาษทำการงบฐานะการเงิน</h2></div>
      <div class="body">
        <div class="tw"><table class="tbl">
          <thead><tr><th>31/12/25x1 · งบฐานะการเงิน</th><th>P</th><th>S</th><th>ตัดบัญชี Dr.</th><th>ตัดบัญชี Cr.</th><th>งบรวม</th></tr></thead>
          <tbody>
            <tr><td class="k">เงินลงทุนในบริษัทย่อย</td><td class="m">330,000</td><td class="m"></td>
                <td class="m el">A&nbsp;&nbsp;23,200<br>C&nbsp;&nbsp;800</td>
                <td class="m el">B&nbsp;&nbsp;32,000<br>D&nbsp;&nbsp;10,000<br>E&nbsp;&nbsp;312,000</td><td class="m">0</td></tr>
            <tr><td class="k">สิทธิบัตร</td><td class="m"></td><td class="m"></td><td class="m el">B&nbsp;&nbsp;40,000</td><td class="m el">C&nbsp;&nbsp;1,000</td><td class="m hi">39,000</td></tr>
            <tr><td class="k">ค่าความนิยม</td><td class="m"></td><td class="m"></td><td class="m el">D&nbsp;&nbsp;10,000</td><td class="m"></td><td class="m hi">10,000</td></tr>
            <tr><td class="k">กำไรสุทธิ &ndash; P</td><td class="m"></td><td class="m"></td><td class="m"></td><td class="m el">A&nbsp;&nbsp;23,200</td><td class="m">X + 23,200</td></tr>
            <tr><td class="k">ทุนหุ้นสามัญ &ndash; S</td><td class="m"></td><td class="m">100,000</td><td class="m el">E&nbsp;&nbsp;100,000</td><td class="m"></td><td class="m">0</td></tr>
            <tr><td class="k">กำไรสะสม &ndash; S</td><td class="m"></td><td class="m">200,000</td><td class="m el">E&nbsp;&nbsp;200,000</td><td class="m"></td><td class="m">0</td></tr>
            <tr><td class="k">กำไรสุทธิ &ndash; S</td><td class="m"></td><td class="m">120,000</td><td class="m el">E&nbsp;&nbsp;120,000</td><td class="m"></td><td class="m">0</td></tr>
            <tr><td class="k">เงินปันผลจ่าย &ndash; S</td><td class="m"></td><td class="m">(30,000)</td><td class="m"></td><td class="m el">E&nbsp;&nbsp;30,000</td><td class="m">0</td></tr>
            <tr class="tot2"><td class="k">ส่วนได้เสียที่ไม่มีอำนาจควบคุม</td><td class="m"></td><td class="m"></td>
                <td class="m el">C&nbsp;&nbsp;200</td>
                <td class="m el">B&nbsp;&nbsp;8,000<br>E&nbsp;&nbsp;78,000</td><td class="m hi">85,800</td></tr>
          </tbody>
        </table></div>
        <h3>รายการตัดบัญชีทั้งห้าตัวทำอะไรบ้าง</h3>
        <div class="tw"><table class="tbl">
          <thead><tr><th>รายการ</th><th>ทำอะไร</th></tr></thead>
          <tbody>
            <tr><td class="k"><span class="mono">A</span></td><td><b>ปรับบัญชีเงินลงทุนให้เป็นวิธีส่วนได้เสีย</b> บวกเข้าไป 23,200 ตามที่คำนวณในหัวข้อ 8</td></tr>
            <tr><td class="k"><span class="mono">B</span></td><td><b>ตั้งสิทธิบัตรที่ยังไม่ได้บันทึก</b> 40,000 แล้วแบ่งเป็นของบริษัทใหญ่ 32,000 กับของ NCI 8,000 ตามสัดส่วน 80 ต่อ 20</td></tr>
            <tr><td class="k"><span class="mono">C</span></td><td><b>ตัดจำหน่ายสิทธิบัตร 3 เดือน</b> 1,000 แล้วแบ่งภาระเป็นของบริษัทใหญ่ 800 กับของ NCI 200</td></tr>
            <tr><td class="k"><span class="mono">D</span></td><td><b>แยกค่าความนิยม</b> 10,000 ออกมาตั้งเป็นสินทรัพย์ของกลุ่ม</td></tr>
            <tr><td class="k"><span class="mono">E</span></td><td><b>ตัดส่วนของผู้ถือหุ้นของบริษัทย่อยทั้งก้อน</b> แล้วโยนเป็นสองทาง คือล้างกับเงินลงทุน 312,000 และตั้ง NCI 78,000</td></tr>
          </tbody>
        </table></div>
        <div class="note key">
          <span class="nh">ตรวจยอด NCI สองทางให้ตรงกัน</span>
          <b>ทางกระดาษทำการ</b> <span class="mono">78,000 + 8,000 &minus; 200 = 85,800</span><br>
          <b>ทางคำนวณตรง</b> <span class="mono">20% &times; (390,000 + 40,000 &minus; 1,000) = 20% &times; 429,000 = 85,800</span><br>
          ถ้าสองทางไม่ตรงกัน แปลว่าลืมแบ่งสิทธิบัตรหรือค่าตัดจำหน่ายให้ NCI · ให้ไล่กลับไปดูรายการ <span class="mono">B</span> กับ <span class="mono">C</span> ก่อนเสมอ
        </div>
        <div class="note warn">
          <span class="nh">สิ่งที่ไม่มีในกระดาษทำการนี้</span>
          สังเกตว่า<b>ไม่มีบรรทัดกำไรก่อนการซื้อหุ้น</b> เพราะกระดาษทำการนี้ใช้<b>วิธีที่ 1</b> คือเอากำไรของบริษัทย่อยมาเฉพาะช่วงหลังซื้อ 40,000 ตั้งแต่แรก · ถ้าโจทย์สั่งให้ใช้วิธีที่ 2 ต้องเอากำไรทั้งปี 120,000 มาตั้ง แล้วเพิ่มบรรทัดหักกำไรก่อนซื้อ 80,000 เข้าไป
        </div>
      </div>
    </section>

    <section class="sec" id="c6s-10">
      <div class="sec-h"><span class="sec-n">10</span><h2>การเปลี่ยนแปลงสัดส่วน · วัดค่าความนิยมเมื่อใด</h2></div>
      <div class="body">
        <p class="lede">หัวข้อนี้มีคำถามเดียวที่ต้องตอบให้ถูก คือ<b>ซื้อหุ้นเพิ่มทุกครั้งต้องคำนวณค่าความนิยมใหม่หรือไม่</b> และคำตอบคือ<b>ไม่</b></p>
        <div class="note key">
          <span class="nh">กฎข้อเดียวที่คุมทั้งหัวข้อ</span>
          <b>คำนวณค่าความนิยมเฉพาะ ณ วันที่ได้อำนาจควบคุมเท่านั้น</b> · ก่อนหน้านั้นเป็นเงินลงทุนธรรมดา และหลังจากนั้นการซื้อเพิ่มถือเป็น<b>รายการในส่วนของเจ้าของ</b> ไม่ใช่การรวมธุรกิจอีกแล้ว
        </div>
        <h3>ไล่ตัวอย่างในโน้ตของอาจารย์</h3>
        <div class="tw"><table class="tbl">
          <thead><tr><th>ครั้งที่</th><th>ซื้อเพิ่ม</th><th>สะสม</th><th>มีอำนาจควบคุมหรือยัง</th><th>คำนวณค่าความนิยมไหม</th></tr></thead>
          <tbody>
            <tr><td class="m">1</td><td class="m">15%</td><td class="m">15%</td><td>ยัง</td><td>ไม่</td></tr>
            <tr><td class="m">2</td><td class="m">20%</td><td class="m">35%</td><td>ยัง</td><td>ไม่</td></tr>
            <tr class="tot"><td class="m">3</td><td class="m">25%</td><td class="m hi">60%</td><td class="hi"><b>ได้อำนาจควบคุมตรงนี้</b></td><td class="hi"><b>คำนวณ ณ วันนี้</b></td></tr>
            <tr><td class="m">4</td><td class="m">15%</td><td class="m">75%</td><td>ควบคุมอยู่แล้ว</td><td>ไม่ · เป็นรายการในส่วนของเจ้าของ</td></tr>
          </tbody>
        </table></div>
        <h3>วิธีวัดค่าความนิยม ณ วันที่ได้อำนาจควบคุม</h3>
        <p>ค่าความนิยมคือ<b>ส่วนต่างของสองก้อน คือก้อนที่ 1 ลบก้อนที่ 2</b></p>
        <div class="tw"><table class="tbl">
          <thead><tr><th>ก้อน</th><th>ประกอบด้วย</th></tr></thead>
          <tbody>
            <tr><td class="k">ก้อนที่ 1</td>
                <td><b>สิ่งตอบแทนโอนให้</b> วัดด้วยมูลค่ายุติธรรม ณ วันที่ซื้อ<br>
                    <b>บวก ส่วนได้เสียที่ไม่มีอำนาจควบคุม</b> วัดด้วยมูลค่ายุติธรรม หรือมูลค่ายุติธรรมของสินทรัพย์สุทธิที่ระบุได้ตามสัดส่วนของ NCI<br>
                    <b>บวก มูลค่ายุติธรรม ณ วันที่ซื้อ ของหุ้นที่ถืออยู่ก่อนหน้า</b></td></tr>
            <tr><td class="k">ก้อนที่ 2</td>
                <td><b>มูลค่าสุทธิ ณ วันที่ซื้อ ของสินทรัพย์ที่ระบุได้ที่ได้มาและหนี้สินที่รับมา</b> วัดมูลค่าด้วยมูลค่ายุติธรรม</td></tr>
          </tbody>
        </table></div>
        <div class="note warn">
          <span class="nh">ก้อนที่มักลืม</span>
          <b>มูลค่ายุติธรรมของหุ้นที่ถืออยู่ก่อนหน้า</b> คือบรรทัดที่คนลืมบ่อยที่สุด · มาตรฐานให้<b>วัดหุ้นเดิมใหม่ด้วยมูลค่ายุติธรรม ณ วันที่ได้อำนาจควบคุม</b> และ<b>ผลต่างจากราคาตามบัญชีเดิมรับรู้เป็นกำไรหรือขาดทุนทันที</b> · เท่ากับว่ามาตรฐานมองว่ากลุ่ม<b>ขายหุ้นเดิมทิ้งแล้วซื้อกลับมาใหม่ทั้งก้อน</b> ณ วันที่คุมได้
        </div>
      </div>
    </section>

    <section class="sec" id="c6s-11">
      <div class="sec-h"><span class="sec-n">11</span><h2>ตัวอย่างที่ 6.4 · การซื้อหุ้นสามัญเพิ่มเป็นขั้น</h2></div>
      <div class="body">
        <div class="tw"><table class="tbl">
          <thead><tr><th>วันที่</th><th>ซื้อหุ้น</th><th>จ่ายเงินสด</th><th>SE:S<br>1/1</th><th>NI:S<br>ทั้งปี</th><th>SE:S<br>วันซื้อ</th><th>SE:S<br>31/12</th><th>NI:S<br>ก่อนวันซื้อ</th></tr></thead>
          <tbody>
            <tr><td class="k">1/7/25x3</td><td class="m hi">10%</td><td class="m">17,000</td><td class="m">100,000</td><td class="m">50,000</td><td class="m">125,000</td><td class="m">150,000</td><td class="m">25,000</td></tr>
            <tr><td class="k">1/4/25x4</td><td class="m hi">50%</td><td class="m">90,000</td><td class="m">150,000</td><td class="m">40,000</td><td class="m">160,000</td><td class="m">190,000</td><td class="m">10,000</td></tr>
            <tr><td class="k">1/10/25x5</td><td class="m hi">15%</td><td class="m">44,300</td><td class="m">190,000</td><td class="m">40,000</td><td class="m">220,000</td><td class="m">222,000</td><td class="m">30,000</td></tr>
          </tbody>
        </table></div>
        <p class="je-cap">จ่ายเงินปันผล 8,000 บาท เมื่อ 31/12/25x5</p>
        <div class="note">
          <span class="nh">ตรวจตัวเลขในตารางให้เห็นที่มา</span>
          <b>แถวแรก</b> ซื้อ 1 กรกฎาคม คือผ่านไปครึ่งปี · <span class="mono">SE วันซื้อ = 100,000 + 50,000 &times; 6/12 = 125,000</span> และ <span class="mono">SE 31/12 = 100,000 + 50,000 = 150,000</span><br>
          <b>แถวที่สอง</b> ซื้อ 1 เมษายน คือผ่านไป 3 เดือน · <span class="mono">160,000 = 150,000 + 40,000 &times; 3/12</span><br>
          <b>แถวที่สาม</b> ซื้อ 1 ตุลาคม คือผ่านไป 9 เดือน · <span class="mono">220,000 = 190,000 + 40,000 &times; 9/12</span> และ <span class="mono">SE 31/12 = 190,000 + 40,000 &minus; 8,000 = 222,000</span> ซึ่งหักเงินปันผลสิ้นปีออกแล้ว
        </div>
        <h3>การคำนวณค่าความนิยม ณ 1 เมษายน 25x4 · วันที่ได้อำนาจควบคุม</h3>
        <p>ถึงจุดนี้สัดส่วนสะสมเป็น <span class="mono">10% + 50% = 60%</span> จึงได้อำนาจควบคุม และ<b>นี่คือวันเดียวที่คำนวณค่าความนิยม</b></p>
        <div class="tw"><table class="tbl">
          <tbody>
            <tr><td class="k">สิ่งตอบแทนโอนให้ <span class="mono">50%</span></td><td class="m">90,000</td></tr>
            <tr><td class="k">ส่วนได้เสียที่ไม่มีอำนาจควบคุม <span class="mono">40% &times; 160,000</span></td><td class="m">64,000</td></tr>
            <tr><td class="k">มูลค่ายุติธรรมของหุ้นที่ถืออยู่ก่อนหน้า <span class="mono">10%</span></td><td class="m">17,700</td></tr>
            <tr class="tot"><td class="k">รวม</td><td class="m">171,700</td></tr>
            <tr><td class="k">มูลค่ายุติธรรมของสินทรัพย์สุทธิที่ระบุได้</td><td class="m">160,000</td></tr>
            <tr class="tot2"><td class="k">ค่าความนิยม</td><td class="m hi">11,700</td></tr>
          </tbody>
        </table></div>
        <div class="note key">
          <span class="nh">หุ้นเดิม 10 เปอร์เซ็นต์ · ราคาทุน 17,000 แต่ใส่ 17,700</span>
          ส่วนต่าง <b>700 บาท</b> คือ<b>กำไรจากการวัดมูลค่าหุ้นเดิมใหม่ด้วยมูลค่ายุติธรรม</b> ณ วันที่ได้อำนาจควบคุม · <b>รับรู้เป็นกำไรในกำไรหรือขาดทุนของบริษัทใหญ่ทันที</b> ไม่ได้เอาไปบวกกับค่าความนิยม<br>
          ถ้าเผลอใช้ราคาทุน 17,000 ค่าความนิยมจะกลายเป็น 11,000 ซึ่งผิด
        </div>
      </div>
    </section>

    <section class="sec" id="c6s-12">
      <div class="sec-h"><span class="sec-n">12</span><h2>ซื้อหุ้นเพิ่มโดยไม่สูญเสียการควบคุม</h2></div>
      <div class="body">
        <div class="note">
          <span class="nh">โจทย์ต่อจากตัวอย่างที่ 6.4</span>
          วันที่ <b>1 ตุลาคม 25x5</b> บริษัทใหญ่ซื้อหุ้นสามัญของบริษัทย่อยเพิ่มอีก <b>15 เปอร์เซ็นต์</b> · ร้อยละการถือหุ้นเพิ่มจาก <b>60 เป็น 75 เปอร์เซ็นต์</b> · เป็น<b>การเปลี่ยนแปลงสัดส่วนการถือหุ้นที่ไม่ทำให้เสียการควบคุม</b>
        </div>
        <div class="tw"><table class="tbl">
          <tbody>
            <tr><td class="k">สิ่งตอบแทนที่จ่ายในการซื้อหุ้นเพิ่มอีก 15 เปอร์เซ็นต์</td><td class="m">44,300</td></tr>
            <tr><td class="k">มูลค่าของส่วนได้เสียที่ไม่มีอำนาจควบคุมที่ซื้อมา <span class="mono">15% &times; 220,000</span></td><td class="m">33,000</td></tr>
            <tr class="tot2"><td class="k">ผลต่างจากการเปลี่ยนแปลงสัดส่วนการถือหุ้น <span class="mono">Dr.</span></td><td class="m hi">11,300</td></tr>
          </tbody>
        </table></div>
        <div class="note key">
          <span class="nh">ผลต่าง 11,300 ไปไหน · ประโยคที่สไลด์เน้นด้วยดาวสองข้าง</span>
          <b>แสดงในงบฐานะการเงินรวม</b> ในฐานะ<b>รายการในส่วนของเจ้าของ</b> · <b>ไม่ใช่ค่าความนิยม</b> และ<b>ไม่ใช่กำไรขาดทุน</b><br>
          เหตุผลคือกลุ่มยังควบคุมบริษัทย่อยอยู่เหมือนเดิมทั้งก่อนและหลังรายการ สิ่งที่เปลี่ยนคือ<b>การแบ่งเค้กระหว่างเจ้าของกลุ่มกับ NCI เท่านั้น</b> ไม่มีสินทรัพย์หรือธุรกิจใดถูกซื้อหรือขายออกไปจากกลุ่ม
        </div>
        <div class="je je-solo">
          <div class="je-side"><div class="je-head">รายการที่เกิดขึ้น</div><div class="je-body">
            <table class="je-t">
              <tr><td class="dr">Dr. ส่วนได้เสียที่ไม่มีอำนาจควบคุม</td><td class="amt">33,000</td></tr>
              <tr><td class="dr">Dr. ส่วนของเจ้าของ · ผลต่างจากการเปลี่ยนสัดส่วน</td><td class="amt">11,300</td></tr>
              <tr><td class="cr">Cr. เงินสด</td><td class="amt">44,300</td></tr>
            </table>
            <p class="je-note">ซื้อ NCI กลับมา 15 เปอร์เซ็นต์ ในราคาที่แพงกว่ามูลค่าตามบัญชีของ NCI ก้อนนั้น 11,300 บาท · ส่วนที่จ่ายแพงกว่าถูกหักออกจากส่วนของเจ้าของโดยตรง</p>
          </div></div>
        </div>
        <div class="note warn">
          <span class="nh">เทียบสองรายการนี้ให้ขาด</span>
          <b>1 เมษายน 25x4</b> ซื้อ 50 เปอร์เซ็นต์ แล้ว<b>ได้อำนาจควบคุม</b> → เป็น<b>การรวมธุรกิจ</b> → <b>คำนวณค่าความนิยม</b> และ<b>วัดหุ้นเดิมใหม่</b><br>
          <b>1 ตุลาคม 25x5</b> ซื้อ 15 เปอร์เซ็นต์ โดย<b>ควบคุมอยู่แล้ว</b> → เป็น<b>รายการในส่วนของเจ้าของ</b> → <b>ไม่มีค่าความนิยมใหม่</b> และ<b>ไม่วัดหุ้นเดิมใหม่</b><br>
          ทั้งสองรายการคือการซื้อหุ้นเพิ่มเหมือนกัน แต่คำตอบคนละเรื่องกันสิ้นเชิง เพราะ<b>สถานะการควบคุมก่อนทำรายการต่างกัน</b>
        </div>
      </div>
    </section>

    <section class="sec" id="c6s-13">
      <div class="sec-h"><span class="sec-n">13</span><h2>ขายหุ้นบางส่วนโดยไม่สูญเสียการควบคุม</h2></div>
      <div class="body">
        <div class="note rule">
          <span class="nh">หมายเหตุเรื่องที่มา</span>
          สไลด์มีหน้าชื่อเรื่อง <b>ตัวอย่างที่ 6.5 การขายหุ้นสามัญบางส่วน</b> แต่<b>ไม่มีเนื้อหาในหน้านั้น</b> · หัวข้อนี้จึงเขียนจาก<b>มาตรฐาน TFRS 10 และตำรา ไม่ได้มาจากสไลด์</b> ใส่ไว้ให้ครบตามหัวข้อที่สไลด์หน้าแรกประกาศไว้
        </div>
        <p class="lede">กรณีนี้เป็น<b>ภาพสะท้อนในกระจก</b>ของหัวข้อที่ 12 · หลักการเหมือนกันทุกประการ เปลี่ยนแค่ทิศทาง</p>
        <div class="note key">
          <span class="nh">หลักเดียวกับการซื้อเพิ่ม</span>
          ตราบใดที่<b>ยังควบคุมอยู่หลังการขาย</b> รายการนั้นเป็น<b>รายการในส่วนของเจ้าของ</b> · <b>ไม่รับรู้กำไรขาดทุนจากการขาย</b> และ<b>ไม่ปรับค่าความนิยม</b>
        </div>
        <h3>วิธีคิด</h3>
        <div class="tw"><table class="tbl">
          <tbody>
            <tr><td class="k">สิ่งตอบแทนที่ได้รับจากการขายหุ้น</td><td class="m">XXX</td></tr>
            <tr><td class="k">หัก มูลค่าตามบัญชีของส่วนได้เสียที่โอนไปให้ NCI</td><td class="m el">(XXX)</td></tr>
            <tr class="tot2"><td class="k">ผลต่าง · บันทึกใน<b>ส่วนของเจ้าของ</b> โดยตรง</td><td class="m hi">XXX</td></tr>
          </tbody>
        </table></div>
        <div class="je je-solo">
          <div class="je-side"><div class="je-head">ขายหุ้นบางส่วน · ยังควบคุมอยู่</div><div class="je-body">
            <table class="je-t">
              <tr><td class="dr">Dr. เงินสด</td><td class="amt">XXX</td></tr>
              <tr><td class="cr">Cr. ส่วนได้เสียที่ไม่มีอำนาจควบคุม</td><td class="amt">XX</td></tr>
              <tr><td class="cr">Cr. ส่วนของเจ้าของ · ผลต่างจากการเปลี่ยนสัดส่วน</td><td class="amt">XX</td></tr>
            </table>
            <p class="je-note">ขายส่วนได้เสียออกไปให้ NCI · ถ้าขายได้แพงกว่ามูลค่าตามบัญชีที่โอนไป ส่วนเกินเข้าส่วนของเจ้าของ ไม่ใช่กำไร</p>
          </div></div>
        </div>
        <div class="note warn">
          <span class="nh">จุดที่ข้อสอบชอบหลอก</span>
          โจทย์จะเล่าว่าบริษัทใหญ่<b>ขายหุ้นได้กำไร</b> แล้วถามว่ารับรู้กำไรเท่าไรในงบกำไรขาดทุนรวม · ถ้ายังควบคุมอยู่ คำตอบคือ<b>ศูนย์</b> · กำไรที่โจทย์พูดถึงเป็นกำไรใน<b>งบเฉพาะกิจการ</b>ของบริษัทใหญ่ ซึ่งคนละงบกับงบการเงินรวม
        </div>
      </div>
    </section>

    <section class="sec" id="c6s-14">
      <div class="sec-h"><span class="sec-n">14</span><h2>การสูญเสียการควบคุม</h2></div>
      <div class="body">
        <div class="note rule">
          <span class="nh">หมายเหตุเรื่องที่มา</span>
          สไลด์หน้าแรกประกาศหัวข้อนี้ไว้เป็น<b>กรณีที่ 4</b> แต่<b>ไม่มีหน้าเนื้อหาในชุดสไลด์เลย</b> · หัวข้อนี้จึงเขียนจาก<b>มาตรฐาน TFRS 10 และตำรา ไม่ได้มาจากสไลด์</b>
        </div>
        <p class="lede">นี่คือ<b>เส้นแบ่ง</b>ของทั้งบท · ตราบใดที่ยังควบคุม ทุกอย่างเป็นรายการในส่วนของเจ้าของ · พอ<b>ข้ามเส้นนี้ไป</b> ทุกอย่างกลับด้านหมด</p>
        <div class="tw"><table class="tbl">
          <thead><tr><th></th><th>เปลี่ยนสัดส่วนแต่<b>ยังควบคุม</b></th><th><b>สูญเสีย</b>การควบคุม</th></tr></thead>
          <tbody>
            <tr><td class="k">ลักษณะของรายการ</td><td>รายการในส่วนของเจ้าของ</td><td class="hi">รายการขายกิจการ</td></tr>
            <tr><td class="k">รับรู้กำไรขาดทุนไหม</td><td>ไม่</td><td class="hi">รับรู้ใน<b>กำไรหรือขาดทุน</b></td></tr>
            <tr><td class="k">ค่าความนิยมเดิม</td><td>คงไว้เหมือนเดิม</td><td class="hi"><b>ตัดออก</b>พร้อมบริษัทย่อย</td></tr>
            <tr><td class="k">เงินลงทุนส่วนที่เหลือ</td><td>ไม่เกี่ยว</td><td class="hi">วัดด้วย<b>มูลค่ายุติธรรม ณ วันที่สูญเสียการควบคุม</b></td></tr>
            <tr><td class="k">ยังทำงบรวมไหม</td><td>ทำต่อ</td><td class="hi"><b>เลิกทำ</b> เปลี่ยนไปใช้วิธีอื่นตามสถานะใหม่</td></tr>
          </tbody>
        </table></div>
        <h3>สิ่งที่ต้องทำ ณ วันที่สูญเสียการควบคุม</h3>
        <ul class="list">
          <li><b>ตัดรายการสินทรัพย์และหนี้สินของบริษัทย่อยออกจากงบรวมทั้งหมด</b> รวมทั้งค่าความนิยมที่เคยรับรู้ไว้</li>
          <li><b>ตัดยอดส่วนได้เสียที่ไม่มีอำนาจควบคุมของบริษัทย่อยนั้นออก</b></li>
          <li><b>รับรู้มูลค่ายุติธรรมของสิ่งตอบแทนที่ได้รับ</b></li>
          <li><b>วัดเงินลงทุนส่วนที่ยังถืออยู่ด้วยมูลค่ายุติธรรม ณ วันที่สูญเสียการควบคุม</b> แล้วใช้มูลค่านั้นเป็นราคาทุนเริ่มต้นของสถานะใหม่</li>
          <li><b>รับรู้ผลต่างทั้งหมดเป็นกำไรหรือขาดทุน</b> ในงบกำไรขาดทุนรวม</li>
          <li><b>จัดประเภทรายการในกำไรขาดทุนเบ็ดเสร็จอื่นที่เกี่ยวกับบริษัทย่อยนั้นใหม่</b> ตามที่มาตรฐานแต่ละฉบับกำหนด เสมือนว่ากลุ่มจำหน่ายสินทรัพย์และหนี้สินที่เกี่ยวข้องออกไปโดยตรง</li>
        </ul>
        <div class="note key">
          <span class="nh">สถานะใหม่หลังสูญเสียการควบคุม</span>
          ขึ้นอยู่กับว่าเหลืออิทธิพลแค่ไหน · ถ้ายังมี<b>อิทธิพลอย่างมีนัยสำคัญ</b> กลายเป็น<b>เงินลงทุนในบริษัทร่วม</b>ตาม TAS 28 ใช้วิธีส่วนได้เสีย · ถ้ามี<b>การควบคุมร่วม</b> กลายเป็น<b>การร่วมค้า</b> · ถ้า<b>ไม่เหลือทั้งสองอย่าง</b> กลายเป็น<b>เครื่องมือทางการเงิน</b>ตาม TFRS 9
        </div>
        <div class="note warn">
          <span class="nh">ประโยคที่ควรจำไปเข้าห้องสอบ</span>
          การวัดส่วนที่เหลือด้วยมูลค่ายุติธรรมหมายความว่า <b>กำไรขาดทุนที่รับรู้ไม่ได้มีแค่ส่วนของหุ้นที่ขายออกไปจริง แต่รวมส่วนของหุ้นที่ยังถืออยู่ด้วย</b> · ข้อสอบชอบให้คำนวณกำไรจากการขายเฉพาะหุ้นที่ขาย ซึ่งเป็นตัวลวงที่ตอบผิดกันมากที่สุดของหัวข้อนี้
        </div>
      </div>
    </section>

    <section class="sec" id="c6s-15">
      <div class="sec-h"><span class="sec-n">15</span><h2>บริษัทย่อยจ่ายหุ้นปันผล</h2></div>
      <div class="body">
        <p class="lede">กรณีสุดท้ายและง่ายที่สุด · สไลด์มีแค่สองบรรทัด แต่สองบรรทัดนี้ตอบคำถามทั้งหมดของหัวข้อ</p>
        <div class="note key">
          <span class="nh">สองบรรทัดจากสไลด์</span>
          <b>1.</b> โอน<b>กำไรสะสม</b>ไปเป็น<b>ทุนหุ้นสามัญ</b>อย่างถาวร<br>
          <b>2.</b> <b>ส่วนของผู้ถือหุ้นไม่เปลี่ยนแปลง</b>
        </div>
        <div class="tw"><table class="tbl">
          <thead><tr><th></th><th>ก่อนจ่ายหุ้นปันผล</th><th>หลังจ่ายหุ้นปันผล</th></tr></thead>
          <tbody>
            <tr><td class="k">ทุนหุ้นสามัญ</td><td class="m">100,000</td><td class="m hi">130,000</td></tr>
            <tr><td class="k">กำไรสะสม</td><td class="m">200,000</td><td class="m hi">170,000</td></tr>
            <tr class="tot2"><td class="k">รวมส่วนของผู้ถือหุ้น</td><td class="m">300,000</td><td class="m">300,000</td></tr>
          </tbody>
        </table></div>
        <div class="note">
          <span class="nh">ผลต่อการจัดทำงบการเงินรวม</span>
          เพราะ<b>ยอดรวมไม่เปลี่ยน</b> ค่าความนิยมจึงไม่เปลี่ยน ยอด NCI ก็ไม่เปลี่ยน และสัดส่วนการถือหุ้นก็ไม่เปลี่ยน เพราะผู้ถือหุ้นทุกคนได้หุ้นปันผล<b>ตามสัดส่วนเดิมที่ถืออยู่</b><br>
          สิ่งเดียวที่ต้องระวังคือ<b>รายการตัดบัญชีต้องตัดยอดตามบัญชีใหม่</b> คือตัดทุนหุ้นสามัญ 130,000 และกำไรสะสม 170,000 แทนที่จะเป็น 100,000 กับ 200,000
        </div>
        <div class="note warn">
          <span class="nh">อย่าสับสนกับเงินปันผลเงินสด</span>
          <b>เงินปันผลเงินสด</b>ทำให้<b>ส่วนของผู้ถือหุ้นลดลงจริง</b> และบริษัทใหญ่บันทึกเป็น<b>เงินปันผลรับ</b> ซึ่งต้องตัดออกในงบรวม<br>
          <b>หุ้นปันผล</b><b>ไม่ลดส่วนของผู้ถือหุ้นเลย</b> และบริษัทใหญ่<b>ไม่บันทึกรายได้ใด ๆ</b> แค่ได้จำนวนหุ้นเพิ่มขึ้นโดยมูลค่าเงินลงทุนเท่าเดิม
        </div>
      </div>
    </section>

    <section class="sec" id="c6s-16">
      <div class="sec-h"><span class="sec-n">16</span><h2>สรุปทั้งบทและจุดที่ข้อสอบชอบถาม</h2></div>
      <div class="body">
        <div class="tw"><table class="tbl">
          <thead><tr><th>กรณี</th><th>สิ่งที่ต้องตอบให้ได้ในหนึ่งประโยค</th></tr></thead>
          <tbody>
            <tr><td class="k">หุ้นบุริมสิทธิ</td>
                <td>หุ้นบุริมสิทธิ<b>ไม่มีสิทธิออกเสียง</b> ส่วนที่บริษัทใหญ่ไม่ได้ถือจึงเป็น <b>NCI</b> ทั้งก้อน และฐานของหุ้นสามัญต้อง<b>กันส่วนของหุ้นบุริมสิทธิออกก่อน</b></td></tr>
            <tr><td class="k">ซื้อระหว่างงวด</td>
                <td>วัดมูลค่ายุติธรรม <b>ณ วันที่ซื้อ ไม่ใช่วันต้นปี</b> · กำไรก่อนซื้อ<b>ไม่ใช่ของกลุ่ม</b> · สองวิธีแสดงงบได้<b>กำไรรวมเท่ากัน</b></td></tr>
            <tr><td class="k">เปลี่ยนสัดส่วน ยังคุมอยู่</td>
                <td>เป็น<b>รายการในส่วนของเจ้าของ</b> · <b>ไม่มีค่าความนิยมใหม่ ไม่มีกำไรขาดทุน</b></td></tr>
            <tr><td class="k">สูญเสียการควบคุม</td>
                <td><b>รับรู้กำไรขาดทุนในกำไรหรือขาดทุน</b> และ<b>วัดส่วนที่เหลือด้วยมูลค่ายุติธรรม</b></td></tr>
            <tr><td class="k">หุ้นปันผล</td>
                <td><b>ส่วนของผู้ถือหุ้นรวมไม่เปลี่ยน</b> ย้ายจากกำไรสะสมไปทุนหุ้นสามัญเท่านั้น</td></tr>
          </tbody>
        </table></div>
        <h3>ห้าจุดที่พลาดกันมากที่สุด</h3>
        <ul class="list">
          <li>เอา<b>ส่วนของผู้ถือหุ้นทั้งก้อนรวมหุ้นบุริมสิทธิ</b>ไปคูณสัดส่วนหุ้นสามัญ · ที่ถูกคือกันก้อนบุริมสิทธิออกก่อน แล้วบวกสินทรัพย์ที่ยังไม่ได้บันทึกเข้าไปในฐานของหุ้นสามัญ</li>
          <li>ใช้ส่วนของผู้ถือหุ้น<b>ณ วันต้นปี</b>แทน<b>ณ วันที่ซื้อ</b> ในการคำนวณค่าความนิยมกรณีซื้อระหว่างงวด</li>
          <li><b>ตัดจำหน่ายสินทรัพย์ที่รับรู้เพิ่มเต็มปี</b> ทั้งที่ซื้อระหว่างงวด ต้องตัดตามจำนวนเดือนนับจากวันซื้อเท่านั้น</li>
          <li>ใช้<b>ราคาทุนของหุ้นเดิม</b>แทน<b>มูลค่ายุติธรรม ณ วันที่ได้อำนาจควบคุม</b> ในการคำนวณค่าความนิยมของการซื้อเป็นขั้น</li>
          <li>รับรู้<b>กำไรจากการขายหุ้น</b>ในงบกำไรขาดทุนรวม ทั้งที่<b>ยังควบคุมอยู่</b> · กรณีนั้นผลต่างเข้าส่วนของเจ้าของ ไม่ใช่กำไร</li>
        </ul>
        <div class="note key">
          <span class="nh">คำถามเดียวที่ควรถามก่อนตอบทุกข้อของบทนี้</span>
          <b>ก่อนทำรายการ กลุ่มควบคุมอยู่หรือยัง และหลังทำรายการ กลุ่มยังควบคุมอยู่หรือไม่</b><br>
          <b>ยังไม่คุม แล้วคุม</b> → รวมธุรกิจ → คำนวณค่าความนิยม วัดหุ้นเดิมใหม่<br>
          <b>คุมอยู่ แล้วยังคุม</b> → รายการในส่วนของเจ้าของ → ไม่มีค่าความนิยม ไม่มีกำไรขาดทุน<br>
          <b>คุมอยู่ แล้วไม่คุมแล้ว</b> → ขายกิจการ → รับรู้กำไรขาดทุน วัดส่วนที่เหลือด้วยมูลค่ายุติธรรม<br>
          ตอบคำถามนี้ได้ ก็ตอบได้เกินครึ่งบท
        </div>
      </div>
    </section>
  </div>
"""
