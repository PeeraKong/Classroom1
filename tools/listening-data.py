# -*- coding: utf-8 -*-
"""บทฟังสำหรับ Part III · Listening ของวิชาภาษาอังกฤษ

แต่ละชุดมีสองส่วนตามแนวข้อสอบจริง
  presentation · การนำเสนอกลุ่มเรื่อง international marketing หลายคนพูดสลับกัน
  talk         · การบรรยายเรื่อง merger case คนเดียวพูดตลอด

ทุกบทตั้งใจใส่ศัพท์จาก Unit 2 และ Unit 12 ให้หนาแน่น เพราะข้อสอบวัดการฟังจับรายละเอียด
ที่ผูกกับศัพท์เหล่านั้นโดยตรง
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
  'context': u'ทีมการตลาดสามคนนำเสนอแผนพาแบรนด์อาหารว่างเข้าสู่ตลาดเวียดนาม',
  'turns': [
   ('Mai', 'm', 'f1',
    "Good morning everyone. I'm Mai, and today my team and I will present our plan for taking Crispbite "
    "into Vietnam. I'll start with the market research, then Daniel will cover segmentation and "
    "positioning, and finally Preecha will talk about the marketing mix and the risks."),
   ('Mai', 'm', 'f1',
    "We carried out market research in four cities over three months. We used two methods: a questionnaire "
    "completed by two thousand shoppers, and six focus groups. The headline finding is that the snack "
    "market in Vietnam is growing at about nine percent a year, which is far faster than our domestic "
    "market. But it is also increasingly competitive. The market leader already holds thirty-one percent "
    "market share, and two international brands entered last year."),
   ('Daniel', 'd', 'm1',
    "Thanks, Mai. So who exactly are we selling to? Our customer profile is clear: urban office workers "
    "between twenty-two and thirty-five, who buy snacks at convenience stores rather than supermarkets. "
    "That segment is small — about twelve percent of all snack buyers — but it spends nearly double the "
    "average."),
   ('Daniel', 'd', 'm1',
    "On brand positioning, we are not going to compete on price. The budget end of the market is already "
    "crowded and the margins are thin. Instead we will position Crispbite as a premium product, roughly "
    "twenty percent above the average shelf price, and build the brand around quality ingredients."),
   ('Preecha', 'p', 'm2',
    "Thank you, Daniel. Let me turn to the marketing mix. On product, we need some market adaptation. Our "
    "original flavour is too sweet for Vietnamese consumers, so the recipe will change. On place, we have "
    "signed with a national distributor who supplies eight thousand retail outlets."),
   ('Preecha', 'p', 'm2',
    "On promotion, the budget is one point two million dollars for the first year. Sixty percent goes to "
    "digital advertising, and the rest to in-store sampling, because free samples are still the most "
    "effective way to build brand awareness in this market."),
   ('Preecha', 'p', 'm2',
    "Finally, the main risk. Brand loyalty in Vietnamese snacks is low — shoppers switch easily. So "
    "customer retention, not just customer acquisition, has to be the priority from day one. Thank you. "
    "We are happy to take questions."),
  ],
  'questions': [
   {'q': 'How long did the market research take?',
    'o': ['Three months', 'Three weeks', 'Nine months', 'One year'], 'a': 0,
    'e': u'Mai บอกว่า "we carried out market research in four cities over three months"'},
   {'q': 'Which two research methods did the team use?',
    'o': ['A questionnaire and focus groups', 'Interviews and a survey',
          'A questionnaire and in-store sampling', 'Focus groups and A/B testing'], 'a': 0,
    'e': u'"a questionnaire completed by two thousand shoppers, and six focus groups"'},
   {'q': "What is the market leader's share?",
    'o': ['Thirty-one percent', 'Thirteen percent', 'Twelve percent', 'Twenty percent'], 'a': 0,
    'e': u'"The market leader already holds thirty-one percent market share" · ระวังสับสนกับ 12% ซึ่งเป็นขนาดของกลุ่มเป้าหมาย'},
   {'q': 'Where does the target segment usually buy snacks?',
    'o': ['At convenience stores', 'At supermarkets', 'Online', 'At wholesale markets'], 'a': 0,
    'e': u'"who buy snacks at convenience stores rather than supermarkets"'},
   {'q': 'Why will the company NOT compete on price?',
    'o': ['The budget end is crowded and margins are thin',
          'The product is too expensive to make',
          'Regulations prevent price competition',
          'The distributor refused a low price'], 'a': 0,
    'e': u'"The budget end of the market is already crowded and the margins are thin"'},
   {'q': 'How will Crispbite be positioned?',
    'o': ['As a premium product about twenty percent above average price',
          'As a budget product below average price',
          'At exactly the average shelf price',
          'As a mid-market product'], 'a': 0,
    'e': u'"position Crispbite as a premium product, roughly twenty percent above the average shelf price"'},
   {'q': 'What market adaptation is needed?',
    'o': ['The recipe is too sweet and must change',
          'The packaging size must be smaller',
          'The brand name must be translated',
          'The product must be made locally'], 'a': 0,
    'e': u'"Our original flavour is too sweet for Vietnamese consumers, so the recipe will change"'},
   {'q': 'How many retail outlets does the distributor supply?',
    'o': ['Eight thousand', 'Eighteen thousand', 'Eight hundred', 'Two thousand'], 'a': 0,
    'e': u'"a national distributor who supplies eight thousand retail outlets" · 2,000 คือจำนวนคนที่ตอบแบบสอบถาม'},
   {'q': 'What share of the promotion budget goes to digital advertising?',
    'o': ['Sixty percent', 'Forty percent', 'Twenty percent', 'One point two percent'], 'a': 0,
    'e': u'"Sixty percent goes to digital advertising, and the rest to in-store sampling"'},
   {'q': 'What does Preecha say is the main risk?',
    'o': ['Low brand loyalty, so customer retention must be a priority',
          'The distributor may not deliver on time',
          'The promotion budget is too small',
          'Competitors will copy the recipe'], 'a': 0,
    'e': u'"Brand loyalty in Vietnamese snacks is low — shoppers switch easily. So customer retention … has to be the priority"'},
  ]},

 {'id': 'L1b', 'kind': 'talk',
  'title': 'The Kraft and Cadbury Takeover',
  'context': u'วิทยากรเล่ากรณีศึกษาการเข้าซื้อกิจการที่โด่งดังในปี 2009 ถึง 2010',
  'turns': [
   ('Speaker', 's', 'm1',
    "Right, let's look at one of the most talked-about takeovers of the last twenty years: Kraft and "
    "Cadbury. It's a useful case because almost every term from this unit appears in it."),
   ('Speaker', 's', 'm1',
    "In September two thousand and nine, Kraft, the American food group, made a bid for Cadbury, the "
    "British confectionery company. The first offer valued Cadbury at around ten point two billion "
    "pounds. Cadbury's board rejected the bid immediately, calling it, and I quote, derisory — meaning "
    "insultingly low."),
   ('Speaker', 's', 'm1',
    "Because the board said no, this became a hostile takeover. Kraft went directly to Cadbury's "
    "shareholders rather than working through the board. That is the defining feature of a hostile bid: "
    "you bypass the directors."),
   ('Speaker', 's', 'm1',
    "Over the following months Kraft raised its bid twice. The final offer, in January two thousand and "
    "ten, was worth about eleven point five billion pounds — a premium of roughly fifty percent over "
    "Cadbury's share price before the approach began. At that level, enough shareholders accepted, and "
    "the deal went through."),
   ('Speaker', 's', 'm1',
    "Now, why did Kraft want Cadbury at all? Two reasons were given publicly. First, synergy: Kraft "
    "claimed it could save at least six hundred and twenty-five million dollars a year by combining "
    "operations. Second, distribution — Cadbury was strong in India and Latin America, markets where "
    "Kraft was weak."),
   ('Speaker', 's', 'm1',
    "There was also controversy. During the bid Kraft said it would keep a Cadbury factory near Bristol "
    "open. One week after the takeover completed, it announced the factory would close. Four hundred "
    "jobs went. Kraft was criticised heavily, and the UK takeover rules were later tightened as a "
    "result."),
   ('Speaker', 's', 'm1',
    "So, three things to remember from this case. A bid can be raised more than once. A hostile takeover "
    "means going around the board, not through it. And promises made during a bid are not always kept."),
  ],
  'questions': [
   {'q': 'When did Kraft first make a bid for Cadbury?',
    'o': ['September 2009', 'January 2010', 'September 2010', 'January 2009'], 'a': 0,
    'e': u'"In September two thousand and nine, Kraft … made a bid for Cadbury"'},
   {'q': 'How much was the first offer worth?',
    'o': ['About 10.2 billion pounds', 'About 11.5 billion pounds',
          'About 625 million dollars', 'About 50 billion pounds'], 'a': 0,
    'e': u'"The first offer valued Cadbury at around ten point two billion pounds" · 11.5 คือข้อเสนอสุดท้าย'},
   {'q': "How did Cadbury's board describe the first offer?",
    'o': ['Derisory, meaning insultingly low', 'Generous but premature',
          'Acceptable in principle', 'Fair but badly timed'], 'a': 0,
    'e': u'"calling it, and I quote, derisory — meaning insultingly low"'},
   {'q': 'What made this a hostile takeover?',
    'o': ["Kraft went directly to shareholders instead of through the board",
          'Kraft refused to raise its offer',
          'The government opposed the deal',
          'Cadbury looked for a white knight'], 'a': 0,
    'e': u'"Kraft went directly to Cadbury’s shareholders rather than working through the board"'},
   {'q': 'How many times did Kraft raise its bid?',
    'o': ['Twice', 'Once', 'Three times', 'It never raised the bid'], 'a': 0,
    'e': u'"Over the following months Kraft raised its bid twice"'},
   {'q': 'What premium did the final offer represent?',
    'o': ['About fifty percent over the earlier share price',
          'About fifteen percent', 'About five percent', 'About twenty-five percent'], 'a': 0,
    'e': u'"a premium of roughly fifty percent over Cadbury’s share price before the approach began"'},
   {'q': 'How much did Kraft claim it could save each year?',
    'o': ['At least 625 million dollars', 'At least 625 million pounds',
          'At least 400 million dollars', 'At least 11.5 million dollars'], 'a': 0,
    'e': u'"it could save at least six hundred and twenty-five million dollars a year" · เป็นดอลลาร์ ไม่ใช่ปอนด์'},
   {'q': 'In which markets was Cadbury strong?',
    'o': ['India and Latin America', 'China and Japan',
          'Germany and France', 'Australia and New Zealand'], 'a': 0,
    'e': u'"Cadbury was strong in India and Latin America, markets where Kraft was weak"'},
   {'q': 'What happened to the factory near Bristol?',
    'o': ['It closed one week after the takeover completed',
          'It stayed open as promised',
          'It was sold to another company',
          'It was expanded'], 'a': 0,
    'e': u'"One week after the takeover completed, it announced the factory would close"'},
   {'q': 'What was one consequence of the controversy?',
    'o': ['The UK takeover rules were tightened',
          'Kraft was fined by the government',
          'The deal was cancelled',
          'Cadbury shareholders sued Kraft'], 'a': 0,
    'e': u'"the UK takeover rules were later tightened as a result"'},
  ]},
]},

# ══════════════════════════════════ ชุดที่ 2 ══════════════════════════════════
{'id': 'L2', 'title': u'ชุดที่ 2', 'parts': [

 {'id': 'L2a', 'kind': 'presentation',
  'title': 'Taking a Coffee Brand into Japan',
  'context': u'สองคนนำเสนอแผนพาแบรนด์กาแฟเข้าญี่ปุ่น เน้นการปรับสินค้าและช่องทางจำหน่าย',
  'turns': [
   ('Sarah', 's', 'f2',
    "Morning. I'm Sarah, and with me is Tom. We've been asked to look at whether Northbrew, our coffee "
    "brand, should enter Japan. Our answer is yes, but not in the way you might expect. I'll cover the "
    "market, and Tom will cover the product and the numbers."),
   ('Sarah', 's', 'f2',
    "Japan is not a growing market in volume terms — coffee consumption has been flat for six years. So "
    "why go? Because the premium segment is expanding at about seven percent a year while the mass market "
    "shrinks. That is a market niche, but a profitable one."),
   ('Sarah', 's', 'f2',
    "We did our market research differently this time. Instead of a questionnaire we ran ethnographic "
    "research — we watched two hundred people actually make and drink coffee at home. What we learned "
    "surprised us. The purchase decision is made on packaging design far more than on taste."),
   ('Tom', 't', 'm3',
    "Thanks Sarah. That finding drives our whole product strategy. We are not changing the coffee itself — "
    "no market adaptation on flavour. What changes is the pack. Smaller sizes, a matte finish, and Japanese "
    "text on the front rather than English."),
   ('Tom', 't', 'm3',
    "On place, we are deliberately avoiding supermarkets in year one. Our distributor will target department "
    "store food halls and specialist coffee outlets only. It is a slower route, but it protects our brand "
    "positioning at the premium end."),
   ('Tom', 't', 'm3',
    "On price, we will sit thirty percent above the category average. On promotion, we will spend almost "
    "nothing on advertising. The budget goes to in-store tasting and to one celebrity endorsement — a "
    "well-known chef who already uses our beans in his restaurants."),
   ('Tom', 't', 'm3',
    "Our target is four percent market share of the premium segment within three years. That sounds modest, "
    "but the premium segment is worth eight hundred million dollars, so four percent is thirty-two million. "
    "Thank you."),
  ],
  'questions': [
   {'q': 'What has happened to coffee consumption in Japan?',
    'o': ['It has been flat for six years', 'It has grown for six years',
          'It has fallen sharply', 'It has grown seven percent a year'], 'a': 0,
    'e': u'"coffee consumption has been flat for six years" · 7% คืออัตราโตของ premium segment'},
   {'q': 'Why is the team still recommending entry?',
    'o': ['The premium segment is expanding about seven percent a year',
          'The mass market is expanding',
          'Competition has disappeared',
          'Production costs are low in Japan'], 'a': 0,
    'e': u'"the premium segment is expanding at about seven percent a year while the mass market shrinks"'},
   {'q': 'What research method did they use?',
    'o': ['Ethnographic research, watching people at home',
          'A questionnaire', 'Focus groups', 'Telephone interviews'], 'a': 0,
    'e': u'"Instead of a questionnaire we ran ethnographic research — we watched two hundred people"'},
   {'q': 'What surprised the team?',
    'o': ['Packaging design matters more than taste',
          'Taste matters more than price',
          'Price matters more than packaging',
          'Brand name matters more than packaging'], 'a': 0,
    'e': u'"The purchase decision is made on packaging design far more than on taste"'},
   {'q': 'Will the coffee itself be changed?',
    'o': ['No, only the packaging changes', 'Yes, the flavour will be adapted',
          'Yes, the beans will be sourced locally', 'Only the caffeine level changes'], 'a': 0,
    'e': u'"We are not changing the coffee itself — no market adaptation on flavour. What changes is the pack"'},
   {'q': 'Which outlets will the distributor target in year one?',
    'o': ['Department store food halls and specialist coffee outlets',
          'Supermarkets and convenience stores',
          'Online retailers only',
          'Wholesale markets'], 'a': 0,
    'e': u'"we are deliberately avoiding supermarkets in year one … department store food halls and specialist coffee outlets only"'},
   {'q': 'How will Northbrew be priced?',
    'o': ['Thirty percent above the category average',
          'Thirty percent below the average',
          'At the category average',
          'Seven percent above the average'], 'a': 0,
    'e': u'"we will sit thirty percent above the category average"'},
   {'q': 'What will most of the promotion budget be spent on?',
    'o': ['In-store tasting and a celebrity endorsement',
          'Television advertising', 'Digital advertising', 'Price discounts'], 'a': 0,
    'e': u'"we will spend almost nothing on advertising. The budget goes to in-store tasting and to one celebrity endorsement"'},
   {'q': 'Who is the celebrity?',
    'o': ['A chef who already uses their beans', 'A famous actor',
          'A sports star', 'A television presenter'], 'a': 0,
    'e': u'"a well-known chef who already uses our beans in his restaurants"'},
   {'q': 'What is the three-year target in money terms?',
    'o': ['Thirty-two million dollars', 'Eight hundred million dollars',
          'Four million dollars', 'Three hundred million dollars'], 'a': 0,
    'e': u'4% ของ premium segment ที่มีมูลค่า 800 ล้าน = 32 ล้าน · ผู้พูดคำนวณให้ในประโยคสุดท้าย'},
  ]},

 {'id': 'L2b', 'kind': 'talk',
  'title': 'Disney and Pixar',
  'context': u'วิทยากรเล่ากรณีการเข้าซื้อที่มักถูกยกเป็นตัวอย่างของดีลที่สำเร็จ',
  'turns': [
   ('Speaker', 's', 'f1',
    "Today I want to give you a contrast to the case we looked at last week. Not every acquisition is "
    "hostile, and not every acquisition destroys value. Disney and Pixar is the example everyone reaches "
    "for."),
   ('Speaker', 's', 'f1',
    "Some background first. From nineteen ninety-one, Disney and Pixar were not owner and subsidiary. They "
    "were partners in a distribution agreement — Pixar made the films, Disney distributed them and took "
    "roughly half the profit. That agreement produced Toy Story, Finding Nemo and several others."),
   ('Speaker', 's', 'f1',
    "By two thousand and four the relationship had broken down. Negotiations to renew the agreement failed, "
    "and the two companies publicly fell out. It looked like the end."),
   ('Speaker', 's', 'f1',
    "Then in January two thousand and six, Disney acquired Pixar outright for seven point four billion "
    "dollars, paid entirely in Disney shares — no cash at all. That detail matters. Because Steve Jobs, "
    "who held about half of Pixar, became Disney's largest individual shareholder with roughly seven "
    "percent of the company."),
   ('Speaker', 's', 'f1',
    "This was a friendly takeover. Both boards agreed, and the deal was recommended to shareholders. There "
    "was no bidding war and no second bidder."),
   ('Speaker', 's', 'f1',
    "What makes the case interesting is what Disney did afterwards. Normally the buyer imposes its own "
    "systems on the target. Disney did the opposite. It left Pixar's culture, its offices and its "
    "management almost untouched, and then put Pixar's leadership in charge of Disney's own animation "
    "studio as well."),
   ('Speaker', 's', 'f1',
    "The result: Disney Animation, which had produced a run of disappointing films, released Tangled, "
    "Frozen and Zootopia over the following decade. So the synergy here was not cost-cutting. It was "
    "creative. Remember that — synergy does not always mean closing factories and reducing staff."),
  ],
  'questions': [
   {'q': 'What was the relationship before 2006?',
    'o': ['A distribution agreement, not ownership',
          'Pixar was a subsidiary of Disney',
          'A joint venture', 'They were competitors only'], 'a': 0,
    'e': u'"they were not owner and subsidiary. They were partners in a distribution agreement"'},
   {'q': 'Roughly how was profit split under that agreement?',
    'o': ['Disney took about half', 'Disney took about a quarter',
          'Pixar took about ninety percent', 'They split it seven to three'], 'a': 0,
    'e': u'"Disney distributed them and took roughly half the profit"'},
   {'q': 'What happened by 2004?',
    'o': ['Negotiations to renew the agreement failed',
          'Disney made a hostile bid',
          'Pixar was sold to another studio',
          'The agreement was extended'], 'a': 0,
    'e': u'"Negotiations to renew the agreement failed, and the two companies publicly fell out"'},
   {'q': 'How much did Disney pay for Pixar?',
    'o': ['7.4 billion dollars', '4.7 billion dollars',
          '7.4 million dollars', '74 billion dollars'], 'a': 0,
    'e': u'"Disney acquired Pixar outright for seven point four billion dollars"'},
   {'q': 'How was the acquisition paid for?',
    'o': ['Entirely in Disney shares', 'Entirely in cash',
          'Half shares, half cash', 'With borrowed money'], 'a': 0,
    'e': u'"paid entirely in Disney shares — no cash at all"'},
   {'q': 'What stake did Steve Jobs end up with in Disney?',
    'o': ['About seven percent', 'About fifty percent',
          'About seventeen percent', 'About one percent'], 'a': 0,
    'e': u'"became Disney’s largest individual shareholder with roughly seven percent" · 50% คือสัดส่วนที่เขาถือใน Pixar'},
   {'q': 'What kind of takeover was it?',
    'o': ['Friendly — both boards agreed', 'Hostile',
          'A management buyout', 'A reverse takeover'], 'a': 0,
    'e': u'"This was a friendly takeover. Both boards agreed"'},
   {'q': 'What did Disney do with Pixar after the deal?',
    'o': ["It left Pixar's culture and management almost untouched",
          "It imposed Disney's systems on Pixar",
          'It merged the two studios into one office',
          'It replaced Pixar management'], 'a': 0,
    'e': u'"It left Pixar’s culture, its offices and its management almost untouched"'},
   {'q': "Who was put in charge of Disney's own animation studio?",
    'o': ["Pixar's leadership", "Disney's existing team",
          'An outside consultant', 'Steve Jobs personally'], 'a': 0,
    'e': u'"put Pixar’s leadership in charge of Disney’s own animation studio as well"'},
   {'q': 'What is the speaker’s main point about synergy?',
    'o': ['It does not always mean cost-cutting; here it was creative',
          'It always means closing factories',
          'It rarely works in practice',
          'It only works in friendly deals'], 'a': 0,
    'e': u'"synergy does not always mean closing factories and reducing staff"'},
  ]},
]},

# ══════════════════════════════════ ชุดที่ 3 ══════════════════════════════════
{'id': 'L3', 'title': u'ชุดที่ 3', 'parts': [

 {'id': 'L3a', 'kind': 'presentation',
  'title': 'A Skincare Launch in Brazil',
  'context': u'สามคนนำเสนอแผนเปิดตัวสกินแคร์ในบราซิล เน้นการแบ่งส่วนตลาดและช่องทางออนไลน์',
  'turns': [
   ('Elena', 'e', 'f3',
    "Hello everyone. Elena here. Our group looked at whether Lumen, our skincare range, should launch in "
    "Brazil. Short answer: yes, but through a channel we have never used before. I'll do the market, "
    "Rafael will do segmentation, and Nok will finish with the numbers."),
   ('Elena', 'e', 'f3',
    "Brazil is the third-largest beauty market in the world. It is a growing market — about six percent a "
    "year — and unusually, it is not dominated by international brands. Domestic companies hold "
    "sixty-eight percent of the market between them. That is the first thing to understand: the market "
    "leader here is local, not global."),
   ('Rafael', 'r', 'm2',
    "Thanks. On market segmentation, we split buyers four ways, but only one segment matters for us. We "
    "call them the informed buyers: women aged twenty-five to forty, who research ingredients online "
    "before purchasing. They are only nine percent of buyers but they account for twenty-six percent of "
    "value."),
   ('Rafael', 'r', 'm2',
    "Critically, this segment does not trust advertising. In our focus groups, the phrase that came up "
    "again and again was that they buy on recommendation. So word of mouth, not advertising, is our main "
    "route to brand awareness."),
   ('Nok', 'n', 'f1',
    "Thank you Rafael. That changes the marketing mix completely. On place, we are skipping retailers "
    "entirely in year one. No wholesaler, no distributor. We sell direct to consumer through our own site "
    "and one online marketplace."),
   ('Nok', 'n', 'f1',
    "On promotion, ninety percent of the budget goes to two hundred micro-influencers — not celebrities, "
    "but dermatologists and chemists with small but trusted audiences. The remaining ten percent is for "
    "free samples sent with every order."),
   ('Nok', 'n', 'f1',
    "On price we hold our international price, which puts us at the top of the market. No discounting in "
    "year one, because a discount now would damage the brand positioning we are trying to build. Our "
    "target is a customer base of forty thousand repeat buyers by the end of year two. Questions?"),
  ],
  'questions': [
   {'q': 'Where does Brazil rank as a beauty market?',
    'o': ['Third-largest in the world', 'Largest in the world',
          'Sixth-largest in the world', 'Second-largest in the world'], 'a': 0,
    'e': u'"Brazil is the third-largest beauty market in the world"'},
   {'q': 'What share do domestic companies hold?',
    'o': ['Sixty-eight percent', 'Twenty-six percent', 'Nine percent', 'Six percent'], 'a': 0,
    'e': u'"Domestic companies hold sixty-eight percent of the market between them"'},
   {'q': 'What is unusual about this market?',
    'o': ['The market leader is local, not global',
          'It is shrinking', 'There is no competition', 'Prices are very low'], 'a': 0,
    'e': u'"the market leader here is local, not global"'},
   {'q': 'How does the team describe its target segment?',
    'o': ['Informed buyers who research ingredients online',
          'Price-sensitive buyers', 'Older buyers aged over fifty', 'Buyers who shop in pharmacies'], 'a': 0,
    'e': u'"We call them the informed buyers: women aged twenty-five to forty, who research ingredients online"'},
   {'q': 'What proportion of value does that segment account for?',
    'o': ['Twenty-six percent', 'Nine percent', 'Sixty-eight percent', 'Forty percent'], 'a': 0,
    'e': u'"They are only nine percent of buyers but they account for twenty-six percent of value" · 9% คือจำนวนคน'},
   {'q': 'What does this segment NOT trust?',
    'o': ['Advertising', 'Dermatologists', 'Online reviews', 'Free samples'], 'a': 0,
    'e': u'"this segment does not trust advertising … they buy on recommendation"'},
   {'q': 'What is the main route to brand awareness?',
    'o': ['Word of mouth', 'Television advertising', 'Billboards', 'Price promotion'], 'a': 0,
    'e': u'"So word of mouth, not advertising, is our main route to brand awareness"'},
   {'q': 'How will the product be sold in year one?',
    'o': ['Direct to consumer, with no retailers or distributors',
          'Through supermarkets', 'Through a national distributor', 'Through pharmacies only'], 'a': 0,
    'e': u'"we are skipping retailers entirely in year one. No wholesaler, no distributor"'},
   {'q': 'Who are the two hundred influencers?',
    'o': ['Dermatologists and chemists with small trusted audiences',
          'Famous actors', 'Sports stars', 'Fashion models'], 'a': 0,
    'e': u'"not celebrities, but dermatologists and chemists with small but trusted audiences"'},
   {'q': 'Why is there no discounting in year one?',
    'o': ['It would damage the brand positioning they are building',
          'Discounts are illegal in Brazil',
          'The margins are already too thin',
          'The distributor forbids it'], 'a': 0,
    'e': u'"a discount now would damage the brand positioning we are trying to build"'},
  ]},

 {'id': 'L3b', 'kind': 'talk',
  'title': 'A Bid That Failed',
  'context': u'วิทยากรเล่ากรณีข้อเสนอซื้อที่ล้มเหลว เพื่อให้เห็นว่าดีลไม่ได้สำเร็จเสมอไป',
  'turns': [
   ('Speaker', 's', 'm2',
    "We spend a lot of time on deals that succeeded. Today I want to do the opposite, because roughly one "
    "in three announced takeovers never completes. Understanding why a bid fails is just as useful."),
   ('Speaker', 's', 'm2',
    "Our case is a European pharmaceutical group — I'll call it Company A — which in March last year "
    "launched a bid for a mid-sized rival, Company B. The opening offer was four point one billion euros, "
    "a premium of eighteen percent over Company B's share price."),
   ('Speaker', 's', 'm2',
    "Company B's board rejected it within four days. Their argument was that the offer undervalued their "
    "drug pipeline — the new medicines still in development. Company A responded by raising the bid to "
    "four point six billion, a premium of about thirty-two percent."),
   ('Speaker', 's', 'm2',
    "At that point three things went wrong at once. First, a second bidder appeared — an American group "
    "that had been watching quietly and had already built up a stake of five percent. That turned it into "
    "a bidding war, which pushes the price up for everyone."),
   ('Speaker', 's', 'm2',
    "Second, the competition authority in Brussels announced it would open a full investigation. The two "
    "companies together would have held over forty percent of one particular treatment market, and "
    "regulators do not like that."),
   ('Speaker', 's', 'm2',
    "Third, and this is the one people forget: during due diligence Company A discovered a manufacturing "
    "problem at two of Company B's plants that had not been disclosed. The cost of fixing it was estimated "
    "at three hundred million euros."),
   ('Speaker', 's', 'm2',
    "In July, Company A withdrew its bid. Its own share price rose four percent on the announcement — "
    "shareholders were relieved. Company B is still independent, and its share price fell twenty-two "
    "percent over the following month."),
   ('Speaker', 's', 'm2',
    "So the lesson. Due diligence is not paperwork. It is the last chance to find out what you are "
    "actually buying, and sometimes the right decision is to walk away."),
  ],
  'questions': [
   {'q': 'Roughly how many announced takeovers never complete?',
    'o': ['About one in three', 'About one in ten', 'About half', 'About one in twenty'], 'a': 0,
    'e': u'"roughly one in three announced takeovers never completes"'},
   {'q': 'What was the opening offer worth?',
    'o': ['4.1 billion euros', '4.6 billion euros', '300 million euros', '41 billion euros'], 'a': 0,
    'e': u'"The opening offer was four point one billion euros" · 4.6 คือข้อเสนอที่ขึ้นแล้ว'},
   {'q': "Why did Company B's board reject the first offer?",
    'o': ['It undervalued their drug pipeline',
          'The premium was too high',
          'They preferred a merger',
          'They had already accepted another bid'], 'a': 0,
    'e': u'"the offer undervalued their drug pipeline — the new medicines still in development"'},
   {'q': 'What premium did the raised bid represent?',
    'o': ['About thirty-two percent', 'About eighteen percent',
          'About five percent', 'About twenty-two percent'], 'a': 0,
    'e': u'"raising the bid to four point six billion, a premium of about thirty-two percent" · 18% คือข้อเสนอแรก'},
   {'q': 'What had the second bidder already done?',
    'o': ['Built up a stake of five percent', 'Made a formal offer',
          'Signed a joint venture', 'Bought a subsidiary'], 'a': 0,
    'e': u'"an American group that had been watching quietly and had already built up a stake of five percent"'},
   {'q': 'Why does a bidding war matter?',
    'o': ['It pushes the price up for everyone',
          'It makes regulators approve faster',
          'It lowers the premium',
          'It forces the target to merge'], 'a': 0,
    'e': u'"That turned it into a bidding war, which pushes the price up for everyone"'},
   {'q': 'Why did the competition authority get involved?',
    'o': ['The two companies would have held over forty percent of one treatment market',
          'The deal was hostile',
          'A factory was going to close',
          'The bidder was foreign'], 'a': 0,
    'e': u'"The two companies together would have held over forty percent of one particular treatment market"'},
   {'q': 'What did due diligence uncover?',
    'o': ['An undisclosed manufacturing problem at two plants',
          'A hidden debt', 'A patent dispute', 'A tax investigation'], 'a': 0,
    'e': u'"during due diligence Company A discovered a manufacturing problem at two of Company B’s plants"'},
   {'q': "What happened to Company A's share price when it withdrew?",
    'o': ['It rose four percent', 'It fell four percent',
          'It fell twenty-two percent', 'It did not move'], 'a': 0,
    'e': u'"Its own share price rose four percent on the announcement — shareholders were relieved"'},
   {'q': "What is the speaker's lesson?",
    'o': ['Due diligence is the last chance to find out what you are buying',
          'Always raise your bid twice',
          'Never bid for a rival',
          'Regulators always block large deals'], 'a': 0,
    'e': u'"Due diligence is not paperwork. It is the last chance to find out what you are actually buying"'},
  ]},
]},

# ══════════════════════════════════ ชุดที่ 4 ══════════════════════════════════
{'id': 'L4', 'title': u'ชุดที่ 4', 'parts': [

 {'id': 'L4a', 'kind': 'presentation',
  'title': 'Repositioning a Budget Airline',
  'context': u'สองคนนำเสนอแผนเปลี่ยนตำแหน่งแบรนด์สายการบินต้นทุนต่ำในยุโรป',
  'turns': [
   ('James', 'j', 'm1',
    "Good afternoon. I'm James and this is Ploy. Our brief was different from the other groups. We were "
    "not asked to enter a new market. We were asked whether SkyLite, an existing budget airline, should "
    "change its brand positioning. Ploy will give you the evidence, then I'll give you the recommendation."),
   ('Ploy', 'p', 'f1',
    "Thank you. Three findings from our research. First, SkyLite has excellent brand awareness — "
    "eighty-one percent of travellers in our survey recognised the name. So awareness is not the problem."),
   ('Ploy', 'p', 'f1',
    "Second, brand image is the problem. When we asked people to describe SkyLite in three words, the most "
    "common words were cheap, crowded and late. Only eleven percent said they would choose SkyLite for a "
    "business trip, even when the schedule suited them."),
   ('Ploy', 'p', 'f1',
    "Third, and this is the commercial point: business travellers are only nineteen percent of passengers "
    "on our routes, but they generate forty-three percent of revenue, because they book late and pay more."),
   ('James', 'j', 'm1',
    "So here is our recommendation, and it is a cautious one. We are not proposing to abandon the budget "
    "market. That would be reckless — it is still eighty-one percent of our revenue base. What we propose "
    "is a mid-market repositioning on three routes only, as a trial."),
   ('James', 'j', 'm1',
    "On those three routes we would add assigned seating, a free cabin bag, and a guaranteed thirty-minute "
    "check-in. Fares would rise by about twelve percent. We would not change the aircraft or the crew."),
   ('James', 'j', 'm1',
    "If the trial works, we roll it out. If it does not, we have lost one quarter of revenue on three "
    "routes, which is manageable. What we must avoid is announcing a full repositioning and then reversing "
    "it, because that damages brand image far more than doing nothing. Thank you."),
  ],
  'questions': [
   {'q': 'What was this group asked to look at?',
    'o': ['Whether an existing airline should change its brand positioning',
          'Whether to enter a new market',
          'Whether to merge with a rival',
          'Whether to buy new aircraft'], 'a': 0,
    'e': u'"We were asked whether SkyLite, an existing budget airline, should change its brand positioning"'},
   {'q': 'What percentage recognised the SkyLite name?',
    'o': ['Eighty-one percent', 'Nineteen percent', 'Forty-three percent', 'Eleven percent'], 'a': 0,
    'e': u'"eighty-one percent of travellers in our survey recognised the name"'},
   {'q': 'Which three words did people most often use?',
    'o': ['Cheap, crowded and late', 'Cheap, fast and friendly',
          'Safe, cheap and modern', 'Late, expensive and crowded'], 'a': 0,
    'e': u'"the most common words were cheap, crowded and late"'},
   {'q': 'What proportion would choose SkyLite for a business trip?',
    'o': ['Eleven percent', 'Nineteen percent', 'Forty-three percent', 'Eighty-one percent'], 'a': 0,
    'e': u'"Only eleven percent said they would choose SkyLite for a business trip"'},
   {'q': 'What share of revenue do business travellers generate?',
    'o': ['Forty-three percent', 'Nineteen percent', 'Twelve percent', 'Eighty-one percent'], 'a': 0,
    'e': u'"business travellers are only nineteen percent of passengers … but they generate forty-three percent of revenue" · 19% คือจำนวนผู้โดยสาร'},
   {'q': 'Why do business travellers pay more?',
    'o': ['They book late', 'They fly longer routes',
          'They buy extra baggage', 'They travel in groups'], 'a': 0,
    'e': u'"because they book late and pay more"'},
   {'q': 'What is the recommendation?',
    'o': ['A mid-market repositioning on three routes as a trial',
          'A full repositioning across all routes',
          'Abandoning the budget market entirely',
          'No change at all'], 'a': 0,
    'e': u'"What we propose is a mid-market repositioning on three routes only, as a trial"'},
   {'q': 'Which of these is NOT part of the trial?',
    'o': ['Changing the aircraft and crew', 'Assigned seating',
          'A free cabin bag', 'A guaranteed thirty-minute check-in'], 'a': 0,
    'e': u'"We would not change the aircraft or the crew"'},
   {'q': 'By how much would fares rise?',
    'o': ['About twelve percent', 'About thirty percent',
          'About forty-three percent', 'About nineteen percent'], 'a': 0,
    'e': u'"Fares would rise by about twelve percent"'},
   {'q': 'What does James say must be avoided?',
    'o': ['Announcing a full repositioning and then reversing it',
          'Running a trial on too few routes',
          'Raising fares at all',
          'Talking to business travellers'], 'a': 0,
    'e': u'"What we must avoid is announcing a full repositioning and then reversing it"'},
  ]},

 {'id': 'L4b', 'kind': 'talk',
  'title': 'A Management Buyout',
  'context': u'วิทยากรเล่ากรณี MBO ของโรงพิมพ์ครอบครัว ให้เห็นว่าต่างจากการถูกซื้อโดยคนนอกอย่างไร',
  'turns': [
   ('Speaker', 's', 'f2',
    "So far we have looked at one company buying another. Today the buyer is different — the buyer is the "
    "management team itself. This is a management buyout, or MBO."),
   ('Speaker', 's', 'f2',
    "The company is a family-owned printing firm in northern England, founded in nineteen sixty-two. By "
    "two thousand and eighteen the founder was seventy-nine and wanted to retire. He had no children in "
    "the business. So he had three options: sell to a competitor, sell to a private equity fund, or sell "
    "to his own managers."),
   ('Speaker', 's', 'f2',
    "He chose the third. Five directors — the managing director, the finance director, and three others — "
    "bought the company for eleven million pounds."),
   ('Speaker', 's', 'f2',
    "Now, the obvious question. Where do five salaried managers find eleven million pounds? They do not. "
    "The structure was this: the managers themselves put in one point one million, which was ten percent, "
    "and most of them remortgaged their houses to do it. A bank lent six million. And the founder himself "
    "left three point nine million in the business, to be repaid over seven years."),
   ('Speaker', 's', 'f2',
    "That last part is common in MBOs and it is called vendor finance — the seller effectively lends the "
    "buyer part of the purchase price. It signals confidence. If the founder did not believe the managers "
    "could run it, he would have wanted all his money on day one."),
   ('Speaker', 's', 'f2',
    "Why did the founder prefer this route? He told the Financial Times two reasons. He wanted the company "
    "to stay in the town, and a competitor would almost certainly have closed the site and moved "
    "production. And he wanted the staff protected — an MBO by people who already work there is far less "
    "likely to lead to redundancies than asset stripping by an outside buyer."),
   ('Speaker', 's', 'f2',
    "Outcome: five years on, the firm employs thirty more people than at the buyout, and the bank loan is "
    "fully repaid. Not every MBO works this well. But it shows why a seller might accept a lower price "
    "from managers than from a trade buyer."),
  ],
  'questions': [
   {'q': 'In an MBO, who is the buyer?',
    'o': ['The management team itself', 'A competitor',
          'A private equity fund', 'The shareholders'], 'a': 0,
    'e': u'"the buyer is the management team itself. This is a management buyout, or MBO"'},
   {'q': 'Why did the founder want to sell?',
    'o': ['He was seventy-nine and wanted to retire, with no children in the business',
          'The company was losing money',
          'A competitor made a hostile bid',
          'The bank forced a sale'], 'a': 0,
    'e': u'"the founder was seventy-nine and wanted to retire. He had no children in the business"'},
   {'q': 'How many directors took part?',
    'o': ['Five', 'Three', 'Seven', 'Two'], 'a': 0,
    'e': u'"Five directors — the managing director, the finance director, and three others"'},
   {'q': 'What was the total purchase price?',
    'o': ['Eleven million pounds', 'Six million pounds',
          'One point one million pounds', 'Three point nine million pounds'], 'a': 0,
    'e': u'"bought the company for eleven million pounds"'},
   {'q': 'How much did the managers put in themselves?',
    'o': ['1.1 million, which was ten percent', '6 million',
          '3.9 million', '11 million'], 'a': 0,
    'e': u'"the managers themselves put in one point one million, which was ten percent"'},
   {'q': 'How did most managers raise their share?',
    'o': ['They remortgaged their houses', 'They sold shares in other companies',
          'They borrowed from family', 'They used savings only'], 'a': 0,
    'e': u'"most of them remortgaged their houses to do it"'},
   {'q': 'What is vendor finance?',
    'o': ['The seller lends the buyer part of the purchase price',
          'The bank lends the whole amount',
          'The buyer pays in shares',
          'A government loan for buyouts'], 'a': 0,
    'e': u'"it is called vendor finance — the seller effectively lends the buyer part of the purchase price"'},
   {'q': 'What does vendor finance signal?',
    'o': ['Confidence that the managers can run the business',
          'That the company is in trouble',
          'That the price was too high',
          'That the bank refused to lend'], 'a': 0,
    'e': u'"It signals confidence. If the founder did not believe the managers could run it, he would have wanted all his money on day one"'},
   {'q': 'Why did the founder avoid selling to a competitor?',
    'o': ['A competitor would probably have closed the site and moved production',
          'A competitor offered less money',
          'A competitor was blocked by regulators',
          'No competitor was interested'], 'a': 0,
    'e': u'"a competitor would almost certainly have closed the site and moved production"'},
   {'q': 'What was the outcome after five years?',
    'o': ['Thirty more staff and the bank loan fully repaid',
          'The company was sold again',
          'Thirty staff were made redundant',
          'The loan was still outstanding'], 'a': 0,
    'e': u'"the firm employs thirty more people than at the buyout, and the bank loan is fully repaid"'},
  ]},
]},

# ══════════════════════════════════ ชุดที่ 5 ══════════════════════════════════
{'id': 'L5', 'title': u'ชุดที่ 5', 'parts': [

 {'id': 'L5a', 'kind': 'presentation',
  'title': 'Market Research Findings for Indonesia',
  'context': u'สามคนรายงานผลวิจัยตลาดอินโดนีเซีย และเสนอว่าควรชะลอการเข้าตลาด',
  'turns': [
   ('Anna', 'a', 'f2',
    "Good morning. I'm Anna. Unlike the other groups, we are going to recommend that we do not launch — at "
    "least not yet. I'll explain the research, Kevin will explain what we found, and Siri will explain what "
    "we think should happen instead."),
   ('Anna', 'a', 'f2',
    "We were asked to test demand for a ready-meal range in Indonesia. We used three methods. Secondary "
    "data from a government statistics office, a questionnaire with fifteen hundred respondents, and "
    "eight focus groups across three cities."),
   ('Kevin', 'k', 'm3',
    "Thanks Anna. On paper this market looks excellent. Two hundred and seventy million people, a growing "
    "middle class, and ready-meal sales up eleven percent last year. Every board paper we have seen says "
    "Indonesia is the obvious next step."),
   ('Kevin', 'k', 'm3',
    "But our focus groups told a different story. Three things came up repeatedly. One: refrigeration. "
    "Only about forty percent of households in our sample had a reliable fridge, and our product needs "
    "chilled storage."),
   ('Kevin', 'k', 'm3',
    "Two: halal certification. Without it we cannot reach the mass market, and certification takes between "
    "nine and fourteen months. Three: price. At our planned price point, a single meal costs about the "
    "same as three meals from a street vendor, and street food is fresher."),
   ('Siri', 's', 'f1',
    "Thank you Kevin. So what do we recommend? Not abandoning Indonesia — the market is real. But we "
    "recommend delaying entry by eighteen months and changing the product."),
   ('Siri', 's', 'f1',
    "Specifically: start halal certification immediately, since that is the longest lead time. Switch from "
    "chilled to ambient — shelf-stable — packaging, which removes the refrigeration problem entirely. And "
    "target a market niche first, not the mass market: office workers in Jakarta buying lunch at "
    "convenience stores."),
   ('Siri', 's', 'f1',
    "One final point. Our recommendation is unpopular, and we know it. But launching a chilled product "
    "into a market where six in ten homes cannot store it is not a marketing problem we can solve with a "
    "bigger advertising budget. Thank you."),
  ],
  'questions': [
   {'q': 'What is this group recommending?',
    'o': ['Not launching yet', 'Launching immediately',
          'Launching in a different country', 'Selling the brand'], 'a': 0,
    'e': u'"we are going to recommend that we do not launch — at least not yet"'},
   {'q': 'How many research methods did they use?',
    'o': ['Three', 'Two', 'Four', 'One'], 'a': 0,
    'e': u'"We used three methods. Secondary data …, a questionnaire …, and eight focus groups"'},
   {'q': 'How many people answered the questionnaire?',
    'o': ['Fifteen hundred', 'Eight hundred', 'Two hundred and seventy', 'Three thousand'], 'a': 0,
    'e': u'"a questionnaire with fifteen hundred respondents"'},
   {'q': 'By how much did ready-meal sales grow last year?',
    'o': ['Eleven percent', 'Forty percent', 'Fourteen percent', 'Seventy percent'], 'a': 0,
    'e': u'"ready-meal sales up eleven percent last year"'},
   {'q': 'What proportion of households had a reliable fridge?',
    'o': ['About forty percent', 'About sixty percent',
          'About eleven percent', 'About ninety percent'], 'a': 0,
    'e': u'"Only about forty percent of households in our sample had a reliable fridge"'},
   {'q': 'How long does halal certification take?',
    'o': ['Between nine and fourteen months', 'Between three and six months',
          'Eighteen months exactly', 'About two years'], 'a': 0,
    'e': u'"certification takes between nine and fourteen months"'},
   {'q': 'How does the price compare with street food?',
    'o': ['One meal costs about the same as three street meals',
          'One meal costs the same as one street meal',
          'It is cheaper than street food',
          'Three meals cost the same as one street meal'], 'a': 0,
    'e': u'"a single meal costs about the same as three meals from a street vendor"'},
   {'q': 'How long a delay do they recommend?',
    'o': ['Eighteen months', 'Nine months', 'Fourteen months', 'Six months'], 'a': 0,
    'e': u'"we recommend delaying entry by eighteen months"'},
   {'q': 'What packaging change do they propose?',
    'o': ['From chilled to ambient, shelf-stable packaging',
          'From ambient to chilled',
          'Smaller pack sizes only',
          'Recyclable packaging'], 'a': 0,
    'e': u'"Switch from chilled to ambient — shelf-stable — packaging, which removes the refrigeration problem"'},
   {'q': "What is Siri's final point?",
    'o': ['A bigger advertising budget cannot solve a storage problem',
          'The advertising budget should be doubled',
          'The team should research again',
          'Indonesia should be abandoned permanently'], 'a': 0,
    'e': u'"launching a chilled product into a market where six in ten homes cannot store it is not a marketing problem we can solve with a bigger advertising budget"'},
  ]},

 {'id': 'L5b', 'kind': 'talk',
  'title': 'A Joint Venture in Batteries',
  'context': u'วิทยากรอธิบายว่าทำไมบางครั้งบริษัทเลือกตั้งกิจการร่วมค้า แทนที่จะซื้อกิจการ',
  'turns': [
   ('Speaker', 's', 'm3',
    "Every case we have studied so far involved one company ending up owning another. Today's case is "
    "different, because nobody buys anybody. This is a joint venture."),
   ('Speaker', 's', 'm3',
    "The two parties are a European car manufacturer and an Asian battery producer. In twenty twenty-one "
    "they set up a joint venture to build a battery plant in Hungary. Each side took fifty percent — an "
    "exact split, which as we will see creates its own problems."),
   ('Speaker', 's', 'm3',
    "Why a joint venture rather than a takeover? Three reasons. First, cost. The plant needed two point "
    "one billion euros. Neither company wanted that on its own balance sheet."),
   ('Speaker', 's', 'm3',
    "Second, and more interesting: what each side actually wanted. The car maker wanted guaranteed supply "
    "of cells. The battery producer wanted a guaranteed customer. Neither wanted to own the other's core "
    "business. The car maker has no interest in running chemical plants, and the battery firm has no "
    "interest in making cars."),
   ('Speaker', 's', 'm3',
    "Third, regulation. A full acquisition of a battery producer by a car manufacturer would have attracted "
    "serious attention from the competition authority. A fifty-fifty joint venture, with a defined and "
    "limited purpose, attracted almost none."),
   ('Speaker', 's', 'm3',
    "Now the problem I mentioned. With a fifty-fifty split, neither partner has control. In year two the "
    "two sides disagreed about whether to expand capacity. The car maker wanted to double output; the "
    "battery producer wanted to wait. There was no mechanism to break the deadlock, and the decision was "
    "delayed by eleven months."),
   ('Speaker', 's', 'm3',
    "They eventually solved it by amending the agreement: an independent chairman now has a casting vote "
    "on capital spending above one hundred million euros. That is the practical lesson. When you set up a "
    "joint venture, agree in advance how you will settle disputes — because you will have them."),
  ],
  'questions': [
   {'q': 'What makes this case different from the others?',
    'o': ['Nobody buys anybody', 'The deal was hostile',
          'A regulator blocked it', 'The buyer paid in shares'], 'a': 0,
    'e': u'"Today’s case is different, because nobody buys anybody. This is a joint venture"'},
   {'q': 'Who are the two parties?',
    'o': ['A European car maker and an Asian battery producer',
          'Two European car makers',
          'Two Asian battery producers',
          'A car maker and a bank'], 'a': 0,
    'e': u'"a European car manufacturer and an Asian battery producer"'},
   {'q': 'Where is the plant?',
    'o': ['Hungary', 'Germany', 'Poland', 'Korea'], 'a': 0,
    'e': u'"they set up a joint venture to build a battery plant in Hungary"'},
   {'q': 'How was ownership split?',
    'o': ['Fifty-fifty', 'Sixty-forty', 'Seventy-thirty', 'Eighty-twenty'], 'a': 0,
    'e': u'"Each side took fifty percent — an exact split"'},
   {'q': 'How much did the plant cost?',
    'o': ['2.1 billion euros', '100 million euros',
          '21 billion euros', '1.2 billion euros'], 'a': 0,
    'e': u'"The plant needed two point one billion euros"'},
   {'q': 'What did the car maker want?',
    'o': ['Guaranteed supply of cells', 'A guaranteed customer',
          'To own a chemical plant', 'To enter the battery market'], 'a': 0,
    'e': u'"The car maker wanted guaranteed supply of cells" · ส่วนผู้ผลิตแบตเตอรี่ต้องการลูกค้าที่แน่นอน'},
   {'q': 'Why did regulation favour a joint venture?',
    'o': ['A full acquisition would have attracted serious attention from the competition authority',
          'Joint ventures pay less tax',
          'Acquisitions are illegal in Hungary',
          'The regulator required a joint venture'], 'a': 0,
    'e': u'"A full acquisition … would have attracted serious attention from the competition authority"'},
   {'q': 'What problem did the fifty-fifty split create?',
    'o': ['Neither partner has control, so a deadlock could not be broken',
          'One side paid more than the other',
          'Profits could not be divided',
          'The plant could not be registered'], 'a': 0,
    'e': u'"With a fifty-fifty split, neither partner has control"'},
   {'q': 'How long was the capacity decision delayed?',
    'o': ['Eleven months', 'Two years', 'Six months', 'Eighteen months'], 'a': 0,
    'e': u'"the decision was delayed by eleven months"'},
   {'q': 'How did they solve it?',
    'o': ['An independent chairman now has a casting vote on large spending',
          'One side bought out the other',
          'They dissolved the joint venture',
          'A regulator decided for them'], 'a': 0,
    'e': u'"an independent chairman now has a casting vote on capital spending above one hundred million euros"'},
  ]},
]},

]
