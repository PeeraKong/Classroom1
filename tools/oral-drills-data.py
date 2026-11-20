# -*- coding: utf-8 -*-
u"""แบบฝึกตามรูปแบบข้อสอบจริงของวิชาภาษาอังกฤษเพื่อการสื่อสาร

อิงรูปแบบจากแบบฝึกของรายวิชาสามแบบ

  เติมคำจากกล่อง      แบบ Exercise 1 และ Exercise 2
                      คลังคำมีจำนวนเท่าช่องว่างพอดี ใช้ครบทุกคำ ไม่มีคำเกิน
  โครง SAR+L          แบบ Task 11 · คำตอบคำถามเชิงพฤติกรรมแบ่งเป็นสี่ช่อง
                      Situation · Action · Result · Lesson แล้วเติมวลีลงช่องว่าง
  โครง Three S's      แบบ Part D · คำตอบคำถาม Tell me about yourself
                      แบ่งเป็น SUCCESS · STRENGTH · SITUATION ยาวราวหนึ่งนาทีครึ่ง

ต่างจากแบบฝึกเดิมในหน้า final-prep.html ตรงที่แบบฝึกชุดนี้
เติม<วลียาว>ลงใน<โครงคำตอบ> ไม่ใช่เติมคำเดี่ยวลงในประโยค
จุดประสงค์คือให้เห็นรูปร่างของคำตอบที่ดีทั้งก้อน ก่อนจะไปพูดเอง

ทุกกิจการ ทุกชื่อบุคคล และทุกตัวเลขสมมุติขึ้นใหม่ทั้งหมด
"""

GROUPS = [
    ('signpost', u'เติมคำ · ภาษาการนำเสนอ',
     u'เติมคำลงช่องว่างด้วยคำจากคลังคำ · ใช้ครบทุกคำ คำละครั้ง'),
    ('prep', u'เติมคำ · คำบุพบท',
     u'เติมคำบุพบทลงช่องว่างด้วยคำจากคลังคำ · ใช้ครบทุกคำ คำละครั้ง'),
    ('sarl', u'โครง SAR+L · คำถามเชิงพฤติกรรม',
     u'เติมวลีลงช่องว่างในคำตอบ · Situation คือสถานการณ์ · Action คือสิ่งที่ลงมือทำ · '
     u'Result คือผลที่เกิด · Lesson คือบทเรียนและการนำไปใช้'),
    ('three', u"โครง Three S's · Tell me about yourself",
     u'เติมวลีลงช่องว่างในคำตอบ · SUCCESS คือผลงานที่ผ่านมา · STRENGTH คือจุดแข็ง · '
     u'SITUATION คือโยงกลับมาที่ตำแหน่งที่สมัคร'),
]


DRILLS = [

# ══════════════════ เติมคำ · ภาษาการนำเสนอ ══════════════════
{'id': 'sp1', 'group': 'signpost', 'title': u'ชุดที่ 1 · เปิดการนำเสนอและวางโครง',
 'box': ['all', 'areas', 'divided', 'finally', 'parts', 'second', 'start', 'then'],
 'blocks': [
  {'label': '1', 't': "I'll [[1]] by outlining the agenda for this morning. [[2]] I'll present "
                      "the quarterly figures. [[3]], I'll suggest three actions for the board."},
  {'label': '2', 't': "I've [[4]] my talk into three [[5]]. First of [[6]], I'll explain why we "
                      "ran the pilot in the first place."},
  {'label': '3', 't': "I'll cover two main [[7]] today: first, staffing; and [[8]], the budget "
                      "for next year."},
 ],
 'ans': {1: 'start', 2: 'then', 3: 'finally', 4: 'divided', 5: 'parts', 6: 'all',
         7: 'areas', 8: 'second'},
 'exp': {1: u'<b>I’ll start by</b> + กริยาเติม ing คือจะเริ่มด้วยการ',
         2: u'<b>then</b> เชื่อมลำดับถัดไป · วางต้นประโยคได้',
         3: u'<b>finally</b> บอกว่าเป็นส่วนสุดท้าย',
         4: u'<b>divide a talk into parts</b> คือแบ่งการนำเสนอออกเป็นส่วน',
         5: u'<b>parts</b> ต้องเป็นพหูพจน์เพราะมี three นำหน้า',
         6: u'<b>first of all</b> เป็นวลีตายตัว แปลว่าอย่างแรกสุด',
         7: u'<b>areas</b> คือด้านหรือประเด็นที่จะพูดถึง · two main areas',
         8: u'<b>second</b> คู่กับ first ที่อยู่ข้างหน้า'}},

{'id': 'sp2', 'group': 'signpost', 'title': u'ชุดที่ 2 · เชื่อมระหว่างส่วน และปิดท้าย',
 'box': ['brings', 'conclusion', 'go', 'look', 'move', 'recap', 'summarise', 'turn'],
 'blocks': [
  {'label': '1', 't': "That [[1]] me to the end of the first part. Let me now [[2]] to the costs."},
  {'label': '2', 't': "I'd like to [[3]] on to my second point, and then [[4]] at the timeline "
                      "in more detail."},
  {'label': '3', 't': "To [[5]], then: costs are down and output is up. In [[6]], I recommend "
                      "that we extend the pilot for another quarter."},
  {'label': '4', 't': "Before I finish, let me [[7]] the three points. After that I'll [[8]] on "
                      "to your questions."},
 ],
 'ans': {1: 'brings', 2: 'turn', 3: 'move', 4: 'look', 5: 'summarise', 6: 'conclusion',
         7: 'recap', 8: 'go'},
 'exp': {1: u'<b>that brings me to</b> คือพามาถึง · ประธานเป็น that จึงเติม s',
         2: u'<b>turn to</b> คือหันไปพูดเรื่องถัดไป',
         3: u'<b>move on to</b> คือข้ามไปประเด็นถัดไป',
         4: u'<b>look at</b> คือพิจารณา · ต่อจาก then จึงเป็นรูปเดิมไม่เติมอะไร',
         5: u'<b>to summarise</b> ขึ้นต้นการสรุป',
         6: u'<b>in conclusion</b> เป็นวลีตายตัว ใช้ปิดท้าย',
         7: u'<b>recap</b> คือทบทวนสิ่งที่พูดไปแล้วอย่างย่อ',
         8: u'<b>go on to</b> คือไปต่อยังสิ่งถัดไป'}},

{'id': 'sp3', 'group': 'signpost', 'title': u'ชุดที่ 3 · คำถาม สื่อประกอบ และผู้ฟัง',
 'box': ['chart', 'feel', 'handouts', 'interrupt', 'questions', 'raise', 'screen', 'welcome'],
 'blocks': [
  {'label': '1', 't': "Please don't [[1]] me during the presentation; there'll be plenty of time "
                      "for [[2]] at the end."},
  {'label': '2', 't': "If anything is unclear, please [[3]] your hand and I'll come back to it. "
                      "Do [[4]] free to stop me if you can't read a figure."},
  {'label': '3', 't': "As you can see on the [[5]], sales rose sharply in the third quarter. "
                      "This [[6]] shows the same data broken down by region."},
  {'label': '4', 't': "I've put all the key figures on the [[7]]. You're [[8]] to take one on "
                      "your way out."},
 ],
 'ans': {1: 'interrupt', 2: 'questions', 3: 'raise', 4: 'feel', 5: 'screen', 6: 'chart',
         7: 'handouts', 8: 'welcome'},
 'exp': {1: u'<b>interrupt</b> คือขัดจังหวะ · don’t + กริยารูปเดิม',
         2: u'<b>time for questions</b> คือช่วงถามตอบ',
         3: u'<b>raise your hand</b> คือยกมือ',
         4: u'<b>do feel free to</b> คือเชิญตามสบาย · do ข้างหน้าใช้เน้น',
         5: u'<b>on the screen</b> คือบนจอ',
         6: u'<b>chart</b> คือแผนภูมิ · this chart ชี้ไปยังภาพที่เพิ่งพูดถึง',
         7: u'<b>handouts</b> คือเอกสารแจก · ใช้พหูพจน์เพราะแจกหลายชุด',
         8: u'<b>you’re welcome to</b> คือเชิญได้เลย ต่างจาก you’re welcome ที่แปลว่าไม่เป็นไร'}},

{'id': 'sp4', 'group': 'signpost', 'title': u'ชุดที่ 4 · เปิดการนำเสนอตามแนว WISEOWL',
 'box': ['about', 'delighted', 'divided', 'familiar', 'importance', 'known', 'outline', 'take'],
 'blocks': [
  {'label': '1', 't': "Good morning, everyone. I'm [[1]] that so many of you could make it today."},
  {'label': '2', 't': "For those of you who don't know me, I'm Kanya, and I'm responsible for "
                      "quality control. My talk today is [[2]] our new inspection process."},
  {'label': '3', 't': "By the end of this talk, you'll be [[3]] with the three stages of the "
                      "process and the [[4]] of each one."},
  {'label': '4', 't': "I've [[5]] my presentation into three parts, and I'll [[6]] them for you "
                      "now."},
  {'label': '5', 't': "My presentation will [[7]] about fifteen minutes. Some of the results "
                      "I'll show you are not widely [[8]] yet."},
 ],
 'ans': {1: 'delighted', 2: 'about', 3: 'familiar', 4: 'importance', 5: 'divided',
         6: 'outline', 7: 'take', 8: 'known'},
 'exp': {1: u'<b>I’m delighted that…</b> ใช้ทักทายในขั้น W คือ Welcome',
         2: u'<b>my talk is about…</b> คือหัวข้อที่จะพูด ตรงกับขั้น S คือ State your topic',
         3: u'<b>be familiar with</b> คือคุ้นเคยกับ · บอกว่าผู้ฟังจะได้อะไร ตรงกับขั้น E คือ Explain',
         4: u'<b>importance</b> เป็นคำนาม ตามหลัง the ได้ · the importance of each one',
         5: u'<b>divided…into three parts</b> ตรงกับขั้น O คือ Outline',
         6: u'<b>outline</b> ใช้เป็นกริยาได้ แปลว่าบอกเค้าโครง',
         7: u'<b>take + ช่วงเวลา</b> คือใช้เวลาเท่าไร ตรงกับขั้น L คือ Let the audience know',
         8: u'<b>widely known</b> คือเป็นที่รู้กันทั่วไป · ใช้รูป passive หลัง verb to be'}},

# ══════════════════ เติมคำ · คำบุพบท ══════════════════
{'id': 'pp1', 'group': 'prep', 'title': u'ชุดที่ 1 · บุพบทในการนำเสนอ',
 'box': ['about', 'at', 'for', 'into', 'of', 'on', 'to', 'with'],
 'blocks': [
  {'label': '1', 't': "Thanks [[1]] making time for us at such short notice."},
  {'label': '2', 't': "Let me begin [[2]] a quick summary of where we are now."},
  {'label': '3', 't': "I'll split the next section [[3]] two halves."},
  {'label': '4', 't': "I'd like to draw your attention [[4]] the figures on the left."},
  {'label': '5', 't': "This slide gives you a picture [[5]] our market share."},
  {'label': '6', 't': "Let's take a closer look [[6]] the second quarter."},
  {'label': '7', 't': "In part two I'll concentrate [[7]] what went wrong."},
  {'label': '8', 't': "I won't say much [[8]] the technical details today."},
 ],
 'ans': {1: 'for', 2: 'with', 3: 'into', 4: 'to', 5: 'of', 6: 'at', 7: 'on', 8: 'about'},
 'exp': {1: u'<b>thanks for</b> + กริยาเติม ing',
         2: u'<b>begin with</b> คือเริ่มด้วย',
         3: u'<b>split something into</b> คือแบ่งออกเป็น',
         4: u'<b>draw attention to</b> คือทำให้สนใจไปที่',
         5: u'<b>a picture of</b> คือภาพของ',
         6: u'<b>take a look at</b> เป็นวลีตายตัว',
         7: u'<b>concentrate on</b> คือมุ่งความสนใจไปที่',
         8: u'<b>say much about</b> คือพูดถึงมากเกี่ยวกับ'}},

{'id': 'pp2', 'group': 'prep', 'title': u'ชุดที่ 2 · บุพบทในการสัมภาษณ์งาน',
 'box': ['as', 'at', 'for', 'from', 'in', 'of', 'to', 'with'],
 'blocks': [
  {'label': '1', 't': "I graduated [[1]] Chulalongkorn University in 2025."},
  {'label': '2', 't': "I worked [[2]] an intern at a logistics company last summer."},
  {'label': '3', 't': "I'm interested [[3]] a career in corporate finance."},
  {'label': '4', 't': "I'm good [[4]] explaining numbers to people outside finance."},
  {'label': '5', 't': "I was responsible [[5]] preparing the weekly cash position."},
  {'label': '6', 't': "I reported directly [[6]] the finance manager."},
  {'label': '7', 't': "I have two years [[7]] part-time experience in accounting."},
  {'label': '8', 't': "I enjoy working [[8]] people from different backgrounds."},
 ],
 'ans': {1: 'from', 2: 'as', 3: 'in', 4: 'at', 5: 'for', 6: 'to', 7: 'of', 8: 'with'},
 'exp': {1: u'<b>graduate from</b> + ชื่อสถาบัน · ถ้าเป็นสาขาใช้ graduate in',
         2: u'<b>work as</b> + ตำแหน่ง คือทำงานในฐานะ',
         3: u'<b>be interested in</b> คือสนใจใน',
         4: u'<b>be good at</b> + กริยาเติม ing คือเก่งเรื่อง',
         5: u'<b>be responsible for</b> + กริยาเติม ing คือรับผิดชอบงาน',
         6: u'<b>report to</b> คือขึ้นตรงต่อ',
         7: u'<b>two years of experience</b> · of เชื่อมช่วงเวลากับคำว่าประสบการณ์',
         8: u'<b>work with</b> คือทำงานร่วมกับ'}},

{'id': 'pp3', 'group': 'prep', 'title': u'ชุดที่ 3 · กริยาวลีในที่ประชุม',
 'box': ['back', 'down', 'forward', 'off', 'on', 'over', 'through', 'up'],
 'blocks': [
  {'label': '1', 't': "I'd like to follow [[1]] on the point Khun Anong raised earlier."},
  {'label': '2', 't': "Let me come [[2]] to that question at the end, if I may."},
  {'label': '3', 't': "Could you break that figure [[3]] by region for us?"},
  {'label': '4', 't': "The meeting was put [[4]] until Friday because two people were away."},
  {'label': '5', 't': "I'll hand [[5]] to my colleague now, who will cover the costs."},
  {'label': '6', 't': "Let me run [[6]] the agenda quickly before we start."},
  {'label': '7', 't': "Shall we move [[7]] to the next item?"},
  {'label': '8', 't': "I'd like to put [[8]] a suggestion, if nobody objects."},
 ],
 'ans': {1: 'up', 2: 'back', 3: 'down', 4: 'off', 5: 'over', 6: 'through', 7: 'on',
         8: 'forward'},
 'exp': {1: u'<b>follow up on</b> คือติดตามต่อจากเรื่องที่พูดไว้',
         2: u'<b>come back to</b> คือย้อนกลับมาที่เรื่องนั้น',
         3: u'<b>break down</b> คือแยกยอดออกเป็นส่วน ๆ',
         4: u'<b>put off</b> คือเลื่อนออกไป',
         5: u'<b>hand over to</b> คือส่งต่อให้อีกคนพูด',
         6: u'<b>run through</b> คือไล่ดูอย่างรวดเร็ว',
         7: u'<b>move on to</b> คือไปยังวาระถัดไป',
         8: u'<b>put forward a suggestion</b> คือเสนอความคิด'}},

{'id': 'pp4', 'group': 'prep', 'title': u'ชุดที่ 4 · บุพบทกับการบอกตัวเลข',
 'box': ['between', 'by', 'from', 'in', 'of', 'over', 'to', 'with'],
 'blocks': [
  {'label': '1', 't': "Sales rose [[1]] twelve percent last year."},
  {'label': '2', 't': "Revenue grew [[2]] forty million [[3]] fifty-two million baht."},
  {'label': '3', 't': "Costs stayed flat [[4]] the same period."},
  {'label': '4', 't': "There's a clear gap [[5]] the two regions."},
  {'label': '5', 't': "All the figures are shown [[6]] millions of baht."},
  {'label': '6', 't': "Compared [[7]] last year, output is up in every plant."},
  {'label': '7', 't': "That's an increase [[8]] nearly a third."},
 ],
 'ans': {1: 'by', 2: 'from', 3: 'to', 4: 'over', 5: 'between', 6: 'in', 7: 'with', 8: 'of'},
 'exp': {1: u'<b>rise by</b> + จำนวนที่เพิ่ม · ถ้าบอกปลายทางใช้ rise to',
         2: u'<b>grow from X to Y</b> คือโตจากเท่าไรไปเท่าไร',
         3: u'คู่กับ from ในข้อเดียวกัน · <b>from…to…</b>',
         4: u'<b>over the same period</b> คือตลอดช่วงเวลาเดียวกัน',
         5: u'<b>a gap between A and B</b> คือช่องว่างระหว่างสองสิ่ง',
         6: u'<b>shown in millions</b> คือแสดงเป็นหน่วยล้าน',
         7: u'<b>compared with</b> คือเทียบกับ',
         8: u'<b>an increase of</b> + ขนาดที่เพิ่ม'}},

# ══════════════════ โครง SAR+L ══════════════════
{'id': 'sl1', 'group': 'sarl',
 'title': u'ชุดที่ 1 · Tell me about a time when you had to meet a tight deadline.',
 'box': ["I was responsible for", "so I broke the work into", "I asked my supervisor",
         "we submitted the report", "I learned that", "I'll use the same habit"],
 'blocks': [
  {'label': 'Situation (S)',
   't': "During my internship at a logistics company last year, our team had to put the weekly "
        "cash position in front of the finance director every Thursday at nine. One week, two of "
        "the three branch files still had not arrived by Wednesday evening. [[1]] collecting the "
        "files and building the report."},
  {'label': 'Action (A)',
   't': "I knew I could not finish everything by nine, [[2]] three smaller tasks and started with "
        "the part that did not depend on the missing files. Then [[3]] which sections the director "
        "read first, so that I could be sure those sections were finished."},
  {'label': 'Result (R)',
   't': "[[4]] at a quarter to nine, with the two missing branches clearly marked as incomplete "
        "and last month's figures shown beside them. The director told me afterwards that marking "
        "the gaps was more useful than a complete report arriving late."},
  {'label': 'Lesson (L)',
   't': "[[5]] something incomplete and on time, with the gap clearly shown, is usually worth more "
        "than something complete and late. [[6]] at Siam Freight, because month-end deadlines "
        "there cannot move either."},
 ],
 'ans': {1: 'I was responsible for', 2: 'so I broke the work into', 3: 'I asked my supervisor',
         4: 'we submitted the report', 5: 'I learned that', 6: "I'll use the same habit"},
 'exp': {1: u'ปิดท้ายส่วน <b>S</b> ด้วยการบอกบทบาทของตัวเอง ผู้ฟังจึงรู้ว่าเรื่องนี้เกี่ยวกับเราตรงไหน',
         2: u'<b>so</b> เชื่อมเหตุกับการลงมือ · เปิดส่วน <b>A</b> ด้วยสิ่งที่ตัดสินใจทำ',
         3: u'ส่วน A ควรมีมากกว่าหนึ่งการกระทำ · ข้อนี้คือการไปถามเพื่อจัดลำดับความสำคัญ',
         4: u'ส่วน <b>R</b> ต้องเป็นผลที่วัดได้ · บอกเวลาที่ส่งและสภาพของงานที่ส่ง',
         5: u'<b>I learned that…</b> เป็นวลีเปิดส่วน <b>L</b>',
         6: u'ส่วน L ที่ดีต้องโยงมาที่งานที่สมัคร · ใช้ <b>will</b> เพราะพูดถึงอนาคต'}},

{'id': 'sl2', 'group': 'sarl',
 'title': u'ชุดที่ 2 · Tell me about a time when you disagreed with someone on your team.',
 'box': ["we had four days left", "rather than argue", "the group chose",
         "the president spotted an error", "what I took from it", "I now bring"],
 'blocks': [
  {'label': 'Situation (S)',
   't': "Last year I was treasurer of the accounting student society. We were planning our annual "
        "seminar, and the president wanted to spend most of the budget on a well-known speaker. "
        "I thought the venue and the catering mattered more to the people who would attend."},
  {'label': 'Action (A)',
   't': "[[1]] before we had to confirm the booking. [[2]] about it in the meeting, I ran a short "
        "survey of the people who came last year and brought the results to the next meeting. "
        "Eighty-one of the ninety replies ranked the venue above the speaker."},
  {'label': 'Result (R)',
   't': "[[3]] to pay a smaller speaker fee and move the difference to the venue. Attendance rose "
        "from 120 to 173. I should add that [[4]] in my table, where I had counted one faculty "
        "twice, and I corrected it before we published anything."},
  {'label': 'Lesson (L)',
   't': "[[5]] is that evidence settles a disagreement far faster than opinion does. [[6]] numbers "
        "to a discussion rather than arguments, and I ask someone to check them before I present."},
 ],
 'ans': {1: 'we had four days left', 2: 'rather than argue', 3: 'the group chose',
         4: 'the president spotted an error', 5: 'what I took from it', 6: 'I now bring'},
 'exp': {1: u'บอกข้อจำกัดเรื่องเวลาไว้ต้นส่วน A ทำให้การกระทำที่ตามมาดูสมเหตุสมผล',
         2: u'<b>rather than</b> + กริยารูปเดิม · บอกว่าเลือกไม่ทำอะไร แล้วทำอะไรแทน',
         3: u'ส่วน R · ใช้ประธานเป็นกลุ่ม ไม่ใช่ตัวเอง จึงไม่ฟังดูยกตนข่มท่าน',
         4: u'การเล่าว่าตัวเองก็มีจุดผิด และยอมรับการแก้จากคนอื่น ทำให้คำตอบน่าเชื่อขึ้นมาก',
         5: u'<b>what I took from it is that…</b> เป็นอีกวลีเปิดส่วน <b>L</b>',
         6: u'<b>now</b> บอกว่าเปลี่ยนเป็นนิสัยไปแล้ว ไม่ใช่แค่คิดได้ครั้งเดียว'}},

{'id': 'sl3', 'group': 'sarl',
 'title': u'ชุดที่ 3 · Tell me about a time when you had to learn something new quickly.',
 'box': ["I had never used", "I spent the first weekend", "by the second week",
         "the senior accountant asked", "what this taught me", "I am not afraid of"],
 'blocks': [
  {'label': 'Situation (S)',
   't': "On the first day of my internship at a mid-sized audit firm, I was put on a client that "
        "kept all its records in an accounting system I had not seen before. [[1]] that system, "
        "and the fieldwork was starting on the Monday."},
  {'label': 'Action (A)',
   't': "[[2]] working through the supplier's online tutorials and rebuilding a sample of our own "
        "practice data inside it. On the Monday I asked one of the client's accounts staff to walk "
        "me through how they actually used it, which turned out to differ from the manual in two "
        "places."},
  {'label': 'Result (R)',
   't': "[[3]] I was extracting the reports our team needed without help, and [[4]] me to write a "
        "one-page note so that the next intern would not have to start from nothing."},
  {'label': 'Lesson (L)',
   't': "[[5]] is that the fastest way into a new system is to use it on real data and then ask "
        "the people who work with it every day. [[6]] software I have not met before, which "
        "matters in audit because every client is different."},
 ],
 'ans': {1: 'I had never used', 2: 'I spent the first weekend', 3: 'by the second week',
         4: 'the senior accountant asked', 5: 'what this taught me', 6: 'I am not afraid of'},
 'exp': {1: u'<b>had never used</b> เป็น past perfect เพราะเกิดก่อนเหตุการณ์หลักในอดีต',
         2: u'<b>spend + ช่วงเวลา + กริยาเติม ing</b> คือใช้เวลาไปกับการทำอะไร',
         3: u'<b>by + เวลา</b> คือภายในเวลานั้น · เปิดส่วน <b>R</b> ด้วยกรอบเวลาที่ชัด',
         4: u'ผลที่คนอื่นมองเห็นและสั่งงานต่อ หนักแน่นกว่าการบอกเองว่าทำได้ดี',
         5: u'<b>what this taught me is that…</b> เปิดส่วน <b>L</b>',
         6: u'ปิดด้วยคุณสมบัติที่ตรงกับงาน พร้อมเหตุผลว่าทำไมจึงสำคัญกับงานนั้น'}},

{'id': 'sl4', 'group': 'sarl',
 'title': u'ชุดที่ 4 · Tell me about a time when you dealt with a difficult customer.',
 'box': ["a customer came back", "I did not argue with him", "I offered him",
         "he left with", "the lesson for me", "I keep that in mind"],
 'blocks': [
  {'label': 'Situation (S)',
   't': "During my second year I worked part time at a bookshop near campus. One Saturday [[1]] "
        "with a textbook he had bought three weeks earlier. The wrapping was open, and the shop's "
        "policy is no refund once the wrapping has been broken."},
  {'label': 'Action (A)',
   't': "[[2]] about the policy straight away. I asked him what had happened, and he explained "
        "that the lecturer had changed to a newer edition after the first class. [[3]] two "
        "choices: a credit note for the full amount, or an exchange for the new edition with the "
        "difference paid. I also checked whether other students had the same problem."},
  {'label': 'Result (R)',
   't': "[[4]] the new edition and came back twice more that term. I passed on what I had heard to "
        "the manager, who asked the department to send the reading list earlier the following year."},
  {'label': 'Lesson (L)',
   't': "[[5]] is that an angry customer usually wants to be understood before they want to be "
        "right. [[6]] whenever somebody complains: find out what happened first, and talk about "
        "the rules afterwards."},
 ],
 'ans': {1: 'a customer came back', 2: 'I did not argue with him', 3: 'I offered him',
         4: 'he left with', 5: 'the lesson for me', 6: 'I keep that in mind'},
 'exp': {1: u'ส่วน <b>S</b> ควรบอกเวลา สถานที่ และเหตุการณ์ตั้งต้นให้ครบในสองสามประโยค',
         2: u'เปิดส่วน <b>A</b> ด้วยสิ่งที่เลือก<i>ไม่</i>ทำ ทำให้เห็นการควบคุมตัวเองได้ชัด',
         3: u'<b>offer somebody something</b> · การเสนอทางเลือกสองทางดีกว่าการยื่นคำขาดทางเดียว',
         4: u'ส่วน <b>R</b> วัดผลได้สองชั้น คือลูกค้ากลับมา และร้านแก้ที่ต้นเหตุ',
         5: u'<b>the lesson for me is that…</b> เป็นวลีเปิดส่วน <b>L</b>',
         6: u'<b>keep something in mind</b> คือจำไว้ใช้เสมอ'}},

{'id': 'sl5', 'group': 'sarl',
 'title': u'ชุดที่ 5 · Tell me about a time when you took the lead.',
 'box': ["nobody wanted to take", "I volunteered to", "I set a short meeting",
         "we finished two days", "looking back", "I would do the same"],
 'blocks': [
  {'label': 'Situation (S)',
   't': "In a group assignment last semester, five of us had to analyse a listed company and "
        "present to the class. Two weeks before the deadline we had done almost nothing, because "
        "[[1]] responsibility for pulling the parts together."},
  {'label': 'Action (A)',
   't': "[[2]] coordinate, although I was not the most senior person in the group. [[3]] every "
        "Monday and Thursday, twenty minutes each, with one question for each person to answer. "
        "I also wrote down who owned which section and sent it round after every meeting."},
  {'label': 'Result (R)',
   't': "[[4]] before the deadline, and we were given the second highest mark in the class. What "
        "mattered more to me is that two members who had been quiet all term presented their own "
        "sections."},
  {'label': 'Lesson (L)',
   't': "[[5]], what made it work was not the schedule itself but writing down who owned each "
        "part. [[6]] again, except that I would start it in the first week rather than the third."},
 ],
 'ans': {1: 'nobody wanted to take', 2: 'I volunteered to', 3: 'I set a short meeting',
         4: 'we finished two days', 5: 'looking back', 6: 'I would do the same'},
 'exp': {1: u'อธิบายว่าทำไมจึงต้องมีคนนำ · ทำให้การเสนอตัวในส่วนถัดไปมีเหตุผลรองรับ',
         2: u'<b>volunteer to</b> + กริยารูปเดิม คือเสนอตัวทำ · เป็นคำที่ตรงกับคำถามเรื่องการนำ',
         3: u'การนำที่เป็นรูปธรรมคือกลไกที่จับต้องได้ ไม่ใช่การบอกว่าตัวเองมีภาวะผู้นำ',
         4: u'ส่วน <b>R</b> มีทั้งผลที่เป็นตัวเลขและผลที่เกิดกับคนในทีม',
         5: u'<b>looking back</b> คือเมื่อมองย้อนกลับไป เป็นวลีเปิดส่วน <b>L</b>',
         6: u'ยอมรับว่ายังมีจุดที่ทำได้ดีกว่านี้ ทำให้บทเรียนไม่ฟังดูสมบูรณ์แบบเกินจริง'}},

{'id': 'sl6', 'group': 'sarl',
 'title': u'ชุดที่ 6 · Tell me about a time when you had to work with limited information.',
 'box': ["we were asked to", "the data only covered", "I wrote down the assumptions",
         "our recommendation was accepted", "I now state", "before I present"],
 'blocks': [
  {'label': 'Situation (S)',
   't': "In a case competition last year, my team of four [[1]] recommend whether a Thai coffee "
        "chain should open in Vietnam. We were given four pages of market data and six hours."},
  {'label': 'Action (A)',
   't': "[[2]] two cities, and there was nothing at all on rents, which was the largest cost in "
        "our model. Instead of guessing quietly, [[3]] on a slide of their own: rent per square "
        "metre, staff cost, and the number of outlets in the first year. I also showed what "
        "happened to the answer if rent turned out to be thirty percent higher."},
  {'label': 'Result (R)',
   't': "[[4]] by the judges, and one of them said afterwards that the assumptions slide was the "
        "reason. We came second out of eighteen teams."},
  {'label': 'Lesson (L)',
   't': "What I learned is that missing data is normal, and that hiding it is what loses trust. "
        "[[5]] my assumptions openly and test the one that would change the answer most. [[6]] "
        "anything now, I ask myself which number would sink the conclusion if I were wrong."},
 ],
 'ans': {1: 'we were asked to', 2: 'the data only covered', 3: 'I wrote down the assumptions',
         4: 'our recommendation was accepted', 5: 'I now state', 6: 'before I present'},
 'exp': {1: u'<b>be asked to</b> + กริยารูปเดิม · บอกโจทย์ที่ได้รับในส่วน <b>S</b>',
         2: u'ระบุช่องว่างของข้อมูลให้ชัดว่าขาดอะไร ไม่ใช่บอกลอย ๆ ว่าข้อมูลน้อย',
         3: u'หัวใจของส่วน <b>A</b> ข้อนี้ คือเปิดเผยข้อสมมติแทนที่จะกลบไว้',
         4: u'ส่วน <b>R</b> · ใช้รูป passive เพราะผู้ตัดสินเป็นผู้รับข้อเสนอ',
         5: u'<b>now</b> อีกครั้ง บอกว่ากลายเป็นวิธีทำงานประจำแล้ว',
         6: u'<b>before I present anything</b> · วางเงื่อนไขเวลาไว้หน้าประโยค'}},

# ══════════════════ โครง Three S's ══════════════════
{'id': 'ts1', 'group': 'three',
 'title': u'ชุดที่ 1 · ผู้สมัครงานสอบบัญชี',
 'box': ["I've been drawn to", "It gave me a clear picture of", "That experience taught me",
         "I'm confident I can"],
 'blocks': [
  {'label': 'SUCCESS',
   't': "[[1]] auditing since my second year, when I took Auditing Principles and earned an A. "
        "I enjoyed it enough to take Advanced Auditing the following year. Last summer I spent ten "
        "weeks as an intern at Phattara and Partners, working on inventory counts and bank "
        "confirmations for three manufacturing clients. [[2]] how an audit actually runs, from "
        "planning through to the final file."},
  {'label': 'STRENGTH',
   't': "Outside university I keep the accounts for a student cooperative with about two hundred "
        "members, and I present the figures at the annual meeting. [[3]] to explain numbers to "
        "people who have never read a financial statement, which I think is half of what an "
        "auditor does."},
  {'label': 'SITUATION',
   't': "So with coursework in auditing, ten weeks of fieldwork, and practice at explaining "
        "figures plainly, [[4]] contribute to your assurance team from my first busy season."},
 ],
 'ans': {1: "I've been drawn to", 2: 'It gave me a clear picture of',
         3: 'That experience taught me', 4: "I'm confident I can"},
 'exp': {1: u'<b>I’ve been drawn to… since…</b> ใช้ present perfect เพราะสนใจมาตั้งแต่อดีตจนถึงตอนนี้',
         2: u'ปิดส่วน <b>SUCCESS</b> ด้วยสิ่งที่ได้จากประสบการณ์ ไม่ใช่จบแค่เล่าว่าไปทำอะไรมา',
         3: u'เปิดส่วน <b>STRENGTH</b> โดยโยงจุดแข็งกลับไปหาประสบการณ์ที่เพิ่งเล่า',
         4: u'<b>I’m confident I can…</b> ปิดส่วน <b>SITUATION</b> ด้วยการบอกว่าจะช่วยองค์กรได้อย่างไร'}},

{'id': 'ts2', 'group': 'three',
 'title': u'ชุดที่ 2 · ผู้สมัครงานการตลาด',
 'box': ["What I enjoyed most was", "I also took part in", "this has made me",
         "I'd like to bring"],
 'blocks': [
  {'label': 'SUCCESS',
   't': "I'm a final-year marketing student at Chulalongkorn University. In my third year I took "
        "Consumer Behaviour, where our team surveyed 240 shoppers and presented the findings to a "
        "local retailer. [[1]] watching the retailer change its shelf layout because of something "
        "we had found."},
  {'label': 'STRENGTH',
   't': "[[2]] a national case competition last year, and we reached the final eight out of sixty "
        "teams. Working to a six-hour deadline with three people I had met that morning — "
        "[[3]] comfortable with pressure and with making a decision before the data is perfect."},
  {'label': 'SITUATION',
   't': "So [[4]] that mix of real research experience and calm under a deadline to your brand "
        "team, where I understand both are part of an ordinary week."},
 ],
 'ans': {1: 'What I enjoyed most was', 2: 'I also took part in', 3: 'this has made me',
         4: "I'd like to bring"},
 'exp': {1: u'<b>What I enjoyed most was</b> + กริยาเติม ing · เป็นโครงเน้นที่ขึ้นต้นด้วย what',
         2: u'<b>take part in</b> คือเข้าร่วม · also เชื่อมหลักฐานชิ้นที่สองเข้ากับชิ้นแรก',
         3: u'<b>make somebody + คำคุณศัพท์</b> คือทำให้เป็นแบบนั้น · ใช้ present perfect เพราะผลยังอยู่',
         4: u'<b>I’d like to bring…to…</b> โยงสิ่งที่มีเข้ากับทีมที่สมัคร'}},

{'id': 'ts3', 'group': 'three',
 'title': u'ชุดที่ 3 · ผู้สมัครโครงการผู้บริหารฝึกหัดของธนาคาร',
 'box': ["I first became interested in", "On top of my studies", "which has given me",
         "I'm looking for a role where"],
 'blocks': [
  {'label': 'SUCCESS',
   't': "[[1]] banking when I took Financial Markets in my second year and built a bond pricing "
        "model for the term project. I earned an A, and the lecturer asked to use my model as a "
        "class example the following year."},
  {'label': 'STRENGTH',
   't': "[[2]], I have worked part time at the university's service centre for two years, dealing "
        "with about forty students a day, [[3]] a great deal of practice at staying patient when "
        "the person in front of me is upset."},
  {'label': 'SITUATION',
   't': "[[4]] I can use both sides of that — the analytical side and the side that deals "
        "with people — and a management trainee programme is exactly that kind of role."},
 ],
 'ans': {1: 'I first became interested in', 2: 'On top of my studies', 3: 'which has given me',
         4: "I'm looking for a role where"},
 'exp': {1: u'<b>become interested in</b> · first บอกจุดเริ่มต้นของความสนใจ',
         2: u'<b>on top of</b> คือนอกเหนือจาก · ใช้เปลี่ยนจากเรื่องเรียนไปเรื่องนอกห้องเรียน',
         3: u'<b>which</b> ขยายความทั้งประโยคข้างหน้า ไม่ได้ขยายคำนามคำเดียว',
         4: u'<b>a role where…</b> คือตำแหน่งที่ซึ่ง · ปิดด้วยการบอกว่ากำลังมองหาอะไร'}},

{'id': 'ts4', 'group': 'three',
 'title': u'ชุดที่ 4 · ผู้สมัครงานภาษี',
 'box': ["I've spent the last two years", "The part I like about tax is",
         "What I bring beyond the technical side is", "and that is the kind of work"],
 'blocks': [
  {'label': 'SUCCESS',
   't': "[[1]] building a background in taxation. I took Fundamental Taxation in my third year and "
        "Advanced Taxation this year, and I earned A's in both. [[2]] that the answer is usually "
        "written down somewhere, and that the skill is knowing where to look and how to read it."},
  {'label': 'STRENGTH',
   't': "[[3]] patience with detail that other people find tedious. For eight months I checked "
        "withholding tax certificates for a small firm, around three hundred a month, and I "
        "redesigned the schedule so that received and agreed were marked separately."},
  {'label': 'SITUATION',
   't': "So with a solid grounding in tax and a habit of checking carefully, I'd like to join your "
        "corporate tax team, [[4]] I would like to be doing for the next several years."},
 ],
 'ans': {1: "I've spent the last two years", 2: 'The part I like about tax is',
         3: 'What I bring beyond the technical side is', 4: 'and that is the kind of work'},
 'exp': {1: u'<b>spend + ช่วงเวลา + กริยาเติม ing</b> · present perfect เพราะยังทำต่อเนื่องถึงปัจจุบัน',
         2: u'<b>the part I like about X is that…</b> โครงเน้นที่ใช้บอกเหตุผลว่าทำไมจึงชอบ',
         3: u'<b>What I bring…is…</b> โครงเน้นด้วย what · ใช้เปิดส่วน STRENGTH ได้ดี',
         4: u'<b>the kind of work I would like to be doing</b> · บอกทิศทางระยะยาวโดยไม่ต้องสัญญาเกินจริง'}},

{'id': 'ts5', 'group': 'three',
 'title': u'ชุดที่ 5 · ผู้สมัครงานโลจิสติกส์',
 'box': ["My interest started with", "I was responsible for", "Since then I have kept",
         "This is why I'm applying"],
 'blocks': [
  {'label': 'SUCCESS',
   't': "[[1]] a factory visit in my second year, where I watched a warehouse team pick two "
        "thousand orders in a single shift. I went back and took every supply chain elective the "
        "faculty offered, and I finished top of the class in Operations Management."},
  {'label': 'STRENGTH',
   't': "Last summer I interned at a distribution centre north of Bangkok. [[2]] checking the "
        "daily cycle count sheets, about sixty locations a day. I noticed that most of the "
        "differences came from one aisle where two products had nearly the same code, and the "
        "team relabelled them. [[3]] the habit of looking for the pattern rather than the single "
        "error."},
  {'label': 'SITUATION',
   't': "[[4]] to your operations graduate scheme. I would like to work somewhere the problem is "
        "physical and the answer is in the data."},
 ],
 'ans': {1: 'My interest started with', 2: 'I was responsible for',
         3: 'Since then I have kept', 4: "This is why I'm applying"},
 'exp': {1: u'<b>my interest started with…</b> เปิดเรื่องด้วยจุดเริ่มที่เป็นรูปธรรม จำง่ายกว่าการบอกว่าสนใจมานาน',
         2: u'<b>be responsible for</b> + กริยาเติม ing · บอกขอบเขตงานที่ทำจริง',
         3: u'<b>since then</b> + present perfect · เชื่อมอดีตเข้ากับนิสัยที่ยังมีอยู่',
         4: u'<b>this is why I’m applying to…</b> ปิดด้วยการโยงทุกอย่างกลับมาที่ตำแหน่ง'}},

{'id': 'ts6', 'group': 'three',
 'title': u'ชุดที่ 6 · ผู้สมัครงานที่ปรึกษา',
 'box': ["I chose this path because", "The strongest evidence of this is", "I'm comfortable",
         "and I believe that is"],
 'blocks': [
  {'label': 'SUCCESS',
   't': "[[1]] I would rather learn across several industries than go deep into one straight away. "
        "[[2]] the three case competitions I entered in the last two years, covering retail, "
        "healthcare and energy. We placed in two of them, and in the third I learned more than in "
        "either of the others."},
  {'label': 'STRENGTH',
   't': "[[3]] saying that I do not know yet. During my internship at a small consultancy I was "
        "asked about a market size I had not researched, and rather than guess I said I would come "
        "back by five o'clock with a sourced figure. I did, and the partner used it in the deck."},
  {'label': 'SITUATION',
   't': "So I bring breadth across industries and a habit of checking before I answer, [[4]] "
        "exactly what a first-year analyst is there to do."},
 ],
 'ans': {1: 'I chose this path because', 2: 'The strongest evidence of this is',
         3: "I'm comfortable", 4: 'and I believe that is'},
 'exp': {1: u'เปิดด้วยเหตุผลของการเลือกสายงาน ตรงกับสิ่งที่ผู้สัมภาษณ์งานที่ปรึกษาอยากรู้',
         2: u'<b>the strongest evidence of this is…</b> · บอกว่ากำลังจะยกหลักฐานมาหนุนสิ่งที่เพิ่งพูด',
         3: u'<b>be comfortable + กริยาเติม ing</b> คือทำสิ่งนั้นได้โดยไม่อึดอัด',
         4: u'ปิดด้วยการบอกว่าสิ่งที่มีตรงกับหน้าที่ของตำแหน่งอย่างไร'}},

]
