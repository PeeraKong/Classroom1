#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""สร้างไฟล์เสียงสำหรับ Part III · Listening ของวิชาภาษาอังกฤษ

ต่างจาก tools/make-audio.py ตรงที่บทเป็นภาษาอังกฤษล้วน และ
การนำเสนอกลุ่มมีผู้พูดหลายคน จึงต้องใช้เสียงคนละตัวสลับกันไปตามผู้พูด

    pip3 install edge-tts
    python3 tools/make-listening.py

ได้ไฟล์ oral-eng/listening/<รหัส>.mp3 พร้อมเขียนดัชนีกลับเข้า index.html
"""

import argparse
import asyncio
import hashlib
import importlib.util
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
COURSE = 'oral-eng'

_spec = importlib.util.spec_from_file_location('make_audio', os.path.join(HERE, 'make-audio.py'))
_ma = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_ma)
synth, mp3_duration = _ma.synth, _ma.mp3_duration

_lspec = importlib.util.spec_from_file_location('ldata', os.path.join(HERE, 'listening-data.py'))
_ld = importlib.util.module_from_spec(_lspec)
_lspec.loader.exec_module(_ld)
SETS, VOICES = _ld.SETS, _ld.VOICES

INDEX_RE = re.compile(r'\n*<script type="application/json" id="ls-audio">.*?</script>', re.S)

# เว้นจังหวะระหว่างผู้พูด ให้ฟังเหมือนการนำเสนอจริงที่มีการสลับคน
#
# เดิมใช้วิธีสังเคราะห์จุดไข่ปลา แต่บริการตอบกลับว่า NoAudioReceived
# เพราะข้อความที่มีแต่เครื่องหมายวรรคตอนไม่มีอะไรให้อ่านออกเสียง
# จึงเปลี่ยนมาประกอบเฟรม MP3 เงียบขึ้นเองแทน ซึ่งไม่ต้องเรียกบริการเลย
#
# เฟรมของบริการนี้คือ MPEG-2 Layer III 24 kHz โมโน 48 kbps
#   FF        ซิงก์
#   F3        ซิงก์ต่อ · เวอร์ชัน MPEG2 · เลเยอร์ III · ไม่มี CRC
#   64        บิตเรต 48 kbps · อัตราสุ่ม 24 kHz · ไม่มีไบต์เสริม
#   C0        โมโน
# ส่วนข้อมูลเสียงเป็นศูนย์ทั้งหมด ตัวถอดรหัสจึงได้ความเงียบ
SILENT_FRAME = bytes([0xFF, 0xF3, 0x64, 0xC0]) + b'\x00' * 140
FRAME_SECONDS = 576 / 24000.0
PAUSE_SECONDS = 0.7


def silence(seconds):
    return SILENT_FRAME * max(1, int(round(seconds / FRAME_SECONDS)))


async def build_part(part):
    """สังเคราะห์ทีละช่วงพูด แล้วต่อกัน คืนเสียง จุดเริ่มของแต่ละช่วง และความยาวรวม"""
    parts, cues, at = [], [], 0.0
    prev_speaker = None
    for i, (name, _key, vkey, text) in enumerate(part['turns']):
        voice = VOICES.get(vkey, vkey)

        # เปลี่ยนคนพูดเมื่อไร ให้เว้นจังหวะก่อน
        if prev_speaker is not None and name != prev_speaker:
            gap = silence(PAUSE_SECONDS)
            at += mp3_duration(gap)
            parts.append(gap)
        prev_speaker = name

        for attempt in range(3):
            try:
                data = await synth(text, voice, '', '')
                break
            except Exception as exc:
                if attempt == 2:
                    raise RuntimeError(
                        u'เรียกบริการอ่านออกเสียงไม่สำเร็จ · %s\n  ข้อความจากระบบ %s'
                        % (part['id'], exc))
                await asyncio.sleep(1.5 * (attempt + 1))

        cues.append(round(at, 3))
        at += mp3_duration(data)
        parts.append(data)
        sys.stdout.write('\r  %s  %d/%d ช่วง · %d:%02d'
                         % (part['id'], i + 1, len(part['turns']), int(at // 60), int(at % 60)))
        sys.stdout.flush()
    sys.stdout.write('\n')
    return b''.join(parts), cues, round(at, 3)


def sig_of(part):
    """ลายเซ็นของคลิป รวมทั้งบทและเสียงที่ใช้ เปลี่ยนอย่างใดอย่างหนึ่งก็สร้างใหม่"""
    key = '\n'.join('%s|%s|%s' % (t[0], VOICES.get(t[2], t[2]), t[3]) for t in part['turns'])
    return hashlib.sha1(key.encode('utf-8')).hexdigest()[:12]


def read_page():
    path = os.path.join(ROOT, COURSE, 'index.html')
    return path, io.open(path, encoding='utf-8').read()


def write_index(clips):
    path, html = read_page()
    block = ('\n\n<script type="application/json" id="ls-audio">\n' +
             json.dumps(clips, ensure_ascii=False, separators=(',', ':')) + '\n</script>')
    html = INDEX_RE.sub('', html).rstrip('\n')
    anchor = '\n<script type="application/json" id="vc-data">'
    at = html.find(anchor)
    html = (html[:at] + block + html[at:]) if at > 0 else (html + block + '\n')
    io.open(path, 'w', encoding='utf-8').write(html.rstrip('\n') + '\n')
    print(u'  ปรับ %s/index.html ให้ชี้ไปยังไฟล์เสียงแล้ว' % COURSE)


# ข้อสอบฟังไม่ควรวัดว่าเคยอ่านข่าวดีลนั้นมาก่อนไหม ทุกกิจการจึงต้องสมมติขึ้นใหม่
REAL_CO = re.compile(r'Kraft|Cadbury|Disney|Pixar|Nestl|Toyota|Panasonic|Vodafone|Unilever|Tesco')


def audit_scripts():
    """ตรวจบทและคำถามก่อนเสียเวลาสังเคราะห์เสียง เพราะรอบหนึ่งใช้เวลาหลายนาที"""
    bad = 0

    def fail(pid, msg):
        nonlocal bad
        bad += 1
        print(u'  %-4s %s' % (pid, msg))

    for st in SETS:
        for part in st['parts']:
            pid = part['id']
            speakers = set(t[0] for t in part['turns'])
            if part['kind'] == 'presentation' and len(speakers) < 2:
                fail(pid, u'เป็นการนำเสนอกลุ่ม แต่มีคนพูดคนเดียว')
            if part['kind'] == 'talk' and len(speakers) != 1:
                fail(pid, u'เป็นการบรรยายเดี่ยว แต่มีผู้พูด %d คน' % len(speakers))

            script = re.sub(r'\s+', ' ', ' '.join(t[3] for t in part['turns'])).replace(u'’', "'")
            for t in part['turns']:
                if t[2] not in VOICES:
                    fail(pid, u'อ้างเสียง %s ซึ่งไม่มีในรายการ' % t[2])
                m = REAL_CO.search(t[3])
                if m:
                    fail(pid, u'บทมีชื่อกิจการจริง %s' % m.group(0))

            if len(part['questions']) != 10:
                fail(pid, u'มีคำถาม %d ข้อ ต้องเป็น 10' % len(part['questions']))
            for q in part['questions']:
                if len(q['o']) != 4 or len(set(q['o'])) != 4:
                    fail(pid, u'ตัวเลือกไม่ครบสี่หรือซ้ำกัน · %s' % q['q'][:40])
                if not (0 <= q['a'] < len(q['o'])):
                    fail(pid, u'ดัชนีคำตอบอยู่นอกช่วง · %s' % q['q'][:40])
                if not q.get('e', '').strip():
                    fail(pid, u'ไม่มีคำอธิบาย · %s' % q['q'][:40])
                # คำอธิบายที่ยกข้อความจากบทมาอ้าง ต้องอ้างได้จริง
                for quote in re.findall(r'"([^"]+)"', q.get('e', '')):
                    quote = quote.replace(u'’', "'").strip()
                    for piece in [x.strip() for x in quote.split(u'…') if len(x.strip()) > 12]:
                        if piece not in script:
                            fail(pid, u'คำอธิบายอ้างข้อความที่ไม่มีในบท · %s' % piece[:50])
    return bad


def check():
    print(u'\nPython ที่ใช้อยู่   %s' % sys.executable)
    try:
        import edge_tts
        print(u'edge-tts           ติดตั้งแล้ว รุ่น %s'
              % getattr(edge_tts, '__version__', u'ไม่ทราบเวอร์ชัน'))
    except ImportError:
        print(u'edge-tts           ยังไม่ได้ติดตั้ง')

    _, html = read_page()
    old = {}
    m = INDEX_RE.search(html)
    if m:
        try:
            old = json.loads(re.search(r'>(.*?)</script>', m.group(0), re.S).group(1))
        except Exception:
            old = {}

    print(u'\nตรวจบทและคำถาม')
    problems = audit_scripts()
    print(u'  พบปัญหา %d จุด' % problems)

    todo = words = 0
    print('')
    for st in SETS:
        print(u'%s' % st['title'])
        for part in st['parts']:
            mp3 = os.path.join(ROOT, COURSE, 'listening', part['id'] + '.mp3')
            prev = old.get(part['id'])
            w = sum(len(t[3].split()) for t in part['turns'])
            if prev and prev.get('sig') == sig_of(part) and os.path.exists(mp3):
                print(u'  %-5s %-40s มีไฟล์แล้ว · %d:%02d'
                      % (part['id'], part['title'], int(prev['dur'] // 60), int(prev['dur'] % 60)))
            else:
                print(u'  %-5s %-40s ยังไม่มีไฟล์ · %d คำ' % (part['id'], part['title'], w))
                todo += 1
                words += w
    if todo:
        print(u'\nต้องสร้าง %d คลิป รวม %d คำ ใช้เวลาราว %d นาที'
              % (todo, words, max(1, round(words / 900.0))))
    else:
        print(u'\nพร้อมแล้ว ทุกคลิปมีไฟล์เสียงครบ')
    return 0


async def main():
    ap = argparse.ArgumentParser(description=u'สร้างไฟล์เสียงสำหรับแบบฝึกฟัง')
    ap.add_argument('--force', action='store_true', help=u'สร้างใหม่แม้บทไม่เปลี่ยน')
    ap.add_argument('--check', action='store_true', help=u'ดูสถานะอย่างเดียว ไม่สร้างจริง')
    a = ap.parse_args()

    if a.check:
        return check()

    try:
        import edge_tts                                            # noqa: F401
    except ImportError:
        print(_ma.problem_edge_tts())
        return 1

    if audit_scripts():
        print(u'\nบทหรือคำถามมีปัญหา ยังไม่สร้างเสียงให้')
        return 1

    outdir = os.path.join(ROOT, COURSE, 'listening')
    os.makedirs(outdir, exist_ok=True)

    _, html = read_page()
    old = {}
    m = INDEX_RE.search(html)
    if m and not a.force:
        try:
            old = json.loads(re.search(r'>(.*?)</script>', m.group(0), re.S).group(1))
        except Exception:
            old = {}

    clips, made, skipped = {}, 0, 0
    for st in SETS:
        print(u'\n%s' % st['title'])
        for part in st['parts']:
            sig = sig_of(part)
            mp3 = os.path.join(outdir, part['id'] + '.mp3')
            prev = old.get(part['id'])
            if prev and prev.get('sig') == sig and os.path.exists(mp3) and not a.force:
                clips[part['id']] = prev
                skipped += 1
                print(u'  ข้าม %s เพราะยังเหมือนเดิม' % part['id'])
                continue

            audio, cues, dur = await build_part(part)
            with open(mp3, 'wb') as f:
                f.write(audio)
            clips[part['id']] = {
                'src': 'listening/' + part['id'] + '.mp3',
                'dur': dur,
                'sig': sig,
                'cues': cues,
                'voices': sorted(set(VOICES.get(t[2], t[2]) for t in part['turns'])),
            }
            made += 1
            print(u'  เขียน %s · %.2f MB · %d:%02d'
                  % (os.path.relpath(mp3, ROOT), len(audio) / 1048576.0,
                     int(dur // 60), int(dur % 60)))

    write_index(clips)
    print(u'\nเสร็จแล้ว สร้างใหม่ %d คลิป · ข้าม %d คลิป' % (made, skipped))
    return 0


if __name__ == '__main__':
    try:
        sys.exit(asyncio.run(main()))
    except KeyboardInterrupt:
        print(u'\nยกเลิกแล้ว')
        sys.exit(1)
