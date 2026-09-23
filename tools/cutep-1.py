# -*- coding: utf-8 -*-
u"""แบบฝึกฟังแนว CU-TEP · ชุดที่ 1

โครงสร้างตามข้อสอบจริง 30 ข้อ 30 คะแนน ฟังรอบเดียว
  short  บทสนทนาสั้นสองคน 15 บท ถามบทละ 1 ข้อ
  long   บทสนทนายาวสองคน 3 บท ถามบทละ 3 ข้อ
  mono   บรรยายเดี่ยว 2 บท ราว 200 ถึง 250 คำ ถามบทละ 3 ข้อ

จุดที่ต่างจากแบบฝึกฟังชุดเดิมของวิชา
  คำถามถูกพูดในไฟล์เสียง ไม่ได้พิมพ์ไว้ให้อ่านก่อน ผู้สอบเห็นแต่ตัวเลือกสี่ข้อ
  คำถามเน้นการตีความ เช่น ผู้พูดหมายความว่าอะไร จะทำอะไรต่อ มีความสัมพันธ์กันแบบไหน
  ไม่ใช่การจับตัวเลขตรง ๆ อย่างแบบฝึกชุดเดิม

ตัวเลือกตัวแรกในรายการคือคำตอบเสมอ หน้าเว็บจะสลับตำแหน่งให้เอง
"""

SET = {
 'id': 'C1', 'title': u'ชุดที่ 1',

 # ── Section 1 · Short dialogues ── 15 บท ถามบทละ 1 ข้อ
 'short': [
  {'id': 'C1s01',
   'turns': [('M', 'm1', "Did you manage to finish the group report last night?"),
             ('W', 'f1', "Let's just say my printer and I are no longer on speaking terms.")],
   'q': 'What does the woman imply?',
   'o': ['She had trouble printing the report.',
         'She has not started writing the report.',
         'She needs to buy a new printer today.',
         'She finished the report without any problems.'],
   'e': u'พูดเล่นว่าไม่คุยกับเครื่องพิมพ์แล้ว แปลว่าเครื่องพิมพ์มีปัญหา · ไม่ได้บอกว่ายังไม่ได้เขียน'},

  {'id': 'C1s02',
   'turns': [('W', 'f1', "Professor Lim's lecture starts at nine, doesn't it?"),
             ('M', 'm1', "It did last term.")],
   'q': 'What does the man imply?',
   'o': ['The starting time may have changed.',
         'The lecture has been cancelled.',
         'He has never attended the lecture.',
         'The professor is always late.'],
   'e': u'ใช้ did ซึ่งเป็นอดีต แปลว่าเทอมนี้อาจไม่ใช่เวลาเดิมแล้ว · เป็นกับดักการฟังรูปกริยา'},

  {'id': 'C1s03',
   'turns': [('M', 'm3', "I could give you a ride to the station if you like."),
             ('W', 'f2', "Oh, would you? This bag weighs a ton.")],
   'q': 'What will the woman probably do?',
   'o': ['Accept the ride.', 'Take a taxi instead.',
         'Leave her bag behind.', 'Walk to the station.'],
   'e': u'Would you? คือการตอบรับอย่างดีใจ ไม่ใช่คำถามจริง'},

  {'id': 'C1s04',
   'turns': [('W', 'f1', "How did the accounting midterm go?"),
             ('M', 'm1', "Let's just say I'll be seeing that chapter again.")],
   'q': 'What does the man mean?',
   'o': ['He did not do well.', 'He found the exam easy.',
         'He missed the exam.', 'He has already passed the course.'],
   'e': u'จะได้เจอบทนั้นอีก แปลว่าต้องกลับไปทบทวนหรืออาจต้องสอบซ่อม'},

  {'id': 'C1s05',
   'turns': [('M', 'm3', "The library closes at eight on Fridays now."),
             ('W', 'f3', "I thought it was ten."),
             ('M', 'm3', "That was before the budget cuts.")],
   'q': 'What can be inferred from the conversation?',
   'o': ['The library reduced its opening hours.',
         'The library will close permanently.',
         'The woman rarely uses the library.',
         'The library opens later on Fridays.'],
   'e': u'สิบโมงเป็นเวลาก่อนถูกตัดงบ ตอนนี้เหลือสองทุ่ม จึงคือการลดเวลาเปิด'},

  {'id': 'C1s06',
   'turns': [('W', 'f2', "Are you coming to the careers talk this afternoon?"),
             ('M', 'm3', "I have a deadline at five.")],
   'q': 'What does the man mean?',
   'o': ['He probably cannot attend.', 'He will arrive a little late.',
         'He has already attended it.', 'He is not interested in careers.'],
   'e': u'ไม่ได้ปฏิเสธตรง ๆ แต่บอกเหตุผลที่ไปไม่ได้ · เป็นรูปแบบที่ข้อสอบชอบใช้'},

  {'id': 'C1s07',
   'turns': [('M', 'm1', "This café is always packed at lunchtime."),
             ('W', 'f1', "Try the one behind the science building. Nobody has found it yet.")],
   'q': 'What does the woman suggest?',
   'o': ['Going to a quieter café.', 'Eating lunch earlier.',
         'Bringing lunch from home.', 'Waiting for a table.'],
   'e': u'ยังไม่มีใครเจอ แปลว่าคนน้อย จึงเป็นการแนะนำร้านที่เงียบกว่า'},

  {'id': 'C1s08',
   'turns': [('W', 'f3', "Did you hear that Daniel finally got the internship?"),
             ('M', 'm3', "After three rejections, he deserved it.")],
   'q': 'What can be inferred about Daniel?',
   'o': ['He applied several times before succeeding.',
         'He was the only applicant.',
         'He turned down three other offers.',
         'He was rejected again this year.'],
   'e': u'ถูกปฏิเสธสามครั้งก่อนหน้า แล้วจึงได้ · ระวังตัวเลือกที่กลับความหมายเป็นการปฏิเสธข้อเสนอ'},

  {'id': 'C1s09',
   'turns': [('M', 'm3', "Should I email the professor about the extension?"),
             ('W', 'f2', "I would go to her office hours if I were you.")],
   'q': 'What does the woman advise the man to do?',
   'o': ['Speak to the professor in person.', 'Send the email immediately.',
         'Ask another student first.', 'Submit the work without an extension.'],
   'e': u'If I were you คือการแนะนำ · office hours คือการไปพบตัวจริง ไม่ใช่การส่งอีเมล'},

  {'id': 'C1s10',
   'turns': [('W', 'f1', "These figures still don't balance, and I have been through them twice."),
             ('M', 'm1', "Did you check the closing entries from last month?")],
   'q': 'Where does this conversation most likely take place?',
   'o': ['In an accounting office.', 'In a bookshop.',
         'At a bank counter.', 'In a laboratory.'],
   'e': u'closing entries คือรายการปิดบัญชี เป็นศัพท์ที่ใช้ในงานบัญชีโดยเฉพาะ'},

  {'id': 'C1s11',
   'turns': [('M', 'm3', "I have been waiting forty minutes for this bus."),
             ('W', 'f3', "There is a strike today. Didn't you see the notice?")],
   'q': 'What can be inferred about the man?',
   'o': ['He was unaware of the strike.', 'He missed his bus.',
         'He is waiting at the wrong stop.', 'He does not usually take the bus.'],
   'e': u'คำถาม Didn’t you see แสดงว่าอีกฝ่ายไม่รู้ข่าว'},

  {'id': 'C1s12',
   'turns': [('W', 'f2', "Could you look at my draft before Thursday?"),
             ('M', 'm3', "Thursday is tight, but send it anyway.")],
   'q': 'What does the man mean?',
   'o': ['He will try, although he may be busy.',
         'He refuses to read the draft.',
         'He wants the draft after Thursday.',
         'He has already read the draft.'],
   'e': u'tight แปลว่าเวลาน้อย แต่ but send it anyway คือยังรับปากจะพยายาม'},

  {'id': 'C1s13',
   'turns': [('M', 'm1', "How are you finding the new supervisor?"),
             ('W', 'f1', "Put it this way, meetings finish on time now.")],
   'q': 'What does the woman imply about the new supervisor?',
   'o': ['He runs meetings more efficiently.', 'He cancels meetings often.',
         'He is difficult to work with.', 'He never attends meetings.'],
   'e': u'ประชุมเลิกตรงเวลาแล้ว เป็นการชมทางอ้อม'},

  {'id': 'C1s14',
   'turns': [('W', 'f3', "Is the seminar room booked for two o'clock?"),
             ('M', 'm3', "It was, but the group cancelled this morning.")],
   'q': 'What can be inferred about the seminar room?',
   'o': ['It is now available.', 'It is being repaired.',
         'It has been booked by another group.', 'It closes at two.'],
   'e': u'จองไว้แล้วแต่ยกเลิก จึงว่างอยู่ · ระวังคำว่า was ซึ่งเป็นอดีต'},

  {'id': 'C1s15',
   'turns': [('M', 'm3', "Shall we split a taxi to the conference?"),
             ('W', 'f2', "I am going the other way, actually.")],
   'q': 'What does the woman mean?',
   'o': ['She cannot share the taxi.', 'She prefers to walk.',
         'She will pay for the taxi.', 'She is not going to the conference.'],
   'e': u'ไปคนละทาง จึงแชร์รถไม่ได้ · ไม่ได้บอกว่าไม่ไปงาน'},
 ],

 # ── Section 2 · Long dialogues ── 3 บท ถามบทละ 3 ข้อ
 'long': [
  {'id': 'C1l1', 'title': 'Changing a Course',
   'context': u'นิสิตปรึกษาอาจารย์ที่ปรึกษาเรื่องขอเปลี่ยนวิชาเรียน',
   'turns': [
    ('W', 'f2', "Come in. You wanted to talk about your registration?"),
    ('M', 'm1', "Yes. I'd like to drop Cost Accounting and take Business Statistics instead."),
    ('W', 'f2', "May I ask why? You were doing reasonably well in it."),
    ('M', 'm1', "It clashes with my internship. The class is Tuesday afternoons, and that's when "
                "the audit team does its fieldwork visits."),
    ('W', 'f2', "I see. The difficulty is that Cost Accounting is a prerequisite for two courses "
                "you'll need in your final year. If you drop it now, you would have to take it in "
                "the summer session."),
    ('M', 'm1', "I didn't realise that. Is the summer session expensive?"),
    ('W', 'f2', "It costs about the same, but it runs five days a week for six weeks. Most students "
                "find it heavy going."),
    ('M', 'm1', "Then perhaps I should speak to my internship supervisor first and see whether the "
                "visits can be moved."),
    ('W', 'f2', "That would be my advice. The deadline for dropping is Friday, so let me know by "
                "Thursday at the latest."),
   ],
   'questions': [
    {'q': 'Why does the student want to change courses?',
     'o': ['The class time conflicts with his internship.',
           'He is failing the course.',
           'The course is too expensive.',
           'He has already taken a similar course.'],
     'e': u'"It clashes with my internship" · ไม่ใช่เพราะเรียนไม่ดี เพราะอาจารย์บอกว่าทำได้พอใช้'},
    {'q': 'What problem does the adviser point out?',
     'o': ['The course is required for later courses.',
           'The new course is already full.',
           'The deadline has already passed.',
           'The student has too few credits.'],
     'e': u'"Cost Accounting is a prerequisite for two courses you’ll need in your final year"'},
    {'q': 'What will the student most likely do next?',
     'o': ['Talk to his internship supervisor.',
           'Register for the summer session.',
           'Drop the course on Friday.',
           'Change his internship.'],
     'e': u'"perhaps I should speak to my internship supervisor first" · และอาจารย์เห็นด้วย'},
   ]},

  {'id': 'C1l2', 'title': 'A Budget Overrun',
   'context': u'พนักงานสองคนคุยกันเรื่องค่าใช้จ่ายเกินงบของโครงการ',
   'turns': [
    ('M', 'm3', "Have you seen the September figures? We're eleven percent over on the project "
                "budget."),
    ('W', 'f1', "I have. Most of it is the contractor, isn't it?"),
    ('M', 'm3', "About two thirds of it. The rest is freight, because we air-freighted the panels "
                "when the shipment was delayed."),
    ('W', 'f1', "That was the right call, though. Waiting for sea freight would have pushed the "
                "whole installation back by a month."),
    ('M', 'm3', "I agree, but finance will still want it explained. They've asked for a variance "
                "report by Wednesday."),
    ('W', 'f1', "Then let's separate the two causes clearly. The contractor overrun is a pricing "
                "problem and we should fix the contract. The freight was a deliberate decision to "
                "protect the schedule."),
    ('M', 'm3', "That's a fair way to put it. Can you pull the contractor invoices together?"),
    ('W', 'f1', "I'll have them to you tomorrow morning."),
   ],
   'questions': [
    {'q': 'What is the main topic of the conversation?',
     'o': ['Why the project went over budget.',
           'Whether to change contractors.',
           'How to delay the installation.',
           'When the shipment will arrive.'],
     'e': u'ทั้งบทวนอยู่กับสาเหตุที่ใช้เงินเกินงบสิบเอ็ดเปอร์เซ็นต์'},
    {'q': 'Why were the panels sent by air?',
     'o': ['To avoid delaying the installation.',
           'Because air freight was cheaper.',
           'Because the contractor requested it.',
           'To reduce the risk of damage.'],
     'e': u'"Waiting for sea freight would have pushed the whole installation back by a month"'},
    {'q': 'How does the woman suggest presenting the overrun?',
     'o': ['By separating the two different causes.',
           'By combining both causes into one figure.',
           'By blaming the contractor entirely.',
           'By delaying the report until October.'],
     'e': u'"let’s separate the two causes clearly" · ตัวหนึ่งเป็นปัญหาราคา อีกตัวเป็นการตัดสินใจโดยตั้งใจ'},
   ]},

  {'id': 'C1l3', 'title': 'A Loan Application',
   'context': u'ลูกค้าคุยกับเจ้าหน้าที่ธนาคารเรื่องขอสินเชื่อธุรกิจ',
   'turns': [
    ('W', 'f3', "Good morning. I understand you're applying for a working capital facility."),
    ('M', 'm3', "That's right. Two million baht, to cover the gap between paying suppliers and "
                "collecting from customers."),
    ('W', 'f3', "How long is that gap at the moment?"),
    ('M', 'm3', "We pay suppliers in thirty days but our customers take about seventy-five, so "
                "roughly forty-five days."),
    ('W', 'f3', "And has that changed recently?"),
    ('M', 'm3', "It has. Two years ago customers paid in sixty days. Three of our larger accounts "
                "have stretched their terms since then."),
    ('W', 'f3', "That's useful to know, and honestly it's the part the committee will focus on. "
                "They'll want to see your receivables ageing for the last eight quarters, not just "
                "the current one."),
    ('M', 'm3', "I can produce that. Anything else?"),
    ('W', 'f3', "The audited accounts for the last two years, and a cash flow forecast for the "
                "coming twelve months. Bring them in together, because an incomplete file goes to "
                "the back of the queue."),
   ],
   'questions': [
    {'q': 'Why does the man want the loan?',
     'o': ['To bridge the gap between paying and being paid.',
           'To buy new equipment.',
           'To repay an existing loan.',
           'To open a second branch.'],
     'e': u'"to cover the gap between paying suppliers and collecting from customers"'},
    {'q': 'What has changed over the last two years?',
     'o': ['Customers are taking longer to pay.',
           'Suppliers are demanding faster payment.',
           'The company has lost three large accounts.',
           'Interest rates have risen.'],
     'e': u'"Two years ago customers paid in sixty days" แล้วตอนนี้เป็นเจ็ดสิบห้าวัน'},
    {'q': 'What does the bank officer warn the man about?',
     'o': ['An incomplete application will be delayed.',
           'The loan amount is too large.',
           'The committee meets only once a year.',
           'Audited accounts are not accepted.'],
     'e': u'"an incomplete file goes to the back of the queue"'},
   ]},
 ],

 # ── Section 3 · Monologues ── 2 บท ถามบทละ 3 ข้อ
 'mono': [
  {'id': 'C1m1', 'title': 'Why Companies Hold Inventory',
   'context': u'ช่วงหนึ่งของคำบรรยายวิชาบัญชีต้นทุน เรื่องเหตุผลที่กิจการต้องถือสินค้าคงเหลือ',
   'turns': [
    ('Lecturer', 'm1',
     "In today's session I want to deal with a question that sounds simple but is not: why does a "
     "company hold inventory at all? Inventory ties up cash, takes up space, and can lose value. So "
     "why not order everything at the moment it is needed?"),
    ('Lecturer', 'm1',
     "There are three standard answers. The first is uncertainty of demand. If you cannot predict "
     "exactly how much customers will buy next week, you hold a buffer. The cost of holding that "
     "buffer is real, but the cost of turning a customer away is usually higher, and it is harder "
     "to measure."),
    ('Lecturer', 'm1',
     "The second is uncertainty of supply. A supplier may be late, a shipment may be held at "
     "customs, a factory may stop. Firms that depend on a single supplier in a single country "
     "usually hold more inventory than firms with several sources, and that is a rational response, "
     "not poor management."),
    ('Lecturer', 'm1',
     "The third is economies of scale. Ordering in larger quantities lowers the cost per unit, both "
     "in purchase price and in the cost of placing the order. That is why the classic ordering "
     "models trade off holding cost against ordering cost."),
    ('Lecturer', 'm1',
     "Now, the point I want you to take away is this. When you see a company with unusually high "
     "inventory, do not jump straight to the conclusion that it is badly run. Ask which of those "
     "three reasons applies. Sometimes the answer is none of them, and the stock is simply unsold "
     "and going stale. But you have to ask before you can tell the difference, and that question is "
     "the beginning of the analysis, not the end of it."),
   ],
   'questions': [
    {'q': 'What is the main purpose of the talk?',
     'o': ['To explain why firms hold inventory.',
           'To show how to calculate order quantities.',
           'To argue that inventory should be eliminated.',
           'To compare suppliers in different countries.'],
     'e': u'วางคำถามหลักไว้ตั้งแต่ต้นว่าทำไมกิจการถึงต้องถือสินค้าคงเหลือ'},
    {'q': 'According to the speaker, why do firms with one supplier hold more inventory?',
     'o': ['It is a rational response to supply risk.',
           'Their suppliers demand larger orders.',
           'They receive better prices for bulk buying.',
           'Their demand is harder to predict.'],
     'e': u'"that is a rational response, not poor management" · เป็นเรื่องความไม่แน่นอนของอุปทาน'},
    {'q': 'What does the speaker warn listeners against?',
     'o': ['Assuming high inventory means poor management.',
           'Ordering in large quantities.',
           'Relying on classic ordering models.',
           'Holding any buffer stock at all.'],
     'e': u'"do not jump straight to the conclusion that it is badly run"'},
   ]},

  {'id': 'C1m2', 'title': 'Library Orientation',
   'context': u'การแนะนำการใช้ห้องสมุดสำหรับนิสิตใหม่',
   'turns': [
    ('Librarian', 'f2',
     "Welcome, everyone. I have fifteen minutes, so I will concentrate on the three things that new "
     "students most often get wrong, rather than reading you the whole handbook."),
    ('Librarian', 'f2',
     "First, borrowing limits. Undergraduates may borrow eight items at a time for two weeks. What "
     "surprises people is that renewal is automatic unless another reader has requested the item. "
     "So you will not usually receive a reminder, and you should check your account rather than "
     "waiting to be told."),
    ('Librarian', 'f2',
     "Second, the reserve collection. Books that a lecturer has put on reserve cannot leave the "
     "building at all during term. Every year somebody argues with the desk staff about this. The "
     "rule exists because one copy has to serve three hundred students, and it is not negotiable."),
    ('Librarian', 'f2',
     "Third, and this is the one that matters most for your assignments: the databases. Almost "
     "everything you will need for coursework is in the subscription databases, not on the open "
     "shelves and not in a general web search. If you search from off campus, you must log in "
     "through the library portal first, otherwise the system will ask you to pay for articles the "
     "university already owns."),
    ('Librarian', 'f2',
     "We run a one-hour database workshop every Wednesday at four. It is not compulsory, but "
     "students who come to it consistently write better reference lists, and your tutors will "
     "notice. Sign-up is at the desk on your way out. Thank you."),
   ],
   'questions': [
    {'q': 'What does the speaker say about renewals?',
     'o': ['They happen automatically unless someone else requests the item.',
           'They must be requested at the desk.',
           'They are limited to eight per term.',
           'They are not allowed during term time.'],
     'e': u'"renewal is automatic unless another reader has requested the item"'},
    {'q': 'Why can reserve books not be taken out?',
     'o': ['One copy must serve a large number of students.',
           'They are too valuable to leave the building.',
           'They are needed for the database workshop.',
           'They belong to individual lecturers.'],
     'e': u'"one copy has to serve three hundred students"'},
    {'q': 'What mistake does the speaker warn about when searching off campus?',
     'o': ['Not logging in through the library portal.',
           'Using the reserve collection.',
           'Borrowing more than eight items.',
           'Missing the Wednesday workshop.'],
     'e': u'"you must log in through the library portal first, otherwise the system will ask you to pay"'},
   ]},
 ],
}
