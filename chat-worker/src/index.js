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
`.trim(),
  },
  audit: {
    name: "การสอบบัญชี",
    scope: `
ขอบเขตของวิชานี้ ณ ตอนนี้คือบทที่ 1 จากตำรา Louwers, Bagley, Blay, Strawser และ Thibodeau
เรื่อง Auditing and Assurance Services

- ความเสี่ยงทางธุรกิจ (business risk) กับความเสี่ยงของข้อมูล (information risk) และความต่างของสองอย่างนี้
- เหตุที่ความต้องการข้อมูลที่เชื่อถือได้เพิ่มขึ้น
- นิยามของการสอบบัญชีงบการเงิน และองค์ประกอบของนิยาม
- ภาพรวมของการสอบบัญชี ว่าผู้สอบบัญชีที่เป็นอิสระเปลี่ยนงบที่น่าเชื่อถือน้อยให้น่าเชื่อถือมากขึ้นอย่างไร
- ข้อกำหนดของผู้บริหาร (management assertions) ตาม PCAOB 5 ข้อ
- ข้อกำหนดตาม ASB ทั้งกลุ่มรายการค้าและเหตุการณ์ และกลุ่มยอดคงเหลือในบัญชี
- การเทียบข้อกำหนดของ PCAOB กับ ASB และการระบุข้อกำหนดจากสถานการณ์
- การสังเกตและสงสัยเยี่ยงผู้ประกอบวิชาชีพ (professional skepticism)
- โครงสร้างสำนักงานสอบบัญชี และเงื่อนไข 3 E

หมายเหตุ ตำราเล่มนี้อธิบายในบริบทของสหรัฐอเมริกา ถ้านิสิตถามถึงบริบทไทย
ให้ชี้ว่ามาตรฐานการสอบบัญชีของไทยกำหนดโดยสภาวิชาชีพบัญชี และควรอ้างอิงประกาศฉบับล่าสุดโดยตรง
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
