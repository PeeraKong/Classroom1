# -*- coding: utf-8 -*-
u"""แบบฝึกฟังแนว CU-TEP · ชุดที่ 5 · โครงสร้างเดียวกับ tools/cutep-1.py"""

SET = {
 'id': 'C5', 'title': u'ชุดที่ 5',

 'short': [
  {'id': 'C5s01',
   'turns': [('M', 'm1', "Did the lecturer say the exam is open book?"),
             ('W', 'f2', "She said we may bring one page of notes.")],
   'q': 'What does the woman mean?',
   'o': ['Only limited notes are allowed.',
         'The exam is fully open book.',
         'No materials may be brought in.',
         'The lecturer has not decided.'],
   'e': u'อนุญาตแค่หนึ่งหน้า จึงไม่ใช่ open book เต็มรูปแบบ'},

  {'id': 'C5s02',
   'turns': [('W', 'f1', "Have you booked the flights for the Chiang Mai visit?"),
             ('M', 'm3', "I am waiting for the client to confirm the dates.")],
   'q': 'What is the situation?',
   'o': ['The flights have not been booked yet.',
         'The flights were booked this morning.',
         'The visit has been cancelled.',
         'The client has confirmed the dates.'],
   'e': u'ยังรอลูกค้ายืนยัน จึงยังไม่ได้จอง'},

  {'id': 'C5s03',
   'turns': [('M', 'm1', "How was the workshop on data analytics?"),
             ('W', 'f3', "I wish I had gone last year instead of this one.")],
   'q': 'What does the woman imply?',
   'o': ['The workshop would have been more useful earlier.',
         'The workshop was cancelled last year.',
         'She did not attend the workshop.',
         'She plans to attend again next year.'],
   'e': u'I wish I had... คือความเสียดายว่าน่าจะไปตั้งแต่ปีที่แล้ว'},

  {'id': 'C5s04',
   'turns': [('W', 'f2', "The report says revenue grew by twenty percent."),
             ('M', 'm3', "Before or after the acquisition?")],
   'q': 'What is the man questioning?',
   'o': ['Whether the growth is comparable.',
         'Whether the report is genuine.',
         'Whether revenue grew at all.',
         'Whether the acquisition was approved.'],
   'e': u'ถ้ารวมกิจการที่เพิ่งซื้อเข้ามา การเติบโตก็เทียบกันไม่ได้'},

  {'id': 'C5s05',
   'turns': [('M', 'm1', "Is there still time for me to change my elective?"),
             ('W', 'f1', "The registration system locked at midnight last night.")],
   'q': 'What does the woman mean?',
   'o': ['It is too late to change.',
         'He must change it before midnight.',
         'The system is being repaired.',
         'He should change it online.'],
   'e': u'ระบบปิดไปแล้วเมื่อเที่ยงคืน จึงเปลี่ยนไม่ได้แล้ว'},

  {'id': 'C5s06',
   'turns': [('W', 'f3', "Is the training compulsory for new joiners?"),
             ('M', 'm3', "You cannot get system access until you have done it.")],
   'q': 'What does the man imply?',
   'o': ['In practice the training is unavoidable.',
         'The training is entirely optional.',
         'System access is granted first.',
         'New joiners are exempt from training.'],
   'e': u'ไม่ตอบว่าบังคับ แต่บอกผลที่ทำให้เลี่ยงไม่ได้'},

  {'id': 'C5s07',
   'turns': [('M', 'm1', "I have booked the small meeting room for the twelve of us."),
             ('W', 'f2', "It seats six.")],
   'q': 'What is the woman pointing out?',
   'o': ['The room is too small for the group.',
         'The booking was made for the wrong day.',
         'Six people have already cancelled.',
         'A larger room costs more.'],
   'e': u'สิบสองคนแต่ห้องจุหก จึงไม่พอ'},

  {'id': 'C5s08',
   'turns': [('W', 'f1', "Did you find the error in the trial balance?"),
             ('M', 'm3', "The difference was exactly nine hundred.")],
   'q': 'What does the man’s answer suggest?',
   'o': ['The error is probably a transposition.',
         'The trial balance is correct.',
         'Nine entries are missing.',
         'The error cannot be located.'],
   'e': u'ผลต่างที่หารด้วยเก้าลงตัว มักเกิดจากการสลับตัวเลข เป็นเคล็ดที่นักบัญชีใช้กัน'},

  {'id': 'C5s09',
   'turns': [('M', 'm1', "The deadline for the scholarship is next Friday."),
             ('W', 'f3', "I have not even started the essay."),
             ('M', 'm1', "It is only five hundred words.")],
   'q': 'What is the man doing?',
   'o': ['Reassuring her that the task is manageable.',
         'Warning her that she will fail.',
         'Offering to write the essay for her.',
         'Suggesting she apply next year.'],
   'e': u'บอกว่าแค่ห้าร้อยคำ เป็นการปลอบว่าทำทันแน่'},

  {'id': 'C5s10',
   'turns': [('W', 'f2', "Do you take the bus or the underground to work?"),
             ('M', 'm3', "Whichever is moving.")],
   'q': 'What does the man mean?',
   'o': ['He chooses depending on the traffic.',
         'He always takes the bus.',
         'He walks to work instead.',
         'He drives his own car.'],
   'e': u'เลือกตามว่าอันไหนไปได้ แปลว่าขึ้นกับสภาพการจราจรในวันนั้น'},

  {'id': 'C5s11',
   'turns': [('M', 'm1', "Kanya said she would finish the schedules by today."),
             ('W', 'f1', "Kanya says that every week.")],
   'q': 'What does the woman imply about Kanya?',
   'o': ['Her promises are not reliable.',
         'She works faster than others.',
         'She has already finished.',
         'She was given too much work.'],
   'e': u'พูดแบบนี้ทุกสัปดาห์ แปลว่าไม่ค่อยทำได้จริง'},

  {'id': 'C5s12',
   'turns': [('W', 'f3', "Shall I print the draft double sided?"),
             ('M', 'm3', "The partner reads with a pen in his hand.")],
   'q': 'What does the man mean?',
   'o': ['Print on one side so there is room to write.',
         'Print double sided to save paper.',
         'Send the draft by email instead.',
         'Ask the partner what he prefers.'],
   'e': u'อ่านไปเขียนไป จึงต้องเว้นที่ว่างสำหรับจดข้าง ๆ'},

  {'id': 'C5s13',
   'turns': [('M', 'm1', "Is the canteen open during the exam period?"),
             ('W', 'f2', "Only the coffee counter, and only until two.")],
   'q': 'What can be inferred?',
   'o': ['The canteen service is limited during exams.',
         'The canteen is closed completely.',
         'The canteen opens later than usual.',
         'The coffee counter has closed permanently.'],
   'e': u'เปิดเฉพาะบางส่วนและเวลาสั้นลง จึงเป็นการให้บริการจำกัด'},

  {'id': 'C5s14',
   'turns': [('W', 'f1', "The consultant charges nine thousand a day."),
             ('M', 'm3', "And how many days does she think it will take?")],
   'q': 'What is the man trying to establish?',
   'o': ['The total cost of the work.',
         'Whether the rate is reasonable.',
         'When the consultant can start.',
         'Whether a cheaper consultant exists.'],
   'e': u'รู้ราคาต่อวันแล้ว ถามจำนวนวันเพื่อคิดยอดรวม'},

  {'id': 'C5s15',
   'turns': [('M', 'm1', "Shall we go over the figures once more before the meeting?"),
             ('W', 'f3', "We have been over them four times.")],
   'q': 'What does the woman mean?',
   'o': ['Further checking is unnecessary.',
         'She has not checked them yet.',
         'She wants to check them again.',
         'The figures contain four errors.'],
   'e': u'ทวนมาสี่รอบแล้ว เป็นการบอกว่าพอแล้ว'},
 ],

 'long': [
  {'id': 'C5l1', 'title': 'An Appointment at the Health Centre',
   'context': u'นิสิตโทรนัดหมายที่ศูนย์สุขภาพของมหาวิทยาลัย',
   'turns': [
    ('W', 'f2', "University health centre, good morning."),
    ('M', 'm3', "Hello. I would like to make an appointment, but I am not sure which clinic I need."),
    ('W', 'f2', "Tell me what the problem is and I will point you in the right direction."),
    ('M', 'm3', "I have been getting headaches most afternoons for about three weeks. They started "
                "around the time I changed my glasses."),
    ('W', 'f2', "Then the first appointment should be with the optometrist rather than the general "
                "clinic. If the prescription is wrong, that is the likeliest cause and it is quick "
                "to check."),
    ('M', 'm3', "And if the glasses turn out to be fine?"),
    ('W', 'f2', "Then come back and we will book you into the general clinic, and the optometrist's "
                "report will already be on your file, which saves repeating everything."),
    ('M', 'm3', "That makes sense. When is the optometrist available?"),
    ('W', 'f2', "Thursday afternoon or Monday morning. Thursday has one slot left, at half past "
                "three."),
    ('M', 'm3', "I have a lab until four on Thursdays. Monday, please."),
   ],
   'questions': [
    {'q': 'What is the student’s symptom?',
     'o': ['Afternoon headaches for about three weeks.',
           'Blurred vision for three weeks.',
           'Headaches every morning.',
           'Pain since changing his timetable.'],
     'e': u'"getting headaches most afternoons for about three weeks"'},
    {'q': 'Why does the receptionist suggest the optometrist first?',
     'o': ['A wrong prescription is the most likely cause.',
           'The general clinic is fully booked.',
           'Students must see the optometrist first.',
           'The optometrist is cheaper.'],
     'e': u'"If the prescription is wrong, that is the likeliest cause and it is quick to check"'},
    {'q': 'Why does the student choose Monday?',
     'o': ['He has a class until four on Thursday.',
           'Monday is the only slot available.',
           'He wants an earlier appointment.',
           'The optometrist is away on Thursday.'],
     'e': u'"I have a lab until four on Thursdays" ส่วนคิวพฤหัสคือบ่ายสามครึ่ง'},
   ]},

  {'id': 'C5l2', 'title': 'Reviewing a Draft Report',
   'context': u'หัวหน้ากับพนักงานคุยกันเรื่องร่างรายงานที่ส่งมา',
   'turns': [
    ('M', 'm1', "I have read your draft. The analysis is sound, but I could not find the "
                "conclusion until page nine."),
    ('W', 'f1', "I put the background first so the reader has the context."),
    ('M', 'm1', "I understand the instinct, but consider who reads this. The committee members get "
                "forty pages the night before. Most of them will read your first page and skim the "
                "rest."),
    ('W', 'f1', "So the conclusion should be at the front."),
    ('M', 'm1', "The conclusion and the recommendation, in the first half page. Everything else "
                "becomes support for it."),
    ('W', 'f1', "Will that not look as though I have not done the work?"),
    ('M', 'm1', "The opposite. Only someone who has done the work can state the answer in three "
                "sentences. The background is still there for anyone who wants it, just not in "
                "front of the answer."),
    ('W', 'f1', "I will restructure it tonight."),
    ('M', 'm1', "Send it to me before you send it on. And keep the appendix exactly as it is, "
                "because that part is genuinely good."),
   ],
   'questions': [
    {'q': 'What is the manager’s main criticism?',
     'o': ['The conclusion appears too late in the report.',
           'The analysis contains errors.',
           'The report is too short.',
           'The appendix is unnecessary.'],
     'e': u'"I could not find the conclusion until page nine"'},
    {'q': 'Why does the manager say the structure matters?',
     'o': ['Readers will only read the first page carefully.',
           'The committee requires a fixed format.',
           'The report will be published.',
           'Background sections are not allowed.'],
     'e': u'"Most of them will read your first page and skim the rest"'},
    {'q': 'What does the manager say about the appendix?',
     'o': ['It should be left unchanged.',
           'It should be moved to the front.',
           'It should be shortened.',
           'It should be removed entirely.'],
     'e': u'"keep the appendix exactly as it is, because that part is genuinely good"'},
   ]},

  {'id': 'C5l3', 'title': 'Organising a Faculty Event',
   'context': u'สองคนวางแผนจัดงานเสวนาของคณะ',
   'turns': [
    ('W', 'f3', "We have the hall for the fourteenth. Now we need to decide the format."),
    ('M', 'm3', "Last year we had four speakers and almost no discussion. Students told us "
                "afterwards that it felt like four lectures in a row."),
    ('W', 'f3', "Then two speakers and a longer panel?"),
    ('M', 'm3', "That is what I would do. Twenty minutes each, then forty minutes of questions."),
    ('W', 'f3', "The risk with forty minutes of questions is silence. If nobody asks anything in "
                "the first two minutes, it dies."),
    ('M', 'm3', "Then we plant the first two questions with students we know, and we collect "
                "written questions at the door so the chair always has something to fall back on."),
    ('W', 'f3', "I like the written questions. It also helps the students who would never speak up "
                "in a room of two hundred."),
    ('M', 'm3', "Agreed. Can you speak to the two speakers this week? I will handle the room and "
                "the catering."),
   ],
   'questions': [
    {'q': 'What was wrong with last year’s event?',
     'o': ['There was too little discussion.',
           'Too few students attended.',
           'The speakers arrived late.',
           'The hall was too small.'],
     'e': u'"four speakers and almost no discussion … it felt like four lectures in a row"'},
    {'q': 'What risk does the woman identify?',
     'o': ['Nobody may ask questions.',
           'The speakers may talk too long.',
           'The hall may not be available.',
           'The event may cost too much.'],
     'e': u'"If nobody asks anything in the first two minutes, it dies"'},
    {'q': 'What advantage of written questions does the woman mention?',
     'o': ['They help students who would not speak up.',
           'They save time during the panel.',
           'They allow the speakers to prepare.',
           'They reduce the need for a chair.'],
     'e': u'"It also helps the students who would never speak up in a room of two hundred"'},
   ]},
 ],

 'mono': [
  {'id': 'C5m1', 'title': 'Reading a Cash Flow Statement',
   'context': u'คำบรรยายเรื่องวิธีอ่านงบกระแสเงินสดให้เห็นประเด็น',
   'turns': [
    ('Lecturer', 'm1',
     "The cash flow statement is the one students find dullest and analysts find most useful, and "
     "that gap is worth closing before you graduate. Today I want to give you three questions to "
     "ask of any cash flow statement, in order."),
    ('Lecturer', 'm1',
     "The first question. Is operating cash flow positive, and is it close to profit? A company "
     "that reports healthy profit while operating cash flow is negative is telling you that the "
     "profit is sitting in receivables or inventory rather than in the bank. That is not "
     "necessarily fraud. A fast-growing company looks exactly like this. But it is always worth "
     "an explanation."),
    ('Lecturer', 'm1',
     "The second question. What is paying for the investing section? If a firm is buying equipment "
     "out of its own operating cash, that is one story. If it is buying equipment out of new "
     "borrowing, year after year, that is a different story, and the second one has a limit."),
    ('Lecturer', 'm1',
     "The third question, and the one people skip. Look at the financing section and ask who is "
     "being paid. Dividends going out while borrowing goes up is a combination that deserves a "
     "question at the annual meeting, because in substance the company may be borrowing in order "
     "to pay its shareholders."),
    ('Lecturer', 'm1',
     "Three questions, in that order. You can apply them to any set of accounts in about four "
     "minutes, and they will tell you where to look in the notes. That is the whole skill: not "
     "reading everything, but knowing which page to turn to."),
   ],
   'questions': [
    {'q': 'What does the speaker say about profit with negative operating cash flow?',
     'o': ['It always deserves an explanation but is not always fraud.',
           'It is a certain sign of fraud.',
           'It is normal and needs no comment.',
           'It means the company is shrinking.'],
     'e': u'"That is not necessarily fraud … But it is always worth an explanation"'},
    {'q': 'What is the second question the speaker recommends?',
     'o': ['What is funding the investing section.',
           'Whether dividends have been paid.',
           'How large the cash balance is.',
           'Whether profit is rising.'],
     'e': u'"What is paying for the investing section?"'},
    {'q': 'Which combination does the speaker say deserves a question?',
     'o': ['Dividends being paid while borrowing increases.',
           'Equipment bought from operating cash.',
           'Operating cash flow close to profit.',
           'Borrowing repaid from operating cash.'],
     'e': u'"Dividends going out while borrowing goes up is a combination that deserves a question"'},
   ]},

  {'id': 'C5m2', 'title': 'Advice on Writing a CV',
   'context': u'ฝ่ายแนะแนวอาชีพให้คำแนะนำเรื่องการเขียนประวัติย่อ',
   'turns': [
    ('Speaker', 'f2',
     "I read about six hundred student CVs a year, and I am going to tell you the three things "
     "that separate the ones that get interviews from the ones that do not. None of them is about "
     "design."),
    ('Speaker', 'f2',
     "First, most students describe duties rather than results. Responsible for updating the "
     "customer database tells me nothing. Cleaned nine hundred duplicate records, which cut the "
     "monthly mailing cost by a fifth, tells me what you are like to work with. Same task, "
     "different sentence."),
    ('Speaker', 'f2',
     "Second, length. One page until you have five years of experience. I know you have more to "
     "say. Everyone does. The discipline of cutting is itself a signal, because the job will ask "
     "you to summarise things too, and the person reading has twelve applications and forty "
     "minutes."),
    ('Speaker', 'f2',
     "Third, and this is the one that costs students interviews without their ever knowing. If you "
     "send the same CV to twenty employers, it reads like a CV sent to twenty employers. You do "
     "not need to rewrite it each time. Reorder the bullet points so the most relevant three sit "
     "at the top, and change nothing else. That takes four minutes."),
    ('Speaker', 'f2',
     "We run CV clinics on Tuesdays and Thursdays. Bring a printed copy rather than a laptop, "
     "because we mark them up, and bring the advertisement for the job you actually want, because "
     "without it we can only give you general advice, and general advice is what you already have."),
   ],
   'questions': [
    {'q': 'What is the first mistake the speaker describes?',
     'o': ['Listing duties instead of results.',
           'Using an unattractive design.',
           'Including too little work experience.',
           'Writing in the wrong tense.'],
     'e': u'"most students describe duties rather than results"'},
    {'q': 'Why does the speaker insist on one page?',
     'o': ['The ability to cut is itself a signal to employers.',
           'Employers refuse longer documents.',
           'Students have little to say.',
           'Printing costs are high.'],
     'e': u'"The discipline of cutting is itself a signal"'},
    {'q': 'What should students bring to the CV clinic?',
     'o': ['A printed CV and the job advertisement.',
           'A laptop and a list of employers.',
           'A printed CV only.',
           'References from previous employers.'],
     'e': u'"Bring a printed copy rather than a laptop … and bring the advertisement for the job you actually want"'},
   ]},
 ],
}
