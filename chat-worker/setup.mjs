#!/usr/bin/env node
// ---------------------------------------------------------------------------
// ตัวช่วยติดตั้งผู้ช่วยตอบคำถาม — ใช้ได้ทั้ง Windows, macOS และ Linux
//
//   node setup.mjs            ติดตั้งทั้งหมดตั้งแต่ต้นจนจบ
//   node setup.mjs link <url> แค่เอา URL ของ Worker ไปใส่ในหน้าเว็บทุกวิชา
//   node setup.mjs unlink     เอา URL ออกจากหน้าเว็บทุกวิชา (ปุ่มแชทจะหายไป)
//
// สคริปต์นี้รันซ้ำได้ ไม่พัง ขั้นตอนไหนทำไปแล้วจะข้ามให้เอง
// ---------------------------------------------------------------------------

import { spawnSync } from "node:child_process";
import { readFileSync, writeFileSync, existsSync, readdirSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import { createInterface } from "node:readline/promises";

const here = dirname(fileURLToPath(import.meta.url));
const repoRoot = join(here, "..");
const wranglerToml = join(here, "wrangler.toml");

const c = {
  b: (s) => `\x1b[1m${s}\x1b[0m`,
  dim: (s) => `\x1b[2m${s}\x1b[0m`,
  ok: (s) => `\x1b[32m${s}\x1b[0m`,
  warn: (s) => `\x1b[33m${s}\x1b[0m`,
  err: (s) => `\x1b[31m${s}\x1b[0m`,
};

const step = (n, total, text) => console.log(`\n${c.b(`[${n}/${total}]`)} ${c.b(text)}`);
const note = (text) => console.log(`      ${c.dim(text)}`);

/** รันคำสั่งแบบให้ผู้ใช้เห็นและโต้ตอบได้ เช่น ตอนล็อกอินหรือวางคีย์ */
function runVisible(cmd, args) {
  const r = spawnSync(cmd, args, { cwd: here, stdio: "inherit", shell: process.platform === "win32" });
  return r.status === 0;
}

/** รันคำสั่งแล้วเก็บผลไว้อ่าน เช่น ตอนหา id ของ KV หรือ URL ที่ deploy ได้ */
function runCapture(cmd, args) {
  const r = spawnSync(cmd, args, { cwd: here, encoding: "utf8", shell: process.platform === "win32" });
  const out = `${r.stdout || ""}${r.stderr || ""}`;
  process.stdout.write(out);
  return { ok: r.status === 0, out };
}

/** หาไฟล์ index.html ของทุกวิชา คือโฟลเดอร์ชั้นเดียวที่มีวิดเจ็ตแชทอยู่ */
function coursePages() {
  return readdirSync(repoRoot, { withFileTypes: true })
    .filter((d) => d.isDirectory() && !d.name.startsWith(".") && d.name !== "chat-worker" && d.name !== "node_modules")
    .map((d) => join(repoRoot, d.name, "index.html"))
    .filter((p) => existsSync(p) && readFileSync(p, "utf8").includes("var ENDPOINT ="));
}

function setEndpoint(url) {
  const pages = coursePages();
  if (pages.length === 0) {
    console.log(c.warn("      ไม่พบหน้าวิชาที่มีวิดเจ็ตแชท ข้ามขั้นตอนนี้"));
    return 0;
  }
  let changed = 0;
  for (const p of pages) {
    const before = readFileSync(p, "utf8");
    const after = before.replace(/var ENDPOINT = "[^"]*";/, `var ENDPOINT = "${url}";`);
    if (after !== before) {
      writeFileSync(p, after);
      changed++;
      console.log(`      ${c.ok("✓")} ${p.replace(repoRoot + "/", "").replace(repoRoot + "\\", "")}`);
    }
  }
  return changed;
}

async function ask(rl, question, fallback = "") {
  const a = (await rl.question(`      ${question} `)).trim();
  return a || fallback;
}

// --------------------------- โหมดย่อย ---------------------------

const mode = process.argv[2];

if (mode === "link" || mode === "unlink") {
  const url = mode === "unlink" ? "" : (process.argv[3] || "").trim();
  if (mode === "link" && !/^https:\/\/\S+$/.test(url)) {
    console.log(c.err("ใช้แบบนี้: node setup.mjs link https://ชื่อ.workers.dev/chat"));
    process.exit(1);
  }
  const n = setEndpoint(url.endsWith("/chat") || url === "" ? url : `${url.replace(/\/$/, "")}/chat`);
  console.log(mode === "unlink"
    ? c.ok(`\nเอา URL ออกจาก ${n} หน้าแล้ว ปุ่มแชทจะไม่แสดง`)
    : c.ok(`\nใส่ URL ลงใน ${n} หน้าแล้ว`));
  process.exit(0);
}

// --------------------------- ติดตั้งเต็มรูปแบบ ---------------------------

// wrangler ต้องการ Node 22 ขึ้นไป ถ้าไม่เช็คตรงนี้ ผู้ใช้จะไปเจอ error ภาษาอังกฤษ
// กลางคันหลังติดตั้ง dependency ไปแล้ว ซึ่งอ่านยากและไม่บอกว่าต้องทำอะไรต่อ
const NODE_MIN = 22;
const nodeMajor = Number(process.versions.node.split(".")[0]);
if (nodeMajor < NODE_MIN) {
  console.log(c.err(`\nNode.js ในเครื่องเป็นรุ่น v${process.versions.node} ซึ่งเก่าเกินไป`));
  console.log(`Cloudflare Wrangler ต้องการ ${c.b("v" + NODE_MIN + " ขึ้นไป")}\n`);
  console.log(c.b("วิธีแก้ที่ง่ายที่สุด"));
  console.log("  1. เปิด https://nodejs.org แล้วโหลดปุ่ม LTS");
  console.log("  2. เปิดไฟล์ที่โหลดมา กด Next ไปจนจบ");
  console.log("  3. " + c.b("ปิดหน้าต่าง Terminal นี้แล้วเปิดใหม่") + " (สำคัญ ไม่งั้นจะยังเห็นรุ่นเก่า)");
  console.log("  4. เช็คด้วย " + c.b("node -v") + " ต้องขึ้น v22 ขึ้นไป แล้วรัน node setup.mjs อีกครั้ง\n");
  console.log(c.dim("ถ้าใช้ nvm อยู่แล้ว:  nvm install 22 && nvm use 22"));
  console.log(c.dim("ถ้าใช้ Homebrew:      brew install node@22\n"));
  process.exit(1);
}

console.log(c.b("\nติดตั้งผู้ช่วยตอบคำถามประจำวิชา"));
console.log(c.dim("จะมีสองจังหวะที่ต้องใช้มือคุณ คือล็อกอิน Cloudflare และวาง API key"));
console.log(c.dim("นอกนั้นสคริปต์จัดการให้ทั้งหมด · กด Ctrl+C เพื่อหยุดได้ทุกเมื่อ"));

const rl = createInterface({ input: process.stdin, output: process.stdout });
const TOTAL = 7;

try {
  // 1 ────────────────────────────────────────────────────────────
  step(1, TOTAL, "ติดตั้ง dependency");
  if (!runVisible("npm", ["install"])) {
    console.log(c.err("      npm install ไม่สำเร็จ ตรวจว่าติดตั้ง Node.js แล้วหรือยัง"));
    process.exit(1);
  }

  // 2 ────────────────────────────────────────────────────────────
  step(2, TOTAL, "ล็อกอิน Cloudflare");
  const who = runCapture("npx", ["wrangler", "whoami"]);
  if (who.ok && /You are logged in/i.test(who.out)) {
    note("ล็อกอินอยู่แล้ว ข้ามขั้นตอนนี้");
  } else {
    note("เบราว์เซอร์จะเปิดขึ้นมา กด Allow แล้วกลับมาที่หน้าต่างนี้");
    if (!runVisible("npx", ["wrangler", "login"])) {
      console.log(c.err("      ล็อกอินไม่สำเร็จ"));
      process.exit(1);
    }
  }

  // 3 ────────────────────────────────────────────────────────────
  step(3, TOTAL, "ใส่ Gemini API key");
  note("สร้างคีย์ได้ที่ https://aistudio.google.com/apikey");
  note("เดี๋ยวจะมีช่องให้วางคีย์ ตัวอักษรจะไม่ขึ้นบนจอ วางแล้วกด Enter ได้เลย");
  const wantKey = await ask(rl, "ตั้งค่าคีย์ตอนนี้เลยไหม [Y/n]", "y");
  if (/^y/i.test(wantKey)) {
    if (!runVisible("npx", ["wrangler", "secret", "put", "GEMINI_API_KEY"])) {
      console.log(c.warn("      ตั้งคีย์ไม่สำเร็จ ตั้งภายหลังได้ด้วย npx wrangler secret put GEMINI_API_KEY"));
    }
  } else {
    note("ข้ามไว้ก่อน — ต้องกลับมาตั้งก่อนใช้งานจริง");
  }

  // 4 ────────────────────────────────────────────────────────────
  step(4, TOTAL, "เปิดโควตารายวัน (KV)");
  let toml = readFileSync(wranglerToml, "utf8");
  if (/^\[\[kv_namespaces\]\]/m.test(toml)) {
    note("ตั้งค่าไว้แล้ว ข้ามขั้นตอนนี้");
  } else {
    const r = runCapture("npx", ["wrangler", "kv", "namespace", "create", "CHAT_KV"]);
    const id = (r.out.match(/\b[0-9a-f]{32}\b/) || [])[0];
    if (id) {
      toml = toml.replace(
        /# \[\[kv_namespaces\]\]\n# binding = "CHAT_KV"\n# id = "[^"]*"/,
        `[[kv_namespaces]]\nbinding = "CHAT_KV"\nid = "${id}"`
      );
      writeFileSync(wranglerToml, toml);
      console.log(`      ${c.ok("✓")} ผูก KV id ${id} ลงใน wrangler.toml แล้ว`);
    } else {
      console.log(c.warn("      หา id ของ KV ไม่เจอจากผลลัพธ์ข้างบน"));
      const manual = await ask(rl, "ถ้าเห็น id เป็นตัวอักษรยาว ๆ ให้วางตรงนี้ (หรือ Enter เพื่อข้าม):");
      if (manual) {
        toml = toml.replace(
          /# \[\[kv_namespaces\]\]\n# binding = "CHAT_KV"\n# id = "[^"]*"/,
          `[[kv_namespaces]]\nbinding = "CHAT_KV"\nid = "${manual}"`
        );
        writeFileSync(wranglerToml, toml);
        console.log(`      ${c.ok("✓")} ผูก KV แล้ว`);
      } else {
        console.log(c.warn("      ข้ามไป — จะไม่มีการจำกัดจำนวนคำถามต่อวัน"));
      }
    }
  }

  // 5 ────────────────────────────────────────────────────────────
  step(5, TOTAL, "ตรวจโดเมนที่อนุญาต");
  const current = (readFileSync(wranglerToml, "utf8").match(/ALLOWED_ORIGINS = "([^"]*)"/) || [])[1] || "";
  note(`ตอนนี้ตั้งไว้ที่ ${current || "(ว่าง)"}`);
  const newOrigin = await ask(rl, "ถ้าเว็บจริงอยู่โดเมนอื่น พิมพ์โดเมนนั้น (หรือ Enter เพื่อใช้ค่าเดิม):");
  if (newOrigin) {
    writeFileSync(wranglerToml, readFileSync(wranglerToml, "utf8")
      .replace(/ALLOWED_ORIGINS = "[^"]*"/, `ALLOWED_ORIGINS = "${newOrigin}"`));
    console.log(`      ${c.ok("✓")} ตั้งเป็น ${newOrigin}`);
  }

  // 6 ────────────────────────────────────────────────────────────
  step(6, TOTAL, "Deploy ขึ้น Cloudflare");
  note("ถ้าถามว่าจะจด subdomain workers.dev ไหม ให้ตอบ yes");
  // ต้องปล่อยให้โต้ตอบได้จริง ถ้าดักอ่านผลลัพธ์ wrangler จะคิดว่าไม่มีคนอยู่
  // แล้วตอบคำถามเรื่อง subdomain ให้เป็น no เอง ทำให้ deploy ไม่ผ่าน
  const deployed = runVisible("npx", ["wrangler", "deploy"]);
  let url = "";
  if (!deployed) {
    console.log(c.warn("\n      deploy ไม่ผ่าน"));
    console.log(c.dim("      สาเหตุที่พบบ่อยที่สุดคือบัญชียังไม่เคยจด subdomain ของ workers.dev"));
    console.log(c.dim("      ถ้าเห็นลิงก์ dash.cloudflare.com ในข้อความข้างบน ให้เปิดลิงก์นั้น"));
    console.log(c.dim("      ตั้งชื่อ subdomain (ตั้งอะไรก็ได้ที่ยังว่าง) แล้วกลับมารันสคริปต์นี้ใหม่"));
  } else {
    note("มองหาบรรทัดที่ลงท้ายด้วย .workers.dev ในข้อความข้างบน");
  }
  url = await ask(rl, "วาง URL ที่ได้ตรงนี้ (หรือ Enter เพื่อข้าม):");

  // 7 ────────────────────────────────────────────────────────────
  step(7, TOTAL, "ใส่ URL ลงในหน้าเว็บทุกวิชา");
  if (url) {
    const endpoint = `${url.replace(/\/$/, "")}/chat`;
    const n = setEndpoint(endpoint);
    console.log(`      ${c.ok("✓")} ใส่ให้ ${n} หน้าแล้ว`);
    console.log(c.b("\nเสร็จแล้ว 🎉"));
    console.log(`   ผู้ช่วยอยู่ที่ ${c.b(endpoint)}`);
    console.log("\n   เหลืออีกขั้นเดียว คือ push ขึ้น GitHub ให้เว็บจริงได้ใช้");
    console.log(c.dim("     git add -A"));
    console.log(c.dim('     git commit -m "เปิดใช้ผู้ช่วยตอบคำถาม"'));
    console.log(c.dim("     git push"));
    console.log(c.dim("\n   อยากปิดปุ่มแชทชั่วคราว: node setup.mjs unlink"));
  } else {
    console.log(c.warn("      ยังไม่ได้ใส่ URL"));
    console.log(c.dim("      deploy สำเร็จเมื่อไรแล้วรัน: node setup.mjs link <url ที่ได้>"));
  }
} finally {
  rl.close();
}
