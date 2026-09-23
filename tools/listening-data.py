# -*- coding: utf-8 -*-
u"""บทฟังสำหรับ Part III · Listening ของวิชาภาษาอังกฤษ

แต่ละชุดมีสองส่วนตามแนวข้อสอบจริง
  presentation · การนำเสนอกลุ่มเรื่อง international marketing หลายคนพูดสลับกัน
  talk         · การบรรยายเรื่อง merger case คนเดียวพูดตลอด

ทุกบทตั้งใจใส่ศัพท์จาก Unit 2 และ Unit 12 ให้หนาแน่น เพราะข้อสอบวัดการฟังจับรายละเอียด
ที่ผูกกับศัพท์เหล่านั้นโดยตรง

── เขียนให้เหมาะกับนิสิตบัญชีชั้นปีที่ 3 ──
ประเภทของบททั้งสองแบบเปลี่ยนไม่ได้ เพราะแนวข้อสอบล็อกไว้ แต่สิ่งที่เปลี่ยนได้คือ
รายละเอียดที่ถูกถาม จึงย้ายไปเป็นตัวเลขที่นิสิตบัญชีอ่านออกทันที เช่น อัตรากำไรขั้นต้น
จุดคุ้มทุน ระยะเวลาคืนทุน เงินลงทุน ค่าความนิยม ต้นทุนการรวมกิจการ และวันที่เริ่มนำมารวมงบ

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
    "ready meals into Vietnam. I'll cover the market research, Daniel will take segmentation and "
    "positioning, and Preecha will finish with the numbers and the risks."),
   ('Mai', 'm', 'f1',
    "We carried out market research in four cities over three months. We used two methods: a "
    "questionnaire completed by two thousand shoppers, and six focus groups. The headline finding "
    "is that the chilled ready meal market is growing at about nine percent a year. But it is also "
    "increasingly competitive. The market leader already holds thirty-one percent market share, "
    "and two international brands entered last year."),
   ('Daniel', 'd', 'm1',
    "Thanks, Mai. So who are we selling to? Our customer profile is narrow: urban office workers "
    "between twenty-two and thirty-five who buy from convenience stores rather than supermarkets. "
    "That segment is only twelve percent of all buyers, but it spends nearly double the average."),
   ('Daniel', 'd', 'm1',
    "On brand positioning, we will not compete on price. The budget end is crowded and the margins "
    "are thin. We will position Freshline as a premium product at roughly twenty percent above the "
    "average shelf price, and build brand awareness around ingredient quality."),
   ('Preecha', 'p', 'm2',
    "Thank you, Daniel. Now the numbers, because this is where the plan lives or dies. Capital "
    "expenditure is four point five million dollars, almost all of it the chilled distribution "
    "network. Our gross margin at the premium price is thirty-eight percent, against twenty-two "
    "percent if we sold at the average price."),
   ('Preecha', 'p', 'm2',
    "We break even in month nineteen, and the payback period on the full investment is three years "
    "and two months. The advertising budget is one point one million dollars in year one, then it "
    "falls to six hundred thousand from year two onwards."),
   ('Preecha', 'p', 'm2',
    "Three risks. First, the cold chain: any failure destroys both the stock and the brand image. "
    "Second, the market leader could start a price war, which would cut our margin to about "
    "twenty-five percent. Third, our distributor handles eight thousand retail outlets, so a single "
    "contract dispute would stop national distribution overnight. We recommend a pilot in two cities "
    "first. Thank you. We are happy to take questions."),
  ],
  'questions': [
   {'q': 'How long did the market research take?',
    'o': ['Three months', 'Three weeks', 'Nine months', 'Two years'], 'a': 0,
    'e': '"market research in four cities over three months"'},
   {'q': 'Which two research methods did the team use?',
    'o': ['A questionnaire and focus groups', 'Interviews and a questionnaire',
          'Focus groups and in-store trials', 'A questionnaire and shelf audits'], 'a': 0,
    'e': '"a questionnaire completed by two thousand shoppers, and six focus groups"'},
   {'q': 'What share does the market leader hold?',
    'o': ['Thirty-one percent', 'Thirteen percent', 'Twelve percent', 'Twenty-two percent'], 'a': 0,
    'e': '"The market leader already holds thirty-one percent market share"'},
   {'q': 'Where does the target segment usually buy?',
    'o': ['At convenience stores', 'At supermarkets', 'Online', 'At wholesale markets'], 'a': 0,
    'e': '"who buy from convenience stores rather than supermarkets"'},
   {'q': 'How much is the planned capital expenditure?',
    'o': ['Four point five million dollars', 'Four point five million a year',
          'One point one million dollars', 'Six hundred thousand dollars'], 'a': 0,
    'e': '"Capital expenditure is four point five million dollars"'},
   {'q': 'What gross margin does the premium price give?',
    'o': ['Thirty-eight percent', 'Twenty-two percent', 'Twenty-five percent', 'Thirty-one percent'], 'a': 0,
    'e': '"Our gross margin at the premium price is thirty-eight percent"'},
   {'q': 'When does the plan break even?',
    'o': ['In month nineteen', 'In month nine', 'After three years and two months', 'In year two'], 'a': 0,
    'e': '"We break even in month nineteen" · อย่าสับสนกับระยะคืนทุน'},
   {'q': 'What happens to the advertising budget after year one?',
    'o': ['It falls to six hundred thousand', 'It rises to one point one million',
          'It stays the same', 'It is cut to zero'], 'a': 0,
    'e': '"then it falls to six hundred thousand from year two onwards"'},
   {'q': 'What would a price war do to the margin?',
    'o': ['Cut it to about twenty-five percent', 'Cut it to about twenty-two percent',
          'Raise it to thirty-eight percent', 'Leave it unchanged'], 'a': 0,
    'e': '"which would cut our margin to about twenty-five percent"'},
   {'q': 'What does the team finally recommend?',
    'o': ['A pilot in two cities first', 'A national launch straight away',
          'Selling at the average shelf price', 'Changing distributor'], 'a': 0,
    'e': '"We recommend a pilot in two cities first"'},
  ]},

 {'id': 'L1b', 'kind': 'talk',
  'title': 'A Takeover in Regional Logistics',
  'context': u'วิทยากรเล่ากรณีซื้อกิจการขนส่งภูมิภาค เน้นสิ่งที่พบตอน due diligence และค่าความนิยม',
  'turns': [
   ('Speaker', 's', 'm3',
    "Good afternoon. Today I want to walk you through a takeover in regional logistics, because it "
    "shows how much of a deal is decided by the accounting work rather than by the strategy."),
   ('Speaker', 's', 'm3',
    "In February, a listed transport group called Northvale made a bid for a family-owned company, "
    "Harbour Freight. The opening offer was two hundred and forty million pounds. The board of "
    "Harbour Freight rejected the bid within nine days, saying it undervalued the depot network."),
   ('Speaker', 's', 'm3',
    "Northvale then went directly to the shareholders, so a friendly approach became a hostile "
    "takeover. It raised the offer twice, first to two hundred and seventy million and finally to "
    "three hundred and ten million pounds. That final price was eleven times earnings."),
   ('Speaker', 's', 'm3',
    "Now to due diligence, which took seven weeks. The buyer's accountants found two things. First, "
    "repair obligations on forty leased vehicles had never been recorded, worth about six million "
    "pounds. Second, one large customer, who provided twenty-eight percent of revenue, had already "
    "given notice to leave."),
   ('Speaker', 's', 'm3',
    "Those findings did not stop the deal, but they changed it. The price stayed at three hundred "
    "and ten million, and instead thirty million was held back for eighteen months against any "
    "further claims."),
   ('Speaker', 's', 'm3',
    "The deal completed on the first of July, and Harbour Freight was consolidated from that date. "
    "The fair value of the net assets acquired was two hundred and five million pounds, so goodwill "
    "of one hundred and five million was recognised."),
   ('Speaker', 's', 'm3',
    "Two lessons. The promised synergies were forty million a year from combining the two depot "
    "networks; after two years the realised figure was twenty-three million. And integration cost "
    "eighteen million, which nobody had put in the original model. When you read a takeover story, "
    "always ask what the synergies actually turned out to be. Thank you."),
  ],
  'questions': [
   {'q': 'What was Northvale’s opening offer?',
    'o': ['Two hundred and forty million pounds', 'Two hundred and seventy million pounds',
          'Three hundred and ten million pounds', 'Two hundred and five million pounds'], 'a': 0,
    'e': '"The opening offer was two hundred and forty million pounds"'},
   {'q': 'Why did the board reject the first offer?',
    'o': ['It undervalued the depot network', 'The buyer was a competitor',
          'The shareholders had not been consulted', 'The price was in the wrong currency'], 'a': 0,
    'e': '"saying it undervalued the depot network"'},
   {'q': 'What turned the approach into a hostile takeover?',
    'o': ['Northvale went directly to the shareholders', 'The price was raised twice',
          'Due diligence was refused', 'A second bidder appeared'], 'a': 0,
    'e': '"Northvale then went directly to the shareholders"'},
   {'q': 'What was the final price as a multiple of earnings?',
    'o': ['Eleven times', 'Nine times', 'Eighteen times', 'Twenty-eight times'], 'a': 0,
    'e': '"That final price was eleven times earnings"'},
   {'q': 'How long did due diligence take?',
    'o': ['Seven weeks', 'Nine days', 'Eighteen months', 'Two years'], 'a': 0,
    'e': '"due diligence, which took seven weeks"'},
   {'q': 'What was the first due diligence finding?',
    'o': ['Unrecorded repair obligations on leased vehicles',
          'An overstated inventory balance', 'A missing insurance policy',
          'An unpaid tax assessment'], 'a': 0,
    'e': '"repair obligations on forty leased vehicles had never been recorded"'},
   {'q': 'How did the parties deal with the findings?',
    'o': ['Thirty million was held back for eighteen months', 'The price was cut by six million',
          'The deal was abandoned', 'The customer contract was renegotiated'], 'a': 0,
    'e': '"instead thirty million was held back for eighteen months"'},
   {'q': 'How much goodwill was recognised?',
    'o': ['One hundred and five million pounds', 'Two hundred and five million pounds',
          'Thirty million pounds', 'Forty million pounds'], 'a': 0,
    'e': '310 ลบ 205 เท่ากับ 105 ล้านปอนด์'},
   {'q': 'What were the realised synergies after two years?',
    'o': ['Twenty-three million a year', 'Forty million a year',
          'Eighteen million a year', 'Six million a year'], 'a': 0,
    'e': '"after two years the realised figure was twenty-three million"'},
   {'q': 'What cost was missing from the original model?',
    'o': ['Integration cost of eighteen million', 'Due diligence fees',
          'The holdback of thirty million', 'Goodwill impairment'], 'a': 0,
    'e': '"integration cost eighteen million, which nobody had put in the original model"'},
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
    "handle the market and the positioning, and Kenji will take the marketing mix and the "
    "financials."),
   ('Nadia', 'n', 'f2',
    "Japan is the third largest coffee market in the world by value. It is mature, growing at only "
    "two percent a year, so this is a market penetration problem, not a market creation problem. We "
    "have to take share from someone."),
   ('Nadia', 'n', 'f2',
    "Market segmentation gives us three groups. Convenience store buyers, at fifty-four percent, "
    "are extremely price sensitive. Speciality cafe customers, at nineteen percent, care about "
    "origin. Office subscription buyers are only eight percent today but growing at fourteen percent "
    "a year. That last group is our target market."),
   ('Kenji', 'k', 'm1',
    "Thanks, Nadia. On the marketing mix, place matters more than promotion here. We will not fight "
    "for shelf space in convenience stores. We will sell direct to offices on a monthly "
    "subscription, which also means we get paid before we deliver."),
   ('Kenji', 'k', 'm1',
    "The unit economics. A subscription box sells at four thousand two hundred yen. Direct cost is "
    "two thousand four hundred, so the contribution is one thousand eight hundred yen per box, or "
    "about forty-three percent."),
   ('Kenji', 'k', 'm1',
    "Fixed costs are ninety million yen a year, mostly the roasting contract and the customer team. "
    "So we need fifty thousand boxes a year to break even, which is about four thousand two hundred "
    "subscriptions a month. Our forecast for year one is thirty-one thousand boxes, so year one is a "
    "planned loss."),
   ('Kenji', 'k', 'm1',
    "Two risks worth naming. Customer retention is everything in a subscription model: if monthly "
    "churn goes above four percent, the break-even point moves out by roughly a year. And the yen "
    "rate affects our green bean cost, which is eighty percent dollar denominated. Thank you."),
  ],
  'questions': [
   {'q': 'How fast is the Japanese coffee market growing?',
    'o': ['Two percent a year', 'Fourteen percent a year',
          'Nineteen percent a year', 'Fifty-four percent a year'], 'a': 0,
    'e': '"growing at only two percent a year"'},
   {'q': 'What kind of problem does Nadia say this is?',
    'o': ['Market penetration', 'Market creation', 'Market adaptation', 'Market segmentation'], 'a': 0,
    'e': '"this is a market penetration problem, not a market creation problem"'},
   {'q': 'Which segment is the target market?',
    'o': ['Office subscription buyers', 'Convenience store buyers',
          'Speciality cafe customers', 'Hotel and restaurant buyers'], 'a': 0,
    'e': '"That last group is our target market" · หมายถึงกลุ่มออฟฟิศ'},
   {'q': 'How fast is the target segment growing?',
    'o': ['Fourteen percent a year', 'Eight percent a year',
          'Two percent a year', 'Four percent a year'], 'a': 0,
    'e': '"only eight percent today but growing at fourteen percent a year"'},
   {'q': 'Why does selling direct to offices help cash flow?',
    'o': ['They get paid before they deliver', 'Offices pay a higher price',
          'There is no delivery cost', 'It avoids import duty'], 'a': 0,
    'e': '"which also means we get paid before we deliver"'},
   {'q': 'What is the contribution per box?',
    'o': ['One thousand eight hundred yen', 'Two thousand four hundred yen',
          'Four thousand two hundred yen', 'Ninety million yen'], 'a': 0,
    'e': '4,200 ลบ 2,400 เท่ากับ 1,800 เยน'},
   {'q': 'How many boxes a year are needed to break even?',
    'o': ['Fifty thousand', 'Thirty-one thousand',
          'Four thousand two hundred', 'Ninety thousand'], 'a': 0,
    'e': '"we need fifty thousand boxes a year to break even"'},
   {'q': 'What does the year one forecast imply?',
    'o': ['A planned loss', 'A small profit', 'Exactly break-even', 'A cash surplus'], 'a': 0,
    'e': '"forecast for year one is thirty-one thousand boxes, so year one is a planned loss"'},
   {'q': 'What happens if monthly churn passes four percent?',
    'o': ['Break-even moves out by about a year', 'Fixed costs fall',
          'The contribution rises', 'The forecast is unaffected'], 'a': 0,
    'e': '"the break-even point moves out by roughly a year"'},
   {'q': 'Why does the exchange rate matter?',
    'o': ['Green bean cost is mostly dollar denominated', 'Subscriptions are billed in dollars',
          'The roasting contract is in euros', 'Import duty is charged in dollars'], 'a': 0,
    'e': '"our green bean cost, which is eighty percent dollar denominated"'},
  ]},

 {'id': 'L2b', 'kind': 'talk',
  'title': 'A Merger of Two Software Firms',
  'context': u'วิทยากรเล่ากรณีควบรวมบริษัทซอฟต์แวร์บัญชีสองราย เน้นการประมาณการ synergies ที่พลาด',
  'turns': [
   ('Speaker', 's', 'm2',
    "Today's case is a merger between two accounting software companies. I picked it because the "
    "strategy was sound and the deal still disappointed, and the reason is entirely in the numbers."),
   ('Speaker', 's', 'm2',
    "Ledgerworks sold software to small firms. Ravenpoint sold to mid-sized groups. Neither competed "
    "with the other, and both boards recommended the deal, so this was a friendly takeover rather "
    "than a hostile one."),
   ('Speaker', 's', 'm2',
    "The structure matters. Ledgerworks shareholders received zero point six Ravenpoint shares for "
    "each share they held. At announcement that valued Ledgerworks at four hundred and eighty "
    "million euros, which was fourteen times earnings. The market reaction was mild: Ravenpoint "
    "shares fell two percent on the day."),
   ('Speaker', 's', 'm2',
    "The case was built on synergies. Management guided the market to fifty-five million euros a "
    "year: thirty million from removing duplicated engineering, fifteen million from the shared "
    "sales force, and ten million from closing one of the two data centres."),
   ('Speaker', 's', 'm2',
    "Due diligence took five weeks, and one finding was disclosed. Ledgerworks recognised licence "
    "revenue over twelve months while Ravenpoint used twenty-four. Aligning the two policies reduced "
    "reported combined revenue by nine million euros in the first year."),
   ('Speaker', 's', 'm2',
    "By year three, the realised synergies were thirty-two million, not fifty-five. The engineering "
    "saving arrived almost in full. The sales saving did not, because the two customer groups needed "
    "different sales skills. And the data centre closure was delayed by two years over a contract "
    "break clause, costing seven million more than planned."),
   ('Speaker', 's', 'm2',
    "So the lesson. Cost synergies that come from removing duplicated work are usually real. "
    "Synergies that depend on customers behaving differently, or on getting out of a contract early, "
    "are the ones that slip. When you see a synergy number in a press release, ask which of the two "
    "kinds it is. Thank you."),
  ],
  'questions': [
   {'q': 'What kind of takeover was this?',
    'o': ['Friendly, because both boards recommended it', 'Hostile, because one board refused',
          'A management buyout', 'A joint venture'], 'a': 0,
    'e': '"both boards recommended the deal, so this was a friendly takeover"'},
   {'q': 'What did Ledgerworks shareholders receive?',
    'o': ['Zero point six Ravenpoint shares per share', 'Cash of four hundred and eighty million',
          'One Ravenpoint share per share', 'Fourteen euros per share'], 'a': 0,
    'e': '"received zero point six Ravenpoint shares for each share they held"'},
   {'q': 'What multiple of earnings did the offer represent?',
    'o': ['Fourteen times', 'Twelve times', 'Twenty-four times', 'Two times'], 'a': 0,
    'e': '"which was fourteen times earnings"'},
   {'q': 'How did Ravenpoint shares react on the day?',
    'o': ['They fell two percent', 'They rose two percent',
          'They fell fourteen percent', 'They were unchanged'], 'a': 0,
    'e': '"Ravenpoint shares fell two percent on the day"'},
   {'q': 'What total annual synergies did management guide to?',
    'o': ['Fifty-five million euros', 'Thirty-two million euros',
          'Thirty million euros', 'Fifteen million euros'], 'a': 0,
    'e': '"Management guided the market to fifty-five million euros a year"'},
   {'q': 'Which saving was expected to be the largest?',
    'o': ['Removing duplicated engineering', 'The shared sales force',
          'Closing a data centre', 'Renegotiating the licence policy'], 'a': 0,
    'e': '"thirty million from removing duplicated engineering" · มากที่สุดในสามก้อน'},
   {'q': 'What did due diligence find?',
    'o': ['The two firms recognised licence revenue over different periods',
          'An unrecorded pension liability', 'A disputed patent',
          'An overstated receivable'], 'a': 0,
    'e': '"Ledgerworks recognised licence revenue over twelve months while Ravenpoint used twenty-four"'},
   {'q': 'What effect did aligning the policies have?',
    'o': ['Combined revenue fell by nine million in year one',
          'Combined revenue rose by nine million', 'Goodwill rose by nine million',
          'It had no effect on reported figures'], 'a': 0,
    'e': '"reduced reported combined revenue by nine million euros in the first year"'},
   {'q': 'What were the realised synergies by year three?',
    'o': ['Thirty-two million', 'Fifty-five million', 'Thirty million', 'Seven million'], 'a': 0,
    'e': '"the realised synergies were thirty-two million, not fifty-five"'},
   {'q': 'Which type of synergy does the speaker say is usually real?',
    'o': ['Savings from removing duplicated work',
          'Savings that depend on customer behaviour',
          'Savings from exiting a contract early', 'Savings from tax planning'], 'a': 0,
    'e': '"Cost synergies that come from removing duplicated work are usually real"'},
  ]},
]},

# ══════════════════════════════════ ชุดที่ 3 ══════════════════════════════════
{'id': 'L3', 'title': u'ชุดที่ 3', 'parts': [

 {'id': 'L3a', 'kind': 'presentation',
  'title': 'A Skincare Launch in Brazil',
  'context': u'ทีมสามคนเสนอแผนเปิดตัวสกินแคร์ในบราซิล เน้นงบโฆษณาและกำไรส่วนเกิน',
  'turns': [
   ('Elena', 'e', 'f3',
    "Good afternoon. I'm Elena, and with me are Tomas and Rafael. We are proposing a product launch "
    "for our Calmara skincare line in Brazil, and I'll begin with why this market and not another."),
   ('Elena', 'e', 'f3',
    "Brazil is the fourth largest beauty market in the world. Our market research covered sixteen "
    "hundred women in three cities. Two findings stood out. Brand awareness for imported skincare is "
    "high, at sixty-one percent. But brand loyalty is low: two thirds of buyers had changed brand in "
    "the past year."),
   ('Tomas', 't', 'm3',
    "Thanks, Elena. Low loyalty cuts both ways. It means we can win share quickly, but it also means "
    "we can lose it just as fast. So our whole plan is built on repeat purchase rather than on a "
    "single launch spike."),
   ('Tomas', 't', 'm3',
    "On market adaptation, one change is essential. The formula we sell in Europe is too heavy for "
    "the climate in the north of the country. Reformulating costs eight hundred thousand euros and "
    "adds four months, and we think it is not optional."),
   ('Rafael', 'r', 'm1',
    "Now the money. The advertising budget is three point two million euros over eighteen months. "
    "Seventy percent of it goes to online video, because television reaches the wrong age group for "
    "us."),
   ('Rafael', 'r', 'm1',
    "On unit economics, the retail price is one hundred and forty reais. After retailer margin and "
    "local tax, we receive seventy-three reais. Our cost is thirty-one, so the contribution is "
    "forty-two reais, a little under fifty-eight percent."),
   ('Rafael', 'r', 'm1',
    "To recover the reformulation and the advertising we need to sell ninety-six thousand units. Our "
    "base case is one hundred and twelve thousand in the first eighteen months, so there is a margin "
    "of safety of about seventeen percent. The main risk is the retailer: three chains control "
    "seventy percent of distribution, and all three review their listings every six months. Thank "
    "you."),
  ],
  'questions': [
   {'q': 'How many women did the market research cover?',
    'o': ['Sixteen hundred', 'Six hundred', 'Sixty-one hundred', 'Three thousand'], 'a': 0,
    'e': '"Our market research covered sixteen hundred women in three cities"'},
   {'q': 'What is brand awareness for imported skincare?',
    'o': ['Sixty-one percent', 'Seventy percent', 'Fifty-eight percent', 'Two thirds'], 'a': 0,
    'e': '"Brand awareness for imported skincare is high, at sixty-one percent"'},
   {'q': 'What does low brand loyalty mean for the plan?',
    'o': ['Share can be won quickly but lost just as fast',
          'Advertising is unnecessary', 'Prices can be raised freely',
          'Distribution is guaranteed'], 'a': 0,
    'e': '"we can win share quickly, but it also means we can lose it just as fast"'},
   {'q': 'Why is reformulation needed?',
    'o': ['The European formula is too heavy for the climate',
          'The packaging fails local rules', 'The ingredients are banned',
          'The price is too high'], 'a': 0,
    'e': '"too heavy for the climate in the north of the country"'},
   {'q': 'What does reformulation cost?',
    'o': ['Eight hundred thousand euros and four months',
          'Three point two million euros', 'Eight hundred thousand reais',
          'Four hundred thousand euros and eight months'], 'a': 0,
    'e': '"Reformulating costs eight hundred thousand euros and adds four months"'},
   {'q': 'Where does most of the advertising budget go?',
    'o': ['Online video', 'Television', 'In-store promotion', 'Print magazines'], 'a': 0,
    'e': '"Seventy percent of it goes to online video"'},
   {'q': 'How much does the company receive per unit after margin and tax?',
    'o': ['Seventy-three reais', 'One hundred and forty reais',
          'Forty-two reais', 'Thirty-one reais'], 'a': 0,
    'e': '"After retailer margin and local tax, we receive seventy-three reais"'},
   {'q': 'What is the contribution per unit?',
    'o': ['Forty-two reais', 'Thirty-one reais', 'Seventy-three reais', 'Fifty-eight reais'], 'a': 0,
    'e': '73 ลบ 31 เท่ากับ 42 เรอัล'},
   {'q': 'How many units must be sold to recover the costs?',
    'o': ['Ninety-six thousand', 'One hundred and twelve thousand',
          'Seventy thousand', 'Seventeen thousand'], 'a': 0,
    'e': '"we need to sell ninety-six thousand units"'},
   {'q': 'What is the main risk Rafael names?',
    'o': ['Three chains control seventy percent of distribution',
          'The exchange rate', 'The cost of online video',
          'A competitor launching first'], 'a': 0,
    'e': '"three chains control seventy percent of distribution"'},
  ]},

 {'id': 'L3b', 'kind': 'talk',
  'title': 'A Bid That Failed',
  'context': u'วิทยากรเล่ากรณีข้อเสนอซื้อกิจการที่ล้มเหลว เน้นเกณฑ์การตอบรับของผู้ถือหุ้น',
  'turns': [
   ('Speaker', 's', 'm2',
    "Most of the cases you read about are deals that completed. Today I want to do the opposite, and "
    "look at a bid that failed, because failed bids teach you where the real obstacles are."),
   ('Speaker', 's', 'm2',
    "The target was Kestrel Instruments, a listed maker of measuring equipment. The predator was a "
    "private equity fund called Braemar Capital. In April, Braemar took a stake of nine point eight "
    "percent, deliberately just under the ten percent disclosure threshold in that market."),
   ('Speaker', 's', 'm2',
    "In June it made a takeover bid of six pounds twenty a share, valuing Kestrel at eight hundred "
    "and sixty million pounds. That was a premium of thirty-one percent over the price before the "
    "stake was announced."),
   ('Speaker', 's', 'm2',
    "The board rejected the bid, and its argument was specific. Kestrel had spent four years and one "
    "hundred and ten million pounds developing a new sensor platform, and the board said the offer "
    "gave no value at all for work that was not yet in the revenue line."),
   ('Speaker', 's', 'm2',
    "Braemar raised the offer once, to six pounds seventy-five, and set an acceptance condition of "
    "seventy-five percent of shares. Two large institutional shareholders, holding thirty-one "
    "percent between them, publicly refused. At that point the condition could not be met."),
   ('Speaker', 's', 'm2',
    "The bid lapsed in September. Braemar sold its stake over the following four months at a small "
    "profit, and the Kestrel share price settled about nine percent above where it had started the "
    "year."),
   ('Speaker', 's', 'm2',
    "Three things to take away. First, an acceptance condition is a real constraint, not a formality. "
    "Second, valuing development work that has no revenue yet is where target boards and bidders "
    "disagree most often. Third, notice that the shareholders, not the board, decided the outcome. "
    "The board can recommend or reject, but it cannot accept on anyone's behalf. Thank you."),
  ],
  'questions': [
   {'q': 'What stake did Braemar take in April?',
    'o': ['Nine point eight percent', 'Ten percent',
          'Thirty-one percent', 'Seventy-five percent'], 'a': 0,
    'e': '"Braemar took a stake of nine point eight percent"'},
   {'q': 'Why did it stop just below ten percent?',
    'o': ['To stay under the disclosure threshold', 'To reduce stamp duty',
          'Because it ran out of cash', 'Because the board refused to sell more'], 'a': 0,
    'e': '"deliberately just under the ten percent disclosure threshold"'},
   {'q': 'What was the opening offer per share?',
    'o': ['Six pounds twenty', 'Six pounds seventy-five',
          'Eight pounds sixty', 'One hundred and ten pounds'], 'a': 0,
    'e': '"a takeover bid of six pounds twenty a share"'},
   {'q': 'What premium did the opening offer represent?',
    'o': ['Thirty-one percent', 'Nine percent', 'Seventy-five percent', 'Ten percent'], 'a': 0,
    'e': '"a premium of thirty-one percent over the price before the stake was announced"'},
   {'q': 'What was the board’s specific objection?',
    'o': ['The offer gave no value for the new sensor platform',
          'The bidder was foreign', 'The offer was in shares rather than cash',
          'The timing was wrong'], 'a': 0,
    'e': '"the offer gave no value at all for work that was not yet in the revenue line"'},
   {'q': 'How much had Kestrel spent on the sensor platform?',
    'o': ['One hundred and ten million pounds over four years',
          'Eight hundred and sixty million pounds', 'Thirty-one million pounds',
          'Nine million pounds a year'], 'a': 0,
    'e': '"four years and one hundred and ten million pounds"'},
   {'q': 'What acceptance condition did Braemar set?',
    'o': ['Seventy-five percent of shares', 'Fifty percent of shares',
          'Thirty-one percent of shares', 'Ninety percent of shares'], 'a': 0,
    'e': '"set an acceptance condition of seventy-five percent of shares"'},
   {'q': 'Why could the condition not be met?',
    'o': ['Two shareholders holding thirty-one percent refused',
          'The regulator blocked the deal', 'Braemar withdrew the offer',
          'The board bought back shares'], 'a': 0,
    'e': '"Two large institutional shareholders, holding thirty-one percent between them, publicly refused"'},
   {'q': 'What happened to Braemar’s stake afterwards?',
    'o': ['It was sold over four months at a small profit',
          'It was kept in full', 'It was sold at a loss',
          'It was transferred to the board'], 'a': 0,
    'e': '"Braemar sold its stake over the following four months at a small profit"'},
   {'q': 'Who decided the outcome, according to the speaker?',
    'o': ['The shareholders', 'The board of directors',
          'The regulator', 'The bidder’s own investors'], 'a': 0,
    'e': '"notice that the shareholders, not the board, decided the outcome"'},
  ]},
]},

# ══════════════════════════════════ ชุดที่ 4 ══════════════════════════════════
{'id': 'L4', 'title': u'ชุดที่ 4', 'parts': [

 {'id': 'L4a', 'kind': 'presentation',
  'title': 'Repositioning a Budget Airline',
  'context': u'สองคนเสนอแผนปรับตำแหน่งสายการบินต้นทุนต่ำ เน้นต้นทุนต่อที่นั่งและอัตราบรรทุก',
  'turns': [
   ('Priya', 'p', 'f1',
    "Good morning. I'm Priya, and Marcus will join me. Our subject is brand positioning: whether "
    "Skylark, which has been a pure budget airline for eleven years, should move up the market."),
   ('Priya', 'p', 'f1',
    "The problem is visible in one number. Our load factor is eighty-nine percent, which is very "
    "high, but our average fare has fallen for three years running. We are filling the aircraft by "
    "cutting the price, and that is not a strategy, it is a habit."),
   ('Priya', 'p', 'f1',
    "Our market research found something useful. Forty-four percent of our passengers are now "
    "travelling on business, up from twenty-six percent five years ago. They choose us on schedule, "
    "not on price, and they are the least price sensitive segment we have."),
   ('Marcus', 'm', 'm2',
    "Thanks, Priya. So the proposal is a partial repositioning. We keep the low cost base, but we "
    "add a business fare with a guaranteed middle seat free, priority boarding, and a changeable "
    "ticket."),
   ('Marcus', 'm', 'm2',
    "The economics are straightforward. Our cost per available seat kilometre is four point one "
    "cents, one of the lowest in the region. Selling the middle seat empty raises the cost per "
    "occupied seat by about fifty percent on those rows, but the business fare is priced at two "
    "point three times the standard fare."),
   ('Marcus', 'm', 'm2',
    "We modelled it on twelve routes. If just eleven percent of seats sell at the business fare, "
    "revenue per flight rises by nine percent. Below eight percent take-up, we are worse off than "
    "today."),
   ('Marcus', 'm', 'm2',
    "The real risk is brand image, not cost. Eleven years of advertising has told the market that we "
    "are the cheapest, and a confused brand loses both ends of the market. So we recommend launching "
    "under a separate fare name on four routes for six months before deciding. Thank you."),
  ],
  'questions': [
   {'q': 'What is Skylark’s load factor?',
    'o': ['Eighty-nine percent', 'Forty-four percent',
          'Twenty-six percent', 'Eleven percent'], 'a': 0,
    'e': '"Our load factor is eighty-nine percent"'},
   {'q': 'What has happened to the average fare?',
    'o': ['It has fallen for three years running', 'It has risen for three years',
          'It has been flat for eleven years', 'It rose then fell'], 'a': 0,
    'e': '"our average fare has fallen for three years running"'},
   {'q': 'What proportion of passengers now travel on business?',
    'o': ['Forty-four percent', 'Twenty-six percent',
          'Eleven percent', 'Eighty-nine percent'], 'a': 0,
    'e': '"Forty-four percent of our passengers are now travelling on business"'},
   {'q': 'What do business passengers choose the airline on?',
    'o': ['Schedule', 'Price', 'Loyalty points', 'Seat width'], 'a': 0,
    'e': '"They choose us on schedule, not on price"'},
   {'q': 'What does the business fare include?',
    'o': ['A free middle seat, priority boarding and a changeable ticket',
          'Lounge access and extra baggage', 'A meal and a refundable ticket',
          'A seat at the front and free wifi'], 'a': 0,
    'e': '"a guaranteed middle seat free, priority boarding, and a changeable ticket"'},
   {'q': 'What is the cost per available seat kilometre?',
    'o': ['Four point one cents', 'Two point three cents',
          'Eleven cents', 'Nine cents'], 'a': 0,
    'e': '"Our cost per available seat kilometre is four point one cents"'},
   {'q': 'How is the business fare priced?',
    'o': ['At two point three times the standard fare', 'At fifty percent above standard',
          'At nine percent above standard', 'At double the standard fare'], 'a': 0,
    'e': '"the business fare is priced at two point three times the standard fare"'},
   {'q': 'At what take-up does revenue per flight rise by nine percent?',
    'o': ['Eleven percent of seats', 'Eight percent of seats',
          'Twelve percent of seats', 'Forty-four percent of seats'], 'a': 0,
    'e': '"If just eleven percent of seats sell at the business fare, revenue per flight rises by nine percent"'},
   {'q': 'Below what take-up is the airline worse off?',
    'o': ['Eight percent', 'Eleven percent', 'Nine percent', 'Four percent'], 'a': 0,
    'e': '"Below eight percent take-up, we are worse off than today"'},
   {'q': 'What does Marcus say is the real risk?',
    'o': ['Brand image', 'Cost per seat', 'Crew scheduling', 'Fuel price'], 'a': 0,
    'e': '"The real risk is brand image, not cost"'},
  ]},

 {'id': 'L4b', 'kind': 'talk',
  'title': 'A Management Buyout',
  'context': u'วิทยากรเล่ากรณีผู้บริหารซื้อกิจการโรงพิมพ์ เน้นโครงสร้างเงินกู้และเงื่อนไขของธนาคาร',
  'turns': [
   ('Speaker', 's', 'm1',
    "This case is a management buyout, and I want you to pay attention to the funding structure, "
    "because in a buyout the structure is the story."),
   ('Speaker', 's', 'm1',
    "Thornbury Print was a commercial printing group owned by a larger media company. The parent "
    "decided to divest it, because printing was no longer core. Rather than sell to a competitor, it "
    "agreed a sale to five of Thornbury's own senior managers."),
   ('Speaker', 's', 'm1',
    "The price was seventy-two million pounds. The managers themselves could put in only three "
    "million, which is a little over four percent. The rest came from two places: forty-four million "
    "of bank debt, and twenty-five million of equity from a private equity fund, which took "
    "sixty-eight percent of the shares."),
   ('Speaker', 's', 'm1',
    "So look at what that structure does. The managers end up with about twenty-eight percent of a "
    "company they used to run for a salary. But the business now carries forty-four million of debt "
    "that was not there before, and the interest is nearly four times the old figure."),
   ('Speaker', 's', 'm1',
    "The bank set two covenants. Net debt had to stay below three point five times earnings before "
    "interest, tax, depreciation and amortisation, and interest cover had to stay above three times. "
    "Both were tested every quarter."),
   ('Speaker', 's', 'm1',
    "In year two, a large customer moved to digital and volume fell eleven percent. Earnings fell "
    "with it, and the net debt ratio reached three point four. That is still inside the covenant, "
    "but one bad quarter away from breaching it, and the managers spent that year running the "
    "balance sheet rather than the business."),
   ('Speaker', 's', 'm1',
    "They recovered by selling two sites for nine million and paying down debt. The fund exited in "
    "year six at a valuation of one hundred and thirty million. So the deal worked. But the point I "
    "want you to keep is this: in a buyout, the operating risk is unchanged, and all the added risk "
    "comes from the funding. Thank you."),
  ],
  'questions': [
   {'q': 'Why did the parent company sell Thornbury Print?',
    'o': ['Printing was no longer core', 'It was making a loss',
          'A regulator required it', 'The managers threatened to leave'], 'a': 0,
    'e': '"because printing was no longer core"'},
   {'q': 'What was the total price?',
    'o': ['Seventy-two million pounds', 'Forty-four million pounds',
          'Twenty-five million pounds', 'One hundred and thirty million pounds'], 'a': 0,
    'e': '"The price was seventy-two million pounds"'},
   {'q': 'How much did the managers themselves put in?',
    'o': ['Three million pounds', 'Twenty-five million pounds',
          'Forty-four million pounds', 'Nine million pounds'], 'a': 0,
    'e': '"The managers themselves could put in only three million"'},
   {'q': 'How much bank debt was used?',
    'o': ['Forty-four million', 'Twenty-five million',
          'Seventy-two million', 'Three million'], 'a': 0,
    'e': '"forty-four million of bank debt"'},
   {'q': 'What percentage of shares did the private equity fund take?',
    'o': ['Sixty-eight percent', 'Twenty-eight percent',
          'Four percent', 'Eleven percent'], 'a': 0,
    'e': '"which took sixty-eight percent of the shares"'},
   {'q': 'What share did the managers end up with?',
    'o': ['About twenty-eight percent', 'About four percent',
          'About sixty-eight percent', 'A half'], 'a': 0,
    'e': '"The managers end up with about twenty-eight percent"'},
   {'q': 'What were the two bank covenants?',
    'o': ['Net debt below three point five times earnings, and interest cover above three times',
          'Net debt below three times, and interest cover above three point five times',
          'Net debt below eleven percent, and interest cover above four times',
          'A minimum cash balance and a dividend ban'], 'a': 0,
    'e': '"Net debt had to stay below three point five times … interest cover … above three times"'},
   {'q': 'What happened in year two?',
    'o': ['A large customer moved to digital and volume fell eleven percent',
          'The bank withdrew the facility', 'A covenant was breached',
          'The fund sold its stake'], 'a': 0,
    'e': '"a large customer moved to digital and volume fell eleven percent"'},
   {'q': 'How did the company recover?',
    'o': ['It sold two sites for nine million and paid down debt',
          'It raised new equity', 'It renegotiated the covenants',
          'It cut the workforce by a third'], 'a': 0,
    'e': '"selling two sites for nine million and paying down debt"'},
   {'q': 'What is the speaker’s main point about buyouts?',
    'o': ['The operating risk is unchanged; the added risk comes from the funding',
          'Managers always overpay', 'Bank covenants are rarely enforced',
          'Private equity funds exit too early'], 'a': 0,
    'e': '"the operating risk is unchanged, and all the added risk comes from the funding"'},
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
    "take the findings; I will start with what we did and what the study cannot tell you."),
   ('Sasha', 's', 'f2',
    "We surveyed two thousand four hundred households across five provinces, and we ran eight focus "
    "groups. The budget was one hundred and ninety thousand dollars and the fieldwork took eleven "
    "weeks. One limitation matters: the sample is urban only, so nothing here applies to rural "
    "demand."),
   ('Arun', 'a', 'm3',
    "Thanks, Sasha. The headline is that the category is growing at seven percent a year, but the "
    "growth is concentrated. Two provinces account for sixty-two percent of it. If you plan national "
    "distribution from day one, you will be paying to reach demand that is not there yet."),
   ('Arun', 'a', 'm3',
    "On price, the finding was clearer than we expected. Willingness to pay drops sharply above "
    "thirty-five thousand rupiah per unit. Below that line, price barely affects choice. Above it, a "
    "ten percent price rise cuts stated purchase intention by almost a third."),
   ('Laila', 'l', 'f3',
    "I will take brand and channel. Brand awareness for the category leader is seventy-eight percent, "
    "but when we asked which brand people had actually bought last, the leader got only forty-one "
    "percent. That gap between awareness and purchase is the opening."),
   ('Laila', 'l', 'f3',
    "On channel, seventy percent of purchases happen in small independent shops rather than modern "
    "retail. That changes everything about distribution cost, because you cannot serve those shops "
    "directly. You need a distributor, and the distributor margin in this market is eighteen percent."),
   ('Laila', 'l', 'f3',
    "Two things we could not answer. We did not test packaging, because the samples were not ready "
    "in time. And we have no data on repeat purchase, since the study was a single wave. If the "
    "board wants a repeat purchase figure, that is a second study of about four months. Thank you."),
  ],
  'questions': [
   {'q': 'How many households were surveyed?',
    'o': ['Two thousand four hundred', 'Two thousand', 'Four hundred', 'Eight hundred'], 'a': 0,
    'e': '"We surveyed two thousand four hundred households across five provinces"'},
   {'q': 'What was the research budget?',
    'o': ['One hundred and ninety thousand dollars', 'One hundred and nineteen thousand dollars',
          'Nineteen thousand dollars', 'Nine hundred thousand dollars'], 'a': 0,
    'e': '"The budget was one hundred and ninety thousand dollars"'},
   {'q': 'What limitation does Sasha flag?',
    'o': ['The sample is urban only', 'The sample is too small',
          'The fieldwork was rushed', 'Only one province was covered'], 'a': 0,
    'e': '"the sample is urban only, so nothing here applies to rural demand"'},
   {'q': 'How is category growth distributed?',
    'o': ['Two provinces account for sixty-two percent of it',
          'It is spread evenly across five provinces',
          'It is concentrated in rural areas', 'It is falling outside the cities'], 'a': 0,
    'e': '"Two provinces account for sixty-two percent of it"'},
   {'q': 'What does Arun warn about national distribution?',
    'o': ['You pay to reach demand that is not there yet',
          'It is cheaper than regional distribution',
          'It is blocked by regulation', 'It requires a joint venture'], 'a': 0,
    'e': '"you will be paying to reach demand that is not there yet"'},
   {'q': 'Above what price does willingness to pay drop sharply?',
    'o': ['Thirty-five thousand rupiah', 'Thirteen thousand rupiah',
          'Seventy thousand rupiah', 'Eighteen thousand rupiah'], 'a': 0,
    'e': '"Willingness to pay drops sharply above thirty-five thousand rupiah per unit"'},
   {'q': 'What is brand awareness for the category leader?',
    'o': ['Seventy-eight percent', 'Forty-one percent',
          'Seventy percent', 'Sixty-two percent'], 'a': 0,
    'e': '"Brand awareness for the category leader is seventy-eight percent"'},
   {'q': 'What does Laila call the opening for a new entrant?',
    'o': ['The gap between awareness and actual purchase',
          'The low price of the leader', 'The weak distribution network',
          'The lack of advertising'], 'a': 0,
    'e': '"That gap between awareness and purchase is the opening"'},
   {'q': 'What is the distributor margin in this market?',
    'o': ['Eighteen percent', 'Seventy percent', 'Forty-one percent', 'Seven percent'], 'a': 0,
    'e': '"the distributor margin in this market is eighteen percent"'},
   {'q': 'Which question could the study not answer?',
    'o': ['Repeat purchase', 'Price sensitivity', 'Brand awareness', 'Channel share'], 'a': 0,
    'e': '"we have no data on repeat purchase, since the study was a single wave"'},
  ]},

 {'id': 'L5b', 'kind': 'talk',
  'title': 'A Joint Venture in Batteries',
  'context': u'วิทยากรเล่ากรณีกิจการร่วมค้าผลิตแบตเตอรี่ เน้นความต่างจากการซื้อกิจการและวิธีบันทึกบัญชี',
  'turns': [
   ('Speaker', 's', 'f2',
    "The last case is a joint venture, and I have kept it until the end because students routinely "
    "confuse it with a takeover. They are not the same thing at all, and the accounting is different "
    "too."),
   ('Speaker', 's', 'f2',
    "Two companies were involved. Caldera Motors, a vehicle manufacturer, and Sentinel Chemical, a "
    "materials producer. Neither acquired the other. They each put capital into a new company, "
    "Voltrek, which builds battery cells."),
   ('Speaker', 's', 'f2',
    "Each side contributed four hundred and twenty million dollars and took exactly fifty percent. "
    "Caldera also contributed a site, valued at sixty million, which counted towards its share. So "
    "its cash contribution was three hundred and sixty million."),
   ('Speaker', 's', 'f2',
    "Now the point that matters for your accounting. Because neither party controls Voltrek, neither "
    "one consolidates it. Each reports its interest using the equity method: one line in the balance "
    "sheet, one line in the income statement. If this had been an acquisition, the whole of Voltrek's "
    "assets and liabilities would appear."),
   ('Speaker', 's', 'f2',
    "Why a joint venture rather than a takeover? Three reasons. The plant costs more than either side "
    "wanted on its own balance sheet. Each brings something the other lacks, Caldera the demand and "
    "Sentinel the chemistry. And the technology may not win, so both wanted to limit the loss."),
   ('Speaker', 's', 'f2',
    "The weakness is governance. With a fifty-fifty split, a genuine disagreement has no tiebreaker. "
    "Here the agreement named an independent chairman with a casting vote on operating matters only, "
    "not on capital spending, which still needs both parties."),
   ('Speaker', 's', 'f2',
    "In year three, the two sides did disagree, about whether to double capacity. Sentinel wanted to; "
    "Caldera did not. Because it was a capital decision, the casting vote did not apply, and the "
    "expansion was delayed by fourteen months. So when you read a joint venture agreement, look at "
    "the deadlock clause before you look at the profit forecast. Thank you."),
  ],
  'questions': [
   {'q': 'What did the two companies do?',
    'o': ['They each put capital into a new company',
          'One acquired the other', 'They merged into a single company',
          'They exchanged shares'], 'a': 0,
    'e': '"They each put capital into a new company, Voltrek"'},
   {'q': 'How much did each side contribute?',
    'o': ['Four hundred and twenty million dollars', 'Three hundred and sixty million dollars',
          'Sixty million dollars', 'Two hundred and ten million dollars'], 'a': 0,
    'e': '"Each side contributed four hundred and twenty million dollars"'},
   {'q': 'What was Caldera’s cash contribution?',
    'o': ['Three hundred and sixty million', 'Four hundred and twenty million',
          'Sixty million', 'Four hundred and eighty million'], 'a': 0,
    'e': '420 ลบที่ดิน 60 เหลือเงินสด 360 ล้าน'},
   {'q': 'Why does neither party consolidate Voltrek?',
    'o': ['Because neither one controls it', 'Because it is loss-making',
          'Because it is in another country', 'Because it is newly formed'], 'a': 0,
    'e': '"Because neither party controls Voltrek, neither one consolidates it"'},
   {'q': 'How is the interest reported instead?',
    'o': ['Using the equity method', 'At cost less impairment',
          'At fair value through profit or loss', 'As a finance lease'], 'a': 0,
    'e': '"Each reports its interest using the equity method"'},
   {'q': 'What would change if this had been an acquisition?',
    'o': ['All of Voltrek’s assets and liabilities would appear',
          'Goodwill would be ignored', 'No entries would be needed',
          'Only the cash paid would be shown'], 'a': 0,
    'e': '"the whole of Voltrek’s assets and liabilities would appear"'},
   {'q': 'What does Caldera bring to the venture?',
    'o': ['The demand', 'The chemistry', 'The site only', 'The financing'], 'a': 0,
    'e': '"Caldera the demand and Sentinel the chemistry"'},
   {'q': 'What is the weakness of a fifty-fifty split?',
    'o': ['A genuine disagreement has no tiebreaker',
          'Neither side can sell its shares', 'Profits cannot be distributed',
          'The venture cannot borrow'], 'a': 0,
    'e': '"With a fifty-fifty split, a genuine disagreement has no tiebreaker"'},
   {'q': 'What does the independent chairman’s casting vote cover?',
    'o': ['Operating matters only', 'Capital spending only',
          'All decisions', 'Only the appointment of directors'], 'a': 0,
    'e': '"a casting vote on operating matters only, not on capital spending"'},
   {'q': 'What was the result of the year three disagreement?',
    'o': ['The expansion was delayed by fourteen months',
          'Sentinel sold its share', 'The venture was wound up',
          'Caldera took full control'], 'a': 0,
    'e': '"the expansion was delayed by fourteen months"'},
  ]},
]},

]
