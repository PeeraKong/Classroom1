# -*- coding: utf-8 -*-
u"""แบบฝึกฟังแนว CU-TEP · ชุดที่ 3 · โครงสร้างเดียวกับ tools/cutep-1.py"""

SET = {
 'id': 'C3', 'title': u'ชุดที่ 3',

 'short': [
  {'id': 'C3s01',
   'turns': [('M', 'm1', "Have you handed in the ethics form for your project?"),
             ('W', 'f1', "I did not know there was one.")],
   'q': 'What can be inferred about the woman?',
   'o': ['She has not submitted the form.',
         'She submitted the form last week.',
         'She lost the form she was given.',
         'She does not need the form.'],
   'e': u'ไม่รู้ว่ามีแบบฟอร์ม จึงยังไม่ได้ส่งแน่นอน'},

  {'id': 'C3s02',
   'turns': [('W', 'f2', "This coffee machine has been broken for a month."),
             ('M', 'm3', "I have stopped noticing.")],
   'q': 'What does the man imply?',
   'o': ['He has got used to the situation.',
         'He repaired the machine himself.',
         'He never uses the machine.',
         'He reported the problem already.'],
   'e': u'เลิกสังเกตแล้ว แปลว่าชินกับสภาพที่เป็นอยู่'},

  {'id': 'C3s03',
   'turns': [('M', 'm1', "Shall we present the findings as a table or a chart?"),
             ('W', 'f3', "The committee has fifteen minutes and twelve slides to get through.")],
   'q': 'What does the woman suggest?',
   'o': ['Using whichever form is quicker to understand.',
         'Removing the findings from the presentation.',
         'Asking the committee for more time.',
         'Presenting both a table and a chart.'],
   'e': u'เวลาน้อยและสไลด์เยอะ จึงเป็นการบอกทางอ้อมว่าต้องเลือกแบบที่เข้าใจเร็ว'},

  {'id': 'C3s04',
   'turns': [('W', 'f1', "Is Mr Wichai the one who signs the purchase orders?"),
             ('M', 'm3', "He was until the reorganisation.")],
   'q': 'What can be inferred?',
   'o': ['Someone else signs them now.',
         'Mr Wichai has left the company.',
         'Purchase orders no longer need signing.',
         'The reorganisation has not happened yet.'],
   'e': u'was until... แปลว่าเปลี่ยนไปแล้ว แต่ไม่ได้บอกว่าเขาลาออก'},

  {'id': 'C3s05',
   'turns': [('M', 'm1', "I thought the deadline was the fifteenth."),
             ('W', 'f2', "It was moved forward a week when the term dates changed.")],
   'q': 'When is the deadline now?',
   'o': ['The eighth.', 'The twenty-second.',
         'The fifteenth.', 'The first.'],
   'e': u'moved forward a week คือเลื่อนให้เร็วขึ้นหนึ่งสัปดาห์ จาก 15 เป็น 8'},

  {'id': 'C3s06',
   'turns': [('W', 'f3', "Do you want to join the study group on Sundays?"),
             ('M', 'm3', "Sundays are when I see my family.")],
   'q': 'What does the man mean?',
   'o': ['He is not available on Sundays.',
         'He will bring his family along.',
         'He would prefer to study alone.',
         'He has already joined a study group.'],
   'e': u'ปฏิเสธอย่างสุภาพโดยบอกว่าติดธุระประจำ'},

  {'id': 'C3s07',
   'turns': [('M', 'm1', "The supplier says the invoice was settled in March."),
             ('W', 'f1', "Then why is it still sitting in the payables ledger?")],
   'q': 'What is the woman suggesting?',
   'o': ['The records may not match the supplier’s claim.',
         'The supplier should be paid immediately.',
         'The invoice was issued in the wrong month.',
         'The ledger should be closed for March.'],
   'e': u'ถ้าจ่ายแล้วจริง ก็ไม่ควรค้างอยู่ในบัญชีเจ้าหนี้ · เป็นการตั้งข้อสงสัยกับข้อมูล'},

  {'id': 'C3s08',
   'turns': [('W', 'f2', "How did you find the internship interview?"),
             ('M', 'm3', "They asked me about my final-year project for twenty minutes.")],
   'q': 'What can be inferred about the interview?',
   'o': ['The interviewers were interested in his project.',
         'The interview was shorter than expected.',
         'He was unprepared for the questions.',
         'He was not asked about his studies.'],
   'e': u'ถามเรื่องเดียวนานถึงยี่สิบนาที แสดงว่าสนใจเรื่องนั้นเป็นพิเศษ'},

  {'id': 'C3s09',
   'turns': [('M', 'm1', "Should I put the exchange rate assumption in the appendix?"),
             ('W', 'f3', "It changes the answer by twelve percent.")],
   'q': 'What does the woman mean?',
   'o': ['The assumption is too important for the appendix.',
         'The appendix is the right place for it.',
         'The assumption should be removed.',
         'The calculation contains an error.'],
   'e': u'กระทบคำตอบถึงสิบสองเปอร์เซ็นต์ จึงสำคัญเกินกว่าจะซ่อนไว้ท้ายเล่ม'},

  {'id': 'C3s10',
   'turns': [('W', 'f1', "Is the shuttle bus running during the holiday?"),
             ('M', 'm3', "Only the morning service, and only on weekdays.")],
   'q': 'What can be inferred about the shuttle bus?',
   'o': ['Its service is reduced during the holiday.',
         'It is not running at all.',
         'It runs more often than usual.',
         'It runs only at weekends.'],
   'e': u'Only... and only... เป็นการบอกว่าให้บริการน้อยลงกว่าปกติ'},

  {'id': 'C3s11',
   'turns': [('M', 'm1', "Did you say the workshop is compulsory?"),
             ('W', 'f2', "I said it is strongly recommended.")],
   'q': 'What is the woman doing?',
   'o': ['Correcting the man’s understanding.',
         'Agreeing with the man.',
         'Inviting the man to the workshop.',
         'Explaining why the workshop was cancelled.'],
   'e': u'I said... เป็นการแก้ความเข้าใจผิด ระหว่างบังคับกับแนะนำอย่างยิ่ง'},

  {'id': 'C3s12',
   'turns': [('W', 'f3', "The client wants the draft accounts by Friday."),
             ('M', 'm1', "We have not received their bank confirmations yet.")],
   'q': 'What is the man indicating?',
   'o': ['The deadline may not be achievable.',
         'He will finish the accounts by Friday.',
         'The client has changed the deadline.',
         'Bank confirmations are not required.'],
   'e': u'ยังขาดหลักฐานสำคัญ จึงเป็นการบอกทางอ้อมว่าอาจไม่ทัน'},

  {'id': 'C3s13',
   'turns': [('M', 'm3', "Everyone says the second-year modules are the hardest."),
             ('W', 'f1', "Everyone says that about whichever year they are in.")],
   'q': 'What does the woman imply?',
   'o': ['The claim is not reliable.',
         'The second year really is the hardest.',
         'She has not reached the second year yet.',
         'The modules have become easier.'],
   'e': u'ชี้ว่าคนพูดแบบนี้กับทุกชั้นปี จึงเชื่อถือไม่ได้'},

  {'id': 'C3s14',
   'turns': [('W', 'f2', "Would Tuesday at three suit you for the review meeting?"),
             ('M', 'm1', "I have the board pack to finish by Tuesday lunchtime."),
             ('W', 'f2', "Three o'clock is after lunch.")],
   'q': 'What does the woman mean?',
   'o': ['The meeting does not conflict with his work.',
         'The meeting should be moved to Wednesday.',
         'He should finish the board pack earlier.',
         'She will attend the meeting without him.'],
   'e': u'ชี้ว่างานเสร็จตอนเที่ยง ส่วนประชุมบ่ายสาม จึงไม่ชนกัน'},

  {'id': 'C3s15',
   'turns': [('M', 'm1', "I have emailed you the revised figures three times."),
             ('W', 'f3', "Try my new address. The old one bounces.")],
   'q': 'Why has the woman not received the figures?',
   'o': ['The man used an address that no longer works.',
         'She deleted the emails by mistake.',
         'The attachments were too large.',
         'The man forgot to send them.'],
   'e': u'bounces แปลว่าอีเมลตีกลับ เพราะที่อยู่เดิมใช้ไม่ได้แล้ว'},
 ],

 'long': [
  {'id': 'C3l1', 'title': 'Choosing Between Two Job Offers',
   'context': u'นิสิตจบใหม่ปรึกษารุ่นพี่เรื่องเลือกระหว่างงานสองที่',
   'turns': [
    ('W', 'f1', "You said you had two offers. How are you thinking about them?"),
    ('M', 'm3', "One is a big four firm, the other is the finance team of a manufacturing company. "
                "The company pays about fifteen percent more."),
    ('W', 'f1', "And which would you take if the pay were identical?"),
    ('M', 'm3', "The firm, probably. But fifteen percent is fifteen percent."),
    ('W', 'f1', "It is, in year one. Ask yourself what each job looks like in year four. In the "
                "firm you will have seen thirty businesses. In the company you will know one "
                "business extremely well."),
    ('M', 'm3', "Which is better?"),
    ('W', 'f1', "Neither is better in the abstract. They open different doors. But there is an "
                "asymmetry worth knowing: moving from the firm into industry is common, and moving "
                "the other way is much rarer."),
    ('M', 'm3', "So the firm keeps more options open."),
    ('W', 'f1', "In general, yes. I would not decide on that alone, but I would weigh it against "
                "the fifteen percent rather than ignoring it."),
   ],
   'questions': [
    {'q': 'What is the man’s dilemma?',
     'o': ['One offer pays more but he prefers the other.',
           'He has not received either offer in writing.',
           'Both offers have the same salary.',
           'He is unsure whether to work at all.'],
     'e': u'ถ้าเงินเท่ากันเขาจะเลือกสำนักงาน แต่บริษัทให้มากกว่าสิบห้าเปอร์เซ็นต์'},
    {'q': 'What does the woman say about experience after four years?',
     'o': ['The firm gives breadth, the company gives depth.',
           'Both give the same experience.',
           'The company gives better technical training.',
           'The firm offers faster promotion.'],
     'e': u'"you will have seen thirty businesses … you will know one business extremely well"'},
    {'q': 'What asymmetry does the woman point out?',
     'o': ['Moving from the firm to industry is easier than the reverse.',
           'Industry salaries rise faster than firm salaries.',
           'Firms recruit more graduates than companies do.',
           'Industry roles require more qualifications.'],
     'e': u'"moving from the firm into industry is common, and moving the other way is much rarer"'},
   ]},

  {'id': 'C3l2', 'title': 'A Problem With a Group Project',
   'context': u'นิสิตสองคนคุยกันเรื่องเพื่อนร่วมกลุ่มที่ไม่ส่งงาน',
   'turns': [
    ('M', 'm1', "Have you heard anything from Pim? Her section was due to us on Sunday."),
    ('W', 'f2', "Nothing. I messaged her twice."),
    ('M', 'm1', "We present on Thursday. I think we should just write it ourselves."),
    ('W', 'f2', "We could, but then she gets the same mark for doing nothing, and we still do not "
                "know why she has gone quiet."),
    ('M', 'm1', "What else can we do at this point?"),
    ('W', 'f2', "Two things. Email her once more, copying the tutor, so there is a record. And "
                "start drafting her section in parallel, so we are covered either way."),
    ('M', 'm1', "Copying the tutor feels harsh."),
    ('W', 'f2', "It is not a complaint. It is a note saying we have tried to reach her and the "
                "deadline is Thursday. If she is ill, the tutor needs to know anyway."),
    ('M', 'm1', "Fair enough. I will start on the draft tonight."),
   ],
   'questions': [
    {'q': 'What is the problem?',
     'o': ['A group member has not submitted her part.',
           'The group has missed the presentation.',
           'The tutor has rejected their draft.',
           'The group cannot agree on a topic.'],
     'e': u'"Her section was due to us on Sunday" แล้วยังไม่ได้รับ'},
    {'q': 'Why does the woman not simply write the missing section?',
     'o': ['The absent member would get credit for nothing.',
           'She does not have time before Thursday.',
           'The tutor has forbidden it.',
           'She does not understand the topic.'],
     'e': u'"then she gets the same mark for doing nothing"'},
    {'q': 'Why does the woman want to copy the tutor?',
     'o': ['To create a record of their attempts to reach her.',
           'To complain about the absent member.',
           'To request an extension.',
           'To ask the tutor to write the section.'],
     'e': u'"It is not a complaint. It is a note saying we have tried to reach her"'},
   ]},

  {'id': 'C3l3', 'title': 'Renting a Flat',
   'context': u'ผู้เช่าคุยกับเจ้าหน้าที่นายหน้าเรื่องสัญญาเช่า',
   'turns': [
    ('W', 'f3', "The rent is eighteen thousand a month. Is that within your range?"),
    ('M', 'm1', "It is at the top of it. What does that include?"),
    ('W', 'f3', "Water and building maintenance. Electricity and internet are separate."),
    ('M', 'm1', "And the deposit?"),
    ('W', 'f3', "Two months, plus one month in advance, so you pay three months on signing."),
    ('M', 'm1', "That is a lot to find at once. Is the deposit refundable?"),
    ('W', 'f3', "In full, provided there is no damage beyond normal wear. The point people miss is "
                "the inventory check. Go through it on the day you move in and photograph anything "
                "already marked or broken."),
    ('M', 'm1', "Otherwise it comes out of the deposit at the end."),
    ('W', 'f3', "Exactly. Most deposit disputes I see come from that one omission, not from "
                "anything the tenant did."),
   ],
   'questions': [
    {'q': 'What is included in the rent?',
     'o': ['Water and building maintenance.',
           'Electricity and internet.',
           'All utilities.',
           'Nothing beyond the flat itself.'],
     'e': u'"Water and building maintenance. Electricity and internet are separate"'},
    {'q': 'How much must the man pay when he signs?',
     'o': ['Three months.', 'Two months.', 'One month.', 'Eighteen thousand only.'],
     'e': u'"Two months, plus one month in advance, so you pay three months on signing"'},
    {'q': 'What does the agent advise the man to do on moving in?',
     'o': ['Check the inventory and photograph existing damage.',
           'Pay the deposit in cash.',
           'Arrange his own maintenance contract.',
           'Ask for a longer contract.'],
     'e': u'"Go through it on the day you move in and photograph anything already marked or broken"'},
   ]},
 ],

 'mono': [
  {'id': 'C3m1', 'title': 'Why Forecasts Go Wrong',
   'context': u'คำบรรยายเรื่องสาเหตุที่ประมาณการมักคลาดเคลื่อน',
   'turns': [
    ('Lecturer', 'm3',
     "Every forecast you will ever prepare will be wrong. That is not a criticism of forecasting. "
     "It is the nature of the exercise. What separates a useful forecast from a useless one is not "
     "accuracy, but whether the person reading it understands where the error is likely to come "
     "from."),
    ('Lecturer', 'm3',
     "There are three common sources. The first is a bad assumption that nobody noticed, because "
     "it was buried three worksheets deep and never stated on the front page. The remedy is simple: "
     "put your assumptions where the reader sees them, not where they have to hunt for them."),
    ('Lecturer', 'm3',
     "The second source is anchoring. Whoever prepares the forecast usually starts from last "
     "year's number and adjusts. That feels sensible, but it means the forecast can only be a "
     "modest distance from where we already are, which is exactly wrong in the years when "
     "something genuinely changes."),
    ('Lecturer', 'm3',
     "The third, and the one I want you to remember, is that forecasts are rarely neutral "
     "documents. Somebody wants the number to come out a particular way. The sales forecast that "
     "supports the bonus, the cost forecast that justifies the project. Nobody has to lie for this "
     "to distort the result. Choosing the optimistic end of a reasonable range, ten times over, is "
     "enough."),
    ('Lecturer', 'm3',
     "So when you are handed a forecast, ask three questions. What are the assumptions? What was "
     "the starting point? And who benefits if this number turns out high rather than low? Those "
     "three will tell you more than recalculating the arithmetic ever will."),
   ],
   'questions': [
    {'q': 'What does the speaker say makes a forecast useful?',
     'o': ['Understanding where the error is likely to come from.',
           'Achieving a high level of accuracy.',
           'Using last year’s figures as a base.',
           'Keeping the assumptions confidential.'],
     'e': u'"not accuracy, but whether the person reading it understands where the error is likely to come from"'},
    {'q': 'What problem does anchoring cause?',
     'o': ['The forecast stays too close to the current position.',
           'The assumptions become too detailed.',
           'The forecast is prepared too late.',
           'Different departments disagree.'],
     'e': u'"the forecast can only be a modest distance from where we already are"'},
    {'q': 'According to the speaker, how do forecasts become distorted?',
     'o': ['By repeatedly choosing the optimistic end of a reasonable range.',
           'By deliberate falsification of figures.',
           'By using the wrong arithmetic.',
           'By being prepared by junior staff.'],
     'e': u'"Nobody has to lie for this … Choosing the optimistic end of a reasonable range, ten times over, is enough"'},
   ]},

  {'id': 'C3m2', 'title': 'Volunteering at the Student Union',
   'context': u'การชี้แจงสำหรับนิสิตที่สนใจเป็นอาสาสมัครขององค์การนิสิต',
   'turns': [
    ('Speaker', 'f1',
     "Thank you for coming. This session is for anyone thinking about volunteering with the union "
     "next semester, and my aim is to be honest about what it involves rather than to recruit you "
     "at any cost."),
    ('Speaker', 'f1',
     "We have four teams. Events runs the concerts and the sports day. Welfare handles the food "
     "bank and the peer listening service. Communications produces the newsletter and the social "
     "accounts. And Finance, which is the smallest team and the one that is always short of "
     "people, keeps the books and processes the society grants."),
    ('Speaker', 'f1',
     "I want to be clear about the time. The advertised commitment is four hours a week. In Events "
     "during festival month it is closer to fifteen, and in Finance it is very light for most of "
     "the year and then extremely heavy for the three weeks of grant applications. If your "
     "timetable cannot absorb those peaks, choose Welfare or Communications, which are steadier."),
    ('Speaker', 'f1',
     "What do you get out of it? Not money, because none of these roles are paid. You get a "
     "reference from someone who has actually watched you work, which is worth more than most "
     "students realise, and in Finance specifically you get experience that employers in our "
     "faculty ask about directly."),
    ('Speaker', 'f1',
     "Applications close on the last Friday of term. There is no interview for Events or "
     "Communications; there is a short one for Welfare, because of the listening service, and for "
     "Finance, because you will be handling other people's money. Forms are on the table by the "
     "door."),
   ],
   'questions': [
    {'q': 'What does the speaker say is her aim?',
     'o': ['To describe the roles honestly rather than recruit at any cost.',
           'To fill every position before the end of term.',
           'To explain how the union spends its budget.',
           'To encourage students to join the Events team.'],
     'e': u'"my aim is to be honest about what it involves rather than to recruit you at any cost"'},
    {'q': 'What is distinctive about the workload in Finance?',
     'o': ['It is light most of the year but very heavy for a short period.',
           'It is the same every week of the year.',
           'It is the heaviest of the four teams overall.',
           'It requires fifteen hours a week during festival month.'],
     'e': u'"very light for most of the year and then extremely heavy for the three weeks of grant applications"'},
    {'q': 'Which teams require an interview?',
     'o': ['Welfare and Finance.', 'Events and Communications.',
           'All four teams.', 'Only Finance.'],
     'e': u'"there is a short one for Welfare … and for Finance"'},
   ]},
 ],
}
