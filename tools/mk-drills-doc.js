// สร้างไฟล์ Word ใบงาน แบบฝึกตามรูปแบบข้อสอบจริง
//
//   python3 tools/mk-drills.py --json /tmp/d.json   ดึงข้อมูลออกมาเป็น JSON
//   node tools/mk-drills-doc.js /tmp/d.json oral-drills.docx
//
// ใช้ข้อมูลชุดเดียวกับหน้าเว็บ คือ tools/oral-drills-data.py
// เนื้อหาสองที่จึงตรงกันเสมอ แก้ที่ไฟล์ข้อมูลแล้วสั่งใหม่ทั้งสองทาง

// สร้างไฟล์ Word ใบงาน แบบฝึกตามรูปแบบข้อสอบจริง
const fs = require('fs');
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
  Table, TableRow, TableCell, WidthType, ShadingType, BorderStyle,
  PageBreak, LevelFormat, Footer, PageNumber,
} = require('docx');

const DATA = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const OUT = process.argv[3];

const FONT = 'TH Sarabun New';
const W = 9026;
const PLUM = '6B3560';
const INK = '1E1917';
const GREY = '7A6E6A';
const RULE = 'DCD2CE';
const BOXF = 'F7F1F5';   // พื้นคลังคำ
const LABF = 'EDE7E4';   // พื้นช่องป้ายกำกับ
const KEYF = 'F6F2EC';   // พื้นเฉลย

const t = (s, o = {}) => new TextRun({ text: s, font: FONT, ...o });
const h1 = (s) => new Paragraph({ heading: HeadingLevel.HEADING_1, children: [t(s)] });
const h2 = (s) => new Paragraph({ heading: HeadingLevel.HEADING_2, children: [t(s)] });

function p(text, o = {}) {
  return new Paragraph({
    alignment: o.align,
    spacing: o.spacing || { after: 100, line: 300 },
    indent: o.indent,
    children: [t(text, { size: o.size || 30, bold: o.bold, color: o.color || INK })],
  });
}

// แปลง [[n]] เป็นเส้นให้เขียนลงไป ความยาวเส้นขึ้นกับว่าเป็นคำเดี่ยวหรือวลี
//
// ใช้ขีดล่างจริง ไม่ใช้ช่องว่างที่ขีดเส้นใต้
// เพราะช่องว่างที่ไปตกท้ายบรรทัดจะถูกตัดทิ้งตอนจัดบรรทัด แล้วเส้นหายไปทั้งเส้น
// ซึ่งเจอมาแล้วตอนตรวจ คือบางช่องมีเส้น บางช่องไม่มี ทั้งที่เขียนเหมือนกัน
function gapRuns(text, long) {
  const out = [];
  const line = long ? '_'.repeat(30) : '_'.repeat(12);
  const re = /\[\[(\d+)\]\]/g;
  let last = 0, m;
  while ((m = re.exec(text)) !== null) {
    if (m.index > last) out.push(t(text.slice(last, m.index), { size: 30 }));
    out.push(t(`(${m[1]}) `, { size: 26, color: PLUM, bold: true }));
    out.push(t(line, { size: 30, color: GREY }));
    last = m.index + m[0].length;
  }
  if (last < text.length) out.push(t(text.slice(last), { size: 30 }));
  return out;
}

function cell(children, o = {}) {
  return new TableCell({
    width: { size: o.w, type: WidthType.DXA },
    shading: o.fill ? { type: ShadingType.CLEAR, fill: o.fill } : undefined,
    margins: { top: 90, bottom: 90, left: 120, right: 120 },
    children,
  });
}

const noBorder = { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' };
const thin = { style: BorderStyle.SINGLE, size: 4, color: RULE };

// คลังคำ · ตารางสองหรือสามคอลัมน์ตามความยาวของรายการ
function wordBox(box) {
  const long = box.some(w => w.length > 18);
  const cols = long ? 2 : 4;
  const cw = Math.floor(W / cols);
  const rows = [];
  for (let i = 0; i < box.length; i += cols) {
    const cs = [];
    for (let j = 0; j < cols; j++) {
      const w = box[i + j];
      cs.push(cell([new Paragraph({
        spacing: { after: 0, line: 280 },
        children: [t(w === undefined ? '' : w, { size: 29 })],
      })], { w: cw, fill: BOXF }));
    }
    rows.push(new TableRow({ children: cs }));
  }
  return new Table({
    columnWidths: new Array(cols).fill(cw),
    width: { size: cw * cols, type: WidthType.DXA },
    borders: {
      top: { style: BorderStyle.DASHED, size: 6, color: PLUM },
      bottom: { style: BorderStyle.DASHED, size: 6, color: PLUM },
      left: { style: BorderStyle.DASHED, size: 6, color: PLUM },
      right: { style: BorderStyle.DASHED, size: 6, color: PLUM },
      insideHorizontal: noBorder, insideVertical: noBorder,
    },
    rows,
  });
}

// บล็อกที่มีป้ายกำกับ ใช้กับ SAR+L และ Three S's · เลียนแบบตารางในใบงานจริง
function framedBlocks(blocks) {
  const lw = 1900, bw = W - lw;
  return new Table({
    columnWidths: [lw, bw],
    width: { size: W, type: WidthType.DXA },
    borders: { top: thin, bottom: thin, left: thin, right: thin,
      insideHorizontal: thin, insideVertical: thin },
    rows: blocks.map(b => new TableRow({
      // แต่ละช่องของโครงต้องไม่ถูกตัดครึ่งข้ามหน้า ไม่งั้นเส้นให้เขียนจะไปอยู่คนละหน้ากับโจทย์
      cantSplit: true,
      children: [
        cell([new Paragraph({ spacing: { after: 0, line: 280 },
          children: [t(b.label, { size: 28, bold: true, color: PLUM })] })],
          { w: lw, fill: LABF }),
        cell([new Paragraph({ spacing: { after: 0, line: 360 },
          children: gapRuns(b.t, true) })], { w: bw }),
      ],
    })),
  });
}

const body = [];

// ───── หน้าปก ─────
body.push(new Paragraph({ spacing: { before: 1800 }, alignment: AlignmentType.CENTER,
  children: [t('ใบงานประกอบการทบทวน', { size: 28, color: PLUM, bold: true })] }));
body.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 160 },
  children: [t('แบบฝึกตามรูปแบบข้อสอบจริง', { size: 60, bold: true })] }));
body.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 120 },
  children: [t("เติมคำจากกล่อง · โครง SAR+L · โครง Three S's", { size: 32, color: GREY })] }));
body.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 600 },
  children: [t('วิชาภาษาอังกฤษเพื่อการสื่อสาร · 5500313 Business English Oral Communication',
    { size: 27, color: GREY })] }));
body.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 40 },
  children: [t('คณะพาณิชยศาสตร์และการบัญชี จุฬาลงกรณ์มหาวิทยาลัย', { size: 27, color: GREY })] }));
body.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 500 },
  children: [t(`แบบฝึก ${DATA.drills.length} ชุด · ช่องว่างรวม ` +
    `${DATA.drills.reduce((a, d) => a + d.box.length, 0)} ช่อง · เฉลยอยู่ท้ายเล่ม`,
    { size: 27, color: GREY })] }));
body.push(new Paragraph({ children: [new PageBreak()] }));

// ───── คำชี้แจง ─────
body.push(h1('คำชี้แจง'));
body.push(p('ทุกชุดในใบงานนี้มีจำนวนรายการในคลังคำเท่ากับจำนวนช่องว่างพอดี ' +
  'จึงต้องใช้ครบทุกรายการ รายการละหนึ่งครั้ง'));
body.push(p('ส่วนที่เป็นโครงคำตอบ ให้ดูตำแหน่งของช่องว่างก่อนดูตัวเลือก ' +
  'เพราะแต่ละส่วนของโครงมีหน้าที่ของตัวเอง'));
body.push(new Table({
  columnWidths: [2400, 6626],
  width: { size: W, type: WidthType.DXA },
  borders: { top: thin, bottom: thin, left: thin, right: thin,
    insideHorizontal: thin, insideVertical: thin },
  rows: [
    ['Situation (S)', 'สถานการณ์ · เกิดที่ไหน เมื่อไร และเราอยู่ตรงไหนของเรื่อง'],
    ['Action (A)', 'สิ่งที่เราลงมือทำ · ควรมีมากกว่าหนึ่งอย่าง และเป็นการกระทำของเราเอง'],
    ['Result (R)', 'ผลที่เกิด · ถ้ามีตัวเลขหรือสิ่งที่คนอื่นพูดถึงจะหนักแน่นกว่า'],
    ['Lesson (L)', 'บทเรียน · ปิดด้วยการบอกว่าจะนำไปใช้กับงานที่สมัครอย่างไร'],
    ['SUCCESS', 'ผลงานที่ผ่านมา · เรียนอะไร ฝึกงานที่ไหน ทำอะไรได้สำเร็จ'],
    ['STRENGTH', 'จุดแข็ง · ควรมีหลักฐานรองรับ ไม่ใช่บอกลอย ๆ ว่าตัวเองเป็นคนแบบไหน'],
    ['SITUATION', 'โยงกลับมาที่ตำแหน่งที่สมัคร · บอกว่าสิ่งที่มีจะช่วยองค์กรได้อย่างไร'],
  ].map(r => new TableRow({
    children: [
      cell([new Paragraph({ spacing: { after: 0, line: 280 },
        children: [t(r[0], { size: 28, bold: true, color: PLUM })] })], { w: 2400, fill: LABF }),
      cell([new Paragraph({ spacing: { after: 0, line: 280 },
        children: [t(r[1], { size: 28 })] })], { w: 6626 }),
    ],
  })),
}));
body.push(new Paragraph({ children: [new PageBreak()] }));

// ───── ใบงาน ─────
DATA.groups.forEach((g, gi) => {
  if (gi) body.push(new Paragraph({ children: [new PageBreak()] }));
  body.push(h1(g.title));
  body.push(p(g.desc, { color: GREY, size: 28 }));
  const items = DATA.drills.filter(d => d.group === g.id);
  const framed = (g.id === 'sarl' || g.id === 'three');

  items.forEach((d, di) => {
    if (di) body.push(new Paragraph({ spacing: { before: 240 }, children: [t('')] }));
    body.push(h2(d.title));
    body.push(wordBox(d.box));
    body.push(new Paragraph({ spacing: { after: 60 }, children: [t('')] }));
    if (framed) {
      body.push(framedBlocks(d.blocks));
    } else {
      d.blocks.forEach(b => {
        const runs = [];
        if (b.label) runs.push(t(b.label + '.  ', { size: 30, bold: true, color: PLUM }));
        gapRuns(b.t, false).forEach(r => runs.push(r));
        body.push(new Paragraph({
          spacing: { after: 110, line: 400 },
          indent: { left: 360, hanging: 360 },
          children: runs,
        }));
      });
    }
  });
});

// ───── เฉลย ─────
body.push(new Paragraph({ children: [new PageBreak()] }));
body.push(h1('เฉลยพร้อมคำอธิบาย'));
body.push(p('ตัวเลขในวงเล็บคือหมายเลขช่องว่าง', { color: GREY, size: 28 }));

DATA.groups.forEach(g => {
  body.push(h2(g.title));
  DATA.drills.filter(d => d.group === g.id).forEach(d => {
    body.push(new Paragraph({
      spacing: { before: 170, after: 70 },
      children: [t(d.title, { size: 29, bold: true })],
    }));
    for (let i = 1; i <= d.box.length; i++) {
      const exp = String(d.exp[String(i)] || '').replace(/<[^>]+>/g, '');
      body.push(new Paragraph({
        shading: { type: ShadingType.CLEAR, fill: KEYF },
        spacing: { after: 0, line: 290 },
        indent: { left: 200, right: 160, hanging: 0 },
        children: [
          t(`(${i})  `, { size: 27, color: PLUM, bold: true }),
          t(d.ans[String(i)], { size: 28, bold: true }),
          t('   ' + exp, { size: 27, color: '4A4240' }),
        ],
      }));
    }
  });
});

body.push(new Paragraph({ spacing: { before: 300 }, children: [t('')] }));
body.push(new Paragraph({
  shading: { type: ShadingType.CLEAR, fill: KEYF },
  border: { left: { style: BorderStyle.SINGLE, size: 18, color: PLUM, space: 8 } },
  spacing: { before: 120, after: 150, line: 300 },
  indent: { left: 170, right: 140 },
  children: [t('ทุกกิจการ ทุกชื่อบุคคล และทุกตัวเลขในใบงานนี้สมมุติขึ้นเพื่อใช้ฝึก ' +
    'ไม่ได้อ้างอิงกิจการหรือบุคคลใด · แบบฝึกชุดนี้เรียบเรียงขึ้นใหม่ ไม่ใช่ข้อสอบเก่า',
    { size: 27 })] }));

// ───── ประกอบเอกสาร ─────
const doc = new Document({
  creator: 'แบบฝึกวิชาภาษาอังกฤษเพื่อการสื่อสาร',
  title: 'แบบฝึกตามรูปแบบข้อสอบจริง',
  description: "เติมคำจากกล่อง · โครง SAR+L · โครง Three S's พร้อมเฉลยภาษาไทยทุกช่อง",
  styles: {
    default: {
      document: { run: { font: FONT, size: 30, color: INK } },
      heading1: { run: { font: FONT, size: 40, bold: true, color: PLUM },
        paragraph: { spacing: { before: 280, after: 140 }, keepNext: true,
          border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: RULE, space: 6 } } } },
      heading2: { run: { font: FONT, size: 32, bold: true, color: INK },
        paragraph: { spacing: { before: 240, after: 110 }, keepNext: true } },
    },
  },
  numbering: { config: [{ reference: 'bul', levels: [{ level: 0, format: LevelFormat.BULLET,
    text: '•', alignment: AlignmentType.LEFT,
    style: { paragraph: { indent: { left: 420, hanging: 220 } } } }] }] },
  sections: [{
    properties: { page: { margin: { top: 1440, bottom: 1440, left: 1440, right: 1440 } } },
    footers: {
      default: new Footer({ children: [new Paragraph({
        alignment: AlignmentType.CENTER,
        children: [new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: 22, color: GREY })],
      })] }),
    },
    children: body,
  }],
});

Packer.toBuffer(doc).then(b => { fs.writeFileSync(OUT, b); console.log('wrote', OUT, b.length, 'bytes'); });
