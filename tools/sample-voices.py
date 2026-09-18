#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""สร้างคลิปตัวอย่างสั้น ๆ หลายแบบ เพื่อให้เลือกว่าจะใช้เสียงอังกฤษตัวไหน

ปัญหาคือเสียงไทยล้วนอ่านคำอังกฤษด้วยระบบเสียงไทย ศัพท์เฉพาะจึงฟังไม่ออก
สคริปต์นี้หยิบย่อหน้าจริงจากบทบรรยายที่มีไทยปนอังกฤษเยอะ ๆ มาอ่านด้วยหลายแบบ
แล้วทำหน้าเว็บให้กดฟังเทียบกันได้ทีละแบบ

    python3 tools/sample-voices.py

ได้ไฟล์ใน samples/ พร้อมหน้า samples/index.html สำหรับเปิดฟัง
"""
import asyncio
import importlib.util
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from langsplit import split_lang                                   # noqa: E402

# make-audio.py มีขีดกลางในชื่อ จึง import ด้วยวิธีปกติไม่ได้ ต้องโหลดจากพาธตรง ๆ
_spec = importlib.util.spec_from_file_location('make_audio', os.path.join(HERE, 'make-audio.py'))
_ma = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_ma)
build_chapter = _ma.build_chapter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'samples')

TH_VOICE = 'th-TH-NiwatNeural'

# แบบที่จะเอามาเทียบกัน · ชื่อที่แสดง กับเสียงอังกฤษที่ใช้ ถ้าว่างคือใช้เสียงไทยอ่านหมด
CANDIDATES = [
    (u'แบบเดิม · เสียงไทยอ่านทั้งหมด', ''),
    (u'อังกฤษแบบอเมริกัน · Andrew',   'en-US-AndrewNeural'),
    (u'อังกฤษแบบอเมริกัน · Guy',      'en-US-GuyNeural'),
    (u'อังกฤษแบบบริติช · Ryan',       'en-GB-RyanNeural'),
]

# ย่อหน้าที่หยิบมาโชว์ เลือกจากบทที่มีศัพท์อังกฤษหนาแน่นต่างกันสามระดับ
PICKS = [
    ('oral-eng',    'np', 0),
    ('oral-eng',    'pr', 2),
    ('adv-acctg-1', 'ch2', 0),
    ('audit',       'ch1', 0),
]


def lines_of(course, chapter_key, section_idx, take=3):
    path = os.path.join(ROOT, course, 'index.html')
    html = io.open(path, encoding='utf-8').read()
    data = json.loads(re.search(r'id="cn-data">(.*?)</script>', html, re.S).group(1))
    sec = data[chapter_key]['c'][section_idx]
    return data[chapter_key]['s'], sec['h'], sec['t'][:take]


async def main():
    os.makedirs(OUT, exist_ok=True)

    picks = []
    for course, key, idx in PICKS:
        try:
            label, head, lines = lines_of(course, key, idx)
            picks.append((course, label, head, lines))
        except Exception as exc:
            print(u'ข้าม %s/%s เพราะ %s' % (course, key, exc))

    all_lines = [ln for _, _, _, lines in picks for ln in lines]
    print(u'ตัวอย่างที่ใช้ %d ย่อหน้า จาก %d บท' % (len(all_lines), len(picks)))
    for _, label, head, lines in picks:
        print(u'  %s · %s · %d ย่อหน้า' % (label, head, len(lines)))

    made = []
    for title, en_voice in CANDIDATES:
        name = (en_voice or 'thai-only').replace('-', '_') + '.mp3'
        path = os.path.join(OUT, name)
        print(u'\nกำลังสร้าง %s' % title)
        audio, cues, dur = await build_chapter(
            all_lines, TH_VOICE, '', '', title, en_voice or None)
        with open(path, 'wb') as f:
            f.write(audio)
        print(u'  เขียน samples/%s · %.2f MB · %d:%02d'
              % (name, len(audio) / 1048576.0, int(dur // 60), int(dur % 60)))
        made.append((title, name, en_voice, dur, cues))

    write_page(picks, all_lines, made)
    print(u'\nเสร็จแล้ว เปิดไฟล์ samples/index.html เพื่อฟังเทียบกัน')
    return 0


def esc(s):
    return (s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))


def write_page(picks, all_lines, made):
    rows = []
    for title, name, en_voice, dur, cues in made:
        rows.append(
            u'<div class="v"><div class="vh"><b>%s</b><span>%s · %d:%02d</span></div>'
            u'<audio controls preload="none" src="%s"></audio>'
            u'<div class="cue">%s</div></div>'
            % (esc(title), esc(en_voice or u'ไม่ใช้เสียงอังกฤษ'),
               int(dur // 60), int(dur % 60), name,
               u' · '.join('%d:%02d' % (int(c // 60), int(c % 60)) for c in cues[:len(all_lines)])))

    script = []
    for _, label, head, lines in picks:
        script.append(u'<h3>%s · %s</h3>' % (esc(label), esc(head)))
        for ln in lines:
            marked = u''.join(
                (u'<em>%s</em>' % esc(s)) if lang == 'en' else esc(s)
                for lang, s in split_lang(ln))
            script.append(u'<p>%s</p>' % marked)

    # ใช้ตัวแทนที่ชื่อชัดเจนแทนการแทนค่าด้วย %s เพราะ CSS มีเครื่องหมาย % อยู่หลายที่
    page = PAGE_TMPL.replace('@@PLAYERS@@', u'\n'.join(rows)) \
                    .replace('@@SCRIPT@@', u'\n'.join(script))
    io.open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8').write(page)


PAGE_TMPL = u"""<meta charset="utf-8">
<title>เทียบเสียงอ่านภาษาอังกฤษ</title>
<style>
:root{--paper:#fbfcfa;--ink:#16211c;--ink2:#41514a;--ink3:#6c7d75;--rule:#cfdbd0;--surface:#f2f5f1;--accent:#1f6b4f}
@media (prefers-color-scheme:dark){:root{--paper:#101613;--ink:#e5ece5;--ink2:#adbcb2;--ink3:#82938a;--rule:#2b3630;--surface:#161d19;--accent:#5cc397}}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);font-family:"IBM Plex Sans Thai",system-ui,sans-serif;line-height:1.7}
.shell{max-width:760px;margin:0 auto;padding:40px 20px 80px}
h1{font-size:1.5rem;margin:0 0 6px}
.lede{color:var(--ink2);margin:0 0 28px}
.v{border:1px solid var(--rule);border-radius:6px;background:var(--surface);padding:14px 16px;margin-bottom:14px}
.vh{display:flex;justify-content:space-between;align-items:baseline;gap:12px;margin-bottom:9px;flex-wrap:wrap}
.vh span{font-family:ui-monospace,monospace;font-size:.76rem;color:var(--ink3)}
audio{width:100%}
.cue{font-family:ui-monospace,monospace;font-size:.68rem;color:var(--ink3);margin-top:7px;word-break:break-all}
h2{font-size:1.05rem;margin:34px 0 10px;padding-top:22px;border-top:1px solid var(--rule)}
h3{font-size:.86rem;color:var(--accent);margin:18px 0 4px;font-family:ui-monospace,monospace;letter-spacing:.04em}
p{margin:0 0 9px;color:var(--ink2)}
em{font-style:normal;background:rgba(31,107,79,.13);color:var(--ink);padding:1px 3px;border-radius:3px;font-weight:600}
.note{border-left:3px solid var(--accent);background:rgba(31,107,79,.08);padding:11px 15px;border-radius:0 4px 4px 0;font-size:.9rem;margin-bottom:26px}
</style>
<div class="shell">
<h1>เทียบเสียงอ่านภาษาอังกฤษ</h1>
<p class="lede">ทุกคลิปใช้ข้อความชุดเดียวกันหมด ต่างกันแค่ว่าช่วงภาษาอังกฤษอ่านด้วยเสียงอะไร</p>
<div class="note">ฟังให้ครบทุกคลิปแล้วบอกได้เลยว่าชอบแบบไหน เดี๋ยวจะสร้างใหม่ทั้ง 25 บทด้วยแบบนั้น<br>
ส่วนที่<em>ไฮไลต์</em>ในบทด้านล่างคือช่วงที่ถูกแยกออกไปอ่านด้วยเสียงอังกฤษ</div>
@@PLAYERS@@
<h2>บทที่ใช้เป็นตัวอย่าง</h2>
@@SCRIPT@@
</div>
"""


if __name__ == '__main__':
    sys.exit(asyncio.run(main()))
