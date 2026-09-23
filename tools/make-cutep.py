#!/usr/bin/env python3
# -*- coding: utf-8 -*-
u"""สร้างไฟล์เสียงและฝังข้อมูลของแบบฝึกฟังแนว CU-TEP

ต่างจาก tools/make-listening.py ตรงที่รูปแบบข้อสอบคนละแบบกัน
  ของเดิม  คลิปยาวสองคลิปต่อชุด คำถามพิมพ์ไว้ให้อ่านก่อน เน้นจับตัวเลข
  ชุดนี้    30 ข้อต่อชุดตามโครงสร้าง CU-TEP และ คำถามถูกพูดอยู่ในไฟล์เสียง

    python3 tools/make-cutep.py --check   ตรวจอย่างเดียว
    python3 tools/make-cutep.py           สร้างเสียงแล้วฝังข้อมูล

ไฟล์เสียงออกที่ oral-eng/cutep/<รหัส>.mp3
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
OUTDIR = os.path.join(ROOT, COURSE, 'cutep')

_spec = importlib.util.spec_from_file_location('make_audio', os.path.join(HERE, 'make-audio.py'))
_ma = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_ma)
synth, mp3_duration = _ma.synth, _ma.mp3_duration

_ls = importlib.util.spec_from_file_location('mk_listening', os.path.join(HERE, 'make-listening.py'))
_ml = importlib.util.module_from_spec(_ls)
_ls.loader.exec_module(_ml)
silence = _ml.silence

# เสียงที่ใช้ · m2 สงวนไว้เป็นผู้อ่านคำถามอย่างเดียว จะได้แยกออกจากเสียงในบทสนทนา
VOICES = {
    'm1': 'en-US-AndrewNeural',
    'm3': 'en-US-GuyNeural',
    'f1': 'en-US-AvaNeural',
    'f2': 'en-GB-SoniaNeural',
    'f3': 'en-US-JennyNeural',
}
NARRATOR = 'en-GB-RyanNeural'

# เว้นจังหวะ · ก่อนคำถามเว้นยาวกว่าในบท เพื่อให้รู้ว่าบทจบแล้ว
GAP_TURN = 0.55
GAP_QUESTION = 1.3

SET_FILES = ['cutep-1.py', 'cutep-2.py', 'cutep-3.py', 'cutep-4.py', 'cutep-5.py']

BLOCK_RE = re.compile(r'\n*<script type="application/json" id="ct-(?:data|audio)">.*?</script>', re.S)
ANCHOR = '\n<script type="application/json" id="vc-data">'


def load_sets():
    out = []
    for name in SET_FILES:
        path = os.path.join(HERE, name)
        if not os.path.exists(path):
            continue
        spec = importlib.util.spec_from_file_location(name[:-3].replace('-', '_'), path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        out.append(mod.SET)
    return out


def items_of(st):
    """คืนรายการคลิปทั้งหมดของชุด ในรูปแบบเดียวกันหมด เพื่อให้วนสร้างเสียงได้ง่าย

    คลิปหนึ่งคือ บทพูด แล้วตามด้วยคำถามที่ถูกอ่านออกเสียง
    บทสนทนาสั้นมีคำถามเดียว ส่วนบทยาวกับบทบรรยายมีสามคำถาม
    """
    out = []
    for d in st['short']:
        out.append({'id': d['id'], 'kind': 'short', 'title': '', 'context': '',
                    'turns': d['turns'],
                    'questions': [{'q': d['q'], 'o': d['o'], 'e': d['e']}]})
    for d in st['long']:
        out.append({'id': d['id'], 'kind': 'long', 'title': d['title'], 'context': d['context'],
                    'turns': d['turns'], 'questions': d['questions']})
    for d in st['mono']:
        out.append({'id': d['id'], 'kind': 'mono', 'title': d['title'], 'context': d['context'],
                    'turns': d['turns'], 'questions': d['questions']})
    return out


def audit(sets):
    """ตรวจให้ครบก่อนเสียเวลาสังเคราะห์เสียง เพราะรอบหนึ่งใช้เวลาหลายสิบนาที"""
    bad = 0

    def fail(where, msg):
        nonlocal bad
        bad += 1
        print(u'  %-7s %s' % (where, msg))

    seen_id = {}
    for st in sets:
        n_short, n_long, n_mono = len(st['short']), len(st['long']), len(st['mono'])
        if (n_short, n_long, n_mono) != (15, 3, 2):
            fail(st['id'], u'โครงสร้างเป็น %d/%d/%d ต้องเป็น 15/3/2 ตาม CU-TEP'
                 % (n_short, n_long, n_mono))

        total = 0
        for it in items_of(st):
            iid = it['id']
            if iid in seen_id:
                fail(iid, u'รหัสซ้ำกับคลิปอื่น')
            seen_id[iid] = True

            want = 1 if it['kind'] == 'short' else 3
            if len(it['questions']) != want:
                fail(iid, u'มีคำถาม %d ข้อ ต้องเป็น %d' % (len(it['questions']), want))
            total += len(it['questions'])

            speakers = set(t[0] for t in it['turns'])
            if it['kind'] in ('short', 'long') and len(speakers) != 2:
                fail(iid, u'บทสนทนาต้องมีผู้พูดสองคน แต่มี %d คน' % len(speakers))
            if it['kind'] == 'mono' and len(speakers) != 1:
                fail(iid, u'บทบรรยายต้องมีผู้พูดคนเดียว แต่มี %d คน' % len(speakers))

            # ผู้พูดคนเดียวกันต้องใช้เสียงเดิมตลอดคลิป ไม่งั้นผู้ฟังแยกไม่ออก
            by_speaker = {}
            for name, vkey, _text in it['turns']:
                if vkey not in VOICES:
                    fail(iid, u'อ้างเสียง %s ซึ่งไม่มีในรายการ' % vkey)
                by_speaker.setdefault(name, set()).add(vkey)
            for name, vs in by_speaker.items():
                if len(vs) > 1:
                    fail(iid, u'ผู้พูด %s ใช้เสียงไม่คงที่' % name)
            if len(set(v for vs in by_speaker.values() for v in vs)) != len(by_speaker):
                fail(iid, u'ผู้พูดต่างคนใช้เสียงเดียวกัน')

            words = sum(len(t[2].split()) for t in it['turns'])
            if it['kind'] == 'short' and not 12 <= words <= 70:
                fail(iid, u'บทสนทนาสั้นมี %d คำ ควรอยู่ราว 12 ถึง 70 คำ' % words)
            if it['kind'] == 'mono' and not 180 <= words <= 280:
                fail(iid, u'บทบรรยายมี %d คำ ควรอยู่ราว 180 ถึง 280 คำ' % words)

            for q in it['questions']:
                if len(q['o']) != 4 or len(set(q['o'])) != 4:
                    fail(iid, u'ตัวเลือกไม่ครบสี่หรือซ้ำกัน · %s' % q['q'][:40])
                if not q.get('e', '').strip():
                    fail(iid, u'ไม่มีคำอธิบาย · %s' % q['q'][:40])
                if not q['q'].rstrip().endswith('?'):
                    fail(iid, u'คำถามไม่ได้ลงท้ายด้วยเครื่องหมายคำถาม · %s' % q['q'][:40])

        if total != 30:
            fail(st['id'], u'รวมได้ %d ข้อ ต้องเป็น 30 ข้อตาม CU-TEP' % total)
    return bad


def sig_of(item):
    """ลายเซ็นรวมทั้งบทและคำถาม เพราะคำถามถูกอ่านอยู่ในไฟล์เสียงด้วย"""
    key = '\n'.join('%s|%s|%s' % (t[0], VOICES[t[1]], t[2]) for t in item['turns'])
    key += '\n#\n' + '\n'.join(q['q'] for q in item['questions'])
    return hashlib.sha1(key.encode('utf-8')).hexdigest()[:12]


async def build_item(item, index):
    """ต่อบทพูดแล้วตามด้วยคำถามที่อ่านออกเสียง คืนเสียง cue และความยาว"""
    chunks, cues, at = [], [], 0.0
    prev = None
    for name, vkey, text in item['turns']:
        if prev is not None and name != prev:
            gap = silence(GAP_TURN)
            at += mp3_duration(gap)
            chunks.append(gap)
        prev = name
        data = await synth_retry(text, VOICES[vkey], item['id'])
        cues.append(round(at, 3))
        at += mp3_duration(data)
        chunks.append(data)

    qcues = []
    for i, q in enumerate(item['questions']):
        gap = silence(GAP_QUESTION)
        at += mp3_duration(gap)
        chunks.append(gap)
        spoken = 'Question %d. %s' % (index + i, q['q'])
        data = await synth_retry(spoken, NARRATOR, item['id'])
        qcues.append(round(at, 3))
        at += mp3_duration(data)
        chunks.append(data)

    return b''.join(chunks), cues, qcues, round(at, 3)


async def synth_retry(text, voice, where):
    for attempt in range(3):
        try:
            return await synth(text, voice, '', '')
        except Exception as exc:
            if attempt == 2:
                raise RuntimeError(u'เรียกบริการอ่านออกเสียงไม่สำเร็จ · %s\n  %s' % (where, exc))
            await asyncio.sleep(1.5 * (attempt + 1))


def read_page():
    path = os.path.join(ROOT, COURSE, 'index.html')
    return path, io.open(path, encoding='utf-8').read()


def old_index():
    _, html = read_page()
    m = re.search(r'id="ct-audio">(.*?)</script>', html, re.S)
    try:
        return json.loads(m.group(1)) if m else {}
    except Exception:
        return {}


def write_page(sets, clips):
    """ฝังทั้งข้อมูลข้อสอบและดัชนีไฟล์เสียง เป็นสองบล็อกติดกัน"""
    data = []
    for st in sets:
        data.append({
            'id': st['id'], 'title': st['title'],
            'items': [{'id': it['id'], 'kind': it['kind'], 'title': it['title'],
                       'context': it['context'],
                       'turns': [[t[0], t[2]] for t in it['turns']],
                       'qs': [{'q': q['q'], 'o': list(q['o']), 'e': q['e']}
                              for q in it['questions']]}
                      for it in items_of(st)],
        })
    path, html = read_page()
    block = ('\n\n<script type="application/json" id="ct-data">\n' +
             json.dumps(data, ensure_ascii=False, separators=(',', ':')) + '\n</script>' +
             '\n<script type="application/json" id="ct-audio">\n' +
             json.dumps(clips, ensure_ascii=False, separators=(',', ':')) + '\n</script>')
    html = BLOCK_RE.sub('', html).rstrip('\n')
    at = html.find(ANCHOR)
    html = (html[:at] + block + html[at:]) if at > 0 else (html + block + '\n')
    io.open(path, 'w', encoding='utf-8').write(html.rstrip('\n') + '\n')
    print(u'  ฝังข้อมูลและดัชนีไฟล์เสียงลง %s/index.html แล้ว' % COURSE)

    # ตรวจซ้ำว่าบทในหน้าเว็บตรงกับไฟล์บทจริง ๆ
    # เครื่องมือของแบบฝึกฟังชุดเดิมเคยเขียนกลับแค่ดัชนีไฟล์เสียง ทำให้หน้าเว็บ
    # โชว์บทเก่าคู่กับเสียงใหม่โดยไม่มีอะไรจับได้ จึงตรวจทุกครั้งไม่ให้เกิดซ้ำ
    _, again = read_page()
    m = re.search(r'id="ct-data">(.*?)</script>', again, re.S)
    got = {i['id']: i for st in json.loads(m.group(1)) for i in st['items']} if m else {}
    bad = 0
    for st in sets:
        for it in items_of(st):
            a = got.get(it['id'])
            if not a:
                print(u'  %s ไม่มีในหน้าเว็บ' % it['id']); bad += 1; continue
            if [t[1] for t in a['turns']] != [t[2] for t in it['turns']]:
                print(u'  %s บทในหน้าเว็บไม่ตรงกับไฟล์บท' % it['id']); bad += 1
            if [q['q'] for q in a['qs']] != [q['q'] for q in it['questions']]:
                print(u'  %s คำถามในหน้าเว็บไม่ตรงกับไฟล์บท' % it['id']); bad += 1
    print(u'  ตรวจบทในหน้าเว็บเทียบกับไฟล์บท · พบไม่ตรง %d จุด' % bad)


def report(sets):
    print('')
    grand = 0
    for st in sets:
        its = items_of(st)
        n = sum(len(i['questions']) for i in its)
        w = sum(len(t[2].split()) for i in its for t in i['turns'])
        grand += n
        print(u'%-4s %-12s %2d คลิป · %2d ข้อ · %5d คำ' % (st['id'], st['title'], len(its), n, w))
    print(u'\nรวม %d ชุด · %d ข้อ' % (len(sets), grand))


async def main():
    ap = argparse.ArgumentParser(description=u'สร้างแบบฝึกฟังแนว CU-TEP')
    ap.add_argument('--check', action='store_true', help=u'ตรวจอย่างเดียว ไม่สร้างเสียง')
    ap.add_argument('--force', action='store_true', help=u'สร้างใหม่แม้บทไม่เปลี่ยน')
    a = ap.parse_args()

    sets = load_sets()
    if not sets:
        print(u'ยังไม่มีไฟล์ชุดข้อสอบเลย')
        return 1

    print(u'\nตรวจบทและคำถาม')
    problems = audit(sets)
    print(u'  พบปัญหา %d จุด' % problems)
    report(sets)
    if problems:
        print(u'\nต้องแก้ข้อมูลก่อน ยังไม่สร้างเสียงให้')
        return 1
    if a.check:
        return 0

    try:
        import edge_tts                                            # noqa: F401
    except ImportError:
        print(_ma.problem_edge_tts())
        return 1

    os.makedirs(OUTDIR, exist_ok=True)
    old = {} if a.force else old_index()
    clips, made, skipped = {}, 0, 0

    for st in sets:
        print(u'\n%s' % st['title'])
        number = 1
        for it in items_of(st):
            sig = sig_of(it)
            mp3 = os.path.join(OUTDIR, it['id'] + '.mp3')
            prev = old.get(it['id'])
            if prev and prev.get('sig') == sig and os.path.exists(mp3) and not a.force:
                clips[it['id']] = prev
                skipped += 1
                number += len(it['questions'])
                continue

            audio, cues, qcues, dur = await build_item(it, number)
            with open(mp3, 'wb') as f:
                f.write(audio)
            clips[it['id']] = {'src': 'cutep/' + it['id'] + '.mp3', 'dur': dur, 'sig': sig,
                               'cues': cues, 'qcues': qcues, 'from': number}
            made += 1
            number += len(it['questions'])
            sys.stdout.write('\r  %s · %d:%02d   ' % (it['id'], int(dur // 60), int(dur % 60)))
            sys.stdout.flush()
        sys.stdout.write('\n')

    write_page(sets, clips)
    print(u'\nเสร็จแล้ว สร้างใหม่ %d คลิป · ข้าม %d คลิป' % (made, skipped))
    return 0


if __name__ == '__main__':
    try:
        sys.exit(asyncio.run(main()))
    except KeyboardInterrupt:
        print(u'\nยกเลิกแล้ว')
        sys.exit(1)
