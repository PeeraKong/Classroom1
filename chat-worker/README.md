# ผู้ช่วยตอบคำถาม (Cloudflare Worker)

Backend ตัวกลางที่เก็บ API key ไว้ฝั่งเซิร์ฟเวอร์ หน้าเว็บของแต่ละวิชายิงคำถามมาที่นี่
แล้ว Worker ค่อยเรียกโมเดลให้ตอบ แล้วสตรีมกลับไปทีละคำ

รองรับสองผู้ให้บริการ สลับได้ที่ `PROVIDER` ใน `wrangler.toml`

| ค่า | โมเดล | คีย์ที่ต้องตั้ง |
|---|---|---|
| `gemini` (ค่าเริ่มต้น) | `gemini-flash-latest` | `GEMINI_API_KEY` |
| `claude` | `claude-sonnet-5` | `ANTHROPIC_API_KEY` |

**คีย์ไม่เคยถูกส่งไปที่เบราว์เซอร์** — นี่คือเหตุผลทั้งหมดที่ต้องมีตัวกลาง ห้ามใส่ API key
ลงในไฟล์ HTML โดยตรงเด็ดขาด เพราะใครกดดู source ก็เอาไปใช้ได้

## สิ่งที่ต้องมีก่อน

1. บัญชี [Cloudflare](https://dash.cloudflare.com/sign-up) — ฟรี ไม่ต้องผูกบัตร
2. **API key ของผู้ให้บริการที่เลือก**
   - Gemini — สร้างที่ [Google AI Studio](https://aistudio.google.com/apikey) ใช้บัญชี Google ธรรมดา
   - Claude — สร้างที่ [Anthropic Console](https://console.anthropic.com) คนละอันกับ Claude Pro ที่ใช้คุยผ่านเว็บ
3. **Node.js v22 ขึ้นไป** — Cloudflare Wrangler บังคับ เช็คด้วย `node -v` ถ้าต่ำกว่านี้ให้โหลดตัว LTS จาก [nodejs.org](https://nodejs.org) แล้วเปิด Terminal ใหม่

## ติดตั้งครั้งแรก — ทางลัด

```bash
cd chat-worker
node setup.mjs
```

สคริปต์จะทำให้ทั้งหมด ตั้งแต่ติดตั้ง dependency ล็อกอิน Cloudflare สร้าง KV แล้วผูก id ให้เอง
deploy และ**เอา URL ที่ได้ไปใส่ในหน้าเว็บทุกวิชาให้อัตโนมัติ** มีสองจังหวะเท่านั้นที่ต้องใช้มือคุณ
คือกด Allow ตอนล็อกอิน และวาง API key

รันซ้ำได้ ขั้นตอนไหนทำไปแล้วจะข้ามให้เอง คำสั่งย่อยที่มีให้

```bash
node setup.mjs link https://ชื่อ.workers.dev   # เอา URL ใส่หน้าเว็บอย่างเดียว
node setup.mjs unlink                          # เอา URL ออก ปุ่มแชทจะหายไป
```

ถ้าอยากทำเองทีละขั้น อ่านหัวข้อถัดไป

## ติดตั้งแบบทีละขั้น

```bash
cd chat-worker
npm install
npx wrangler login          # เปิดเบราว์เซอร์ให้ล็อกอิน Cloudflare
```

### ใส่ API key เป็น secret

```bash
npx wrangler secret put GEMINI_API_KEY
# วางคีย์แล้วกด Enter
```

ถ้าใช้ Claude ให้เปลี่ยน `PROVIDER = "claude"` ใน `wrangler.toml` แล้วตั้ง `ANTHROPIC_API_KEY` แทน

### เช็คว่าคีย์ใช้โมเดลไหนได้บ้าง

`gemini-flash-latest` เป็น alias ที่ชี้ไปยังรุ่น flash ปัจจุบันเสมอ ถ้าอยากตรึงรุ่นหรือดูว่ามีรุ่นอะไรให้ใช้

```bash
node -e "const {GoogleGenAI}=require('@google/genai');
new GoogleGenAI({apiKey:process.env.GEMINI_API_KEY}).models.list()
  .then(async p=>{for await(const m of p) console.log(m.name)})"
```

แล้วเอาชื่อที่ได้ไปใส่ `GEMINI_MODEL` ใน `wrangler.toml`

### (ทางเลือก) ตั้งรหัสเข้าใช้ของชั้นเรียน

ถ้าอยากให้เฉพาะนิสิตในวิชาใช้ได้ ตั้งรหัสไว้แล้วแจกในห้องเรียน

```bash
npx wrangler secret put ACCESS_CODE
```

นิสิตต้องเก็บรหัสไว้ในเบราว์เซอร์ครั้งแรกด้วยการเปิด Console (F12) แล้วพิมพ์

```js
localStorage.setItem("classroom-access-code", "รหัสที่อาจารย์แจก")
```

ถ้าไม่ตั้ง `ACCESS_CODE` ใครก็ใช้ได้ที่หน้าเว็บนั้น — ควบคุมค่าใช้จ่ายด้วยโควตารายวันแทน

### (แนะนำ) เปิดโควตารายวัน

```bash
npx wrangler kv namespace create CHAT_KV
```

เอา `id` ที่ได้ไปใส่ใน `wrangler.toml` แล้วลบ `#` หน้าสามบรรทัดของ `[[kv_namespaces]]` ออก
ถ้าไม่ผูก KV ระบบจะ **ไม่จำกัดจำนวนครั้ง** ซึ่งเสี่ยงต่อค่าใช้จ่าย

### แก้โดเมนที่อนุญาต

ใน `wrangler.toml` ตั้ง `ALLOWED_ORIGINS` เป็นโดเมนเว็บจริงของคุณ เช่น `https://peerakong.github.io`
เว็บอื่นจะเรียก Worker นี้ไม่ได้ กันคนเอา endpoint ไปใช้ฟรี

### Deploy

```bash
npx wrangler deploy
```

จะได้ URL หน้าตาแบบ `https://classroom-chat.<ชื่อบัญชี>.workers.dev`

> **ครั้งแรกของบัญชีใหม่** Cloudflare จะถามว่าจะจด subdomain ของ `workers.dev` ไหม ให้ตอบ **yes**
> ถ้าเผลอตอบ no หรือ deploy ขึ้น `You need to register a workers.dev subdomain` ให้เปิดลิงก์
> `dash.cloudflare.com/.../workers/onboarding` ที่แสดงในข้อความ ตั้งชื่อ subdomain แล้ว deploy ใหม่
> เป็นการตั้งค่าครั้งเดียวของบัญชี

## เชื่อมหน้าเว็บเข้ากับ Worker

เปิดไฟล์ `index.html` ของแต่ละวิชา เลื่อนไปท้ายไฟล์ หา

```js
var ENDPOINT = "";
```

แล้วเปลี่ยนเป็น

```js
var ENDPOINT = "https://classroom-chat.<ชื่อบัญชี>.workers.dev/chat";
```

**ตราบใดที่ยังว่างอยู่ ปุ่มแชทจะไม่ปรากฏเลย** และหน้าเว็บทำงานปกติทุกอย่าง —
ตั้งใจออกแบบไว้แบบนี้ เพื่อให้เว็บใช้งานได้ก่อนที่จะ deploy Worker

## เพิ่มวิชาใหม่

1. เพิ่มรายการใน `SUBJECTS` ของ `src/index.js` พร้อมขอบเขตเนื้อหาของวิชานั้น
   (ขอบเขตนี้สำคัญ — เป็นตัวบอกผู้ช่วยว่าอะไรอยู่ในวิชา อะไรอยู่นอกวิชา)
2. `npx wrangler deploy`
3. คัดลอก `widget.template.html` ไปแปะท้าย `index.html` ของวิชานั้น แล้วแก้
   `__SUBJECT__`, `__LABEL__`, `__HINT__` และ `ENDPOINT`

## ค่าใช้จ่าย

ราคาและโควตาฟรีของแต่ละผู้ให้บริการเปลี่ยนบ่อย **ให้ดูจากหน้าราคาอย่างเป็นทางการก่อนเปิดใช้จริง**
— [ราคา Gemini API](https://ai.google.dev/pricing) และ [ราคา Claude](https://www.anthropic.com/pricing)
Gemini มีโควตาให้ทดลองใช้ฟรีในระดับหนึ่ง ซึ่งมักพอสำหรับการใช้ในชั้นเรียน

ตัวคุมค่าใช้จ่ายที่ตั้งไว้แล้วในโค้ด

| กลไก | ค่าเริ่มต้น | แก้ที่ |
|---|---|---|
| โควตาต่อคนต่อวัน | 40 ครั้ง | `DAILY_LIMIT` ใน `wrangler.toml` |
| ความยาวคำตอบสูงสุด | 8,000 token | `max_tokens` ใน `src/index.js` |
| จำนวนข้อความที่ส่งย้อนหลัง | 20 ข้อความ | `MAX_MESSAGES` |
| ความยาวต่อข้อความ | 4,000 ตัวอักษร | `MAX_CHARS_PER_MESSAGE` |

ตั้งงบจำกัดหรือเปิดการแจ้งเตือนที่หน้า console ของผู้ให้บริการด้วย จะได้ไม่มีเซอร์ไพรส์

> โควตารายวันนับจากรหัสประจำเบราว์เซอร์ที่เก็บใน localStorage ซึ่งนิสิตล้างทิ้งเพื่อรีเซ็ตได้
> ถ้าต้องการกันจริงจังให้ตั้ง `ACCESS_CODE` ร่วมด้วย

## ทดสอบก่อน deploy

```bash
echo 'GEMINI_API_KEY=...' > .dev.vars   # ไฟล์นี้อยู่ใน .gitignore แล้ว
npx wrangler dev
```

แล้วยิงทดสอบ

```bash
curl -N -X POST http://127.0.0.1:8787/chat \
  -H 'Origin: https://peerakong.github.io' \
  -H 'content-type: application/json' \
  -d '{"subject":"audit","messages":[{"role":"user","content":"ทดสอบ"}]}'
```

## ข้อจำกัดที่ต้องรู้

- **ใช้ได้เฉพาะเว็บไซต์จริง** เช่น GitHub Pages — ในหน้าพรีวิวของ Artifact
  การเรียกออกนอกโดเมนถูกบล็อกไว้ ปุ่มจะกดได้แต่จะขึ้นข้อความบอกว่าใช้ได้เฉพาะเว็บจริง
- **ผู้ช่วยตอบผิดได้** มีคำเตือนแสดงอยู่ใต้ช่องพิมพ์ตลอด และ system prompt สั่งให้บอกเมื่อไม่แน่ใจ
  รวมทั้งไม่ให้เฉลยการบ้านตรง ๆ แต่ให้อธิบายหลักการแล้วชวนนิสิตลองทำเอง
- ผู้ช่วยเห็นเฉพาะ **ขอบเขตเนื้อหาที่เขียนไว้ใน `SUBJECTS`** ไม่ได้อ่านหน้าเว็บหรือ PDF จริง
  ถ้าเพิ่มบทใหม่ในหน้าเว็บ อย่าลืมมาเพิ่มขอบเขตตรงนี้ด้วย

## วิชาที่ตั้งขอบเขตไว้แล้ว

| คีย์ใน `SUBJECTS` | วิชา | หน้าเว็บ |
|---|---|---|
| `adv-acctg-1` | การบัญชีขั้นสูง 1 (2601-421) | `adv-acctg-1/index.html` |
| `audit` | การสอบบัญชี | `audit/index.html` |
| `erp` | ระบบวางแผนทรัพยากรองค์กร (ERP) | `erp/index.html` |
