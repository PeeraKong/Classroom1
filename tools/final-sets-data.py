# -*- coding: utf-8 -*-
u"""Part 1 Vocabulary กับ Part 2 Language Points ของข้อสอบเสมือนจริงปลายภาค 9 ชุด

โครงของข้อสอบจริงคือ
    Part 1  Vocabulary        10 คะแนน
    Part 2  Language Points   10 คะแนน
    Part 3  Listening         20 คะแนน
    รวม                       40 คะแนน

ไฟล์นี้เก็บเฉพาะสองพาร์ตแรก ส่วน Part 3 อยู่ที่ tools/final-listening-data.py
เพราะพาร์ตนั้นต้องสร้างไฟล์เสียงจริงด้วย จึงใช้ไปป์ไลน์คนละตัว

รูปแบบของแต่ละพาร์ตเหมือนกับข้อสอบชุดแรกที่ oral-eng/final.html ใช้อยู่
คือเป็นการเติมคำในช่องว่างจากคลังคำที่ให้มา

    box     คลังคำที่แสดงให้ผู้สอบเห็น ต้องมีคำลวงอย่างน้อยสามคำ
    blocks  ย่อหน้าของบท ช่องว่างเขียนเป็น [[1]] ถึง [[10]]
    ans     คำตอบของแต่ละช่อง ต้องเป็นคำที่อยู่ใน box
    exp     คำอธิบายภาษาไทยของแต่ละช่อง

ตัวสร้าง tools/mk-final-sets.py ตรวจทุกข้อนี้ก่อนเขียนหน้าเว็บ
ถ้าช่องว่างขาด เกิน ซ้ำ หรือคำตอบไม่อยู่ในคลังคำ จะไม่เขียนให้เลย

เนื้อหาของสองพาร์ตนี้ผูกกับเรื่องในคลิป Part 3 ของชุดเดียวกัน
นิสิตที่ทำทั้งชุดจะได้เจอศัพท์ชุดเดียวกันสามครั้งในบริบทต่างกัน
ซึ่งช่วยให้จำได้มากกว่าการท่องรายการคำศัพท์
"""

SETS2 = [

# ══════════════════════════════════ ชุดที่ 2 ══════════════════════════════════
{'id': 'F1', 'title': u'ชุดที่ 2', 'theme': u'เปลี่ยนระบบเบิกค่าใช้จ่าย · สัมภาษณ์ผู้ช่วยผู้สอบบัญชี',

 'p1': {
  'box': ['pleasure', 'briefly', 'objective', 'divided', 'outline', 'handout',
          'interrupt', 'move on', 'summarise', 'recommendation',
          'grateful', 'agenda', 'available', 'refer'],
  'blocks': [
   {'who': 'Opening a presentation (WISEOWL)',
    't': "Good morning, everyone. It's a [[1]] to see so many of you here today. For those of "
         "you who don't know me, let me [[2]] introduce myself. I'm Nattha, and I work in "
         "finance operations. My [[3]] this morning is to persuade you that we should replace "
         "the expense claim system. I've [[4]] my talk into three parts, and I'll [[5]] them "
         "for you now: the cost of the present process, the system we propose, and what we need "
         "from you today. I've put all the figures on a [[6]], so there's no need to take notes. "
         "Please don't [[7]] as I go along, because we've left eight minutes for questions at "
         "the end."},
   {'who': 'Signposting and closing',
    't': "That brings me to the end of the cost picture, so let me [[8]] to the system itself. "
         "… To [[9]], the present way of working costs us close to a million baht a year in "
         "time alone, and it loses documents the auditors ask for. My [[10]] is that we sign "
         "for three years."},
  ],
  'ans': {1: 'pleasure', 2: 'briefly', 3: 'objective', 4: 'divided', 5: 'outline',
          6: 'handout', 7: 'interrupt', 8: 'move on', 9: 'summarise', 10: 'recommendation'},
  'exp': {1: u'<b>a pleasure to see you</b> เป็นวลีทักทายในขั้น W คือ Welcome · grateful ใช้กับ '
             u'I am grateful <b>for</b> ไม่ใช่ it is grateful',
          2: u'<b>briefly</b> แปลว่าอย่างย่อ ใช้ขยายกริยา introduce ในขั้น I คือ Introduce yourself',
          3: u'<b>objective</b> คือจุดมุ่งหมายของการพูดครั้งนี้ ตรงกับขั้น S คือ State your topic',
          4: u'<b>divide a talk into parts</b> คือแบ่งการนำเสนอเป็นส่วน ๆ ตรงกับขั้น O คือ Outline',
          5: u'<b>outline</b> ใช้เป็นกริยาได้ แปลว่าบอกเค้าโครง · ประโยคนี้บอกลำดับ ตรงกับขั้น '
             u'What comes when',
          6: u'<b>handout</b> คือเอกสารที่แจกให้ผู้ฟัง ตรงกับขั้น L คือ Let the audience know',
          7: u'<b>interrupt</b> คือขัดจังหวะ · การบอกว่าจะถามได้เมื่อไรอยู่ในขั้น L เช่นกัน',
          8: u'<b>move on to</b> คือเปลี่ยนไปหัวข้อถัดไป เป็นวลีเชื่อมระหว่างส่วน',
          9: u'<b>to summarise</b> ขึ้นต้นการสรุปปิดท้าย · recap ใช้ได้เหมือนกันแต่ที่นี่ต้องการคำกริยา '
             u'ที่ตามหลัง to ซึ่งโจทย์กันไว้ด้วยช่องที่ 10',
          10: u'<b>recommendation</b> คือข้อเสนอว่าควรทำอะไรต่อ ซึ่งเป็น call to action ของการปิด'},
 },

 'p2': {
  'box': ['responsible', 'came across', 'raised', 'outcome', 'learned', 'tend',
          'aware', 'weakness', 'resolved', 'approach',
          'involved', 'initiative', 'strength', 'developed'],
  'blocks': [
   {'who': 'Q: Tell me about a time when you found something that looked wrong.',
    't': "Last summer I was [[1]] for testing goods received notes against purchase orders. "
         "While I was working through the sample, I [[2]] eleven items where the quantity "
         "received was higher than the quantity ordered. I [[3]] the matter with my senior "
         "rather than signing the work off."},
   {'who': 'Q: And what was the result?',
    't': "The [[4]] was that the client changed its receiving procedure before the year end. "
         "What I [[5]] from it is that a concern is much easier to act on when it arrives "
         "organised."},
   {'who': 'Q: What would you say is a weakness of yours?',
    't': "I [[6]] to carry on checking after the evidence is already sufficient. I'm [[7]] "
         "that this costs time, so I now agree what finished looks like before I begin. It's a "
         "[[8]] I manage rather than one I've [[9]] completely."},
   {'who': 'Q: How would you describe the way you work?',
    't': "I'd describe my [[10]] as methodical. I plan each task step by step before I start."},
  ],
  'ans': {1: 'responsible', 2: 'came across', 3: 'raised', 4: 'outcome', 5: 'learned',
          6: 'tend', 7: 'aware', 8: 'weakness', 9: 'resolved', 10: 'approach'},
  'exp': {1: u'<b>be responsible for</b> + กริยาเติม ing คือรับผิดชอบงานนั้น · involved ต้องใช้ '
             u'be involved <b>in</b> จึงไม่เข้ากับ for ที่ตามมา',
          2: u'<b>come across</b> คือเจอโดยไม่ได้ตั้งใจหา เหมาะกับการเจอรายการผิดปกติระหว่างทำงาน',
          3: u'<b>raise a matter with somebody</b> คือยกเรื่องขึ้นหารือกับใคร เป็นส่วน A คือ Action '
             u'ของโครง SAR+L',
          4: u'<b>outcome</b> คือผลที่เกิดขึ้น เป็นส่วน R คือ Result ของโครง SAR+L',
          5: u'<b>what I learned is that…</b> เป็นวลีเปิดส่วน L คือ Lesson ซึ่งปิดคำตอบเชิงพฤติกรรม',
          6: u'<b>I tend to…</b> คือมักจะ เป็นวลี softening ที่ทำให้การยอมรับจุดอ่อนฟังเบาลง',
          7: u'<b>be aware that…</b> คือรู้ตัวว่า แสดงว่าผู้สมัครเห็นผลกระทบของจุดอ่อนตัวเอง',
          8: u'ประโยคนี้ต้องการคำนามที่หมายถึงข้อด้อย จึงเป็น <b>weakness</b> '
             u'· strength มีความหมายตรงข้าม จึงขัดกับ manage rather than resolved',
          9: u'<b>resolve</b> คือแก้ให้หมดไป · การบอกว่ายังไม่หายไปทั้งหมดทำให้คำตอบน่าเชื่อกว่า',
          10: u'<b>approach</b> คือวิธีการทำงาน · a methodical approach เป็นวลีที่ใช้บ่อยในห้องสัมภาษณ์'},
 }},

# ══════════════════════════════════ ชุดที่ 3 ══════════════════════════════════
{'id': 'F2', 'title': u'ชุดที่ 3', 'theme': u'จ้างภายนอกทำเงินเดือน · สัมภาษณ์นักวิเคราะห์การเงิน',

 'p1': {
  'box': ['behalf', 'turn', 'nutshell', 'figures', 'breakdown', 'highlight',
          'clear', 'recap', 'implications', 'hesitate',
          'previous', 'accordingly', 'estimate', 'reliable'],
  'blocks': [
   {'who': 'Opening and stating the message',
    't': "Good morning. I'm speaking on [[1]] of the payroll project team. Before I [[2]] to "
         "the detail, let me put the whole thing in a [[3]]. We cannot staff payroll safely for "
         "the next two years, so the processing should go outside while the control stays here."},
   {'who': 'Presenting the evidence',
    't': "If you look at the [[4]] on the second page, you'll see a [[5]] of the cost per "
         "payslip. I'd like to [[6]] one of them in particular, which is sixty-one baht. I "
         "should be [[7]] that this figure includes work the provider will not do for us."},
   {'who': 'Closing and inviting questions',
    't': "Let me [[8]] the three points before I finish, and then I'll explain the [[9]] for "
         "the two staff who would stay. If anything I've said is unclear, please don't [[10]] "
         "to ask."},
  ],
  'ans': {1: 'behalf', 2: 'turn', 3: 'nutshell', 4: 'figures', 5: 'breakdown',
          6: 'highlight', 7: 'clear', 8: 'recap', 9: 'implications', 10: 'hesitate'},
  'exp': {1: u'<b>on behalf of</b> คือในนามของ ใช้เมื่อพูดแทนทีมหรือองค์กร',
          2: u'<b>turn to the detail</b> คือหันไปพูดเรื่องรายละเอียด · before I turn to… '
             u'เป็นวลีบอกว่ากำลังจะข้ามไปไหน',
          3: u'<b>in a nutshell</b> คือกล่าวโดยย่อที่สุด ใช้วางข้อสรุปไว้ก่อนตามหลัก Pyramid',
          4: u'<b>figures</b> คือตัวเลขในเอกสาร · estimate เป็นการประมาณ ซึ่งไม่ใช่สิ่งที่อยู่บนหน้ากระดาษ',
          5: u'<b>breakdown</b> คือการแยกยอดรวมออกเป็นส่วน ๆ ให้เห็นว่าประกอบด้วยอะไร',
          6: u'<b>highlight</b> คือเน้นให้ผู้ฟังสังเกตจุดใดจุดหนึ่งเป็นพิเศษ',
          7: u'<b>I should be clear that…</b> คือขอบอกให้ชัดว่า ใช้เมื่อจะเปิดข้อจำกัดของตัวเลขตัวเอง',
          8: u'<b>recap</b> คือทบทวนประเด็นที่พูดไปแล้ว ใช้ตอนปิด',
          9: u'<b>implications</b> คือผลที่ตามมา ซึ่งที่นี่หมายถึงผลต่อพนักงานสองคนที่ยังอยู่',
          10: u'<b>don’t hesitate to ask</b> คือถามได้เลยไม่ต้องเกรงใจ เป็นวลีปิดที่สุภาพ'},
 },

 'p2': {
  'box': ['certain', 'evidence', 'alternative', 'trial', 'permanent', 'persuade',
          'guided', 'range', 'negotiate', 'reluctant',
          'expectations', 'convinced', 'propose', 'decline'],
  'blocks': [
   {'who': 'Q: Tell me about a time when you had to persuade somebody.',
    't': "My manager was [[1]] that Sunday trading was profitable, because the takings looked "
         "good. Rather than argue about it, I brought the [[2]] to the next meeting and set out "
         "an [[3]], which was moving the same eight hours to Friday evening."},
   {'who': 'Q: And what happened?',
    't': "He didn't agree in the meeting, but he did agree to a [[4]]. After one month he made "
         "the change [[5]]. I hadn't expected to [[6]] him in a single conversation, and I "
         "don't think I should have."},
   {'who': 'Q: What are your salary expectations?',
    't': "I'd rather be [[7]] by you on that, if that's acceptable. I know roughly what the "
         "graduate [[8]] is in this market, and I'd be glad to [[9]] once I understand the role "
         "better. I'm [[10]] to name a figure now, in case I price myself out of a programme "
         "I've just told you I want."},
  ],
  'ans': {1: 'certain', 2: 'evidence', 3: 'alternative', 4: 'trial', 5: 'permanent',
          6: 'persuade', 7: 'guided', 8: 'range', 9: 'negotiate', 10: 'reluctant'},
  'exp': {1: u'<b>be certain that…</b> คือมั่นใจว่า · convinced ใช้ได้ในความหมายใกล้กัน '
             u'แต่โจทย์เก็บไว้เป็นคำลวงเพราะ convinced มักตามด้วย by หรือ of',
          2: u'<b>evidence</b> คือหลักฐาน ซึ่งเป็นสิ่งที่นำเข้าประชุมได้ ต่างจากการเถียงด้วยความเห็น',
          3: u'<b>set out an alternative</b> คือเสนอทางเลือกอีกทางหนึ่ง '
             u'· การเสนอทางเลือกหนักกว่าการบอกว่าของเดิมไม่ดี',
          4: u'<b>agree to a trial</b> คือตกลงให้ทดลองก่อน ไม่ใช่ตกลงเปลี่ยนถาวร',
          5: u'<b>make a change permanent</b> คือทำให้การเปลี่ยนแปลงเป็นการถาวร',
          6: u'<b>persuade somebody</b> คือโน้มน้าวให้ใครเปลี่ยนความคิด',
          7: u'<b>I’d rather be guided by you</b> เป็นวลี softening ที่ยกเรื่องเงินให้อีกฝ่ายเสนอก่อน',
          8: u'<b>the graduate range</b> คือช่วงเงินเดือนของบัณฑิตใหม่ในตลาดนั้น',
          9: u'<b>negotiate</b> คือเจรจาต่อรอง · การบอกว่าพร้อมเจรจาทำให้ไม่ถูกมองว่าไม่สนใจค่าตอบแทน',
          10: u'<b>be reluctant to…</b> คือไม่ค่อยอยากจะ เป็น softening ที่ปฏิเสธอย่างสุภาพ '
              u'· decline เป็นการปฏิเสธตรง ๆ ซึ่งแข็งเกินไปในบริบทนี้'},
 }},

# ══════════════════════════════════ ชุดที่ 4 ══════════════════════════════════
{'id': 'F3', 'title': u'ชุดที่ 4', 'theme': u'เลือกซอฟต์แวร์ตรวจสอบ · สัมภาษณ์ผู้ตรวจสอบภายใน',

 'p1': {
  'box': ['whereas', 'respect', 'outperformed', 'dearer', 'drawback', 'permanent',
          'sufficient', 'trade-off', 'in favour', 'confident',
          'marginally', 'likewise', 'comparable', 'shortcoming'],
  'blocks': [
   {'who': 'Comparing the two packages',
    't': "Package A had our juniors working by the second day, [[1]] Audara took until the "
         "fourth. In one important [[2]], however, Audara [[3]] it: of the eleven errors we "
         "planted, Audara found ten and Package A found seven. Audara is also roughly a third "
         "[[4]] across three years."},
   {'who': 'The weakness of the cheaper package',
    't': "The main [[5]] of Package A is what it leaves in the audit file. If a test is "
         "repeated with a different filter, there is no [[6]] record of the first attempt, "
         "which our external auditors would not regard as [[7]]."},
   {'who': 'The recommendation',
    't': "So there is a [[8]] here: three more findings and a defensible record, against two "
         "days of learning time per person. On balance we come down [[9]] of Audara, and we are "
         "[[10]] that the difference in price is justified."},
  ],
  'ans': {1: 'whereas', 2: 'respect', 3: 'outperformed', 4: 'dearer', 5: 'drawback',
          6: 'permanent', 7: 'sufficient', 8: 'trade-off', 9: 'in favour', 10: 'confident'},
  'exp': {1: u'<b>whereas</b> เชื่อมสองข้อความที่ขัดกัน แปลว่าในขณะที่ · likewise แปลว่าเช่นเดียวกัน '
             u'จึงให้ความหมายตรงข้ามกับที่ประโยคต้องการ',
          2: u'<b>in one respect</b> คือในแง่หนึ่ง ใช้จำกัดขอบเขตของการเปรียบเทียบ',
          3: u'<b>outperform</b> คือทำได้ดีกว่า ใช้กับการเทียบผลงานของสองสิ่ง',
          4: u'<b>dear</b> ในภาษาอังกฤษแบบอังกฤษแปลว่าแพง จึง <b>dearer</b> คือแพงกว่า',
          5: u'<b>drawback</b> คือข้อเสีย · shortcoming ใกล้เคียงกันแต่มักใช้กับคนหรือผลงาน '
             u'ส่วน drawback ใช้กับสิ่งของหรือทางเลือก',
          6: u'<b>permanent record</b> คือบันทึกที่ลบไม่ได้ ซึ่งเป็นสิ่งที่งานตรวจสอบต้องการ',
          7: u'<b>sufficient</b> คือเพียงพอ ซึ่งเป็นคำที่ใช้กับความเพียงพอของหลักฐานการสอบบัญชี',
          8: u'<b>trade-off</b> คือการได้อย่างเสียอย่าง เป็นคำที่ควรใช้เมื่อเสนอทางเลือกอย่างตรงไปตรงมา',
          9: u'<b>come down in favour of</b> คือสรุปว่าเลือกฝ่ายนั้น',
          10: u'<b>be confident that…</b> คือมั่นใจว่า ใช้ปิดข้อเสนอโดยไม่สัญญาเกินจริง'},
 },

 'p2': {
  'box': ['beyond', 'grades', 'reconciling', 'balanced', 'investigate', 'supervisor',
          'pattern', 'pretend', 'direction', 'floor',
          'aim', 'entitled', 'proud', 'channel'],
  'blocks': [
   {'who': 'Q: Why should we take you rather than another student with the same grades?',
    't': "[[1]] my [[2]], what I would bring is a year of actually finding things. I spent a "
         "year [[3]] the pharmacy stock of a hospital group, which never [[4]], and which "
         "nobody else wanted to do."},
   {'who': 'Q: Give me an example of that.',
    't': "My role was to reconcile, not to [[5]], so I told my [[6]] what I had seen before I "
         "went any further. The [[7]] in the timing turned out to matter more than the size of "
         "the shortfall."},
   {'who': 'Q: Where would you like to be in five years?',
    't': "I'd rather not [[8]] to a precise plan. What I can give you is the [[9]]: I want to "
         "be the person who can take an area nobody understands well and come back with "
         "something the business can act on."},
   {'who': 'Q: Is there anything you would like to ask me?',
    't': "Thank you. If the [[10]] is mine, I have two questions."},
  ],
  'ans': {1: 'beyond', 2: 'grades', 3: 'reconciling', 4: 'balanced', 5: 'investigate',
          6: 'supervisor', 7: 'pattern', 8: 'pretend', 9: 'direction', 10: 'floor'},
  'exp': {1: u'<b>beyond</b> คือเหนือไปกว่า · ใช้ยอมรับสิ่งที่มีอยู่ก่อน แล้วชี้ไปที่สิ่งที่เพิ่มเข้ามา',
          2: u'<b>grades</b> คือผลการเรียน · ผู้สมัครไม่ปฏิเสธเกรด แต่บอกว่าเกรดวัดอะไรไม่ได้',
          3: u'หลัง spent a year ต้องเป็นกริยาเติม ing จึงเป็น <b>reconciling</b> คือการกระทบยอด',
          4: u'<b>balance</b> ใช้เป็นกริยาได้ แปลว่ายอดตรงกัน · never balanced คือไม่เคยตรงเลย',
          5: u'<b>investigate</b> คือสอบสวนหาสาเหตุ ซึ่งเป็นงานของคนอื่น ไม่ใช่งานของเธอ',
          6: u'<b>supervisor</b> คือหัวหน้างานโดยตรง · การรายงานขึ้นไปตามสายเป็นประเด็นสำคัญของคำตอบนี้',
          7: u'<b>pattern</b> คือรูปแบบที่เกิดซ้ำ · ที่นี่คือช่วงเวลาที่ของขาดซ้ำ ๆ',
          8: u'<b>pretend to a plan</b> คือแกล้งทำเป็นว่ามีแผน · การยอมรับว่ายังไม่มีแผนแน่ชัดแต่บอกทิศได้ '
             u'ดีกว่าการแต่งคำตอบ',
          9: u'<b>direction</b> คือทิศทาง ซึ่งตอบได้แม้ยังไม่มีแผนละเอียด',
          10: u'<b>the floor is yours</b> คือถึงตาคุณพูด · เมื่อผู้สัมภาษณ์เปิดให้ถาม ผู้สมัครควรมีคำถามเตรียมไว้'},
 }},

# ══════════════════════════════════ ชุดที่ 5 ══════════════════════════════════
{'id': 'F4', 'title': u'ชุดที่ 5', 'theme': u'รัดกุมเงื่อนไขเครดิต · สัมภาษณ์โครงการบัณฑิตใหม่',

 'p1': {
  'box': ['terms', 'outstanding', 'concentrated', 'overdue', 'incentive', 'collected',
          'deposit', 'settlement', 'release', 'discount',
          'write off', 'balance', 'exceed', 'waive'],
  'blocks': [
   {'who': 'The position today',
    't': "Our standard [[1]] are thirty days, but the time we actually wait is sixty-eight. "
         "Just over a fifth of the balance has been [[2]] for more than ninety days, and it is "
         "heavily [[3]]: eleven customers hold sixty-one percent of everything that is [[4]]."},
   {'who': 'Why it happens',
    't': "The sales [[5]] points the wrong way, because the team is paid on orders taken rather "
         "than on cash [[6]]. When a customer asks for another thirty days, the person who "
         "grants it carries none of the cost."},
   {'who': 'The proposal',
    't': "New customers would pay a [[7]] until they have a [[8]] record with us. Supply would "
         "stop automatically at sixty days, and only a credit manager could [[9]] it. And we "
         "would offer a [[10]] of one and a half percent for payment inside ten days."},
  ],
  'ans': {1: 'terms', 2: 'outstanding', 3: 'concentrated', 4: 'overdue', 5: 'incentive',
          6: 'collected', 7: 'deposit', 8: 'settlement', 9: 'release', 10: 'discount'},
  'exp': {1: u'<b>terms</b> ในบริบทการค้าคือเงื่อนไขการชำระเงิน เช่น thirty days',
          2: u'<b>outstanding</b> คือยังค้างชำระอยู่ · ใช้กับยอดที่ยังไม่ได้รับเงิน',
          3: u'<b>concentrated</b> คือกระจุกตัว ตรงข้ามกับกระจายทั่ว',
          4: u'<b>overdue</b> คือเกินกำหนดชำระแล้ว ซึ่งหนักกว่า outstanding ที่อาจยังไม่ถึงกำหนด',
          5: u'<b>incentive</b> คือสิ่งจูงใจ · ที่นี่คือวิธีจ่ายผลตอบแทนที่ทำให้พฤติกรรมเป็นอย่างที่เห็น',
          6: u'<b>cash collected</b> คือเงินที่เก็บได้จริง ต่างจาก orders taken ที่เป็นยอดสั่งซื้อ',
          7: u'<b>deposit</b> คือเงินมัดจำหรือเงินวางประกันก่อนให้เครดิต',
          8: u'<b>settlement record</b> คือประวัติการชำระเงิน ซึ่งใช้ดูว่าควรให้เครดิตหรือไม่',
          9: u'<b>release supply</b> คือปล่อยให้ส่งของต่อ หลังจากที่ระบบระงับไว้',
          10: u'<b>discount for early payment</b> คือส่วนลดเงินสด '
              u'· waive คือยกเว้นหรือสละสิทธิ ซึ่งความหมายไม่ตรง'},
 },

 'p2': {
  'box': ['simpler', 'mattered', 'shrinking', 'overnight', 'defend', 'submitted',
          'correction', 'pushed', 'eyes', 'flattering',
          'disagreed', 'guided', 'convinced', 'cohort'],
  'blocks': [
   {'who': 'Q: Tell me about a time when you disagreed with somebody in a team.',
    't': "One member of the group wanted to use a single growth rate for the whole forecast, "
         "because it was [[1]] to explain. I thought it hid the thing that [[2]], which was "
         "that two of the three segments were [[3]]."},
   {'who': 'Q: What did you do about it?',
    't': "We had four days left, so I built both versions [[4]] and brought them to the next "
         "meeting side by side. I didn't say his method was wrong. I asked the group which of "
         "the two we could [[5]] if the lecturer asked where the growth came from."},
   {'who': 'Q: And the outcome?',
    't': "They chose the segment version, and he chose it with them. He then spotted that I had "
         "the lease expiry dates wrong, and we [[6]] the piece with his [[7]] in it."},
   {'who': 'Q: What did you take from it?',
    't': "I was close to winning the argument and losing the work. If I had [[8]] him out of "
         "it, I wouldn't have had his second pair of [[9]]. That isn't an especially [[10]] "
         "thing to admit, but it is the honest lesson."},
  ],
  'ans': {1: 'simpler', 2: 'mattered', 3: 'shrinking', 4: 'overnight', 5: 'defend',
          6: 'submitted', 7: 'correction', 8: 'pushed', 9: 'eyes', 10: 'flattering'},
  'exp': {1: u'<b>simpler</b> คือง่ายกว่า · ประโยคเทียบสองวิธี จึงต้องใช้รูปขั้นกว่า',
          2: u'<b>matter</b> ใช้เป็นกริยาได้ แปลว่าสำคัญ · the thing that mattered คือสิ่งที่สำคัญจริง',
          3: u'<b>shrinking</b> คือกำลังหดตัว ใช้กับยอดขายหรือส่วนงานที่เล็กลงเรื่อย ๆ',
          4: u'<b>overnight</b> คือข้ามคืน บอกว่าเขาลงแรงเองนอกเวลา',
          5: u'<b>defend</b> ที่นี่คือแก้ต่างให้ตัวเลขได้เมื่อถูกถาม '
             u'· การเปลี่ยนคำถามจากใครถูกไปเป็นอะไรที่แก้ต่างได้ ทำให้ทีมตัดสินใจร่วมกันได้',
          6: u'<b>submit</b> คือส่งงาน · ที่นี่ต้องเป็นรูปอดีต submitted',
          7: u'<b>correction</b> คือสิ่งที่แก้ให้ถูก · การเอ่ยถึงการแก้ของเพื่อนร่วมทีมทำให้คำตอบไม่ดูยกตนข่มท่าน',
          8: u'<b>push somebody out of something</b> คือผลักให้เขาออกไปจากเรื่องนั้น',
          9: u'<b>a second pair of eyes</b> คือคนช่วยตรวจทานอีกคน เป็นสำนวนที่ใช้บ่อยในงานบัญชี',
          10: u'<b>flattering</b> คือทำให้ตัวเองดูดี · not a flattering thing to admit '
              u'คือไม่ใช่เรื่องน่าภูมิใจที่จะยอมรับ'},
 }},

# ══════════════════════════════════ ชุดที่ 6 ══════════════════════════════════
{'id': 'F5', 'title': u'ชุดที่ 6', 'theme': u'อธิบายผลต่างจากงบประมาณ · สัมภาษณ์ผู้ช่วยงานภาษี',

 'p1': {
  'box': ['timing', 'shortfall', 'apart', 'understated', 'lapsed', 'cover',
          'plain', 'mix', 'contribution', 'influence',
          'forecast', 'accrued', 'margin', 'discount'],
  'blocks': [
   {'who': 'Separating two different problems',
    't': "Revenue is three percent below budget, and that gap is almost entirely a question of "
         "[[1]]. The margin [[2]] is not. Those are two different problems, and I'd like you to "
         "hold them [[3]]."},
   {'who': 'The revenue line',
    't': "One customer moved an order out of June and into July. It has been invoiced and the "
         "cash has arrived, so the half-year revenue is [[4]] and the second half will carry "
         "it. I wouldn't ask for any action on that."},
   {'who': 'The freight element',
    't': "Roughly a third of the margin gap is freight. The annual contract [[5]] in February, "
         "and nobody arranged [[6]] when the contract manager left. I want to be [[7]] that "
         "this one was ours: procurement sits in my division."},
   {'who': 'The rest of the gap',
    't': "The remainder is [[8]] rather than price. We held our list prices, but the "
         "lower-margin bulk grades grew. Commission now follows [[9]] instead of volume. What "
         "customers order is something we can [[10]] but do not control."},
  ],
  'ans': {1: 'timing', 2: 'shortfall', 3: 'apart', 4: 'understated', 5: 'lapsed',
          6: 'cover', 7: 'plain', 8: 'mix', 9: 'contribution', 10: 'influence'},
  'exp': {1: u'<b>a question of timing</b> คือเป็นเรื่องจังหวะเวลา ไม่ใช่เรื่องผลประกอบการที่แย่ลง',
          2: u'<b>shortfall</b> คือจำนวนที่ขาดไปจากเป้า',
          3: u'<b>hold two things apart</b> คือแยกสองเรื่องออกจากกัน ไม่เอามาปนกัน',
          4: u'<b>understated</b> คือแสดงไว้ต่ำกว่าความจริง ตรงข้ามกับ overstated',
          5: u'<b>lapse</b> คือหมดอายุไปเองเพราะไม่มีใครต่อ ต่างจากการยกเลิกซึ่งมีคนตั้งใจทำ',
          6: u'<b>arrange cover</b> คือจัดคนมาทำงานแทนชั่วคราว',
          7: u'<b>I want to be plain that…</b> คือขอพูดตรง ๆ ว่า ใช้เมื่อจะยอมรับความผิดของฝ่ายตัวเอง',
          8: u'<b>mix</b> คือสัดส่วนของสิ่งที่ขายได้ · สาเหตุนี้ต่างจากราคาและจากต้นทุน',
          9: u'<b>contribution</b> คือกำไรส่วนเกิน ซึ่งเป็นฐานที่ควรใช้จ่ายค่าคอมมิชชัน',
          10: u'<b>influence</b> คือมีอิทธิพลต่อ ซึ่งอ่อนกว่า control คือควบคุมได้ '
              u'· คู่คำนี้ใช้บอกขอบเขตของคำสัญญา'},
 },

 'p2': {
  'box': ['ticked', 'complete', 'certificates', 'treated', 'queried', 'amend',
          'deduction', 'careful', 'sophisticated', 'announcements',
          'marks', 'drop', 'source', 'released'],
  'blocks': [
   {'who': 'Q: Tell me about a mistake that had consequences for somebody else.',
    't': "I [[1]] a schedule as [[2]] when I had forty-one of the forty-three [[3]]. The two "
         "that were missing were small, and I had a note from the client saying they would "
         "follow. I [[4]] the note as though it were the certificate itself."},
   {'who': 'Q: And what happened?',
    't': "The revenue department [[5]] it four months later. By then the client had changed "
         "bookkeeper and the documents couldn't be found. The firm had to [[6]] the return, and "
         "the client lost the [[7]]."},
   {'who': 'Q: What is the lesson?',
    't': "The lesson isn't that I should have been more [[8]], because everybody says that and "
         "it changes nothing. The lesson is that my schedule let a promise and a document look "
         "the same."},
   {'who': 'Q: How do you keep up with changes in the rules?',
    't': "Two habits, and I wouldn't claim either is [[9]]. I read the revenue department's "
         "[[10]] on the first Monday of the month, and I keep a file of the five rules I use "
         "most often, with the date I last checked each one."},
  ],
  'ans': {1: 'ticked', 2: 'complete', 3: 'certificates', 4: 'treated', 5: 'queried',
          6: 'amend', 7: 'deduction', 8: 'careful', 9: 'sophisticated', 10: 'announcements'},
  'exp': {1: u'<b>tick</b> คือทำเครื่องหมายถูก ซึ่งในกระดาษทำการหมายถึงรับรองว่าตรวจแล้ว',
          2: u'<b>tick something as complete</b> คือรับรองว่าครบถ้วน ซึ่งเป็นจุดที่ผิดพลาด',
          3: u'<b>certificates</b> ที่นี่คือหนังสือรับรองการหักภาษี ณ ที่จ่าย',
          4: u'<b>treat A as though it were B</b> คือทำกับ A เหมือนว่าเป็น B '
             u'· รูป were หลัง as though คือ subjunctive ใช้กับสิ่งที่ไม่จริง',
          5: u'<b>query</b> ใช้เป็นกริยาได้ แปลว่าตั้งคำถามหรือทักท้วง',
          6: u'<b>amend a return</b> คือยื่นแบบแสดงรายการภาษีเพิ่มเติมเพื่อแก้ไข',
          7: u'<b>deduction</b> คือรายการที่หักได้ · lose the deduction คือเสียสิทธิหักนั้นไป',
          8: u'<b>careful</b> คือระมัดระวัง · เธอยกคำนี้ขึ้นมาเพื่อปฏิเสธว่าเป็นบทเรียนที่ใช้ได้',
          9: u'<b>sophisticated</b> คือซับซ้อนหรือแพรวพราว · การบอกว่าวิธีของตัวเองไม่ซับซ้อน '
             u'ทำให้คำตอบน่าเชื่อว่าทำจริง',
          10: u'<b>announcements</b> คือประกาศของหน่วยงาน ซึ่งเป็นแหล่งข้อมูลชั้นต้น'},
 }},

# ══════════════════════════════════ ชุดที่ 7 ══════════════════════════════════
{'id': 'F6', 'title': u'ชุดที่ 7', 'theme': u'ผลการทดลองทำงานจากบ้าน · สัมภาษณ์ผู้ช่วยนักบัญชีโรงงาน',

 'p1': {
  'box': ['pilot', 'surveyed', 'informed', 'backlog', 'handover', 'fragile',
          'tickets', 'faults', 'settled', 'index',
          'temporary', 'predict', 'permanent', 'measured'],
  'blocks': [
   {'who': 'Scope of the study',
    't': "Forty-six people across four departments took part in the three-month [[1]]. We "
         "[[2]] them twice, in July and again in September. Seventy-one percent said their "
         "concentration had improved, but they also felt less [[3]] about what their colleagues "
         "were doing."},
   {'who': 'The operational effect',
    't': "Output held up wherever the work belongs to one person, and the reconciliation [[4]] "
         "actually came down. What failed was the goods-received [[5]], which had always been "
         "[[6]]. Being in the same room had been covering for a procedure nobody had written "
         "down."},
   {'who': 'The cost nobody expected',
    't': "[[7]] at the service desk rose by about thirty percent in the first six weeks, and "
         "most of them were not technical [[8]] at all. People were asking where a document "
         "was. It [[9]] down once we published a single [[10]] of where things live, so the "
         "cost was real but short-lived."},
  ],
  'ans': {1: 'pilot', 2: 'surveyed', 3: 'informed', 4: 'backlog', 5: 'handover',
          6: 'fragile', 7: 'tickets', 8: 'faults', 9: 'settled', 10: 'index'},
  'exp': {1: u'<b>pilot</b> ในบริบทธุรกิจคือการทดลองใช้ในวงจำกัดก่อนตัดสินใจทั้งองค์กร',
          2: u'<b>survey</b> ใช้เป็นกริยาได้ แปลว่าสำรวจความเห็น',
          3: u'<b>feel informed about…</b> คือรู้สึกว่าได้รับข้อมูลเพียงพอ',
          4: u'<b>backlog</b> คืองานค้างที่สะสมอยู่ · came down คือลดลง',
          5: u'<b>handover</b> คือการส่งต่องานจากคนหนึ่งไปอีกคน ซึ่งเป็นจุดที่ล้มเหลว',
          6: u'<b>fragile</b> คือเปราะบาง พร้อมจะพังเมื่อมีอะไรมากระทบ',
          7: u'<b>ticket</b> ที่ศูนย์บริการผู้ใช้คือเรื่องที่แจ้งเข้ามาหนึ่งรายการ',
          8: u'<b>faults</b> คือข้อขัดข้องทางเทคนิค · การบอกว่าไม่ใช่ fault ชี้ว่าปัญหาอยู่ที่อื่น',
          9: u'<b>settle down</b> คือเข้าที่เข้าทาง สงบลง ใช้กับสถานการณ์ที่ผันผวนแล้วกลับสู่ปกติ',
          10: u'<b>index</b> ที่นี่คือสารบัญหรือรายการบอกว่าอะไรเก็บไว้ที่ไหน'},
 },

 'p2': {
  'box': ['announced', 'collectors', 'evenings', 'affected', 'option', 'reference',
          'judge', 'lands', 'tedious', 'wear',
          'patient', 'dropped', 'queue', 'convenient'],
  'blocks': [
   {'who': 'Q: Tell me about something you tried that did not work.',
    't': "I [[1]] a change from cash to bank transfer two weeks before our main event. I didn't "
         "tell the two [[2]] who took money at the door, and I didn't think about members with "
         "no smartphone. It took me three [[3]] afterwards to work out who had paid."},
   {'who': 'Q: What did you do next?',
    't': "I didn't drop the idea, because the idea was right. I wrote down who was [[4]], spoke "
         "to the two at the door first, kept cash as an [[5]], and asked people to put their student "
         "number in the transfer [[6]]. That second attempt is the part I'd want you to [[7]] "
         "me on."},
   {'who': 'Q: And what would you say you are good at?',
    't': "I'm quite good at seeing what should change, and I was poor at asking who it [[8]] "
         "on. I'm patient with detail that other people find [[9]]. I won't say I enjoy it, but "
         "it doesn't [[10]] me down, and I've noticed that isn't true of everybody."},
  ],
  'ans': {1: 'announced', 2: 'collectors', 3: 'evenings', 4: 'affected', 5: 'option',
          6: 'reference', 7: 'judge', 8: 'lands', 9: 'tedious', 10: 'wear'},
  'exp': {1: u'<b>announce a change</b> คือประกาศการเปลี่ยนแปลง · ปัญหาของเธอคือประกาศก่อนคุยกับคนที่เกี่ยวข้อง',
          2: u'<b>collector</b> คือคนเก็บเงิน · สร้างจากกริยา collect เติม or',
          3: u'<b>three evenings</b> คือสามเย็น บอกว่าเสียเวลาหลังเลิกงานไปเท่าไร',
          4: u'<b>who was affected</b> คือใครได้รับผลกระทบ · นี่คือสิ่งที่เธอลืมคิดในรอบแรก',
          5: u'<b>keep something as an option</b> คือคงไว้เป็นทางเลือก ไม่บังคับ',
          6: u'<b>transfer reference</b> คือข้อความอ้างอิงที่ใส่ตอนโอนเงิน ใช้ระบุว่าใครโอน',
          7: u'<b>judge somebody on something</b> คือตัดสินใครจากสิ่งนั้น '
             u'· เธอขอให้ดูที่การแก้ไข ไม่ใช่ที่ความผิดพลาด',
          8: u'<b>land on somebody</b> คือตกไปอยู่กับใคร ใช้กับภาระที่เกิดจากการเปลี่ยนแปลง '
             u'· ประธานเป็น it จึงเติม s',
          9: u'<b>tedious</b> คือน่าเบื่อซ้ำซาก',
          10: u'<b>wear somebody down</b> คือบั่นทอนกำลังใจทีละน้อย '
              u'· การบอกว่าไม่ได้ชอบแต่ทนได้ น่าเชื่อกว่าการบอกว่าชอบงานซ้ำ ๆ'},
 }},

# ══════════════════════════════════ ชุดที่ 8 ══════════════════════════════════
{'id': 'F7', 'title': u'ชุดที่ 8', 'theme': u'เปลี่ยนวิธีนับสต๊อก · สัมภาษณ์นักวิเคราะห์การเงินเชิงพาณิชย์',

 'p1': {
  'box': ['shut', 'borrowed', 'recounted', 'locations', 'shipped', 'continuous',
          'announced', 'cleared', 'accumulate', 'discipline',
          'terminals', 'quarter', 'sign', 'acceptable'],
  'blocks': [
   {'who': 'What the December count costs',
    't': "We [[1]] the warehouse on the twenty-eighth and twenty-ninth of December. Forty-two "
         "people count, of whom about thirty are [[2]] from other departments. Last December we "
         "[[3]] one hundred and forty [[4]] because the first and second counts disagreed, and "
         "we held about eleven million baht of orders that would otherwise have [[5]]."},
   {'who': 'What the auditors would require',
    't': "A [[6]] count is acceptable in principle, but only on two conditions. Every location "
         "must be counted at least twice in the year, and the second count must not be [[7]]. "
         "And differences must be investigated and [[8]] within the same month, because if we "
         "let them [[9]], we end up with a number nobody will sign."},
   {'who': 'The catch',
    't': "What the new method needs, and I wouldn't want to understate this, is [[10]] every "
         "single week. The December count forgives a bad November. Counting through the year "
         "does not."},
  ],
  'ans': {1: 'shut', 2: 'borrowed', 3: 'recounted', 4: 'locations', 5: 'shipped',
          6: 'continuous', 7: 'announced', 8: 'cleared', 9: 'accumulate', 10: 'discipline'},
  'exp': {1: u'<b>shut</b> เป็นกริยาที่รูปอดีตเหมือนรูปปัจจุบัน แปลว่าปิด',
          2: u'<b>borrowed from other departments</b> คือยืมตัวมาจากแผนกอื่น',
          3: u'<b>recount</b> คือนับใหม่ · เติม re ข้างหน้าเพื่อบอกว่าทำซ้ำ',
          4: u'<b>location</b> ในคลังสินค้าคือตำแหน่งเก็บของหนึ่งจุด',
          5: u'<b>ship</b> คือส่งของออกไป · would otherwise have shipped คือถ้าไม่ปิดก็จะได้ส่งไปแล้ว',
          6: u'<b>continuous count</b> คือการนับหมุนเวียนต่อเนื่องตลอดปี ตรงข้ามกับการนับครั้งเดียวปลายปี',
          7: u'<b>announced</b> คือแจ้งล่วงหน้า · การนับรอบสองต้องไม่แจ้งล่วงหน้า จึงใช้ must not be announced',
          8: u'<b>clear a difference</b> คือสะสางส่วนที่ไม่ตรงกันให้จบ',
          9: u'<b>accumulate</b> คือสะสมพอกพูน · if we let them accumulate คือถ้าปล่อยให้ค้างไว้',
          10: u'<b>discipline</b> คือความสม่ำเสมอในการทำตามขั้นตอน ไม่ใช่การลงโทษ'},
 },

 'p2': {
  'box': ['background', 'donations', 'reserve', 'cross', 'shape', 'detail',
          'guess', 'route', 'memory', 'factor',
          'volunteered', 'retired', 'donation', 'admit'],
  'blocks': [
   {'who': 'Q: Tell me about explaining something financial to a non-finance audience.',
    't': "The committee were all volunteers and none of them had a finance [[1]]. They asked me "
         "why the kitchen was short of money when [[2]] had gone up. The answer was that food "
         "costs had risen far faster, and that the gap was coming out of a [[3]] with about "
         "seven months left in it."},
   {'who': 'Q: How did you explain it?',
    't': "I brought one sheet of paper with two lines on it and no figures at all. I asked them "
         "what they thought was happening, and one of them said straight away that the lines "
         "were going to [[4]]. They needed the [[5]] before the figures, so the order mattered "
         "more than the [[6]]."},
   {'who': 'Q: What do you do when you are asked something and you do not know?',
    't': "I say so. I'd rather say I don't know and come back in an hour than [[7]] and be "
         "remembered for it. What I try to add is a time and a [[8]]."},
   {'who': 'Q: Has that always come naturally?',
    't': "No, it was learned. In my first internship I answered a question about a stock balance "
         "from [[9]] and I was out by a [[10]] of ten. My supervisor pointed out that she now "
         "had to check everything else I had told her that week."},
  ],
  'ans': {1: 'background', 2: 'donations', 3: 'reserve', 4: 'cross', 5: 'shape',
          6: 'detail', 7: 'guess', 8: 'route', 9: 'memory', 10: 'factor'},
  'exp': {1: u'<b>a finance background</b> คือพื้นความรู้ทางการเงิน',
          2: u'ประโยคใช้ <b>had gone up</b> ซึ่งเป็นพหูพจน์ จึงต้องเป็น <b>donations</b> ไม่ใช่ donation',
          3: u'<b>reserve</b> คือเงินสำรองที่เก็บไว้ · with seven months left คือพอใช้ได้อีกเจ็ดเดือน',
          4: u'<b>the lines are going to cross</b> คือเส้นสองเส้นจะตัดกัน '
             u'ซึ่งเป็นจุดที่รายจ่ายแซงรายรับ',
          5: u'<b>shape</b> ที่นี่คือรูปร่างของปัญหา หรือภาพรวมก่อนลงรายละเอียด',
          6: u'<b>detail</b> คือรายละเอียด · บทเรียนคือลำดับสำคัญกว่าปริมาณรายละเอียด',
          7: u'<b>guess</b> คือเดา · เป็นสิ่งที่เขาเลือกไม่ทำ',
          8: u'<b>route</b> ที่นี่คือเส้นทางหรือวิธีที่จะไปหาคำตอบ',
          9: u'<b>from memory</b> คือตอบจากความจำโดยไม่เปิดเอกสาร',
          10: u'<b>out by a factor of ten</b> คือผิดไปสิบเท่า '
              u'· factor of ten หมายถึงคูณหรือหารสิบ ไม่ใช่ต่างกันสิบหน่วย'},
 }},

# ══════════════════════════════════ ชุดที่ 9 ══════════════════════════════════
{'id': 'F8', 'title': u'ชุดที่ 9', 'theme': u'รายงานผลสอบทานงานจัดซื้อ · สัมภาษณ์ผู้ช่วยฝ่ายบริหารเงิน',

 'p1': {
  'box': ['fieldwork', 'findings', 'conclusion', 'limit', 'gap', 'records',
          'contract', 'suspended', 'creation', 'released',
          'approval', 'signature', 'runs', 'minutes'],
  'blocks': [
   {'who': 'Opening the report',
    't': "Oraphan led the [[1]] and we are presenting the [[2]] of the review of purchasing at "
         "the Rayong plant. Let me give you the [[3]] first. The control that failed was not "
         "the approval [[4]]. It was that the same person could create a supplier and approve a "
         "payment to it. Everything else in this report follows from that one [[5]]."},
   {'who': 'What was found',
    't': "Four of the nineteen cases were not explained, and all four involved one supplier. "
         "That supplier received eleven payments for maintenance at a site that had been closed "
         "for a year. There are no work [[6]] and there is no [[7]]. Both individuals have been "
         "[[8]] on full pay while the employment process runs."},
   {'who': 'The recommendations',
    't': "Supplier [[9]] moves out of purchasing entirely and sits with the master data team. "
         "And no payment is [[10]] to a supplier created within the previous thirty days "
         "without a second signature."},
  ],
  'ans': {1: 'fieldwork', 2: 'findings', 3: 'conclusion', 4: 'limit', 5: 'gap',
          6: 'records', 7: 'contract', 8: 'suspended', 9: 'creation', 10: 'released'},
  'exp': {1: u'<b>fieldwork</b> คือการลงตรวจที่หน้างาน ต่างจากการวางแผนหรือการเขียนรายงาน',
          2: u'<b>findings</b> คือสิ่งที่ตรวจพบ · ใช้รูปพหูพจน์เสมอในรายงานตรวจสอบ',
          3: u'<b>give you the conclusion first</b> คือบอกข้อสรุปก่อน ตามหลัก Pyramid Principle',
          4: u'<b>approval limit</b> คือวงเงินอนุมัติ · ผู้รายงานตัดสาเหตุนี้ออกไปตั้งแต่ต้น',
          5: u'<b>gap</b> ที่นี่คือช่องว่างของระบบควบคุม ซึ่งก็คือการไม่แบ่งแยกหน้าที่',
          6: u'<b>work records</b> คือหลักฐานว่ามีการทำงานจริง · ไม่มีหลักฐานนี้คือข้อสังเกตสำคัญ',
          7: u'<b>contract</b> คือสัญญาจ้าง · การจ่ายเงินโดยไม่มีสัญญาเป็นข้อบกพร่องของการควบคุม',
          8: u'<b>suspended on full pay</b> คือพักงานโดยยังได้รับเงินเดือน '
             u'ซึ่งเป็นวิธีปฏิบัติระหว่างสอบข้อเท็จจริง',
          9: u'<b>supplier creation</b> คือการตั้งผู้ขายรายใหม่ในระบบ '
             u'· การย้ายงานนี้ออกไปคือการแบ่งแยกหน้าที่',
          10: u'<b>release a payment</b> คือปล่อยให้จ่ายเงินออกไป · ที่นี่ต้องเป็นรูป passive คือ is released'},
 },

 'p2': {
  'box': ['inputs', 'reliably', 'marked', 'shape', 'risk', 'incomplete',
          'absent', 'habits', 'intentions', 'private',
          'locks', 'share', 'landed', 'stopped'],
  'blocks': [
   {'who': 'Q: Tell me about a deadline you did not control.',
    't': "The [[1]] came from three places, and one of them, the overseas branch, was [[2]] "
         "late. One week the file didn't arrive at all. I sent what I had before the deadline, "
         "clearly [[3]] as two branches out of three, with the last four weeks of the missing "
         "branch beside it so that he could see the usual [[4]] of it."},
   {'who': 'Q: Was there anything else in it?',
    't': "One line on what the [[5]] was, which is the part he told me afterwards was useful. "
         "The lesson I took is that something [[6]] and on time, with the gap shown, is worth "
         "more than something complete and late. But that only holds if you say exactly what is "
         "[[7]]."},
   {'who': 'Q: How do you handle confidential information?',
    't': "In practice it comes down to small [[8]] rather than good [[9]]. I don't discuss what "
         "I'm working on outside the team, I lock the screen even for two minutes, and I don't "
         "send a draft to my own [[10]] email to work on at home."},
  ],
  'ans': {1: 'inputs', 2: 'reliably', 3: 'marked', 4: 'shape', 5: 'risk',
          6: 'incomplete', 7: 'absent', 8: 'habits', 9: 'intentions', 10: 'private'},
  'exp': {1: u'<b>inputs</b> คือข้อมูลที่ป้อนเข้ามา · ประโยคใช้ came ซึ่งเป็นพหูพจน์ จึงต้องเป็น inputs',
          2: u'<b>reliably late</b> คือสายเป็นปกติทุกครั้ง เป็นการประชดเบา ๆ ที่ใช้กันในที่ทำงาน',
          3: u'<b>marked as…</b> คือระบุกำกับไว้ว่า · การกำกับให้ชัดคือสิ่งที่ทำให้งานไม่ครบยังใช้ได้',
          4: u'<b>the usual shape of it</b> คือหน้าตาตามปกติของตัวเลขชุดนั้น',
          5: u'<b>risk</b> คือความเสี่ยง · บรรทัดที่บอกว่าตัวเลขอาจผิดไปทางไหน คือส่วนที่ผู้บริหารต้องการ',
          6: u'<b>incomplete</b> คือไม่ครบ · คู่กับ on time ในประโยคเปรียบเทียบ',
          7: u'<b>absent</b> คือสิ่งที่ขาดไป · ใช้เป็นคำนามรวมในวลี what is absent',
          8: u'<b>habits</b> คือนิสัยที่ทำเป็นกิจวัตร · เธอเทียบนิสัยกับเจตนา',
          9: u'<b>good intentions</b> คือเจตนาดี ซึ่งอย่างเดียวไม่พอสำหรับการรักษาความลับ',
          10: u'<b>private email</b> คืออีเมลส่วนตัว · การส่งงานไปอีเมลตัวเองเป็นช่องรั่วที่พบบ่อย'},
 }},

# ══════════════════════════════════ ชุดที่ 10 ═════════════════════════════════
{'id': 'F9', 'title': u'ชุดที่ 10', 'theme': u'ข้อเสนอเปิดคลังแห่งที่สอง · สัมภาษณ์นักวิเคราะห์ที่ปรึกษา',

 'p1': {
  'box': ['lease', 'expires', 'saving', 'justify', 'transit', 'reliability',
          'fit-out', 'assumption', 'modelled', 'payback',
          'downside', 'weigh', 'demand', 'approve'],
  'blocks': [
   {'who': 'Why a decision is needed today',
    't': "The [[1]] we have been offered [[2]] on the fifteenth of December, which is why we "
         "are asking you to decide this morning rather than in January."},
   {'who': 'What actually makes the case',
    't': "The proposal was first raised in order to cut freight cost, but the freight [[3]] on "
         "its own would not [[4]] the project. What justifies it is service. The difference "
         "between the north and the centre is almost all [[5]] time, and three of the four "
         "accounts we lost last year named delivery [[6]] first."},
   {'who': 'The numbers and the uncertainty',
    't': "The premises, the [[7]] and the additional stock come to about thirty-one million baht "
         "in the first year. The contribution from holding those accounts is an [[8]] and not a "
         "measurement, so I have [[9]] it at half as well. At half it still works, but the "
         "[[10]] moves from under three years to over five."},
  ],
  'ans': {1: 'lease', 2: 'expires', 3: 'saving', 4: 'justify', 5: 'transit',
          6: 'reliability', 7: 'fit-out', 8: 'assumption', 9: 'modelled', 10: 'payback'},
  'exp': {1: u'<b>lease</b> คือสัญญาเช่า',
          2: u'<b>expire</b> คือสิ้นอายุ · ประธานเป็นเอกพจน์ the lease จึงเติม s',
          3: u'<b>saving</b> คือจำนวนที่ประหยัดได้ ใช้เป็นคำนาม',
          4: u'<b>justify</b> คือทำให้มีเหตุผลเพียงพอที่จะทำ · ใช้กับการพิจารณาข้อเสนอลงทุน',
          5: u'<b>transit time</b> คือเวลาที่สินค้าอยู่ระหว่างขนส่ง',
          6: u'<b>delivery reliability</b> คือความน่าเชื่อถือของการส่งมอบ ว่าส่งได้ตรงเวลาสม่ำเสมอแค่ไหน',
          7: u'<b>fit-out</b> คือการตกแต่งและติดตั้งอุปกรณ์ในอาคารเช่า',
          8: u'<b>assumption</b> คือข้อสมมติ · ผู้พูดแยกข้อสมมติออกจากการวัดผลจริงอย่างชัดเจน',
          9: u'<b>model</b> ใช้เป็นกริยาได้ แปลว่าทำแบบจำลองคำนวณ · ที่นี่ต้องเป็นรูปอดีต',
          10: u'<b>payback</b> คือระยะเวลาคืนทุน ยิ่งยาวยิ่งเสี่ยง'},
 },

 'p2': {
  'box': ['flattering', 'deep', 'advantage', 'settling', 'split', 'estate',
          'holding', 'matched', 'causes', 'picture',
          'evidence', 'stand', 'competitor', 'promotion'],
  'blocks': [
   {'who': 'Q: Why consulting rather than a finance role in industry?',
    't': "Two reasons, and the second is less [[1]] than the first. I'd rather learn across "
         "several businesses than go [[2]] into one straight away, and this is the only job I "
         "know of where not yet knowing is an [[3]]. The second reason is that I'm a little "
         "afraid of [[4]] into a routine too early."},
   {'who': 'Q: A client with forty outlets is losing profit. Where would you start?',
    't': "May I ask two questions first? Has it happened in every outlet or in some, and has it "
         "happened in revenue or in cost? Those two answers [[5]] the problem four ways. Once I "
         "knew, I'd stop looking at the whole [[6]] and start comparing the twelve weak outlets "
         "with twelve that are [[7]] up, [[8]] as closely as I can on size and type of "
         "location."},
   {'who': 'Q: And what would you deliver at the end of the week?',
    't': "At the end of one week I'd rather hand over two likely [[9]] with the evidence for "
         "each, and say plainly what I haven't looked at, than a full [[10]] I can't stand "
         "behind."},
  ],
  'ans': {1: 'flattering', 2: 'deep', 3: 'advantage', 4: 'settling', 5: 'split',
          6: 'estate', 7: 'holding', 8: 'matched', 9: 'causes', 10: 'picture'},
  'exp': {1: u'<b>flattering</b> คือทำให้ตัวเองดูดี · less flattering คือฟังดูไม่สวยเท่า',
          2: u'<b>go deep into something</b> คือลงลึกในเรื่องเดียว ตรงข้ามกับ learn across',
          3: u'<b>an advantage</b> คือข้อได้เปรียบ · เธอพลิกข้อด้อยคือยังไม่รู้ ให้เป็นข้อดีของงานนี้',
          4: u'หลัง afraid of ต้องเป็นกริยาเติม ing จึงเป็น <b>settling into a routine</b> '
             u'คือลงหลักปักฐานอยู่กับงานประจำ',
          5: u'<b>split a problem four ways</b> คือแบ่งปัญหาออกเป็นสี่ทาง '
             u'· เป็นวิธีคิดแบบจำกัดขอบเขตก่อนลงมือ',
          6: u'<b>estate</b> ในธุรกิจค้าปลีกคือกลุ่มสาขาทั้งหมดที่กิจการมี',
          7: u'<b>hold up</b> คือยังไปได้ดี ไม่ทรุด · ที่นี่ใช้รูป are holding up',
          8: u'<b>matched on size and location</b> คือจับคู่ให้เหมือนกันในเรื่องขนาดและทำเล '
             u'เพื่อให้ตัวแปรที่ต่างกันเหลือน้อย',
          9: u'<b>causes</b> คือสาเหตุ · ใช้พหูพจน์เพราะเธอเสนอสองสาเหตุที่น่าจะเป็น',
          10: u'<b>a full picture I can’t stand behind</b> คือภาพรวมที่ตัวเองยืนยันไม่ได้ '
              u'· stand behind something คือรับรองสิ่งนั้น'},
 }},

]
