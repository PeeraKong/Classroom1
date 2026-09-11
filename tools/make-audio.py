#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
สร้างไฟล์เสียงบรรยายประจำบทด้วยเสียงไทยผู้ชายแบบ neural

ใช้บริการอ่านออกเสียงตัวเดียวกับปุ่ม Read Aloud ของ Microsoft Edge ผ่านแพ็กเกจ edge-tts
ไม่ต้องมี API key ไม่ต้องสมัครอะไร แต่ต้องต่ออินเทอร์เน็ตตอนสร้าง

    pip3 install edge-tts
    python3 tools/make-audio.py

จะได้ไฟล์ <วิชา>/audio/<บท>.mp3 และเขียนตารางเวลาของแต่ละย่อหน้ากลับเข้าไปใน
index.html ของวิชานั้น เพื่อให้เครื่องเล่นในหน้าเว็บไฮไลต์ตามและกดข้ามย่อหน้าได้

รันซ้ำได้ บทไหนที่บทบรรยายไม่เปลี่ยนจะถูกข้ามไป ถ้าอยากสร้างใหม่ทั้งหมดให้ใส่ --force
"""

import argparse
import asyncio
import hashlib
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COURSES = ['adv-acctg-1', 'audit', 'erp', 'marketing']

# เสียงไทยที่บริการนี้มีให้ ตัวแรกเป็นผู้ชาย
VOICES = {
    'male':   'th-TH-NiwatNeural',
    'female': 'th-TH-PremwadeeNeural',
}

DATA_RE  = re.compile(r'(<script type="application/json" id="cn-data">)(.*?)(</script>)', re.S)
AUDIO_RE = re.compile(r'\n*<script type="application/json" id="cn-audio">.*?</script>', re.S)

# ความยาวหนึ่งเฟรมของ MP3 ที่บริการนี้ส่งกลับมา คือ MPEG-2 Layer III 24 kHz โมโน
# เฟรมหนึ่งมี 576 ตัวอย่าง จึงยาว 576 / 24000 วินาที
SAMPLES_PER_FRAME = 576
BITRATES_V2_L3 = [0, 8, 16, 24, 32, 40, 48, 56, 64, 80, 96, 112, 128, 144, 160, 0]
RATES_V2  = [22050, 24000, 16000, 0]
RATES_V25 = [11025, 12000, 8000, 0]


def mp3_duration(data):
    """ไล่ส่วนหัวของแต่ละเฟรมเพื่อหาความยาวจริง โดยไม่ต้องพึ่ง ffmpeg"""
    i, total = 0, 0.0
    n = len(data)
    while i + 4 <= n:
        if data[i] != 0xFF or (data[i + 1] & 0xE0) != 0xE0:
            # ข้ามแท็ก ID3 ที่บริการแนบมาต้นไฟล์
            if data[i:i + 3] == b'ID3' and i + 10 <= n:
                size = ((data[i + 6] & 0x7F) << 21 | (data[i + 7] & 0x7F) << 14 |
                        (data[i + 8] & 0x7F) << 7 | (data[i + 9] & 0x7F))
                i += 10 + size
                continue
            i += 1
            continue
        ver = (data[i + 1] >> 3) & 0x03      # 0 = MPEG2.5, 2 = MPEG2, 3 = MPEG1
        layer = (data[i + 1] >> 1) & 0x03    # 1 = Layer III
        bri = (data[i + 2] >> 4) & 0x0F
        sri = (data[i + 2] >> 2) & 0x03
        pad = (data[i + 2] >> 1) & 0x01
        if layer != 1 or ver == 1 or bri in (0, 15) or sri == 3:
            i += 1
            continue
        rate = (RATES_V25 if ver == 0 else RATES_V2)[sri] if ver != 3 else 0
        if not rate:
            i += 1
            continue
        kbps = BITRATES_V2_L3[bri]
        length = (72 * kbps * 1000) // rate + pad
        if length <= 4:
            i += 1
            continue
        total += SAMPLES_PER_FRAME / float(rate)
        i += length
    return total


def read_page(course):
    path = os.path.join(ROOT, course, 'index.html')
    if not os.path.exists(path):          # วิชาที่ยังไม่มีหน้าเว็บ ให้ข้ามไปแทนที่จะพัง
        return None, None, None
    html = io.open(path, encoding='utf-8').read()
    m = DATA_RE.search(html)
    if not m:
        return None, None, None
    return path, html, json.loads(m.group(2))


def chapter_lines(chapter):
    out = []
    for cue in chapter.get('c', []):
        for line in cue.get('t', []):
            out.append(line)
    return out


async def synth(text, voice, rate, pitch):
    import edge_tts
    args = {}
    if rate:
        args['rate'] = rate
    if pitch:
        args['pitch'] = pitch
    buf = bytearray()
    comm = edge_tts.Communicate(text, voice, **args)
    async for chunk in comm.stream():
        if chunk['type'] == 'audio':
            buf.extend(chunk['data'])
    return bytes(buf)


async def build_chapter(lines, voice, rate, pitch, label):
    """สร้างทีละย่อหน้าแล้วต่อกัน เพื่อให้รู้เวลาเริ่มของแต่ละย่อหน้าอย่างแม่นยำ"""
    parts, cues, at = [], [], 0.0
    for i, line in enumerate(lines):
        for attempt in range(3):
            try:
                data = await synth(line, voice, rate, pitch)
                break
            except Exception as exc:                      # เครือข่ายสะดุดเป็นเรื่องปกติ ลองใหม่
                if attempt == 2:
                    raise RuntimeError(
                        u'เรียกบริการอ่านออกเสียงไม่สำเร็จ สาเหตุที่พบบ่อยคือเน็ตหลุด '
                        u'หรือเครือข่ายที่ใช้อยู่บล็อกปลายทาง speech.platform.bing.com '
                        u'ลองเปลี่ยนเครือข่ายหรือปิด VPN แล้วรันใหม่ '
                        u'สคริปต์จะทำต่อจากบทที่ค้างไว้ให้เอง\n  ข้อความจากระบบ %s' % exc)
                await asyncio.sleep(1.5 * (attempt + 1))
        cues.append(round(at, 3))
        at += mp3_duration(data)
        parts.append(data)
        sys.stdout.write('\r  %s  %d/%d ย่อหน้า · %d:%02d' %
                         (label, i + 1, len(lines), int(at // 60), int(at % 60)))
        sys.stdout.flush()
    sys.stdout.write('\n')
    return b''.join(parts), cues, round(at, 3)


def problem_edge_tts():
    return (u'\n  ยังไม่ได้ติดตั้ง edge-tts สำหรับ Python ตัวที่กำลังรันอยู่\n'
            u'  ตัวที่รันอยู่คือ %s\n\n'
            u'  ให้ติดตั้งด้วยคำสั่งนี้ ซึ่งผูกกับ Python ตัวเดียวกันแน่นอน\n\n'
            u'      %s -m pip install edge-tts\n\n'
            u'  แล้วรันใหม่อีกครั้ง\n' % (sys.executable, sys.executable))


def sig_of(lines, voice, rate, pitch):
    """ลายเซ็นของบท ใช้ตัดสินว่าต้องสร้างไฟล์เสียงใหม่หรือไม่"""
    return hashlib.sha1(('\n'.join(lines) + '|' + voice + '|' + rate + '|' + pitch)
                        .encode('utf-8')).hexdigest()[:12]


def check(voice='th-TH-NiwatNeural', rate='', pitch='', courses=None):
    """บอกสถานะทุกอย่างที่จำเป็น เพื่อให้รู้ว่าติดตรงไหน"""
    print(u'\nPython ที่ใช้อยู่   %s' % sys.executable)
    print(u'เวอร์ชัน            %s' % sys.version.split()[0])
    try:
        import edge_tts
        v = getattr(edge_tts, '__version__', 'ไม่ทราบเวอร์ชัน')
        print(u'edge-tts           ติดตั้งแล้ว รุ่น %s' % v)
        ok = True
    except ImportError:
        print(u'edge-tts           ยังไม่ได้ติดตั้ง')
        ok = False

    print('')
    total_ch = total_done = total_lines = 0
    for course in (courses or COURSES):
        path, html, data = read_page(course)
        if not data:
            print(u'%-13s ไม่พบบทบรรยายในหน้า' % course)
            continue
        m = AUDIO_RE.search(html or '')
        clips = {}
        if m:
            try:
                clips = json.loads(re.search(r'>(.*?)</script>', m.group(0), re.S).group(1))
            except Exception:
                clips = {}
        done, todo = [], []
        for key, ch in data.items():
            lines = chapter_lines(ch)
            c = clips.get(key)
            has = os.path.exists(os.path.join(ROOT, course, 'audio', key + '.mp3'))
            if not has:
                todo.append((key, len(lines), u'ยังไม่มีไฟล์'))
            elif not c or c.get('sig') != sig_of(lines, voice, rate, pitch):
                todo.append((key, len(lines), u'บทบรรยายเปลี่ยน ต้องสร้างใหม่'))
            else:
                done.append(key)
        total_ch += len(data)
        total_done += len(done)
        total_lines += sum(t[1] for t in todo)
        if not todo and data:
            v = (clips.get(list(data)[0]) or {}).get('voice', '')
            print(u'%-13s ครบ %d บท · เสียง %s' % (course, len(data), v))
        else:
            print(u'%-13s พร้อม %d จาก %d บท' % (course, len(done), len(data)))
            for key, n, why in todo:
                print(u'              %-5s %3d ย่อหน้า · %s' % (key, n, why))

    print('')
    if total_done == total_ch and total_ch:
        print(u'พร้อมแล้ว ทุกบทมีไฟล์เสียง เปิดหน้าเว็บแล้วกดฟังสรุปบทได้เลย')
    elif not ok:
        print(problem_edge_tts())
    else:
        # ประมาณเวลาจากจำนวนย่อหน้า วัดได้ราว 25 ย่อหน้าต่อนาทีจากการใช้งานจริง
        mins = max(1, int(round(total_lines / 25.0)))
        print(u'ต้องสร้างไฟล์เสียง %d บท รวม %d ย่อหน้า ใช้เวลาราว %d นาที'
              % (total_ch - total_done, total_lines, mins))
        print(u'ให้รัน  %s tools/make-audio.py' % sys.executable)
    return 0


async def main():
    ap = argparse.ArgumentParser(description='สร้างไฟล์เสียงบรรยายประจำบท')
    ap.add_argument('courses', nargs='*', default=[], help='ชื่อโฟลเดอร์วิชา เว้นว่างคือทำทุกวิชา')
    ap.add_argument('--voice', default='male', help='male, female หรือชื่อเสียงเต็ม เช่น th-TH-NiwatNeural')
    ap.add_argument('--rate', default='', help='ปรับความเร็วตอนสร้าง เช่น -10%% หรือ +15%%')
    ap.add_argument('--pitch', default='', help='ปรับระดับเสียงตอนสร้าง เช่น -5Hz')
    ap.add_argument('--force', action='store_true', help='สร้างใหม่แม้บทบรรยายไม่เปลี่ยน')
    ap.add_argument('--check', action='store_true', help='ตรวจว่าพร้อมสร้างไหม แล้วรายงานสถานะ ไม่สร้างจริง')
    a = ap.parse_args()

    # ชื่อวิชาที่ไม่รู้จักต้องบอกให้ชัดตั้งแต่ต้น ไม่ใช่ปล่อยไปพังตอนเปิดไฟล์
    # กรณีที่เจอบ่อยที่สุดคือพิมพ์ตัวเลือกตกขีดสองขีด เช่น check แทน --check
    unknown = [c for c in a.courses if c not in COURSES]
    if unknown:
        print(u'\nไม่รู้จักวิชา %s' % ' '.join(unknown))
        for c in unknown:
            flag = c.lstrip('-')
            if flag in ('check', 'force', 'voice', 'rate', 'pitch', 'help'):
                print(u'\nถ้าตั้งใจจะใช้ตัวเลือก ต้องมีขีดสองขีดนำหน้าเสมอ')
                print(u'   พิมพ์   --%s' % flag)
                print(u'   ไม่ใช่  %s' % c)
                break
        print(u'\nชื่อวิชาที่ใช้ได้คือ %s' % ' '.join(COURSES))
        print(u'เว้นว่างไว้คือทำทุกวิชา')
        return 1

    if a.check:
        return check(VOICES.get(a.voice, a.voice), a.rate, a.pitch, a.courses or None)

    try:
        import edge_tts  # noqa: F401
    except ImportError:
        print(problem_edge_tts())
        return 1

    voice = VOICES.get(a.voice, a.voice)
    courses = a.courses or COURSES
    made = skipped = 0
    found = []          # เก็บไว้บอกผู้ใช้ว่าหน้าเว็บในเครื่องนี้มีบทอะไรบ้าง

    for course in courses:
        path, html, data = read_page(course)
        if not data:
            print('ข้าม %s เพราะไม่พบบทบรรยายในหน้า' % course)
            continue

        outdir = os.path.join(ROOT, course, 'audio')
        os.makedirs(outdir, exist_ok=True)
        clips = {}
        old = {}
        m = AUDIO_RE.search(html)
        if m and not a.force:
            try:
                old = json.loads(re.search(r'>(.*?)</script>', m.group(0), re.S).group(1))
            except Exception:
                old = {}

        found.append((course, list(data)))
        print('\n%s · %d บท · เสียง %s' % (course, len(data), voice))
        print('  บทที่พบในหน้าเว็บ  %s' % ' '.join(data))
        for key, chapter in data.items():
            lines = chapter_lines(chapter)
            if not lines:
                continue
            sig = sig_of(lines, voice, a.rate, a.pitch)
            mp3 = os.path.join(outdir, key + '.mp3')
            prev = old.get(key)
            if prev and prev.get('sig') == sig and os.path.exists(mp3) and not a.force:
                clips[key] = prev
                skipped += 1
                print('  ข้าม %s เพราะยังเหมือนเดิม' % key)
                continue

            audio, cues, dur = await build_chapter(lines, voice, a.rate, a.pitch,
                                                   key + ' ' + (chapter.get('s') or ''))
            with open(mp3, 'wb') as f:
                f.write(audio)
            clips[key] = {
                'src': 'audio/' + key + '.mp3',
                'dur': dur,
                'voice': voice,
                'sig': sig,
                'cues': cues,
            }
            made += 1
            print('  เขียน %s · %.1f MB · %d:%02d' %
                  (os.path.relpath(mp3, ROOT), len(audio) / 1048576.0, int(dur // 60), int(dur % 60)))

        block = ('\n\n<script type="application/json" id="cn-audio">\n' +
                 json.dumps(clips, ensure_ascii=False, separators=(',', ':')) + '\n</script>')
        html = AUDIO_RE.sub('', html).rstrip('\n')
        # วางไว้ก่อนบล็อกเครื่องเล่น เพื่อให้สคริปต์อ่านเจอตอนทำงาน
        anchor = '\n<!-- ============================================================\n     เครื่องเล่นเสียงบรรยายประจำบท'
        at = html.find(anchor)
        html = (html[:at] + block + html[at:]) if at > 0 else (html + block + '\n')
        io.open(path, 'w', encoding='utf-8').write(html.rstrip('\n') + '\n')
        print('  ปรับ %s/index.html ให้ชี้ไปยังไฟล์เสียงแล้ว' % course)

    print('\nเสร็จแล้ว สร้างใหม่ %d บท · ข้าม %d บท' % (made, skipped))
    if made:
        print('อย่าลืม git add แล้ว commit ไฟล์ในโฟลเดอร์ audio ด้วยนะครับ')
    else:
        # กรณีที่สับสนกันบ่อยที่สุด คือหน้าเว็บในเครื่องยังเป็นรุ่นเก่า
        # จึงไม่มีบทใหม่ให้สร้าง แต่สคริปต์บอกแค่ว่าข้ามหมด ทำให้ดูเหมือนไม่ทำงาน
        print(u'\nไม่ได้สร้างไฟล์เสียงใหม่เลย เพราะทุกบทที่พบมีไฟล์เสียงตรงกันอยู่แล้ว')
        print(u'\nบทที่พบในเครื่องนี้')
        for course, keys in found:
            print(u'   %-13s %s' % (course, ' '.join(keys)))
        print(u'\nถ้าคิดว่าควรมีบทมากกว่านี้ แปลว่าไฟล์ index.html ในเครื่องยังไม่ใช่รุ่นล่าสุด')
        print(u'ให้รันคำสั่งนี้ก่อน แล้วดับเบิลคลิกไฟล์นี้ใหม่')
        print(u'\n    git pull\n')
    return 0


if __name__ == '__main__':
    try:
        sys.exit(asyncio.run(main()))
    except KeyboardInterrupt:
        print('\nยกเลิกแล้ว')
        sys.exit(1)
