# -*- coding: utf-8 -*-
u"""บทฟังสำหรับ Part III · Listening ของวิชาภาษาอังกฤษ

แต่ละชุดมีสองส่วนตามแนวข้อสอบจริง
  presentation · การนำเสนอกลุ่มเรื่อง international marketing หลายคนพูดสลับกัน
  talk         · การบรรยายเรื่อง merger case คนเดียวพูดตลอด

ทุกบทตั้งใจใส่ศัพท์จาก Unit 2 และ Unit 12 ให้หนาแน่น เพราะข้อสอบวัดการฟังจับรายละเอียด
ที่ผูกกับศัพท์เหล่านั้นโดยตรง

── กติกาสำคัญ คลิปต้องไม่พูดคำตอบออกมาตรง ๆ ──
เดิมบททุกคลิปพูดคำตอบเป๊ะตามตัวเลือก นิสิตจึงทำข้อสอบได้โดยแค่รอจับเสียง
ให้ตรงกับคำในตัวเลือก ไม่ต้องเข้าใจว่าพูดอะไรเลย ซึ่งไม่ได้วัดการฟังจริง

ตอนนี้ตัวเลือกที่ถูกต้องเป็นอย่างใดอย่างหนึ่งเสมอ
  ถอดความ  · บทพูดว่า just under a third ตัวเลือกเขียนว่า close to thirty percent
  ใช้ศัพท์  · บทเล่าอาการ ตัวเลือกเรียกชื่อศัพท์ เช่น บทว่า both boards recommended it
              ตัวเลือกว่า friendly takeover ซึ่งเป็นคำที่คลิปไม่ได้พูดเลย
  คำนวณ    · บทให้ตัวเลขตั้งต้น ตัวเลือกเป็นผลลัพธ์ เช่น 310 ลบ 205 เท่ากับ goodwill 105
  ตีความ    · บทให้สัญญาณ ตัวเลือกเป็นข้อสรุป เช่น ยอดขายต่ำกว่าจุดคุ้มทุน แปลว่าปีแรกขาดทุน

tools/make-listening.py บังคับกติกานี้ด้วยเครื่อง ถ้าตัวเลือกที่ถูกไปตรงกับข้อความในบท
ทั้งวลี หรือคำเนื้อความครบทุกคำในช่วงสั้น ๆ จะไม่ยอมสังเคราะห์เสียงให้เลย

ตัวลวงยังดึงมาจากตัวเลขที่คลิปพูดจริง เพื่อให้คนที่ฟังผ่าน ๆ แล้วจับคำได้อย่างเดียว
ติดกับดัก ส่วนคนที่เข้าใจเนื้อความจะตัดตัวลวงออกได้

── เขียนให้เหมาะกับนิสิตบัญชีชั้นปีที่ 3 ──
ประเภทของบททั้งสองแบบเปลี่ยนไม่ได้ เพราะแนวข้อสอบล็อกไว้ แต่สิ่งที่ถูกถามย้ายไปเป็น
เรื่องที่นิสิตบัญชีอ่านออกทันที เช่น อัตรากำไรขั้นต้น จุดคุ้มทุน ระยะเวลาคืนทุน เงินลงทุน
ค่าความนิยม ต้นทุนการรวมกิจการ วิธีส่วนได้เสีย และวันที่เริ่มนำมารวมงบ

ไม่ใช้ชื่อบริษัทจริงหรือดีลจริงเลย ทุกกิจการสมมติขึ้นใหม่ เพราะข้อสอบฟังควรวัดว่า
จับรายละเอียดจากเสียงได้ไหม ไม่ใช่วัดว่าเคยอ่านข่าวดีลนั้นมาก่อนหรือเปล่า

ความยาวคุมไว้ราว 300 คำต่อคลิป และพูดด้วยความเร็วปกติ ได้คลิปละราวสองนาที
ซึ่งเป็นความยาวที่ฟังรวดเดียวได้โดยไม่เสียสมาธิ
"""

# เสียงที่ใช้ · ตั้งชื่อย่อไว้ให้อ้างง่ายในบท
VOICES = {
    'm1': 'en-US-AndrewNeural',
    'm2': 'en-GB-RyanNeural',
    'm3': 'en-US-GuyNeural',
    'f1': 'en-US-AvaNeural',
    'f2': 'en-GB-SoniaNeural',
    'f3': 'en-US-JennyNeural',
}

SETS = [

# ══════════════════════════════════ ชุดที่ 1 ══════════════════════════════════
{'id': 'L1', 'title': u'ชุดที่ 1', 'parts': [

 {'id': 'L1a', 'kind': 'presentation',
  'title': 'Entering the Vietnamese Market',
  'context': u'ทีมสามคนเสนอแผนพาแบรนด์อาหารพร้อมทานเข้าตลาดเวียดนาม พร้อมตัวเลขการลงทุนและจุดคุ้มทุน',
  'turns': [
   ('Mai', 'm', 'f1',
    "Good morning everyone. I'm Mai. Today my team will present our plan for taking Freshline "
    "ready meals into Vietnam. I'll cover the research, Daniel will take segmentation and "
    "positioning, and Preecha will finish with the numbers and the risks."),
   ('Mai', 'm', 'f1',
    "We were in the field from the beginning of June until the end of August, working across four "
    "cities. Two thousand shoppers filled in a form for us, and separately we sat down with six "
    "small groups of buyers and just listened. The headline is that chilled ready meals are adding "
    "about nine percent a year. But the category is filling up. The biggest player is already "
    "sitting on just under a third of it, and two international names arrived last year."),
   ('Daniel', 'd', 'm1',
    "Thanks, Mai. So who are we selling to? The buyer we want is narrow: office workers in the big "
    "cities, twenty-two to thirty-five, who pick something up on the way home rather than doing a "
    "weekly shop. They are only twelve percent of all buyers, but each one of them spends nearly "
    "twice what the average buyer spends."),
   ('Daniel', 'd', 'm1',
    "On positioning, we are not going anywhere near a price fight. The cheap end is crowded and "
    "there is nothing left in the margin down there. We will put Freshline about a fifth above the "
    "average shelf price, and build the name on where the ingredients come from."),
   ('Preecha', 'p', 'm2',
    "Thank you, Daniel. Now the numbers, because this is where the plan lives or dies. We need four "
    "and a half million dollars before we sell anything, and almost every cent of that is the "
    "refrigerated delivery network. At the higher price our gross margin is thirty-eight percent. "
    "Sold at the average shelf price it would be twenty-two."),
   ('Preecha', 'p', 'm2',
    "We stop losing money in the nineteenth month, and the whole investment is back three years and "
    "two months in. Advertising takes one point one million dollars in the first year, and a little "
    "over half of that from the second year onwards."),
   ('Preecha', 'p', 'm2',
    "Three risks. First, the cold chain: one failure and we lose the stock and the name together. "
    "Second, the biggest player could start cutting prices, and that would take our margin down to "
    "around twenty-five. Third, one distributor handles eight thousand shops for us, so a single "
    "contract dispute stops us nationally overnight. Our advice is not to go national at once. Take "
    "two cities, learn, then decide. Thank you. We are happy to take questions."),
  ],
  'questions': [
   {'q': 'How long did the team spend collecting data?',
    'o': ['About three months', 'About three weeks', 'About nine months', 'About two years'], 'a': 0,
    'e': u'"from the beginning of June until the end of August" คือมิถุนายน กรกฎาคม สิงหาคม '
         u'· คลิปไม่ได้พูดคำว่าสามเดือนเลย ต้องนับเดือนเอง'},
   {'q': 'Which two research methods did the team use?',
    'o': ['A questionnaire and focus groups', 'Interviews and a shelf audit',
          'Focus groups and in-store trials', 'A questionnaire and a sales trial'], 'a': 0,
    'e': u'"Two thousand shoppers filled in a form" คือ questionnaire และ "six '
         u'small groups of buyers" คือ focus groups · คลิปเล่าอาการ ตัวเลือกเรียกชื่อศัพท์'},
   {'q': 'What does Mai say about the biggest player?',
    'o': ['It holds close to thirty percent of the market', 'It holds more than half the market',
          'It holds about one tenth of the market', 'It arrived only last year'], 'a': 0,
    'e': u'"sitting on just under a third of it" · หนึ่งในสามคือราว 33 เปอร์เซ็นต์ '
         u'ต่ำกว่านั้นเล็กน้อยจึงราว 30 · สองแบรนด์ที่เพิ่งเข้ามาเป็นคนละเรื่อง'},
   {'q': 'Where does the target segment usually buy?',
    'o': ['At convenience stores', 'At supermarkets', 'Online', 'At wholesale markets'], 'a': 0,
    'e': u'"pick something up on the way home rather than doing a weekly shop" '
         u'· ซื้อระหว่างทางกลับบ้านทีละนิด คือร้านสะดวกซื้อ ไม่ใช่ซูเปอร์มาร์เก็ตที่ซื้อทีเดียวทั้งสัปดาห์'},
   {'q': 'Why does Daniel rule out competing on price?',
    'o': ['The low end is crowded and the margins are too thin',
          'The company cannot produce cheaply enough',
          'Local rules set a minimum price', 'The distributor refuses to discount'], 'a': 0,
    'e': u'"The cheap end is crowded and there is nothing left in the margin down there"'},
   {'q': 'What is almost all of the upfront money spent on?',
    'o': ['The chilled distribution network', 'Advertising in the first year',
          'Buying shelf space', 'Reformulating the product'], 'a': 0,
    'e': u'"almost every cent of that is the refrigerated delivery network" '
         u'· refrigerated delivery คือคำเดียวกับ chilled distribution'},
   {'q': 'What does selling at the average shelf price cost the company?',
    'o': ['Sixteen points of gross margin', 'Twenty-two points of gross margin',
          'Thirty-eight points of gross margin', 'Nothing, the margin is the same'], 'a': 0,
    'e': u'38 ลบ 22 เท่ากับ 16 จุด · คลิปให้ตัวเลขสองตัว แต่ไม่ได้พูดผลต่าง ต้องลบเอง'},
   {'q': 'When does the plan break even?',
    'o': ['In month nineteen', 'In month nine', 'After three years and two months', 'In year two'], 'a': 0,
    'e': u'"We stop losing money in the nineteenth month" คือจุดคุ้มทุน '
         u'· สามปีสองเดือนคือระยะเวลาคืนทุน คนละตัว'},
   {'q': 'What happens to advertising spending after the first year?',
    'o': ['It falls to about six hundred thousand', 'It rises to one point one million',
          'It stays where it is', 'It stops altogether'], 'a': 0,
    'e': u'"a little over half of that from the second year onwards" '
         u'· ครึ่งหนึ่งของ 1.1 ล้านคือ 550,000 มากกว่านั้นนิดหน่อยจึงราว 600,000'},
   {'q': 'What does the team finally recommend?',
    'o': ['Starting with a pilot in two cities', 'Launching nationally straight away',
          'Selling at the average shelf price', 'Finding a second distributor'], 'a': 0,
    'e': u'"not to go national at once. Take two cities, learn, then decide" '
         u'· ทดลองก่อนในวงจำกัดคือ pilot'},
  ]},

 {'id': 'L1b', 'kind': 'talk',
  'title': 'A Takeover in Regional Logistics',
  'context': u'วิทยากรเล่ากรณีซื้อกิจการขนส่งภูมิภาค เน้นสิ่งที่พบตอน due diligence และค่าความนิยม',
  'turns': [
   ('Speaker', 's', 'm3',
    "Good afternoon. Today I want to walk you through a takeover in regional logistics, because it "
    "shows how much of a deal is settled by the accounting work rather than by the strategy."),
   ('Speaker', 's', 'm3',
    "In February a listed transport group called Northvale approached a family-owned business, "
    "Harbour Freight, and put two hundred and forty million pounds on the table. Nine days later the "
    "Harbour Freight board sent it back. Their argument was that the figure took no account of what "
    "the depot network was actually worth."),
   ('Speaker', 's', 'm3',
    "Northvale then went over the board's head and put the offer to the owners of the shares "
    "directly. It lifted the price twice, first to two hundred and seventy million and in the end to "
    "three hundred and ten. At that level it was paying eleven pounds for every pound of annual "
    "profit the business made."),
   ('Speaker', 's', 'm3',
    "Now to the investigation of the books before completion. The buyer's accountants were given "
    "under two months, which for a business of this size is not long, and I want you to hold on to "
    "that. They still found two things. Repair obligations on forty leased vehicles had never gone "
    "into the accounts at all, worth about six million pounds. And one customer, bringing in more "
    "than a quarter of the revenue, had already written to say it was leaving."),
   ('Speaker', 's', 'm3',
    "Those findings did not kill the deal, but they changed the shape of it. The headline price did "
    "not move. Instead thirty million of it was put to one side for eighteen months, payable only if "
    "no claims came in."),
   ('Speaker', 's', 'm3',
    "Completion was the first of July, and from that day Harbour Freight's results were added into "
    "the group figures line by line. The net assets it brought with it were worth two hundred and "
    "five million at fair value."),
   ('Speaker', 's', 'm3',
    "Two lessons. The model promised forty million a year from putting the two depot networks "
    "together. Two years on, what actually came through was a little over half of that. And joining "
    "the two businesses up cost eighteen million that nobody had put in the model at all. When you "
    "read a takeover story, always ask what the promised savings turned out to be. Thank you."),
  ],
  'questions': [
   {'q': 'Why did the Harbour Freight board turn down the first offer?',
    'o': ['It did not reflect what the depots were worth', 'The buyer was a direct competitor',
          'The owners had not been consulted', 'The payment was to be in shares'], 'a': 0,
    'e': u'"the figure took no account of what the depot network was actually worth" '
         u'· คือบอกว่าตีมูลค่าต่ำไป ซึ่งคือคำว่า undervalued'},
   {'q': 'What kind of takeover did this become, and why?',
    'o': ['Hostile, because the bidder approached the shareholders directly',
          'Friendly, because the board later agreed',
          'A management buyout, because managers took part',
          'A merger of equals, because the two were the same size'], 'a': 0,
    'e': u'"went over the board\'s head and put the offer to the owners of the shares directly" '
         u'· คลิปไม่ได้พูดคำว่า hostile เลย ต้องรู้ว่าอาการแบบนี้เรียกว่าอะไร'},
   {'q': 'What was the final price as a multiple of earnings?',
    'o': ['Eleven times', 'Nine times', 'Eighteen times', 'Forty times'], 'a': 0,
    'e': u'"paying eleven pounds for every pound of annual profit" คือ 11 เท่าของกำไร'},
   {'q': 'What does the speaker suggest about the time allowed to check the books?',
    'o': ['It was short for a deal of this size', 'It was generous by market standards',
          'It was fixed by the regulator', 'It was wasted, since nothing was found'], 'a': 0,
    'e': u'"given under two months, which for a business of this size is not long" '
         u'· และยังบอกให้ผู้ฟังจำไว้ แปลว่าเห็นว่าสั้นเกินไป'},
   {'q': 'What was wrong with the forty leased vehicles?',
    'o': ['Obligations to repair them had never been recorded',
          'They had been sold twice', 'They were valued at replacement cost',
          'Their insurance had lapsed'], 'a': 0,
    'e': u'"Repair obligations on forty leased vehicles had never gone into the accounts at all"'},
   {'q': 'What had the large customer already done?',
    'o': ['Given notice that it was leaving', 'Asked for a lower price',
          'Been taken over by Northvale', 'Failed to pay its invoices'], 'a': 0,
    'e': u'"had already written to say it was leaving" คือการแจ้งบอกเลิกล่วงหน้า'},
   {'q': 'How did the two sides deal with what was found?',
    'o': ['Part of the price was held back for eighteen months',
          'The price was reduced by six million',
          'The deal was abandoned', 'The customer contract was renegotiated'], 'a': 0,
    'e': u'"thirty million of it was put to one side for eighteen months" '
         u'· ราคารวมไม่ขยับ แต่กันเงินไว้ส่วนหนึ่ง'},
   {'q': 'What happened on the first of July?',
    'o': ['Harbour Freight began to be consolidated',
          'The offer was raised for the second time',
          'The holdback was released', 'Due diligence started'], 'a': 0,
    'e': u'"from that day Harbour Freight\'s results were added into the group figures line by line" '
         u'· การนำมารวมทีละบรรทัดคือ consolidation'},
   {'q': 'How much goodwill arose on the acquisition?',
    'o': ['One hundred and five million pounds', 'Two hundred and five million pounds',
          'Thirty million pounds', 'Six million pounds'], 'a': 0,
    'e': u'ราคาสุดท้าย 310 ลบมูลค่ายุติธรรมของสินทรัพย์สุทธิ 205 เท่ากับ 105 ล้านปอนด์ '
         u'· คลิปให้ตัวเลขสองตัวแต่ไม่ได้พูดผลลัพธ์'},
   {'q': 'What were the savings actually achieved after two years?',
    'o': ['A little over twenty million a year', 'The full forty million a year',
          'Eighteen million a year', 'Nothing at all'], 'a': 0,
    'e': u'"a little over half of that" ของที่สัญญาไว้ 40 ล้าน · '
         u'ส่วน 18 ล้านคือต้นทุนการรวมกิจการที่ลืมใส่ในแบบจำลอง ไม่ใช่ประโยชน์ที่ได้'},
  ]},
]},

# ══════════════════════════════════ ชุดที่ 2 ══════════════════════════════════
{'id': 'L2', 'title': u'ชุดที่ 2', 'parts': [

 {'id': 'L2a', 'kind': 'presentation',
  'title': 'Taking a Coffee Brand into Japan',
  'context': u'สองคนเสนอแผนพาแบรนด์กาแฟเข้าญี่ปุ่น เน้นต้นทุนต่อหน่วยและจุดคุ้มทุน',
  'turns': [
   ('Nadia', 'n', 'f2',
    "Morning. Nadia here, with Kenji. We are proposing to take Aurelia coffee into Japan. I will "
    "handle the market and the positioning, and Kenji will take the mix and the financials."),
   ('Nadia', 'n', 'f2',
    "Japan is the third largest coffee market in the world by value. It is also a mature one. It "
    "adds only a couple of percent a year, so nobody there is waiting for a new brand to turn up. "
    "Whatever we sell, somebody else stops selling."),
   ('Nadia', 'n', 'f2',
    "Segmentation gives us three groups. Just over half of all buyers pick their coffee up in a "
    "convenience store, and they will change brand over ten yen. Speciality cafe customers are "
    "about one in five, and they care where the beans were grown. Then there are offices buying on "
    "a monthly plan: fewer than one buyer in ten today, but that group is adding fourteen percent a "
    "year. That is the one we are going after."),
   ('Kenji', 'k', 'm1',
    "Thanks, Nadia. On the mix, place matters far more than promotion here. We are not going to "
    "fight for shelf space in the convenience chains. We will sell straight to offices on a monthly "
    "plan, and notice what that does to cash: the money is in our bank before the coffee leaves the "
    "roastery."),
   ('Kenji', 'k', 'm1',
    "The unit economics. A box goes out at four thousand two hundred yen. It costs us two thousand "
    "four hundred to fill and ship."),
   ('Kenji', 'k', 'm1',
    "Fixed costs run at ninety million yen a year, mostly the roasting contract and the customer "
    "team. So work out how many boxes have to go out before we make a single yen of profit. Our "
    "forecast for the first year is thirty-one thousand boxes."),
   ('Kenji', 'k', 'm1',
    "Two risks worth naming. In a business built on monthly plans, keeping the customers you already "
    "have is the whole game: lose more than four percent of them a month and the break-even point "
    "slides out by roughly a year. And four fifths of what we pay for green beans is settled in "
    "dollars, so the exchange rate goes straight through to the margin. Thank you."),
  ],
  'questions': [
   {'q': 'How fast is the Japanese coffee market growing?',
    'o': ['About two percent a year', 'About fourteen percent a year',
          'About twenty percent a year', 'It is not growing at all'], 'a': 0,
    'e': u'"It adds only a couple of percent a year" · a couple แปลว่าสอง '
         u'· 14 เปอร์เซ็นต์เป็นอัตราโตของกลุ่มออฟฟิศ ไม่ใช่ของทั้งตลาด'},
   {'q': 'What does Nadia mean by “whatever we sell, somebody else stops selling”?',
    'o': ['Growth has to come from taking share from rivals',
          'The market is too small to enter',
          'Demand is falling every year', 'Customers buy only one brand for life'], 'a': 0,
    'e': u'ตลาดโตแค่สองเปอร์เซ็นต์ ยอดขายใหม่จึงต้องแย่งมาจากคนอื่น '
         u'· นี่คือ market penetration ซึ่งคลิปไม่ได้เอ่ยชื่อ'},
   {'q': 'Why are convenience store buyers unattractive?',
    'o': ['They switch brand over a tiny price difference',
          'They buy only once a year', 'They never drink coffee at work',
          'They cannot be reached by advertising'], 'a': 0,
    'e': u'"they will change brand over ten yen" · สิบเยนคือเงินจำนวนเล็กมาก '
         u'แปลว่าไม่มีความภักดีต่อแบรนด์เลย'},
   {'q': 'Which segment is the target market?',
    'o': ['Office subscription buyers', 'Convenience store buyers',
          'Speciality cafe customers', 'Hotel and restaurant buyers'], 'a': 0,
    'e': u'"offices buying on a monthly plan … That is the one we are going after"'},
   {'q': 'Why does selling direct to offices help cash flow?',
    'o': ['Customers pay before the goods are delivered',
          'Offices are charged a higher price', 'There is no delivery cost',
          'It avoids import duty'], 'a': 0,
    'e': u'"the money is in our bank before the coffee leaves the roastery" '
         u'· เก็บเงินก่อนส่งของ เงินสดจึงเข้าก่อน'},
   {'q': 'What is the contribution per box?',
    'o': ['One thousand eight hundred yen', 'Two thousand four hundred yen',
          'Four thousand two hundred yen', 'Ninety thousand yen'], 'a': 0,
    'e': u'4,200 ลบ 2,400 เท่ากับ 1,800 เยน · คลิปให้ราคาขายกับต้นทุน แต่ไม่ได้พูดผลต่าง'},
   {'q': 'How many boxes a year are needed to break even?',
    'o': ['Fifty thousand', 'Thirty-one thousand',
          'Ninety thousand', 'Four thousand two hundred'], 'a': 0,
    'e': u'ต้นทุนคงที่ 90 ล้าน หารด้วยกำไรส่วนเกินต่อกล่อง 1,800 เท่ากับ 50,000 กล่อง '
         u'· ต้องคำนวณสองชั้น คลิปไม่ได้บอกคำตอบ'},
   {'q': 'What does the first year forecast tell you?',
    'o': ['The first year is a planned loss', 'The first year makes a small profit',
          'The first year breaks even exactly', 'The forecast has not been made yet'], 'a': 0,
    'e': u'ประมาณการ 31,000 กล่อง ต่ำกว่าจุดคุ้มทุน 50,000 กล่อง จึงขาดทุนตั้งแต่ตั้งใจแล้ว'},
   {'q': 'What happens if monthly churn passes four percent?',
    'o': ['Break-even is pushed back by about a year', 'Fixed costs fall',
          'The contribution per box rises', 'The forecast is unaffected'], 'a': 0,
    'e': u'"the break-even point slides out by roughly a year"'},
   {'q': 'Why does the exchange rate matter?',
    'o': ['Most of the bean cost is paid in dollars', 'Subscriptions are billed in dollars',
          'The roasting contract is priced in euros', 'Import duty is charged in dollars'], 'a': 0,
    'e': u'"four fifths of what we pay for green beans is settled in dollars" '
         u'· สี่ในห้าคือแปดสิบเปอร์เซ็นต์'},
  ]},

 {'id': 'L2b', 'kind': 'talk',
  'title': 'A Merger of Two Software Firms',
  'context': u'วิทยากรเล่ากรณีควบรวมบริษัทซอฟต์แวร์บัญชีสองราย เน้นการประมาณการ synergies ที่พลาด',
  'turns': [
   ('Speaker', 's', 'm2',
    "Today's case brings together two accounting software companies. I picked it because the "
    "strategy was sound and the deal still disappointed, and the reason is entirely in the numbers."),
   ('Speaker', 's', 'm2',
    "Ledgerworks sold to small practices. Ravenpoint sold to mid-sized groups. Neither was taking "
    "business away from the other, and both boards put the deal to their own investors with a "
    "recommendation to accept it."),
   ('Speaker', 's', 'm2',
    "The structure matters. Ledgerworks holders received six Ravenpoint shares for every ten they "
    "owned. On the day of the announcement that put a value of four hundred and eighty million "
    "euros on Ledgerworks, or fourteen euros of price for every euro of annual profit. The market "
    "barely reacted: Ravenpoint closed two percent down."),
   ('Speaker', 's', 'm2',
    "The case was built on what the two would save together. Management told the market to expect "
    "fifty-five million euros a year. Thirty of that was taking out engineering work being done "
    "twice, fifteen was a single sales force instead of two, and ten was shutting one of the two "
    "data centres."),
   ('Speaker', 's', 'm2',
    "The review of the books ran five weeks and turned up one thing worth telling the market about. "
    "Ledgerworks spread licence income over a year. Ravenpoint spread the same kind of income over "
    "two. Putting both onto one basis took nine million euros off the combined top line in the "
    "first year."),
   ('Speaker', 's', 'm2',
    "By year three, what had actually arrived was a little over half of what was promised. The "
    "engineering saving came through almost in full. The sales saving did not, because selling to a "
    "two-partner practice and selling to a group finance director are not the same job. And the data "
    "centre stayed open two years longer than planned, because the lease could not be ended early, "
    "which cost another seven million."),
   ('Speaker', 's', 'm2',
    "So the lesson. Savings that come from doing the same work once instead of twice are usually "
    "real. Savings that depend on customers behaving differently, or on getting out of a contract "
    "early, are the ones that slip. When you see one of these numbers in a press release, ask which "
    "of the two kinds it is. Thank you."),
  ],
  'questions': [
   {'q': 'What kind of takeover was this?',
    'o': ['Friendly, because both boards recommended it',
          'Hostile, because one board refused',
          'A management buyout', 'A joint venture'], 'a': 0,
    'e': u'"both boards put the deal to their own investors with a recommendation to accept it" '
         u'· คณะกรรมการทั้งสองฝ่ายเห็นชอบ คลิปไม่ได้พูดคำว่า friendly'},
   {'q': 'What did Ledgerworks shareholders receive?',
    'o': ['Zero point six Ravenpoint shares per share held',
          'Cash of four hundred and eighty million',
          'One Ravenpoint share per share held', 'Fourteen euros per share'], 'a': 0,
    'e': u'"six Ravenpoint shares for every ten they owned" คือ 6 หาร 10 เท่ากับ 0.6 ต่อหุ้น'},
   {'q': 'What multiple of earnings did the offer represent?',
    'o': ['Fourteen times', 'Twelve times', 'Twenty-four times', 'Two times'], 'a': 0,
    'e': u'"fourteen euros of price for every euro of annual profit"'},
   {'q': 'How did the market react on the day?',
    'o': ['Ravenpoint shares slipped slightly', 'Ravenpoint shares jumped sharply',
          'Ledgerworks shares were suspended', 'Neither share moved at all'], 'a': 0,
    'e': u'"The market barely reacted: Ravenpoint closed two percent down" '
         u'· ลงเล็กน้อย ไม่ใช่ไม่ขยับเลย'},
   {'q': 'Which saving was expected to be the largest?',
    'o': ['Removing duplicated engineering work', 'Running a single sales force',
          'Closing one of the data centres', 'Changing the licence income policy'], 'a': 0,
    'e': u'"Thirty of that was taking out engineering work being done twice" '
         u'· มากที่สุดในสามก้อน คือ 30 เทียบกับ 15 และ 10'},
   {'q': 'What did the review of the books find?',
    'o': ['The two firms spread licence income over different periods',
          'An unrecorded pension liability', 'A disputed patent',
          'An overstated receivable'], 'a': 0,
    'e': u'"Ledgerworks spread licence income over a year. Ravenpoint spread the same kind of '
         u'income over two" · คือนโยบายรับรู้รายได้ต่างกัน'},
   {'q': 'What effect did putting both onto one basis have?',
    'o': ['Reported combined revenue fell in the first year',
          'Reported combined revenue rose in the first year',
          'Goodwill increased by nine million', 'It had no effect on reported figures'], 'a': 0,
    'e': u'"took nine million euros off the combined top line in the first year" '
         u'· top line คือรายได้'},
   {'q': 'What were the savings actually achieved by year three?',
    'o': ['About thirty million euros a year', 'The full fifty-five million euros a year',
          'About seven million euros a year', 'Nothing at all'], 'a': 0,
    'e': u'"a little over half of what was promised" ของ 55 ล้าน จึงราวสามสิบต้น ๆ'},
   {'q': 'Why did the sales saving fail to arrive?',
    'o': ['The two customer groups needed different selling skills',
          'The sales team refused to merge', 'Customers cancelled their contracts',
          'The saving had been double counted'], 'a': 0,
    'e': u'"selling to a two-partner practice and selling to a group finance director are not the '
         u'same job"'},
   {'q': 'Which kind of saving does the speaker trust?',
    'o': ['Savings from removing duplicated work',
          'Savings that depend on customer behaviour',
          'Savings from leaving a contract early', 'Savings from tax planning'], 'a': 0,
    'e': u'"Savings that come from doing the same work once instead of twice are usually real"'},
  ]},
]},

# ══════════════════════════════════ ชุดที่ 3 ══════════════════════════════════
{'id': 'L3', 'title': u'ชุดที่ 3', 'parts': [

 {'id': 'L3a', 'kind': 'presentation',
  'title': 'A Skincare Launch in Brazil',
  'context': u'ทีมสามคนเสนอแผนเปิดตัวสกินแคร์ในบราซิล เน้นงบโฆษณาและกำไรส่วนเกิน',
  'turns': [
   ('Elena', 'e', 'f3',
    "Good afternoon. I'm Elena, and with me are Tomas and Rafael. We are proposing to launch our "
    "Calmara skincare line in Brazil, and I'll begin with why this market and not another."),
   ('Elena', 'e', 'f3',
    "Brazil is the fourth largest beauty market in the world. We put our questions to sixteen "
    "hundred women in three cities. Two findings stood out. People here know the imported names: "
    "six in ten could list at least three of them without help. But they do not stay with any of "
    "them. Two thirds had moved to a different brand within the past year."),
   ('Tomas', 't', 'm3',
    "Thanks, Elena. That second finding cuts both ways. We can take share quickly, and we can lose "
    "it again just as quickly. So the whole plan is built on getting the same woman to buy a second "
    "and a third time, not on one loud launch week."),
   ('Tomas', 't', 'm3',
    "One change to the product is not optional. The formula we sell in Europe sits far too heavily "
    "on the skin in the heat of the north of the country. Putting that right costs eight hundred "
    "thousand euros and pushes the launch back by a third of a year."),
   ('Rafael', 'r', 'm1',
    "Now the money. We have three point two million euros for advertising, spread over eighteen "
    "months. Seven euros in every ten go to video on people's phones, because television would put "
    "us in front of the wrong age group entirely."),
   ('Rafael', 'r', 'm1',
    "On unit economics, the price on the shelf is one hundred and forty reais. By the time the "
    "retailer and the tax authorities have taken their share, seventy-three reais reach us. Making "
    "it and shipping it costs thirty-one."),
   ('Rafael', 'r', 'm1',
    "To get the reformulation and the advertising back we have to move ninety-six thousand units. "
    "Our base case is a hundred and twelve thousand over those eighteen months, so we are carrying "
    "a cushion of roughly one unit in six. The risk I would watch is the retailer: three chains "
    "control seven tenths of everything sold, and all three look again at what they stock every six "
    "months. Thank you."),
  ],
  'questions': [
   {'q': 'What is brand awareness for imported skincare?',
    'o': ['About sixty percent', 'About seventy percent',
          'About thirty percent', 'About two thirds'], 'a': 0,
    'e': u'"six in ten could list at least three of them without help" คือราว 60 เปอร์เซ็นต์ '
         u'· สองในสามคือตัวเลขคนที่เปลี่ยนแบรนด์ คนละเรื่อง'},
   {'q': 'What does the switching figure show?',
    'o': ['Brand loyalty is low', 'Brand awareness is low',
          'The market is shrinking', 'Prices are falling'], 'a': 0,
    'e': u'"Two thirds had moved to a different brand within the past year" '
         u'· เปลี่ยนแบรนด์กันมาก แปลว่าไม่ภักดี คลิปไม่ได้พูดคำว่า loyalty'},
   {'q': 'What is the whole plan built on?',
    'o': ['Repeat purchase', 'A single large launch event',
          'Undercutting the local brands', 'Winning shelf space in pharmacies'], 'a': 0,
    'e': u'"getting the same woman to buy a second and a third time, not on one loud launch week"'},
   {'q': 'Why must the formula be changed?',
    'o': ['It is too heavy for the climate', 'The packaging breaks local rules',
          'Two ingredients are banned', 'It costs too much to make'], 'a': 0,
    'e': u'"sits far too heavily on the skin in the heat of the north of the country"'},
   {'q': 'How much does the reformulation delay the launch?',
    'o': ['About four months', 'About eight months',
          'About eighteen months', 'It causes no delay'], 'a': 0,
    'e': u'"pushes the launch back by a third of a year" · หนึ่งในสามของสิบสองเดือนคือสี่เดือน'},
   {'q': 'Where does most of the advertising budget go?',
    'o': ['Online video', 'Television', 'In-store promotion', 'Print magazines'], 'a': 0,
    'e': u'"Seven euros in every ten go to video on people\'s phones" คือวิดีโอออนไลน์'},
   {'q': 'Why is television rejected?',
    'o': ['It reaches the wrong age group', 'It is too expensive',
          'It is not available nationally', 'The retailers forbid it'], 'a': 0,
    'e': u'"television would put us in front of the wrong age group entirely"'},
   {'q': 'What is the contribution per unit?',
    'o': ['Forty-two reais', 'Thirty-one reais',
          'Seventy-three reais', 'One hundred and forty reais'], 'a': 0,
    'e': u'73 ที่ได้รับจริง ลบต้นทุน 31 เท่ากับ 42 เรอัล · 140 คือราคาบนชั้นวาง ไม่ใช่เงินที่เข้าบริษัท'},
   {'q': 'What margin of safety does the base case give?',
    'o': ['About seventeen percent above break-even',
          'About six percent above break-even',
          'About thirty percent above break-even', 'None; the base case is below break-even'], 'a': 0,
    'e': u'"a cushion of roughly one unit in six" · หนึ่งในหกคือราว 17 เปอร์เซ็นต์'},
   {'q': 'What risk does Rafael single out?',
    'o': ['A few chains control most of the distribution',
          'The exchange rate', 'The cost of online video',
          'A competitor launching first'], 'a': 0,
    'e': u'"three chains control seven tenths of everything sold" '
         u'· และยังทบทวนรายการสินค้าทุกหกเดือน อำนาจต่อรองจึงอยู่ที่ร้าน'},
  ]},

 {'id': 'L3b', 'kind': 'talk',
  'title': 'A Bid That Failed',
  'context': u'วิทยากรเล่ากรณีข้อเสนอซื้อกิจการที่ล้มเหลว เน้นเกณฑ์การตอบรับของผู้ถือหุ้น',
  'turns': [
   ('Speaker', 's', 'm2',
    "Most of the cases you read about are deals that completed. Today I want to do the opposite and "
    "look at one that failed, because a failed bid shows you where the real obstacles sit."),
   ('Speaker', 's', 'm2',
    "The target was Kestrel Instruments, a listed maker of measuring equipment. The buyer was a "
    "private equity fund called Braemar Capital. In April it quietly bought nine point eight percent "
    "of the company, and that number is not an accident. Ten is the level at which that market makes "
    "you announce yourself."),
   ('Speaker', 's', 'm2',
    "In June it bid six pounds twenty a share, which put a value of eight hundred and sixty million "
    "pounds on the whole business. Measured against the price before anyone knew Braemar was there, "
    "that was thirty-one percent on top."),
   ('Speaker', 's', 'm2',
    "The board said no, and its reason was specific. Kestrel had put four years and a hundred and "
    "ten million pounds into a new sensor platform that had not yet earned a single pound of income, "
    "and the board's case was that the offer valued all of that work at nothing."),
   ('Speaker', 's', 'm2',
    "Braemar lifted the offer once, to six pounds seventy-five, and made it conditional on three "
    "quarters of the company being tendered to it. Two institutions holding thirty-one percent "
    "between them said in public that they would not sell. From that moment the arithmetic could not "
    "work."),
   ('Speaker', 's', 'm2',
    "The bid lapsed in September. Braemar sold out over the following four months and made a little "
    "money doing it. Kestrel ended the year about nine percent above where it had started."),
   ('Speaker', 's', 'm2',
    "Three things to take away. First, a condition like that is a real constraint, not a formality. "
    "Second, putting a value on work that has cost a great deal and earned nothing yet is where "
    "target boards and bidders argue most often. Third, notice who actually settled this. Not the "
    "board. The board can recommend, or refuse to, but it cannot accept on anybody else's behalf. "
    "Thank you."),
  ],
  'questions': [
   {'q': 'What size stake did Braemar build in April?',
    'o': ['Just under ten percent', 'Just over ten percent',
          'About a third', 'Three quarters'], 'a': 0,
    'e': u'"nine point eight percent" ซึ่งต่ำกว่าสิบเล็กน้อย'},
   {'q': 'Why did it stop where it did?',
    'o': ['To avoid having to disclose the holding', 'To reduce the tax on the purchase',
          'Because it ran out of money', 'Because the board refused to sell more'], 'a': 0,
    'e': u'"Ten is the level at which that market makes you announce yourself" '
         u'· ซื้อต่ำกว่านั้นจึงยังไม่ต้องเปิดเผยตัว'},
   {'q': 'What premium did the opening offer carry?',
    'o': ['Around a third above the undisturbed price',
          'Around a tenth above the undisturbed price',
          'Around half above the undisturbed price', 'It was offered at a discount'], 'a': 0,
    'e': u'"that was thirty-one percent on top" · undisturbed price คือราคาก่อนตลาดรู้ข่าว'},
   {'q': 'What was the board’s objection?',
    'o': ['The offer put no value on the new sensor platform',
          'The bidder was based abroad',
          'The offer was in shares rather than cash', 'The timing clashed with the year end'], 'a': 0,
    'e': u'"the offer valued all of that work at nothing"'},
   {'q': 'What was unusual about the sensor platform?',
    'o': ['It had cost a great deal but earned nothing yet',
          'It had already been sold to a rival',
          'It was fully written off in the accounts', 'It belonged to a joint venture'], 'a': 0,
    'e': u'"four years and a hundred and ten million pounds … had not yet earned a single pound of '
         u'income"'},
   {'q': 'What acceptance condition did Braemar set?',
    'o': ['Seventy-five percent of the shares', 'Fifty percent of the shares',
          'Thirty-one percent of the shares', 'Ninety percent of the shares'], 'a': 0,
    'e': u'"conditional on three quarters of the company being tendered" · สามในสี่คือ 75 เปอร์เซ็นต์'},
   {'q': 'Why could the condition not be met?',
    'o': ['Two holders of thirty-one percent refused to sell',
          'The regulator blocked the deal', 'Braemar withdrew the offer',
          'The board bought back its own shares'], 'a': 0,
    'e': u'ถ้า 31 เปอร์เซ็นต์ไม่ขาย ที่เหลือมีไม่ถึง 75 เปอร์เซ็นต์ เงื่อนไขจึงเป็นไปไม่ได้'},
   {'q': 'What happened to Braemar’s holding afterwards?',
    'o': ['It was sold at a small profit', 'It was kept in full',
          'It was sold at a loss', 'It was transferred to the board'], 'a': 0,
    'e': u'"sold out over the following four months and made a little money doing it"'},
   {'q': 'Who settled the outcome, according to the speaker?',
    'o': ['The shareholders', 'The board of directors',
          'The regulator', 'The bidder’s own investors'], 'a': 0,
    'e': u'"Not the board. The board can recommend, or refuse to, but it cannot accept on anybody '
         u'else\'s behalf" · คนที่ตอบรับได้คือเจ้าของหุ้น'},
   {'q': 'What does the speaker say about acceptance conditions?',
    'o': ['They are a genuine obstacle, not a formality',
          'They are almost always waived', 'They are set by the target board',
          'They only apply to private companies'], 'a': 0,
    'e': u'"a condition like that is a real constraint, not a formality"'},
  ]},
]},

# ══════════════════════════════════ ชุดที่ 4 ══════════════════════════════════
{'id': 'L4', 'title': u'ชุดที่ 4', 'parts': [

 {'id': 'L4a', 'kind': 'presentation',
  'title': 'Repositioning a Budget Airline',
  'context': u'สองคนเสนอแผนปรับตำแหน่งสายการบินต้นทุนต่ำ เน้นต้นทุนต่อที่นั่งและอัตราบรรทุก',
  'turns': [
   ('Priya', 'p', 'f1',
    "Good morning. I'm Priya, and Marcus will join me shortly. Our subject is positioning: whether "
    "Skylark, which has sold nothing but cheap seats for eleven years, should move up the market."),
   ('Priya', 'p', 'f1',
    "The problem shows up in one place. Nearly nine seats in ten are sold on an average flight, "
    "which is about as good as this industry gets. And yet the average fare has gone down in each "
    "of the last three years. We are filling the aircraft by cutting the price, and that is not a "
    "strategy, it is a habit."),
   ('Priya', 'p', 'f1',
    "Our research found something useful. Business travellers were about a quarter of our passengers "
    "five years ago. Today they are getting on for half. They pick us for the timetable, not for the "
    "fare, and they are the least price sensitive people on the aircraft."),
   ('Marcus', 'm', 'm2',
    "Thanks, Priya. So the proposal is a partial repositioning. Keep the low cost base exactly as it "
    "is, but add a second fare: the seat beside you stays empty, you get on the aircraft first, and "
    "you can move to another flight without paying again."),
   ('Marcus', 'm', 'm2',
    "The economics are straightforward. It costs us four point one cents to fly one seat one "
    "kilometre, which is about as low as anyone in this region gets. Leaving the middle seat empty "
    "pushes the cost of each seat we do sell in that row up by half. But we would sell the new fare "
    "at two point three times the ordinary one."),
   ('Marcus', 'm', 'm2',
    "We modelled it on twelve routes. Sell a little over one seat in ten at the new fare and revenue "
    "per flight goes up nine percent. Sell fewer than eight in every hundred and we are worse off "
    "than we are today."),
   ('Marcus', 'm', 'm2',
    "The real risk is not the cost. It is what people already think we are. Eleven years of "
    "advertising have told this market one single thing about us, and a brand that says two things "
    "loses both ends of the market. So we would put it on four routes for six months under a "
    "different fare name, and decide nothing until we see that. Thank you."),
  ],
  'questions': [
   {'q': 'What is Skylark’s load factor?',
    'o': ['About eighty-nine percent', 'About forty-four percent',
          'About twenty-six percent', 'About eleven percent'], 'a': 0,
    'e': u'"Nearly nine seats in ten are sold on an average flight" คือราว 89 เปอร์เซ็นต์ '
         u'· load factor แปลว่าอัตราการขายที่นั่ง'},
   {'q': 'How has the share of business passengers changed?',
    'o': ['It has risen from about a quarter to nearly a half',
          'It has fallen from about a half to a quarter',
          'It has stayed at about a quarter', 'It has doubled every year'], 'a': 0,
    'e': u'"about a quarter of our passengers five years ago. Today they are getting on for half"'},
   {'q': 'Why do business travellers choose Skylark?',
    'o': ['For the schedule', 'For the price', 'For the loyalty scheme', 'For the seat width'], 'a': 0,
    'e': u'"They pick us for the timetable, not for the fare" · timetable คือตารางบิน'},
   {'q': 'What does the new fare include?',
    'o': ['An empty middle seat, priority boarding and a changeable ticket',
          'Lounge access and extra baggage',
          'A meal and a fully refundable ticket', 'A front seat and free wifi'], 'a': 0,
    'e': u'"the seat beside you stays empty, you get on the aircraft first, and you can move to '
         u'another flight without paying again"'},
   {'q': 'What is the cost per available seat kilometre?',
    'o': ['Just over four cents', 'Just over two cents',
          'Just over nine cents', 'Just over eleven cents'], 'a': 0,
    'e': u'"four point one cents to fly one seat one kilometre" · จุดหนึ่งคือเศษเล็กน้อย '
         u'จึงเป็นสี่เซนต์กว่า ๆ ไม่ใช่สี่เซนต์พอดี'},
   {'q': 'What happens to the cost of each seat sold in those rows?',
    'o': ['It rises by about half', 'It falls by about half',
          'It rises by about nine percent', 'It is unchanged'], 'a': 0,
    'e': u'"pushes the cost of each seat we do sell in that row up by half" '
         u'· เพราะขายได้สองที่แทนที่จะเป็นสาม'},
   {'q': 'How is the new fare priced?',
    'o': ['At more than twice the ordinary fare', 'At half as much again as the ordinary fare',
          'At nine percent above the ordinary fare', 'At the same level as the ordinary fare'], 'a': 0,
    'e': u'"two point three times the ordinary one" คือมากกว่าสองเท่า'},
   {'q': 'What take-up is needed for revenue per flight to rise nine percent?',
    'o': ['About eleven percent of seats', 'About eight percent of seats',
          'About twelve percent of seats', 'About half the seats'], 'a': 0,
    'e': u'"a little over one seat in ten" คือมากกว่าสิบเปอร์เซ็นต์เล็กน้อย '
         u'· สิบสองคือจำนวนเส้นทางที่ใช้ทดลอง ไม่ใช่สัดส่วนที่นั่ง'},
   {'q': 'Below what take-up is the airline worse off than today?',
    'o': ['Eight percent of seats', 'Eleven percent of seats',
          'Nine percent of seats', 'Four percent of seats'], 'a': 0,
    'e': u'"Sell fewer than eight in every hundred and we are worse off than we are today"'},
   {'q': 'What does Marcus say the real risk is?',
    'o': ['Damage to the brand image', 'The cost of the empty middle seat',
          'Crew scheduling', 'The fuel price'], 'a': 0,
    'e': u'"It is what people already think we are … a brand that says two things loses both ends"'},
  ]},

 {'id': 'L4b', 'kind': 'talk',
  'title': 'A Management Buyout',
  'context': u'วิทยากรเล่ากรณีผู้บริหารซื้อกิจการโรงพิมพ์ เน้นโครงสร้างเงินกู้และเงื่อนไขของธนาคาร',
  'turns': [
   ('Speaker', 's', 'm1',
    "In this case the buyers already worked in the building, and I want you to watch the funding "
    "structure the whole way through, because in a deal like this the structure is the story."),
   ('Speaker', 's', 'm1',
    "Thornbury Print was a commercial printing group sitting inside a larger media company. The "
    "parent decided it no longer belonged there, because printing was not what the group was about "
    "any more. Rather than sell to a competitor, it agreed a sale to five of Thornbury's own senior "
    "managers."),
   ('Speaker', 's', 'm1',
    "The price was seventy-two million pounds. The five managers could find three million of it "
    "between them. Forty-four million came from the bank. A private equity fund put in the other "
    "twenty-five and took sixty-eight percent of the shares."),
   ('Speaker', 's', 'm1',
    "Now look at what that structure does. Five people who used to run this company for a salary now "
    "own a bit under a third of it. But the business is carrying forty-four million of debt that was "
    "not there before, and the interest bill is close to four times what it used to be."),
   ('Speaker', 's', 'm1',
    "The bank attached two conditions. Net debt was not to go above three and a half times earnings "
    "before interest, tax, depreciation and amortisation. And interest cover was not to fall below "
    "three times. Both were tested every quarter."),
   ('Speaker', 's', 'm1',
    "In year two a large customer went digital and volume dropped eleven percent. Earnings went with "
    "it, and the net debt ratio touched three point four. Nobody had to ring the bank that quarter, "
    "but one poor quarter more and somebody would have. The managers spent that whole year running "
    "the balance sheet instead of running the business."),
   ('Speaker', 's', 'm1',
    "They got out of it by selling two sites for nine million and using the cash to pay down debt. "
    "The fund sold out in year six at a valuation of a hundred and thirty million, so the deal "
    "worked. But keep this. The printing business was exactly as risky the day after the sale as it "
    "had been the day before. Everything that was added came from the way it was paid for. Thank "
    "you."),
  ],
  'questions': [
   {'q': 'What kind of transaction does the speaker describe?',
    'o': ['A management buyout', 'A hostile takeover',
          'A merger of equals', 'A joint venture'], 'a': 0,
    'e': u'"the buyers already worked in the building" และ "a sale to five of Thornbury\'s own '
         u'senior managers" · ผู้บริหารเดิมซื้อกิจการที่ตนบริหารอยู่'},
   {'q': 'Why did the parent company sell Thornbury Print?',
    'o': ['Printing no longer fitted the group', 'The business was making a loss',
          'A regulator required the sale', 'The managers threatened to resign'], 'a': 0,
    'e': u'"printing was not what the group was about any more" คือไม่ใช่ธุรกิจหลักอีกต่อไป'},
   {'q': 'Roughly what share of the price did the managers fund themselves?',
    'o': ['About four percent', 'About a third', 'About two thirds', 'About a quarter'], 'a': 0,
    'e': u'3 ล้าน จาก 72 ล้าน คือราวสี่เปอร์เซ็นต์ · คลิปให้ตัวเลขสองตัว แต่ไม่ได้บอกสัดส่วน'},
   {'q': 'What shareholding did the managers end up with?',
    'o': ['A little under thirty percent', 'A little under seventy percent',
          'Exactly half', 'About four percent'], 'a': 0,
    'e': u'"own a bit under a third of it" · หนึ่งในสามคือราว 33 ต่ำกว่านั้นจึงราว 28 ถึง 30'},
   {'q': 'What happened to the interest bill?',
    'o': ['It rose to nearly four times its old level', 'It fell by about a quarter',
          'It stayed the same', 'It was fixed for six years'], 'a': 0,
    'e': u'"the interest bill is close to four times what it used to be"'},
   {'q': 'What were the two bank covenants?',
    'o': ['Net debt below three and a half times earnings, and interest cover above three times',
          'Net debt below three times, and interest cover above three and a half times',
          'Net debt below eleven percent, and interest cover above four times',
          'A minimum cash balance and a ban on dividends'], 'a': 0,
    'e': u'"Net debt was not to go above three and a half times earnings … interest cover was not '
         u'to fall below three times" · ระวังสลับตัวเลขสองตัว'},
   {'q': 'What does the speaker imply about year two?',
    'o': ['The company came close to breaching a covenant',
          'The company breached a covenant', 'The bank withdrew the facility',
          'The fund sold its stake early'], 'a': 0,
    'e': u'"Nobody had to ring the bank that quarter, but one poor quarter more and somebody would '
         u'have" · แปลว่าเฉียดแต่ยังไม่ผิดเงื่อนไข'},
   {'q': 'What did the managers spend year two doing?',
    'o': ['Managing the balance sheet rather than the business',
          'Looking for a buyer', 'Renegotiating the covenants',
          'Cutting the workforce'], 'a': 0,
    'e': u'"running the balance sheet instead of running the business"'},
   {'q': 'How did the company recover?',
    'o': ['It sold two sites and reduced its borrowings',
          'It raised new equity from the fund', 'It renegotiated the covenants',
          'It closed the loss-making division'], 'a': 0,
    'e': u'"selling two sites for nine million and using the cash to pay down debt"'},
   {'q': 'What is the speaker’s main point about buyouts?',
    'o': ['The added risk comes from the funding, not from the operations',
          'Managers always pay too much', 'Bank covenants are rarely enforced',
          'Private equity funds exit too early'], 'a': 0,
    'e': u'"The printing business was exactly as risky the day after the sale as it had been the '
         u'day before. Everything that was added came from the way it was paid for"'},
  ]},
]},

# ══════════════════════════════════ ชุดที่ 5 ══════════════════════════════════
{'id': 'L5', 'title': u'ชุดที่ 5', 'parts': [

 {'id': 'L5a', 'kind': 'presentation',
  'title': 'Market Research Findings for Indonesia',
  'context': u'สามคนรายงานผลวิจัยตลาดอินโดนีเซียก่อนตัดสินใจลงทุน พร้อมข้อจำกัดของงานวิจัย',
  'turns': [
   ('Sasha', 's', 'f2',
    "Good morning. I'm Sasha. This is a research report, not a recommendation. Arun and Laila will "
    "take the findings themselves. I will start with what we did and what this study cannot tell "
    "you."),
   ('Sasha', 's', 'f2',
    "We put the questions to two thousand four hundred households across five provinces, and we ran "
    "eight group discussions alongside that. It cost a hundred and ninety thousand dollars, and the "
    "fieldwork ran from the middle of January to the very start of April. One limitation matters "
    "more than the rest: every single person we spoke to lives in a town. Nothing in here tells you "
    "anything about the villages."),
   ('Arun', 'a', 'm3',
    "Thanks, Sasha. The headline is that the category is adding seven percent a year, but that "
    "growth is not spread out. Two of the five provinces account for very nearly two thirds of it. "
    "Plan national distribution from day one and you will be paying to reach demand that has not "
    "arrived yet."),
   ('Arun', 'a', 'm3',
    "On price, the finding was sharper than we expected. Below thirty-five thousand rupiah a unit, "
    "the price barely affects what people choose at all. Go above that line and a ten percent "
    "increase takes almost a third off stated purchase intention."),
   ('Laila', 'l', 'f3',
    "I'll take brand and channel. Nearly eight people in ten can name the category leader without "
    "prompting. But when we asked which brand they had actually bought last time, the leader came "
    "out at just over four in ten. The space between those two numbers is the opening."),
   ('Laila', 'l', 'f3',
    "On channel, seven purchases in every ten happen in small independent shops rather than modern "
    "retail. That changes the whole distribution cost, because you cannot serve shops like that "
    "yourself. You need somebody in between, and in this market they take a little under a fifth."),
   ('Laila', 'l', 'f3',
    "Two things we could not answer. We did not test packaging, because the samples were not ready "
    "in time. And because we only went out into the field once, we have nothing at all on whether "
    "the same household buys a second time. If the board wants that, it is a second study and about "
    "four months. Thank you."),
  ],
  'questions': [
   {'q': 'What limitation does Sasha flag?',
    'o': ['The sample covers only urban households', 'The sample was too small',
          'The fieldwork was rushed', 'Only one province was covered'], 'a': 0,
    'e': u'"every single person we spoke to lives in a town. Nothing in here tells you anything '
         u'about the villages"'},
   {'q': 'How long did the fieldwork take?',
    'o': ['About eleven weeks', 'About four weeks', 'About six months', 'About a year'], 'a': 0,
    'e': u'"from the middle of January to the very start of April" คือราวสองเดือนครึ่งถึงสามเดือน '
         u'หรือราวสิบเอ็ดสัปดาห์'},
   {'q': 'How is the category’s growth distributed?',
    'o': ['Most of it sits in two of the five provinces',
          'It is spread evenly across the five provinces',
          'It is concentrated in the villages', 'It is falling outside the cities'], 'a': 0,
    'e': u'"Two of the five provinces account for very nearly two thirds of it"'},
   {'q': 'What does Arun warn about national distribution?',
    'o': ['You would pay to reach demand that is not there yet',
          'It is cheaper than regional distribution',
          'It is blocked by local regulation', 'It requires a joint venture'], 'a': 0,
    'e': u'"you will be paying to reach demand that has not arrived yet"'},
   {'q': 'What happens above thirty-five thousand rupiah a unit?',
    'o': ['Buyers become very sensitive to price',
          'Buyers stop noticing the price', 'Demand rises sharply',
          'The distributor takes a larger margin'], 'a': 0,
    'e': u'ต่ำกว่าเส้นนี้ราคาแทบไม่มีผล แต่เหนือเส้นนี้ขึ้นราคา 10 เปอร์เซ็นต์ '
         u'"takes almost a third off stated purchase intention"'},
   {'q': 'What does a ten percent price rise above that line do?',
    'o': ['It cuts stated purchase intention by roughly thirty percent',
          'It cuts stated purchase intention by roughly ten percent',
          'It has almost no effect', 'It raises revenue by roughly a third'], 'a': 0,
    'e': u'"takes almost a third off stated purchase intention" · หนึ่งในสามคือราว 30 เปอร์เซ็นต์'},
   {'q': 'What is brand awareness for the category leader?',
    'o': ['Almost eighty percent', 'Just over forty percent',
          'Seven in ten', 'Nearly two thirds'], 'a': 0,
    'e': u'"Nearly eight people in ten can name the category leader without prompting" '
         u'· สี่ในสิบคือสัดส่วนคนที่ซื้อจริง ไม่ใช่คนที่รู้จัก'},
   {'q': 'What does Laila call the opening for a new entrant?',
    'o': ['The gap between knowing a brand and actually buying it',
          'The low price of the leader', 'The weakness of modern retail',
          'The absence of advertising'], 'a': 0,
    'e': u'รู้จัก 8 ใน 10 แต่ซื้อจริง 4 ใน 10 · "The space between those two numbers is the opening"'},
   {'q': 'What margin does the middleman take in this market?',
    'o': ['About eighteen percent', 'About seven percent',
          'About thirty percent', 'About forty percent'], 'a': 0,
    'e': u'"they take a little under a fifth" · หนึ่งในห้าคือ 20 ต่ำกว่านั้นเล็กน้อยจึงราว 18'},
   {'q': 'Which question could the study not answer?',
    'o': ['Repeat purchase', 'Price sensitivity', 'Brand awareness', 'Channel share'], 'a': 0,
    'e': u'"we have nothing at all on whether the same household buys a second time" '
         u'· การซื้อซ้ำคือ repeat purchase ซึ่งคลิปไม่ได้เอ่ยชื่อ'},
  ]},

 {'id': 'L5b', 'kind': 'talk',
  'title': 'A Joint Venture in Batteries',
  'context': u'วิทยากรเล่ากรณีกิจการร่วมค้าผลิตแบตเตอรี่ เน้นความต่างจากการซื้อกิจการและวิธีบันทึกบัญชี',
  'turns': [
   ('Speaker', 's', 'f2',
    "For the last case, two companies built something together without either of them buying the "
    "other. I have kept it until the end because students routinely mix this up with a takeover. It "
    "is not the same thing, and the accounting is not the same either."),
   ('Speaker', 's', 'f2',
    "Caldera Motors makes vehicles. Sentinel Chemical makes materials. Neither bought the other. "
    "They each put money into a brand new company, Voltrek, which builds battery cells."),
   ('Speaker', 's', 'f2',
    "Each side put in four hundred and twenty million dollars, and each ended up with exactly half. "
    "Caldera handed over a site as part of its share, and that site was valued at sixty million."),
   ('Speaker', 's', 'f2',
    "Here is the point that matters for your accounting. Because neither one is in charge, neither "
    "one brings Voltrek's assets and liabilities onto its own balance sheet. Each shows what it owns "
    "as a single line in the balance sheet and a single line in the income statement. Had one of "
    "them simply bought the other out, the whole of Voltrek would have come in."),
   ('Speaker', 's', 'f2',
    "Why do it this way? Three reasons. The plant cost more than either wanted sitting on its own "
    "balance sheet. Each brings what the other has not got, Caldera the customers and Sentinel the "
    "chemistry. And the technology may simply not win, so both wanted a ceiling on what they could "
    "lose."),
   ('Speaker', 's', 'f2',
    "The weakness is governance. Split something down the middle and a real disagreement has nothing "
    "to break it. Here they named an independent chairman with a casting vote, but only on running "
    "the business day to day. Spending capital still needs both of them to agree."),
   ('Speaker', 's', 'f2',
    "And in year three they did disagree, about whether to double the size of the plant. Sentinel "
    "wanted to; Caldera did not. It was a capital decision, so the chairman's vote was no help at "
    "all, and the expansion sat still for fourteen months. When you read one of these agreements, "
    "look at what happens when the two sides cannot agree, before you look at the profit forecast. "
    "Thank you."),
  ],
  'questions': [
   {'q': 'What kind of arrangement is described?',
    'o': ['A joint venture', 'An acquisition', 'A merger', 'A management buyout'], 'a': 0,
    'e': u'"two companies built something together without either of them buying the other" '
         u'· ลงทุนร่วมกันตั้งกิจการใหม่ คลิปไม่ได้เอ่ยชื่อศัพท์นี้เลย'},
   {'q': 'What was Caldera’s contribution in cash?',
    'o': ['Three hundred and sixty million dollars', 'Four hundred and twenty million dollars',
          'Sixty million dollars', 'Four hundred and eighty million dollars'], 'a': 0,
    'e': u'420 ลบที่ดิน 60 เหลือเงินสด 360 ล้าน · คลิปให้ตัวเลขสองตัวแต่ไม่ได้พูดผลลัพธ์'},
   {'q': 'What does the fifty-fifty split tell you?',
    'o': ['Neither party controls Voltrek', 'Caldera controls Voltrek',
          'Voltrek controls both parents', 'Voltrek is a subsidiary of Sentinel'], 'a': 0,
    'e': u'"Because neither one is in charge" · ถือคนละครึ่ง จึงไม่มีใครมีอำนาจควบคุม'},
   {'q': 'How does each party report its interest?',
    'o': ['Using the equity method', 'By full consolidation',
          'At cost less impairment', 'As a finance lease'], 'a': 0,
    'e': u'"a single line in the balance sheet and a single line in the income statement" '
         u'· นั่นคือวิธีส่วนได้เสีย ซึ่งคลิปอธิบายอาการแต่ไม่ได้เรียกชื่อ'},
   {'q': 'What would be different if one party had bought the other out?',
    'o': ['All of Voltrek’s assets and liabilities would be brought in',
          'Goodwill would be ignored', 'No accounting entries would be needed',
          'Only the cash paid would be shown'], 'a': 0,
    'e': u'"the whole of Voltrek would have come in" คือการนำมารวมทั้งหมด'},
   {'q': 'What does Caldera bring to the venture?',
    'o': ['The demand for the product', 'The chemistry',
          'The financing', 'The management team'], 'a': 0,
    'e': u'"Caldera the customers and Sentinel the chemistry" · ลูกค้าคืออุปสงค์'},
   {'q': 'Why did both sides prefer this to a takeover?',
    'o': ['Each wanted to cap its possible losses',
          'They wanted to avoid paying tax', 'The regulator would not allow a takeover',
          'Neither could raise any finance'], 'a': 0,
    'e': u'"the technology may simply not win, so both wanted a ceiling on what they could lose"'},
   {'q': 'What is the weakness of an equal split?',
    'o': ['A real disagreement has no tiebreaker',
          'Neither side can sell its shares', 'Profits cannot be distributed',
          'The venture cannot borrow'], 'a': 0,
    'e': u'"a real disagreement has nothing to break it"'},
   {'q': 'What does the chairman’s casting vote not cover?',
    'o': ['Capital expenditure decisions', 'Day-to-day operations',
          'Appointing directors', 'Setting salaries'], 'a': 0,
    'e': u'"only on running the business day to day. Spending capital still needs both of them to '
         u'agree"'},
   {'q': 'What was the result of the year three disagreement?',
    'o': ['The expansion was held up for more than a year',
          'Sentinel sold its share', 'The venture was wound up',
          'Caldera took full control'], 'a': 0,
    'e': u'"the expansion sat still for fourteen months" · สิบสี่เดือนคือเกินหนึ่งปี'},
  ]},
]},

]
