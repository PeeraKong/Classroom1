# -*- coding: utf-8 -*-
u"""เนื้อหาฐานข้อมูลของระบบ SAP สำหรับวิชา ERP

ที่มา เอกสารประกอบการสอนสองชุด
  10.0.1 Traditional RDBMS in SAP System AnyDB   12 สไลด์
  10.0.2 SAP Business Suite 7                    13 สไลด์

สไลด์ชุดแรกมีหน้าที่หัวเรื่องกับโลโก้ไม่ตรงกันสามหน้า คือหน้าที่ขึ้นหัวว่า
Oracle แต่โชว์โลโก้ Sybase หน้าที่ขึ้นหัวว่า DBII แต่โชว์ MaxDB
และหน้าที่ขึ้นหัวว่า MaxDB แต่โชว์ Oracle · หน้านี้จึงเล่าเป็นรายชื่อ
ฐานข้อมูลที่ SAP รองรับแทนการไล่ทีละหน้า แล้วกำกับข้อสังเกตไว้ให้เห็น

ไม่ได้ฝังภาพสไลด์ เพราะเกือบทุกหน้าเป็นโลโก้ของผู้ผลิตฐานข้อมูล
ซึ่งเป็นเครื่องหมายการค้าของบริษัทอื่น และไม่ได้ให้ข้อมูลเกินกว่าชื่อ
"""

RAIL = u"""    <nav id="rail-db" class="hidden" aria-label="หัวข้อฐานข้อมูลของ SAP">
      <div class="rail-h">ฐานข้อมูลของ SAP</div>
      <ol>
        <li><a href="#db-1"><i>1</i>สถาปัตยกรรมสามชั้น</a></li>
        <li><a href="#db-2"><i>2</i>ฐานข้อมูลทำหน้าที่อะไร</a></li>
        <li><a href="#db-3"><i>3</i>AnyDB คืออะไร</a></li>
        <li><a href="#db-4"><i>4</i>สิทธิ์ใช้ Oracle ผ่าน SAP</a></li>
        <li><a href="#db-5"><i>5</i>เส้นตายของ AnyDB</a></li>
        <li><a href="#db-6"><i>6</i>SAP Business Suite</a></li>
        <li><a href="#db-7"><i>7</i>ห้าองค์ประกอบของ Suite 7</a></li>
        <li><a href="#db-8"><i>8</i>SAP ECC</a></li>
        <li><a href="#db-9"><i>9</i>วงจรชีวิตของ Suite 7</a></li>
      </ol>
    </nav>
"""

PANEL = u"""  <div id="db" class="hidden" role="tabpanel" aria-labelledby="t-db">
    <p class="lede">สามบทแรกเราดูว่า <b>SAP ทำอะไรได้บ้าง</b> · แท็บนี้ลงไปอีกชั้นหนึ่ง คือ<b>ข้อมูลทั้งหมดนั้นไปเก็บอยู่ที่ไหน</b> · คำตอบเดิมคือ<b>ฐานข้อมูลของใครก็ได้</b> ซึ่ง SAP เรียกว่า <b>AnyDB</b> · และคำตอบนั้นกำลังจะหมดอายุ ซึ่งเป็นเหตุผลทั้งหมดที่ทำให้เกิด HANA ในแท็บถัดไป</p>

    <div class="note key">
      <span class="nh">เส้นเรื่องของแท็บนี้ในสามบรรทัด</span>
      <b>หนึ่ง</b> SAP ออกแบบระบบให้แยกชั้นฐานข้อมูลออกมา จึงเปลี่ยนยี่ห้อฐานข้อมูลได้<br>
      <b>สอง</b> ความยืดหยุ่นนั้นแลกมาด้วยการที่ SAP ไม่ได้เป็นเจ้าของชั้นที่สำคัญที่สุดของระบบตัวเอง<br>
      <b>สาม</b> SAP จึงเดินออกจาก AnyDB ด้วยการสร้างฐานข้อมูลของตัวเอง แล้วกำหนดเส้นตายให้ลูกค้าย้ายตาม
    </div>

    <section class="sec" id="db-1">
      <div class="sec-h"><span class="sec-n">1</span><h2>สถาปัตยกรรมสามชั้นของ SAP</h2></div>
      <div class="body">
        <p>บทที่ 1 เคยพูดถึงสถาปัตยกรรมสามชั้นไปแล้วตอนเล่าเรื่อง <b>R/3</b> · ตรงนี้เรากลับมาดูอีกครั้งโดยเน้น<b>ชั้นล่างสุด</b> เป็นหลัก</p>
        <div class="flow">
          <div class="fstep"><span class="fn">1</span><div><div class="ft">Client Tier <span class="en">ชั้นนำเสนอ</span></div><div class="fd">คือ <b>SAP Front End</b> ที่ผู้ใช้เห็น ได้แก่ SAP GUI หรือเบราว์เซอร์ · ทำหน้าที่รับคำสั่งและแสดงผลเท่านั้น ไม่ได้คิดอะไรเอง</div></div></div>
          <div class="fstep"><span class="fn">2</span><div><div class="ft">Application Tier <span class="en">ชั้นประมวลผล</span></div><div class="fd">คือ <b>Application Server</b> ซึ่งรันโปรแกรมที่เขียนด้วย <b>ABAP</b> · ตรรกะทางธุรกิจทั้งหมดอยู่ชั้นนี้</div></div></div>
          <div class="fstep"><span class="fn">3</span><div><div class="ft">Database Tier <span class="en">ชั้นฐานข้อมูล</span></div><div class="fd">คือ <b>Database Server</b> ซึ่งเก็บข้อมูลจริงทั้งหมด · ชั้นนี้เองที่เป็นได้หลายยี่ห้อ</div></div></div>
        </div>
        <div class="note key">
          <span class="nh">ตัวเชื่อมระหว่างชั้นที่สองกับชั้นที่สามคือ Open SQL</span>
          โปรแกรม <b>ABAP</b> ไม่ได้คุยกับฐานข้อมูลด้วยภาษาเฉพาะของยี่ห้อนั้น ๆ แต่คุยผ่าน <b>Open SQL</b> ซึ่งเป็นภาษากลาง<br>
          ตัวกลางนี้คือเหตุผลทั้งหมดที่ทำให้ <b>เปลี่ยนยี่ห้อฐานข้อมูลได้โดยไม่ต้องเขียนโปรแกรมใหม่</b>
        </div>
        <p>ขอให้เห็นภาพว่านี่คือ<b>การออกแบบที่ตั้งใจ</b> ไม่ใช่เรื่องบังเอิญนะครับ · SAP จงใจไม่ผูกตัวเองกับฐานข้อมูลยี่ห้อใดยี่ห้อหนึ่ง เพื่อให้ขายระบบเข้าไปในองค์กรที่ใช้ฐานข้อมูลอะไรอยู่ก็ได้</p>
      </div>
    </section>

    <section class="sec" id="db-2">
      <div class="sec-h"><span class="sec-n">2</span><h2>ฐานข้อมูลในระบบ SAP ทำหน้าที่อะไร</h2></div>
      <div class="body">
        <div class="note key">
          <span class="nh">นิยามที่สไลด์ให้ไว้</span>
          ฐานข้อมูลคือ <b>กลุ่มข้อมูลที่จัดระเบียบไว้และถือเป็นหน่วยเดียวกัน</b> <span class="en">Organized collection of data treated as an unit</span><br>
          วัตถุประสงค์คือ <b>จัดเก็บและเรียกคืนข้อมูลที่เกี่ยวข้องกัน</b> <span class="en">To store and retrieve related information</span>
        </div>
        <p>คำว่า<b>ถือเป็นหน่วยเดียวกัน</b>สำคัญกว่าที่ดูนะครับ · มันหมายความว่าข้อมูลใบสั่งซื้อ ข้อมูลลูกค้า และข้อมูลสินค้าคงคลัง ไม่ได้อยู่กันคนละแฟ้มแยกขาด แต่อยู่ในที่เดียวกันและอ้างถึงกันได้ · นั่นคือหัวใจของคำว่า<b>บูรณาการ</b>ที่เราพูดถึงตั้งแต่บทที่ 1</p>
        <h3>งานที่ฐานข้อมูลของ SAP ต้องรับ</h3>
        <div class="tw"><table class="tbl">
          <thead><tr><th>ลักษณะงาน</th><th>ความหมาย</th><th>สิ่งที่ฐานข้อมูลต้องเก่ง</th></tr></thead>
          <tbody>
            <tr><td class="pc">OLTP</td><td>งานประมวลผลรายการประจำวัน เช่น สร้างใบสั่งขาย รับของเข้าคลัง ตั้งหนี้</td><td><b>เขียนเร็วและถูกต้อง</b> รองรับผู้ใช้จำนวนมากพร้อมกัน และต้องไม่ทำข้อมูลเสียหายเมื่อระบบล่ม</td></tr>
            <tr><td class="pc">OLAP</td><td>งานวิเคราะห์ เช่น สรุปยอดขายรายภูมิภาค เทียบกับงบประมาณ</td><td><b>อ่านและรวมยอดเร็ว</b> จากข้อมูลจำนวนมหาศาล</td></tr>
          </tbody>
        </table></div>
        <div class="note">
          <span class="nh">สองงานนี้ขัดกันเอง และนั่นคือปัญหาที่ค้างมาหลายสิบปี</span>
          ฐานข้อมูลที่ออกแบบมาให้<b>เขียนเร็ว</b>จะเก็บข้อมูลเรียงเป็น<b>แถว</b> เพราะหนึ่งรายการคือหนึ่งแถว เขียนทีเดียวจบ<br>
          แต่ฐานข้อมูลที่ออกแบบมาให้<b>รวมยอดเร็ว</b>อยากได้ข้อมูลเรียงเป็น<b>คอลัมน์</b> เพราะการรวมยอดขายคือการอ่านคอลัมน์เดียวทั้งคอลัมน์<br>
          ทางออกเดิมคือ<b>ทำสองระบบ</b> คือระบบ ERP ไว้เขียน แล้วคัดลอกข้อมูลไปไว้อีกระบบหนึ่งเพื่อวิเคราะห์ · ซึ่งแปลว่า<b>ข้อมูลที่เอาไปวิเคราะห์ไม่ใช่ข้อมูลล่าสุดเสมอ</b><br>
          จำปัญหานี้ไว้ให้ดีนะครับ เพราะแท็บถัดไปทั้งแท็บคือคำตอบของปัญหานี้
        </div>
      </div>
    </section>

    <section class="sec" id="db-3">
      <div class="sec-h"><span class="sec-n">3</span><h2>AnyDB · ฐานข้อมูลที่ SAP รองรับ</h2></div>
      <div class="body">
        <p><b>AnyDB</b> เป็นคำที่ SAP ใช้เรียก<b>ฐานข้อมูลยี่ห้อใดก็ได้ที่ไม่ใช่ HANA</b> ซึ่ง SAP รับรองให้ใช้กับระบบของตน</p>
        <div class="tw"><table class="tbl">
          <thead><tr><th>ฐานข้อมูล</th><th>ผู้ผลิต</th><th>หมายเหตุ</th></tr></thead>
          <tbody>
            <tr><td class="pc">Oracle Database</td><td>Oracle</td><td>ฐานข้อมูลที่ลูกค้า SAP ใช้มากที่สุด · สไลด์เรียกว่า <b>World's #1 Database</b></td></tr>
            <tr><td class="pc">DB2</td><td>IBM</td><td>พบมากในองค์กรที่ใช้เมนเฟรมของ IBM อยู่แล้ว</td></tr>
            <tr><td class="pc">SQL Server</td><td>Microsoft</td><td>พบมากในองค์กรที่ใช้ระบบฝั่ง Windows เป็นหลัก</td></tr>
            <tr><td class="pc">Sybase ASE</td><td>Sybase</td><td>SAP ซื้อ Sybase มาในปี 2010 ฐานข้อมูลตัวนี้จึงกลายเป็นของ SAP เอง</td></tr>
            <tr><td class="pc">MaxDB</td><td>เดิมคู่กับ MySQL</td><td>ฐานข้อมูลที่ SAP ดูแลเอง มักใช้กับระบบขนาดเล็กและระบบทดสอบ</td></tr>
            <tr><td class="pc">SAP HANA</td><td>SAP</td><td>ไม่ใช่ AnyDB · เป็นฐานข้อมูลของ SAP เองที่จะมาแทนทั้งหมด ดูแท็บถัดไป</td></tr>
          </tbody>
        </table></div>
        <h3>ส่วนแบ่งตลาดฐานข้อมูลตามที่สไลด์แสดง</h3>
        <div class="tw"><table class="tbl">
          <thead><tr><th>ผู้ผลิต</th><th>ส่วนแบ่ง</th></tr></thead>
          <tbody>
            <tr><td class="pc">Oracle</td><td>45.6 เปอร์เซ็นต์</td></tr>
            <tr><td class="pc">Microsoft</td><td>19.1 เปอร์เซ็นต์</td></tr>
            <tr><td class="pc">IBM</td><td>15.7 เปอร์เซ็นต์</td></tr>
            <tr><td class="pc">SAP</td><td>9.6 เปอร์เซ็นต์</td></tr>
            <tr><td class="pc">Teradata</td><td>3.2 เปอร์เซ็นต์</td></tr>
            <tr><td class="pc">อื่น ๆ</td><td>6.8 เปอร์เซ็นต์</td></tr>
          </tbody>
        </table></div>
        <div class="note key">
          <span class="nh">ตัวเลขชุดนี้คือเหตุผลที่สไลด์ใส่เครื่องหมายคำถามไว้ข้าง SAP</span>
          SAP เป็น<b>เจ้าตลาดซอฟต์แวร์ ERP</b> แต่มีส่วนแบ่งตลาด<b>ฐานข้อมูล</b>แค่ไม่ถึงสิบเปอร์เซ็นต์<br>
          แปลว่าทุกครั้งที่ SAP ขายระบบได้หนึ่งระบบ <b>เงินค่าฐานข้อมูลส่วนใหญ่ไหลไปหาคู่แข่ง</b> โดยเฉพาะ Oracle<br>
          นี่คือแรงจูงใจทางธุรกิจที่อยู่เบื้องหลังเรื่องทั้งหมดในแท็บนี้และแท็บถัดไป
        </div>
        <div class="note src">
          <span class="nh">ข้อสังเกตเรื่องสไลด์ชุดนี้</span>
          สไลด์มีหน้าที่<b>หัวเรื่องกับโลโก้ไม่ตรงกันสามหน้า</b> คือหน้าที่ขึ้นหัวว่า Oracle แต่โชว์โลโก้ Sybase · หน้าที่ขึ้นหัวว่า DBII แต่โชว์ MaxDB · และหน้าที่ขึ้นหัวว่า MaxDB แต่โชว์ Oracle<br>
          น่าจะเป็นความคลาดเคลื่อนตอนจัดหน้า หน้านี้จึงเล่าเป็น<b>รายชื่อฐานข้อมูลที่รองรับ</b>แทนการไล่ทีละหน้า · เนื้อหาที่ต้องจำคือ<b>รายชื่อ</b> ไม่ใช่ลำดับของสไลด์
        </div>
      </div>
    </section>

    <section class="sec" id="db-4">
      <div class="sec-h"><span class="sec-n">4</span><h2>การให้สิทธิ์ใช้ Oracle ผ่าน SAP</h2></div>
      <div class="body">
        <div class="note key">
          <span class="nh">สิทธิ์ที่ SAP ขายให้ไม่ใช่สิทธิ์ Oracle เต็มรูปแบบ</span>
          สิทธิ์ Oracle ที่ซื้อผ่าน SAP เป็นแบบ <b>Application Specific Full Use</b> หรือ <b>ASFU</b><br>
          เรียกอีกอย่างว่า <b>Oracle runtime license</b> หรือ <b>OEM license</b>
        </div>
        <ul class="list">
          <li>สิทธิ์นี้อนุญาตให้<b>เชื่อมต่อฐานข้อมูล Oracle ได้เฉพาะจากซอฟต์แวร์ของ SAP เท่านั้น</b></li>
          <li>ข้อยกเว้นมีอย่างเดียว คือ<b>เครื่องมือดูแลฐานข้อมูลของผู้ผลิตรายอื่น</b> <span class="en">3rd party database admin tools</span></li>
        </ul>
        <div class="note">
          <span class="nh">แปลเป็นภาษาคนว่าอย่างไร</span>
          ถ้ากิจการซื้อ Oracle ผ่าน SAP แล้วอยากเอาฐานข้อมูลก้อนเดียวกันนั้น<b>ไปใช้กับโปรแกรมอื่นที่ไม่ใช่ SAP</b> เช่นเขียนระบบของตัวเองมาต่อตรง · <b>ทำไม่ได้</b> ต้องไปซื้อสิทธิ์เต็มจาก Oracle แยกต่างหาก<br>
          ข้อนี้เป็นเรื่องที่ผู้ตรวจสอบสัญญาซอฟต์แวร์จับได้บ่อย และค่าปรับไม่ใช่เงินน้อย
        </div>
        <h3>แผนการรับรองรุ่นของ Oracle ตามที่สไลด์อ้าง</h3>
        <ul class="list">
          <li><b>Oracle Database 19c</b> ได้รับการรับรองให้ใช้กับ SAP ตั้งแต่<b>เดือนธันวาคม 2019</b> และเป็นรุ่นที่ SAP แนะนำสำหรับลูกค้า Oracle ทุกราย</li>
          <li>การสนับสนุนหลัก <span class="en">Primary Support</span> สิ้นสุด<b>วันที่ 31 มีนาคม 2023</b></li>
          <li>การสนับสนุนส่วนขยาย <span class="en">Extended Support</span> สิ้นสุด<b>วันที่ 31 มีนาคม 2026</b></li>
          <li>SAP จะทดสอบรับรอง Oracle รุ่นใหม่เมื่อซอฟต์แวร์รุ่นนั้นพร้อมใช้งานบน<b>ทุกแพลตฟอร์มแบบติดตั้งในองค์กร</b> <span class="en">on-premise</span> แล้ว</li>
        </ul>
        <div class="note src">
          <span class="nh">วันที่ในหัวข้อนี้มาจากสไลด์ซึ่งทำไว้ก่อนหน้านี้</span>
          วันสิ้นสุดการสนับสนุนของผู้ผลิตฐานข้อมูล<b>เลื่อนได้</b> และเลื่อนมาแล้วหลายครั้ง · เวลาต้องใช้ตัวเลขจริงในการทำงาน ให้ดูประกาศฉบับล่าสุดของ Oracle และ SAP โดยตรง<br>
          สิ่งที่ข้อสอบมักถามคือ<b>หลักการ</b> คือสิทธิ์แบบ ASFU ใช้ได้เฉพาะกับซอฟต์แวร์ SAP ไม่ใช่ตัวเลขวันที่
        </div>
      </div>
    </section>

    <section class="sec" id="db-5">
      <div class="sec-h"><span class="sec-n">5</span><h2>เส้นตายของ AnyDB</h2></div>
      <div class="body">
        <p>หัวข้อนี้คือ<b>จุดหักเห</b>ของทั้งแท็บครับ</p>
        <div class="note">
          <span class="nh">ข่าวเดือนธันวาคม 2019 ที่สไลด์ยกมา</span>
          สัญญาฐานข้อมูลระหว่าง SAP กับ <b>IBM</b> <b>Microsoft</b> และ <b>Oracle</b> จะสิ้นสุดลงในปี <b>2025</b> โดย<b>SAP เป็นฝ่ายบอกเลิกสัญญาไปแล้ว</b><br>
          การทำสัญญาใหม่หรือต่ออายุสัญญาที่บอกเลิกไปแล้ว <b>ดูจะเป็นเรื่องยากและแทบเป็นไปไม่ได้</b><br>
          กระนั้นกลุ่มผู้ใช้ SAP ที่พูดภาษาเยอรมัน หรือ <b>DSAG</b> ก็ยังต้องการหารือเรื่อง AnyDB กับ SAP ต่อไป
        </div>
        <p>อ่านข่าวนี้ให้ออกนะครับ · ประเด็นไม่ใช่ว่าฐานข้อมูลพวกนั้นจะใช้ไม่ได้ แต่คือ<b>SAP จะไม่ขายและไม่รับผิดชอบมันให้อีกต่อไป</b> · ลูกค้าที่ยังใช้อยู่จะกลายเป็นคนที่ต้องไปตกลงกับผู้ผลิตฐานข้อมูลเอง</p>
        <h3>แล้วเส้นตายก็เลื่อน</h3>
        <div class="note key">
          <span class="nh">ข่าวเดือนกุมภาพันธ์ 2020</span>
          SAP <b>เลื่อนวันสิ้นสุดการสนับสนุน Business Suite 7 จากปี 2025 ไปเป็นปี 2027</b> พร้อมการสนับสนุนส่วนขยายต่อไปจนถึงปี <b>2030</b><br>
          แต่ประกาศนั้น<b>ไม่ได้พูดถึง NetWeaver 7.2 หรือ AnyDB เลย</b> · จึงเกิดคำถามว่าข้อเสนอนี้ครอบคลุมเฉพาะ <b>Suite on HANA</b> หรือเปล่า
        </div>
        <div class="note">
          <span class="nh">สิ่งที่ต้องจับจากหัวข้อนี้</span>
          <b>เส้นตายเลื่อนได้</b> และเลื่อนมาแล้วจริง ๆ จาก 2025 เป็น 2027 · อย่าท่องตัวเลขอย่างเดียว<br>
          แต่<b>ทิศทางไม่เคยเปลี่ยน</b> คือ SAP ต้องการให้ลูกค้าย้ายจากฐานข้อมูลของคนอื่น มาอยู่บนฐานข้อมูลของตัวเอง<br>
          ถ้าข้อสอบถามว่าทำไม SAP ถึงสร้าง HANA คำตอบที่ลึกที่สุดอยู่ตรงนี้ ไม่ได้อยู่ที่เรื่องความเร็วอย่างเดียว
        </div>
      </div>
    </section>

    <section class="sec" id="db-6">
      <div class="sec-h"><span class="sec-n">6</span><h2>SAP Business Suite คืออะไร</h2></div>
      <div class="body">
        <div class="note key">
          <span class="nh">นิยามที่ต้องจำ</span>
          <b>SAP Business Suite</b> คือ<b>ผลิตภัณฑ์หลักของ SAP</b> ซึ่งประกอบด้วยโซลูชันหลายตัว<br>
          และจุดที่สไลด์ขีดเส้นใต้ไว้คือ <b>ซื้อหรือขอสิทธิ์ใช้งานแยกทีละตัวก็ได้ หรือจะเอาทั้งชุดก็ได้</b>
        </div>
        <p>ประโยคที่ขีดเส้นใต้นั่นสำคัญในทางปฏิบัติมากครับ · มันแปลว่าองค์กรไม่จำเป็นต้องซื้อทุกอย่างพร้อมกัน · เริ่มจาก ERP ตัวเดียวก่อน แล้วค่อยเติม CRM หรือ SCM ทีหลังเมื่อพร้อมก็ได้</p>
        <div class="note key">
          <span class="nh">นิยามของ Business Suite 7</span>
          เป็น<b>ชุดโปรแกรมทางธุรกิจ</b>ที่ให้<b>การบูรณาการของข้อมูลและกระบวนการ การทำงานร่วมกัน ความสามารถเฉพาะอุตสาหกรรม และความสามารถในการขยายตัว</b><br>
          และเป็น<b>กลุ่มโปรแกรมที่บูรณาการกันอย่างสมบูรณ์</b> ได้แก่ <b>CRM</b> <b>ERP</b> <b>PLM</b> <b>SRM</b> และ <b>SCM</b>
        </div>
      </div>
    </section>

    <section class="sec" id="db-7">
      <div class="sec-h"><span class="sec-n">7</span><h2>ห้าองค์ประกอบของ Business Suite 7</h2></div>
      <div class="body">
        <p>ภาพในสไลด์วาง <b>SAP ERP</b> ไว้ตรงกลาง แล้วล้อมด้วยอีกสี่ตัว โดยมี <b>SAP NetWeaver</b> เป็นฐานรองรับทั้งหมด · โครงนี้ต้องวาดได้จากความจำครับ</p>
        <div class="tw"><table class="tbl">
          <thead><tr><th>ตัวย่อ</th><th>ชื่อเต็ม</th><th>ทำอะไร</th></tr></thead>
          <tbody>
            <tr><td class="pc">ERP</td><td>Enterprise Resource Planning</td><td><b>อยู่ตรงกลาง</b> ครอบคลุม Analytics · Financials · Human Resources · Corporate Services · Operations</td></tr>
            <tr><td class="pc">CRM</td><td>Customer Relationship Management</td><td>ดูแลความสัมพันธ์กับ<b>ลูกค้า</b> ตั้งแต่การขาย บริการ การตลาด การค้า และการวางบิล</td></tr>
            <tr><td class="pc">SRM</td><td>Supplier Relationship Management</td><td>ดูแลความสัมพันธ์กับ<b>ผู้ขาย</b> ครอบคลุมวงจรจัดซื้อจนถึงจ่ายเงินทั้งวงจร</td></tr>
            <tr><td class="pc">SCM</td><td>Supply Chain Management</td><td>ดูแล<b>ห่วงโซ่อุปทาน</b> ทั้งเครือข่าย การวางแผน การประสานงาน และการปฏิบัติการ</td></tr>
            <tr><td class="pc">PLM</td><td>Product Lifecycle Management</td><td>ดูแล<b>วงจรชีวิตผลิตภัณฑ์</b> ตั้งแต่ความคิดแรก ผ่านการผลิต จนถึงการบริการหลังการขาย</td></tr>
          </tbody>
        </table></div>
        <div class="note key">
          <span class="nh">วิธีจำห้าตัวนี้โดยไม่ต้องท่อง</span>
          มองจาก<b>ทิศทางของสิ่งที่ไหลเข้าออกกิจการ</b> ครับ<br>
          <b>SRM</b> คือฝั่งที่ของไหล<b>เข้า</b> · <b>CRM</b> คือฝั่งที่ของไหล<b>ออก</b> · <b>SCM</b> คือเส้นทางที่ของเดิน · <b>PLM</b> คือตัวสินค้าเองตั้งแต่เกิดจนตาย · และ <b>ERP</b> คือบัญชีและทรัพยากรที่อยู่ตรงกลางรับรู้ทุกอย่าง
        </div>
        <h3>รายละเอียดที่สไลด์ให้เพิ่มของแต่ละตัว</h3>
        <div class="grid g2">
          <div class="card">
            <span class="cn">CRM</span>
            <div class="ct">การซื้อ Hybris ในปี 2013</div>
            <div class="cs">หลังซื้อ <b>Hybris</b> SAP ค่อย ๆ ปรับกลยุทธ์ฝั่ง CRM เพื่อสู้กับผู้นำตลาดคือ <b>SalesForce.com</b> ซึ่งเป็นโซลูชันบนคลาวด์ · ปัจจุบันรวมโซลูชัน CRM ไว้ใต้แบรนด์ Hybris โดยแบ่งเป็น <b>Sales · Service · Marketing · Commerce · Billing</b></div>
          </div>
          <div class="card">
            <span class="cn">SCM</span>
            <div class="ct">กลุ่มโปรแกรมย่อย</div>
            <div class="cs">ครอบคลุม supply chain networking · planning · coordination และ <b>SCE</b> คือ Supply Chain Execution · โปรแกรมหลักได้แก่ <b>SNC</b> <b>EWM</b> <b>APO</b> <b>FRE</b> <b>TM</b> และ <b>IBP</b></div>
          </div>
          <div class="card">
            <span class="cn">SRM</span>
            <div class="ct">วงจรจัดซื้อจนถึงจ่ายเงิน</div>
            <div class="cs">ทำให้กระบวนการ <b>procure-to-pay</b> ง่ายขึ้น เป็นอัตโนมัติ และรวมศูนย์ · ดูแลตั้งแต่การหาแหล่งซื้อ การซื้อ การจ่ายเงิน จนถึงการประเมินผลงานผู้ขาย พร้อมเครื่องมือจัดการแค็ตตาล็อกและสัญญาแบบรวมศูนย์</div>
          </div>
          <div class="card">
            <span class="cn">PLM</span>
            <div class="ct">การสนับสนุนแบบรอบด้าน</div>
            <div class="cs">ช่วยวางแผน ออกแบบ สร้าง และบริหารการผลิตโดย<b>มองเห็นและควบคุมได้มากขึ้น</b> · ให้การสนับสนุน <b>360 องศา</b> สำหรับทุกกระบวนการที่เกี่ยวกับผลิตภัณฑ์</div>
          </div>
        </div>
      </div>
    </section>

    <section class="sec" id="db-8">
      <div class="sec-h"><span class="sec-n">8</span><h2>SAP ECC · หัวใจของ Business Suite</h2></div>
      <div class="body">
        <div class="note key">
          <span class="nh">ECC ย่อมาจากอะไร</span>
          <b>SAP ERP Central Component</b> หรือ <b>ECC</b> คือ<b>สินทรัพย์ที่คนรู้จักมากที่สุดชิ้นหนึ่งของ SAP</b><br>
          เป็นซอฟต์แวร์ ERP ที่ประกอบด้วย<b>โมดูลหลายโมดูล</b> ซึ่งให้องค์กรควบคุมกระบวนการทางธุรกิจที่สำคัญได้
        </div>
        <p>ขอให้เห็นความสัมพันธ์ของชื่อให้ชัดนะครับ · ในภาพของ Business Suite กล่องสีเหลืองตรงกลางที่เขียนว่า <b>SAP ERP</b> กับที่เขียนว่า <b>SAP ERP Central Component</b> คือ<b>ตัวเดียวกัน</b> · ECC คือชื่อทางเทคนิคของแกนกลางนั้น</p>
        <h3>โมดูลของ ECC ตามภาพในสไลด์</h3>
        <div class="tw"><table class="tbl">
          <thead><tr><th>ตัวย่อ</th><th>ชื่อเต็ม</th></tr></thead>
          <tbody>
            <tr><td class="pc">FI</td><td>Financial Accounting · การบัญชีการเงิน</td></tr>
            <tr><td class="pc">CO</td><td>Controlling · การบัญชีบริหาร</td></tr>
            <tr><td class="pc">AM</td><td>Fixed Assets Management · การจัดการสินทรัพย์ถาวร</td></tr>
            <tr><td class="pc">SD</td><td>Sales and Distribution · การขายและการกระจายสินค้า</td></tr>
            <tr><td class="pc">MM</td><td>Materials Management · การจัดการวัสดุ</td></tr>
            <tr><td class="pc">PP</td><td>Production Planning · การวางแผนการผลิต</td></tr>
            <tr><td class="pc">QM</td><td>Quality Management · การจัดการคุณภาพ</td></tr>
            <tr><td class="pc">PM</td><td>Plant Maintenance · การบำรุงรักษาโรงงาน</td></tr>
            <tr><td class="pc">HR</td><td>Human Resources · ทรัพยากรบุคคล</td></tr>
            <tr><td class="pc">PS</td><td>Project System · ระบบโครงการ</td></tr>
            <tr><td class="pc">WF</td><td>Workflow · ผังการไหลของงาน</td></tr>
            <tr><td class="pc">IS</td><td>Industry Solutions · โซลูชันเฉพาะอุตสาหกรรม</td></tr>
          </tbody>
        </table></div>
        <div class="note key">
          <span class="nh">เส้นทางของชื่อ</span>
          <b>SAP R/3</b> กลายเป็น <b>SAP ECC</b> · รุ่นล่าสุดของ SAP ERP ออกในปี <b>2006</b> และ <b>enhancement package 8 สำหรับ SAP ERP 6.0</b> ออกในปี <b>2016</b><br>
          ขอให้สังเกตว่าหลังปี 2016 ก็ไม่มีรุ่นใหม่ของ ECC อีกเลย · เพราะความสนใจทั้งหมดย้ายไปที่ S/4HANA แล้ว
        </div>
      </div>
    </section>

    <section class="sec" id="db-9">
      <div class="sec-h"><span class="sec-n">9</span><h2>วงจรชีวิตของ Business Suite 7</h2></div>
      <div class="body">
        <p>หัวข้อสุดท้ายของแท็บนี้คือ<b>ตารางเวลา</b>ที่เป็นแรงผลักให้ทั้งอุตสาหกรรมต้องขยับ</p>
        <ol class="tl">
          <li><span class="ty">สิ้นปี 2027</span><div class="tt">สิ้นสุดการบำรุงรักษาหลัก</div><div class="td">โปรแกรมแกนของ <b>SAP Business Suite 7</b> สิ้นสุด <b>mainstream maintenance</b> · นี่คือวันที่เลื่อนมาจากเดิมคือปี 2025</div></li>
          <li><span class="ty">ต้นปี 2028</span><div class="tt">เริ่มการบำรุงรักษาส่วนขยาย</div><div class="td">เข้าสู่ช่วง <b>extended maintenance</b> ซึ่งโดยทั่วไปมีค่าใช้จ่ายเพิ่มและได้รับเฉพาะการแก้ปัญหาที่จำเป็น ไม่ได้ฟีเจอร์ใหม่</div></li>
          <li><span class="ty">สิ้นปี 2030</span><div class="tt">เส้นตายการย้ายไป S/4HANA</div><div class="td">สิ้นสุดการบำรุงรักษาส่วนขยาย · หลังจากนี้ลูกค้าที่ยังอยู่บน Business Suite 7 จะไม่ได้รับการสนับสนุนตามปกติอีก</div></li>
          <li><span class="ty">ปี 2040</span><div class="tt">สิ้นสุดการสนับสนุนการย้ายระบบ</div><div class="td">การสนับสนุนการย้ายไป <b>SAP S/4HANA</b> สิ้นสุดลง ซึ่งสไลด์เรียกว่าเป็น<b>คำมั่นระยะยาว</b>ของ SAP</div></li>
        </ol>
        <div class="note">
          <span class="nh">ทำไมเรื่องนี้ถึงเป็นเรื่องใหญ่สำหรับนิสิตบัญชี</span>
          เพราะการย้ายจาก ECC ไป S/4HANA <b>ไม่ใช่การอัปเดตโปรแกรม</b> แต่เป็น<b>โครงการที่กินเวลาเป็นปีและเปลี่ยนผังบัญชีกับวิธีทำงานจริง</b><br>
          องค์กรที่ยังไม่ย้ายภายในกรอบเวลานี้ จะต้องรันระบบบัญชีหลักของตัวเองโดยไม่มีผู้ผลิตรองรับ ซึ่งเป็น<b>ประเด็นความเสี่ยงที่ผู้สอบบัญชีต้องพิจารณา</b>ด้วย<br>
          ตารางเวลาชุดนี้จึงเป็นเหตุผลที่โครงการ S/4HANA เต็มไปหมดในตลาดงานตอนนี้
        </div>
        <div class="note key">
          <span class="nh">สรุปแท็บนี้ในสามประโยค</span>
          <b>หนึ่ง</b> SAP แยกชั้นฐานข้อมูลออกมาตั้งแต่ยุค R/3 จึงใช้ฐานข้อมูลยี่ห้อใดก็ได้ ซึ่งเรียกรวมว่า <b>AnyDB</b><br>
          <b>สอง</b> ความยืดหยุ่นนั้นทำให้ SAP ได้ส่วนแบ่งตลาดฐานข้อมูลแค่ไม่ถึงสิบเปอร์เซ็นต์ ทั้งที่เป็นเจ้าตลาด ERP<br>
          <b>สาม</b> SAP จึงบอกเลิกสัญญากับผู้ผลิตฐานข้อมูลรายอื่น และกำหนดวันสิ้นสุดการสนับสนุน Business Suite 7 เพื่อผลักลูกค้าไปที่ <b>S/4HANA บน HANA</b> ซึ่งคือเนื้อหาของแท็บถัดไป
        </div>
      </div>
    </section>
  </div>
"""
