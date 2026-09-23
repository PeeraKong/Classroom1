# -*- coding: utf-8 -*-
u"""แบบฝึกฟังแนว CU-TEP · ชุดที่ 4 · โครงสร้างเดียวกับ tools/cutep-1.py"""

SET = {
 'id': 'C4', 'title': u'ชุดที่ 4',

 'short': [
  {'id': 'C4s01',
   'turns': [('W', 'f1', "Are you taking the eight o'clock class next term?"),
             ('M', 'm3', "I have seen what eight o'clock does to my attendance.")],
   'q': 'What does the man mean?',
   'o': ['He will avoid the early class.',
         'He always attends early classes.',
         'He has not decided yet.',
         'He prefers morning classes.'],
   'e': u'รู้ว่าคาบเช้าทำให้ตัวเองขาดเรียน จึงเลี่ยง'},

  {'id': 'C4s02',
   'turns': [('M', 'm1', "The supplier quoted us ninety thousand."),
             ('W', 'f2', "That is before tax and delivery, I assume.")],
   'q': 'What is the woman doing?',
   'o': ['Checking what the quoted figure covers.',
         'Agreeing that the price is reasonable.',
         'Suggesting a different supplier.',
         'Offering to negotiate the price.'],
   'e': u'I assume เป็นการยืนยันความเข้าใจว่าราคานั้นรวมอะไรบ้าง'},

  {'id': 'C4s03',
   'turns': [('W', 'f3', "Did Sarah enjoy her placement in Singapore?"),
             ('M', 'm3', "She has applied to go back.")],
   'q': 'What does the man imply?',
   'o': ['Sarah had a good experience.',
         'Sarah did not complete the placement.',
         'Sarah has not returned yet.',
         'Sarah prefers to work in Thailand.'],
   'e': u'สมัครกลับไปอีก เป็นการตอบทางอ้อมว่าชอบ'},

  {'id': 'C4s04',
   'turns': [('M', 'm1', "I cannot open the spreadsheet you sent."),
             ('W', 'f1', "Which version of the software are you running?")],
   'q': 'What does the woman think may be the problem?',
   'o': ['The man’s software may be out of date.',
         'The file was never sent.',
         'The file is too large to open.',
         'The man typed the password wrongly.'],
   'e': u'ถามรุ่นของโปรแกรม แสดงว่าสงสัยเรื่องความเข้ากันได้ของเวอร์ชัน'},

  {'id': 'C4s05',
   'turns': [('W', 'f2', "Shall we include last year's comparatives in the handout?"),
             ('M', 'm3', "The whole point of the meeting is the trend.")],
   'q': 'What does the man mean?',
   'o': ['The comparatives are essential.',
         'The comparatives should be left out.',
         'The meeting should be postponed.',
         'The handout is already too long.'],
   'e': u'ถ้าประเด็นคือแนวโน้ม ก็ต้องมีตัวเลขปีก่อนไว้เทียบ'},

  {'id': 'C4s06',
   'turns': [('M', 'm1', "Do you know where the fire assembly point is?"),
             ('W', 'f3', "It moved when they started building the new wing.")],
   'q': 'What can be inferred?',
   'o': ['The assembly point is no longer in its old place.',
         'There is no assembly point at present.',
         'The new wing is already finished.',
         'The woman does not know the answer.'],
   'e': u'It moved... แปลว่าย้ายที่แล้ว ไม่ได้แปลว่าไม่มี'},

  {'id': 'C4s07',
   'turns': [('W', 'f1', "Professor Nara wants the assignment in hard copy."),
             ('M', 'm3', "Since when?"),
             ('W', 'f1', "Since two people submitted the same file last term.")],
   'q': 'Why did the professor change the rule?',
   'o': ['Because of a suspected case of copying.',
         'Because the online system failed.',
         'Because students asked for it.',
         'Because printing is cheaper.'],
   'e': u'สองคนส่งไฟล์เดียวกัน เป็นเหตุให้สงสัยการลอก'},

  {'id': 'C4s08',
   'turns': [('M', 'm1', "The train leaves at six forty."),
             ('W', 'f2', "Six forty? I thought we had until seven.")],
   'q': 'How does the woman feel?',
   'o': ['Surprised that there is less time than she thought.',
         'Pleased that the train is later than expected.',
         'Annoyed that the man is late.',
         'Confident that they will catch the train.'],
   'e': u'การทวนเวลาพร้อม I thought... แสดงความประหลาดใจว่าเวลาน้อยกว่าที่คิด'},

  {'id': 'C4s09',
   'turns': [('W', 'f3', "Can I take the depreciation schedule home to finish?"),
             ('M', 'm1', "Client files do not leave the office.")],
   'q': 'What does the man mean?',
   'o': ['She is not permitted to take the file.',
         'She should finish the work tomorrow.',
         'The schedule is already complete.',
         'She may take a copy instead.'],
   'e': u'เป็นการบอกกฎ ซึ่งเท่ากับปฏิเสธคำขอ'},

  {'id': 'C4s10',
   'turns': [('M', 'm3', "How many people replied to the survey?"),
             ('W', 'f1', "Ninety-one out of four hundred.")],
   'q': 'What can be concluded about the survey?',
   'o': ['The response rate was low.',
         'Most people responded.',
         'The sample was too large.',
         'The survey was sent twice.'],
   'e': u'91 จาก 400 คือราวยี่สิบสามเปอร์เซ็นต์ ซึ่งถือว่าตอบกลับน้อย'},

  {'id': 'C4s11',
   'turns': [('W', 'f2', "I have put you down for the Monday presentation."),
             ('M', 'm3', "I fly back on Monday morning.")],
   'q': 'What is the man indicating?',
   'o': ['Monday may not be suitable for him.',
         'He is happy to present on Monday.',
         'He will cancel his flight.',
         'He has already presented.'],
   'e': u'บินกลับเช้าวันนั้น จึงเป็นการบอกทางอ้อมว่าอาจไม่สะดวก'},

  {'id': 'C4s12',
   'turns': [('M', 'm1', "Is the new policy easier to understand than the old one?"),
             ('W', 'f3', "It is shorter.")],
   'q': 'What does the woman imply?',
   'o': ['Being shorter does not make it clearer.',
         'The new policy is much clearer.',
         'The old policy was shorter.',
         'She has not read the new policy.'],
   'e': u'ตอบเลี่ยงคำว่าเข้าใจง่าย โดยพูดถึงความสั้นแทน เป็นการไม่เห็นด้วยอย่างสุภาพ'},

  {'id': 'C4s13',
   'turns': [('W', 'f1', "Shall I chase the confirmation from the lawyer?"),
             ('M', 'm3', "She replied while you were at lunch.")],
   'q': 'What does the man mean?',
   'o': ['No further chasing is needed.',
         'The lawyer has still not replied.',
         'The woman should call after lunch.',
         'He will contact the lawyer himself.'],
   'e': u'ตอบกลับมาแล้ว จึงไม่ต้องตามอีก'},

  {'id': 'C4s14',
   'turns': [('M', 'm1', "This is the third time the system has crashed today."),
             ('W', 'f2', "They are migrating the servers this week.")],
   'q': 'What is the woman doing?',
   'o': ['Explaining the likely cause.',
         'Apologising for the problem.',
         'Denying that there is a problem.',
         'Suggesting he restart the system.'],
   'e': u'ให้ข้อมูลว่ากำลังย้ายเซิร์ฟเวอร์ ซึ่งอธิบายสาเหตุ'},

  {'id': 'C4s15',
   'turns': [('W', 'f3', "Everyone in the team agreed with the proposal."),
             ('M', 'm3', "Was Kittipong at that meeting?")],
   'q': 'What does the man imply?',
   'o': ['Not everyone may have been consulted.',
         'Kittipong wrote the proposal.',
         'He agrees with the proposal.',
         'The meeting lasted too long.'],
   'e': u'ถามว่าคนนั้นอยู่ไหม เป็นการตั้งข้อสงสัยกับคำว่าทุกคนเห็นด้วย'},
 ],

 'long': [
  {'id': 'C4l1', 'title': 'Setting Up a Bank Account',
   'context': u'นิสิตต่างชาติเปิดบัญชีธนาคารและถามเงื่อนไข',
   'turns': [
    ('M', 'm1', "Good morning. I would like to open a student account."),
    ('W', 'f2', "Certainly. May I see your passport and your student card?"),
    ('M', 'm1', "Here they are. I also have my rental agreement if you need proof of address."),
    ('W', 'f2', "That is helpful, thank you. Most people arrive without it and have to come back. "
                "Now, the student account has no monthly fee while you are enrolled, and the "
                "minimum opening deposit is five hundred baht."),
    ('M', 'm1', "Is there a limit on transfers?"),
    ('W', 'f2', "Domestic transfers are unlimited. International transfers are capped at fifty "
                "thousand baht a day until the account has been open for six months."),
    ('M', 'm1', "My family sends money from abroad. Would that be affected?"),
    ('W', 'f2', "Incoming transfers are not limited, only outgoing. So you will be fine."),
    ('M', 'm1', "And the card?"),
    ('W', 'f2', "The debit card is printed here and ready in about twenty minutes. The mobile app "
                "needs a Thai phone number, so if you do not have one yet, come back once you do "
                "and we will activate it in two minutes."),
   ],
   'questions': [
    {'q': 'What does the woman say most applicants forget to bring?',
     'o': ['Proof of address.', 'Their passport.',
           'The opening deposit.', 'A Thai phone number.'],
     'e': u'"Most people arrive without it and have to come back" · หมายถึงหลักฐานที่อยู่'},
    {'q': 'What limit applies during the first six months?',
     'o': ['A daily cap on outgoing international transfers.',
           'A cap on all transfers.',
           'A limit on incoming transfers from abroad.',
           'A monthly fee on the account.'],
     'e': u'"International transfers are capped at fifty thousand baht a day … Incoming transfers are not limited, only outgoing"'},
    {'q': 'What must the man do before using the mobile app?',
     'o': ['Obtain a Thai phone number.', 'Deposit a larger amount.',
           'Wait six months.', 'Collect a different card.'],
     'e': u'"The mobile app needs a Thai phone number"'},
   ]},

  {'id': 'C4l2', 'title': 'Preparing for a Presentation',
   'context': u'อาจารย์ให้คำแนะนำนิสิตก่อนนำเสนองาน',
   'turns': [
    ('W', 'f1', "You wanted me to look at your slides before Thursday."),
    ('M', 'm3', "Yes. I have thirty-two, and I think that is too many for twelve minutes."),
    ('W', 'f1', "It is roughly three times too many. But the number is the symptom, not the "
                "problem. What is the one sentence you want the audience to remember?"),
    ('M', 'm3', "That small firms are dropping the audit exemption voluntarily because their banks "
                "ask for audited accounts."),
    ('W', 'f1', "Good. That is clear. Now, how many of your thirty-two slides are needed to "
                "establish that sentence?"),
    ('M', 'm3', "Maybe eight."),
    ('W', 'f1', "Then build the talk from those eight and put the rest in an appendix. If somebody "
                "asks, you can bring a slide up. If nobody asks, you have lost nothing."),
    ('M', 'm3', "What about the methodology? I spent a lot of time on it."),
    ('W', 'f1', "One slide, and be ready to defend it in questions. The effort you spent is not "
                "wasted because it appears on screen; it is wasted if it crowds out your finding."),
   ],
   'questions': [
    {'q': 'What does the tutor say is the real problem?',
     'o': ['The talk lacks a clear central message.',
           'The slides are badly designed.',
           'The student has not done enough research.',
           'The presentation time is too short.'],
     'e': u'"the number is the symptom, not the problem" แล้วถามหาประโยคเดียวที่อยากให้จำ'},
    {'q': 'What does the tutor suggest doing with the extra slides?',
     'o': ['Move them to an appendix.', 'Delete them entirely.',
           'Use them in a second presentation.', 'Hand them out on paper.'],
     'e': u'"put the rest in an appendix … If somebody asks, you can bring a slide up"'},
    {'q': 'What does the tutor say about the methodology?',
     'o': ['Cover it briefly and defend it in questions.',
           'Present it in detail at the start.',
           'Leave it out of the talk completely.',
           'Rewrite it before Thursday.'],
     'e': u'"One slide, and be ready to defend it in questions"'},
   ]},

  {'id': 'C4l3', 'title': 'A Disagreement Over an Estimate',
   'context': u'ผู้สอบบัญชีคุยกับผู้จัดการฝ่ายบัญชีของลูกค้าเรื่องค่าเผื่อหนี้สงสัยจะสูญ',
   'turns': [
    ('M', 'm1', "I wanted to talk about the allowance for doubtful debts before we finalise."),
    ('W', 'f3', "You think it is too low."),
    ('M', 'm1', "I think it needs more support. You have provided four hundred thousand against a "
                "receivables balance where two point one million is over ninety days."),
    ('W', 'f3', "Those older balances are almost all with two customers we have dealt with for "
                "fifteen years. They always pay, just slowly."),
    ('M', 'm1', "That is a reasonable argument, and if the history supports it I am content. What I "
                "need is the evidence. Can you show me what those two customers paid in the last "
                "three years, and how late?"),
    ('W', 'f3', "I can pull that from the ledger."),
    ('M', 'm1', "Then let us do that. If the pattern is consistent, your four hundred thousand may "
                "well be right and I will say so in the file. If one of them has been getting "
                "slower each year, we should talk again."),
    ('W', 'f3', "That is fair. I will have it by Wednesday."),
   ],
   'questions': [
    {'q': 'What is the auditor’s concern?',
     'o': ['The allowance is not sufficiently supported.',
           'The receivables balance is overstated.',
           'The client has two customers only.',
           'The ledger has not been reconciled.'],
     'e': u'"I think it needs more support" · ไม่ได้บอกว่าผิด แต่ยังไม่มีหลักฐานพอ'},
    {'q': 'What is the accountant’s justification?',
     'o': ['The customers are long-standing and always pay eventually.',
           'The balances have already been written off.',
           'The amounts are too small to matter.',
           'The auditors agreed the figure last year.'],
     'e': u'"They always pay, just slowly"'},
    {'q': 'What do they agree to do?',
     'o': ['Examine the two customers’ payment history.',
           'Increase the allowance immediately.',
           'Refer the matter to the partner.',
           'Delay finalising until next year.'],
     'e': u'"show me what those two customers paid in the last three years, and how late"'},
   ]},
 ],

 'mono': [
  {'id': 'C4m1', 'title': 'What Internal Control Cannot Do',
   'context': u'คำบรรยายเรื่องข้อจำกัดของระบบควบคุมภายใน',
   'turns': [
    ('Lecturer', 'f2',
     "We have spent two weeks on what internal control does. Today I want to spend one session on "
     "what it cannot do, because a student who only knows the first half will give confident wrong "
     "answers in practice."),
    ('Lecturer', 'f2',
     "Start with the obvious limit. Controls cost money. A control that costs more than the loss "
     "it prevents is not prudent, it is wasteful, and boards are entitled to decide that a small "
     "risk is cheaper to accept than to control. So the absence of a control is not automatically a "
     "failure."),
    ('Lecturer', 'f2',
     "The second limit is collusion. Almost every control you will design assumes that two people "
     "who must both approve something are acting independently. If they agree to cooperate, the "
     "control produces exactly the same paperwork as if it had worked. The documents look perfect, "
     "which is why collusion is so hard to detect from the file alone."),
    ('Lecturer', 'f2',
     "The third and most important limit is management override. Controls are designed to govern "
     "the behaviour of staff. But the people who design the system, and who can authorise an "
     "exception to it, are management themselves. A system cannot easily constrain the people who "
     "hold the pen that wrote it."),
    ('Lecturer', 'f2',
     "This is why you will hear repeatedly that controls give reasonable assurance and never "
     "absolute assurance. It is not a legal hedge. It is an accurate description of three real "
     "limits, and if you can name those three in an exam you will have answered most of what this "
     "topic asks."),
   ],
   'questions': [
    {'q': 'Why does the speaker say the absence of a control may be acceptable?',
     'o': ['The control may cost more than the loss it prevents.',
           'Small risks never cause losses.',
           'Auditors rarely test small controls.',
           'Staff dislike too many controls.'],
     'e': u'"A control that costs more than the loss it prevents is not prudent, it is wasteful"'},
    {'q': 'Why is collusion difficult to detect?',
     'o': ['The paperwork looks exactly as it should.',
           'It usually involves senior management.',
           'It leaves no documents at all.',
           'It happens outside working hours.'],
     'e': u'"the control produces exactly the same paperwork as if it had worked"'},
    {'q': 'What does the speaker call the most important limit?',
     'o': ['Management override.', 'Cost versus benefit.',
           'Collusion between staff.', 'Human error.'],
     'e': u'"The third and most important limit is management override"'},
   ]},

  {'id': 'C4m2', 'title': 'A Museum Tour Introduction',
   'context': u'ไกด์แนะนำก่อนเริ่มนำชมพิพิธภัณฑ์',
   'turns': [
    ('Guide', 'm3',
     "Good morning and welcome. The tour takes about seventy minutes, and I will keep us moving, "
     "because the building closes to tour groups at four and the last room is the one most people "
     "want time in."),
    ('Guide', 'm3',
     "A word about photography. You may photograph anything in the ground floor galleries without "
     "flash. On the first floor, where the textiles are, photography is not permitted at all, and "
     "that is a conservation rule rather than a copyright one. Light damages dye, and the damage "
     "does not reverse."),
    ('Guide', 'm3',
     "The collection is arranged by material rather than by date, which surprises visitors who "
     "expect a timeline. Ceramics are together, metalwork is together, textiles are together. The "
     "reason is that the founder was a maker himself and wanted visitors to see how one craft "
     "developed, rather than what happened to be produced in a particular century."),
    ('Guide', 'm3',
     "If you lose the group, do not search for us. Go back to the entrance hall and wait by the "
     "desk. We pass through it twice, and the staff there can tell you where we are. Searching "
     "corridor by corridor is how people miss the whole tour."),
    ('Guide', 'm3',
     "One last thing. There is a temporary exhibition in the basement which is not included in "
     "this ticket, but your ticket gives you a reduced rate if you want to see it afterwards. Ask "
     "at the desk on your way down. Right, if everyone is ready, we will start in the ceramics "
     "room."),
   ],
   'questions': [
    {'q': 'Why does the guide say he will keep the group moving?',
     'o': ['The building closes to tour groups at four.',
           'The tour is longer than seventy minutes.',
           'Another group is waiting to start.',
           'The first room takes the longest.'],
     'e': u'"the building closes to tour groups at four and the last room is the one most people want time in"'},
    {'q': 'Why is photography banned on the first floor?',
     'o': ['Light causes permanent damage to the textiles.',
           'The works are protected by copyright.',
           'The room is too crowded for cameras.',
           'The lighting is too poor for photographs.'],
     'e': u'"that is a conservation rule rather than a copyright one. Light damages dye"'},
    {'q': 'What should visitors do if they lose the group?',
     'o': ['Wait at the entrance hall desk.',
           'Search the corridors for the guide.',
           'Go to the basement exhibition.',
           'Leave the building and wait outside.'],
     'e': u'"Go back to the entrance hall and wait by the desk"'},
   ]},
 ],
}
