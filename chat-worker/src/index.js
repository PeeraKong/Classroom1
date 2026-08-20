import Anthropic from "@anthropic-ai/sdk";

// ---------------------------------------------------------------------------
// ผู้ช่วยตอบคำถามประจำวิชา — Cloudflare Worker
//
// หน้าเว็บในคลังสื่อการเรียนยิง POST มาที่ /chat แล้ว Worker ตัวนี้เรียก Claude ให้
// API key อยู่ใน secret ของ Worker เท่านั้น ไม่เคยถูกส่งไปที่เบราว์เซอร์
// ---------------------------------------------------------------------------

const MODEL = "claude-sonnet-5";

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
  // Claude ต้องเริ่มด้วย user เสมอ
  while (out.length && out[0].role !== "user") out.shift();
  return out.length ? out : null;
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
    if (!env.ANTHROPIC_API_KEY) {
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

    const client = new Anthropic({ apiKey: env.ANTHROPIC_API_KEY });
    const system = `${SHARED_RULES}\n\nวิชาที่นิสิตกำลังทบทวนคือ ${subject.name}\n\n${subject.scope}`;

    const { readable, writable } = new TransformStream();
    const writer = writable.getWriter();
    const enc = new TextEncoder();
    const send = (obj) => writer.write(enc.encode(`data: ${JSON.stringify(obj)}\n\n`));

    ctx.waitUntil(
      (async () => {
        try {
          const stream = client.messages.stream({
            model: MODEL,
            max_tokens: 8000,
            system,
            thinking: { type: "adaptive" },
            output_config: { effort: env.EFFORT || "medium" },
            messages,
          });

          for await (const event of stream) {
            if (
              event.type === "content_block_delta" &&
              event.delta.type === "text_delta"
            ) {
              await send({ text: event.delta.text });
            }
          }

          const final = await stream.finalMessage();
          await send({ done: true, stop_reason: final.stop_reason });
        } catch (err) {
          // เรียงจากเฉพาะเจาะจงไปกว้าง เพื่อแยกกรณีที่ลองใหม่ได้ออกจากกรณีที่ลองใหม่ไม่ช่วย
          let code = "server_error";
          if (err instanceof Anthropic.RateLimitError) code = "upstream_rate_limited";
          else if (err instanceof Anthropic.AuthenticationError) code = "bad_api_key";
          else if (err instanceof Anthropic.PermissionDeniedError) code = "upstream_forbidden";
          else if (err instanceof Anthropic.BadRequestError) code = "bad_request";
          else if (err instanceof Anthropic.InternalServerError) code = "upstream_error";
          else if (err instanceof Anthropic.APIConnectionError) code = "upstream_unreachable";
          else if (err instanceof Anthropic.APIError) code = "upstream_error";
          console.error(code, err && err.message);
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
