# -*- coding: utf-8 -*-
u"""บทฟังสำหรับ Part 3 · Listening ของข้อสอบเสมือนจริง<ปลายภาค> วิชาภาษาอังกฤษ

ต่างจาก tools/listening-data.py ซึ่งเป็นชุด<กลางภาค> ที่อิง Unit 2 กับ Unit 12
ชุดนี้อิงแนวข้อสอบปลายภาค คือ Book 2 ถึง Book 4 ว่าด้วย Presentations
และ Job Interviews จึงมีบทสองแบบสลับกันทุกชุด

  presentation · การนำเสนอในที่ประชุม มีผู้พูดตั้งแต่สองคนขึ้นไป
                 วางโครงตาม WISEOWL ตอนเปิด Pyramid Principle ตอนเนื้อหา
                 และปิดด้วย summary กับ call to action ตาม Book 2
  interview    · การสัมภาษณ์งาน มีผู้พูดสองคนคือผู้สัมภาษณ์กับผู้สมัคร
                 เดินตาม Four Phases และใช้ SAR+L, Three S, CIQ, softening
                 ตาม Book 3 และ Book 4

── กติกาสำคัญ คลิปต้องไม่พูดคำตอบออกมาตรง ๆ ──
กติกาเดียวกับชุดกลางภาค tools/make-listening.py บังคับด้วยเครื่อง
ถ้าตัวเลือกที่ถูกไปตรงกับข้อความในบททั้งวลี หรือมีคำเนื้อความครบทุกคำในช่วงสั้น ๆ
จะไม่ยอมสังเคราะห์เสียงให้เลย ตัวเลือกที่ถูกจึงต้องเป็นอย่างใดอย่างหนึ่งใน
  ถอดความ · ใช้ศัพท์เรียกสิ่งที่บทเล่าเป็นอาการ · คำนวณ · หรือตีความ

── เขียนให้เหมาะกับนิสิตบัญชีชั้นปีที่ 3 ──
เรื่องที่พูดถึงเป็นงานที่นิสิตบัญชีจะเจอจริง เช่น ระบบเบิกค่าใช้จ่าย การจ้างภายนอก
การประเมินผู้ขาย การควบคุมภายใน และการสัมภาษณ์ตำแหน่งผู้ช่วยผู้สอบบัญชี
นักวิเคราะห์การเงิน และผู้ตรวจสอบภายใน

ไม่ใช้ชื่อบริษัทจริงหรือบุคคลจริงเลย ทุกกิจการและทุกตัวละครสมมติขึ้นใหม่
ความยาวคุมไว้ราว 300 คำต่อคลิป ได้คลิปละราวสองนาที

ไฟล์นี้ให้เฉพาะ SETS ส่วน VOICES ใช้ร่วมกับ tools/listening-data.py
เพื่อไม่ให้รายการเสียงแตกออกเป็นสองชุดที่ค่อย ๆ ต่างกัน
"""

SETS = [

# ══════════════════════════════════ ชุดที่ 2 ══════════════════════════════════
{'id': 'F1', 'title': u'ชุดที่ 2', 'parts': [

 {'id': 'F1a', 'kind': 'presentation',
  'title': 'Replacing the Expense Claim System',
  'context': u'ทีมสามคนเสนอคณะกรรมการการเงินให้เปลี่ยนระบบเบิกค่าใช้จ่ายจากกระดาษเป็นแอป '
             u'เปิดด้วย WISEOWL วางเนื้อหาแบบ Pyramid และปิดด้วยข้อเสนอให้ตัดสินใจ',
  'turns': [
   ('Nattha', 'n', 'f1',
    "Good morning everyone, and thank you for making time. My name is Nattha, and I work in the "
    "finance operations team. With me are Krit from internal audit and Supaporn from IT. Over the "
    "next twelve minutes we will ask you to approve a replacement for the expense claim system. "
    "Please hold your questions until the end, and we will leave eight minutes for them."),
   ('Nattha', 'n', 'f1',
    "Here is our message in one line. The paper process is costing us more than the software would, "
    "so we should stop running it. Everything after this slide is evidence for that single claim. "
    "Krit will give you the cost picture, Supaporn will cover the system itself, and I will come "
    "back at the end with what we need from you today."),
   ('Krit', 'k', 'm1',
    "Thank you, Nattha. Last year staff submitted forty-one thousand claim forms. Finance touched "
    "every one of them by hand. We timed the work over six weeks: fourteen minutes of staff time "
    "per claim once you add approval, keying and filing. At our average loaded rate that comes to "
    "roughly nine hundred and fifty thousand baht a year in time alone."),
   ('Krit', 'k', 'm1',
    "That is only the visible part. Sixty-two claims last year were paid twice, because the paper "
    "copy and the scanned copy both reached us. We recovered most of it, but not all. And when the "
    "auditors asked for a sample of forty claims in March, it took two staff four days to find "
    "thirty-eight of them. Two we never found at all."),
   ('Supaporn', 's', 'f2',
    "Thanks, Krit. So what would replace it? Staff photograph the receipt on their phone, the "
    "system reads the amount and the date, and the claim goes straight to the approver. No paper "
    "moves anywhere. The licence is four hundred and twenty thousand baht a year, plus a one-off "
    "setup of three hundred thousand in the first year."),
   ('Supaporn', 's', 'f2',
    "I want to be straight with you about the risks, because two of them are real. The reading of "
    "handwritten receipts is about ninety-one percent accurate, so roughly one claim in eleven "
    "still needs a human eye. And staff who have filled in the same form for nine years will not "
    "enjoy the first month. We have budgeted for two training sessions in every department."),
   ('Nattha', 'n', 'f1',
    "So, to bring the three parts together. The present way of working costs us close to a million "
    "baht a year in time, loses documents the auditors ask for, and pays some suppliers twice. The "
    "replacement costs less than that even in the year we install it, and from the second year it "
    "costs under half. What we need from this committee today is approval to sign for three years. "
    "Thank you. We are glad to take your questions now."),
  ],
  'questions': [
   {'q': 'How does Nattha open the presentation?',
    'o': ['By greeting the audience, introducing the team and setting out the timing',
          'By showing the first set of figures immediately',
          'By asking the committee what they already know about the system',
          'By apologising for the length of the session'], 'a': 0,
    'e': u'เปิดด้วยการทักทาย แนะนำตัวและทีม แล้วบอกกรอบเวลากับช่วงถามตอบ '
         u'ตรงกับขั้นต้นของ WISEOWL คือ welcome, introduce, subject และ outline'},
   {'q': 'What is the single claim that the rest of the presentation supports?',
    'o': ['The current way of working is more expensive than the software',
          'The software will reduce the number of claims staff submit',
          'The finance team is too small for the volume of work',
          'The auditors have asked the company to change systems'], 'a': 0,
    'e': u'"The paper process is costing us more than the software would" '
         u'· การวางข้อสรุปไว้ก่อนแล้วค่อยให้หลักฐานตามมา คือ Pyramid Principle'},
   {'q': 'How did the team arrive at the fourteen minutes per claim?',
    'o': ['They measured the work themselves over a period of weeks',
          'They used a figure published by the software supplier',
          'They asked each department to estimate it',
          'They took it from last year audit report'], 'a': 0,
    'e': u'"We timed the work over six weeks" · การจับเวลาเองคือการวัด ไม่ใช่การประมาณหรือหยิบตัวเลขคนอื่นมาใช้'},
   {'q': 'Why were sixty-two claims paid twice?',
    'o': ['The same claim arrived through two different routes',
          'Approvers signed the same form twice',
          'Staff deliberately submitted duplicates',
          'The bank processed the payment file twice'], 'a': 0,
    'e': u'"the paper copy and the scanned copy both reached us" · เอกสารชุดเดียวเดินทางมาถึงสองทาง '
         u'จึงถูกจ่ายซ้ำ ไม่ได้เกิดจากคนอนุมัติหรือจากธนาคาร'},
   {'q': 'What does the March sample tell us about the filing?',
    'o': ['Records were slow to retrieve and a few were missing altogether',
          'Records were complete but stored in the wrong order',
          'The auditors asked for more claims than finance could produce',
          'The claims had been destroyed under the retention policy'], 'a': 0,
    'e': u'ใช้เวลาสองคนสี่วันหาได้ 38 จาก 40 แปลว่าค้นช้าและหายไปสองฉบับ '
         u'· ข้อสรุปนี้ได้จากตัวเลข ไม่ได้มีใครพูดคำว่าช้าหรือหายออกมา'},
   {'q': 'What happens to a receipt under the proposed system?',
    'o': ['An image is captured and the details are extracted automatically',
          'It is posted to the finance department as usual',
          'It is scanned by the finance team on arrival',
          'It is kept by the member of staff until year end'], 'a': 0,
    'e': u'"Staff photograph the receipt on their phone, the system reads the amount and the date" '
         u'· ถ่ายภาพแล้วระบบดึงข้อมูลเอง คือ capture และ extract'},
   {'q': 'What is the difference between the two cost figures Supaporn gives?',
    'o': ['One is charged every year and the other only at the start',
          'One covers the software and the other covers training',
          'One is a maximum and the other is a minimum',
          'One applies to the finance team and the other to all staff'], 'a': 0,
    'e': u'"a one-off setup of three hundred thousand in the first year" '
         u'· ตัวหนึ่งเป็นค่าลิขสิทธิ์รายปี อีกตัวเก็บครั้งเดียวตอนติดตั้ง '
         u'การแยกรายจ่ายประจำออกจากรายจ่ายครั้งเดียวเป็นสิ่งที่ผู้ฟังสายบัญชีต้องจับให้ได้'},
   {'q': 'Roughly how often will a claim still need to be checked by a person?',
    'o': ['Just under one claim in every ten',
          'About one claim in every ninety',
          'About one claim in every two',
          'Almost every claim'], 'a': 0,
    'e': u'อ่านแม่น 91 เปอร์เซ็นต์ แปลว่าราวหนึ่งใน 11 ต้องให้คนดู ซึ่งใกล้เคียงหนึ่งในสิบ '
         u'· ตัวลวงคือหยิบเลข 91 มาอ่านเป็นหนึ่งในเก้าสิบ'},
   {'q': 'How does Supaporn handle the weak points of the proposal?',
    'o': ['She raises them herself and explains how each will be managed',
          'She leaves them for the question session',
          'She says there are no significant risks',
          'She asks the committee to raise any concerns they have'], 'a': 0,
    'e': u'"I want to be straight with you about the risks" แล้วตามด้วยแผนอบรมสองรอบทุกแผนก '
         u'· การยกจุดอ่อนขึ้นมาเองพร้อมทางแก้ ทำให้ข้อเสนอน่าเชื่อถือกว่าการรอให้ถูกถาม'},
   {'q': 'What does Nattha ask the committee to do at the close?',
    'o': ['Agree to a three-year commitment',
          'Run a pilot in one department first',
          'Review the figures and meet again next month',
          'Ask the supplier for a lower price'], 'a': 0,
    'e': u'"approval to sign for three years" · การปิดที่ดีต้องสรุปใจความแล้วบอกให้ชัดว่า '
         u'ต้องการให้ผู้ฟังทำอะไรต่อ ซึ่งคือ call to action'},
  ]},

 {'id': 'F1b', 'kind': 'interview',
  'title': 'Interview for a Junior Auditor Position',
  'context': u'ผู้สัมภาษณ์ถามผู้สมัครตำแหน่งผู้ช่วยผู้สอบบัญชี มีทั้งคำถามเปิดตัว '
             u'คำถามเชิงพฤติกรรมที่ต้องตอบแบบ SAR+L และคำถามปิดท้าย',
  'turns': [
   ('Interviewer', 'i', 'm2',
    "Good afternoon. Thank you for coming in. I am Daniel Oakes, I lead the assurance team here at "
    "Brightwater, and this will take about forty minutes. I will ask you a few questions, then "
    "there will be time for yours. Shall we start?"),
   ('Pim', 'p', 'f3',
    "Good afternoon. Yes, please."),
   ('Interviewer', 'i', 'm2',
    "So, tell me something about yourself."),
   ('Pim', 'p', 'f3',
    "Certainly. I am in my final year of an accounting degree at Siriwat University, and I expect "
    "to finish in May. Last summer I spent ten weeks with a mid-sized firm, mostly on inventory "
    "counts and bank confirmations for three manufacturing clients. What I took from that was how "
    "much of the work is really about asking the right question of the right person. That is why I "
    "am applying to a firm that puts juniors in front of clients early, which I understand you do."),
   ('Interviewer', 'i', 'm2',
    "Good. Now tell me about a time when you noticed something was wrong and had to raise it with "
    "someone more senior than you."),
   ('Pim', 'p', 'f3',
    "Yes. During that placement I was testing goods received notes against purchase orders for one "
    "client. There were about two hundred in my sample. I found eleven where the quantity on the "
    "note was higher than the quantity ordered, and all eleven came from the same supplier and the "
    "same two weeks."),
   ('Pim', 'p', 'f3',
    "My task was only to tick and sign, and the senior on the job was very busy that week. But I "
    "did not think I could sign something I was not comfortable with. So I put the eleven into a "
    "short table, wrote two sentences on what the pattern was, and asked for ten minutes of her "
    "time rather than catching her in the corridor."),
   ('Pim', 'p', 'f3',
    "She took it to the manager the same afternoon. It turned out the supplier had been shipping "
    "part orders and then re-sending the balance under the original reference, so the client had "
    "been receiving goods twice against one order. The client changed its receiving procedure "
    "before the year end."),
   ('Pim', 'p', 'f3',
    "What I learned is that a concern is much easier to act on when it arrives organised. If I had "
    "said I think something looks odd with the goods received notes, I am not sure anything would "
    "have happened that week."),
   ('Interviewer', 'i', 'm2',
    "That is useful, thank you. Last one from me. What would you say is a weakness of yours?"),
   ('Pim', 'p', 'f3',
    "I tend to carry on checking after the point where the evidence is already sufficient. On the "
    "placement my senior told me I had spent a day and a half on a section that was budgeted at "
    "half a day. Since then I have started agreeing with whoever is running the job what finished "
    "looks like before I begin, and I flag it the moment I think I will go over. It has not "
    "disappeared, but it is now something I manage rather than something I discover afterwards."),
  ],
  'questions': [
   {'q': 'What does the interviewer do in his first turn?',
    'o': ['He introduces himself and explains how the interview will run',
          'He asks the candidate to describe her degree',
          'He explains what the firm does',
          'He asks whether the candidate has any questions'], 'a': 0,
    'e': u'แนะนำตัว บอกบทบาท บอกระยะเวลาและลำดับขั้น คือ opening phase ของการสัมภาษณ์ '
         u'ซึ่งมีไว้ลดความตึงเครียดและทำให้ผู้สมัครรู้ว่าจะเจออะไร'},
   {'q': 'How does Pim structure her answer to the opening question?',
    'o': ['Present situation, then relevant experience, then why this firm',
          'Childhood, then education, then hobbies',
          'Her strengths, then her weaknesses, then her goals',
          'A list of every job she has held'], 'a': 0,
    'e': u'เรียงจากสถานะปัจจุบัน ไปประสบการณ์ที่เกี่ยวข้อง แล้วปิดด้วยเหตุผลที่สมัครที่นี่ '
         u'· คำถาม tell me about yourself ไม่ได้ขอประวัติส่วนตัว แต่ขอสิ่งที่เกี่ยวกับงาน'},
   {'q': 'What pattern did Pim find in the eleven exceptions?',
    'o': ['They were concentrated with one supplier over a short period',
          'They were spread evenly across all suppliers',
          'They all involved the same member of staff',
          'They all fell in the final week of the year'], 'a': 0,
    'e': u'"all eleven came from the same supplier and the same two weeks" '
         u'· กระจุกตัวที่ผู้ขายรายเดียวในช่วงสั้น ๆ คือ concentrated'},
   {'q': 'Why did Pim decide not to simply sign the work off?',
    'o': ['She was not satisfied that the evidence supported it',
          'Her senior had instructed her to escalate anything unusual',
          'The firm manual required a second signature',
          'She had run out of time to finish the testing'], 'a': 0,
    'e': u'"I did not think I could sign something I was not comfortable with" '
         u'· เธอยังไม่พอใจกับหลักฐาน ไม่ใช่เพราะมีคำสั่งหรือกฎบังคับ'},
   {'q': 'How did Pim choose to raise the issue?',
    'o': ['She prepared a written summary and asked for a scheduled slot',
          'She mentioned it quickly when she passed her senior in the corridor',
          'She sent it straight to the manager',
          'She waited until the end of the assignment'], 'a': 0,
    'e': u'"put the eleven into a short table, wrote two sentences…and asked for ten minutes of her time" '
         u'· เตรียมมาเป็นลายลักษณ์อักษรและขอเวลาอย่างเป็นทางการ ตรงข้ามกับการพูดแวบเดียวตอนเดินสวนกัน'},
   {'q': 'What had the supplier actually been doing?',
    'o': ['Delivering orders in instalments but quoting the original reference each time',
          'Charging for goods it had never delivered',
          'Delivering goods that had not been ordered at all',
          'Raising invoices before the goods were shipped'], 'a': 0,
    'e': u'"shipping part orders and then re-sending the balance under the original reference" '
         u'· ส่งเป็นงวดแล้วอ้างอิงเลขที่ใบสั่งซื้อเดิมทุกครั้ง ทำให้นับซ้ำ ไม่ใช่การส่งของที่ไม่ได้สั่ง'},
   {'q': 'Which part of the SAR+L structure is “What I learned is that a concern is much easier to act on when it arrives organised”?',
    'o': ['The lesson', 'The situation', 'The action', 'The result'], 'a': 0,
    'e': u'SAR+L คือ situation, action, result แล้วปิดด้วย lesson '
         u'· ประโยคที่ขึ้นต้นว่าสิ่งที่ได้เรียนรู้คือ เป็นส่วน L เสมอ'},
   {'q': 'What does Pim name as her weakness?',
    'o': ['Spending longer on testing than the work requires',
          'Finding it hard to speak to senior colleagues',
          'Losing concentration on repetitive tasks',
          'Being uncomfortable with figures'], 'a': 0,
    'e': u'"I tend to carry on checking after the point where the evidence is already sufficient" '
         u'· ทำเกินกว่าที่งานต้องการ คือการใช้เวลานานเกินไปกับการทดสอบ'},
   {'q': 'What makes her weakness answer a strong one?',
    'o': ['She names a real limitation and shows the steps she now takes to control it',
          'She chooses a weakness that is really a strength in disguise',
          'She explains that the problem has now gone completely',
          'She blames the budget she was given'], 'a': 0,
    'e': u'คำตอบที่ดีต้องเป็นจุดอ่อนจริง มีวิธีจัดการที่เป็นรูปธรรม และซื่อตรงพอที่จะบอกว่ายังไม่หายไปทั้งหมด '
         u'· "It has not disappeared, but it is now something I manage"'},
   {'q': 'What does Pim say she now agrees before starting a section?',
    'o': ['What a completed piece of work should look like',
          'How many hours she will be paid for',
          'Which colleague will review her work',
          'Which client contact she may speak to'], 'a': 0,
    'e': u'"agreeing with whoever is running the job what finished looks like before I begin" '
         u'· ตกลงนิยามของคำว่าเสร็จไว้ก่อน เป็นวิธีคุมเวลาที่ใช้ได้จริง'},
  ]},

]},

# ══════════════════════════════════ ชุดที่ 3 ══════════════════════════════════
{'id': 'F2', 'title': u'ชุดที่ 3', 'parts': [

 {'id': 'F2a', 'kind': 'presentation',
  'title': 'A Proposal to Outsource Payroll',
  'context': u'ทีมสามคนเสนอคณะกรรมการให้ย้ายงานประมวลผลเงินเดือนออกไปให้ผู้ให้บริการภายนอก '
             u'แต่เก็บการควบคุมไว้ในองค์กร เปิดด้วยข้อสรุปแล้วค่อยให้เหตุผล',
  'turns': [
   ('Araya', 'a', 'f1',
    "Good morning, and thank you all for coming. I am Araya, head of payroll, and with me are "
    "Thanet from human resources and Chanin from finance. We have twenty minutes, and our subject "
    "is the payroll function. We will ask you for a decision at the end, so please keep your "
    "questions until then."),
   ('Araya', 'a', 'f1',
    "Our message is short. We cannot staff payroll safely for the next two years, so the "
    "processing should go to a provider while the control stays here. Thanet will explain the "
    "staffing position, Chanin will give you the numbers, and I will close."),
   ('Thanet', 't', 'm1',
    "Thank you. The payroll team is five people. Two of them reach retirement within the next "
    "eighteen months, and a third has told us she is moving to Chiang Mai in April. We advertised "
    "the senior payroll post twice this year. We had nine applications and interviewed two. "
    "Neither of them accepted."),
   ('Thanet', 't', 'm1',
    "I want to be clear about what that means. By next October we could be running payroll for one "
    "thousand two hundred and forty staff with two people, one of whom joined in March. That is "
    "not a workload problem. It is a single point of failure."),
   ('Chanin', 'c', 'm3',
    "On cost. Running payroll in house costs us sixty-one baht per payslip, once you include "
    "salaries, the software licence and our share of the finance system. The two providers we "
    "approached quoted thirty-eight baht and forty-four baht. Both prices hold for three years."),
   ('Chanin', 'c', 'm3',
    "There is a second number worth your attention. Last year one point eight percent of payslips "
    "had to be corrected after issue. Most of the amounts were small, but each one takes a phone "
    "call, a recalculation and sometimes a separate transfer. We spent around four hundred hours "
    "on corrections alone."),
   ('Chanin', 'c', 'm3',
    "I should say that the comparison is not a perfect one. Our sixty-one baht includes work the "
    "provider will not do, such as answering questions from staff about their tax. We would keep "
    "two people here for that, and I have already included their cost in the figure I gave you."),
   ('Araya', 'a', 'f1',
    "Two risks, and I will not hide either of them. The first is that we lose direct sight of the "
    "calculation. We deal with that by keeping the review and the approval of every run inside "
    "this building. Nothing is paid without a signature from my team. The second is the data. "
    "Salary histories go to a third party, so the contract has to carry the right clauses, and our "
    "legal team has drafted them already."),
   ('Araya', 'a', 'f1',
    "So, to put the three parts together. We cannot recruit, the in-house cost sits above both "
    "quotations, and corrections are taking four hundred hours a year. What we ask of the "
    "committee today is permission to open negotiations with the cheaper of the two providers and "
    "to bring you a draft contract in February. Thank you. Your questions now, please."),
  ],
  'questions': [
   {'q': 'What does Araya ask the audience to do with their questions?',
    'o': ['Wait until the presentation has finished',
          'Interrupt whenever something is unclear',
          'Send them in writing after the meeting',
          'Put them to Chanin rather than to her'], 'a': 0,
    'e': u'"please keep your questions until then" · การบอกตั้งแต่ต้นว่าจะถามได้เมื่อไร '
         u'เป็นส่วนหนึ่งของการวางกรอบในขั้นเปิด ทำให้ผู้ฟังไม่ต้องเดา'},
   {'q': 'What single claim does the rest of the presentation support?',
    'o': ['Payroll cannot be staffed reliably, so processing should be handed outside',
          'The payroll software needs to be replaced',
          'The payroll team should be made larger',
          'Payroll costs have risen faster than expected'], 'a': 0,
    'e': u'"We cannot staff payroll safely for the next two years, so the processing should go to a '
         u'provider while the control stays here" · ข้อสรุปมาก่อน หลักฐานตามมา'},
   {'q': 'Why does Thanet call the staffing position a single point of failure?',
    'o': ['Too few experienced people would be left to cover the work',
          'Only one provider is able to do the work',
          'The payroll software runs on one computer',
          'Only one person is authorised to approve payments'], 'a': 0,
    'e': u'เหลือสองคนทำเงินเดือนให้พนักงาน 1,240 คน และคนหนึ่งเพิ่งเข้ามาเดือนมีนาคม '
         u'· single point of failure หมายถึงจุดเดียวที่ถ้าพลาดแล้วงานทั้งระบบหยุด'},
   {'q': 'What happened when the senior payroll post was advertised?',
    'o': ['Very few people applied and no one took the job',
          'The best candidate asked for too much money',
          'The post was filled but the person left quickly',
          'Human resources cancelled the recruitment'], 'a': 0,
    'e': u'"We had nine applications and interviewed two. Neither of them accepted" '
         u'· ผู้สมัครน้อยและไม่มีใครรับข้อเสนอ'},
   {'q': 'How do the two quotations compare with the in-house cost?',
    'o': ['Both come in below what the company pays now',
          'Both are above what the company pays now',
          'One is above and one is below',
          'They are about the same as the current cost'], 'a': 0,
    'e': u'ทำเองอยู่ที่ 61 บาทต่อใบ ผู้ให้บริการเสนอ 38 กับ 44 บาท '
         u'· ทั้งสองรายอยู่ใต้ต้นทุนปัจจุบัน'},
   {'q': 'Why is a corrected payslip expensive?',
    'o': ['Each one needs several follow-up actions by staff',
          'The amounts involved are usually large',
          'A penalty is charged by the tax authority',
          'The payroll software charges for each correction'], 'a': 0,
    'e': u'"each one takes a phone call, a recalculation and sometimes a separate transfer" '
         u'· ต้นทุนอยู่ที่งานที่ตามมา ไม่ใช่ที่จำนวนเงิน ซึ่ง Chanin บอกว่าส่วนใหญ่เป็นยอดเล็ก'},
   {'q': 'Why does Chanin say the comparison is not perfect?',
    'o': ['The internal figure covers tasks the provider will not take on',
          'The provider prices may change during the contract',
          'The internal figure excludes the software licence',
          'The two providers quoted on different terms'], 'a': 0,
    'e': u'"Our sixty-one baht includes work the provider will not do" '
         u'· ผู้นำเสนอที่น่าเชื่อถือจะบอกข้อจำกัดของตัวเลขตัวเองด้วย ไม่ปล่อยให้ผู้ฟังไปเจอเอง'},
   {'q': 'How will the company keep control of the calculation?',
    'o': ['Every run will still be checked and authorised internally',
          'A copy of the provider software will be installed in house',
          'The provider will send a monthly report to the committee',
          'The internal audit team will test one run each quarter'], 'a': 0,
    'e': u'"keeping the review and the approval of every run inside this building" '
         u'· งานประมวลผลออกไปข้างนอก แต่การสอบทานกับการอนุมัติยังอยู่ข้างใน'},
   {'q': 'What has already been done about the risk to the data?',
    'o': ['The contract wording has been prepared',
          'The provider has been audited',
          'Salary records have been made anonymous',
          'A separate insurance policy has been taken out'], 'a': 0,
    'e': u'"our legal team has drafted them already" · them หมายถึง clauses ในสัญญา '
         u'· ความเสี่ยงที่มีทางรับมือเตรียมไว้แล้ว ย่อมเบากว่าความเสี่ยงที่ยังไม่มีใครแตะ'},
   {'q': 'What decision does Araya ask for?',
    'o': ['Permission to begin talks with one of the providers',
          'Approval to sign a contract immediately',
          'Agreement to make two payroll staff redundant',
          'Approval of the payroll budget for next year'], 'a': 0,
    'e': u'"permission to open negotiations with the cheaper of the two providers" '
         u'· ยังไม่ขอให้เซ็นสัญญา ขอแค่ให้เริ่มเจรจาและจะกลับมาเสนอร่างสัญญาในเดือนกุมภาพันธ์'},
  ]},

 {'id': 'F2b', 'kind': 'interview',
  'title': 'Interview for a Financial Analyst Position',
  'context': u'ผู้จัดการฝ่ายวางแผนและวิเคราะห์สัมภาษณ์ผู้สมัครตำแหน่งนักวิเคราะห์การเงิน '
             u'มีคำถามว่าทำไมจึงสมัคร คำถามเชิงพฤติกรรมเรื่องการโน้มน้าว และคำถามเรื่องจุดที่ต้องพัฒนา',
  'turns': [
   ('Interviewer', 'i', 'f2',
    "Good morning. I am Helena Ward, and I manage the planning and analysis team. Three of us are "
    "seeing candidates today and I am the first. We have about thirty minutes. I will start with a "
    "general question, then move on to some examples from your experience, and I will leave time "
    "at the end for anything you would like to ask me."),
   ('Wit', 'w', 'm2',
    "Thank you. That sounds fine."),
   ('Interviewer', 'i', 'f2',
    "Would you start by telling me why you applied for this role?"),
   ('Wit', 'w', 'm2',
    "Of course. I finish an accounting degree in May, with a minor in statistics, and I have spent "
    "the last two semesters doing the forecasting for a student-run cafe on campus. Its turnover "
    "is around two million baht a year, which is small, but it is real money and real decisions. "
    "What I found is that I enjoy the part where the numbers change somebody's mind. Your "
    "advertisement said the team sits in the monthly business reviews rather than sending a pack "
    "and leaving, and that is the part I want."),
   ('Interviewer', 'i', 'f2',
    "Thank you. Now, tell me about a time when you had to persuade somebody who did not agree with "
    "your analysis."),
   ('Wit', 'w', 'm2',
    "Yes. At the cafe we were deciding whether to keep opening on Sundays. The manager was certain "
    "Sunday was profitable, because the takings were good. I looked at it hour by hour and found "
    "that Sunday takings were around seventy percent of a weekday, while the staffing cost was the "
    "same, and we paid a weekend rate on top of it."),
   ('Wit', 'w', 'm2',
    "My job was only to produce the monthly pack, so I could have left it there. Instead I asked "
    "him for fifteen minutes and brought two things. The first was Sunday on its own, with the "
    "weekend rate shown separately. The second was what the same eight hours would earn if we "
    "moved them to Friday evening, which was our busiest window."),
   ('Wit', 'w', 'm2',
    "He did not agree in the meeting, and I think that was fair, because he had six months of "
    "habit against one page from me. What he did agree to was a trial. We closed on Sundays for "
    "one month and extended Friday. The month came out ahead, and he made the change permanent in "
    "the following term."),
   ('Wit', 'w', 'm2',
    "What I took from it is that people rarely move position because the analysis is correct. They "
    "move when the next step is small enough to try. If I had asked him to close Sundays for good, "
    "I am fairly sure the answer would have been no."),
   ('Interviewer', 'i', 'f2',
    "That is helpful. One more. What would your previous supervisor say you need to work on?"),
   ('Wit', 'w', 'm2',
    "I would say presentation, in the narrow sense. My analysis has been sound, but I used to hand "
    "over a spreadsheet with everything in it and expect the reader to find the point. He told me, "
    "quite directly, that if the conclusion is on row forty, nobody will reach it. So now I write "
    "the finding in one sentence at the top and keep the working behind it. It is a habit rather "
    "than an instinct at this stage, which is why I still check it before I send anything."),
  ],
  'questions': [
   {'q': 'What does Helena explain before the questions begin?',
    'o': ['That she is one of several interviewers, and how her part will run',
          'That the role has already been offered to another candidate',
          'That the interview will be recorded',
          'That she has not had time to read his application'], 'a': 0,
    'e': u'"Three of us are seeing candidates today and I am the first" แล้วบอกลำดับและเวลา '
         u'· ขั้นเปิดของการสัมภาษณ์มีไว้ให้ผู้สมัครรู้ว่าจะเจออะไร'},
   {'q': 'Why does Wit mention how small the cafe is?',
    'o': ['To show that the stakes were genuine despite the modest scale',
          'To explain why his forecasts were often wrong',
          'To suggest that he is ready for something larger',
          'To account for the gap in his experience'], 'a': 0,
    'e': u'"which is small, but it is real money and real decisions" '
         u'· เขายอมรับขนาดก่อน แล้วชี้ว่าสิ่งที่ได้ฝึกคือการตัดสินใจจริง ไม่ใช่แบบฝึกหัด'},
   {'q': 'What attracted Wit to this particular team?',
    'o': ['The analysts join the discussion instead of only supplying reports',
          'The team works with much larger figures',
          'The team allows staff to choose their own projects',
          'The role includes training in statistics'], 'a': 0,
    'e': u'"the team sits in the monthly business reviews rather than sending a pack and leaving" '
         u'· เขาอ่านประกาศรับสมัครมาแล้วหยิบจุดที่ตรงกับสิ่งที่ตัวเองอยากทำ'},
   {'q': 'What had the manager based his view of Sunday on?',
    'o': ['The amount of money the day brought in',
          'The number of customers who came in',
          'What other cafes nearby were doing',
          'The preference of the weekend staff'], 'a': 0,
    'e': u'"The manager was certain Sunday was profitable, because the takings were good" '
         u'· takings คือยอดเงินที่รับเข้ามา เขาดูแต่ด้านรายได้ ไม่ได้ดูด้านต้นทุน'},
   {'q': 'What did the hour-by-hour analysis show?',
    'o': ['Revenue was lower but the cost of staffing was not',
          'Both revenue and staffing cost were lower',
          'Revenue was higher in the evening than at midday',
          'Sunday was the busiest day of the week'], 'a': 0,
    'e': u'ยอดวันอาทิตย์อยู่ราวร้อยละเจ็ดสิบของวันธรรมดา แต่ต้นทุนพนักงานเท่าเดิมและยังมีค่าแรงวันหยุดเพิ่ม '
         u'· รายได้ลดแต่ต้นทุนไม่ลด'},
   {'q': 'What were the two things Wit brought to the meeting?',
    'o': ['A view of one day alone, and a comparison with another trading period',
          'Two years of figures and a written recommendation',
          'A forecast and a list of the risks',
          'The monthly pack and a note from a colleague'], 'a': 0,
    'e': u'อย่างแรกคือวันอาทิตย์แยกเดี่ยวพร้อมแยกค่าแรงวันหยุดออกมา '
         u'อย่างที่สองคือถ้าย้ายชั่วโมงเดียวกันไปเย็นวันศุกร์จะได้เท่าไร'},
   {'q': 'Why does Wit think it was fair that the manager did not agree at once?',
    'o': ['The manager long-standing experience outweighed one page of analysis',
          'The analysis contained an error the manager had spotted',
          'The manager had not been given the figures in advance',
          'The decision was not the manager to take'], 'a': 0,
    'e': u'"he had six months of habit against one page from me" '
         u'· ผู้สมัครที่มองมุมของอีกฝ่ายได้ มักทำงานร่วมกับคนอื่นได้ดีกว่า'},
   {'q': 'What did the manager agree to instead?',
    'o': ['A limited test before committing',
          'To review the figures again next term',
          'To hand the decision to the owners',
          'To reduce the weekend rate'], 'a': 0,
    'e': u'"What he did agree to was a trial" · ทดลองหนึ่งเดือนก่อน แล้วค่อยเปลี่ยนเป็นการถาวร'},
   {'q': 'According to Wit, what finally moves people?',
    'o': ['A first step that feels low in risk',
          'Being shown that the analysis is correct',
          'Pressure from somebody more senior',
          'Seeing what a competitor has done'], 'a': 0,
    'e': u'"people rarely move position because the analysis is correct. They move when the next '
         u'step is small enough to try" · บทเรียนคือต้องทำให้ก้าวถัดไปเล็กพอที่อีกฝ่ายจะกล้าลอง'},
   {'q': 'What weakness does Wit name, and what does he now do about it?',
    'o': ['He used to bury the conclusion, and now states it at the start',
          'He used to rush his analysis, and now allows more time',
          'He used to avoid presenting, and now volunteers for it',
          'He used to work alone, and now asks for review'], 'a': 0,
    'e': u'"if the conclusion is on row forty, nobody will reach it. So now I write the finding in '
         u'one sentence at the top" · จุดอ่อนจริง มีวิธีแก้ที่เป็นรูปธรรม และยังยอมรับว่าต้องคอยตรวจตัวเอง'},
  ]},

]},

# ══════════════════════════════════ ชุดที่ 4 ══════════════════════════════════
{'id': 'F3', 'title': u'ชุดที่ 4', 'parts': [

 {'id': 'F3a', 'kind': 'presentation',
  'title': 'Recommending One of Two Audit Software Packages',
  'context': u'ทีมตรวจสอบภายในสามคนเปรียบเทียบซอฟต์แวร์สองตัวที่ทดลองใช้ '
             u'แล้วเสนอคณะกรรมการว่าควรเลือกตัวไหนและเพราะอะไร',
  'turns': [
   ('Benja', 'b', 'f3',
    "Good afternoon everybody. My name is Benja and I lead the internal audit team. Ratana and "
    "Korn are here with me. Over the next quarter of an hour we will compare the two audit "
    "software packages we tested, and we will tell you which one we recommend and why. We have "
    "handed round a one-page summary, so there is no need to write anything down."),
   ('Benja', 'b', 'f3',
    "Let me give you the recommendation first and the reasoning afterwards. We recommend the "
    "second package, which is called Audara, even though it is the dearer of the two. Ratana will "
    "take you through how we tested them, Korn will cover what we found, and I will come back to "
    "the price."),
   ('Ratana', 'r', 'f2',
    "We did not want a demonstration from a salesperson, so we ran both packages on our own data. "
    "We took the trade payables file for last year, four hundred and eleven thousand lines, and "
    "gave the same five tests to each one. Three of our juniors used each package for a week with "
    "no training at all, and we timed them."),
   ('Ratana', 'r', 'f2',
    "We also did something a little unusual. We put eleven errors into the file ourselves and said "
    "nothing to the juniors. We wanted to know what each package would surface and what it would "
    "let through."),
   ('Korn', 'k', 'm3',
    "Here is what came out of that. The first package, which I will call Package A, completed all "
    "five tests and was quicker to pick up. Our juniors were productive on day two. It found seven "
    "of our eleven planted errors. Audara took until day four before anybody was comfortable with "
    "it, but it found ten."),
   ('Korn', 'k', 'm3',
    "The one that got past both of them was the same kind in each case, a payment to a supplier "
    "whose bank details had changed during the year. Neither package reads that history, so we "
    "will keep doing that test by hand."),
   ('Korn', 'k', 'm3',
    "The other difference matters for the audit file. Audara keeps a record of every step the user "
    "takes and writes it to a log we cannot edit. Package A lets you export your workings, but if "
    "somebody repeats a test with a different filter, there is nothing to show that the earlier "
    "attempt happened. Our external auditors raised exactly that point in their management letter "
    "two years ago."),
   ('Benja', 'b', 'f3',
    "On price. Audara is roughly a third dearer across three years. What that difference buys you "
    "is three more findings out of eleven, and a record of the work that answers the point the "
    "external auditors made. What you give up is two days of learning time per person, once."),
   ('Benja', 'b', 'f3',
    "To summarise, both packages do the testing. One of them also proves what we did. We would "
    "like the committee to approve Audara, and we are happy to take your questions."),
  ],
  'questions': [
   {'q': 'Why does Benja mention the one-page summary?',
    'o': ['So the audience can follow without taking notes',
          'Because the slides are not working',
          'So the audience can read ahead of the speakers',
          'Because the full report is confidential'], 'a': 0,
    'e': u'"so there is no need to write anything down" '
         u'· ผู้ฟังที่ก้มจดจะไม่ได้ฟัง การแจกสรุปหน้าเดียวจึงปลดภาระนั้นออกไป'},
   {'q': 'Where does the recommendation come in this presentation?',
    'o': ['At the beginning, before the supporting detail',
          'At the very end, after all the evidence',
          'In the middle, between the two speakers',
          'It is left for the committee to work out'], 'a': 0,
    'e': u'"Let me give you the recommendation first and the reasoning afterwards" '
         u'· วางข้อสรุปไว้ยอดพีระมิดแล้วให้เหตุผลรองรับ ผู้ฟังจะรู้ตั้งแต่ต้นว่ากำลังฟังไปหาอะไร'},
   {'q': 'Why did the team avoid a supplier demonstration?',
    'o': ['They preferred evidence from their own records to a sales pitch',
          'The suppliers refused to visit the office',
          'A demonstration would have cost extra',
          'They had already seen both packages demonstrated'], 'a': 0,
    'e': u'"We did not want a demonstration from a salesperson, so we ran both packages on our own '
         u'data" · ผู้ขายย่อมสาธิตด้วยข้อมูลที่ตัวเองเตรียมมา ซึ่งบอกไม่ได้ว่าจะใช้กับงานจริงได้ไหม'},
   {'q': 'What condition was placed on the juniors who tested the packages?',
    'o': ['They had to use the software without being taught first',
          'They had to work in pairs',
          'They were told which errors to look for',
          'They had to finish within one day'], 'a': 0,
    'e': u'"Three of our juniors used each package for a week with no training at all" '
         u'· ตั้งใจไม่อบรม เพื่อวัดว่าซอฟต์แวร์เรียนรู้ได้เร็วแค่ไหนด้วยตัวมันเอง'},
   {'q': 'Why were eleven errors put into the file?',
    'o': ['To see which problems each package could detect',
          'To test how fast each package could run',
          'To check whether the juniors were working carefully',
          'To meet a requirement of the external auditors'], 'a': 0,
    'e': u'"We wanted to know what each package would surface and what it would let through" '
         u'· วางของผิดที่รู้คำตอบอยู่แล้วลงไป จึงวัดความสามารถในการจับได้จริง'},
   {'q': 'How did the two packages differ in ease of learning?',
    'o': ['Package A had people working sooner',
          'Audara had people working sooner',
          'Both took about the same time',
          'Neither could be used without training'], 'a': 0,
    'e': u'Package A ทำงานได้วันที่สอง ส่วน Audara ต้องถึงวันที่สี่ '
         u'· Package A เรียนรู้ง่ายกว่า แต่จับข้อผิดพลาดได้น้อยกว่า'},
   {'q': 'Why will one test still be done by hand?',
    'o': ['Neither package looks at changes in a supplier banking details',
          'The data for that test is held outside the system',
          'The committee asked for one manual test',
          'Both packages were too slow for that test'], 'a': 0,
    'e': u'"Neither package reads that history" · ไม่มีตัวไหนดูประวัติการเปลี่ยนเลขบัญชีของผู้ขาย '
         u'ซึ่งเป็นช่องทางทุจริตที่พบบ่อย จึงต้องตรวจด้วยมือต่อไป'},
   {'q': 'What is the weakness of Package A for the audit file?',
    'o': ['A repeated test leaves no trace of the earlier attempt',
          'Workings cannot be exported from it at all',
          'It does not record who ran each test',
          'Its log can be read only by the supplier'], 'a': 0,
    'e': u'"there is nothing to show that the earlier attempt happened" '
         u'· ถ้าลองใหม่ด้วยเงื่อนไขอื่นได้โดยไม่เหลือร่องรอย ผู้สอบบัญชีก็พิสูจน์ไม่ได้ว่าทำอะไรไปแล้ว'},
   {'q': 'Why does the record of each step matter so much here?',
    'o': ['The external auditors had already criticised its absence',
          'The law requires it for payables testing',
          'It allows two juniors to share one licence',
          'It makes the tests run faster'], 'a': 0,
    'e': u'"Our external auditors raised exactly that point in their management letter two years ago" '
         u'· ข้อเสนอนี้แก้ประเด็นที่ถูกทักไว้แล้ว ซึ่งหนักกว่าการชอบฟังก์ชันหนึ่งเป็นการส่วนตัว'},
   {'q': 'How does Benja present the extra cost?',
    'o': ['As a trade: better detection and a defensible record, against some learning time',
          'As a figure that cannot be avoided',
          'As an amount already included in the budget',
          'As a cost that the supplier may still reduce'], 'a': 0,
    'e': u'เธอบอกว่าส่วนต่างซื้ออะไรได้ และต้องแลกกับอะไร '
         u'· การวางได้กับเสียไว้ข้างกันเปิดโอกาสให้ผู้ฟังตัดสินใจเอง ไม่ใช่การเชียร์'},
  ]},

 {'id': 'F3b', 'kind': 'interview',
  'title': 'Interview for an Internal Audit Position',
  'context': u'หัวหน้าฝ่ายตรวจสอบภายในสัมภาษณ์ผู้สมัคร ถามว่าทำไมต้องเลือกเธอ '
             u'ขอตัวอย่างจากประสบการณ์ ถามเป้าหมายห้าปี แล้วเปิดให้ผู้สมัครถามกลับ',
  'turns': [
   ('Interviewer', 'i', 'm1',
    "Good morning, do come in. I am Samuel Reid, head of internal audit. Thank you for sending the "
    "case exercise through on time. We will spend about forty minutes together. I would like to "
    "hear about your experience, then I have two situations I would like your view on, and after "
    "that the floor is yours."),
   ('Ornicha', 'o', 'f3',
    "Thank you very much."),
   ('Interviewer', 'i', 'm1',
    "Why should we take you rather than another final-year student with the same grades?"),
   ('Ornicha', 'o', 'f3',
    "I would put it this way. Grades tell you that I can pass an examination. What I would bring "
    "beyond that is a year of actually finding things. I worked part time in the accounts office "
    "of a hospital group while studying, three days a week for a year. By the end I was "
    "reconciling the pharmacy stock, which nobody wanted to do because it never balanced. It "
    "taught me to sit with a figure that is wrong and keep going until I know why."),
   ('Interviewer', 'i', 'm1',
    "Give me an example of that."),
   ('Ornicha', 'o', 'f3',
    "The pharmacy stock was short by between two and five percent every month, and that had been "
    "accepted as wastage for years. I started recording not just the shortfall but when it "
    "appeared. The gap always showed up after a week in which a delivery had arrived on a "
    "Saturday."),
   ('Ornicha', 'o', 'f3',
    "My role was to reconcile, not to investigate, so I told my supervisor what I had seen before "
    "I went any further. She asked me to carry on for two more months and keep it between the two "
    "of us, which I did. Saturday deliveries were being signed for by a porter and left in the "
    "corridor, because the pharmacist was not on duty and the store room was locked."),
   ('Ornicha', 'o', 'f3',
    "Once we knew that, the fix was dull. Deliveries were moved to weekdays. The shortfall fell to "
    "under half a percent and stayed there. The part I am proud of is not the finding. It is that "
    "I told somebody at the right moment, instead of either saying nothing or going round my "
    "supervisor."),
   ('Ornicha', 'o', 'f3',
    "The lesson I took is that a pattern in the timing can be worth more than the size of the "
    "difference. For months everybody had been looking at how much was missing. Nobody had looked "
    "at when."),
   ('Interviewer', 'i', 'm1',
    "Thank you. Where would you like to be in five years?"),
   ('Ornicha', 'o', 'f3',
    "I would rather not pretend to a precise plan. What I can tell you is the direction. I want to "
    "be the person who can take an area nobody understands well and come back with something the "
    "business can act on. Whether that is a senior role in internal audit or a move into "
    "operations, I am honestly not sure yet, and I would rather say that than invent an answer."),
   ('Interviewer', 'i', 'm1',
    "Fair enough. Is there anything you would like to ask me?"),
   ('Ornicha', 'o', 'f3',
    "Two things, if I may. First, when a junior here raises something uncomfortable, who hears "
    "about it and how quickly? Second, you mentioned the case exercise. Could you tell me what you "
    "were hoping to see in it? I would find that useful whether or not I end up working here."),
  ],
  'questions': [
   {'q': 'What does the interviewer set out before the questions start?',
    'o': ['The order of the interview and that she will have her own turn to ask',
          'The salary and the holiday entitlement',
          'The names of everyone she will meet during the day',
          'The result of the case exercise she submitted'], 'a': 0,
    'e': u'"I would like to hear about your experience, then I have two situations…and after that '
         u'the floor is yours" · the floor is yours หมายถึงถึงตาคุณถาม'},
   {'q': 'How does Ornicha answer the question about why she should be chosen?',
    'o': ['By naming something her grades cannot show',
          'By comparing herself with the other candidates',
          'By listing the subjects she scored highest in',
          'By saying she needs the position more than others do'], 'a': 0,
    'e': u'"Grades tell you that I can pass an examination. What I would bring beyond that is a '
         u'year of actually finding things" · ไม่ปฏิเสธเกรด แต่ชี้ไปที่สิ่งที่เกรดวัดไม่ได้'},
   {'q': 'What did reconciling the pharmacy stock teach her?',
    'o': ['To stay with an unexplained difference until she understands it',
          'To accept that some differences cannot be explained',
          'To finish routine work as quickly as possible',
          'To ask for help as soon as something does not balance'], 'a': 0,
    'e': u'"It taught me to sit with a figure that is wrong and keep going until I know why" '
         u'· นี่คือนิสัยที่งานตรวจสอบต้องการ คือไม่ปล่อยยอดที่อธิบายไม่ได้ให้ผ่านไป'},
   {'q': 'What did she start recording in addition to the shortfall?',
    'o': ['When each gap appeared',
          'Which supplier the stock came from',
          'Who had counted the stock',
          'How the wastage had been approved'], 'a': 0,
    'e': u'"I started recording not just the shortfall but when it appeared" '
         u'· เพิ่มมิติเวลาเข้าไปในข้อมูลที่คนอื่นดูแต่ยอด'},
   {'q': 'What did the timing point to?',
    'o': ['Stock that arrived outside the normal working week',
          'A member of staff who worked only at weekends',
          'A monthly reporting deadline',
          'A fault in the stock recording system'], 'a': 0,
    'e': u'"The gap always showed up after a week in which a delivery had arrived on a Saturday" '
         u'· ของมาถึงในวันที่ไม่ใช่วันทำงานปกติ'},
   {'q': 'What did she do before taking the matter any further?',
    'o': ['She reported what she had noticed to her supervisor',
          'She counted the stock a second time',
          'She spoke to the porter who signed for deliveries',
          'She wrote a report for the finance director'], 'a': 0,
    'e': u'"I told my supervisor what I had seen before I went any further" '
         u'· งานของเธอคือกระทบยอด ไม่ใช่สอบสวน จึงส่งเรื่องให้คนที่มีอำนาจตัดสินใจ'},
   {'q': 'What was actually happening to the Saturday deliveries?',
    'o': ['They were left unsecured because the right person was not there',
          'They were being delivered to the wrong address',
          'They were signed for but never arrived',
          'They were recorded twice in the stock system'], 'a': 0,
    'e': u'"signed for by a porter and left in the corridor, because the pharmacist was not on duty '
         u'and the store room was locked" · ของวางไว้ในที่ที่ไม่มีการควบคุม'},
   {'q': 'What is she most proud of in this story?',
    'o': ['Raising the matter through the right channel at the right moment',
          'Finding the cause of the shortfall',
          'Reducing the wastage to under half a percent',
          'Carrying on with the work for two extra months'], 'a': 0,
    'e': u'"The part I am proud of is not the finding. It is that I told somebody at the right '
         u'moment" · เธอชี้ที่การใช้ช่องทางให้ถูก ไม่ใช่ที่ผลงาน'},
   {'q': 'How does she handle the question about five years from now?',
    'o': ['She gives a direction and admits she cannot be more exact',
          'She says she expects to be managing the team',
          'She says she has not thought about it',
          'She asks what the usual career path is'], 'a': 0,
    'e': u'"I would rather not pretend to a precise plan. What I can tell you is the direction" '
         u'· ซื่อตรงแต่ไม่ลอย ยังตอบได้ว่าอยากไปทางไหน'},
   {'q': 'What do her own two questions have in common?',
    'o': ['Both are about how the organisation behaves rather than about the package',
          'Both are about the salary and the hours',
          'Both ask the interviewer to judge her performance',
          'Both concern training and qualifications'], 'a': 0,
    'e': u'ข้อแรกถามว่าถ้าเด็กใหม่ทักเรื่องไม่สบายใจแล้วใครรับเรื่องเร็วแค่ไหน ข้อสองถามว่าแบบฝึกหัดต้องการเห็นอะไร '
         u'· ทั้งสองถามถึงวิธีทำงานขององค์กร ไม่ใช่ผลตอบแทน'},
  ]},

]},

# ══════════════════════════════════ ชุดที่ 5 ══════════════════════════════════
{'id': 'F4', 'title': u'ชุดที่ 5', 'parts': [

 {'id': 'F4a', 'kind': 'presentation',
  'title': 'A Proposal to Tighten Credit Terms',
  'context': u'ทีมควบคุมสินเชื่อ ฝ่ายขาย และฝ่ายระบบบัญชี เสนอคณะกรรมการให้รัดกุมเรื่องเงื่อนไขการให้เครดิต '
             u'โดยขอทดลองกับลูกค้ารายใหม่ก่อน',
  'turns': [
   ('Pornthip', 'p', 'f2',
    "Good morning. I am Pornthip from the credit control team, and this is Decha from sales and "
    "Ying from the finance systems group. Our subject this morning is the terms we give our "
    "customers. We will take fifteen minutes, and at the end we will ask you to approve a trial. "
    "Do stop me if a figure is not clear, but the broader questions are best kept for the end."),
   ('Pornthip', 'p', 'f2',
    "Our conclusion is this. We are lending money to our customers at no charge and without ever "
    "deciding to. Everything that follows is the evidence for it. Ying will show you where the "
    "overdue balances sit, Decha will put the sales view, and I will come back with what we "
    "propose."),
   ('Ying', 'y', 'f3',
    "Let me start with the receivables balance, which stood at one hundred and eighty-four million "
    "baht at the end of September. Our standard terms are thirty days. The time we actually wait, "
    "on average, is sixty-eight. Just over a fifth of the balance has been outstanding for more "
    "than ninety days."),
   ('Ying', 'y', 'f3',
    "What surprised us is how concentrated it is. Eleven customers account for sixty-one percent "
    "of everything overdue. These are not small accounts that slipped through a gap. They are "
    "large accounts that have learned that nothing happens."),
   ('Decha', 'd', 'm1',
    "I will give you the sales view, and it is not a comfortable one for me. My team is paid on "
    "orders taken, not on cash collected. So when a customer asks for another thirty days, the "
    "person who grants it carries none of the cost. I am not defending that. I am saying it "
    "explains the pattern better than any argument about discipline does."),
   ('Decha', 'd', 'm1',
    "I would ask you to hold one thing in mind, though. Two or three of those eleven will walk if "
    "we turn rigid overnight. I do not think that is a reason to do nothing. I think it is a reason "
    "to start with new customers rather than with the book we already have."),
   ('Pornthip', 'p', 'f2',
    "So here is the proposal, in three parts. New customers pay a deposit until they have a "
    "settlement record with us. Supply stops automatically at sixty days overdue, and releasing it "
    "needs my signature rather than the salesperson's. And we offer one and a half percent off for "
    "payment inside ten days."),
   ('Pornthip', 'p', 'f2',
    "The discount is the part people query, so let me take it head on. It looks like giving money "
    "away. What it actually does is let a customer choose to be early, which is cheaper for us "
    "than the borrowing we do to cover the gap. Last year we wrote off four point one million in "
    "bad debts, and we paid interest on an overdraft that exists largely because of this."),
   ('Pornthip', 'p', 'f2',
    "To bring it together. We wait more than twice as long as our terms say, the overdue balance "
    "sits with a handful of large accounts, and the sales incentive points the wrong way. We ask "
    "the committee to approve the three measures for new customers only, from January, and to let "
    "us report back in June before anything is applied to the existing accounts. Thank you."),
  ],
  'questions': [
   {'q': 'What does Pornthip say about questions during the presentation?',
    'o': ['Small points of clarification are welcome, but bigger questions should hold',
          'No questions at all until the very end',
          'All questions should go to Ying',
          'Questions should be put in writing'], 'a': 0,
    'e': u'"Do stop me if a figure is not clear, but the broader questions are best kept for the end" '
         u'· แยกคำถามสองแบบออกจากกัน ทำให้การนำเสนอไม่สะดุดแต่ผู้ฟังก็ไม่ค้างคา'},
   {'q': 'What is the single claim the presentation sets out to prove?',
    'o': ['The company is financing its customers without having chosen to',
          'The company is losing customers to competitors',
          'The credit control team is understaffed',
          'The sales team is breaking company policy'], 'a': 0,
    'e': u'"We are lending money to our customers at no charge and without ever deciding to" '
         u'· การให้เครดิตโดยไม่คิดดอกเบี้ยคือการให้กู้ และเกิดขึ้นโดยไม่มีใครตัดสินใจ'},
   {'q': 'What do the sixty-eight days tell us?',
    'o': ['Customers take well over twice the agreed period to pay',
          'Customers pay a little later than agreed',
          'The company pays its own suppliers in sixty-eight days',
          'Invoices take sixty-eight days to be issued'], 'a': 0,
    'e': u'เงื่อนไขคือ 30 วัน แต่รอจริงเฉลี่ย 68 วัน · ช่องว่างนี้คือเงินที่กิจการออกให้ลูกค้าใช้ฟรี'},
   {'q': 'What is notable about the overdue balance?',
    'o': ['A few large accounts hold the greater part of it',
          'It is spread thinly across many small accounts',
          'It consists mostly of accounts under ninety days',
          'It has arisen entirely in the last quarter'], 'a': 0,
    'e': u'ลูกค้า 11 รายคิดเป็นร้อยละ 61 ของยอดเกินกำหนด '
         u'· กระจุกตัวแบบนี้แปลว่าการแก้ที่ลูกค้าไม่กี่รายได้ผลมากกว่าการออกกฎทั้งระบบ'},
   {'q': 'Why does Decha say discipline is not the real explanation?',
    'o': ['The person granting extra time bears none of the consequence',
          'The sales team has never been told the credit terms',
          'The credit control team approves every extension',
          'Customers are not informed of the standard terms'], 'a': 0,
    'e': u'"My team is paid on orders taken, not on cash collected" '
         u'· เมื่อแรงจูงใจไม่ผูกกับเงินที่เก็บได้ พฤติกรรมที่เห็นก็เป็นผลของการวัดผล ไม่ใช่เรื่องวินัย'},
   {'q': 'What does Decha warn the committee about?',
    'o': ['A few of the biggest debtors may take their business elsewhere',
          'The sales team may resign if the rules change',
          'The proposal will need a change to the accounting system',
          'Competitors offer much longer terms'], 'a': 0,
    'e': u'"Two or three of those eleven will walk if we turn rigid overnight" '
         u'· เขาไม่ได้ใช้ความเสี่ยงนี้คัดค้าน แต่ใช้มันสนับสนุนให้เริ่มที่ลูกค้าใหม่'},
   {'q': 'What happens once an account is sixty days overdue?',
    'o': ['Deliveries halt until a credit manager authorises them',
          'The account is handed to a debt collection agency',
          'Interest is charged on the outstanding amount',
          'The customer loses the early payment discount'], 'a': 0,
    'e': u'"Supply stops automatically at sixty days overdue, and releasing it needs my signature '
         u'rather than the salesperson’s" · ย้ายอำนาจปล่อยของออกจากคนที่มีแรงจูงใจจะปล่อย'},
   {'q': 'How does Pornthip defend the early payment discount?',
    'o': ['It costs the company less than borrowing to bridge the delay',
          'It is standard practice in the industry',
          'It will be funded out of the bad debt provision',
          'Few customers are expected to take it up'], 'a': 0,
    'e': u'"which is cheaper for us than the borrowing we do to cover the gap" '
         u'· ส่วนลดดูเหมือนรายจ่าย แต่ต้องเทียบกับดอกเบี้ยเงินกู้ที่ประหยัดได้'},
   {'q': 'Who would the three measures apply to at first?',
    'o': ['Only accounts opened from January onwards',
          'All accounts from January onwards',
          'Only the eleven largest overdue accounts',
          'Only accounts outside the standard terms'], 'a': 0,
    'e': u'"approve the three measures for new customers only, from January" '
         u'· ของเดิมยังไม่แตะ และจะกลับมารายงานในเดือนมิถุนายนก่อน'},
   {'q': 'Why begin with new customers?',
    'o': ['It avoids the immediate risk of losing established accounts',
          'New customers are easier to contact',
          'The accounting system cannot yet handle old accounts',
          'New customers owe the largest amounts'], 'a': 0,
    'e': u'Decha เตือนว่าถ้าเข้มกับลูกค้าเดิมทันทีอาจเสียลูกค้าใหญ่ไปสองสามราย '
         u'· การเริ่มที่ลูกค้าใหม่จึงได้ประโยชน์โดยไม่รับความเสี่ยงนั้นทันที'},
  ]},

 {'id': 'F4b', 'kind': 'interview',
  'title': 'Interview for a Graduate Programme',
  'context': u'ผู้ดูแลโครงการบัณฑิตใหม่สัมภาษณ์ผู้สมัคร ถามว่าทำไมเลือกสำนักงานขนาดเล็ก '
             u'ขอตัวอย่างเรื่องความเห็นต่างในทีม และถามเรื่องเงินเดือนที่คาดหวัง',
  'turns': [
   ('Interviewer', 'i', 'f1',
    "Come in, please. I am Grace Lindahl and I look after the graduate programme. There are two "
    "parts this morning. I will ask you some questions for about half an hour, and then you will "
    "sit with two of last year's graduates without me in the room, which people usually find more "
    "useful than talking to me."),
   ('Teerapat', 't', 'm3',
    "Thank you. I am glad that second part exists."),
   ('Interviewer', 'i', 'f1',
    "Let us start with why us. You have applied to a firm that is smaller than most of the ones "
    "that recruit at your university."),
   ('Teerapat', 't', 'm3',
    "That was deliberate. I spent three days last year at an open event with one of the very large "
    "firms, and what I saw was impressive and also quite narrow. The graduates I met had each spent "
    "six months on one section of one client. When I spoke to your people at the careers fair, two "
    "of them described working on the whole audit of a mid-sized client in their first year. I "
    "would rather be stretched early than specialised early."),
   ('Interviewer', 'i', 'f1',
    "Thank you. Now, tell me about a time when you disagreed with somebody in a team."),
   ('Teerapat', 't', 'm3',
    "Yes. In my final-year group project, four of us had to produce a valuation of a listed "
    "property company. One member wanted to use a single growth rate for the whole forecast, "
    "because it was simpler to explain. I thought it hid the thing that mattered, which was that "
    "two of the three segments were shrinking."),
   ('Teerapat', 't', 'm3',
    "We had four days left, so there was no room for a long argument. What I did was build both "
    "versions overnight and bring them to the next meeting side by side. I did not say his method "
    "was wrong. I asked the group which of the two we could defend if the lecturer asked us where "
    "the growth came from."),
   ('Teerapat', 't', 'm3',
    "They chose the segment version, and he chose it with them, which mattered to me. He then "
    "spotted that I had the lease expiry dates wrong in one segment, which would have cost us more "
    "marks than the growth rate ever would. We submitted with his correction in it, and the piece "
    "came back with the highest mark in the cohort."),
   ('Teerapat', 't', 'm3',
    "The lesson I keep from it is that I was close to winning the argument and losing the work. If "
    "I had pushed him out of it, I would not have had his second pair of eyes."),
   ('Interviewer', 'i', 'f1',
    "Good. One practical question. What are your salary expectations?"),
   ('Teerapat', 't', 'm3',
    "I would rather be guided by you on that, if that is acceptable. I know roughly what the "
    "graduate range is in this market, and nothing I have seen suggests you sit at the bottom of "
    "it. What matters more to me at this stage is the first two years of experience, and I would "
    "not want to price myself out of a programme I have just told you I want."),
  ],
  'questions': [
   {'q': 'What is unusual about the second part of the morning?',
    'o': ['He will talk to recent graduates with no interviewer present',
          'He will sit a written test',
          'He will be shown around the office by a partner',
          'He will meet the other candidates'], 'a': 0,
    'e': u'"you will sit with two of last year’s graduates without me in the room" '
         u'· ผู้สมัครจะถามได้ตรงกว่าเมื่อไม่มีผู้สัมภาษณ์อยู่ด้วย'},
   {'q': 'Why did Teerapat choose a smaller firm?',
    'o': ['He expects wider work sooner in his career',
          'He believes the pay is better there',
          'He thought his chances of an offer were higher',
          'The office is closer to his home'], 'a': 0,
    'e': u'"I would rather be stretched early than specialised early" '
         u'· เขาอธิบายเหตุผลด้วยสิ่งที่อยากได้จากงาน ไม่ใช่ด้วยการพูดถึงข้อเสียของที่อื่นลอย ๆ'},
   {'q': 'What did he notice about the graduates at the large firm?',
    'o': ['Their work had been confined to a narrow area',
          'They had been given no training',
          'They were not planning to stay long',
          'They worked much longer hours'], 'a': 0,
    'e': u'"The graduates I met had each spent six months on one section of one client" '
         u'· หกเดือนกับงานส่วนเดียวของลูกค้ารายเดียว คือขอบเขตที่แคบ'},
   {'q': 'What was the disagreement in the group project about?',
    'o': ['Whether one rate could stand for the whole of a forecast',
          'Which company the group should value',
          'Who should present the group findings',
          'Whether the forecast period was long enough'], 'a': 0,
    'e': u'สมาชิกคนหนึ่งอยากใช้อัตราเติบโตเดียวทั้งประมาณการเพราะอธิบายง่าย '
         u'แต่ Teerapat เห็นว่าทำให้ประเด็นสำคัญหายไป คือสองในสามส่วนงานกำลังหดตัว'},
   {'q': 'How did he respond, given that only four days were left?',
    'o': ['He prepared both approaches and let the group compare them',
          'He asked the lecturer to settle the question',
          'He agreed to the simpler method to save time',
          'He divided the work so each version was submitted'], 'a': 0,
    'e': u'"build both versions overnight and bring them to the next meeting side by side" '
         u'· เมื่อเวลาน้อย การเอาหลักฐานมาวางเทียบกันเร็วกว่าการถกเถียงกันด้วยเหตุผล'},
   {'q': 'How did he frame the choice for the group?',
    'o': ['By asking which version they could justify to the marker',
          'By explaining that his own method was correct',
          'By asking the group to vote',
          'By pointing out the error in his colleague method'], 'a': 0,
    'e': u'"I asked the group which of the two we could defend if the lecturer asked us where the '
         u'growth came from" · เปลี่ยนจากการเถียงว่าใครถูก ไปเป็นเกณฑ์ที่ทุกคนยอมรับร่วมกัน'},
   {'q': 'Why did it matter that the other student chose the same version?',
    'o': ['He stayed involved and later caught a serious error',
          'He had the final say in the group',
          'He was the one who had to present it',
          'He would otherwise have reported the group'], 'a': 0,
    'e': u'"If I had pushed him out of it, I would not have had his second pair of eyes" '
         u'· การชนะแบบที่ทำให้อีกฝ่ายถอนตัว ทำให้เสียคนตรวจทานไปด้วย'},
   {'q': 'What did the other student find?',
    'o': ['Some of the lease dates were incorrect',
          'The segment figures had been added twice',
          'The discount rate was too low',
          'The company accounts were out of date'], 'a': 0,
    'e': u'"I had the lease expiry dates wrong in one segment" '
         u'· และข้อผิดพลาดนั้นจะหักคะแนนหนักกว่าเรื่องอัตราเติบโตที่เถียงกันอยู่'},
   {'q': 'What is the lesson Teerapat draws?',
    'o': ['Winning the exchange could have cost him the better result',
          'He should have raised his concern sooner',
          'Group projects should be divided more clearly',
          'He needs to explain his methods more simply'], 'a': 0,
    'e': u'"I was close to winning the argument and losing the work" '
         u'· บทเรียนที่ดีต้องเป็นสิ่งที่ผู้สมัครคิดได้เอง ไม่ใช่คำคมทั่ว ๆ ไปเรื่องการทำงานเป็นทีม'},
   {'q': 'How does he handle the question about pay?',
    'o': ['He defers to the firm while showing he has looked into the market',
          'He names a figure and says it is not negotiable',
          'He says pay does not matter to him at all',
          'He asks what the previous graduates were paid'], 'a': 0,
    'e': u'"I would rather be guided by you on that" บวกกับ "I know roughly what the graduate range '
         u'is in this market" · softening ที่ไม่เสียเปรียบ คือยอมให้อีกฝ่ายเสนอ แต่ให้รู้ว่าเราทำการบ้านมา'},
  ]},

]},

# ══════════════════════════════════ ชุดที่ 6 ══════════════════════════════════
{'id': 'F5', 'title': u'ชุดที่ 6', 'parts': [

 {'id': 'F5a', 'kind': 'presentation',
  'title': 'Explaining the Half-Year Variance to the Board',
  'context': u'ผู้ควบคุมการเงินกลุ่มกับหัวหน้าฝ่ายพาณิชย์อธิบายผลครึ่งปีที่ต่ำกว่างบประมาณ '
             u'แยกส่วนที่เป็นเรื่องจังหวะเวลาออกจากส่วนที่เป็นปัญหาจริง',
  'turns': [
   ('Anchali', 'a', 'f3',
    "Good afternoon. I am Anchali, the group financial controller, and Pisit heads our commercial "
    "team. We have ten minutes on the half-year result against budget. I will explain where the "
    "gap came from, and Pisit will explain what we are doing about the part of it that is ours to "
    "fix. I will not read the pack to you. It is in front of you, and I will point to the three "
    "lines that matter."),
   ('Anchali', 'a', 'f3',
    "The short version is that revenue is three percent below budget and that gap is almost "
    "entirely a question of timing, but the margin shortfall is not. Those are two different "
    "problems and I would like you to hold them apart."),
   ('Anchali', 'a', 'f3',
    "On revenue. One customer moved an order out of June and into July. That order is worth about "
    "nine percent of a normal month. It has been invoiced, and the cash arrived on the eleventh of "
    "July. So the revenue line for the half year is understated and the second half will carry it. "
    "I would not ask for any action on that at all."),
   ('Anchali', 'a', 'f3',
    "On margin, which is the one I would ask you to look at. Gross margin is two point four points "
    "below budget. Roughly a third of that is freight. Our outbound freight cost per tonne rose by "
    "eighteen percent over the half year, and we were buying at spot rates because the annual "
    "contract lapsed in February and was not put back in place."),
   ('Anchali', 'a', 'f3',
    "I want to be plain that the lapse was ours. Procurement sits in my division. There was no "
    "cover arranged when the contract manager left, and nobody picked it up for eleven weeks. I "
    "have changed how contract renewal dates are held, so that they belong to a role and not to a "
    "person."),
   ('Pisit', 'p', 'm2',
    "Thank you. On the rest of the margin gap, which is about two thirds of it, the cause is mix "
    "and not price. We held our list prices, and we did not discount more than we did last year. "
    "What changed is what customers bought. The lower-margin bulk grades grew, while the specialty "
    "grades were flat."),
   ('Pisit', 'p', 'm2',
    "What we are doing about it comes in two parts. The first is pricing the bulk grades separately "
    "from the specialty ones, which we should have done years ago. The second is that from the "
    "first of August we stopped paying commission on volume alone. Commission now follows "
    "contribution."),
   ('Pisit', 'p', 'm2',
    "I will not promise you that the second half closes the whole gap. The freight part should, "
    "because the contract is signed. The mix part will take longer, because it depends on what "
    "customers order, and we can influence that but we do not control it."),
  ],
  'questions': [
   {'q': 'Why does Anchali say she will not read the pack?',
    'o': ['The board has it already and she will highlight only a few lines',
          'The pack contains figures that are still being checked',
          'There is not enough time to cover all of it',
          'Pisit will take the board through it instead'], 'a': 0,
    'e': u'"It is in front of you, and I will point to the three lines that matter" '
         u'· ผู้ฟังอ่านเองได้เร็วกว่าฟังคนอ่านให้ หน้าที่ของผู้นำเสนอคือชี้ว่าบรรทัดไหนสำคัญ'},
   {'q': 'What distinction does Anchali ask the board to keep in mind?',
    'o': ['A shortfall caused by timing is not the same as one caused by trading',
          'Budget figures are not the same as forecast figures',
          'Group results are not the same as divisional results',
          'Cash is not the same as profit'], 'a': 0,
    'e': u'"Those are two different problems and I would like you to hold them apart" '
         u'· รายได้ที่เลื่อนไปอีกงวดจะกลับมาเอง แต่กำไรขั้นต้นที่หายไปไม่กลับมาเอง'},
   {'q': 'What will happen to the revenue shortfall?',
    'o': ['It will come back in the following period',
          'It will be written off',
          'It will be recovered by raising prices',
          'It will be matched by a cost saving'], 'a': 0,
    'e': u'"the revenue line for the half year is understated and the second half will carry it" '
         u'· ของที่เลื่อนออกไปงวดหน้า จะไปปรากฏในงวดหน้า'},
   {'q': 'Why was freight being bought at spot rates?',
    'o': ['An expired contract had never been replaced',
          'Freight volumes were too small for a contract',
          'The usual carrier had gone out of business',
          'Spot rates were cheaper at the start of the year'], 'a': 0,
    'e': u'"the annual contract lapsed in February and was not put back in place" '
         u'· lapse คือหมดอายุไปเองโดยไม่มีใครต่อ'},
   {'q': 'How does Anchali deal with responsibility for the lapse?',
    'o': ['She accepts that it happened inside her own division',
          'She points out that the contract manager had left',
          'She says the board was told at the time',
          'She leaves the question for Pisit to answer'], 'a': 0,
    'e': u'"I want to be plain that the lapse was ours. Procurement sits in my division" '
         u'· เธอบอกข้อเท็จจริงเรื่องคนลาออกด้วย แต่ไม่ได้ใช้มันเป็นข้ออ้าง'},
   {'q': 'What has she changed so that it does not recur?',
    'o': ['Renewal dates now belong to a post rather than an individual',
          'Procurement has been moved to another division',
          'All contracts now need board approval',
          'A deputy contract manager has been appointed'], 'a': 0,
    'e': u'"so that they belong to a role and not to a person" '
         u'· การผูกหน้าที่ไว้กับตำแหน่ง ทำให้งานไม่หายไปพร้อมคนที่ลาออก'},
   {'q': 'What caused the larger part of the margin gap?',
    'o': ['Customers moved towards the less profitable range',
          'Raw material prices rose sharply',
          'Prices were cut to hold volume',
          'Production costs rose at one factory'], 'a': 0,
    'e': u'"The lower-margin bulk grades grew, while the specialty grades were flat" '
         u'· mix หมายถึงสัดส่วนของสิ่งที่ขายได้เปลี่ยนไป ไม่ใช่ราคาเปลี่ยน'},
   {'q': 'What does Pisit explicitly rule out as a cause?',
    'o': ['Heavier discounting',
          'Higher freight costs',
          'A fall in total volume',
          'A change in the product specification'], 'a': 0,
    'e': u'"We held our list prices, and we did not discount more than we did last year" '
         u'· การตัดสาเหตุที่ผู้ฟังน่าจะคิดถึงออกไปก่อน ช่วยให้คำอธิบายที่เหลือน่าเชื่อขึ้น'},
   {'q': 'What has changed in the way the sales team is rewarded?',
    'o': ['Pay now depends on profitability instead of quantity sold',
          'Commission has been replaced by a fixed bonus',
          'Commission is now paid only once a year',
          'Commission now depends on cash collected'], 'a': 0,
    'e': u'"we stopped paying commission on volume alone. Commission now follows contribution" '
         u'· contribution คือกำไรส่วนเกิน การวัดผลจึงเลิกจ่ายตามปริมาณล้วน'},
   {'q': 'How confident is Pisit about the second half?',
    'o': ['Confident about one element and cautious about the other',
          'Confident that the whole gap will close',
          'Doubtful that any of the gap will close',
          'Unwilling to comment until the contract is signed'], 'a': 0,
    'e': u'"The freight part should, because the contract is signed. The mix part will take longer" '
         u'· แยกสิ่งที่ควบคุมได้ออกจากสิ่งที่ทำได้แค่มีอิทธิพล แล้วไม่สัญญาเกินนั้น'},
  ]},

 {'id': 'F5b', 'kind': 'interview',
  'title': 'Interview for a Tax Assistant Position',
  'context': u'หัวหน้ากลุ่มภาษีนิติบุคคลสัมภาษณ์ผู้สมัคร ขอตัวอย่างความผิดพลาดที่กระทบคนอื่น '
             u'ถามวิธีติดตามกฎที่เปลี่ยน และถามว่าทำอย่างไรเมื่องานล้นมือ',
  'turns': [
   ('Interviewer', 'i', 'm3',
    "Thank you for waiting. I am Ellis Varga and I run the corporate tax group. I have your file "
    "here. I am not going to ask you anything about your transcript, because I have read it. What I "
    "want to understand is how you work. We have about thirty-five minutes."),
   ('Praew', 'p', 'f1',
    "Thank you. That is something of a relief."),
   ('Interviewer', 'i', 'm3',
    "Tell me about a mistake you made that had consequences for somebody else."),
   ('Praew', 'p', 'f1',
    "Yes, I have one. I spent eight months as a part-time assistant at a small firm that prepared "
    "returns for about forty owner-managed businesses. One of my jobs was collecting the "
    "withholding tax certificates from clients and matching them to the amounts claimed."),
   ('Praew', 'p', 'f1',
    "For one client I ticked the schedule as complete when I had forty-one of the forty-three "
    "certificates. The two that were missing were small, and I had a note from the client saying "
    "they would follow. I treated the note as though it were the certificate. The return went in "
    "with the full amount claimed."),
   ('Praew', 'p', 'f1',
    "The revenue department queried it four months later. By then the client had changed bookkeeper "
    "and the two certificates could not be found anywhere. The firm had to amend the return, and "
    "the client lost the deduction. My supervisor told the client it was a firm error and not "
    "theirs, which I thought was decent of her, and then she sat me down."),
   ('Praew', 'p', 'f1',
    "What I did afterwards was change my own schedule. I stopped using one tick for a line and "
    "started using two marks, one for received and one for agreed to the amount. Anything carrying "
    "only the first mark had to be listed on the front page before I handed the file over. I kept "
    "doing that for the rest of my time there, and two of the other assistants took it up."),
   ('Praew', 'p', 'f1',
    "The lesson is not that I should have been more careful, because everybody says that and it "
    "changes nothing. The lesson is that my schedule let a promise and a document look the same. A "
    "form that cannot tell those two apart will catch somebody out eventually."),
   ('Interviewer', 'i', 'm3',
    "That is a good answer. How do you keep up with changes in the rules?"),
   ('Praew', 'p', 'f1',
    "Two habits, and I would not claim that either is sophisticated. I read the revenue "
    "department's announcements page on the first Monday of the month, which takes about twenty "
    "minutes and is mostly nothing. And I keep a single file of the five rules I use most often, "
    "with the date I last checked each one against the source."),
   ('Interviewer', 'i', 'm3',
    "And when you are busy and something has to give?"),
   ('Praew', 'p', 'f1',
    "I would tell whoever is waiting as early as I can, with a time I can actually meet. I would "
    "rather have an uncomfortable conversation on Tuesday than an impossible one on Friday. And if "
    "I have to choose what to drop, I would ask, rather than decide quietly and hope that nobody "
    "notices which thing I chose."),
  ],
  'questions': [
   {'q': 'Why will the interviewer not ask about her transcript?',
    'o': ['He has been through it already',
          'Transcripts are not considered at this stage',
          'Her transcript has not arrived',
          'Another interviewer will cover it'], 'a': 0,
    'e': u'"I am not going to ask you anything about your transcript, because I have read it. What I '
         u'want to understand is how you work" · เขาสนใจวิธีทำงาน ไม่ใช่ผลการเรียนที่อ่านได้เองแล้ว'},
   {'q': 'What was Praew job at the small firm?',
    'o': ['Gathering tax certificates and agreeing them to what was claimed',
          'Preparing the returns from start to finish',
          'Answering client questions about their tax',
          'Reconciling the firm own bank accounts'], 'a': 0,
    'e': u'"collecting the withholding tax certificates from clients and matching them to the '
         u'amounts claimed" · งานคือเก็บหลักฐานแล้วกระทบยอดกับจำนวนที่ขอเครดิต'},
   {'q': 'What exactly did she do wrong?',
    'o': ['She accepted an assurance in place of the evidence',
          'She added up the certificates incorrectly',
          'She filed the return after the deadline',
          'She claimed an amount the client had not asked for'], 'a': 0,
    'e': u'"I treated the note as though it were the certificate" '
         u'· คำรับรองว่าจะส่งตามมา ไม่ใช่หลักฐานที่ขอเครดิตได้'},
   {'q': 'What was the consequence for the client?',
    'o': ['A tax deduction had to be surrendered',
          'A penalty was charged by the revenue department',
          'The client had to change bookkeeper',
          'The client was charged an extra fee by the firm'], 'a': 0,
    'e': u'"The firm had to amend the return, and the client lost the deduction" '
         u'· แก้แบบแล้วเครดิตที่ขอไว้ก็ต้องตัดออก'},
   {'q': 'What did her supervisor do before speaking to Praew?',
    'o': ['She took the blame on the firm behalf',
          'She asked the client to look again for the certificates',
          'She reported the matter to the revenue department',
          'She reviewed every other file Praew had worked on'], 'a': 0,
    'e': u'"My supervisor told the client it was a firm error and not theirs" '
         u'· รับผิดในนามสำนักงานก่อน แล้วค่อยคุยกับผู้ช่วยเป็นการภายใน'},
   {'q': 'What change did Praew make to her own working paper?',
    'o': ['She separated proof of receipt from agreement of the amount',
          'She started keeping copies of every certificate',
          'She asked a second person to review each schedule',
          'She stopped signing schedules altogether'], 'a': 0,
    'e': u'"two marks, one for received and one for agreed to the amount" '
         u'· แยกสองสิ่งที่เดิมใช้เครื่องหมายเดียวกัน ความคลุมเครือจึงหมดไป'},
   {'q': 'Why does she reject “I should have been more careful” as the lesson?',
    'o': ['It is advice that changes nothing about how the work is done',
          'The error was not really hers',
          'She had already been as careful as possible',
          'Her supervisor told her not to say it'], 'a': 0,
    'e': u'"because everybody says that and it changes nothing" '
         u'· บทเรียนที่ใช้ได้ต้องแก้ที่ระบบงาน ไม่ใช่การตั้งใจให้มากขึ้น'},
   {'q': 'What is her routine for keeping up with the rules?',
    'o': ['A short monthly check of announcements plus a dated list of the rules she uses',
          'A weekly meeting with her supervisor',
          'A subscription to a professional update service',
          'An annual training course'], 'a': 0,
    'e': u'อ่านประกาศทุกวันจันทร์แรกของเดือนราวยี่สิบนาที และเก็บแฟ้มกฎห้าข้อที่ใช้บ่อย '
         u'พร้อมวันที่ตรวจทานล่าสุดของแต่ละข้อ'},
   {'q': 'What does she do when she cannot meet a deadline?',
    'o': ['Warns the other person early and offers a date she can keep',
          'Works late until the task is finished',
          'Finishes the task and explains afterwards',
          'Passes the task to a colleague'], 'a': 0,
    'e': u'"I would rather have an uncomfortable conversation on Tuesday than an impossible one on '
         u'Friday" · บอกเร็วพร้อมกำหนดใหม่ที่ทำได้จริง'},
   {'q': 'What does she say about deciding which work to drop?',
    'o': ['She would raise it rather than make the choice silently',
          'She would always drop the smallest task',
          'She would leave the decision until the last moment',
          'She would drop whatever the client notices least'], 'a': 0,
    'e': u'"I would ask, rather than decide quietly and hope that nobody notices which thing I chose" '
         u'· การเลือกเองเงียบ ๆ ย้ายความเสี่ยงไปให้หัวหน้าโดยที่หัวหน้าไม่รู้ตัว'},
  ]},

]},

# ══════════════════════════════════ ชุดที่ 7 ══════════════════════════════════
{'id': 'F6', 'title': u'ชุดที่ 7', 'parts': [

 {'id': 'F6a', 'kind': 'presentation',
  'title': 'Results of a Remote Working Pilot',
  'context': u'ฝ่ายบุคคล ฝ่ายปฏิบัติการ และฝ่ายบริการผู้ใช้ รายงานผลการทดลองทำงานจากบ้านสามเดือน '
             u'โดยยังไม่ขอให้ตัดสินใจ แต่ขอให้บอกว่าต้องการให้วัดอะไรเพิ่ม',
  'turns': [
   ('Siriporn', 's', 'f1',
    "Good morning. I am Siriporn from human resources. Wasan is here from operations and Nid from "
    "the service desk. Our subject is the three-month remote working pilot that ended in "
    "September. We have twelve minutes, and we are not asking you to decide anything today. We are "
    "asking you to tell us what else you want measured before you do."),
   ('Siriporn', 's', 'f1',
    "The headline is that the pilot worked for individuals and did not work for handovers. I will "
    "give you the staff response, Wasan will give you the operational effect, and Nid will tell "
    "you what it did to the service desk, which is the part we did not predict."),
   ('Siriporn', 's', 'f1',
    "Forty-six people took part, across four departments. We surveyed them twice, in July and "
    "again in September, and we had forty-one replies out of forty-six. Seventy-one percent said "
    "their ability to concentrate improved. The same survey asked whether they felt informed about "
    "what their colleagues were doing, and that answer fell between the July round and the "
    "September round."),
   ('Wasan', 'w', 'm2',
    "On the operational side, output held up wherever the work belongs to one person. Our monthly "
    "close was on time in all three months, and the reconciliation backlog actually came down. "
    "Where it did not hold up was any task that passes between two people. We missed the "
    "goods-received handover twice in August, both times on a Friday, and both times because each "
    "person believed the other one had it."),
   ('Wasan', 'w', 'm2',
    "I would not quite call that a remote working problem. The handover was always fragile. Being "
    "in the same room was covering for a procedure that had never been written down. The pilot did "
    "not break it. The pilot showed us that it was broken."),
   ('Nid', 'n', 'f2',
    "The service desk is where the cost landed. Tickets rose by about thirty percent in the first "
    "six weeks. Most of them were not technical faults at all. They were people asking where a "
    "document was, or who had a file open. That tells you the difficulty was access to "
    "information, not the laptops."),
   ('Nid', 'n', 'f2',
    "It settled down after we published a single index of where things live. By the last month, "
    "tickets were a little above the level before the pilot, not thirty percent above. I would "
    "want you to know that the first six weeks are not what a permanent arrangement would look "
    "like."),
   ('Siriporn', 's', 'f1',
    "So, to draw it together. People concentrated better and felt less connected. Individual work "
    "held and shared work did not, and the weakness lay in procedures rather than in the "
    "equipment. The service desk cost was real but temporary. What we would like from you this "
    "morning is what else you want measured before the decision in December, and in particular "
    "whether you want new joiners looked at separately, because none of the forty-six had been "
    "here less than two years."),
  ],
  'questions': [
   {'q': 'What is the team asking of the board today?',
    'o': ['Guidance on what further evidence it wants before deciding',
          'Approval to make the arrangement permanent',
          'Approval to extend the pilot by three months',
          'A decision on whether to buy more laptops'], 'a': 0,
    'e': u'"we are not asking you to decide anything today. We are asking you to tell us what else '
         u'you want measured" · การรายงานกลางทางที่ขอความเห็นเรื่องเกณฑ์ ก่อนจะถึงการตัดสินใจจริง'},
   {'q': 'What is the headline finding?',
    'o': ['It suited work done alone but exposed weaknesses where work is passed on',
          'It suited every kind of work tested',
          'It reduced costs but lowered output',
          'It was too short to show anything'], 'a': 0,
    'e': u'"the pilot worked for individuals and did not work for handovers" '
         u'· วางข้อสรุปทั้งสองด้านไว้ตั้งแต่ต้น ผู้ฟังจึงรู้ว่าจะได้ฟังทั้งข้อดีและข้อเสีย'},
   {'q': 'What changed between the July and September surveys?',
    'o': ['Staff felt less aware of what their colleagues were doing',
          'Fewer staff replied to the survey',
          'Staff reported more difficulty concentrating',
          'More staff asked to return to the office'], 'a': 0,
    'e': u'คำถามเรื่องการรู้ว่าเพื่อนร่วมงานทำอะไร ได้คำตอบลดลงจากรอบกรกฎาคมมาถึงรอบกันยายน '
         u'· สมาธิดีขึ้นแต่ความเชื่อมโยงกับทีมแย่ลง สองอย่างนี้เกิดพร้อมกันได้'},
   {'q': 'Which kind of work held up during the pilot?',
    'o': ['Tasks that a single person finishes without passing on',
          'Tasks involving contact with customers',
          'Tasks that needed the factory systems',
          'Tasks carried out by the newest staff'], 'a': 0,
    'e': u'"output held up wherever the work belongs to one person" '
         u'· งานที่จบในมือคนเดียวไม่ต้องพึ่งการส่งต่อ จึงไม่กระทบ'},
   {'q': 'What does Wasan conclude about the missed handover?',
    'o': ['The weakness existed beforehand and had been hidden by working side by side',
          'It was caused by the laptops failing on a Friday',
          'It shows remote working cannot be used in operations',
          'It was the fault of one member of staff'], 'a': 0,
    'e': u'"The pilot did not break it. The pilot showed us that it was broken" '
         u'· ขั้นตอนที่ไม่เคยเขียนไว้เคยรอดมาได้เพราะนั่งอยู่ห้องเดียวกัน'},
   {'q': 'What were most of the extra service desk tickets about?',
    'o': ['Locating information rather than faulty equipment',
          'Setting up the laptops at home',
          'Problems with the internet connection',
          'Requests for extra software licences'], 'a': 0,
    'e': u'"They were people asking where a document was, or who had a file open" '
         u'· ปัญหาอยู่ที่การเข้าถึงข้อมูล ไม่ใช่ที่ตัวเครื่อง'},
   {'q': 'What brought the number of tickets down?',
    'o': ['Publishing one place that said where everything was kept',
          'Adding staff to the service desk',
          'Replacing the laptops',
          'Bringing two departments back to the office'], 'a': 0,
    'e': u'"after we published a single index of where things live" '
         u'· แก้ที่สาเหตุคือคนหาของไม่เจอ ไม่ได้แก้ด้วยการเพิ่มคนรับเรื่อง'},
   {'q': 'Why does Nid mention the figure for the last month?',
    'o': ['To show that the early rise was not a permanent level',
          'To show that the problem is still getting worse',
          'To argue that the service desk needs more budget',
          'To show that the index made no difference'], 'a': 0,
    'e': u'"the first six weeks are not what a permanent arrangement would look like" '
         u'· ต้นทุนช่วงเปลี่ยนผ่านกับต้นทุนในภาวะปกติเป็นของต่างกัน'},
   {'q': 'Where does Siriporn locate the cause of the shared-work failure?',
    'o': ['In undocumented working practices rather than in the equipment',
          'In the attitude of the staff involved',
          'In the choice of departments for the pilot',
          'In the length of the pilot'], 'a': 0,
    'e': u'"the weakness lay in procedures rather than in the equipment" '
         u'· ซึ่งตรงกับที่ Wasan เล่าว่าขั้นตอนการส่งต่อไม่เคยถูกเขียนไว้'},
   {'q': 'What limitation of the pilot group does Siriporn raise herself?',
    'o': ['Nobody taking part was recent to the organisation',
          'Only one department took part',
          'Fewer than half the staff replied',
          'The pilot ran over a holiday period'], 'a': 0,
    'e': u'"none of the forty-six had been here less than two years" '
         u'· คนที่เพิ่งเข้ามาต้องเรียนงานจากคนอื่น ผลที่ได้จากกลุ่มนี้จึงใช้แทนกันไม่ได้'},
  ]},

 {'id': 'F6b', 'kind': 'interview',
  'title': 'Interview for an Accounting Trainee at a Manufacturer',
  'context': u'ผู้จัดการฝ่ายการเงินของโรงงานสัมภาษณ์ผู้สมัครตำแหน่งผู้ช่วยนักบัญชีฝึกหัด '
             u'ขอตัวอย่างสิ่งที่ลองทำแล้วไม่สำเร็จ และถามว่าถนัดอะไร',
  'turns': [
   ('Interviewer', 'i', 'm1',
    "Do sit down. I am Arthit Boonmee, the finance manager here. This is a smaller operation than "
    "the firms most graduates look at, so I will be honest with you about what the job is, and "
    "then I would like to hear whether it is what you want. There are three of us in finance and "
    "one factory. You would see everything, and you would also do a fair amount of work that "
    "nobody enjoys."),
   ('Nalin', 'n', 'f3',
    "Thank you for saying so."),
   ('Interviewer', 'i', 'm1',
    "Tell me about something you tried that did not work."),
   ('Nalin', 'n', 'f3',
    "I will take one from outside my studies, if that is all right. I ran the accounts for a "
    "student society in my second year, and I decided we should move from cash to bank transfer "
    "for member payments. The reason was a good one. We were holding four or five thousand baht in "
    "a tin, and I could not reconcile it properly."),
   ('Nalin', 'n', 'f3',
    "What I did badly was the order of things. I announced the change two weeks before our main "
    "event, I did not tell the two people who collected money at the door, and I did not think "
    "about members who have no smartphone. On the night we had a queue, two people taking cash "
    "anyway because that is what they had always done, and a set of transfers with no names "
    "attached to them."),
   ('Nalin', 'n', 'f3',
    "It took me three evenings to work out who had paid. I got there in the end, but the "
    "reconciliation was worse than the one I had set out to fix. The president asked me, quite "
    "reasonably, why I had not told her what I was planning."),
   ('Nalin', 'n', 'f3',
    "What I did next is the part I would want you to judge me on. I did not drop the idea, because "
    "the idea was right. I wrote down who was affected, spoke to the two collectors first, kept "
    "cash as an option, and asked people to put their student number in the transfer reference. We "
    "ran it again at the next event and the reconciliation took twenty minutes."),
   ('Nalin', 'n', 'f3',
    "What I learned is that I am quite good at seeing what should change, and I was poor at asking "
    "who it lands on. I now make myself list the people a change touches before I announce it, and "
    "I speak to the ones who have to do the work first."),
   ('Interviewer', 'i', 'm1',
    "Useful, thank you. And what would you say you are good at?"),
   ('Nalin', 'n', 'f3',
    "I would say I am patient with detail that other people find tedious. I did a semester of bank "
    "reconciliations for a tutor's consultancy, around six hundred lines a month, and I did not "
    "mind it. I am aware that saying I enjoy routine work in an interview sounds convenient, so "
    "the honest version is this. I do not enjoy it, but it does not wear me down, and I have "
    "noticed that this is not true of everybody."),
  ],
  'questions': [
   {'q': 'What does the interviewer make clear at the start?',
    'o': ['What the job actually involves, including its least attractive parts',
          'That several other candidates are stronger',
          'That the position may not be filled this year',
          'That he has not yet read her application'], 'a': 0,
    'e': u'"you would also do a fair amount of work that nobody enjoys" '
         u'· ผู้สัมภาษณ์ที่บอกข้อเสียของงานตั้งแต่ต้น ช่วยให้ทั้งสองฝ่ายไม่เสียเวลา'},
   {'q': 'Why did Nalin want to change the way members paid?',
    'o': ['The cash on hand could not be reconciled properly',
          'Members had complained about paying cash',
          'The society had been asked to by the university',
          'Cash had gone missing from the tin'], 'a': 0,
    'e': u'"We were holding four or five thousand baht in a tin, and I could not reconcile it '
         u'properly" · เหตุผลตั้งต้นถูกต้อง ปัญหาอยู่ที่วิธีนำไปใช้'},
   {'q': 'What does she say she got wrong?',
    'o': ['The sequence in which she introduced the change',
          'The choice of payment method',
          'The amount she asked members to pay',
          'The record she kept of the cash'], 'a': 0,
    'e': u'"What I did badly was the order of things" '
         u'· ความคิดถูก แต่ลำดับการทำผิด ซึ่งเป็นการวินิจฉัยตัวเองที่คมกว่าการบอกว่าทำพลาด'},
   {'q': 'Which people had she failed to consider?',
    'o': ['Those taking the money, and those with no smartphone',
          'The society president and the treasurer',
          'Members who had already paid for the year',
          'The bank and the university finance office'], 'a': 0,
    'e': u'"I did not tell the two people who collected money at the door, and I did not think '
         u'about members who have no smartphone"'},
   {'q': 'What happened on the night of the event?',
    'o': ['A slow queue formed and some payments could not be identified',
          'Nobody was able to pay at all',
          'The bank transfer system stopped working',
          'More members attended than expected'], 'a': 0,
    'e': u'"we had a queue, two people taking cash anyway…and a set of transfers with no names '
         u'attached to them" · โอนเข้ามาแต่ไม่รู้ว่าใครโอน จึงระบุตัวไม่ได้'},
   {'q': 'How did the result compare with the problem she set out to solve?',
    'o': ['It made that problem worse for a time',
          'It solved the problem but created a new one',
          'It left the problem exactly as it was',
          'It solved the problem sooner than expected'], 'a': 0,
    'e': u'"the reconciliation was worse than the one I had set out to fix" '
         u'· งานกระทบยอดที่อยากให้ง่ายขึ้น กลับยากกว่าเดิมในรอบนั้น'},
   {'q': 'What did she do differently the second time?',
    'o': ['She consulted the people affected and left the old method available',
          'She asked the president to announce the change',
          'She made the change compulsory for everybody',
          'She waited until the end of the academic year'], 'a': 0,
    'e': u'"spoke to the two collectors first, kept cash as an option, and asked people to put '
         u'their student number in the transfer reference" · แก้ทั้งเรื่องคนและเรื่องข้อมูลอ้างอิง'},
   {'q': 'What does she name as her real shortcoming?',
    'o': ['Not thinking about who a change lands on',
          'Not being able to reconcile accurately',
          'Taking too long to make decisions',
          'Being unwilling to abandon her own ideas'], 'a': 0,
    'e': u'"I am quite good at seeing what should change, and I was poor at asking who it lands on" '
         u'· วางจุดแข็งกับจุดอ่อนไว้คู่กันในประโยคเดียว'},
   {'q': 'What does she now do before announcing a change?',
    'o': ['Notes down everybody it affects and talks to those who must carry it out',
          'Asks permission from the person in charge',
          'Tests the change on a small group first',
          'Writes a procedure for the new method'], 'a': 0,
    'e': u'"list the people a change touches before I announce it, and I speak to the ones who have '
         u'to do the work first" · เปลี่ยนบทเรียนให้เป็นขั้นตอนที่ทำซ้ำได้'},
   {'q': 'How does she describe her tolerance for routine work?',
    'o': ['It does not wear her out, although she does not claim to enjoy it',
          'She finds it genuinely enjoyable',
          'She can manage it for short periods only',
          'She prefers it to work that involves other people'], 'a': 0,
    'e': u'"I do not enjoy it, but it does not wear me down" '
         u'· เธอรู้ว่าการบอกว่าชอบงานซ้ำ ๆ ในห้องสัมภาษณ์ฟังดูเอาใจ จึงเลือกตอบแบบที่ตรวจสอบได้จริง'},
  ]},

]},

# ══════════════════════════════════ ชุดที่ 8 ══════════════════════════════════
{'id': 'F7', 'title': u'ชุดที่ 8', 'parts': [

 {'id': 'F7a', 'kind': 'presentation',
  'title': 'Changing the Way Stock Is Counted',
  'context': u'ผู้ควบคุมการเงิน หัวหน้าคลังสินค้า และผู้จัดการตรวจสอบภายใน '
             u'เสนอให้เลิกปิดคลังนับสต๊อกปลายปี แล้วเปลี่ยนไปนับหมุนเวียนตลอดปี',
  'turns': [
   ('Kanya', 'k', 'f2',
    "Good morning. I am Kanya, the financial controller. Somchai runs the warehouse and Lek is our "
    "internal audit manager. We have fifteen minutes on how we count stock. Our recommendation "
    "needs a decision from you before the end of November, because whichever method we choose has "
    "to be agreed with the external auditors in December."),
   ('Kanya', 'k', 'f2',
    "Our recommendation is that we stop closing the warehouse for two days in December and count "
    "continuously through the year instead. The reason is not the cost of those two days. It is "
    "that the December count has stopped telling us anything we did not already know."),
   ('Somchai', 's', 'm3',
    "Let me explain what the two days actually involve. We shut on the twenty-eighth and "
    "twenty-ninth of December. Forty-two people count, of whom about thirty are borrowed from "
    "other departments and have not counted since the year before. We turn away deliveries for two "
    "days, and we hold about eleven million baht of orders that would otherwise have shipped."),
   ('Somchai', 's', 'm3',
    "And the quality is not what you would hope for. Last December we recounted one hundred and "
    "forty locations because the first count and the second count disagreed. That is a quarter of "
    "the warehouse counted three times. Most of what we found was not a stock difference at all. "
    "It was people getting the count wrong because they do it once a year."),
   ('Lek', 'l', 'f1',
    "From the audit side, the question is whether a different method gives the auditors what they "
    "need. It can, but only on two conditions, and I want to be clear about both. The first is "
    "that every location is counted at least twice in the year, and that the second count is not "
    "announced. The second is that the differences are investigated and cleared within the same "
    "month. If we let them accumulate, we end up with a number nobody will sign."),
   ('Lek', 'l', 'f1',
    "I have spoken to the audit partner informally. Her view was that the method is acceptable in "
    "principle, and that she would want to attend some of our counts during the year rather than "
    "only in December. That is not a difficulty for us. It is arguably better."),
   ('Kanya', 'k', 'f2',
    "The cost side is straightforward. Continuous counting needs two people full time rather than "
    "forty-two for two days, and it uses the handheld terminals we have already bought for "
    "picking. What it also needs, and I would not want to understate this, is discipline every "
    "single week. The December count forgives a bad November. Continuous counting does not."),
   ('Kanya', 'k', 'f2',
    "So, to summarise. The December shutdown costs us two days of shipping, it is done largely by "
    "people who do not count often, and a quarter of it had to be done twice. The alternative "
    "satisfies the auditors on two conditions we can meet, and it costs less in total. What we ask "
    "of you today is approval in principle, so that Lek can take the written proposal to the "
    "external auditors next week."),
  ],
  'questions': [
   {'q': 'Why must the committee decide before the end of November?',
    'o': ['The method has to be settled with the external auditors in December',
          'The warehouse lease expires in December',
          'The handheld terminals must be ordered in November',
          'The borrowed staff must be booked in advance'], 'a': 0,
    'e': u'"whichever method we choose has to be agreed with the external auditors in December" '
         u'· การบอกเส้นตายและเหตุผลของเส้นตายไว้ตั้งแต่ต้น ทำให้ผู้ฟังรู้ว่าทำไมต้องตัดสินวันนี้'},
   {'q': 'What is the main reason for the recommendation?',
    'o': ['The December count no longer produces new information',
          'The two days of closure are too expensive',
          'The external auditors have asked for a change',
          'The warehouse has grown too large to count in two days'], 'a': 0,
    'e': u'"The reason is not the cost of those two days. It is that the December count has stopped '
         u'telling us anything we did not already know" · เธอตัดเหตุผลที่คนมักเดาออกไปก่อนด้วย'},
   {'q': 'What is the cost of the shutdown that does not appear as an expense?',
    'o': ['Orders that could not be despatched during the closure',
          'Overtime paid to the borrowed staff',
          'The cost of recounting disputed locations',
          'Interest on the stock held in the warehouse'], 'a': 0,
    'e': u'"we hold about eleven million baht of orders that would otherwise have shipped" '
         u'· รายได้ที่เลื่อนออกไปไม่ปรากฏเป็นค่าใช้จ่ายในบัญชี แต่เป็นต้นทุนจริงของการปิดคลัง'},
   {'q': 'Who does most of the counting in December?',
    'o': ['People brought in from other departments who seldom do it',
          'The two full-time stock controllers',
          'Staff from the external audit firm',
          'The warehouse picking team'], 'a': 0,
    'e': u'"about thirty are borrowed from other departments and have not counted since the year '
         u'before" · สามสิบจากสี่สิบสองคนเป็นคนยืมมาและไม่ได้นับมาตลอดปี'},
   {'q': 'What caused most of the differences found in the recount?',
    'o': ['Mistakes by inexperienced counters rather than stock that was missing',
          'Stock recorded in the wrong location',
          'Deliveries received during the count',
          'Errors in the stock recording system'], 'a': 0,
    'e': u'"It was people getting the count wrong because they do it once a year" '
         u'· นับผิดไม่ใช่ของหาย ซึ่งหมายความว่าการนับปีละครั้งกำลังสร้างงานเพิ่มโดยไม่ได้ข้อมูลที่ดีขึ้น'},
   {'q': 'What is the first condition Lek sets for the new method?',
    'o': ['Each location must have a second count given without warning',
          'Each location must be counted once every month',
          'Internal audit must attend every count',
          'The warehouse must close for one day a quarter'], 'a': 0,
    'e': u'"every location is counted at least twice in the year, and that the second count is not '
         u'announced" · การนับรอบสองที่ไม่บอกล่วงหน้า ทำให้ไม่มีใครเตรียมตัวรับการตรวจ'},
   {'q': 'Why must differences be cleared within the month?',
    'o': ['A build-up would leave a figure nobody is willing to certify',
          'The accounting system closes each month permanently',
          'The external auditors require monthly reporting',
          'Staff would forget what they had counted'], 'a': 0,
    'e': u'"If we let them accumulate, we end up with a number nobody will sign" '
         u'· ส่วนที่ไม่ตรงกันซึ่งค้างสะสมไว้ จะอธิบายไม่ได้ในที่สุด ไม่ว่าจะมีเวลาเท่าไร'},
   {'q': 'What did the audit partner want in return?',
    'o': ['To observe counts spread across the year',
          'A written undertaking from the committee',
          'A higher audit fee',
          'To approve each count in advance'], 'a': 0,
    'e': u'"she would want to attend some of our counts during the year rather than only in '
         u'December" · และ Lek บอกว่านั่นไม่ใช่ปัญหา กลับเป็นผลดีกับกิจการเอง'},
   {'q': 'What does Kanya say the new method demands that the old one does not?',
    'o': ['Consistent attention in every week of the year',
          'More expensive counting equipment',
          'More staff in the warehouse overall',
          'Approval from the committee each quarter'], 'a': 0,
    'e': u'"The December count forgives a bad November. Continuous counting does not" '
         u'· การนับปลายปีกลบความหละหลวมระหว่างปีได้ แต่การนับหมุนเวียนกลบไม่ได้'},
   {'q': 'What are they asking the committee for today?',
    'o': ['Agreement in principle so that the proposal can be put to the auditors',
          'Authority to buy new handheld terminals',
          'A final decision on the counting method',
          'Permission to recruit two stock controllers'], 'a': 0,
    'e': u'"approval in principle, so that Lek can take the written proposal to the external '
         u'auditors next week" · ยังไม่ใช่การตัดสินขั้นสุดท้าย เป็นไฟเขียวให้ไปคุยกับผู้สอบบัญชี'},
  ]},

 {'id': 'F7b', 'kind': 'interview',
  'title': 'Interview for a Commercial Finance Analyst',
  'context': u'ผู้จัดการฝ่ายการเงินเชิงพาณิชย์ของกิจการค้าปลีกสัมภาษณ์ผู้สมัครที่ศูนย์กระจายสินค้า '
             u'ถามเรื่องการอธิบายตัวเลขให้คนที่ไม่ใช่นักบัญชี และเรื่องการรับมือกับคำถามที่ตอบไม่ได้',
  'turns': [
   ('Interviewer', 'i', 'f2',
    "Thank you for coming out to the distribution centre rather than to the head office. I am Mei "
    "Lau and I manage the commercial finance team. I wanted you to see where the work actually "
    "lands. Half of what we do is explaining numbers to people who run shops, and they are not "
    "accountants. We have forty minutes."),
   ('Chaiyaporn', 'c', 'm1',
    "Thank you. I am glad to see it."),
   ('Interviewer', 'i', 'f2',
    "Tell me about a time when you had to explain something financial to somebody without a "
    "finance background."),
   ('Chaiyaporn', 'c', 'm1',
    "Yes. I volunteered for two years with a community kitchen that serves about three hundred "
    "meals a week. The committee were all volunteers, mostly retired, and none of them had worked "
    "with accounts. They asked me to explain why the kitchen was short of money when donations had "
    "gone up."),
   ('Chaiyaporn', 'c', 'm1',
    "The answer was that donations had risen by about twelve percent while the cost of the food had "
    "risen by nearly thirty, and that the difference was being covered out of a reserve with about "
    "seven months left in it. If I had said it in those words, I would have lost them in the first "
    "sentence."),
   ('Chaiyaporn', 'c', 'm1',
    "What I did instead was bring one sheet of paper with two lines drawn on it, one for money "
    "coming in and one for money going out, over three years. I put no figures on it at first. I "
    "asked them to tell me what they thought was happening, and one of them said straight away "
    "that the two lines were going to cross. That was the whole message."),
   ('Chaiyaporn', 'c', 'm1',
    "Then I put the numbers on, and then I told them about the seven months, because by that point "
    "they were asking for it rather than being told. They voted that evening to raise the suggested "
    "donation, which they had refused to discuss twice before."),
   ('Chaiyaporn', 'c', 'm1',
    "What I learned is that the order matters more than the detail. They did not need less "
    "information. They needed the shape before the figures."),
   ('Interviewer', 'i', 'f2',
    "That is exactly the job. Now, a harder one. What do you do when somebody asks you something "
    "and you do not know the answer?"),
   ('Chaiyaporn', 'c', 'm1',
    "I say so. I would rather say I do not know and come back in an hour than guess and be "
    "remembered for it. What I try to add is a time and a route. So, not simply I do not know, but "
    "I do not know, I will look at the supplier file this afternoon, and I will tell you by five "
    "whether the answer is in there or whether we have to ask the supplier."),
   ('Chaiyaporn', 'c', 'm1',
    "I will admit that this was learned rather than natural. In my first internship I answered a "
    "question about a stock balance from memory and I was out by a factor of ten. Nobody acted on "
    "it, fortunately, but my supervisor pointed out that she now had to check everything else I had "
    "told her that week. That stayed with me."),
  ],
  'questions': [
   {'q': 'Why did Mei hold the interview at the distribution centre?',
    'o': ['So that he could see the setting the work serves',
          'Because the head office was being refurbished',
          'Because the rest of the team is based there',
          'So that he could meet the shop managers'], 'a': 0,
    'e': u'"I wanted you to see where the work actually lands" '
         u'· เธออยากให้ผู้สมัครเห็นปลายทางของงาน ไม่ใช่แค่โต๊ะทำงาน'},
   {'q': 'What does Mei say half of the team work consists of?',
    'o': ['Making figures understandable to people outside finance',
          'Preparing the monthly management accounts',
          'Negotiating with suppliers',
          'Checking the accuracy of shop records'], 'a': 0,
    'e': u'"explaining numbers to people who run shops, and they are not accountants" '
         u'· ทักษะการสื่อสารจึงไม่ใช่ของแถม แต่เป็นครึ่งหนึ่งของเนื้องาน'},
   {'q': 'Why was the kitchen short of money?',
    'o': ['Its costs had climbed much faster than its income',
          'Donations had fallen during the year',
          'It was serving more meals than it could fund',
          'A large donor had withdrawn'], 'a': 0,
    'e': u'เงินบริจาคเพิ่มราวร้อยละสิบสอง แต่ต้นทุนอาหารเพิ่มเกือบร้อยละสามสิบ '
         u'· รายรับเพิ่มก็จริง แต่เพิ่มช้ากว่ารายจ่ายมาก'},
   {'q': 'What was the position of the reserve?',
    'o': ['It would run out in well under a year at that rate',
          'It had already been fully used',
          'It could cover the gap for several more years',
          'It was restricted and could not be used'], 'a': 0,
    'e': u'"a reserve with about seven months left in it" · เจ็ดเดือนคือไม่ถึงหนึ่งปี'},
   {'q': 'Why did he not simply state those figures?',
    'o': ['He judged that the committee would stop following him',
          'He did not have the figures with him',
          'The committee had asked for a written report instead',
          'The figures were not yet confirmed'], 'a': 0,
    'e': u'"If I had said it in those words, I would have lost them in the first sentence" '
         u'· ผู้ฟังที่หลุดไปในประโยคแรก จะไม่ได้ยินอะไรที่ตามมาเลย'},
   {'q': 'What did he bring to the meeting instead?',
    'o': ['A single drawing with no figures on it to start with',
          'A full set of accounts for three years',
          'A written recommendation',
          'A spreadsheet projected on a screen'], 'a': 0,
    'e': u'"one sheet of paper with two lines drawn on it…I put no figures on it at first" '
         u'· เอารูปทรงของปัญหาขึ้นก่อน แล้วค่อยเติมตัวเลข'},
   {'q': 'Why did he ask the committee what they could see?',
    'o': ['So that the finding came from them rather than from him',
          'Because he was not sure of his own reading',
          'To check whether they had understood the drawing',
          'Because the chair had asked him to'], 'a': 0,
    'e': u'"one of them said straight away that the two lines were going to cross" '
         u'· ข้อสรุปที่ผู้ฟังพูดออกมาเอง หนักกว่าข้อสรุปที่เราบอกเขา'},
   {'q': 'What did the committee then do?',
    'o': ['They approved an increase they had twice declined to consider',
          'They asked for a second opinion',
          'They decided to reduce the number of meals',
          'They launched a fundraising campaign'], 'a': 0,
    'e': u'"They voted that evening to raise the suggested donation, which they had refused to '
         u'discuss twice before" · เรื่องเดิมที่ไม่ยอมแม้จะคุย กลับผ่านในคืนเดียว'},
   {'q': 'What does Chaiyaporn add when he does not know an answer?',
    'o': ['A time by which he will reply and how he will find out',
          'An apology and an explanation of why he does not know',
          'A guess, clearly marked as a guess',
          'The name of a colleague who may know'], 'a': 0,
    'e': u'"What I try to add is a time and a route" '
         u'· ไม่รู้เฉย ๆ ทำให้คนที่ถามไปต่อไม่ได้ แต่ไม่รู้พร้อมกำหนดเวลาและวิธีหา ทำให้เขาวางแผนได้'},
   {'q': 'What did his internship mistake cost his supervisor?',
    'o': ['She had to go back over his other work from that week',
          'She had to apologise to a supplier',
          'She lost a bonus for the quarter',
          'She had to recount the stock herself'], 'a': 0,
    'e': u'"she now had to check everything else I had told her that week" '
         u'· การเดาครั้งเดียวทำให้ทุกอย่างที่เราพูดถูกตั้งคำถามไปด้วย'},
  ]},

]},

# ══════════════════════════════════ ชุดที่ 9 ══════════════════════════════════
{'id': 'F8', 'title': u'ชุดที่ 9', 'parts': [

 {'id': 'F8a', 'kind': 'presentation',
  'title': 'Reporting a Purchasing Review to the Audit Committee',
  'context': u'หัวหน้าตรวจสอบภายใน ผู้ทำงานตรวจ และฝ่ายกฎหมาย '
             u'รายงานผลการสอบทานงานจัดซื้อที่โรงงานแห่งหนึ่งต่อคณะกรรมการตรวจสอบ',
  'turns': [
   ('Pradit', 'p', 'm1',
    "Good afternoon. I am Pradit, head of internal audit. Oraphan led the fieldwork and Suriya is "
    "from our group legal team. We have twenty minutes, and we are presenting the findings of the "
    "review of purchasing at the Rayong plant. Legal have asked us to keep two names out of this "
    "room until the employment process finishes, and the committee secretary holds the full "
    "report."),
   ('Pradit', 'p', 'm1',
    "Let me give you the conclusion. The control that failed was not the approval limit. It was "
    "that the same person could create a supplier and approve a payment to it. Everything else in "
    "this report follows from that one gap."),
   ('Oraphan', 'o', 'f3',
    "Here is what we did. We took every supplier created in the last three years, which was two "
    "thousand one hundred and six, and we matched the creation record against the payment approval "
    "record. We were looking for cases where the two were the same person. There were nineteen."),
   ('Oraphan', 'o', 'f3',
    "Of the nineteen, fifteen were explained within a day. They were cases where a purchasing "
    "officer set up a supplier and later approved a small payment under the routine limit, which "
    "the system allows and which we had never treated as a problem. Four were not explained, and "
    "all four involved one supplier set up in March of last year."),
   ('Oraphan', 'o', 'f3',
    "That supplier received eleven payments totalling just under two million baht, for maintenance "
    "services at a site that had been closed since the year before. There are no work records, "
    "there is no contract, and the bank account it was paid into had been opened two weeks before "
    "the supplier was created."),
   ('Suriya', 's', 'm2',
    "On the legal side I will say only what I can at this stage. The employment process is under "
    "way and the two individuals have been suspended on full pay, which is what our own procedure "
    "requires. We have reported the matter to the bank. Whether it goes beyond the employment "
    "process is not a decision for this committee tonight, and I would advise against discussing "
    "that in the minutes."),
   ('Pradit', 'p', 'm1',
    "Our recommendations are three, and they are all about the gap rather than about the people. "
    "First, supplier creation moves out of purchasing entirely and sits with the master data team, "
    "which is two people who cannot raise a purchase order. Second, no payment is released to a "
    "supplier created within the previous thirty days without a second signature. Third, the report "
    "that would have caught this, which lists suppliers created and paid by the same user, runs "
    "monthly from January and comes to this committee."),
   ('Pradit', 'p', 'm1',
    "I would make one last point, and it is not a comfortable one. This test took Oraphan four "
    "days. We could have run it at any time in the last three years. Nobody asked for it because "
    "nobody had thought of it. That is the real finding."),
  ],
  'questions': [
   {'q': 'Why are two names being withheld from the meeting?',
    'o': ['An employment process has not yet concluded',
          'The individuals have not yet been interviewed',
          'The committee secretary has not received the report',
          'The bank has asked for confidentiality'], 'a': 0,
    'e': u'"Legal have asked us to keep two names out of this room until the employment process '
         u'finishes" · ระหว่างกระบวนการทางวินัยยังไม่จบ การเอ่ยชื่อในที่ประชุมสร้างความเสี่ยงทางกฎหมาย'},
   {'q': 'Which control actually failed?',
    'o': ['One person was able both to set up a supplier and to authorise paying it',
          'The approval limit was set too high',
          'Payments were released without any approval at all',
          'The bank details of suppliers were never checked'], 'a': 0,
    'e': u'"It was that the same person could create a supplier and approve a payment to it" '
         u'· นี่คือการขาดการแบ่งแยกหน้าที่ ไม่ใช่เรื่องวงเงินอนุมัติ'},
   {'q': 'How was the test designed?',
    'o': ['Every new supplier record was matched with who approved its payments',
          'A sample of payments over the limit was examined',
          'All payments to closed sites were listed',
          'Bank accounts were compared with the supplier master file'], 'a': 0,
    'e': u'"we matched the creation record against the payment approval record" '
         u'· ทดสอบทั้งประชากร 2,106 ราย ไม่ได้สุ่มตัวอย่าง จึงไม่มีรายการไหนรอดการตรวจ'},
   {'q': 'What were fifteen of the nineteen cases?',
    'o': ['Combinations the system permits and nobody had questioned',
          'Errors in the supplier master file',
          'Payments that had already been recovered',
          'Cases the previous audit had cleared'], 'a': 0,
    'e': u'"which the system allows and which we had never treated as a problem" '
         u'· ระบบยอมให้ทำได้ และไม่มีใครเคยมองว่าเป็นปัญหา จึงไม่เคยถูกตั้งคำถาม'},
   {'q': 'What do the four unexplained cases have in common?',
    'o': ['They all concern a single supplier account',
          'They were all approved by the same manager',
          'They were all for amounts under the routine limit',
          'They all fell in the last month of the year'], 'a': 0,
    'e': u'"all four involved one supplier set up in March of last year" '
         u'· สี่รายการผูกกับผู้ขายรายเดียวที่เพิ่งตั้งขึ้น'},
   {'q': 'What makes the payments to that supplier implausible?',
    'o': ['Work was billed for premises that were no longer in use',
          'The amounts were far above the approval limit',
          'The supplier had no registered address',
          'The payments were all made on the same day'], 'a': 0,
    'e': u'"for maintenance services at a site that had been closed since the year before" '
         u'· จ่ายค่าบำรุงรักษาสถานที่ที่ปิดไปแล้ว และไม่มีทั้งสัญญาและบันทึกการทำงาน'},
   {'q': 'What is striking about the bank account?',
    'o': ['It came into existence just before the supplier did',
          'It belonged to a company in another country',
          'It had been used by another supplier before',
          'It was closed immediately after the last payment'], 'a': 0,
    'e': u'"the bank account it was paid into had been opened two weeks before the supplier was '
         u'created" · ลำดับเวลาแบบนี้บอกว่ามีการเตรียมการไว้ล่วงหน้า'},
   {'q': 'What does Suriya advise the committee about the minutes?',
    'o': ['Not to record any debate about going further than the employment process',
          'To record the names of both individuals',
          'To record that the bank has been informed',
          'To postpone approving the minutes until next month'], 'a': 0,
    'e': u'"I would advise against discussing that in the minutes" '
         u'· สิ่งที่บันทึกไว้ในรายงานการประชุมอาจถูกใช้เป็นหลักฐานภายหลัง'},
   {'q': 'What is the purpose of the thirty-day rule?',
    'o': ['To require a further signature while a supplier is still newly set up',
          'To delay payment to new suppliers by a month',
          'To give the master data team time to verify details',
          'To allow the bank to confirm the account'], 'a': 0,
    'e': u'"no payment is released to a supplier created within the previous thirty days without a '
         u'second signature" · ช่วงที่ความเสี่ยงสูงที่สุดคือช่วงที่ผู้ขายยังใหม่'},
   {'q': 'What does Pradit call the real finding?',
    'o': ['That it had never occurred to anybody to run such a test',
          'That the plant staff had concealed the payments',
          'That the system allowed the payments to be made',
          'That the previous audit had missed the problem'], 'a': 0,
    'e': u'"Nobody asked for it because nobody had thought of it" '
         u'· การตรวจที่ใช้เวลาสี่วันและทำได้ตลอดสามปีที่ผ่านมา ไม่เคยมีใครคิดถึง '
         u'เขาจึงชี้ว่าปัญหาอยู่ที่การออกแบบแผนตรวจสอบ ไม่ใช่ที่คนทำงานตรวจ'},
  ]},

 {'id': 'F8b', 'kind': 'interview',
  'title': 'Interview for a Treasury Assistant Position',
  'context': u'หัวหน้าฝ่ายบริหารเงินสัมภาษณ์ผู้สมัคร บอกตรง ๆ ว่ากำลังวัดอะไร '
             u'แล้วถามเรื่องงานที่มีเส้นตายซึ่งควบคุมไม่ได้ และเรื่องการรักษาความลับ',
  'turns': [
   ('Interviewer', 'i', 'm3',
    "Good morning. I am Marcus Flynn and I look after group treasury. There are four of us and we "
    "move a reasonable amount of money every day, so I will be direct with you about what I am "
    "testing for in this conversation. I want to know how you behave when something is urgent, and "
    "how you behave with information that should not leave the room. We have thirty minutes."),
   ('Ratchanee', 'r', 'f2',
    "Understood. Thank you for telling me."),
   ('Interviewer', 'i', 'm3',
    "Let us take the first of those. Tell me about a time you had to deliver something to a "
    "deadline you did not control."),
   ('Ratchanee', 'r', 'f2',
    "Yes. I spent last year as a part-time assistant in the finance office of a logistics company. "
    "Every Thursday morning the cash position for the following week had to be with the finance "
    "director by nine. The inputs came from three places, and one of them, the overseas branch, "
    "was reliably late."),
   ('Ratchanee', 'r', 'f2',
    "In my second month the branch file did not arrive at all. I had until nine, and I had two of "
    "the three inputs. What I did not do was wait and hope. At half past seven I sent what I had, "
    "marked clearly as two branches out of three, with the last four weeks of the missing branch "
    "shown beside it so that he could see the usual shape of it."),
   ('Ratchanee', 'r', 'f2',
    "I also wrote one line on what the risk was, which was that the missing branch had a large "
    "customer receipt due, and that if it had not landed, the group position was about four million "
    "baht weaker than the sheet showed. He told me afterwards that the line about the risk was the "
    "useful part. The file turned up at eleven and the receipt had landed."),
   ('Ratchanee', 'r', 'f2',
    "The lesson I took is that something incomplete and on time, with the gap marked, is usually "
    "worth more than something complete and late. But that only holds if you say exactly what is "
    "absent. If I had sent two branches and called it the cash position, that would have been "
    "worse than sending nothing at all."),
   ('Interviewer', 'i', 'm3',
    "Good. Now the second one. How do you handle information that is confidential?"),
   ('Ratchanee', 'r', 'f2',
    "In practice it comes down to small habits rather than good intentions. I do not discuss what I "
    "am working on outside the team, including with people inside the company who ask casually. I "
    "lock the screen even for two minutes. I do not send a draft to my own private email to work "
    "on at home, which I know people do."),
   ('Ratchanee', 'r', 'f2',
    "And if I am asked something I should not answer, I would rather say that it is not mine to "
    "share and point the person to whoever can decide. I would not invent a reason or pretend not "
    "to know, because that tends to tell the person something as well."),
   ('Interviewer', 'i', 'm3',
    "That last point is a fair one. Is there anything you would like to ask me?"),
   ('Ratchanee', 'r', 'f2',
    "One thing. When a payment has to be stopped at short notice, who can authorise that, and how "
    "late in the day is it still possible? I ask because that is the situation I would least like "
    "to be discovering for the first time while it was happening."),
  ],
  'questions': [
   {'q': 'What two things does the interviewer say he is testing for?',
    'o': ['Conduct under time pressure, and conduct with sensitive material',
          'Technical knowledge of banking and of accounting',
          'Attention to detail and speed of calculation',
          'Willingness to travel and to work long hours'], 'a': 0,
    'e': u'"how you behave when something is urgent, and how you behave with information that '
         u'should not leave the room" · ผู้สัมภาษณ์ที่บอกเกณฑ์ไว้ก่อน ช่วยให้ผู้สมัครเลือกตัวอย่างได้ตรง'},
   {'q': 'What made the Thursday deadline difficult?',
    'o': ['One of the sources was habitually slow',
          'The finance director often changed the deadline',
          'The figures had to be prepared by hand',
          'She was only in the office two days a week'], 'a': 0,
    'e': u'"one of them, the overseas branch, was reliably late" '
         u'· reliably late คือสายเป็นปกติ พูดแบบประชดเบา ๆ'},
   {'q': 'What did she do when the branch file failed to arrive?',
    'o': ['Sent what she had before the deadline, showing plainly what was absent',
          'Waited until the file arrived and sent it late',
          'Estimated the missing branch from the previous week',
          'Asked the finance director for more time'], 'a': 0,
    'e': u'"At half past seven I sent what I had, marked clearly as two branches out of three" '
         u'· ส่งก่อนเก้าโมงพร้อมระบุชัดว่าขาดอะไร'},
   {'q': 'Why did she attach the previous four weeks of the missing branch?',
    'o': ['To give the reader a sense of what the normal pattern looked like',
          'Because the director had asked for a trend',
          'To show that the branch was often late',
          'To replace the figures that were missing'], 'a': 0,
    'e': u'"so that he could see the usual shape of it" '
         u'· ไม่ได้เอาตัวเลขเก่ามาแทนตัวเลขที่ขาด แต่ให้ผู้อ่านเห็นว่าปกติหน้าตาเป็นอย่างไร'},
   {'q': 'What did the finance director find most useful?',
    'o': ['The note on what might go wrong',
          'The speed with which it arrived',
          'The comparison with the previous week',
          'The fact that it was marked as incomplete'], 'a': 0,
    'e': u'"the line about the risk was the useful part" '
         u'· ผู้บริหารต้องการรู้ว่าตัวเลขอาจผิดไปทางไหนและเท่าไร มากกว่าตัวเลขที่ดูเรียบร้อย'},
   {'q': 'What is her lesson about deadlines?',
    'o': ['A partial answer on time usually beats a full one that is late',
          'A deadline should be renegotiated as early as possible',
          'Work should never be sent out until it is complete',
          'The person waiting should decide what can be left out'], 'a': 0,
    'e': u'"something incomplete and on time, with the gap marked, is usually worth more than '
         u'something complete and late"'},
   {'q': 'What condition does she attach to that lesson?',
    'o': ['What is left out must be stated precisely',
          'The recipient must agree to it beforehand',
          'It applies only to internal reporting',
          'It applies only when the delay is somebody else fault'], 'a': 0,
    'e': u'"If I had sent two branches and called it the cash position, that would have been worse '
         u'than sending nothing at all" · ของไม่ครบที่บอกว่าไม่ครบมีประโยชน์ ของไม่ครบที่อ้างว่าครบเป็นอันตราย'},
   {'q': 'How does she describe handling confidential information?',
    'o': ['As a matter of everyday discipline rather than of good intentions',
          'As something the company rules take care of',
          'As a question of judgement in each case',
          'As the responsibility of her supervisor'], 'a': 0,
    'e': u'"it comes down to small habits rather than good intentions" '
         u'· เธอยกตัวอย่างนิสัยเล็ก ๆ ที่ทำได้ทุกวัน ไม่ได้พูดถึงเจตนาดี'},
   {'q': 'What does she say she will not do with a draft?',
    'o': ['Move it to a personal mailbox to work on elsewhere',
          'Print it and take it home',
          'Share it with another department',
          'Keep it after the work is finished'], 'a': 0,
    'e': u'"I do not send a draft to my own private email to work on at home, which I know people '
         u'do" · เธอยกตัวอย่างที่คนทำกันจริง ซึ่งแสดงว่าเข้าใจความเสี่ยงในทางปฏิบัติ'},
   {'q': 'Why does she ask about stopping a payment?',
    'o': ['She would rather know the procedure before she ever needs it',
          'She has had to do it in a previous job',
          'She wants to know who in the team is most senior',
          'She is concerned that the controls are too weak'], 'a': 0,
    'e': u'"that is the situation I would least like to be discovering for the first time while it '
         u'was happening" · คำถามของผู้สมัครที่ดี บอกว่าเขาคิดถึงงานจริงไว้แล้ว'},
  ]},

]},

# ══════════════════════════════════ ชุดที่ 10 ══════════════════════════════════
{'id': 'F9', 'title': u'ชุดที่ 10', 'parts': [

 {'id': 'F9a', 'kind': 'presentation',
  'title': 'A Business Case for a Second Warehouse',
  'context': u'ฝ่ายวางแผนห่วงโซ่อุปทาน ฝ่ายการเงิน และฝ่ายบริการลูกค้า '
             u'เสนอคณะกรรมการเรื่องการเปิดคลังสินค้าแห่งที่สองในภาคเหนือ',
  'turns': [
   ('Jinda', 'j', 'f1',
    "Good morning. I am Jinda from supply chain planning, with Ploy from finance and Narong from "
    "customer service. Our subject is whether we open a second warehouse in the north. We will "
    "take eighteen minutes, and we are asking for a decision today because the lease we have been "
    "offered expires on the fifteenth of December."),
   ('Jinda', 'j', 'f1',
    "Our recommendation is yes, but not for the reason the proposal was first raised. It was "
    "raised in order to cut freight cost. The freight saving on its own would not justify it. What "
    "justifies it is what we are currently losing on late deliveries, and Narong has that part."),
   ('Narong', 'n', 'm3',
    "Last year we delivered ninety-one percent of northern orders inside the promised window. In "
    "the central region it was ninety-eight. The difference is almost all transit time. We lost "
    "four accounts in the north last year, and in the exit conversations three of the four named "
    "delivery reliability first."),
   ('Narong', 'n', 'm3',
    "I should be careful here. I cannot tell you that a warehouse would have kept all four. Two of "
    "them were also unhappy about price. What I can tell you is that it was the same complaint in "
    "all four cases, and that we hear it from the accounts we still have."),
   ('Ploy', 'p', 'f2',
    "On the numbers. The lease, the fit-out and the additional stock come to about thirty-one "
    "million baht in the first year, of which nineteen is stock and therefore comes back to us if "
    "we close. Annual running cost after that is around nine million. The freight saving is about "
    "five and a half million a year, so on freight alone it does not pay."),
   ('Ploy', 'p', 'f2',
    "The revenue side is where I have to be honest about the uncertainty. If we hold the four "
    "accounts we would otherwise lose each year, the contribution is roughly seven million. That "
    "is an assumption and not a measurement. I have modelled it at half that as well, and at half "
    "it still works, but the payback moves from under three years to over five."),
   ('Ploy', 'p', 'f2',
    "One more thing the committee should know. Nineteen of the thirty-one million is stock we would "
    "hold anyway if demand grows as planned. If demand does not grow, we are carrying stock in two "
    "places instead of one, and that is the downside I would want you to weigh."),
   ('Jinda', 'j', 'f1',
    "To pull it together. Freight alone does not make the case. Service does, provided you accept "
    "Narong's reading of why we lose northern accounts, and Ploy has shown that it survives a much "
    "weaker assumption than the one we believe to be true. We ask you to approve the lease before "
    "the fifteenth, and Ploy will bring the stock policy back to you separately in the new year."),
  ],
  'questions': [
   {'q': 'Why is a decision needed today?',
    'o': ['An offer on the premises runs out in December',
          'The northern customers have given a deadline',
          'The budget for next year closes this week',
          'Construction must begin before the rainy season'], 'a': 0,
    'e': u'"the lease we have been offered expires on the fifteenth of December" '
         u'· เส้นตายมาจากข้อเสนอเช่า ไม่ใช่จากความเร่งร้อนของผู้เสนอ'},
   {'q': 'What has changed about the justification for the project?',
    'o': ['The reason it was first raised turns out not to be enough on its own',
          'The cost of the project has risen since it was first raised',
          'The project is now larger than first proposed',
          'A different location is now being recommended'], 'a': 0,
    'e': u'"It was raised in order to cut freight cost. The freight saving on its own would not '
         u'justify it" · ทีมที่กล้าบอกว่าเหตุผลตั้งต้นไม่พอ น่าเชื่อถือกว่าทีมที่ดันเหตุผลเดิมต่อ'},
   {'q': 'What explains the service gap in the north?',
    'o': ['The time taken for goods to travel there',
          'A shortage of staff in the northern team',
          'Orders being placed later than in other regions',
          'Stock shortages at the main warehouse'], 'a': 0,
    'e': u'"The difference is almost all transit time" · transit time คือเวลาที่ของอยู่ระหว่างทาง'},
   {'q': 'How does Narong qualify his own evidence?',
    'o': ['He cannot prove a warehouse would have retained those customers',
          'He admits the exit conversations were not recorded',
          'He says the figures cover only part of the year',
          'He accepts that the central region is not comparable'], 'a': 0,
    'e': u'"I cannot tell you that a warehouse would have kept all four. Two of them were also '
         u'unhappy about price" · เขาเล่าสิ่งที่ขัดกับข้อเสนอของตัวเองด้วย'},
   {'q': 'What strengthens his argument in spite of that?',
    'o': ['The same complaint is heard from customers who have stayed',
          'The four accounts were the largest in the region',
          'The central region has never lost an account',
          'The complaints were all made in writing'], 'a': 0,
    'e': u'"we hear it from the accounts we still have" '
         u'· ถ้าลูกค้าที่ยังอยู่ก็บ่นเรื่องเดียวกัน ปัญหานั้นก็ยังทำงานอยู่ ไม่ใช่เรื่องของสี่รายที่เสียไปแล้ว'},
   {'q': 'What is notable about the first-year investment?',
    'o': ['A large part of it would be recovered if the site closed',
          'All of it would be written off in the first year',
          'It is lower than the annual running cost',
          'Most of it is spent on the fit-out'], 'a': 0,
    'e': u'"nineteen is stock and therefore comes back to us if we close" '
         u'· สินค้าคงเหลือไม่ใช่เงินที่จ่ายทิ้ง ต่างจากค่าตกแต่งสถานที่'},
   {'q': 'Does the freight saving justify the project by itself?',
    'o': ['No, it is smaller than the yearly running cost',
          'Yes, it alone covers the whole investment',
          'Yes, but only after five years',
          'Ploy does not say'], 'a': 0,
    'e': u'ค่าขนส่งที่ประหยัดได้ราว 5.5 ล้านบาทต่อปี แต่ค่าดำเนินงานรายปีราว 9 ล้านบาท '
         u'· ประหยัดได้น้อยกว่าที่ต้องจ่ายเพิ่ม'},
   {'q': 'How does Ploy deal with the uncertainty in the revenue case?',
    'o': ['She tests it again using a far more cautious figure',
          'She leaves the revenue side out of the case',
          'She asks the committee to accept it on trust',
          'She uses the figure the sales team supplied'], 'a': 0,
    'e': u'"I have modelled it at half that as well, and at half it still works" '
         u'· การทดสอบด้วยสมมติฐานที่แย่กว่าความเชื่อของตัวเอง เป็นวิธีแสดงว่าข้อเสนอทนทาน'},
   {'q': 'What downside does Ploy want the committee to weigh?',
    'o': ['Stock would be held in two places if growth does not arrive',
          'The lease cannot be ended early',
          'The northern staff would need to be recruited quickly',
          'The freight contract would have to be renegotiated'], 'a': 0,
    'e': u'"If demand does not grow, we are carrying stock in two places instead of one" '
         u'· สมมติฐานเรื่องการเติบโตเป็นเงื่อนไขของทั้งข้อดีและข้อเสีย'},
   {'q': 'What exactly are they asking the committee to approve?',
    'o': ['The lease now, with the stock question brought back later',
          'Both the lease and the stock policy together',
          'The lease, subject to a review after one year',
          'A further study before any commitment'], 'a': 0,
    'e': u'"approve the lease before the fifteenth, and Ploy will bring the stock policy back to '
         u'you separately in the new year" · ขอเฉพาะเรื่องที่มีเส้นตาย ที่เหลือแยกไปขออนุมัติภายหลัง'},
  ]},

 {'id': 'F9b', 'kind': 'interview',
  'title': 'Interview for a Consulting Analyst Position',
  'context': u'ผู้จัดการทีมที่ปรึกษาด้านการเพิ่มประสิทธิภาพสัมภาษณ์ผู้สมัคร '
             u'ถามว่าทำไมเลือกงานที่ปรึกษา แล้วให้โจทย์สถานการณ์หนึ่งข้อให้คิดสด',
  'turns': [
   ('Interviewer', 'i', 'm2',
    "Good afternoon. I am Noah Bergstrom, a manager in the performance improvement team. This is "
    "the second of three conversations, so I will not go over your background in detail. What I "
    "would like to do is spend most of the time on how you think. I will give you one situation to "
    "work through, and after that you can ask me whatever you like."),
   ('Supansa', 's', 'f1',
    "Thank you. That sounds good."),
   ('Interviewer', 'i', 'm2',
    "Before the situation, one quick question. Why consulting rather than a finance role in "
    "industry?"),
   ('Supansa', 's', 'f1',
    "Two reasons, and the second is less flattering than the first. The first is that I would "
    "rather learn across several businesses than go deep into one straight away. I do not yet know "
    "what industry I want, and this is the only job I know of where not knowing is an advantage. "
    "The second reason is that I am a little afraid of settling into a routine too early, and I "
    "would rather be somewhere that does not let me."),
   ('Interviewer', 'i', 'm2',
    "Honest. Here is the situation. A client runs forty retail outlets. Profit has fallen for three "
    "quarters and nobody can say why. You have one week, and you can have whatever data exists. "
    "Where do you start?"),
   ('Supansa', 's', 'f1',
    "May I ask two questions first?"),
   ('Interviewer', 'i', 'm2',
    "Go ahead."),
   ('Supansa', 's', 'f1',
    "Has the fall happened in every outlet, or in some of them? And has it happened in what they "
    "take in, or in what they spend? Those two answers split the problem four ways, and I would "
    "not know which quarter of it to work in without them."),
   ('Interviewer', 'i', 'm2',
    "Say it is a fall in gross margin, concentrated in about a dozen outlets."),
   ('Supansa', 's', 'f1',
    "Then I would stop looking at the whole estate and start comparing those twelve with twelve "
    "that are holding up. I would want them matched as closely as I could manage, on size and on "
    "type of location, so that whatever is different between the two groups is a short list rather "
    "than everything."),
   ('Supansa', 's', 'f1',
    "And I would spend one of the five days in two of the twelve, standing in the shop. Not "
    "because the data is wrong, but because the thing that explains a margin fall in a shop is "
    "often something that never reaches a report. A promotion the staff apply wrongly. A product "
    "mix the local manager changed. Something the nearest competitor did in March."),
   ('Supansa', 's', 'f1',
    "What I would be careful about is spending the week building something complete. At the end of "
    "one week I would rather hand over two likely causes with the evidence for each, and say "
    "plainly what I have not looked at, than a full picture I cannot stand behind."),
   ('Interviewer', 'i', 'm2',
    "Thank you. What would you like to ask me?"),
   ('Supansa', 's', 'f1',
    "What happens on a project when the answer turns out to be something the client does not want "
    "to hear? I would like to know whether it reaches them, and who carries it."),
  ],
  'questions': [
   {'q': 'What is different about this conversation?',
    'o': ['It concentrates on how she reasons rather than on her background',
          'It is the first of several interviews',
          'It will be conducted entirely as a written test',
          'It is shorter than the other two'], 'a': 0,
    'e': u'"I will not go over your background in detail. What I would like to do is spend most of '
         u'the time on how you think"'},
   {'q': 'What is her first reason for choosing consulting?',
    'o': ['She wants exposure to several industries before narrowing down',
          'She expects the pay to be higher',
          'She wants to travel for work',
          'She has been advised to by a lecturer'], 'a': 0,
    'e': u'"I would rather learn across several businesses than go deep into one straight away" '
         u'· และเสริมว่างานนี้เป็นงานเดียวที่การยังไม่รู้กลายเป็นข้อดี'},
   {'q': 'What is the second, less flattering reason?',
    'o': ['She does not trust herself to avoid falling into a rut',
          'She was not offered a place in industry',
          'She finds accounting work dull',
          'She wants to leave her home town'], 'a': 0,
    'e': u'"I am a little afraid of settling into a routine too early, and I would rather be '
         u'somewhere that does not let me" · ยอมรับแรงจูงใจที่ไม่สวยนัก ซึ่งทำให้เหตุผลข้อแรกน่าเชื่อขึ้น'},
   {'q': 'What does she do before attempting the case?',
    'o': ['She asks for two pieces of missing information',
          'She asks for more time to think',
          'She explains the framework she will use',
          'She asks what the client has already tried'], 'a': 0,
    'e': u'"May I ask two questions first" · การถามก่อนตอบไม่ใช่การถ่วงเวลา '
         u'แต่เป็นการไม่เดาในสิ่งที่ถามได้'},
   {'q': 'Why does she ask those two questions in particular?',
    'o': ['They cut the problem down to one of four possibilities',
          'They tell her how much data is available',
          'They reveal how long the client has known',
          'They establish who her client contact is'], 'a': 0,
    'e': u'"Those two answers split the problem four ways, and I would not know which quarter of it '
         u'to work in without them" · ทุกคู่ของคำตอบให้พื้นที่ปัญหาที่ต่างกันโดยสิ้นเชิง'},
   {'q': 'What is her approach once she is told the answer?',
    'o': ['Set the weaker outlets beside similar ones that are performing',
          'Look at every one of the forty outlets in turn',
          'Begin with the accounts of the whole company',
          'Interview the head office management first'], 'a': 0,
    'e': u'"start comparing those twelve with twelve that are holding up" '
         u'· การเทียบกลุ่มที่มีปัญหากับกลุ่มที่ไม่มี ทำให้ตัวแปรที่ต่างกันเหลือน้อยลง'},
   {'q': 'Why does she want the two groups matched?',
    'o': ['So that the list of possible differences stays short',
          'So that the client cannot dispute the sample',
          'So that the same staff can be interviewed',
          'So that the data can be collected in one visit'], 'a': 0,
    'e': u'"so that whatever is different between the two groups is a short list rather than '
         u'everything" · ถ้าสองกลุ่มต่างกันทุกอย่าง ก็สรุปไม่ได้ว่าอะไรเป็นสาเหตุ'},
   {'q': 'Why would she spend a day inside two of the shops?',
    'o': ['Some causes never show up in any report',
          'Because the data from the shops is unreliable',
          'To check whether the staff are working properly',
          'Because the client asked for shop visits'], 'a': 0,
    'e': u'"Not because the data is wrong, but because the thing that explains a margin fall in a '
         u'shop is often something that never reaches a report" · เธอตัดการตีความที่ผิดออกไปเองด้วย'},
   {'q': 'What does she say she would avoid doing in the week?',
    'o': ['Producing a complete picture she could not defend',
          'Spending time with the client staff',
          'Looking at more than two possible causes',
          'Reporting anything before the week is over'], 'a': 0,
    'e': u'"I would rather hand over two likely causes with the evidence for each, and say plainly '
         u'what I have not looked at, than a full picture I cannot stand behind"'},
   {'q': 'What does her own question to the interviewer concern?',
    'o': ['Whether unwelcome conclusions actually reach the client',
          'How long a typical project lasts',
          'Whether analysts choose their own projects',
          'How performance is assessed in the first year'], 'a': 0,
    'e': u'"when the answer turns out to be something the client does not want to hear…whether it '
         u'reaches them, and who carries it" · เธอถามถึงความซื่อตรงขององค์กรและการแบ่งความรับผิดชอบ'},
  ]},

]},

]
