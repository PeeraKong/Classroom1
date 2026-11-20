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

def _load(name):
    spec = importlib.util.spec_from_file_location(
        re.sub(r'\W', '_', name), os.path.join(HERE, name))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# รายการเสียงอยู่ที่ไฟล์บทชุดกลางภาคที่เดียว ทั้งสองชุดใช้ร่วมกัน
# ไม่งั้นรายการเสียงจะแตกเป็นสองชุดที่ค่อย ๆ ต่างกันโดยไม่มีใครรู้
_ld = _load('listening-data.py')
VOICES = _ld.VOICES

# ชุดกลางภาคกับชุดปลายภาคใช้เครื่องมือตัวนี้ร่วมกัน
# ต่างกันแค่สี่อย่าง ไฟล์บท หน้าเว็บที่เขียนกลับ โฟลเดอร์ไฟล์เสียง
# และรหัสบล็อก JSON ที่ฝังในหน้า จึงรวบไว้เป็นตารางที่เดียวตรงนี้
#
# anchor คือจุดที่จะแทรกบล็อกเข้าไปข้างหน้า ถ้าไม่มีก็ต่อท้ายไฟล์
EXAMS = {
    'midterm': {'data': 'listening-data.py', 'page': 'index.html',
                'dir': 'listening', 'pre': 'ls',
                'anchor': '\n<script type="application/json" id="vc-data">'},
    # หน้าชุดปลายภาคมีหมุดไว้ให้แล้ว เพราะสคริปต์ของหน้าต้องอ่านบล็อกนี้
    # ถ้าต่อท้ายไฟล์เฉย ๆ บล็อกจะไปอยู่หลังสคริปต์ แล้ว Part 3 จะว่าง
    'final': {'data': 'final-listening-data.py', 'page': 'final-sets.html',
              'dir': 'listening-final', 'pre': 'fl', 'anchor': '\n<!-- fl:blocks -->'},
}

EXAM = EXAMS['midterm']
SETS = _ld.SETS

# ต้องเขียนกลับทั้งสองบล็อก บทกับดัชนีไฟล์เสียง
#
# เดิมเขียนแค่ ls-audio ส่วน ls-data ซึ่งเป็นบทและคำถามที่หน้าเว็บแสดง
# ถูกฝังไว้ครั้งเดียวตอนสร้างแท็บ พอแก้ tools/listening-data.py แล้วสร้างเสียงใหม่
# ไฟล์เสียงจึงเป็นบทใหม่ แต่หน้าเว็บยังโชว์บทเก่าและถามคำถามเก่า
# ซึ่งไม่มีอะไรจับได้เลยเพราะจำนวนช่วงพูดบังเอิญเท่ากัน
BLOCK_RE = re.compile(
    r'\n*<script type="application/json" id="ls-(?:data|audio)">.*?</script>', re.S)


def select(exam):
    u"""เลือกว่ารอบนี้ทำชุดไหน แล้วตั้งค่าทั้งหมดให้ตรงกับชุดนั้น"""
    global EXAM, SETS, BLOCK_RE
    EXAM = EXAMS[exam]
    SETS = _ld.SETS if exam == 'midterm' else _load(EXAM['data']).SETS
    BLOCK_RE = re.compile(
        r'\n*<script type="application/json" id="%s-(?:data|audio)">.*?</script>'
        % EXAM['pre'], re.S)


def aid(what):
    u"""รหัสบล็อก JSON ของชุดที่กำลังทำ เช่น ls-data หรือ fl-audio"""
    return '%s-%s' % (EXAM['pre'], what)

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

        # บริการอ่านออกเสียงตอบ NoAudioReceived เป็นช่วง ๆ เมื่อเรียกติด ๆ กันนาน
        # รอบที่ทำสิบแปดคลิปรวดเคยล้มกลางทางมาแล้วทั้งที่ลองซ้ำสามครั้ง
        # จึงเพิ่มจำนวนครั้งและยืดเวลารอแบบทวีคูณ ให้ข้ามช่วงที่บริการไม่รับไปได้
        waits = (2, 5, 12, 25)
        for attempt in range(len(waits) + 1):
            try:
                data = await synth(text, voice, '', '')
                break
            except Exception as exc:
                if attempt == len(waits):
                    raise RuntimeError(
                        u'เรียกบริการอ่านออกเสียงไม่สำเร็จ · %s ช่วงที่ %d\n  ข้อความจากระบบ %s'
                        % (part['id'], i + 1, exc))
                sys.stdout.write(u'\n  %s ช่วงที่ %d ไม่ผ่าน จะลองใหม่ในอีก %d วินาที · %s\n'
                                 % (part['id'], i + 1, waits[attempt], exc))
                sys.stdout.flush()
                await asyncio.sleep(waits[attempt])

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
    path = os.path.join(ROOT, COURSE, EXAM['page'])
    # ตอนเริ่มทำชุดใหม่ ยังไม่มีหน้าเว็บ แต่อยากตรวจบทกับคำถามก่อนแล้ว
    # จึงยอมให้ยังไม่มีไฟล์ เพื่อให้ --check ใช้ได้ตั้งแต่ยังไม่มีหน้า
    if not os.path.exists(path):
        return path, u''
    return path, io.open(path, encoding='utf-8').read()


def page_data():
    """แปลงบทจาก listening-data.py เป็นรูปแบบที่หน้าเว็บอ่าน"""
    # ติดลายเซ็นของบทไปกับหน้าเว็บด้วย หน้าเว็บจะได้เทียบกับลายเซ็นที่ติดมากับไฟล์เสียง
    # แล้วรู้เองว่าคลิปยังพูดบทเก่าอยู่ไหม ไม่ต้องรอให้คนมาเจอเอง
    return [{'id': st['id'], 'title': st['title'],
             'parts': [{'id': p['id'], 'kind': p['kind'], 'title': p['title'],
                        'context': p['context'], 'sig': sig_of(p),
                        'turns': [[t[0], t[3]] for t in p['turns']],
                        'questions': [{'q': q['q'], 'o': list(q['o']),
                                       'a': q['a'], 'e': q['e']} for q in p['questions']]}
                       for p in st['parts']]}
            for st in SETS]


def write_index(clips):
    path, html = read_page()
    block = ('\n\n<script type="application/json" id="%s">\n' % aid('data') +
             json.dumps(page_data(), ensure_ascii=False, separators=(',', ':')) + '\n</script>' +
             '\n<script type="application/json" id="%s">\n' % aid('audio') +
             json.dumps(clips, ensure_ascii=False, separators=(',', ':')) + '\n</script>')
    html = BLOCK_RE.sub('', html).rstrip('\n')
    at = html.find(EXAM['anchor']) if EXAM['anchor'] else -1
    html = (html[:at] + block + html[at:]) if at > 0 else (html + block + '\n')
    io.open(path, 'w', encoding='utf-8').write(html.rstrip('\n') + '\n')
    print(u'  เขียนบทและดัชนีไฟล์เสียงกลับเข้า %s/%s แล้ว' % (COURSE, EXAM['page']))
    verify_page()


def verify_page():
    """ตรวจว่าบทในหน้าเว็บตรงกับไฟล์บทจริง ๆ หลังเขียนเสร็จ

    ข้อนี้เคยพลาดมาแล้ว จึงตรวจทุกครั้งไม่ให้เกิดซ้ำ
    """
    _, html = read_page()
    m = re.search(r'id="%s">(.*?)</script>' % aid('data'), html, re.S)
    if not m:
        print(u'  ตรวจแล้วไม่พบบทในหน้าเว็บ')
        return 1
    page = {p['id']: p for st in json.loads(m.group(1)) for p in st['parts']}
    bad = 0
    for st in SETS:
        for p in st['parts']:
            a = page.get(p['id'])
            if not a:
                print(u'  %s ไม่มีในหน้าเว็บ' % p['id']); bad += 1; continue
            if [t[1] for t in a['turns']] != [t[3] for t in p['turns']]:
                print(u'  %s บทในหน้าเว็บไม่ตรงกับไฟล์บท' % p['id']); bad += 1
            if [q['q'] for q in a['questions']] != [q['q'] for q in p['questions']]:
                print(u'  %s คำถามในหน้าเว็บไม่ตรงกับไฟล์บท' % p['id']); bad += 1
    print(u'  ตรวจบทในหน้าเว็บเทียบกับไฟล์บท · พบไม่ตรง %d จุด' % bad)

    # เทียบลายเซ็นของบทกับลายเซ็นที่ติดมากับไฟล์เสียง
    # นับจำนวนช่วงเสียงอย่างเดียวไม่พอ เพราะแก้ข้อความโดยไม่เพิ่มลดจำนวนช่วง
    # จะผ่านการตรวจแบบนั้นไปได้ทั้งที่คลิปยังพูดของเก่า ซึ่งเคยเกิดขึ้นมาแล้วจริง
    old = {}
    ma = re.search(r'id="%s">(.*?)</script>' % aid('audio'), html, re.S)
    if ma:
        try:
            old = json.loads(ma.group(1)) or {}
        except Exception:
            old = {}
    stale = [p['id'] for st in SETS for p in st['parts']
             if (old.get(p['id']) or {}).get('sig') not in (None, sig_of(p))]
    missing = [p['id'] for st in SETS for p in st['parts'] if p['id'] not in old]
    if stale:
        print(u'  คลิปที่ยังพูดบทเก่า ต้องสร้างเสียงใหม่ %d คลิป · %s'
              % (len(stale), ' '.join(stale)))
    if missing:
        print(u'  คลิปที่ยังไม่มีไฟล์เสียง %d คลิป · %s' % (len(missing), ' '.join(missing)))
    if not stale and not missing:
        print(u'  ไฟล์เสียงทุกคลิปตรงกับบทปัจจุบัน')
    return bad


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
            # การสัมภาษณ์งานมีสองฝ่ายพอดี ผู้สัมภาษณ์กับผู้สมัคร
            # ถ้าเหลือคนเดียวก็ไม่ใช่การสัมภาษณ์ ถ้าเกินสองก็ไม่ใช่แนวข้อสอบนี้
            if part['kind'] == 'interview' and len(speakers) != 2:
                fail(pid, u'เป็นการสัมภาษณ์งาน แต่มีผู้พูด %d คน ต้องเป็น 2' % len(speakers))
            if part['kind'] not in ('presentation', 'talk', 'interview'):
                fail(pid, u'ไม่รู้จักชนิดบท %s' % part['kind'])

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

                # หัวใจของแบบฝึกฟัง คือคลิปต้องไม่พูดคำตอบออกมาตรง ๆ
                # ถ้าพูดเป๊ะ นิสิตแค่รอจับเสียงให้ตรงคำในตัวเลือกก็ได้คะแนน
                # โดยไม่ต้องเข้าใจว่าพูดอะไร ตัวเลือกที่ถูกจึงต้องเป็นการถอดความ
                # หรือเป็นข้อสรุปจากสิ่งที่ได้ยิน
                why = echoes(q['o'][q['a']], script)
                if why:
                    fail(pid, u'คลิปพูดคำตอบตรง ๆ (%s) · %s' % (why, q['o'][q['a']][:44]))

                # แบบฝึกนี้วัดการฟัง ไม่ได้วัดการคิดเลข
                # ถ้าคำตอบคือผลลบหรือผลหาร นิสิตที่ฟังเข้าใจครบแต่คิดเลขพลาด
                # จะเสียคะแนนทั้งที่ทักษะที่ข้อสอบตั้งใจวัดไม่ได้บกพร่องเลย
                why = arithmetic(q['o'][q['a']], q.get('e', ''))
                if why:
                    fail(pid, u'คำถามต้องคิดเลข (%s) · %s' % (why, q['o'][q['a']][:44]))
    return bad


# คำบอกจำนวนในภาษาอังกฤษ ใช้ดูว่าคำตอบเป็นตัวเลขล้วนหรือเปล่า
NUMBER_WORDS = set(u'''
one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen
sixteen seventeen eighteen nineteen twenty thirty forty fifty sixty seventy eighty ninety
hundred thousand million billion percent point half third quarter quarters fifth fifths
tenth tenths twice double dozen
'''.split())

# ร่องรอยของการคิดเลขในคำอธิบาย เช่น 310 ลบ 205 เท่ากับ 105
# เทียบกับตัวเลขข้างหน้าเสมอ ไม่งั้นคำว่า บริหาร จะโดนจับเพราะมี หาร อยู่ข้างใน
CALC_RE = re.compile(
    u'\\d[\\d,\\.]*\\s*(?:ลบ|บวก|คูณ|หาร|[-+×÷*/])|เท่ากับ|ผลต่าง|หารด้วย')


def arithmetic(answer, why):
    u"""ข้อนี้บังคับให้คิดเลขหรือเปล่า

    จับสองแบบ
      คำตอบเป็นตัวเลขล้วน เช่น One thousand eight hundred yen
        ซึ่งแปลว่าต้องไปหาตัวเลขมาบวกลบเอง เพราะคลิปพูดตรง ๆ ไม่ได้อยู่แล้ว
      คำอธิบายมีร่องรอยการคำนวณ เช่น 420 ลบที่ดิน 60 เหลือเงินสด 360 ล้าน
    """
    core = [w for w in re.findall(r"[a-z']+", answer.lower())
            if w not in STOP and w not in ('about', 'over', 'under', 'almost', 'nearly')]
    if core and sum(1 for w in core if w in NUMBER_WORDS) * 2 >= len(core):
        return u'คำตอบเป็นตัวเลขล้วน'
    if CALC_RE.search(why):
        return u'คำอธิบายมีการคำนวณ'
    return u''


# คำไวยากรณ์ที่ไม่นับเป็นเนื้อความ เพราะมีอยู่ทุกประโยคอยู่แล้ว
STOP = {'a', 'an', 'the', 'of', 'to', 'in', 'on', 'at', 'by', 'for', 'and', 'or',
        'is', 'was', 'were', 'are', 'be', 'been', 'it', 'its', 'that', 'this',
        'with', 'from', 'as', 'than', 'then', 'they', 'their', 'he', 'she'}


def words(s):
    return re.sub(r'[^a-z0-9 ]', ' ', s.lower().replace(u'’', "'")).split()


def echoes(answer, script):
    u"""ตัวเลือกที่ถูก ไปตรงกับข้อความในบทมากเกินไปหรือเปล่า

    จับสองแบบ
      พูดเป๊ะทั้งวลี เช่น ตัวเลือก "Three months" กับบท "over three months"
      พูดครบทุกคำในช่วงสั้น ๆ แม้สลับลำดับ เช่น "It falls to six hundred thousand"
        กับบท "then it falls to six hundred thousand from year two"
    คืนเหตุผลเป็นข้อความถ้าซ้ำ คืนค่าว่างถ้าผ่าน
    """
    aw = words(answer)
    sw = words(script)
    if not aw:
        return u''

    joined = ' '.join(sw)
    if ' '.join(aw) in joined:
        return u'ตรงทั้งวลี'

    # ตัวเลือกคำเดียวที่เป็นคำไวยากรณ์ ไม่ต้องตรวจ เพราะเลี่ยงไม่ได้
    core = [w for w in aw if w not in STOP]
    if len(core) < 2:
        return u''

    # หาหน้าต่างในบทที่ยาวพอ ๆ กับตัวเลือก แล้วดูว่ากินคำเนื้อความไปหมดไหม
    span = len(aw) + 4
    need = set(core)
    for i in range(max(1, len(sw) - span + 1)):
        if need <= set(sw[i:i + span]):
            return u'คำเนื้อความครบทุกคำในช่วงเดียว'
    return u''


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
    m = re.search(r'id="%s">(.*?)</script>' % aid('audio'), html, re.S)
    if m:
        try:
            old = json.loads(m.group(1))
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
            mp3 = os.path.join(ROOT, COURSE, EXAM['dir'], part['id'] + '.mp3')
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
    ap.add_argument('--page-only', action='store_true',
                    help=u'เขียนบทกลับเข้าหน้าเว็บอย่างเดียว ไม่แตะไฟล์เสียง')
    ap.add_argument('--exam', choices=sorted(EXAMS), default='midterm',
                    help=u'ทำชุดกลางภาคหรือชุดปลายภาค ค่าตั้งต้นคือ midterm')
    a = ap.parse_args()
    select(a.exam)

    if a.check:
        return check()

    # ใช้เมื่อแก้แต่คำถามหรือคำอธิบาย ซึ่งไม่กระทบไฟล์เสียง จึงไม่ต้องสังเคราะห์ใหม่
    if a.page_only:
        if audit_scripts():
            print(u'\nบทหรือคำถามมีปัญหา ยังไม่เขียนให้')
            return 1
        _, html = read_page()
        m = re.search(r'id="%s">(.*?)</script>' % aid('audio'), html, re.S)
        try:
            clips = json.loads(m.group(1)) if m else {}
        except Exception:
            clips = {}
        write_index(clips)
        return 0

    try:
        import edge_tts                                            # noqa: F401
    except ImportError:
        print(_ma.problem_edge_tts())
        return 1

    if audit_scripts():
        print(u'\nบทหรือคำถามมีปัญหา ยังไม่สร้างเสียงให้')
        return 1

    outdir = os.path.join(ROOT, COURSE, EXAM['dir'])
    os.makedirs(outdir, exist_ok=True)

    _, html = read_page()
    old = {}
    m = re.search(r'id="%s">(.*?)</script>' % aid('audio'), html, re.S)
    if m and not a.force:
        try:
            old = json.loads(m.group(1))
        except Exception:
            old = {}

    clips, made, skipped, failed = {}, 0, 0, []
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

            # คลิปเดียวล้มต้องไม่ทิ้งคลิปที่ทำเสร็จไปแล้วทั้งหมด
            # เดิมปล่อยให้ข้อผิดพลาดลอยขึ้นไป ทั้งรอบจึงจบลงโดยไม่ได้เขียนดัชนี
            # ไฟล์ mp3 ที่สร้างเสร็จแล้วก็เลยไม่ถูก commit และต้องเริ่มใหม่หมด
            try:
                audio, cues, dur = await build_part(part)
            except Exception as exc:
                failed.append(part['id'])
                print(u'  ข้าม %s เพราะสร้างไม่สำเร็จ · %s' % (part['id'], exc))
                continue

            with open(mp3, 'wb') as f:
                f.write(audio)
            clips[part['id']] = {
                'src': EXAM['dir'] + '/' + part['id'] + '.mp3',
                'dur': dur,
                'sig': sig,
                'cues': cues,
                'voices': sorted(set(VOICES.get(t[2], t[2]) for t in part['turns'])),
            }
            made += 1
            print(u'  เขียน %s · %.2f MB · %d:%02d'
                  % (os.path.relpath(mp3, ROOT), len(audio) / 1048576.0,
                     int(dur // 60), int(dur % 60)))

    # เขียนดัชนีด้วยเท่าที่ทำได้เสมอ แม้มีคลิปที่ล้ม
    # หน้าเว็บรองรับคลิปที่ยังไม่มีไฟล์เสียงอยู่แล้ว คือขึ้นว่ายังไม่มีและเปิดบทอ่านแทน
    write_index(clips)
    print(u'\nเสร็จแล้ว สร้างใหม่ %d คลิป · ข้าม %d คลิป' % (made, skipped))
    if failed:
        print(u'สร้างไม่สำเร็จ %d คลิป · %s' % (len(failed), ' '.join(failed)))
        print(u'สั่งซ้ำได้เลย คลิปที่เสร็จแล้วจะถูกข้าม เพราะเทียบจากลายเซ็นของบท')
        return 1
    return 0


if __name__ == '__main__':
    try:
        sys.exit(asyncio.run(main()))
    except KeyboardInterrupt:
        print(u'\nยกเลิกแล้ว')
        sys.exit(1)
