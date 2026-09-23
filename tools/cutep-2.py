# -*- coding: utf-8 -*-
u"""แบบฝึกฟังแนว CU-TEP · ชุดที่ 2 · โครงสร้างเดียวกับ tools/cutep-1.py"""

SET = {
 'id': 'C2', 'title': u'ชุดที่ 2',

 'short': [
  {'id': 'C2s01',
   'turns': [('W', 'f2', "Did you get a seat at the guest lecture?"),
             ('M', 'm1', "I got as far as the door.")],
   'q': 'What does the man mean?',
   'o': ['The lecture was too full to enter.',
         'He arrived exactly on time.',
         'He decided not to attend.',
         'He sat near the front.'],
   'e': u'ไปได้แค่ประตู แปลว่าเข้าไม่ได้เพราะคนเต็ม'},

  {'id': 'C2s02',
   'turns': [('M', 'm3', "Is Dr Suthep still taking on final-year projects?"),
             ('W', 'f1', "He took his last one in August.")],
   'q': 'What does the woman imply?',
   'o': ['He is no longer accepting projects.',
         'He accepts projects only in August.',
         'He has just started accepting projects.',
         'He supervises only one student a year.'],
   'e': u'his last one แปลว่ารับคนสุดท้ายไปแล้ว จึงไม่รับเพิ่ม'},

  {'id': 'C2s03',
   'turns': [('W', 'f3', "I am thinking of dropping the statistics elective."),
             ('M', 'm1', "You know it is the only one that counts towards the analytics minor.")],
   'q': 'What is the man doing?',
   'o': ['Warning her about a consequence.',
         'Agreeing with her decision.',
         'Offering to teach her statistics.',
         'Asking her to explain her reasons.'],
   'e': u'You know that... เป็นการเตือนถึงผลที่ตามมา ไม่ใช่การเห็นด้วย'},

  {'id': 'C2s04',
   'turns': [('M', 'm3', "The printer on the third floor is out of toner again."),
             ('W', 'f2', "Again? That is the second time this week.")],
   'q': 'How does the woman feel?',
   'o': ['Frustrated.', 'Amused.', 'Relieved.', 'Indifferent.'],
   'e': u'การทวนคำว่า Again? พร้อมนับจำนวนครั้ง แสดงความหงุดหงิด'},

  {'id': 'C2s05',
   'turns': [('W', 'f1', "Would you like me to book the meeting room for Monday?"),
             ('M', 'm1', "Let us wait until the client confirms.")],
   'q': 'What does the man suggest?',
   'o': ['Delaying the booking.', 'Booking a larger room.',
         'Cancelling the meeting.', 'Contacting a different client.'],
   'e': u'Let us wait until... คือการขอให้ชะลอไว้ก่อน'},

  {'id': 'C2s06',
   'turns': [('M', 'm3', "How long have you worked in the tax department?"),
             ('W', 'f3', "Long enough to know that April is not the month to take leave.")],
   'q': 'What can be inferred about the woman?',
   'o': ['She is experienced in the department.',
         'She has just joined the department.',
         'She is planning to take leave in April.',
         'She works in a different department now.'],
   'e': u'Long enough to know... แปลว่าอยู่มานานพอจะรู้จังหวะงาน'},

  {'id': 'C2s07',
   'turns': [('W', 'f2', "The canteen has raised its prices again."),
             ('M', 'm1', "I have started bringing lunch from home."),
             ('W', 'f2', "Perhaps I should do the same.")],
   'q': 'What will the woman probably do?',
   'o': ['Start bringing her own lunch.',
         'Complain to the canteen manager.',
         'Eat lunch at a different canteen.',
         'Skip lunch to save money.'],
   'e': u'Perhaps I should do the same คือมีแนวโน้มจะทำตาม'},

  {'id': 'C2s08',
   'turns': [('M', 'm1', "Have you finished the reconciliation?"),
             ('W', 'f1', "I would have, if the bank statement had arrived on Monday.")],
   'q': 'What does the woman mean?',
   'o': ['The statement arrived late, so she has not finished.',
         'She finished it on Monday.',
         'The bank sent the wrong statement.',
         'She does not need the statement.'],
   'e': u'I would have, if... เป็นรูปเงื่อนไขที่ไม่เป็นจริง แปลว่ายังทำไม่เสร็จเพราะเอกสารมาช้า'},

  {'id': 'C2s09',
   'turns': [('W', 'f3', "Shall I send the report to the whole committee?"),
             ('M', 'm3', "I would let the chair see it first.")],
   'q': 'What does the man recommend?',
   'o': ['Showing the report to one person before circulating it.',
         'Sending the report to everyone immediately.',
         'Rewriting the report before sending it.',
         'Presenting the report at the meeting instead.'],
   'e': u'ให้ประธานดูก่อน แล้วค่อยส่งให้ทุกคน'},

  {'id': 'C2s10',
   'turns': [('M', 'm1', "Excuse me, is this the queue for course registration?"),
             ('W', 'f2', "This is for fee payment. Registration is one floor up.")],
   'q': 'What will the man probably do next?',
   'o': ['Go up to the next floor.', 'Stay in the same queue.',
         'Pay his fees first.', 'Come back another day.'],
   'e': u'ต่อผิดแถว และได้รับบอกทางแล้ว จึงน่าจะขึ้นไปชั้นบน'},

  {'id': 'C2s11',
   'turns': [('W', 'f1', "Professor Chen marks very strictly, doesn't she?"),
             ('M', 'm3', "She marks fairly. There is a difference.")],
   'q': 'What does the man imply?',
   'o': ['The professor is demanding but not unfair.',
         'The professor marks too generously.',
         'He disagrees that the professor is strict at all.',
         'He has never been marked by the professor.'],
   'e': u'There is a difference คือการแก้คำว่าเข้มงวดให้เป็นยุติธรรม'},

  {'id': 'C2s12',
   'turns': [('M', 'm3', "Did the auditors finish at the warehouse yesterday?"),
             ('W', 'f3', "They are going back on Thursday.")],
   'q': 'What can be inferred?',
   'o': ['The work at the warehouse is not complete.',
         'The auditors finished ahead of schedule.',
         'The warehouse was closed yesterday.',
         'A different team will go on Thursday.'],
   'e': u'ต้องกลับไปอีก แปลว่ายังทำไม่เสร็จ'},

  {'id': 'C2s13',
   'turns': [('W', 'f2', "I have booked us on the eight o'clock train."),
             ('M', 'm1', "The meeting starts at nine, and the station is half an hour away.")],
   'q': 'What is the man concerned about?',
   'o': ['There may not be enough time.',
         'The train will be too expensive.',
         'The meeting may be cancelled.',
         'The station is difficult to find.'],
   'e': u'รถไฟแปดโมง เดินทางต่ออีกครึ่งชั่วโมง ประชุมเก้าโมง จึงเสี่ยงไม่ทัน'},

  {'id': 'C2s14',
   'turns': [('M', 'm1', "Are you applying for the exchange programme?"),
             ('W', 'f1', "My grades are fine, but the deadline was yesterday.")],
   'q': 'Why will the woman not apply?',
   'o': ['She missed the deadline.', 'Her grades are too low.',
         'She is not interested in the programme.',
         'She has already been accepted.'],
   'e': u'เกรดผ่าน แต่หมดเขตไปแล้วเมื่อวาน · ระวังตัวเลือกที่สลับเหตุผล'},

  {'id': 'C2s15',
   'turns': [('W', 'f3', "Could I borrow your notes from Tuesday?"),
             ('M', 'm3', "I was at the dentist on Tuesday.")],
   'q': 'What does the man mean?',
   'o': ['He does not have the notes.',
         'He will lend her the notes later.',
         'He lost his notes at the dentist.',
         'He took notes for her already.'],
   'e': u'ไม่ได้เข้าเรียนวันนั้น จึงไม่มีโน้ตให้ยืม'},
 ],

 'long': [
  {'id': 'C2l1', 'title': 'A Complaint About a Delivery',
   'context': u'ลูกค้าโทรร้องเรียนเรื่องสินค้าส่งผิด และเจ้าหน้าที่หาทางแก้',
   'turns': [
    ('M', 'm1', "Good afternoon, customer service. How can I help?"),
    ('W', 'f2', "I ordered forty office chairs last Monday, and thirty-eight arrived this morning. "
                "Two are missing and one of the ones that came is damaged."),
    ('M', 'm1', "I am sorry about that. Do you have the delivery note number?"),
    ('W', 'f2', "It is four two nine one. The driver did make a note of the damage, but he said I "
                "should call you about the missing ones."),
    ('M', 'm1', "He was right. I can see the order here. The two missing chairs were on a second "
                "van that had a breakdown, so they are still at the depot."),
    ('W', 'f2', "When can we expect them? We have a training session on Friday and we need the "
                "full set."),
    ('M', 'm1', "I can put them on tomorrow's route, which arrives before noon. The damaged one is "
                "different, though. A replacement has to come from the manufacturer, and that takes "
                "about ten days."),
    ('W', 'f2', "Ten days is no good for Friday."),
    ('M', 'm1', "Then let me send a loan chair with tomorrow's delivery, and we will swap it when "
                "the replacement arrives. You will not be charged for either."),
    ('W', 'f2', "That would work. Thank you."),
   ],
   'questions': [
    {'q': 'What is the woman’s main problem?',
     'o': ['Part of her order is missing and one item is damaged.',
           'The whole order arrived at the wrong address.',
           'She was charged for items she did not order.',
           'The delivery arrived a week late.'],
     'e': u'"thirty-eight arrived … Two are missing and one … is damaged"'},
    {'q': 'Why were two chairs not delivered?',
     'o': ['The van carrying them broke down.',
           'They were out of stock.',
           'The driver forgot them.',
           'They were damaged in transit.'],
     'e': u'"on a second van that had a breakdown, so they are still at the depot"'},
    {'q': 'How does the man solve the problem with the damaged chair?',
     'o': ['He will send a temporary replacement.',
           'He will refund the cost of the chair.',
           'He will deliver a new one before Friday.',
           'He will ask the manufacturer to repair it.'],
     'e': u'"let me send a loan chair … and we will swap it when the replacement arrives"'},
   ]},

  {'id': 'C2l2', 'title': 'Choosing a Dissertation Topic',
   'context': u'นิสิตปรึกษาอาจารย์เรื่องเลือกหัวข้อวิจัย',
   'turns': [
    ('W', 'f1', "So, you wanted to talk about narrowing your topic."),
    ('M', 'm3', "Yes. At the moment I have written down environmental reporting, which I know is "
                "far too broad."),
    ('W', 'f1', "It is. What drew you to it?"),
    ('M', 'm3', "I read that companies in the same industry report very different figures for the "
                "same kind of emissions, and nobody seems to be checking."),
    ('W', 'f1', "That is a much better starting point than the topic you wrote down. You are "
                "interested in comparability, and in who verifies the numbers."),
    ('M', 'm3', "Could I compare the reports of, say, twenty companies?"),
    ('W', 'f1', "You could, but twenty is a lot for one term. I would take eight, from two "
                "industries, and go deep rather than wide. A shallow comparison of twenty tells you "
                "less than a careful comparison of eight."),
    ('M', 'm3', "And where would I find the reports?"),
    ('W', 'f1', "They are public, but collecting them is slower than students expect. Start that "
                "this week, before you write a single word of the literature review."),
   ],
   'questions': [
    {'q': 'What is the student’s difficulty?',
     'o': ['His topic is too broad.',
           'He cannot find any data.',
           'He has missed the submission deadline.',
           'He disagrees with his supervisor.'],
     'e': u'"environmental reporting, which I know is far too broad"'},
    {'q': 'What does the supervisor say is the real interest behind his idea?',
     'o': ['Comparability and who verifies the figures.',
           'The environmental impact of industry.',
           'The cost of preparing reports.',
           'The history of reporting standards.'],
     'e': u'"You are interested in comparability, and in who verifies the numbers"'},
    {'q': 'What does the supervisor advise about the sample?',
     'o': ['Use fewer companies and study them in depth.',
           'Use twenty companies from one industry.',
           'Wait until next term to choose a sample.',
           'Use only companies that publish verified data.'],
     'e': u'"I would take eight, from two industries, and go deep rather than wide"'},
   ]},

  {'id': 'C2l3', 'title': 'Planning a Site Visit',
   'context': u'หัวหน้าทีมกับผู้ช่วยวางแผนการไปตรวจนับสินค้าที่โรงงาน',
   'turns': [
    ('M', 'm1', "We need to plan the inventory count at the Rayong plant. It is on the thirty-first."),
    ('W', 'f3', "That is a public holiday, isn't it?"),
    ('M', 'm1', "It is, which is exactly why they chose it. The lines stop, so nothing moves while "
                "we count."),
    ('W', 'f3', "How many of us will go?"),
    ('M', 'm1', "Four. Two in the raw materials store, two in finished goods. I would like you to "
                "take finished goods, because that is where the valuation issue was last year."),
    ('W', 'f3', "The slow-moving items?"),
    ('M', 'm1', "Yes. Last year we found stock from two seasons ago still carried at full cost. "
                "This time I want the ageing report printed and signed before we start counting, "
                "not afterwards."),
    ('W', 'f3', "Understood. Shall I ask them to send it in advance?"),
    ('M', 'm1', "Ask, but do not rely on it. Bring a laptop so you can pull it yourself if it is "
                "not ready when we arrive."),
   ],
   'questions': [
    {'q': 'Why is the count being held on a public holiday?',
     'o': ['Production stops, so stock does not move.',
           'The staff are paid more on that day.',
           'The auditors are unavailable on other days.',
           'The plant is closed for maintenance.'],
     'e': u'"The lines stop, so nothing moves while we count"'},
    {'q': 'Why does the man want the woman in finished goods?',
     'o': ['That area had a valuation problem last year.',
           'It is the largest part of the warehouse.',
           'She has counted there before.',
           'It is the easiest area to count.'],
     'e': u'"that is where the valuation issue was last year"'},
    {'q': 'What does the man insist on this year?',
     'o': ['Having the ageing report signed before counting begins.',
           'Counting finished goods twice.',
           'Sending more staff to the raw materials store.',
           'Starting the count a day earlier.'],
     'e': u'"I want the ageing report printed and signed before we start counting, not afterwards"'},
   ]},
 ],

 'mono': [
  {'id': 'C2m1', 'title': 'How Standards Get Written',
   'context': u'คำบรรยายเรื่องกระบวนการออกมาตรฐานการรายงานทางการเงิน',
   'turns': [
    ('Lecturer', 'f2',
     "People often talk about accounting standards as if they simply appear, handed down from "
     "somewhere. They do not. They are written by committees, in public, over several years, and "
     "understanding that process tells you a great deal about why the standards look the way they "
     "do."),
    ('Lecturer', 'f2',
     "A typical standard begins with a research phase, in which the board decides whether there is "
     "a problem worth solving at all. Then comes a discussion paper, which sets out possible "
     "approaches without recommending one. Only after that does the board publish an exposure "
     "draft, which is a proper draft standard, open for comment."),
    ('Lecturer', 'f2',
     "The comment period is the part students usually skip, and it is the most revealing. Anyone "
     "may write in. Preparers write in, auditors write in, investors write in, and so do trade "
     "associations. Those letters are published, which means you can read exactly who objected to "
     "what, and on what grounds."),
    ('Lecturer', 'f2',
     "Now, the reason this matters. When a final standard contains an exception that looks "
     "untidy, an exemption for a particular kind of transaction, say, that exception usually has a "
     "history. Somebody argued for it during the comment period, and the board judged the argument "
     "strong enough to accept."),
    ('Lecturer', 'f2',
     "So when you meet a rule that seems arbitrary, my advice is not to memorise it and move on. "
     "Go and find the basis for conclusions, which is published with every standard and explains "
     "why the board decided as it did. It is the least read document in our field and one of the "
     "most useful."),
   ],
   'questions': [
    {'q': 'What is the speaker’s main point?',
     'o': ['Standards are the product of a long public process.',
           'Standards change too often to be useful.',
           'Committees should have less influence on standards.',
           'Students should memorise standards carefully.'],
     'e': u'"They are written by committees, in public, over several years"'},
    {'q': 'What does the speaker say about the comment period?',
     'o': ['The letters are public and show who objected.',
           'Only auditors are allowed to comment.',
           'It usually lasts several years.',
           'The board rarely reads the comments.'],
     'e': u'"Those letters are published, which means you can read exactly who objected to what"'},
    {'q': 'What does the speaker advise students to do?',
     'o': ['Read the basis for conclusions.',
           'Memorise the exceptions first.',
           'Write to the board themselves.',
           'Ignore standards that seem arbitrary.'],
     'e': u'"Go and find the basis for conclusions … It is the least read document in our field"'},
   ]},

  {'id': 'C2m2', 'title': 'A Talk on Sleep and Study',
   'context': u'คำบรรยายสั้นเรื่องการนอนกับการเรียน สำหรับนิสิตช่วงสอบ',
   'turns': [
    ('Speaker', 'm3',
     "I have been asked to talk for ten minutes about sleep, which is not a subject students "
     "normally want to hear about in exam week. So let me put it in terms that might actually "
     "change what you do tonight."),
    ('Speaker', 'm3',
     "The common belief is that sleep is time taken away from studying. The research points the "
     "other way. A great deal of what we call learning happens after the studying stops, while you "
     "are asleep. The material you reviewed in the evening is reorganised overnight, and what "
     "survives that process is what you will still have in the exam hall."),
    ('Speaker', 'm3',
     "There is a practical consequence. Four hours of revision followed by seven hours of sleep "
     "will usually leave you with more than eight hours of revision followed by three. This is not "
     "encouragement to be lazy. It is a statement about where the return on your time is highest."),
    ('Speaker', 'm3',
     "The second point concerns caffeine. Its effect lasts far longer than most people assume, so "
     "a coffee at four in the afternoon is still working at ten at night. If you are lying awake "
     "wondering why, that is frequently the reason, and it is easy to fix."),
    ('Speaker', 'm3',
     "And the last point, which I will keep short. If you are revising and you notice that you "
     "have read the same paragraph three times, stop. You are no longer learning; you are only "
     "moving your eyes. Twenty minutes of sleep at that moment is worth more than two more hours "
     "at the desk. Thank you."),
   ],
   'questions': [
    {'q': 'What is the main idea of the talk?',
     'o': ['Sleep is part of learning rather than time lost.',
           'Students should study for longer hours.',
           'Caffeine improves exam performance.',
           'Revision is best done early in the morning.'],
     'e': u'"A great deal of what we call learning happens after the studying stops, while you are asleep"'},
    {'q': 'What does the speaker say about caffeine?',
     'o': ['Its effect lasts longer than people expect.',
           'It should be avoided completely.',
           'It helps memory during revision.',
           'It is harmless before the evening.'],
     'e': u'"Its effect lasts far longer than most people assume"'},
    {'q': 'What should a student do after reading the same paragraph three times?',
     'o': ['Stop and sleep.', 'Read it once more slowly.',
           'Switch to a different subject.', 'Make more detailed notes.'],
     'e': u'"stop … Twenty minutes of sleep at that moment is worth more than two more hours at the desk"'},
   ]},
 ],
}
