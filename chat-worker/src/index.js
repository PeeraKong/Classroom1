import { GoogleGenAI, ApiError } from "@google/genai";
import Anthropic from "@anthropic-ai/sdk";

// ---------------------------------------------------------------------------
// ผู้ช่วยตอบคำถามประจำวิชา — Cloudflare Worker
//
// หน้าเว็บในคลังสื่อการเรียนยิง POST มาที่ /chat แล้ว Worker ตัวนี้เรียกโมเดลให้
// API key อยู่ใน secret ของ Worker เท่านั้น ไม่เคยถูกส่งไปที่เบราว์เซอร์
//
// เลือกผู้ให้บริการได้ด้วยตัวแปร PROVIDER ใน wrangler.toml
//   gemini (ค่าเริ่มต้น) ใช้ GEMINI_API_KEY
//   claude               ใช้ ANTHROPIC_API_KEY
// ---------------------------------------------------------------------------

const DEFAULT_GEMINI_MODEL = "gemini-flash-latest";
const DEFAULT_CLAUDE_MODEL = "claude-sonnet-5";
const MAX_OUTPUT_TOKENS = 8000;

// เพดานความยาว กันคนวางข้อความยาวผิดปกติเข้ามาให้เปลืองโทเคน
const MAX_MESSAGES = 20;
const MAX_CHARS_PER_MESSAGE = 4000;

const SHARED_RULES = `
คุณคือผู้ช่วยติวประจำวิชาในคลังสื่อการเรียนของคณะพาณิชยศาสตร์และการบัญชี จุฬาลงกรณ์มหาวิทยาลัย
ผู้ใช้คือนิสิตปริญญาตรีที่กำลังทบทวนเนื้อหาจากหน้าเว็บของวิชานี้

วิธีตอบ
- ตอบเป็นภาษาไทย แต่คงศัพท์เทคนิคภาษาอังกฤษไว้ในวงเล็บเสมอ เพราะข้อสอบใช้คำอังกฤษ
- ตอบให้ตรงคำถามก่อนในหนึ่งถึงสองประโยค แล้วค่อยขยายความ
- เวลาอธิบายการคำนวณ ให้แสดงวิธีคิดเป็นขั้น ๆ พร้อมตัวเลข ไม่ใช่บอกแต่คำตอบ
- ถ้านิสิตถามว่า "ทำไม" ให้ตอบด้วยเหตุผลเชิงหลักการ ไม่ใช่ท่องนิยาม
- ใช้ **ตัวหนา** เน้นคำสำคัญได้ แต่อย่าใช้หัวข้อหรือตารางแบบ Markdown เพราะกล่องแชทแสดงไม่ได้
- ความยาวพอเหมาะ อย่ายาวเกินจำเป็น

ความซื่อตรงทางวิชาการ
- ถ้าไม่แน่ใจ ให้บอกว่าไม่แน่ใจ และแนะให้ตรวจกับเอกสารประกอบการสอนหรืออาจารย์ผู้สอน
- ห้ามแต่งตัวเลข ชื่อมาตรฐาน เลขย่อหน้า หรือชื่อกรณีศึกษาที่ไม่มีอยู่จริง
- ถ้านิสิตเอาโจทย์การบ้านหรือข้อสอบมาถาม ให้ช่วยด้วยการอธิบายหลักการและยกตัวอย่างที่คล้ายกัน
  แล้วชวนให้เขาลองทำเอง แทนการให้คำตอบสำเร็จรูป
- ถ้าคำถามอยู่นอกขอบเขตวิชานี้ ให้บอกตรง ๆ ว่าอยู่นอกขอบเขต แล้วชวนกลับเข้าเนื้อหา
`.trim();

const SUBJECTS = {
  "adv-acctg-1": {
    name: "การบัญชีขั้นสูง 1 (2601-421)",
    scope: `
ขอบเขตของวิชานี้คือ

บทที่ 1 การบัญชีสำนักงานใหญ่และสาขา
- บัญชีระหว่างกัน (reciprocal accounts) คู่ Branch กับ Home office และคู่ Shipment to branch กับ Shipment from HO
- การบันทึกรายการค้าระหว่างสำนักงานใหญ่กับสาขา
- อุปกรณ์ที่สาขาใช้ 4 กรณี ตามว่าใครจ่ายเงินและสมุดของใครบันทึกสินทรัพย์
- งบทดลอง งบกำไรขาดทุนของแต่ละหน่วยงาน และรายการปิดบัญชี
- กระดาษทำการงบการเงินรวมและรายการตัดบัญชี
- ราคาสินค้าที่ส่งไปสาขา ทั้งราคาทุน ราคาทุนบวกกำไรส่วนเพิ่ม และราคาตลาด
- การกระทบยอดเมื่อยอด Branch กับ Home office ไม่ตรงกัน
- ค่าขนส่งส่วนเกินระหว่างสาขา

บทที่ 2 การรวมธุรกิจ ตาม TFRS 3
- รูปแบบการรวมธุรกิจ 4 แบบ และสัดส่วนการถือหุ้นกับมาตรฐานที่ใช้
- นิยามของธุรกิจ และการทดสอบการกระจุกตัวของมูลค่ายุติธรรม
- วิธีซื้อ (acquisition method) 4 ขั้นตอน
- การรับรู้และวัดมูลค่าสินทรัพย์ที่ระบุได้และหนี้สินที่รับมา พร้อมข้อยกเว้น
- ค่าความนิยม การปันส่วนราคาซื้อ และกำไรจากการต่อรองราคาซื้อ
- ต้นทุนที่เกี่ยวข้องกับการซื้อ และต้นทุนการออกตราสารทุนหรือตราสารหนี้
- สินทรัพย์ไม่มีตัวตนที่ระบุได้
- ระยะเวลาในการวัดมูลค่า และการเปิดเผยข้อมูล
- การรวมธุรกิจภายใต้การควบคุมเดียวกัน (BCUCC) ด้วยวิธีมูลค่าตามบัญชี

บทที่ 3 การทำงบการเงินรวม ณ วันซื้อหุ้น
- ความสัมพันธ์บริษัทใหญ่กับบริษัทย่อย และความต่างจากการซื้อสินทรัพย์ในบทที่ 2
- การควบคุมตาม TFRS 10 คือ อำนาจ ผลตอบแทนที่ผันแปร และความเชื่อมโยงของสองข้อนี้
- กรณีที่ควบคุมได้แม้ถือหุ้นไม่ถึงกึ่งหนึ่งหรือไม่ถือหุ้นเลย
- ข้อยกเว้นสี่ข้อที่ทำให้ไม่ต้องจัดทำงบการเงินรวม
- การซื้อธุรกิจแบบย้อนกลับ (reverse acquisition)
- การบันทึกบัญชีของบริษัทใหญ่เมื่อซื้อหุ้น ทั้งจ่ายเงินสด โอนสินทรัพย์ และออกหุ้น
- ขั้นตอนการจัดทำงบการเงินรวมและรายการตัดบัญชีบนกระดาษทำการ
- กรณีซื้อที่มูลค่าตามบัญชี จ่ายสูงกว่าจนเกิดค่าความนิยม บริษัทย่อยมีค่าความนิยมเดิม และจ่ายต่ำกว่าจนเกิดกำไรจากการต่อรองราคาซื้อ
- การซื้อหุ้นบางส่วนและส่วนได้เสียที่ไม่มีอำนาจควบคุม (NCI) พร้อมสองวิธีวัดมูลค่า NCI
- สำรองตามกฎหมาย และการปรับนโยบายการบัญชีให้เหมือนกัน
- ทฤษฎีความเป็นหน่วยงาน (entity theory) เทียบกับทฤษฎีความเป็นเจ้าของ (proprietary theory) ที่เลิกใช้แล้ว
- สินทรัพย์ถาวรที่มีค่าเสื่อมราคาสะสม และการล้างค่าเสื่อมราคาสะสมของบริษัทย่อย

บทที่ 4 การจัดทำงบการเงินรวมภายหลังวันซื้อหุ้น
- ความต่างระหว่างงบการเงินเฉพาะกิจการกับงบการเงินรวม และเหตุที่บัญชีเงินลงทุนในบริษัทย่อยหายไปในงบรวม
- สามทางเลือกในงบเฉพาะกิจการ คือ วิธีราคาทุน (2550+) ตามที่กำหนดใน TFRS 9 (2563+) และวิธีส่วนได้เสีย (2560+)
  โดยต้องใช้วิธีเดียวกันสำหรับเงินลงทุนประเภทเดียวกัน
- วิธีราคาทุน การบันทึกเงินลงทุนเริ่มแรกและการรับรู้เงินปันผลเป็นรายได้เมื่อมีสิทธิได้รับ
- ทางเลือกตาม TFRS 9 ทั้ง FVTPL สำหรับที่ถือไว้เพื่อค้า และ FVOCI สำหรับที่ไม่ได้ถือไว้เพื่อค้า
  รวมถึงความต่างเรื่องต้นทุนการทำรายการและปลายทางของกำไรขาดทุนเมื่อขาย
- วิธีส่วนได้เสีย นิยาม หลักการ และรายการบันทึกบัญชีสี่แบบ คือ ลงทุนเริ่มแรก ส่วนแบ่งกำไรหรือขาดทุน
  เงินปันผลที่หักจากบัญชีเงินลงทุน และส่วนแบ่งในกำไรขาดทุนเบ็ดเสร็จอื่น
- กฎสำคัญว่ากำไรสุทธิของบริษัทใหญ่ตามวิธีส่วนได้เสียเท่ากับกำไรส่วนที่เป็นของบริษัทใหญ่ในงบการเงินรวมเสมอ
  พร้อมตัวอย่างจากงบจริงปี 2567 ของ PTG (ใช้ราคาทุน ตัวเลขไม่ตรง) แลนด์แอนด์เฮ้าส์ และ AIS (ใช้ส่วนได้เสีย ตัวเลขตรงกัน)
- ตัวอย่างเดินยาวสามปี ซื้อ 60% ราคา 400,000 ส่วนของผู้ถือหุ้น 500,000 สิทธิบัตร 80,000 อายุ 10 ปี
  ค่าความนิยม 52,000 ยอดเงินลงทุนปลายปี 413,200 / 414,400 / 433,600 และยอด NCI 240,800 / 241,600 / 254,400
- ตารางไล่ยอดสามชุด คือ ส่วนของผู้ถือหุ้น ส่วนที่ตีเพิ่ม และค่าความนิยม พร้อมการพิสูจน์ยอดเงินลงทุนสามทาง
- การเปรียบเทียบวิธีราคาทุนกับวิธีส่วนได้เสีย และข้อที่ว่างบการเงินรวมออกมาเหมือนกันไม่ว่าเลือกวิธีใด
- บริษัทร่วมตามมาตรฐานการบัญชีฉบับที่ 28 และอิทธิพลอย่างมีนัยสำคัญ เกณฑ์ 20% ที่เป็นข้อสันนิษฐานหักล้างได้สองทาง
- การนำเสนองบการเงินสามกรณี ตามว่ามีบริษัทย่อย บริษัทร่วม หรือทั้งสองอย่าง
- วิธีส่วนได้เสียกับบริษัทร่วม ค่าความนิยมรวมอยู่ในมูลค่าเงินลงทุน ส่วนกรณีจ่ายต่ำกว่าถือเป็นรายได้ในงวดที่ซื้อ
  และข้อยกเว้นที่ไม่ต้องใช้วิธีส่วนได้เสีย
- การเลิกใช้วิธีส่วนได้เสีย ทั้งกรณีกลายเป็นบริษัทย่อยและกรณีเหลือเป็นสินทรัพย์ทางการเงิน
  รวมถึงการตีมูลค่าส่วนที่เหลือด้วยมูลค่ายุติธรรม และการจัดประเภทกำไรขาดทุนเบ็ดเสร็จอื่นใหม่
`.trim(),
  },
  audit: {
    name: "การสอบบัญชี",
    scope: `
ขอบเขตของวิชานี้คือบทที่ 1, 3 และ 4 จากตำรา Louwers, Bagley, Blay, Strawser และ Thibodeau
เรื่อง Auditing and Assurance Services โดยบทที่ 2 ไม่ได้อยู่ในเอกสารที่ใช้ทำสื่อนี้

บทที่ 1 ความต้องการข้อมูลที่เชื่อถือได้และข้อกำหนดของผู้บริหาร

- ความเสี่ยงทางธุรกิจ (business risk) กับความเสี่ยงของข้อมูล (information risk) และความต่างของสองอย่างนี้
- เหตุที่ความต้องการข้อมูลที่เชื่อถือได้เพิ่มขึ้น
- นิยามของการสอบบัญชีงบการเงิน และองค์ประกอบของนิยาม
- ภาพรวมของการสอบบัญชี ว่าผู้สอบบัญชีที่เป็นอิสระเปลี่ยนงบที่น่าเชื่อถือน้อยให้น่าเชื่อถือมากขึ้นอย่างไร
- ข้อกำหนดของผู้บริหาร (management assertions) ตาม PCAOB 5 ข้อ
- ข้อกำหนดตาม ASB ทั้งกลุ่มรายการค้าและเหตุการณ์ และกลุ่มยอดคงเหลือในบัญชี
- การเทียบข้อกำหนดของ PCAOB กับ ASB และการระบุข้อกำหนดจากสถานการณ์
- การสังเกตและสงสัยเยี่ยงผู้ประกอบวิชาชีพ (professional skepticism)
- โครงสร้างสำนักงานสอบบัญชี และเงื่อนไข 3 E

บทที่ 3 การวางแผนงานสอบบัญชี
- กิจกรรมก่อนรับงาน คือการรับหรือคงไว้ซึ่งลูกค้า ความเป็นอิสระและจรรยาบรรณ และหนังสือตอบรับงาน
- การติดต่อผู้สอบบัญชีคนเดิม ผู้สอบบัญชีคนใหม่เป็นฝ่ายที่ต้องพยายามติดต่อ ต้องได้รับอนุญาตจากลูกค้าก่อน
  และต้องถามเรื่องความซื่อสัตย์ของผู้บริหาร ข้อขัดแย้งกับผู้บริหาร และเหตุผลที่เปลี่ยนผู้สอบบัญชี
- ความเป็นอิสระสามด้าน คือ in fact, in mental attitude และ in appearance
- หนังสือตอบรับงาน (engagement letter) ในฐานะสัญญา และสิ่งที่ต้องระบุไว้
- แผนการสอบบัญชี (audit plan) และเป้าหมายสามข้อของการวางแผน
- การจัดทีมงาน การใช้ผลงานของผู้ตรวจสอบภายใน และการใช้ผู้เชี่ยวชาญทั้งฝั่งผู้สอบบัญชีและฝั่งกิจการ
- งบประมาณเวลาและรายงานเวลา งานระหว่างงวด (interim) กับงานสิ้นงวด (year-end)
- ความมีสาระสำคัญ เกณฑ์เชิงปริมาณและเชิงคุณภาพ ความสัมพันธ์แบบบนลงล่างระหว่าง overall materiality
  กับ performance materiality และการใช้ความมีสาระสำคัญในการวางแผน ประเมินหลักฐาน และออกรายงาน
- วัตถุประสงค์สามข้อของวิธีการตรวจสอบ คือ risk assessment procedures, tests of controls
  และ substantive procedures
- ตารางเชื่อมข้อกำหนดกับหลักฐานและวิธีการตรวจสอบ (Exhibit 3.6)
- ประเภทของวิธีการตรวจสอบทั้งแปด และความต่างของ vouching (บัญชีไปหาเอกสาร ทดสอบ existence
  หรือ occurrence) กับ tracing (เอกสารไปหาบัญชี ทดสอบ completeness)
- วิธีวิเคราะห์เปรียบเทียบห้ารูปแบบ และข้อที่ว่าบังคับในขั้นวางแผนและขั้นสอบทานตอนจบงาน
  แต่ไม่บังคับในขั้นทดสอบ
- เอกสารหลักฐานการสอบบัญชี แฟ้มถาวรกับแฟ้มปีปัจจุบัน เกณฑ์ผู้สอบบัญชีที่มีประสบการณ์ซึ่งไม่เคย
  เกี่ยวข้องกับงาน บัญชีที่มีสาระสำคัญและข้อกำหนดที่เกี่ยวข้อง และการเก็บรักษาเอกสาร
  (ไม่ใช่บริษัทมหาชน 5 ปีและ 60 วัน บริษัทมหาชน 7 ปีและ 14 วัน)

บทที่ 4 การประเมินความเสี่ยง
- ความเสี่ยงในการสอบบัญชี (audit risk) และองค์ประกอบสามตัว คือ inherent risk, control risk
  และ detection risk พร้อมปัจจัยที่กระทบแต่ละตัว
- ความเสี่ยงจากการแสดงข้อมูลที่ขัดต่อข้อเท็จจริงอันเป็นสาระสำคัญ RMM = IR x CR ซึ่งเป็นความเสี่ยง
  ฝั่งลูกค้าที่ผู้สอบบัญชีประเมินได้แต่เปลี่ยนไม่ได้ ส่วน DR เป็นตัวเดียวที่ผู้สอบบัญชีควบคุมได้
- แบบจำลองความเสี่ยง AR = IR x CR x DR และการจัดรูปเป็น DR = AR หารด้วย (IR x CR)
- ผลของระดับ DR ต่อลักษณะ เวลา และขอบเขตของวิธีการตรวจสอบ และเมทริกซ์กำหนดระดับ DR จาก IR กับ CR
- sampling risk กับ nonsampling risk
- การทุจริตและความเสี่ยงจากการทุจริต โดยเจตนา (intent) เป็นสิ่งที่แยกการทุจริตออกจากข้อผิดพลาด
- สามกลุ่มปัจจัยที่บ่งชี้ความเสี่ยงจากการรายงานทางการเงินที่เป็นเท็จ
- ประเภทของการทุจริต คือ fraudulent financial reporting กับ misappropriation of assets
  และศัพท์ employee fraud, embezzlement, larceny, defalcation
- การประเมินความเสี่ยงสืบเนื่อง ตารางเทียบประเภทข้อผิดพลาดกับข้อกำหนดที่ถูกละเมิด
  และปัจจัยที่ทำให้บัญชีอ่อนไหว
- ความเข้าใจธุรกิจของลูกค้าและแหล่งข้อมูล
- วิธีวิเคราะห์เปรียบเทียบขั้นต้นและห้าขั้นตอนของการทำ
- การประชุมระดมสมองของทีมซึ่งเป็นวิธีการที่บังคับ และกลุ่มบุคคลที่ต้องสอบถาม
- คำถาม what can go wrong กับบัญชีที่มีสาระสำคัญและข้อกำหนดที่เกี่ยวข้อง
- ข้อสันนิษฐานว่าการรับรู้รายได้ที่ไม่เหมาะสมเป็นความเสี่ยงจากการทุจริต การล้มล้างการควบคุม
  โดยผู้บริหาร และความเสี่ยงที่มีนัยสำคัญ
- การสื่อสารความเสี่ยงจากการทุจริต โดยรายงานสูงกว่าผู้เกี่ยวข้องอย่างน้อยหนึ่งระดับ และการทุจริต
  ของผู้บริหารถือว่ามีสาระสำคัญเสมอ
- การไม่ปฏิบัติตามกฎหมายและข้อบังคับ แบบ direct-effect กับ indirect-effect และความรับผิดชอบ
  ของผู้สอบบัญชีที่ต่างกัน พร้อมสัญญาณบ่งชี้
- การจัดทำเอกสารการประเมินความเสี่ยง และบันทึกกลยุทธ์การสอบบัญชี (audit strategy memorandum)

หมายเหตุ ตำราเล่มนี้อธิบายในบริบทของสหรัฐอเมริกา ถ้านิสิตถามถึงบริบทไทย
ให้ชี้ว่ามาตรฐานการสอบบัญชีของไทยกำหนดโดยสภาวิชาชีพบัญชี และควรอ้างอิงประกาศฉบับล่าสุดโดยตรง
`.trim(),
  },
  marketing: {
    name: "หลักการตลาด (Principles of Marketing)",
    scope: `
ขอบเขตของวิชานี้คือเนื้อหาสอบกลางภาค อ้างอิงตำรา Kotler และ Armstrong เรื่อง Principles of Marketing
มี 5 บท คือบทที่ 1, 3, 4, 5 และ 6 โดยบทที่ 2 ไม่ได้อยู่ในเอกสารที่ใช้ทำสื่อนี้

บทที่ 1 กระบวนการการตลาด
- นิยามการตลาดของ Kotler ว่าเป็นกระบวนการที่บริษัทสร้างคุณค่าให้ลูกค้าและสร้างความสัมพันธ์
  เพื่อเก็บเกี่ยวคุณค่ากลับคืน รวมถึงนิยามของ AMA ปี 2017
- มุมมองเก่าคือ telling and selling เทียบมุมมองใหม่คือการตอบสนองความต้องการของลูกค้า
- กระบวนการการตลาด 5 ขั้น โดยขั้นที่ 1 ถึง 4 คือสร้างคุณค่า และขั้นที่ 5 คือเก็บเกี่ยวคุณค่ากลับคืน
- แนวคิดแกนกลาง 5 ข้อ คือ needs wants demands, market offerings, value และ satisfaction,
  exchanges และ relationships, และ markets
- Needs คือสภาวะรู้สึกขาด Wants คือรูปแบบที่ needs แปลงไปตามวัฒนธรรมและบุคลิกภาพ
  Demands คือ wants ที่มีกำลังซื้อหนุนหลัง
- Marketing myopia คือการสนใจตัวสินค้ามากกว่าประโยชน์และประสบการณ์ที่สินค้าสร้าง
- กับดักการตั้งความคาดหวังทั้งต่ำเกินไปและสูงเกินไป
- Marketing management, segmentation, targeting, value proposition, demand management และ de-marketing
- แนวคิดการจัดการการตลาด 5 แบบ คือ production, product, selling, marketing และ societal marketing
- ความต่างของ selling concept ที่เริ่มจากโรงงาน กับ marketing concept ที่เริ่มจากตลาด
- ส่วนประสมการตลาด 4P และความสำคัญของการบูรณาการ
- CRM, customer-perceived value, customer satisfaction, การ delight ลูกค้า และโปรแกรมสร้างความภักดี
- Customer lifetime value, share of customer, customer equity และความต่างจาก share of market
- ภูมิทัศน์ที่เปลี่ยนไป ได้แก่ ดิจิทัล AI และ big data องค์กรไม่แสวงหากำไร โลกาภิวัตน์ และความยั่งยืน
- ข้อวิจารณ์ทางสังคมและจริยธรรมทางการตลาด

บทที่ 3 สภาพแวดล้อมทางการตลาด
- นิยามสภาพแวดล้อมทางการตลาด และความต่างระหว่าง microenvironment กับ macroenvironment
- ผู้แสดงใน microenvironment 6 กลุ่ม คือ บริษัทเอง ซัพพลายเออร์ คนกลาง คู่แข่ง สาธารณชน และลูกค้า
- Publics 7 ประเภท และ customer markets 5 ตลาด
- PESTLE ครบ 6 ด้าน คือ political, economic, social, technological, legal และ environmental
- เหตุผล 3 ข้อของกฎหมายธุรกิจ และกฎหมายการตลาดไทยทั้งยุคดั้งเดิมและยุคดิจิทัลรวมถึง PDPA
- ระบบเศรษฐกิจ 3 แบบ คือ industrial, subsistence และ developing และการกระจายรายได้ที่สร้างตลาดแบบแบ่งชั้น
- ประชากรศาสตร์และ 5 เจเนอเรชัน คือ Baby Boomers 1946-1964, Gen X 1965-1980, Gen Y 1981-1996,
  Gen Z 1997-2012 และ Gen Alpha 2013-2025 พร้อมประโยคสรุป Trust Me, Help Me, Understand Me,
  Represent Me และ Engage Me
- Core beliefs และ secondary beliefs และผลของวัฒนธรรมต่อกลยุทธ์ข้ามชาติ
- เทคโนโลยี IoT และสิ่งแวดล้อมทางธรรมชาติกับความยั่งยืน
- SWOT โดย S กับ W เป็นเรื่องภายใน ส่วน O กับ T เป็นเรื่องภายนอก
- การตอบสนองแบบ reactive เทียบ proactive

บทที่ 4 การบริหารสารสนเทศทางการตลาดและการวิจัยตลาด
- Customer insights และความต่างจากข้อมูลดิบ ปัญหาสมัยนี้ไม่ใช่การขาดข้อมูลแต่คือการแปลงข้อมูลเป็นความเข้าใจ
- Marketing information ecosystem 3 ช่วง และหลักการถ่วงดุลข้อมูลที่อยากได้กับที่จำเป็นต้องมี
- ข้อมูลภายในและข้อจำกัด และ competitive marketing intelligence ที่ใช้เฉพาะข้อมูลที่เปิดเผยต่อสาธารณะ
- กระบวนการวิจัยตลาด 4 ขั้น
- ประเภทการวิจัย 3 แบบ คือ exploratory, descriptive และ causal
- Secondary data เทียบ primary data และลำดับที่ควรใช้
- วิธีวิจัย ได้แก่ observation, survey, interview และ focus group, customer insight communities,
  experiment, digital text analysis, biosensors และ online tracking
- Ethnographic research และข้อจำกัดของการสังเกตที่มองไม่เห็นความรู้สึกและพฤติกรรมระยะยาว
- A/B testing และ online listening, behavioral targeting, social targeting
- วิธีติดต่อ 4 แบบ คือ mail, telephone, personal และ online พร้อมข้อดีข้อเสียของแต่ละแบบ
- แผนสุ่มตัวอย่าง 3 คำถาม คือ sampling unit, sample size และ sampling procedure
- เครื่องมือวิจัย ทั้งแบบสอบถามและเครื่องมือกลไกรวมถึง neuromarketing
- Big data, marketing analytics และประเด็นความเป็นส่วนตัวกับการใช้ผลวิจัยในทางที่ผิด

บทที่ 5 พฤติกรรมผู้บริโภค
- นิยามตลาดผู้บริโภคและพฤติกรรมผู้ซื้อ
- แบบจำลองกล่องดำ คือ สิ่งเร้าเข้า ผ่านกล่องดำ แล้วออกมาเป็นการตอบสนอง
- ปัจจัย 4 กลุ่ม คือ cultural, social, personal และ psychological
- วัฒนธรรม วัฒนธรรมย่อย และชนชั้นทางสังคม 7 ระดับ ซึ่งวัดจากส่วนผสมของอาชีพ รายได้ การศึกษา และความมั่งคั่ง
- Reference groups, opinion leaders, influencer marketing, ครอบครัว และความต่างของ role กับ status
- Age, occupation, economic situation, lifestyle, personality และ self-concept
- Motivation และ Maslow, perception ที่มี selective attention distortion และ retention,
  learning, beliefs และ attitudes
- กระบวนการตัดสินใจซื้อ 5 ขั้น และแหล่งข้อมูล 4 ประเภท
- สองสิ่งที่ขวางระหว่างความตั้งใจกับการซื้อจริง คือ ทัศนคติของผู้อื่นและปัจจัยเชิงสถานการณ์ที่ไม่คาดคิด
- สมการความพอใจ สมรรถนะต่ำกว่าความคาดหวังคือผิดหวัง เท่ากันคือพอใจ สูงกว่าคือปลื้ม
- Adoption process 5 ขั้น คือ awareness, interest, evaluation, trial และ adoption
- Adopter categories 5 กลุ่ม คือ innovators 2.5 เปอร์เซ็นต์ early adopters 13.5 เปอร์เซ็นต์
  early mainstream 34 เปอร์เซ็นต์ late mainstream 34 เปอร์เซ็นต์ และ lagging adopters 16 เปอร์เซ็นต์
- คุณลักษณะ 6 ข้อที่กำหนดอัตราการยอมรับ โดย 4 ข้อแรกเร่งการยอมรับ ส่วน complexity และ perceived risk ชะลอ

บทที่ 6 กลยุทธ์การตลาดที่ขับเคลื่อนด้วยลูกค้า หรือ STP
- สี่ขั้นคือ segmentation, targeting, differentiation และ positioning พร้อมนิยามของแต่ละขั้น
  โดย positioning คือการครองพื้นที่ที่ชัดเจน โดดเด่น และน่าปรารถนา ในใจของผู้บริโภคเป้าหมาย
  และ product position คือวิธีที่ผู้บริโภคนิยามสินค้าจากคุณลักษณะที่สำคัญ
- ฐานการแบ่งส่วนตลาดผู้บริโภค 4 ฐาน คือ geographic, demographic, psychographic และ behavioral
- ประชากรศาสตร์ ตัวแปรที่ใช้บ่อยคือ อายุและช่วงวงจรชีวิต เพศ และรายได้
  ตัวอย่างคือ Disney Cruise Lines เจาะครอบครัวที่มีลูก และ Harley-Davidson ที่ผู้หญิงเป็นกลุ่มโตเร็วที่สุด
  คิดเป็น 12 เปอร์เซ็นต์ของยอดซื้อรถใหม่
- จิตวิทยา แบ่งจากชนชั้นทางสังคม รูปแบบการดำเนินชีวิต หรือบุคลิกภาพ ตัวอย่างคือ Panera และ Zipcar
- พฤติกรรม 5 ตัวแปร คือ occasions, benefits sought, user status, usage rate และ loyalty status
  โดย user status แบ่งเป็น nonusers, ex-users, potential users, first-time users และ regular users
  ส่วน usage rate แบ่งเป็น light, medium และ heavy
- multiple segmentation และระบบเชิงพาณิชย์ คือ Mosaic USA ของ Experian ที่มี 71 ส่วนตลาด
  กับ 19 ระดับความมั่งคั่ง และ Personicx ของ Acxiom
- การแบ่งส่วนตลาดธุรกิจ มีตัวแปรเพิ่ม 4 กลุ่ม คือ operating characteristics, purchasing approaches,
  situational factors และ personal characteristics
- เกณฑ์ 5 ข้อของการแบ่งส่วนที่ได้ผล คือ measurable, accessible, substantial, differentiable และ actionable
- การประเมินส่วนตลาด 3 เรื่อง คือ ขนาดและการเติบโต ความน่าสนใจเชิงโครงสร้าง และวัตถุประสงค์กับทรัพยากรของบริษัท
- กลยุทธ์การเลือกตลาดเป้าหมาย 4 แบบ เรียงจากกว้างไปแคบ คือ undifferentiated หรือ mass marketing,
  differentiated หรือ segmented marketing, concentrated หรือ niche marketing และ micromarketing
  โดย micromarketing แบ่งเป็น local marketing และ individual marketing ซึ่งเรียกอีกชื่อว่า
  one-to-one marketing หรือ mass customization
- ปัจจัย 5 ข้อที่ใช้เลือกกลยุทธ์ คือ ทรัพยากรของบริษัท ความแปรผันของสินค้า ขั้นในวงจรชีวิตของสินค้า
  ความแปรผันของตลาด และกลยุทธ์การตลาดของคู่แข่ง
- การตลาดเป้าหมายที่รับผิดชอบต่อสังคม ประเด็นเรื่องกลุ่มเปราะบาง กลุ่มน้อย กลุ่มด้อยโอกาส และเด็กกับวัยรุ่น
- persona ในฐานะการแปลงส่วนตลาดให้เป็นภาพคนหนึ่งคน
- positioning map แสดงการรับรู้ของผู้บริโภคต่อแบรนด์เทียบคู่แข่งบนมิติการซื้อที่สำคัญ
  โดยขนาดของวงกลมบอกส่วนแบ่งตลาดสัมพัทธ์
- กลยุทธ์การสร้างความแตกต่างและการวางตำแหน่ง 4 ขั้น และ competitive advantage
  คือความได้เปรียบที่ได้จากการเสนอคุณค่าที่มากกว่า ด้วยราคาที่ต่ำกว่าหรือประโยชน์ที่มากกว่าจนคุ้มราคาที่สูงกว่า
- มิติของการสร้างความแตกต่าง 5 มิติ คือ product, services, channels, people และ image
- เกณฑ์ 7 ข้อของความได้เปรียบที่คุ้มค่าจะสื่อสาร คือ important, distinctive, superior, communicable,
  preemptive, affordable และ profitable
- value proposition คือการวางตำแหน่งทั้งชุดของแบรนด์ ตารางไขว้ระหว่างประโยชน์กับราคา
  ข้อเสนอที่ชนะคือ more for more, more for the same, more for less, the same for less
  และ less for much less โดย more for less เป็น best winning proposition
  ส่วนช่องที่ให้เท่าเดิมหรือน้อยลงในราคาเท่าเดิมหรือแพงขึ้นคือข้อเสนอที่แพ้
- positioning statement ตามรูปแบบ To (ส่วนตลาดเป้าหมายและความต้องการ) our (แบรนด์) is (แนวคิด)
  that (จุดที่แตกต่าง) พร้อมตัวอย่างของ Evernote
  และหลักที่ว่าส่วนประสมการตลาดทุกตัวต้องสนับสนุนกลยุทธ์การวางตำแหน่งที่เลือกไว้

หมายเหตุ ตัวเลขสัดส่วนชนชั้นทางสังคมและตัวอย่างส่วนใหญ่อยู่ในบริบทสหรัฐอเมริกาตามตำรา
ถ้านิสิตถามถึงบริบทไทยให้ระบุว่าตัวเลขอาจต่างออกไป และถ้าถามเรื่องบทที่ 2 ให้บอกว่าอยู่นอกขอบเขตของสื่อชุดนี้
`.trim(),
  },
  erp: {
    name: "ระบบวางแผนทรัพยากรองค์กร (ERP)",
    scope: `
ขอบเขตของวิชานี้คือ

บทที่ 1 ERP และ SAP
- ตลาด ERP และผู้เล่นหลัก SAP กับ Oracle ความหมายของ Tier-1 ERP
- องค์กรยุคก่อน ERP ที่แยกตามหน้าที่ (functional area) ระบบแยกกัน มี interface คั่น และต้องทำ audit กับ reconciliation
- กรณีศึกษาบริษัท A ใช้เวลาราว 2 นาที เทียบกับบริษัท B ที่ใช้ฐานข้อมูลกลางแล้วเหลือราว 5 วินาที
- ความต่างระหว่าง business function กับ business process และระบบบูรณาการ (integrated information system)
- ที่มาของคำว่า ERP โดย Gartner Group ปี 1990 ต่อยอดจาก MRP และ MRP II และนิยามของ ERP
- คุณลักษณะ 5 ข้อ ได้แก่ Integrated System, Real Time, Best Practice, Customizing (Configuration) และ Process Oriented
- เป้าหมายเชิงกลยุทธ์ 4 ข้อ และระบบสารสนเทศ 4 ระดับ คือ OLTP, MIS, DSS, EIS
- โมดูลของ ERP ทั่วไป และ Enterprise Application รุ่นแรกที่ครอบคลุมเฉพาะงาน back office
- ประวัติ SAP ก่อตั้งปี 1972 ที่ Mannheim โดยอดีตนักวิเคราะห์ระบบของ IBM 5 คน ที่มาของชื่อย่อทั้งสองความหมาย และการย้ายสำนักงานใหญ่ไป Walldorf ปี 1977
- วิวัฒนาการ R/1 ปี 1973 สถาปัตยกรรม 1 ชั้น, R/2 ปี 1978 สถาปัตยกรรม 2 ชั้น, R/3 ปี 1992 สถาปัตยกรรม 3 ชั้น และตัว R ย่อมาจาก Real-time
- สถาปัตยกรรม 3 ชั้น Presentation, Application (ABAP), Database และเรื่อง scalability
- โมดูลของ SAP ได้แก่ FI, CO, AM, TR, MM, SD, LE, PP, QM, PM, PS, HR, CA (WF และ Office), IS พร้อมชั้นเทคนิค BC (SAP Basis) และภาษา ABAP กับ ABAP Workbench
- แนวคิด Best Practice ที่ธุรกิจต้องปรับกระบวนการเข้าหาซอฟต์แวร์ และเครื่องมือ Business Engineering กับ Business Navigator
- Industry Solution ICOE ปี 1995 IBU ปี 1998 และข้อสำคัญว่าโมดูล IS เช่น IS-OIL ต้องติดตั้งเป็น Add-On ไม่ได้อยู่ในแกนหลัก
- SAP Business One เทียบกับ SAP Business ByDesign ทั้งกลุ่มเป้าหมาย จำนวนผู้ใช้ และงบประมาณติดตั้ง รวมถึงกรณี Microsoft ที่ใช้ SAP แทน Dynamics ของตัวเอง
- แพลตฟอร์มฮาร์ดแวร์ที่รองรับ ตั้งแต่ PC Server, Mini Computer จนถึง Mainframe

บทที่ 2 การใช้งาน SAP (SAP Navigation)
- SAP GUI ในฐานะ presentation server และ SAP Logon ที่ใช้เลือกระบบ
- การเข้าสู่ระบบด้วย Client, User, Password และ Logon Language ระบบตัวอย่างของวิชาคือ SID AC4 client 900
- ความหมายของ Client ว่าเป็นหน่วยข้อมูลอิสระในระบบเดียวกัน และเรื่อง multiple logon
- หน้าจอ SAP Easy Access ทั้ง user menu และ SAP menu
- โครงสร้างหน้าจอ 6 ส่วน คือ menu bar, standard toolbar, title bar, application toolbar, screen body และ status bar
- ปุ่มบน standard toolbar โดยเฉพาะความต่างระหว่าง Enter กับ Save และระหว่าง Back, Exit, Cancel
- Transaction code คืออะไร โดยปกติยาว 4 ตัวอักษร ทุกฟังก์ชันมี T-Code ผูกอยู่
- วิธีหา T-Code จาก status bar, เมนู System แล้ว Status และการเปิดแสดงชื่อทางเทคนิคที่ Extras แล้ว Settings
- Command Field (OK Code Field) และคำสั่ง /n, /o, /i, /nend, /nex พร้อมรูปแบบ /n ตามด้วย T-Code และ /o ตามด้วย T-Code
- Session การสร้างและปิด ข้อความ Maximum number of sessions reached และพารามิเตอร์ที่ RZ11
- ปุ่ม F1 (help และ technical information รวมถึง Parameter ID) กับ F4 (value help หรือ possible entry)
- Decimal notation และ date format ตั้งที่ SU01 สำหรับผู้ใช้คนอื่น และ SU3 สำหรับตัวเอง
- Parameter ID ที่ตั้งเป็นค่าเริ่มต้นของช่องข้อมูลผ่านแท็บ Parameters ของ SU3
- การรันรายงาน ABAP ที่ SA38 ทั้งแบบ foreground ที่มีเพดานเวลาจนเกิด time limit exceeded และแบบ background ที่ติดตามที่ SMX รวมถึงความต่างจาก SE38 ที่ใช้เขียนโปรแกรม
- Favorites, ธีมของ SAP GUI (Enjoy, Blue Crystal, Quartz), SBWP ที่เป็นเมลภายใน และ SPRO ที่ใช้ตั้งค่าระบบ
- T-Code ที่ใช้ในแบบฝึกหัดของระบบ AC4 ได้แก่ F-02, SE38, SU01, VA01, SU03, SA38, SM04

บทที่ 3 การนำระบบมาใช้ (SAP ERP Implementation)
- วิธี ASAP หรือ Accelerated SAP ซึ่งเป็น waterfall project methodology
- 5 เฟส คือ Project Preparation, Business Blueprint, Realization, Final Preparation, Go-Live and Support และเส้นทางต่อไปเป็น Continuous Improvement
- กิจกรรมที่ปรากฏในทุกเฟส ได้แก่ Project Management, Organizational Change Management, Training และ Quality Check
- คนในโครงการ แบ่งเป็นสาย Technical (Basis Administrator, ABAP Programmer) และสาย Functional (FI, CO, MM, SD)
- Configuration ผ่าน IMG (Implementation Guide) ที่เปิดด้วย SPRO
- ตัวอย่างกระบวนการจ่ายเงินเจ้าหนี้ ทั้งแบบทีละรายการและ Automatic Payment Program ที่ F110
- งานก่อน Go-Live ได้แก่ integration test, data conversion และ end user training รวมถึงคำว่า cutover
- การเปลี่ยนมือจากบริษัทที่ปรึกษาไปเป็นทีม IT ขององค์กรเองหลัง Go-Live
- ต้นทุนรวมของการเป็นเจ้าของในอัตราส่วน 1 ต่อ 2 ต่อ 4 คือ hardware, software license และ implementation รวมถึงค่าสนับสนุนรายปีที่ราว 22 เปอร์เซ็นต์ของค่าลิขสิทธิ์
- กรณีศึกษา Exotic Food Thailand ปิดงบจาก 14 วันเหลือ 8 วัน คำนวณวัตถุดิบจาก 3 ชั่วโมงเหลือ 2 ถึง 3 นาที รายได้ปี 2023 โต 31 เปอร์เซ็นต์ด้วยพนักงานเท่าเดิม และอัตราลาออกลดเหลือ 3 เปอร์เซ็นต์

หมายเหตุ วิชานี้อิงระบบ SAP R/3 หรือ SAP ERP แบบ on-premise ตามเอกสารประกอบการสอน
ถ้านิสิตถามถึง SAP S/4HANA หรือ SAP Fiori ให้บอกตรง ๆ ว่าอยู่นอกขอบเขตของเอกสารชุดนี้
และค่า Client, User, Password ที่ปรากฏเป็นค่าตัวอย่างของระบบฝึกปฏิบัติเท่านั้น
`.trim(),
  },
};

const json = (obj, status, origin) =>
  new Response(JSON.stringify(obj), {
    status,
    headers: { "content-type": "application/json; charset=utf-8", ...cors(origin) },
  });

function cors(origin) {
  return {
    "access-control-allow-origin": origin || "*",
    "access-control-allow-methods": "POST, OPTIONS",
    "access-control-allow-headers": "content-type",
    "access-control-max-age": "86400",
    vary: "origin",
  };
}

/** อนุญาตเฉพาะ origin ที่ตั้งไว้ใน ALLOWED_ORIGINS (คั่นด้วยจุลภาค) — ว่าง = อนุญาตทุกที่ */
function resolveOrigin(request, env) {
  const origin = request.headers.get("origin");
  const allowed = (env.ALLOWED_ORIGINS || "")
    .split(",")
    .map((s) => s.trim())
    .filter(Boolean);
  if (allowed.length === 0) return origin || "*";
  return origin && allowed.includes(origin) ? origin : null;
}

/**
 * นับโควตารายวันต่อผู้ใช้หนึ่งคน เก็บใน KV และหมดอายุเองหลัง 48 ชั่วโมง
 * คืน null เมื่อยังไม่เกิน หรือคืนจำนวนที่ใช้ไปแล้วเมื่อเกินโควตา
 */
async function checkQuota(env, clientId) {
  if (!env.CHAT_KV) return null; // ไม่ได้ผูก KV ไว้ = ไม่จำกัด
  const limit = Number(env.DAILY_LIMIT || 40);
  if (!Number.isFinite(limit) || limit <= 0) return null;

  const day = new Date().toISOString().slice(0, 10);
  const key = `q:${day}:${clientId}`;
  const used = Number((await env.CHAT_KV.get(key)) || 0);
  if (used >= limit) return used;
  await env.CHAT_KV.put(key, String(used + 1), { expirationTtl: 60 * 60 * 48 });
  return null;
}

function sanitize(messages) {
  if (!Array.isArray(messages) || messages.length === 0) return null;
  const trimmed = messages.slice(-MAX_MESSAGES);
  const out = [];
  for (const m of trimmed) {
    if (!m || (m.role !== "user" && m.role !== "assistant")) return null;
    if (typeof m.content !== "string" || m.content.trim() === "") return null;
    out.push({ role: m.role, content: m.content.slice(0, MAX_CHARS_PER_MESSAGE) });
  }
  // บทสนทนาต้องเริ่มด้วยฝั่งผู้ใช้เสมอ ทั้งสองผู้ให้บริการ
  while (out.length && out[0].role !== "user") out.shift();
  return out.length ? out : null;
}

/** เลือกผู้ให้บริการและตรวจว่ามีคีย์ครบ คืน {name, key, model} หรือ null */
function resolveProvider(env) {
  const name = (env.PROVIDER || "gemini").toLowerCase();
  if (name === "claude") {
    if (!env.ANTHROPIC_API_KEY) return null;
    return { name, key: env.ANTHROPIC_API_KEY, model: env.CLAUDE_MODEL || DEFAULT_CLAUDE_MODEL };
  }
  if (!env.GEMINI_API_KEY) return null;
  return { name: "gemini", key: env.GEMINI_API_KEY, model: env.GEMINI_MODEL || DEFAULT_GEMINI_MODEL };
}

/**
 * ยิงคำถามไปยัง Gemini แล้วส่งข้อความกลับทีละส่วนผ่าน onText
 * Gemini ใช้ role ว่า "model" แทน "assistant" และรับ system prompt ผ่าน config.systemInstruction
 */
async function streamGemini(provider, system, messages, onText) {
  const ai = new GoogleGenAI({ apiKey: provider.key });
  const stream = await ai.models.generateContentStream({
    model: provider.model,
    contents: messages.map((m) => ({
      role: m.role === "assistant" ? "model" : "user",
      parts: [{ text: m.content }],
    })),
    config: {
      systemInstruction: system,
      maxOutputTokens: MAX_OUTPUT_TOKENS,
    },
  });
  for await (const chunk of stream) {
    const text = chunk.text;
    if (text) await onText(text);
  }
}

/** ยิงคำถามไปยัง Claude แล้วส่งข้อความกลับทีละส่วนผ่าน onText */
async function streamClaude(provider, system, messages, onText) {
  const client = new Anthropic({ apiKey: provider.key });
  const stream = client.messages.stream({
    model: provider.model,
    max_tokens: MAX_OUTPUT_TOKENS,
    system,
    thinking: { type: "adaptive" },
    messages,
  });
  for await (const event of stream) {
    if (event.type === "content_block_delta" && event.delta.type === "text_delta") {
      await onText(event.delta.text);
    }
  }
  await stream.finalMessage();
}

/** แปลงข้อผิดพลาดของแต่ละผู้ให้บริการเป็นรหัสเดียวกัน เพื่อให้หน้าเว็บแสดงข้อความไทยได้ */
function errorCode(err, providerName) {
  if (providerName === "gemini") {
    if (err instanceof ApiError) {
      // คีย์ผิดของ Google กลับมาเป็น 400 ไม่ใช่ 401 จึงต้องดูเหตุผลในเนื้อความด้วย
      // ไม่อย่างนั้นความผิดพลาดที่พบบ่อยที่สุดจะขึ้นข้อความว่า "คำขอไม่ถูกต้อง" ซึ่งชี้ทางผิด
      const detail = String(err.message || "");
      if (detail.includes("API_KEY_INVALID") || detail.includes("API key not valid")) {
        return "bad_api_key";
      }
      if (detail.includes("RESOURCE_EXHAUSTED") || err.status === 429) return "upstream_rate_limited";
      if (err.status === 401 || err.status === 403) return "upstream_forbidden";
      if (err.status === 400) return "bad_request";
      return "upstream_error";
    }
    return "server_error";
  }
  // เรียงจากเฉพาะเจาะจงไปกว้าง เพื่อแยกกรณีที่ลองใหม่ได้ออกจากกรณีที่ลองใหม่ไม่ช่วย
  if (err instanceof Anthropic.RateLimitError) return "upstream_rate_limited";
  if (err instanceof Anthropic.AuthenticationError) return "bad_api_key";
  if (err instanceof Anthropic.PermissionDeniedError) return "upstream_forbidden";
  if (err instanceof Anthropic.BadRequestError) return "bad_request";
  if (err instanceof Anthropic.InternalServerError) return "upstream_error";
  if (err instanceof Anthropic.APIConnectionError) return "upstream_unreachable";
  if (err instanceof Anthropic.APIError) return "upstream_error";
  return "server_error";
}

export default {
  async fetch(request, env, ctx) {
    const origin = resolveOrigin(request, env);

    if (request.method === "OPTIONS") {
      return new Response(null, { status: 204, headers: cors(origin || "") });
    }
    if (origin === null) {
      return json({ error: "origin_not_allowed" }, 403, "");
    }
    if (request.method !== "POST") {
      return json({ error: "method_not_allowed" }, 405, origin);
    }

    const provider = resolveProvider(env);
    if (!provider) {
      return json({ error: "server_not_configured" }, 500, origin);
    }

    let body;
    try {
      body = await request.json();
    } catch {
      return json({ error: "bad_json" }, 400, origin);
    }

    // รหัสเข้าใช้ของชั้นเรียน — ตั้งค่า ACCESS_CODE ไว้จึงจะบังคับ
    if (env.ACCESS_CODE && body.accessCode !== env.ACCESS_CODE) {
      return json({ error: "bad_access_code" }, 401, origin);
    }

    const subject = SUBJECTS[body.subject];
    if (!subject) {
      return json({ error: "unknown_subject" }, 400, origin);
    }

    const messages = sanitize(body.messages);
    if (!messages) {
      return json({ error: "bad_messages" }, 400, origin);
    }

    const clientId =
      (typeof body.clientId === "string" && body.clientId.slice(0, 64)) ||
      request.headers.get("cf-connecting-ip") ||
      "unknown";
    const over = await checkQuota(env, clientId);
    if (over !== null) {
      return json({ error: "quota_exceeded", used: over }, 429, origin);
    }

    const system = `${SHARED_RULES}\n\nวิชาที่นิสิตกำลังทบทวนคือ ${subject.name}\n\n${subject.scope}`;

    const { readable, writable } = new TransformStream();
    const writer = writable.getWriter();
    const enc = new TextEncoder();
    const send = (obj) => writer.write(enc.encode(`data: ${JSON.stringify(obj)}\n\n`));

    ctx.waitUntil(
      (async () => {
        let sent = 0;
        try {
          const onText = async (text) => {
            sent += text.length;
            await send({ text });
          };
          if (provider.name === "gemini") {
            await streamGemini(provider, system, messages, onText);
          } else {
            await streamClaude(provider, system, messages, onText);
          }
          if (sent === 0) {
            // โมเดลไม่ส่งข้อความกลับเลย มักเกิดจากตัวกรองความปลอดภัยของผู้ให้บริการ
            await send({ error: "empty_response" });
          } else {
            await send({ done: true });
          }
        } catch (err) {
          const code = errorCode(err, provider.name);
          console.error(provider.name, code, err && err.message);
          await send({ error: code });
        } finally {
          await writer.close();
        }
      })()
    );

    return new Response(readable, {
      headers: {
        "content-type": "text/event-stream; charset=utf-8",
        "cache-control": "no-store",
        connection: "keep-alive",
        ...cors(origin),
      },
    });
  },
};
