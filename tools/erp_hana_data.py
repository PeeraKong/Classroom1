# -*- coding: utf-8 -*-
u"""เนื้อหา SAP HANA และ SAP S/4HANA สำหรับวิชา ERP

ที่มา เอกสารประกอบการสอนสองชุด
  10.1.1 SAP HANA Overview      32 สไลด์
  10.1.2 SAP S/4HANA Overview   39 สไลด์

ไม่ได้ฝังภาพสไลด์ เพราะเกือบทั้งหมดเป็นโลโก้ ภาพโฆษณาของ SAP
และภาพหน้าจอที่ย่อจนอ่านไม่ออก · ตารางและผังทั้งหมดพิมพ์ขึ้นใหม่เป็น
ตารางเว็บแทน จะได้อ่านบนมือถือได้และค้นหาด้วยคำได้
"""

RAIL = u"""    <nav id="rail-hana" class="hidden" aria-label="หัวข้อ HANA และ S/4HANA">
      <div class="rail-h">HANA และ S/4HANA</div>
      <ol>
        <li><a href="#hana-1"><i>1</i>ฐานข้อมูลในหน่วยความจำ</a></li>
        <li><a href="#hana-2"><i>2</i>ที่มาของ HANA</a></li>
        <li><a href="#hana-3"><i>3</i>HANA คืออะไร</a></li>
        <li><a href="#hana-4"><i>4</i>Appliance เทียบกับ TDI</a></li>
        <li><a href="#hana-5"><i>5</i>เก็บเป็นแถวหรือเป็นคอลัมน์</a></li>
        <li><a href="#hana-6"><i>6</i>การบีบอัดข้อมูล</a></li>
        <li><a href="#hana-7"><i>7</i>HANA Platform สามชั้น</a></li>
        <li><a href="#hana-8"><i>8</i>Database Services</a></li>
        <li><a href="#hana-9"><i>9</i>Application และ Integration</a></li>
        <li><a href="#hana-10"><i>10</i>วิเคราะห์เชิงทำนายและ PAL</a></li>
        <li><a href="#hana-11"><i>11</i>IoT และ Smart Data Streaming</a></li>
        <li><a href="#hana-12"><i>12</i>จาก R/1 ถึง S/4HANA</a></li>
        <li><a href="#hana-13"><i>13</i>S/4HANA คืออะไร</a></li>
        <li><a href="#hana-14"><i>14</i>S/4HANA เทียบกับ ECC</a></li>
        <li><a href="#hana-15"><i>15</i>Fiori และ Embedded Analytics</a></li>
        <li><a href="#hana-16"><i>16</i>รอบการออกรุ่น</a></li>
        <li><a href="#hana-17"><i>17</i>สรุปและจุดที่สับสน</a></li>
      </ol>
    </nav>
"""

PANEL = u"""  <div id="hana" class="hidden" role="tabpanel" aria-labelledby="t-hana">
    <p class="lede">แท็บที่แล้วจบลงที่คำถามว่า <b>SAP จะออกจาก AnyDB อย่างไร</b> · คำตอบคือสร้างฐานข้อมูลของตัวเองชื่อ <b>SAP HANA</b> แล้วเขียน ERP ขึ้นใหม่ทั้งตัวให้รันบนมันอย่างเดียว ซึ่งก็คือ <b>SAP S/4HANA</b> · แท็บนี้เล่าทั้งสองเรื่องต่อกัน</p>

    <div class="note key">
      <span class="nh">สามคำที่ห้ามสับสนกันตลอดทั้งแท็บ</span>
      <b>SAP HANA</b> คือ<b>ฐานข้อมูล</b> · <b>SAP S/4HANA</b> คือ<b>ระบบ ERP ที่รันอยู่บนฐานข้อมูลนั้น</b> · <b>SAP ECC</b> คือ<b>ระบบ ERP รุ่นก่อนหน้า</b> ซึ่งรันบนฐานข้อมูลยี่ห้อใดก็ได้<br>
      ข้อสอบชอบสลับสามคำนี้ · ถ้าจับได้ว่าตัวไหนเป็นฐานข้อมูลและตัวไหนเป็นโปรแกรม จะไม่พลาดเลย
    </div>

    <section class="sec" id="hana-1">
      <div class="sec-h"><span class="sec-n">1</span><h2>ฐานข้อมูลในหน่วยความจำ</h2></div>
      <div class="body">
        <div class="note key">
          <span class="nh">นิยามของ In-Memory Database</span>
          <b>IMDB</b> คือ<b>ระบบจัดการฐานข้อมูลที่อาศัยหน่วยความจำหลักเป็นที่เก็บข้อมูลเป็นหลัก</b><br>
          ตรงข้ามกับระบบจัดการฐานข้อมูลที่ใช้กลไก<b>การเก็บบนดิสก์</b>
        </div>
        <h3>ทำไมถึงเร็วกว่า · สไลด์ให้เหตุผลไว้สามข้อ</h3>
        <ul class="list">
          <li><b>การเข้าถึงดิสก์ช้ากว่าการเข้าถึงหน่วยความจำ</b></li>
          <li><b>อัลกอริทึมที่ใช้ปรับแต่งภายในเรียบง่ายกว่า</b></li>
          <li><b>ใช้คำสั่งซีพียูน้อยกว่า</b></li>
        </ul>
        <p>และข้อที่สี่ซึ่งสไลด์เขียนไว้ต่อท้าย คือ<b>การอ่านข้อมูลในหน่วยความจำตัดเวลาค้นหาตำแหน่งทิ้งไปเลย</b> <span class="en">eliminates seek time</span> จึงได้ประสิทธิภาพที่<b>เร็วกว่าและคาดเดาได้แน่นอนกว่า</b>ดิสก์</p>
        <div class="note">
          <span class="nh">คำว่าคาดเดาได้แน่นอนกว่า สำคัญไม่แพ้คำว่าเร็วกว่า</span>
          ดิสก์แบบจานหมุนต้องขยับหัวอ่านไปยังตำแหน่งที่ต้องการก่อน · เวลาที่ใช้จึง<b>ขึ้นกับว่าข้อมูลอยู่ตรงไหนของจาน</b> คำสั่งเดียวกันอาจเร็วหรือช้าต่างกันหลายเท่า<br>
          หน่วยความจำไม่มีการขยับอะไรทั้งสิ้น เวลาเข้าถึงทุกตำแหน่ง<b>เท่ากันหมด</b> · สำหรับระบบที่ต้องตอบในเวลาที่กำหนด ความแน่นอนนี้มีค่ามาก
        </div>
      </div>
    </section>

    <section class="sec" id="hana-2">
      <div class="sec-h"><span class="sec-n">2</span><h2>ที่มาของ SAP HANA</h2></div>
      <div class="body">
        <ol class="tl">
          <li><span class="ty">2002</span><div class="tt">ก่อตั้ง Transact In Memory, Inc.</div><div class="td"><b>P*TIME</b> ก่อตั้งบริษัทนี้ขึ้นที่ซิลิคอนวัลเลย์ เพื่อระดมทุนพัฒนา<b>ระบบจัดการฐานข้อมูลในหน่วยความจำรุ่นถัดไป</b> · บริษัทลูกที่ถือหุ้นทั้งหมดชื่อ <b>TIM System</b> ตั้งขึ้นที่เกาหลีตั้งแต่ปี 2000 · ชื่อ P*TIME ย่อมาจาก <b>Parallel Transact-In-Memory Engine</b></div></li>
          <li><span class="ty">1 พ.ย. 2005</span><div class="tt">SAP ซื้อเทคโนโลยีจาก ดร. Cha</div><div class="td">SAP ซื้อเทคโนโลยีที่เป็นฐานของ HANA จาก <b>ดร. Sang Kyun Cha</b> ซึ่งเป็นผู้บุกเบิกเทคโนโลยีฐานข้อมูลในหน่วยความจำ · SAP แปลง TIM System เป็น <b>SAP Labs Korea</b> และประกาศอย่างเป็นทางการในเดือน<b>มีนาคม 2008</b></div></li>
          <li><span class="ty">1 ต.ค. 2006</span><div class="tt">Hasso Plattner มอบโจทย์ให้นักศึกษาปริญญาเอก</div><div class="td"><b>Hasso Plattner</b> ระบุว่า HANA เริ่มต้นจากการเป็น<b>หัวข้อวิจัยของนักศึกษาปริญญาเอก</b>ที่ <b>Hasso Plattner Institute</b> · แนวคิดตั้งต้นคือ<b>ฐานข้อมูลที่ตอบสนองในเวลาเป็นศูนย์</b> <span class="en">zero response time database</span></div></li>
          <li><span class="ty">2008</span><div class="tt">พัฒนาร่วมกับ HPI และ Stanford</div><div class="td">ผลิตภัณฑ์ถูกพัฒนาขึ้นโดยความร่วมมือระหว่าง <b>Hasso Plattner Institute</b> กับ <b>มหาวิทยาลัยสแตนฟอร์ด</b> · เป้าหมายคือ<b>การวิเคราะห์ข้อมูลจำนวนมากแบบทันเวลา</b></div></li>
          <li><span class="ty">2010</span><div class="tt">SAP ซื้อ Sybase</div><div class="td">SAP ซื้อ <b>Sybase</b> ด้วยเงิน <b>5.8 พันล้านดอลลาร์</b> · แต่แม้จะซื้อแล้ว ระบบ SAP จำนวนมากก็ยังคงใช้ <b>Oracle</b> <b>DB2</b> และฐานข้อมูลอื่นอยู่ดี</div></li>
        </ol>
        <div class="note key">
          <span class="nh">เหตุผลเชิงเทคนิคที่ Plattner ยกมา และเป็นหัวใจของเรื่องทั้งหมด</span>
          <b>เทคโนโลยีแรมพัฒนาขึ้นอย่างมหาศาลในช่วงสองทศวรรษ ดีขึ้นเป็นพันเท่า</b><br>
          ในขณะที่<b>เทคโนโลยีดิสก์ ซึ่งฐานข้อมูลส่วนใหญ่พึ่งพาอยู่ ดีขึ้นเพียงสิบเท่า</b><br>
          ช่องว่างที่ถ่างออกเรื่อย ๆ นี้ทำให้สถาปัตยกรรมที่ออกแบบไว้สำหรับยุคที่แรมแพงมาก<b>กลายเป็นตัวถ่วงประสิทธิภาพของทั้งระบบ</b>
        </div>
        <p>และคำพูดของ Plattner ที่สไลด์ยกมา ผมคิดว่าน่าอ่านมากครับ · เขาบอกว่าแนวคิดอย่าง<b>ฐานข้อมูลที่ตอบสนองในเวลาเป็นศูนย์</b> จะไม่มีวันได้รับการยอมรับในบริษัทอย่าง SAP · แต่<b>ในมหาวิทยาลัยคุณฝันได้</b> ตราบใดที่ผลิตงานวิจัยที่มีความหมายออกมา</p>
        <div class="note">
          <span class="nh">HANA เป็นแค่ฐานข้อมูลหรือเปล่า</span>
          สไลด์ตอบไว้ตรง ๆ ว่า <b>ไม่ใช่</b><br>
          ตอน SAP สร้าง HANA เขามองเห็นว่าโปรแกรมทางธุรกิจรุ่นถัดไปต้องการ<b>แนวทางที่บูรณาการมากกว่าเดิมมาก</b><br>
          HANA จึงมี<b>ชิ้นส่วนสำหรับสร้างโปรแกรมระดับองค์กรมาให้ในตัว</b> ทั้งฐานข้อมูลรายการ ฐานข้อมูลรายงาน ชั้นบูรณาการ การค้นหา การทำนาย และเว็บ · ทั้งหมดนี้ทำงานได้จากการติดตั้งครั้งเดียว
        </div>
      </div>
    </section>

    <section class="sec" id="hana-3">
      <div class="sec-h"><span class="sec-n">3</span><h2>SAP HANA คืออะไร</h2></div>
      <div class="body">
        <div class="note key">
          <span class="nh">นิยามที่ต้องจำให้ได้ทั้งประโยค</span>
          <b>SAP HANA</b> คือ<b>ระบบจัดการฐานข้อมูลเชิงสัมพันธ์ แบบในหน่วยความจำ และจัดเก็บแบบคอลัมน์</b><br>
          <span class="en">In-Memory, Column-Oriented, Relational Database Management System</span><br>
          หน้าที่หลักในฐานะเซิร์ฟเวอร์ฐานข้อมูลคือ<b>จัดเก็บและเรียกคืนข้อมูลตามที่โปรแกรมร้องขอ</b>
        </div>
        <div class="note key">
          <span class="nh">ชื่อย่อ</span>
          <b>HANA</b> มาจาก <b>H</b>igh performance <b>AN</b>alytics <b>A</b>ppliance<br>
          ภาษาไทยคือ <b>เครื่องสำเร็จรูปสำหรับการวิเคราะห์สมรรถนะสูง</b>
        </div>
        <p>สไลด์ให้ตัวเลขไว้ว่า HANA <b>เร็วกว่าฐานข้อมูลทั่วไปอย่าง Oracle บนฮาร์ดแวร์ชุดเดียวกัน 10 ถึง 1000 เท่า</b> สำหรับงานหลายประเภท</p>
        <h3>ผลที่ตามมาจากความเร็วนั้น</h3>
        <ul class="list">
          <li><b>ทำให้การออกแบบและการดำเนินงานง่ายลง</b> เพราะไม่ต้องสร้างทางลัดไว้เยอะ ๆ เพื่อเลี่ยงความช้า</li>
          <li><b>ทำโปรแกรมทางธุรกิจที่ทำงานทันเวลาได้</b></li>
          <li><b>ลดความซับซ้อนของระบบไอที</b> เพราะไม่ต้องมี Application Server หลายตัว ไม่ต้องมี Operational Data Store ไม่ต้องมี Datamart และไม่ต้องติดตั้งเครื่องมือ BI ที่ซับซ้อนแยกต่างหาก</li>
        </ul>
        <div class="note">
          <span class="nh">ข้อที่สามคือข้อที่มีมูลค่าทางธุรกิจสูงที่สุด</span>
          ระบบเดิมต้อง<b>คัดลอกข้อมูลออกไปอีกหลายที่</b>เพื่อให้รายงานเร็วพอใช้งาน · ทุกชุดที่คัดลอกคือ<b>ข้อมูลที่ล้าสมัยไปแล้วหนึ่งรอบ</b> และเป็นค่าใช้จ่ายที่ต้องดูแลตลอดไป<br>
          ถ้าฐานข้อมูลเร็วพอที่จะทำรายงานจากข้อมูลจริงได้เลย <b>สำเนาทั้งหมดนั้นก็ไม่จำเป็นอีกต่อไป</b> · นี่คือเหตุผลที่สไลด์พูดถึงการเอาระบบหลายตัวออก ไม่ใช่แค่พูดถึงความเร็ว
        </div>
        <div class="note key">
          <span class="nh">HANA รองรับ SQL หรือไม่</span>
          รองรับครับ · สไลด์เขียนไว้ว่า <b>ฐานข้อมูลเชิงสัมพันธ์ส่วนใหญ่ใช้ SQL เป็นภาษาของฐานข้อมูล และ SAP HANA ก็รองรับ SQL ด้วย</b><br>
          ข้อนี้สำคัญ เพราะแปลว่าความรู้ SQL ที่มีอยู่<b>ใช้กับ HANA ได้ทันที</b> ไม่ต้องเรียนภาษาใหม่ทั้งหมด
        </div>
      </div>
    </section>

    <section class="sec" id="hana-4">
      <div class="sec-h"><span class="sec-n">4</span><h2>Appliance เทียบกับ Tailored Data Center Integration</h2></div>
      <div class="body">
        <p>คำว่า <b>Appliance</b> ใน HANA ไม่ได้เป็นแค่ตัวอักษรในชื่อย่อ แต่เป็น<b>วิธีส่งมอบ</b>จริง ๆ ครับ</p>
        <div class="grid g2">
          <div class="card">
            <span class="cn">แบบที่ 1</span>
            <div class="ct">Appliance</div>
            <div class="cs">SAP เริ่มส่งมอบ HANA ในรูป<b>เครื่องสำเร็จรูปที่เป็นมาตรฐานและปรับแต่งมาอย่างดี</b> โดยเลือกได้จากพันธมิตรฮาร์ดแวร์หลายราย · สร้างตาม<b>ข้อกำหนดฮาร์ดแวร์ที่นิยามไว้ชัดเจน</b> เพื่อให้ได้สมรรถนะตามที่เทคโนโลยีในหน่วยความจำต้องการ<br>ทุกอย่างมาในกล่องเดียว ตั้งแต่ Application Server · Database · ระบบปฏิบัติการ · Virtualization · เซิร์ฟเวอร์ · เครือข่าย · จนถึงที่เก็บข้อมูล</div>
          </div>
          <div class="card">
            <span class="cn">แบบที่ 2</span>
            <div class="ct">Tailored Data Center Integration</div>
            <div class="cs">ภายหลัง SAP เพิ่มทางเลือกนี้ขึ้นมา เรียกย่อว่า <b>TDI</b><br>แนวคิดคือ<b>ใช้ฮาร์ดแวร์ที่องค์กรมีอยู่แล้วและถนัดอยู่แล้ว</b> · ให้<b>ความยืดหยุ่นมากกว่า</b>ในการเลือกองค์ประกอบฮาร์ดแวร์ที่ใช้รัน HANA โดยเฉพาะเครือข่ายและที่เก็บข้อมูลขององค์กรเอง</div>
          </div>
        </div>
        <div class="note key">
          <span class="nh">เลือกแบบไหน</span>
          สไลด์ตอบไว้ว่า ถ้าต้องการ<b>ฮาร์ดแวร์ที่ตั้งค่ามาแล้วพร้อมซอฟต์แวร์ที่ติดตั้งไว้ล่วงหน้า</b> ซึ่งพันธมิตรฮาร์ดแวร์ติดตั้งให้ได้อย่างรวดเร็ว · <b>Appliance คือรูปแบบที่เหมาะ</b> และได้รับการสนับสนุนเต็มรูปแบบทั้งจากพันธมิตรฮาร์ดแวร์และจาก SAP<br>
          พูดอีกอย่างคือ <b>Appliance แลกความยืดหยุ่นกับความเร็วในการติดตั้งและความชัดเจนเรื่องผู้รับผิดชอบ</b> ส่วน <b>TDI แลกกลับกัน</b>
        </div>
        <h3>ทะเบียนฮาร์ดแวร์ที่ผ่านการรับรอง</h3>
        <p>SAP มี <b>SAP HANA Certified Hardware Directory</b> ซึ่งรวบรวม<b>ฮาร์ดแวร์ทุกตัวที่ผ่านการรับรองในโครงการรับรองฮาร์ดแวร์ของ HANA</b> หรือที่รองรับสำหรับ HANA รุ่น SPS และสถาปัตยกรรมซีพียูที่กำหนด</p>
        <ul class="list">
          <li>ฮาร์ดแวร์ถูก<b>ทดสอบโดยพันธมิตรฮาร์ดแวร์ร่วมกับ SAP LinuxLab</b></li>
          <li>ระบบปฏิบัติการที่รองรับคือ <b>SUSE</b> และ <b>Red Hat</b> ซึ่งทั้งคู่เป็นลินุกซ์</li>
          <li>สถาปัตยกรรมที่รองรับคือ <b>Intel</b> และ <b>IBM Power Systems</b></li>
          <li>จำนวนโซลูชันในทะเบียน<b>เพิ่มขึ้นตลอดเวลา</b> · สไลด์แสดงตัวเลขไว้สองจุด คือ <b>419 โซลูชัน</b> ในภาพเก่า และ <b>1016 โซลูชัน</b> ณ วันที่ 30 มีนาคม 2026</li>
        </ul>
        <div class="note">
          <span class="nh">ข้อที่คนมักมองข้าม</span>
          HANA <b>รันบนลินุกซ์เท่านั้น</b> ไม่มีรุ่นสำหรับ Windows · องค์กรที่ใช้ SQL Server บน Windows มาตลอดจึงต้องเปลี่ยนทั้งฐานข้อมูลและระบบปฏิบัติการพร้อมกัน<br>
          นี่เป็นต้นทุนแฝงของการย้ายไป S/4HANA ที่มักไม่ได้อยู่ในใบเสนอราคาตั้งต้น
        </div>
      </div>
    </section>

    <section class="sec" id="hana-5">
      <div class="sec-h"><span class="sec-n">5</span><h2>เก็บเป็นแถวหรือเก็บเป็นคอลัมน์</h2></div>
      <div class="body">
        <p>หัวข้อนี้คือ<b>กลไกที่ทำให้ HANA เร็ว</b> ครับ และผมอยากให้เข้าใจมันจริง ๆ ไม่ใช่ท่องว่าคอลัมน์ดีกว่า</p>
        <div class="tw"><table class="tbl">
          <thead><tr><th>เรื่อง</th><th>Row store · เก็บเป็นแถว</th><th>Column store · เก็บเป็นคอลัมน์</th></tr></thead>
          <tbody>
            <tr><td class="pc">วิธีเก็บ</td><td>เรียง<b>แนวนอน</b> คือหนึ่งรายการอยู่ติดกันทั้งแถว</td><td>เรียง<b>แนวตั้ง</b> คือข้อมูลชนิดเดียวกันมาอยู่ด้วยกัน</td></tr>
            <tr><td class="pc">ข้อดี</td><td><b>เพิ่มหรือแก้รายการได้ง่าย</b> เพราะเขียนที่เดียวจบ</td><td><b>อ่านเฉพาะข้อมูลที่ต้องใช้</b> ไม่ต้องลากทั้งแถวมา</td></tr>
            <tr><td class="pc">ข้อเสีย</td><td><b>อาจอ่านข้อมูลที่ไม่จำเป็นติดมาด้วย</b></td><td><b>การเขียนหนึ่งรายการต้องเข้าถึงหลายที่</b></td></tr>
            <tr><td class="pc">เหมาะกับ</td><td>งานรายการประจำวัน คือ <b>OLTP</b></td><td>งานวิเคราะห์และรวมยอด คือ <b>OLAP</b></td></tr>
          </tbody>
        </table></div>
        <div class="note key">
          <span class="nh">สิ่งที่ HANA ทำ และเป็นคำตอบของข้อสอบ</span>
          <b>SAP HANA เก็บข้อมูลได้ทั้งแบบแถวและแบบคอลัมน์</b> <span class="en">Row and Column store</span><br>
          ไม่ได้เลือกอย่างใดอย่างหนึ่ง · ตารางไหนควรเป็นแบบไหนก็ตั้งค่าให้เป็นแบบนั้น<br>
          นี่คือวิธีที่ HANA แก้ปัญหา OLTP กับ OLAP ขัดกันเอง ซึ่งเราทิ้งไว้ในแท็บที่แล้ว
        </div>
        <h3>ประโยชน์ของการเก็บแบบคอลัมน์ตามที่สไลด์ระบุ</h3>
        <ul class="list">
          <li><b>การบีบอัดข้อมูล</b></li>
          <li><b>อ่านและเขียนตารางได้เร็วกว่า</b>การเก็บแบบแถวทั่วไป</li>
          <li><b>ความยืดหยุ่นและการประมวลผลแบบขนาน</b></li>
          <li><b>รวมยอดและคำนวณได้ด้วยความเร็วที่สูงกว่า</b></li>
        </ul>
        <div class="note">
          <span class="nh">ทำไมเก็บเป็นคอลัมน์แล้วบีบอัดได้ดีกว่า</span>
          เพราะข้อมูลในคอลัมน์เดียวกัน<b>เป็นชนิดเดียวกันและซ้ำกันเยอะ</b> · คอลัมน์ประเทศของใบสั่งขายหนึ่งล้านใบ อาจมีค่าต่างกันแค่ไม่กี่สิบค่า<br>
          เก็บเรียงต่อกันแบบนั้น วิธีบีบอัดอย่างง่ายก็ลดขนาดลงได้มหาศาล · ส่วนการเก็บเป็นแถว ข้อมูลข้าง ๆ กันเป็นคนละชนิด จึงหาแบบแผนมาบีบอัดได้ยากกว่ามาก
        </div>
        <div class="note key">
          <span class="nh">ตัวอย่างที่สไลด์ใช้</span>
          คำสั่งอย่าง <b>รวมยอดขายของสินค้าข้าวโพด แยกตามประเทศ</b> ต้องการแค่สามคอลัมน์ คือประเทศ สินค้า และยอดขาย<br>
          ฐานข้อมูลแบบแถวต้อง<b>ลากทั้งแถวขึ้นมาทุกแถว</b>แล้วค่อยทิ้งคอลัมน์ที่ไม่ใช้<br>
          ฐานข้อมูลแบบคอลัมน์<b>หยิบมาแค่สามคอลัมน์</b> · ยิ่งตารางมีคอลัมน์เยอะ ส่วนต่างยิ่งมหาศาล และตารางของ SAP มีคอลัมน์เป็นร้อย
        </div>
      </div>
    </section>

    <section class="sec" id="hana-6">
      <div class="sec-h"><span class="sec-n">6</span><h2>การบีบอัดข้อมูล</h2></div>
      <div class="body">
        <p>ถ้าข้อมูลต้องอยู่ในหน่วยความจำทั้งหมด คำถามแรกที่ทุกคนถามคือ <b>แล้วแรมจะพอเหรอ</b> · การบีบอัดคือคำตอบครับ</p>
        <div class="note key">
          <span class="nh">วิธีบีบอัดหลักคือ Dictionary Compression</span>
          แทนที่จะเก็บคำว่า <b>Miller</b> ซ้ำ ๆ ทุกแถว ระบบจะทำ<b>พจนานุกรม</b>ขึ้นมาหนึ่งชุด แล้วเก็บเป็น<b>เลขรหัสที่ชี้ไปยังพจนานุกรม</b>แทน<br>
          ลำดับของรหัสในคอลัมน์บอกเองว่าแถวไหนเป็นค่าอะไร จึงไม่ต้องเก็บเลขแถวเพิ่ม<br>
          วิธีบีบอัดอื่นที่สไลด์เอ่ยถึงได้แก่ <b>run length</b> · <b>cluster</b> · และ <b>prefix</b>
        </div>
        <h3>ตัวเลขที่สไลด์ให้ไว้</h3>
        <div class="tw"><table class="tbl">
          <thead><tr><th>ตัวชี้วัด</th><th>ค่า</th></tr></thead>
          <tbody>
            <tr><td class="pc">อัตราบีบอัด</td><td><b>5 ถึง 30 เท่า</b></td></tr>
            <tr><td class="pc">การลดขนาดเมื่อย้ายไป S/4HANA</td><td>สไลด์แสดงกราฟที่ลดลง <b>25 เท่า</b> ไล่จาก ERP 6.0 บน Oracle · Suite on HANA · S/4HANA บนที่เก็บข้อมูลแบบดั้งเดิม · จนถึง S/4HANA บน Pure Storage</td></tr>
            <tr><td class="pc">ตัวอย่างขนาดจริง</td><td><b>7.1 เทระไบต์</b> เมื่ออยู่บน AnyDB · เหลือ <b>1.8 เทระไบต์</b> เมื่อย้ายมาบน HANA ด้วยการจัดบ้านและบีบอัด · และเหลือ <b>0.8 เทระไบต์</b> หลังทำให้ง่ายขึ้นด้วยการจัดชั้นอายุข้อมูลและตัดความซ้ำซ้อนออก</td></tr>
          </tbody>
        </table></div>
        <div class="note key">
          <span class="nh">สูตรประมาณแรมที่ต้องใช้</span>
          สไลด์แสดงสูตรไว้ว่า แรมเท่ากับ <b>ขนาดตารางแบบคอลัมน์หารสี่ บวกกับขนาดตารางแบบแถวหารหนึ่งจุดห้า แล้วคูณด้วยตัวประกอบบีบอัดของฐานข้อมูลต้นทาง จากนั้นบวกเพิ่มอีกห้าสิบกิกะไบต์</b><br>
          ความหมายของค่าคงที่แต่ละตัวคือ <b>หารสี่</b> เป็นตัวประกอบบีบอัดเฉลี่ยของตารางแบบคอลัมน์ · <b>หารหนึ่งจุดห้า</b> เป็นของตารางแบบแถว · ตัวคูณคือ<b>ตัวประกอบบีบอัดของฐานข้อมูลต้นทาง</b> · และ<b>ห้าสิบกิกะไบต์</b>ที่บวกเพิ่มคือเผื่อไว้สำหรับแคชของ HANA และบริการเสริมอื่น ๆ<br>
          ยังมีส่วนเผื่อสำหรับ<b>วัตถุที่สร้างตอนทำงาน</b> <span class="en">runtime objects</span> รวมอยู่ในสูตรด้วย
        </div>
        <div class="note">
          <span class="nh">สังเกตว่าตารางแบบแถวบีบอัดได้น้อยกว่ามาก</span>
          หารสี่เทียบกับหารหนึ่งจุดห้า คือ<b>ต่างกันเกือบสามเท่า</b><br>
          นี่เป็นอีกหลักฐานหนึ่งว่าทำไม HANA ถึงใช้การเก็บแบบคอลัมน์เป็นค่าตั้งต้น และเก็บแบบแถวไว้เฉพาะตารางที่จำเป็นจริง ๆ
        </div>
      </div>
    </section>

    <section class="sec" id="hana-7">
      <div class="sec-h"><span class="sec-n">7</span><h2>SAP HANA Platform · สามชั้นบริการ</h2></div>
      <div class="body">
        <p>ถึงตรงนี้ขอเปลี่ยนมุมมองนะครับ · จากที่มอง HANA เป็นฐานข้อมูล เรามามองมันเป็น<b>แพลตฟอร์ม</b> ซึ่งเป็นวิธีที่ SAP อยากให้มอง</p>
        <div class="flow">
          <div class="fstep"><span class="fn">1</span><div><div class="ft">Database Services</div><div class="fd">บริการฐานข้อมูล · เป็นชั้นล่างสุดและเป็นรากฐานของทุกอย่าง</div></div></div>
          <div class="fstep"><span class="fn">2</span><div><div class="ft">Application Services</div><div class="fd">บริการสำหรับสร้างโปรแกรม · ทำให้ HANA สร้างเว็บแอปได้เองโดยไม่ต้องมีเซิร์ฟเวอร์แยก</div></div></div>
          <div class="fstep"><span class="fn">3</span><div><div class="ft">Integration Services</div><div class="fd">บริการเชื่อมต่อ · ดึงข้อมูลจากระบบอื่นเข้ามาหรือเข้าถึงโดยไม่ต้องย้าย</div></div></div>
        </div>
        <div class="note key">
          <span class="nh">ช่องทางที่โปรแกรมภายนอกเข้ามาคุยกับ HANA</span>
          <b>SQL</b> · <b>JSON</b> · <b>ADO.NET</b> · <b>JDBC และ ODBC</b> · <b>OData</b> · <b>HTML5</b> · <b>MDX</b> · <b>XML/A</b><br>
          รายการนี้ยาวโดยตั้งใจ · มันบอกว่า HANA ไม่ได้ออกแบบมาให้คุยกับ SAP อย่างเดียว แต่ให้โปรแกรมอะไรก็ได้มาต่อ
        </div>
        <p>และสไลด์ระบุว่าแพลตฟอร์มนี้ใช้ได้ทั้งแบบ <b>ติดตั้งในองค์กร</b> <span class="en">On-Premise</span> · <b>บนคลาวด์</b> <span class="en">Cloud</span> · และ<b>แบบผสม</b> <span class="en">Hybrid</span></p>
      </div>
    </section>

    <section class="sec" id="hana-8">
      <div class="sec-h"><span class="sec-n">8</span><h2>Database Services</h2></div>
      <div class="body">
        <p>ชั้นนี้สไลด์แบ่งเป็นสองส่วน คือ<b>รากฐาน</b>กับ<b>ความสามารถในการประมวลผล</b></p>
        <h3>ส่วนที่หนึ่ง · รากฐาน</h3>
        <div class="tw"><table class="tbl">
          <thead><tr><th>ความสามารถ</th><th>ความหมาย</th></tr></thead>
          <tbody>
            <tr><td class="pc">In-Memory ACID Columnar</td><td>เก็บในหน่วยความจำ แบบคอลัมน์ และยัง<b>รักษาคุณสมบัติ ACID</b> ของฐานข้อมูลรายการไว้ครบ</td></tr>
            <tr><td class="pc">Multi-Core / Parallelization</td><td>ใช้<b>ซีพียูหลายแกนพร้อมกัน</b> · การเก็บแบบคอลัมน์ทำให้แบ่งงานไปคนละแกนได้ง่าย</td></tr>
            <tr><td class="pc">Advanced Compression</td><td><b>การบีบอัดขั้นสูง</b> ตามที่เล่าไว้ในหัวข้อที่ 6</td></tr>
            <tr><td class="pc">Multitenant Database Containers</td><td><b>แยกฐานข้อมูลหลายชุดในเครื่องเดียว</b> โดยแต่ละชุดไม่เห็นข้อมูลของกันและกัน</td></tr>
            <tr><td class="pc">Dynamic Tiering</td><td><b>การจัดชั้นข้อมูลแบบพลวัต</b> · ดูคำอธิบายในกล่องถัดไป</td></tr>
          </tbody>
        </table></div>
        <div class="note key">
          <span class="nh">Dynamic Tiering คืออะไร และเป็นข้อที่ออกสอบบ่อย</span>
          ตัวเลือกนี้ช่วยให้ผู้ใช้เลือกได้ว่าจะใช้<b>หน่วยความจำสำหรับข้อมูลร้อน</b> และ<b>ดิสก์สำหรับข้อมูลอุ่น</b><br>
          คือเก็บ<b>ข้อมูลที่ใช้บ่อย</b> ซึ่งเรียกว่า <b>hot</b> ไว้ในหน่วยความจำ และเก็บ<b>ข้อมูลที่ใช้ไม่บ่อย</b> ซึ่งเรียกว่า <b>warm</b> ไว้บนดิสก์<br>
          ข้อนี้สำคัญเพราะมันบอกว่า <b>HANA ไม่ได้เอาทุกอย่างยัดลงแรมแบบไม่คิด</b> · แรมยังแพงกว่าดิสก์มาก จึงต้องเลือกว่าอะไรคุ้มที่จะอยู่ในแรม
        </div>
        <h3>ส่วนที่สอง · ความสามารถในการประมวลผล</h3>
        <p>สไลด์บอกว่านอกเหนือจากความสามารถรากฐานแล้ว แพลตฟอร์มยังมีความสามารถที่<b>เปิดทางให้ทำการวิเคราะห์ขั้นสูงกับข้อมูลหลากหลายชนิด</b></p>
        <div class="tw"><table class="tbl">
          <thead><tr><th>ความสามารถ</th><th>ใช้ทำอะไร</th></tr></thead>
          <tbody>
            <tr><td class="pc">Spatial</td><td>ข้อมูล<b>เชิงพื้นที่</b> เช่น พิกัดและแผนที่</td></tr>
            <tr><td class="pc">Predictive</td><td>การ<b>ทำนาย</b> · ดูหัวข้อที่ 10</td></tr>
            <tr><td class="pc">Search</td><td>การ<b>ค้นหา</b></td></tr>
            <tr><td class="pc">Text Analytics</td><td>การ<b>วิเคราะห์ข้อความ</b></td></tr>
            <tr><td class="pc">Text Mining</td><td>การ<b>ขุดค้นข้อความ</b></td></tr>
            <tr><td class="pc">Graph</td><td>ข้อมูลแบบ<b>กราฟ</b> คือความสัมพันธ์ระหว่างสิ่งต่าง ๆ</td></tr>
            <tr><td class="pc">Data Quality</td><td><b>คุณภาพข้อมูล</b></td></tr>
            <tr><td class="pc">Series Data</td><td>ข้อมูล<b>อนุกรม</b> เช่น ค่าที่วัดตามเวลา</td></tr>
            <tr><td class="pc">Function Libraries</td><td><b>คลังฟังก์ชัน</b>สำเร็จรูปที่เรียกใช้ได้เลย</td></tr>
          </tbody>
        </table></div>
        <div class="note">
          <span class="nh">ประเด็นที่ต้องเข้าใจ ไม่ใช่ท่องรายชื่อ</span>
          ความสามารถทั้งเก้าข้อนี้ถ้าเป็นระบบเดิมคือ<b>ซอฟต์แวร์คนละตัว</b>ที่ต้องซื้อแยก ติดตั้งแยก และย้ายข้อมูลไปมา<br>
          การที่มันอยู่<b>ในฐานข้อมูลเดียวกับข้อมูล</b> แปลว่า<b>ไม่ต้องย้ายข้อมูลออกไปวิเคราะห์</b> ซึ่งทั้งเร็วกว่าและไม่มีปัญหาข้อมูลไม่ตรงกัน
        </div>
      </div>
    </section>

    <section class="sec" id="hana-9">
      <div class="sec-h"><span class="sec-n">9</span><h2>Application Services และ Integration Services</h2></div>
      <div class="body">
        <h3>Application Services</h3>
        <p>แพลตฟอร์มมีบริการสำหรับ<b>สร้างโปรแกรมบนเว็บ</b> และรองรับ<b>มาตรฐานการพัฒนาแบบเปิด</b> เช่น SQL · HTML5 · JavaScript · JDBC · ODBC · JSON และ OData</p>
        <div class="tw"><table class="tbl">
          <thead><tr><th>องค์ประกอบ</th><th>หน้าที่</th></tr></thead>
          <tbody>
            <tr><td class="pc">Web Server</td><td><b>เว็บเซิร์ฟเวอร์</b>ในตัว จึงให้บริการหน้าเว็บได้โดยไม่ต้องมีเครื่องแยก</td></tr>
            <tr><td class="pc">SAP Fiori UX</td><td><b>หน้าตาผู้ใช้แบบ Fiori</b> ซึ่งเป็นรูปแบบหน้าจอใหม่ของ SAP · ดูหัวข้อที่ 15</td></tr>
            <tr><td class="pc">Application Lifecycle Management</td><td><b>การจัดการวงจรชีวิตของโปรแกรม</b> ตั้งแต่พัฒนา ทดสอบ จนขึ้นใช้งานจริง</td></tr>
          </tbody>
        </table></div>
        <h3>Integration Services</h3>
        <p>สไลด์เปิดด้วยข้อเท็จจริงว่า <b>องค์กรสร้างและเก็บข้อมูลไว้ในหลายระบบ</b> · เพื่อให้เห็นภาพรวมขององค์กรได้ครบ แพลตฟอร์มจึงมีบริการเชื่อมต่อที่รับมือกับ<b>กลยุทธ์การเชื่อมต่อหลายแบบจากแหล่งข้อมูลที่หลากหลาย</b></p>
        <div class="tw"><table class="tbl">
          <thead><tr><th>บริการ</th><th>รูปแบบ</th><th>แหล่งข้อมูลที่สไลด์ยกตัวอย่าง</th></tr></thead>
          <tbody>
            <tr><td class="pc">Smart Data Access</td><td><b>Federation</b> คือเข้าถึงข้อมูลที่อยู่ที่เดิมโดยไม่ย้าย</td><td>IBM DB2 · Netezza · Oracle · MS SQL Server · Teradata · SAP HANA · SAP ASE · SAP IQ · HIVE</td></tr>
            <tr><td class="pc">Smart Data Integration</td><td><b>Loading</b> คือดึงข้อมูลเข้ามาเก็บจริง</td><td>IBM DB2 · Oracle · MS SQL Server · Twitter · HIVE · OData · อะแดปเตอร์ที่เขียนเอง</td></tr>
            <tr><td class="pc">Smart Data Streaming</td><td><b>Streaming</b> คือรับข้อมูลที่ไหลเข้ามาต่อเนื่อง · เรียกอีกชื่อว่า <b>CEP</b></td><td>อุปกรณ์เคลื่อนที่ · หุ่นยนต์ · เซนเซอร์ · มาตรวัด · รถบรรทุก</td></tr>
            <tr><td class="pc">Remote Data Sync</td><td><b>Synchronize</b> คือทำให้ข้อมูลสองฝั่งตรงกัน</td><td>อุปกรณ์ปลายทางที่มีฐานข้อมูลของตัวเอง เช่น รถยนต์ อาคาร และแท่นขุดเจาะ</td></tr>
            <tr><td class="pc">Hadoop Integration</td><td>เชื่อมกับระบบ<b>ข้อมูลขนาดใหญ่</b></td><td>Spark · Hive · Hadoop</td></tr>
          </tbody>
        </table></div>
        <div class="note key">
          <span class="nh">ความต่างระหว่างสองตัวแรก คือจุดที่ข้อสอบชอบถาม</span>
          <b>Smart Data Access</b> คือ<b>เห็นข้อมูลโดยไม่ย้าย</b> · ข้อมูลยังอยู่ที่ระบบต้นทาง HANA แค่มองทะลุเข้าไป เหมาะเมื่อข้อมูลใหญ่มากหรือต้องการค่าล่าสุดเสมอ<br>
          <b>Smart Data Integration</b> คือ<b>ย้ายข้อมูลเข้ามาเก็บจริง</b> · เหมาะเมื่อต้องการประมวลผลหนัก ๆ หรือระบบต้นทางรับภาระไม่ไหว
        </div>
      </div>
    </section>

    <section class="sec" id="hana-10">
      <div class="sec-h"><span class="sec-n">10</span><h2>การวิเคราะห์เชิงทำนายและ PAL</h2></div>
      <div class="body">
        <div class="note key">
          <span class="nh">นิยามของ Predictive Analytics</span>
          คือ<b>การใช้ข้อมูล อัลกอริทึมทางสถิติ และเทคนิคการเรียนรู้ของเครื่อง เพื่อระบุความน่าจะเป็นของผลลัพธ์ในอนาคตจากข้อมูลในอดีต</b><br>
          เป้าหมายคือ<b>ก้าวข้ามจากการรู้ว่าเกิดอะไรขึ้น ไปสู่การประเมินให้ดีที่สุดว่าอะไรจะเกิดขึ้นในอนาคต</b>
        </div>
        <h3>บันไดสี่ขั้นของการวิเคราะห์</h3>
        <div class="tw"><table class="tbl">
          <thead><tr><th>ขั้น</th><th>ชื่อ</th><th>ตอบคำถามว่า</th></tr></thead>
          <tbody>
            <tr><td class="pc">1</td><td>Descriptive Analytics</td><td><b>เกิดอะไรขึ้น</b></td></tr>
            <tr><td class="pc">2</td><td>Diagnostic Analytics</td><td><b>ทำไมถึงเกิดขึ้น</b></td></tr>
            <tr><td class="pc">3</td><td>Predictive Analytics</td><td><b>อะไรจะเกิดขึ้น</b></td></tr>
            <tr><td class="pc">4</td><td>Prescriptive Analytics</td><td><b>เราจะทำให้มันเกิดขึ้นได้อย่างไร</b></td></tr>
          </tbody>
        </table></div>
        <p>บันไดนี้จำง่ายและใช้ได้ทั้งชีวิตครับ · รายงานบัญชีทั่วไปอยู่ขั้นที่หนึ่ง · การวิเคราะห์ผลต่างอยู่ขั้นที่สอง · การพยากรณ์ยอดขายอยู่ขั้นที่สาม · และการที่ระบบเสนอว่าควรลดราคาเท่าไรจึงจะได้กำไรสูงสุดอยู่ขั้นที่สี่</p>
        <div class="note key">
          <span class="nh">KXEN · บริษัทที่ SAP ซื้อมาเพื่อความสามารถนี้</span>
          <b>KXEN</b> ก่อตั้งเมื่อ<b>เดือนมิถุนายน 1998</b> โดย <b>Roger Haddad</b> และ <b>Michel Bera</b> จากแนวคิดตั้งต้นของ <b>Léon Bottou</b> ซึ่งอาศัย<b>ทฤษฎีการลดความเสี่ยงเชิงโครงสร้างของ Vladimir Vapnik</b><br>
          KXEN ทำตลาด<b>ซอฟต์แวร์วิเคราะห์เชิงทำนาย</b>เป็นหลัก<br>
          <b>วันที่ 10 กันยายน 2013</b> SAP ประกาศแผนเข้าซื้อ KXEN และ<b>วันที่ 1 ตุลาคม 2013</b> การเข้าซื้อก็เสร็จสมบูรณ์
        </div>
        <h3>PAL · คลังฟังก์ชันวิเคราะห์เชิงทำนาย</h3>
        <p><b>PAL</b> เป็นหนึ่งในองค์ประกอบของ <b>AFL</b> หรือ <b>Application Function Library</b> ใน SAP HANA · สามารถนิยามฟังก์ชันที่<b>เรียกได้จากในโพรซีเยอร์ SQL Script</b> เพื่อทำ<b>อัลกอริทึมวิเคราะห์ขั้นสูง</b> · อัลกอริทึมของ PAL แบ่งเป็น <b>10 หมวด</b></p>
        <div class="tw"><table class="tbl">
          <thead><tr><th>หมวด</th><th>ตัวอย่างอัลกอริทึมที่สไลด์ระบุ</th></tr></thead>
          <tbody>
            <tr><td class="pc">Classification</td><td>CART · C4.5 · CHAID · K Nearest Neighbour · Logistic Regression Elastic Net · Back-Propagation Neural Network · Naïve Bayes · Support Vector Machine · Confusion Matrix · AUC</td></tr>
            <tr><td class="pc">Cluster</td><td>ABC Classification · DBSCAN · <b>K-Means</b> · K-Medoid · K-Medians · Kohonen Self Organized Maps · Agglomerate Hierarchical · Affinity Propagation · LDA · GMM</td></tr>
            <tr><td class="pc">Association</td><td><b>Apriori</b> · Apriori Lite · FP-Growth · KORD</td></tr>
            <tr><td class="pc">Regression</td><td>Multiple Linear Regression Elastic Net · Polynomial · Exponential · Bi-Variate Geometric · Bi-Variate Logarithmic</td></tr>
            <tr><td class="pc">Time Series</td><td>Single, Double, Triple Exponential Smoothing · ARIMA และ Seasonal ARIMA · Brown Exponential Smoothing · Croston · Forecast Accuracy Measure</td></tr>
            <tr><td class="pc">Probability Distribution</td><td>Distribution Fit หรือ Weibull analysis · Cumulative Distribution Function · Quantile Function · Kaplan-Meier Survival Analysis</td></tr>
            <tr><td class="pc">Outlier Detection</td><td>Inter-Quartile Range Test หรือ Tukey's Test · Variance Test · Anomaly Detection · Grubbs Outlier Test</td></tr>
            <tr><td class="pc">Link Prediction</td><td>Common Neighbors · Jaccard's Coefficient · Adamic/Adar · Katz</td></tr>
            <tr><td class="pc">Statistic Functions</td><td>ค่าเฉลี่ย มัธยฐาน ความแปรปรวน ส่วนเบี่ยงเบนมาตรฐาน ความโด่ง ความเบ้ · Covariance Matrix · Pearson Correlations Matrix · Chi-squared Tests · F-test</td></tr>
            <tr><td class="pc">Data Preparation</td><td>Sampling · Binning · Scaling · Partitioning · Principal Component Analysis</td></tr>
          </tbody>
        </table></div>
        <div class="note">
          <span class="nh">ไม่ต้องท่องรายชื่อนี้นะครับ</span>
          สิ่งที่ต้องจำคือ<b>มีสิบหมวด</b> และ<b>เรียกใช้ได้จาก SQL Script โดยตรง</b><br>
          ประเด็นที่ลึกกว่านั้นคือ การที่อัลกอริทึมเหล่านี้<b>รันอยู่ในฐานข้อมูล</b> แปลว่าไม่ต้องดึงข้อมูลออกมาที่เครื่องนักวิเคราะห์ก่อน · ซึ่งทั้งเร็วกว่าและปลอดภัยกว่าในแง่การควบคุมข้อมูล
        </div>
      </div>
    </section>

    <section class="sec" id="hana-11">
      <div class="sec-h"><span class="sec-n">11</span><h2>IoT และ Smart Data Streaming</h2></div>
      <div class="body">
        <div class="note key">
          <span class="nh">นิยามของ Internet of Things</span>
          <b>IoT</b> อธิบายถึง<b>เครือข่ายของวัตถุทางกายภาพ ซึ่งฝังเซนเซอร์ ซอฟต์แวร์ และเทคโนโลยีอื่น ๆ ไว้ เพื่อเชื่อมต่อและแลกเปลี่ยนข้อมูลกับอุปกรณ์และระบบอื่นผ่านอินเทอร์เน็ต</b>
        </div>
        <p>โครงสร้างที่สไลด์วาดไว้มีสามส่วน คือ <b>เซนเซอร์และอุปกรณ์</b> · <b>เซิร์ฟเวอร์บนคลาวด์</b> · และ<b>โปรแกรมที่เอาข้อมูลไปใช้</b> โดยมี<b>เครือข่าย</b>เชื่อมทั้งสองช่วง และข้อมูลวิ่งได้<b>สองทาง</b></p>
        <h3>Smart Data Streaming</h3>
        <div class="note key">
          <span class="nh">อะไรบ้างที่เป็นแหล่งของกระแสเหตุการณ์</span>
          สไลด์ตอบกว้างมาก คือ <b>อุปกรณ์หรือโปรแกรมใดก็ตามที่ผลิตข้อมูลออกมาเมื่อมีอะไรเกิดขึ้น หรือรายงานสถานะเป็นประจำ ล้วนเป็นแหล่งของกระแสเหตุการณ์ได้ทั้งสิ้น</b><br>
          ตัวอย่างที่ยกไว้ ได้แก่ <b>เซนเซอร์</b> · <b>กระแสการคลิก</b> · <b>สื่อสังคมออนไลน์</b> · <b>รายการค้า</b> · และ<b>ราคาตลาด</b>
        </div>
        <p><b>SAP HANA Smart Data Streaming</b> เป็น<b>ส่วนขยายที่เลือกติดตั้งได้</b>ของแพลตฟอร์ม ออกแบบมาเพื่อ<b>รับ ประมวลผล และตอบสนองต่อกระแสข้อมูลเหตุการณ์ที่ไหลเข้ามาอย่างต่อเนื่องแบบทันเวลา</b> · ทำให้โปรแกรมรับข้อมูลความเร็วสูงเข้ามาได้ เช่น<b>ค่าจากเซนเซอร์ IoT</b> <b>ราคาซื้อขายทางการเงิน</b> และ<b>บันทึกของระบบ</b> <b>ก่อนที่ข้อมูลนั้นจะถูกเขียนลงฐานข้อมูลแบบดั้งเดิม</b></p>
        <div class="tw"><table class="tbl">
          <thead><tr><th>ความสามารถที่สไลด์ระบุ</th></tr></thead>
          <tbody>
            <tr><td><b>รับ กรอง วิเคราะห์ และตอบสนองต่อเหตุการณ์หลายล้านรายการต่อวินาทีแบบทันเวลา</b></td></tr>
            <tr><td><b>เก็บข้อมูลที่มีคุณค่าสูงไว้ใน SAP HANA</b> และส่งข้อมูลอื่นเข้า Hadoop ผ่านอะแดปเตอร์สำหรับ HDFS หรืองาน MapReduce เข้า Hive</td></tr>
            <tr><td><b>ส่งข้อมูลสดไปยังแดชบอร์ดการปฏิบัติงาน</b></td></tr>
            <tr><td><b>ทำคำสั่งค้นหาต่อเนื่อง</b>ด้วยภาษาเชิงประกาศ <b>CCL</b> หรือวิธีที่ขับเคลื่อนด้วยแบบจำลอง</td></tr>
          </tbody>
        </table></div>
        <h3>Machine Learning</h3>
        <div class="note key">
          <span class="nh">นิยามและความสัมพันธ์กับ AI</span>
          <b>Machine Learning</b> คือ<b>การศึกษาอัลกอริทึมคอมพิวเตอร์ที่พัฒนาตัวเองได้โดยอัตโนมัติผ่านประสบการณ์และการใช้ข้อมูล</b> · ถือเป็น<b>ส่วนหนึ่งของปัญญาประดิษฐ์</b><br>
          ความสัมพันธ์ของสามคำคือ <b>Artificial Intelligence</b> ครอบ <b>Machine Learning</b> และ <b>Machine Learning</b> ครอบ <b>Deep Learning</b> อีกที
        </div>
        <div class="tw"><table class="tbl">
          <thead><tr><th>ด้าน</th><th>สิ่งที่สไลด์ระบุ</th></tr></thead>
          <tbody>
            <tr><td class="pc">ข้อมูลเข้า</td><td>ข้อมูลที่<b>มีโครงสร้างและไม่มีโครงสร้าง</b> ได้แก่ <b>ตาราง</b> · <b>ข้อความ</b> · <b>ภาพ เสียง และวีดิทัศน์</b> · <b>ข้อมูลอนุกรมเวลาและข้อมูลภูมิสารสนเทศ</b></td></tr>
            <tr><td class="pc">กระบวนการ</td><td><b>เตรียมข้อมูล</b> แล้ว<b>ฝึกแบบจำลอง</b> แล้ว<b>นำแบบจำลองไปใช้</b> แล้ว<b>เก็บผลป้อนกลับ</b> แล้ววนกลับไปฝึกใหม่</td></tr>
            <tr><td class="pc">ผลลัพธ์</td><td><b>เปลี่ยนข้อมูลขนาดใหญ่ให้เป็นข้อมูลที่ฉลาด</b> ได้แก่ <b>การทำนาย</b> · <b>การจำแนกและการจัดกลุ่ม</b> · <b>การแนะนำ</b> · และ<b>การทำงานอัตโนมัติ</b></td></tr>
          </tbody>
        </table></div>
      </div>
    </section>

    <section class="sec" id="hana-12">
      <div class="sec-h"><span class="sec-n">12</span><h2>จาก R/1 ถึง S/4HANA</h2></div>
      <div class="body">
        <p>ครึ่งหลังของแท็บนี้เป็นเรื่อง <b>S/4HANA</b> ครับ · เริ่มจากเส้นเวลาซึ่งต่อจากบทที่ 1 โดยตรง</p>
        <ol class="tl">
          <li><span class="ty">1973</span><div class="tt">SAP R/1</div><div class="td">พัฒนาต่อจากระบบบัญชี <b>RF</b> · รันบนเซิร์ฟเวอร์ IBM และระบบปฏิบัติการ DOS · มีลูกค้า <b>40 ราย</b> ภายในปี 1978</div></li>
          <li><span class="ty">1979</span><div class="tt">SAP R/2 · ยุคเมนเฟรม</div><div class="td">ประมวลผลข้อมูลแบบ<b>ทันเวลาบนเมนเฟรม</b> ครอบคลุมบัญชี การผลิต โลจิสติกส์ และทรัพยากรบุคคล · ปี 1991 มีลูกค้า <b>2200 ราย</b> ใน <b>31 ประเทศ</b> · รายได้ <b>5.1 ล้านยูโร</b> พนักงาน <b>60 คน</b> ในปีเริ่มต้น</div></li>
          <li><span class="ty">1992</span><div class="tt">SAP R/3 · สถาปัตยกรรมสามชั้น</div><div class="td">เป็นโค้ดชุดใหม่ <span class="en">new codeline</span> · สถาปัตยกรรมแบบ <b>Client/Server</b> ทำให้องค์กรทั่วไปใช้ SAP ได้ · เริ่มด้วยลูกค้าใหม่ <b>1089 ราย</b> และการติดตั้งกว่า <b>9000 แห่ง</b> · รายได้ <b>424 ล้านยูโร</b> พนักงาน <b>3200 คน</b> ลูกค้า <b>2800 ราย</b> ใน <b>35 ประเทศ</b></div></li>
          <li><span class="ty">1999</span><div class="tt">mySAP.com</div><div class="td">ยุค <b>One-Step-Business</b> · รายได้ <b>6.3 พันล้านยูโร</b> พนักงาน <b>25000 คน</b> ลูกค้า <b>15000 ราย</b> ใน <b>120 ประเทศ</b></div></li>
          <li><span class="ty">2003</span><div class="tt">SAP Business Suite และ NetWeaver</div><div class="td">สถาปัตยกรรมแบบ <b>Enterprise Services</b> · รายได้ <b>7.0 พันล้านยูโร</b> พนักงาน <b>29610 คน</b> ลูกค้า <b>20500 ราย</b> ใน <b>120 ประเทศขึ้นไป</b></div></li>
          <li><span class="ty">2015</span><div class="tt">SAP S/4HANA</div><div class="td">เป็น<b>โค้ดชุดใหม่อีกครั้ง</b> ซึ่งเกิดขึ้นเพียงสองครั้งในประวัติศาสตร์ของ SAP คือตอน R/3 และตอนนี้ · รายได้ <b>16.8 พันล้านยูโร</b> พนักงาน <b>68000 คน</b> ลูกค้า <b>251000 ราย</b> ใน <b>120 ประเทศขึ้นไป</b> · เทคโนโลยีฝั่งพัฒนาคือ <b>ABAP RAP</b> และ <b>SAPUI5</b></div></li>
        </ol>
        <div class="note key">
          <span class="nh">คำว่า New Codeline คือคำสำคัญของเส้นเวลานี้</span>
          เส้นสีแดงในภาพสไลด์ขีดไว้<b>สองจุดเท่านั้น</b> คือก่อน <b>R/3</b> และก่อน <b>S/4HANA</b><br>
          แปลว่าทุกอย่างระหว่าง R/3 กับ Business Suite คือ<b>การต่อยอดจากฐานโค้ดเดิม</b> · ส่วน S/4HANA คือ<b>การเขียนขึ้นใหม่</b><br>
          นี่คือเหตุผลที่การย้ายจาก ECC ไป S/4HANA ยากกว่าการอัปเกรดรุ่นปกติมาก
        </div>
        <h3>ประวัติเลขรุ่นที่ควรรู้</h3>
        <div class="tw"><table class="tbl">
          <thead><tr><th>ตระกูล</th><th>รุ่นและปี</th></tr></thead>
          <tbody>
            <tr><td class="pc">SAP R/3</td><td>1.0 ปี 1992 · 2.0 ปี 1993 · <b>3.0 ปี 1995</b> · 4.0 ปี 1998 · 4.5 ปี 1999 · 4.6 ปี 2001 · 4.7 ปี 2003</td></tr>
            <tr><td class="pc">SAP ECC</td><td>ECC 5.0 ปี 2004 · <b>ECC 6.0 ปี 2005</b></td></tr>
            <tr><td class="pc">SAP ERP</td><td>ERP 6.0 EHP1 ปี 2006 · <b>EHP6 ปี 2011</b> · <b>EHP7 ปี 2013</b> · <b>EHP8 ปี 2016</b></td></tr>
            <tr><td class="pc">SAP S/4HANA</td><td>1511 · 1610 · ไปจนถึง 2020 และ <b>2023</b></td></tr>
          </tbody>
        </table></div>
        <div class="note key">
          <span class="nh">Unified General Ledger · จุดที่คนบัญชีต้องรู้</span>
          ใน <b>SAP S/4HANA Finance 1503</b> มีการนำ<b>บัญชีแยกประเภททั่วไปแบบรวม</b> <span class="en">Unified General Ledger หรือ U-GL</span> มาใช้<br>
          มันรวมองค์ประกอบที่เคยแยกกันคือ <b>Financial Accounting</b> หรือ <b>FI</b> กับ <b>Controlling</b> หรือ <b>CO</b> <b>เข้ามาเป็นแหล่งข้อมูลทางธุรกิจแหล่งเดียวกัน</b><br>
          สำหรับคนบัญชี นี่คือการเปลี่ยนแปลงที่สัมผัสได้ชัดที่สุดของ S/4HANA · การกระทบยอดระหว่าง FI กับ CO ที่เคยเป็นงานประจำทุกสิ้นเดือน <b>หายไปเพราะมันเป็นตารางเดียวกันแล้ว</b>
        </div>
      </div>
    </section>

    <section class="sec" id="hana-13">
      <div class="sec-h"><span class="sec-n">13</span><h2>SAP S/4HANA คืออะไร</h2></div>
      <div class="body">
        <div class="note key">
          <span class="nh">ชื่อย่อ</span>
          <b>SAP S/4HANA</b> ย่อมาจาก <b>SAP Business Suite 4 SAP HANA</b><br>
          <b>S</b> คือ <b>SAP Business Suite</b> · <b>4</b> คือ<b>รุ่นที่สี่ของซอฟต์แวร์ระดับองค์กรของ SAP</b> · และ <b>HANA</b> คือ<b>ฐานข้อมูลที่มันรันอยู่</b><br>
          อ่านเต็ม ๆ คือ <b>SAP Business Suite 4 (generation) for SAP High-performance ANalytic Appliance</b>
        </div>
        <p>ในฐานะ<b>รุ่นที่สี่ของ SAP Business Suite</b> มันเป็นผลิตภัณฑ์ล่าสุดจาก SAP และ<b>รันได้บนฐานข้อมูล HANA เท่านั้น</b></p>
        <div class="note">
          <span class="nh">ข้อแลกเปลี่ยนที่สไลด์พูดตรง ๆ ว่าเป็นทั้งข้อดีและข้อเสีย</span>
          SAP <b>เขียน SAP ECC ขึ้นใหม่ทั้งหมดตั้งแต่ฐานรากในปี 2015</b> เพื่อใช้ประโยชน์จากสมรรถนะและความสามารถด้านการวิเคราะห์ของ HANA<br>
          <b>ข้อดี</b> คือได้ความเร็วและความสามารถใหม่เต็มที่<br>
          <b>ข้อเสีย</b> คือ <b>S/4HANA รันได้บน HANA อย่างเดียว</b> ในขณะที่ <b>ECC รันบนฐานข้อมูลของผู้ผลิตรายอื่นได้</b> ซึ่งก็คือ AnyDB<br>
          ประโยคนี้คือหัวใจของทั้งแท็บ และเป็นคำตอบของคำถามว่า ECC ต่างจาก S/4HANA อย่างไร
        </div>
        <h3>นิยามอื่นที่สไลด์ให้ไว้</h3>
        <ul class="list">
          <li>เป็น<b>โซลูชัน ERP ใหม่จาก SAP</b> ที่มี<b>ข้อมูลที่เรียบง่ายขึ้น</b> · <b>การออกแบบเครื่องมือที่เรียบง่าย</b> · <b>คล่องตัว</b> · <b>ใช้ง่ายขึ้น</b> · <b>คำนวณสิ่งที่ซับซ้อนได้</b> · และ<b>รองรับข้อมูลปริมาณมากขึ้น</b></li>
          <li>ติดตั้งได้ทั้งแบบ<b>ในองค์กร</b> · <b>บนคลาวด์</b> · หรือ<b>แบบผสม</b></li>
          <li>เป็นชุดโปรแกรมที่เปิดตัวในฐานะโซลูชัน ERP ที่แข็งแรง ซึ่งมี<b>ทั้งความสามารถ ERP และ BI</b> โดยใช้พลังการประมวลผลในหน่วยความจำของ HANA</li>
          <li>ออกแบบมาเพื่อ<b>แก้ปัญหาที่ซับซ้อนและจัดการข้อมูลปริมาณมากกว่า ECC และ R/3</b> · ให้<b>ประสบการณ์ผู้ใช้ที่ดีกว่าด้วย SAP Fiori</b> · และ<b>เปลี่ยนจากระบบที่บันทึกรายการ ไปเป็นข้อมูลทันเวลาจากทั้งแหล่งภายในและภายนอก</b></li>
        </ul>
        <div class="note key">
          <span class="nh">OLTP กับ OLAP รวมกันได้แล้ว</span>
          สไลด์เขียนไว้ว่า ด้วย S/4HANA <b>OLTP และ OLAP ถูกรวมเข้าด้วยกันบนแพลตฟอร์มในหน่วยความจำเดียว</b><br>
          แปลว่า<b>ไม่ต้องย้ายข้อมูลไปมา ไม่ต้องสร้างสำเนาหลายชุด และไม่มีความล่าช้าในการดูข้อมูลผลการดำเนินงานอีกต่อไป</b><br>
          นี่คือปัญหาที่เราตั้งไว้ตั้งแต่หัวข้อที่ 2 ของแท็บที่แล้ว และนี่คือคำตอบของมัน
        </div>
        <h3>ข้อเท็จจริงสำคัญของ S/4HANA</h3>
        <ul class="list">
          <li><b>วิเคราะห์และออกรายงานได้เร็วขึ้น</b></li>
          <li><b>ขั้นตอนในกระบวนการน้อยลง</b></li>
          <li><b>SAP Fiori UX ใช้ได้กับทุกอุปกรณ์</b></li>
          <li><b>ERP CRM SRM SCM และ PLM ติดตั้งอยู่ร่วมกัน</b> <span class="en">co-deployed</span></li>
          <li><b>รองรับข้อมูลทุกชนิด</b> ทั้งสื่อสังคม ข้อความ ภูมิศาสตร์ กราฟ และการประมวลผล</li>
          <li><b>ข้อมูลปัจจุบัน 25 เปอร์เซ็นต์ และข้อมูลย้อนหลัง 75 เปอร์เซ็นต์</b></li>
          <li><b>ขนาดข้อมูลรวมเล็กลง</b></li>
        </ul>
        <div class="note">
          <span class="nh">ข้อที่สี่คือการเปลี่ยนแปลงเชิงโครงสร้างที่ใหญ่ที่สุด</span>
          ใน Business Suite 7 นั้น <b>CRM SRM SCM และ PLM เป็นระบบแยกที่ต้องเชื่อมต่อกัน</b> · แต่ละตัวมีฐานข้อมูลของตัวเองและต้องส่งข้อมูลหากัน<br>
          ใน S/4HANA ทั้งหมด<b>ติดตั้งอยู่บนระบบเดียวกัน</b> · ข้อมูลลูกค้ารายเดียวกันจึงเป็น<b>แถวเดียวกัน</b> ไม่ใช่สำเนาที่ต้องกระทบยอดกัน
        </div>
      </div>
    </section>

    <section class="sec" id="hana-14">
      <div class="sec-h"><span class="sec-n">14</span><h2>S/4HANA เทียบกับ SAP ERP 6.0</h2></div>
      <div class="body">
        <div class="note key">
          <span class="nh">สไลด์บอกว่าต่างกันในสี่ด้าน</span>
          <b>หนึ่ง แบบจำลองข้อมูล</b> <span class="en">Data model</span><br>
          <b>สอง ความสามารถของระบบ</b> <span class="en">Functionalities</span><br>
          <b>สาม ส่วนติดต่อผู้ใช้</b> <span class="en">User interface</span><br>
          <b>สี่ การออกรายงาน</b> ซึ่งทำให้ทำรายงานทันเวลาและวิเคราะห์เชิงทำนายได้<br>
          และแต่ละโมดูลหรือ LoB คือ FI CO MM SD PP PM QM ล้วนมีนวัตกรรมและการทำให้เรียบง่ายขึ้นในทั้งสี่ด้านนี้
        </div>
        <h3>แบบจำลองข้อมูลใหม่</h3>
        <p>นี่คือด้านที่เปลี่ยนแรงที่สุดครับ · สไลด์เปรียบเทียบจำนวนตารางก่อนและหลัง</p>
        <div class="tw"><table class="tbl">
          <thead><tr><th>ขอบเขต</th><th>ใน Business Suite เดิม</th><th>ใน S/4HANA</th></tr></thead>
          <tbody>
            <tr><td class="pc">Sales and Distribution</td><td>ตารางเอกสารหลัก ตารางดัชนี ตารางสถานะ ตารางส่งออกนำเข้า ตาราง LIS ตารางดัชนีส่วนลด และตารางจัดการเอกสารออก</td><td>เหลือ <b>VBAK · LIKP · VBRK · VBAP · LIPS · VBRP · VBFA</b></td></tr>
            <tr><td class="pc">Inventory Management</td><td>ตารางยอดรวมและตารางประวัติจำนวนมาก</td><td>เหลือตารางเดียวคือ <b>MATDOC</b></td></tr>
            <tr><td class="pc">Material Ledger</td><td>ตารางยอดรวม ตารางเอกสาร และตารางดัชนีหลายชุด</td><td>เหลือ <b>Material Prices</b></td></tr>
            <tr><td class="pc">Accounting</td><td>ตารางยอดรวม ตารางดัชนี และตารางเอกสารจำนวนมาก เช่น BSIS BSAS BSIK BSAK GLPCT FAGLFLEXT</td><td>เหลือ <b>BKPF</b> และ <b>ACDOCA</b></td></tr>
          </tbody>
        </table></div>
        <div class="tw"><table class="tbl">
          <thead><tr><th>หลักการ</th><th>ความหมาย</th></tr></thead>
          <tbody>
            <tr><td class="pc">Simple Data Model</td><td><b>เหลือเฉพาะตารางหลัก ไม่มีความซ้ำซ้อน</b> · <b>แยกข้อมูลหลักออกจากข้อมูลรายการอย่างชัดเจน</b> · <b>ลดขนาดหน่วยความจำที่ใช้</b></td></tr>
            <tr><td class="pc">Principle of One</td><td><b>มีวิธีตีราคาเพียงวิธีเดียว</b> คือ Material Ledger แทนที่จะมีสองวิธีคือ IM และ ML · และมี<b>การจัดการส่วนลดที่ยืดหยุ่น</b>แทนความซ้ำซ้อนที่ยุ่งยากและมีราคาแพง</td></tr>
            <tr><td class="pc">Throughput Increase</td><td><b>ลงบัญชีด้วยการเพิ่มแถวอย่างเดียวในระดับฐานข้อมูล</b> · <b>ไม่มีการล็อกสำหรับการตีราคาด้วยราคามาตรฐาน</b></td></tr>
          </tbody>
        </table></div>
        <div class="note">
          <span class="nh">ทำไมตารางถึงหายไปได้เยอะขนาดนั้น</span>
          ตารางที่หายไปส่วนใหญ่เป็น<b>ตารางยอดรวม</b> <span class="en">totals tables</span> และ<b>ตารางดัชนี</b> <span class="en">index tables</span><br>
          ตารางพวกนี้มีอยู่เพราะ<b>ฐานข้อมูลเดิมรวมยอดสดไม่ทัน</b> จึงต้องรวมไว้ล่วงหน้าแล้วเก็บไว้<br>
          เมื่อ HANA รวมยอดจากรายการดิบได้ทันที <b>ตารางยอดรวมก็ไม่จำเป็นอีก</b> · และการตัดมันออกยังแก้ปัญหาที่ยอดรวมกับรายการไม่ตรงกันไปในตัว
        </div>
        <h3>การลดขนาดข้อมูล</h3>
        <ul class="list">
          <li>ตารางใน HANA ถูก<b>บีบอัดโดยอัตโนมัติ</b> จึงเก็บข้อมูลจำนวนมากในพื้นที่เล็กได้</li>
          <li>ลดขนาดเพิ่มอีกด้วยการ<b>ตัดตารางและดัชนีที่ไม่จำเป็นออก</b> ซึ่งในฐานข้อมูลแบบเดิมต้องมีไว้เพื่อให้ตอบสนองทันเวลา</li>
          <li>ใน <b>SAP Simple Finance</b> จำนวนตารางฐานข้อมูล<b>ลดจาก 15 ตารางเหลือเพียง 4 ตาราง</b></li>
          <li>ขั้นสุดท้ายคือ<b>กลยุทธ์การจัดชั้นอายุข้อมูล</b> <span class="en">data ageing</span> โดยแบ่งข้อมูลเป็นชั้น<b>ร้อน</b>ที่อยู่ในหน่วยความจำ และชั้น<b>อุ่น</b>ที่อยู่บนดิสก์ · <b>ผู้พัฒนาไม่จำเป็นต้องรู้ว่าข้อมูลอยู่ที่ไหน</b> เพราะ HANA จัดการเอง และข้อมูลนั้น<b>ยังเรียกใช้ได้เสมอเมื่อต้องการ</b></li>
          <li>ตัวเลขตัวอย่างที่สไลด์แสดงไล่จาก <b>593 กิกะไบต์</b> บนฐานข้อมูลเดิม เหลือ <b>118.6 กิกะไบต์</b> เมื่ออยู่บน HANA เหลือ <b>42.4 กิกะไบต์</b> เมื่อเป็น S/4HANA และเหลือ <b>8.4 กิกะไบต์</b> เมื่อนับเฉพาะข้อมูลปัจจุบัน</li>
        </ul>
      </div>
    </section>

    <section class="sec" id="hana-15">
      <div class="sec-h"><span class="sec-n">15</span><h2>SAP Fiori และ Embedded Analytics</h2></div>
      <div class="body">
        <h3>สองหน้าตาที่มีให้เลือก</h3>
        <p>ในระบบ S/4HANA มี<b>ส่วนติดต่อผู้ใช้สองแบบ</b> คือ<b>แบบคลาสสิกที่อยู่ใน SAP GUI</b> ซึ่งผู้ใช้ ECC 6.0 ทุกคนคุ้นเคยอยู่แล้ว และ<b>แบบใหม่คือ SAP Fiori</b> ซึ่งสร้างบนเทคโนโลยีเว็บแบบเปิด</p>
        <div class="note key">
          <span class="nh">ทำไม Fiori ถึงสร้างบนเทคโนโลยีเว็บ</span>
          เพราะต้องตอบความต้องการของ<b>เศรษฐกิจดิจิทัล</b> คือ<b>เข้าถึงระบบ ERP ได้จากอุปกรณ์ใดก็ได้ที่ต่ออินเทอร์เน็ต โดยเฉพาะอุปกรณ์เคลื่อนที่</b><br>
          เทคโนโลยีที่ใช้ได้แก่ <b>HTML5</b> · <b>JavaScript</b> · และโพรโทคอลแลกเปลี่ยนข้อมูล <b>OData</b><br>
          โปรแกรม Fiori สร้างด้วยเทคโนโลยีอย่าง <b>SAPUI5</b> ออกแบบมาให้<b>ไม่ขึ้นกับแพลตฟอร์มและเข้าถึงได้จากอุปกรณ์หลากหลาย</b>
        </div>
        <div class="note key">
          <span class="nh">ประสบการณ์ผู้ใช้ตามบทบาท · Role-Based User Experience</span>
          <b>SAP Fiori แตกรายการขนาดใหญ่ออกเป็นแอปย่อยหลายตัวที่เหมาะกับบทบาทของผู้ใช้</b><br>
          แอปทุกตัวเชื่อมถึงกัน งานทุกอย่างของรายการนั้นจึงยังทำได้ครบ แต่<b>จะทำก็ต่อเมื่อผู้ใช้ต้องการจะทำจริง ๆ</b><br>
          <b>SAP Fiori launchpad</b> ทำหน้าที่เป็น<b>จุดเข้าใช้งานกลางของแอปทั้งหมดของผู้ใช้คนนั้น</b><br>
          ส่วนหน้าจอคลาสสิกแบบ Transaction มัก<b>ยัดรายการที่ซับซ้อนรายการเดียวไว้ให้ผู้ใช้หลายบทบาทใช้ร่วมกัน</b> · งานของผู้ใช้คนเดียวจึงต้องเปิดหลายรายการหรือหลายโปรแกรม
        </div>
        <div class="note">
          <span class="nh">SAP GUI จะหายไปไหม</span>
          สไลด์พูดทั้งสองด้าน และต้องจับให้ครบทั้งคู่<br>
          <b>ด้านที่บอกว่ายังอยู่</b> คือ SAP GUI <b>ยังได้รับการสนับสนุนสำหรับ S/4HANA รุ่นติดตั้งในองค์กร</b> และ<b>ใช้ควบคู่ไปกับแอป Fiori ได้</b> · ช่วยให้ลูกค้าเดิมปรับตัวง่ายขึ้น และยัง<b>มีหลายรายการที่ยังไม่ได้แปลงเป็นแอป Fiori</b> จึงยังต้องใช้ GUI อยู่<br>
          <b>ด้านที่บอกว่าจะหายไป</b> คือ <b>SAP GUI กำลังถูกแทนที่ด้วย Fiori และสักวันหนึ่งจะไม่ได้รับการดูแลอีก</b> · และ<b>การพัฒนาและนวัตกรรมทั้งหมดของ SAP มุ่งไปที่ Fiori แล้ว</b> ความสามารถบางอย่างจึง<b>มีเฉพาะใน Fiori และไม่มีใน GUI</b>
        </div>
        <h3>Embedded Analytics</h3>
        <div class="note key">
          <span class="nh">ทำไมถึงเรียกว่าฝังอยู่ในระบบ</span>
          เพราะ<b>ในอดีต การวิเคราะห์กับการประมวลผลรายการถือเป็นงานคนละอย่าง และมักมีระบบของตัวเองแยกกัน</b><br>
          รายงานเหล่านี้ใน S/4HANA <b>ไม่ต้องใช้ระบบ BW แยกต่างหาก</b> และ<b>แสดงผลจากข้อมูลทันเวลา</b>
        </div>
        <p>สไลด์ยกสถานการณ์ตัวอย่างไว้ และผมคิดว่าเล่าได้ดีมาก ขอเล่าตามนะครับ</p>
        <ol class="tl">
          <li><span class="ty">วันแรก</span><div class="tt">ผู้ใช้สร้างใบสั่งขายให้ลูกค้าใหม่</div><div class="td">ระหว่างทำรายการ ต้องตัดสินใจว่าจะให้ส่วนลดเท่าไร โดยดูจาก<b>ความน่าจะเป็นที่ลูกค้าจะกลับมาซื้ออีก</b> · ตัดสินใจไม่ได้ จึง<b>บันทึกรายการที่ยังไม่สมบูรณ์เอาไว้</b></div></li>
          <li><span class="ty">วันแรก ตอนเย็น</span><div class="tt">ฝ่ายวิเคราะห์ทำรายงาน</div><div class="td">มีการวิเคราะห์และออกรายงาน<b>จัดระดับมูลค่าตลอดช่วงชีวิตของลูกค้า</b> พร้อมเสนอช่วงส่วนลดที่ให้ได้</div></li>
          <li><span class="ty">วันถัดมา</span><div class="tt">กลับมาเปิดใบสั่งขายอีกครั้ง</div><div class="td">ใส่ส่วนลดที่เหมาะสมแล้วโทรหาลูกค้าเพื่อยืนยันคำสั่งซื้อ</div></li>
          <li><span class="ty">สายไปแล้ว</span><div class="tt">ลูกค้าชอบส่วนลดมาก แต่สั่งกับคนอื่นไปแล้ว</div><div class="td">ลูกค้า<b>สั่งซื้อกับผู้ขายที่ตอบสนองเร็วกว่าไปเรียบร้อย</b> · <b>คำสั่งซื้อนั้นหายไป</b></div></li>
        </ol>
        <div class="note key">
          <span class="nh">บทสรุปของเรื่องนี้</span>
          <b>ภายในหนึ่งรายการ ผู้ใช้ควรถูกล้อมด้วยข้อมูลเชิงลึกที่เกี่ยวข้องกับบริบทนั้น</b><br>
          แปลว่า<b>ข้อมูลสำคัญควรปรากฏอยู่ข้างในรายการ ตรงจุดที่ต้องใช้มัน</b> ไม่ใช่อยู่ในรายงานที่ต้องไปเปิดอีกระบบหนึ่ง<br>
          ตัวอย่างที่สไลด์ยกอีกอันหนึ่งคือ ผู้ใช้กำลังสร้างใบขอซื้อและต้องเลือกผู้ขาย · มีผู้ขายหลายรายที่ขายของชิ้นนั้นได้ · การวิเคราะห์ที่ฝังอยู่ในโปรแกรมให้ข้อมูลประกอบการตัดสินใจทันที <b>โดยไม่ต้องออกจากโปรแกรม</b> · ผู้ใช้จึง<b>เลือกผู้ขายที่มีผลงานการส่งมอบดีที่สุด</b>ได้เลย
        </div>
      </div>
    </section>

    <section class="sec" id="hana-16">
      <div class="sec-h"><span class="sec-n">16</span><h2>รอบการออกรุ่นของ S/4HANA</h2></div>
      <div class="body">
        <div class="note key">
          <span class="nh">วิธีอ่านเลขรุ่น</span>
          เลขรุ่นของทั้งสองรุ่นย่อยใช้รูปแบบ <b>YYMM</b> คือ<b>ปีสองหลักตามด้วยเดือนสองหลัก</b><br>
          เช่น <b>1909</b> หมายถึง<b>เดือนกันยายน ปี 2019</b> · และ <b>1511</b> หมายถึง<b>เดือนพฤศจิกายน ปี 2015</b>
        </div>
        <h3>ยุคที่หนึ่ง · ปีละรุ่น</h3>
        <ul class="list">
          <li>S/4HANA เปิดตัวสำหรับตลาดแบบติดตั้งในองค์กรเมื่อ<b>ต้นปี 2015</b> และรุ่น <b>1511</b> ที่ออกเดือนพฤศจิกายนนำนวัตกรรมและการทำให้เรียบง่ายมาสู่งานจัดซื้อ การผลิต ห่วงโซ่อุปทาน และอื่น ๆ</li>
          <li>สำหรับรุ่นติดตั้งในองค์กร SAP ส่ง<b>รุ่นหลักใหม่ปีละหนึ่งรุ่น</b> และ<b>Feature Pack Stacks หรือ FPS สามชุดต่อเนื่องกันทุกไตรมาส</b></li>
          <li>รายการรุ่นที่สไลด์ระบุ ได้แก่ <b>1511</b> เดือนพฤศจิกายน 2015 · <b>2020</b> เดือนตุลาคม 2020 · <b>2021</b> เดือนตุลาคม 2021 · <b>2022</b> เดือนตุลาคม 2022 · และ <b>2023</b> เดือนตุลาคม</li>
        </ul>
        <h3>ยุคที่สอง · สองปีต่อรุ่น</h3>
        <div class="note key">
          <span class="nh">การเปลี่ยนแปลงหลังรุ่นปี 2023</span>
          หลังรุ่นประจำปี <b>2023</b> นั้น S/4HANA <b>เปลี่ยนไปใช้รอบการออกรุ่นทุกสองปี</b> พร้อมกับ<b>ขยายช่วงการบำรุงรักษาหลักจาก 5 ปีเป็น 7 ปี</b><br>
          แปลว่ามี<b>รุ่นฐานหนึ่งรุ่นทุกสองปี</b> และแต่ละรุ่นฐานจะ<b>พ้นจากการบำรุงรักษาหลักเมื่อครบ 7 ปี</b><br>
          เมื่อมีรุ่นฐานใหม่ออกมา <b>FPS จะออกทุก 6 เดือน</b> พร้อมฟีเจอร์ใหม่ที่ไม่สร้างความปั่นป่วน จนกว่ารุ่นฐานถัดไปจะออก
        </div>
        <div class="tw"><table class="tbl">
          <thead><tr><th>สถานการณ์</th><th>สิ่งที่เกิดขึ้น</th></tr></thead>
          <tbody>
            <tr><td class="pc">รอบใหม่</td><td>รุ่นฐานออกใน<b>ปี 2023 · 2025 · 2027</b> ไล่ไปเรื่อย ๆ · ตัวอย่างชื่อคือ S/4HANA 2025 FPS01 · FPS02 · FPS03 · FPS04</td></tr>
            <tr><td class="pc">ติดตั้งรุ่นฐานถัดไปแล้ว</td><td><b>เริ่มนับ FPS01 ถึง FPS04 ใหม่</b>สำหรับรุ่นล่าสุด</td></tr>
            <tr><td class="pc">ยังไม่ติดตั้งรุ่นฐานถัดไป</td><td>เข้าสู่<b>การบำรุงรักษาหลักด้วย Support Pack Stacks หรือ SPS ทุก 6 เดือน</b> เช่น SPS05 และ SPS06 ไปจนสิ้นสุดการบำรุงรักษาหลักที่ 7 ปี</td></tr>
          </tbody>
        </table></div>
        <div class="note">
          <span class="nh">ความต่างระหว่าง FPS กับ SPS คือจุดที่ข้อสอบชอบถาม</span>
          <b>FPS</b> คือ <b>Feature Pack Stack</b> ซึ่ง<b>มีฟีเจอร์ใหม่มาด้วย</b> · ออกในช่วงที่รุ่นนั้นยังเป็นรุ่นล่าสุดอยู่<br>
          <b>SPS</b> คือ <b>Support Pack Stack</b> ซึ่ง<b>มีแต่การแก้ไขและการดูแล ไม่มีฟีเจอร์ใหม่</b> · ออกหลังจากมีรุ่นฐานใหม่มาแทนที่แล้ว<br>
          จำง่าย ๆ ว่า <b>F คือ Feature ได้ของใหม่</b> ส่วน <b>S คือ Support ได้แค่ของซ่อม</b>
        </div>
      </div>
    </section>

    <section class="sec" id="hana-17">
      <div class="sec-h"><span class="sec-n">17</span><h2>สรุปและจุดที่สับสนบ่อย</h2></div>
      <div class="body">
        <div class="note key">
          <span class="nh">ข้อสรุปของ S/4HANA ตามที่สไลด์ให้ไว้</span>
          เป็น<b>ระบบ ERP รุ่นถัดไปของ SAP</b><br>
          <b>สร้างบนฐานข้อมูลในหน่วยความจำ SAP HANA</b> จึงใช้ความสามารถทั้งหมดของแพลตฟอร์มในหน่วยความจำได้ รวมถึง<b>การขุดค้นข้อความอย่างชาญฉลาด การวิเคราะห์พยากรณ์ การจำลองสถานการณ์ และการสนับสนุนการตัดสินใจแบบทันเวลาโดยเข้าถึงข้อมูลการปฏิบัติงานทั้งหมดได้ทันที</b><br>
          ผู้ใช้ได้<b>ส่วนติดต่อผู้ใช้ใหม่คือ SAP Fiori</b> ซึ่งให้ประสบการณ์ใหม่บนทุกอุปกรณ์<br>
          และ<b>มีการพัฒนาโค้ดขึ้นใหม่ทั้งหมด พร้อมปรับโครงสร้างแบบจำลองข้อมูลใหม่</b>ตามโค้ดชุดใหม่นั้น
        </div>
        <h3>ตารางเทียบสามคำที่ต้องแยกให้ออก</h3>
        <div class="tw"><table class="tbl">
          <thead><tr><th>เรื่อง</th><th>SAP HANA</th><th>SAP ECC</th><th>SAP S/4HANA</th></tr></thead>
          <tbody>
            <tr><td class="pc">เป็นอะไร</td><td><b>ฐานข้อมูล</b>และแพลตฟอร์ม</td><td><b>ระบบ ERP</b> รุ่นก่อน</td><td><b>ระบบ ERP</b> รุ่นที่สี่</td></tr>
            <tr><td class="pc">รันบนฐานข้อมูลอะไร</td><td>ตัวมันเองคือฐานข้อมูล</td><td><b>AnyDB</b> หรือ HANA ก็ได้</td><td><b>HANA เท่านั้น</b></td></tr>
            <tr><td class="pc">หน้าตาผู้ใช้</td><td>ไม่มีหน้าตาผู้ใช้สำหรับงานธุรกิจโดยตรง</td><td><b>SAP GUI</b> เป็นหลัก</td><td><b>SAP Fiori</b> เป็นหลัก และยังใช้ GUI ได้</td></tr>
            <tr><td class="pc">ปีที่เกิด</td><td>ประกาศปี <b>2008</b> หลังซื้อเทคโนโลยีมาตั้งแต่ปี 2005</td><td><b>2004</b> สำหรับ ECC 5.0</td><td><b>2015</b></td></tr>
            <tr><td class="pc">เลิกสนับสนุนเมื่อไร</td><td>ยังเป็นผลิตภัณฑ์หลักของ SAP</td><td>บำรุงรักษาหลักถึง<b>สิ้นปี 2027</b> ส่วนขยายถึง<b>สิ้นปี 2030</b></td><td>รอบรุ่นทุกสองปี บำรุงรักษาหลัก<b>รุ่นละ 7 ปี</b></td></tr>
          </tbody>
        </table></div>
        <div class="note">
          <span class="nh">สี่กับดักที่เจอบ่อยที่สุด</span>
          <b>หนึ่ง</b> คิดว่า S/4HANA คือฐานข้อมูล · ไม่ใช่ครับ มันคือโปรแกรม ERP · ฐานข้อมูลคือ HANA<br>
          <b>สอง</b> คิดว่า HANA เร็วเพราะอยู่ในแรมอย่างเดียว · ที่จริงมีสามอย่างประกอบกัน คือ<b>อยู่ในหน่วยความจำ</b> <b>เก็บแบบคอลัมน์</b> และ<b>บีบอัด</b><br>
          <b>สาม</b> คิดว่า HANA เก็บแบบคอลัมน์อย่างเดียว · ที่จริง<b>เก็บได้ทั้งแถวและคอลัมน์</b><br>
          <b>สี่</b> คิดว่า ECC รันบน HANA ไม่ได้ · ที่จริง<b>รันได้</b> ซึ่งเรียกว่า <b>Suite on HANA</b> · สิ่งที่รันบน AnyDB ไม่ได้คือ <b>S/4HANA</b> ต่างหาก
        </div>
        <div class="note key">
          <span class="nh">เส้นเรื่องของสองแท็บนี้ในห้าบรรทัด</span>
          <b>หนึ่ง</b> SAP แยกชั้นฐานข้อมูลออกมาตั้งแต่ R/3 จึงใช้ฐานข้อมูลยี่ห้อใดก็ได้ เรียกว่า AnyDB<br>
          <b>สอง</b> แต่ฐานข้อมูลแบบดิสก์แยกงานบันทึกกับงานวิเคราะห์ออกจากกัน องค์กรจึงต้องมีระบบซ้ำซ้อนและข้อมูลไม่เคยสด<br>
          <b>สาม</b> แรมถูกลงเป็นพันเท่าในขณะที่ดิสก์ดีขึ้นแค่สิบเท่า SAP จึงสร้าง HANA ซึ่งเก็บทุกอย่างในหน่วยความจำ แบบคอลัมน์ และบีบอัด<br>
          <b>สี่</b> เมื่อฐานข้อมูลเร็วพอ ตารางยอดรวมและสำเนาข้อมูลทั้งหมดก็ไม่จำเป็น SAP จึงเขียน ERP ขึ้นใหม่ทั้งตัวเป็น S/4HANA<br>
          <b>ห้า</b> และกำหนดวันสิ้นสุดการสนับสนุน Business Suite 7 เพื่อให้ลูกค้าทั้งโลกย้ายตาม ซึ่งเป็นเหตุผลที่ตลาดงานเต็มไปด้วยโครงการย้ายระบบในตอนนี้
        </div>
      </div>
    </section>
  </div>
"""
