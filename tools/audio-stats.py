#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""นับจำนวนบท ความยาว และขนาดของไฟล์เสียงบรรยายทุกวิชา

    python3 tools/audio-stats.py            สรุปรายวิชา
    python3 tools/audio-stats.py --chapters  ไล่ทีละบท
    python3 tools/audio-stats.py --markdown  พิมพ์ตารางพร้อมแปะลง README

มีไว้เพราะตารางสรุปไฟล์เสียงใน README เคยค้างอยู่หลายหน่วย
คือเพิ่มบทใหม่ไปแล้วแต่ตารางยังบอกเลขเดิม ซึ่งไม่มีใครจับได้เพราะไม่มีอะไรตรวจ
ตัวเลขทุกตัวที่นี่อ่านจาก cn-audio ในหน้าเว็บ ซึ่งเป็นตัวเดียวกับที่เครื่องเล่นใช้
และจากขนาดไฟล์บนดิสก์จริง ไม่ได้พิมพ์ตามความจำ

ถ้าจะแก้ตารางใน README ให้รันด้วย --markdown แล้วคัดลอกไปแปะ
"""

import argparse
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ชื่อวิชาเรียงตามลำดับที่ปรากฏในหน้าแรก
COURSES = [
    ('adv-acctg-1', u'การบัญชีขั้นสูง 1'),
    ('audit',       u'การสอบบัญชี'),
    ('erp',         u'ERP'),
    ('marketing',   u'หลักการตลาด'),
    ('oral-eng',    u'ภาษาอังกฤษเพื่อการสื่อสาร'),
]

DATA_RE  = re.compile(r'<script type="application/json" id="cn-data">(.*?)</script>', re.S)
AUDIO_RE = re.compile(r'<script type="application/json" id="cn-audio">(.*?)</script>', re.S)
MB = 1048576.0


def mmss(sec):
    """ปัดวินาทีรวมก่อนแล้วค่อยหาร ไม่ใช่ปัดเศษวินาทีทีหลัง

    ถ้าปัดทีหลังจะได้ผลอย่าง 368:60 ซึ่งไม่ใช่เวลาที่มีอยู่จริง
    """
    s = int(round(sec))
    return u'%d:%02d' % (s // 60, s % 60)


def hhmm(sec):
    h = int(sec // 3600)
    m = int(round((sec - h * 3600) / 60.0))
    if m == 60:
        h, m = h + 1, 0
    return u'%d ชั่วโมง %d นาที' % (h, m)


def read_course(slug):
    path = os.path.join(ROOT, slug, 'index.html')
    if not os.path.exists(path):
        return None
    html = io.open(path, encoding='utf-8').read()
    md = DATA_RE.search(html)
    ma = AUDIO_RE.search(html)
    return (json.loads(md.group(1)) if md else {},
            json.loads(ma.group(1)) if ma else {})


def main():
    ap = argparse.ArgumentParser(description=u'สรุปไฟล์เสียงบรรยายทุกวิชา')
    ap.add_argument('--chapters', action='store_true', help=u'ไล่ทีละบท')
    ap.add_argument('--markdown', action='store_true', help=u'พิมพ์ตารางแบบ markdown')
    a = ap.parse_args()

    rows, longest = [], None
    tot = {'ch': 0, 'sec': 0, 'para': 0, 'dur': 0.0, 'size': 0}
    problems = []

    for slug, name in COURSES:
        got = read_course(slug)
        if got is None:
            problems.append(u'ไม่พบ %s/index.html' % slug)
            continue
        narration, clips = got

        secs = paras = 0
        for key, ch in narration.items():
            for cue in ch.get('c', []):
                secs += 1
                paras += len(cue.get('t', []))

        n = 0
        dur = 0.0
        size = 0
        chapters = []
        for key, clip in sorted(clips.items()):
            mp3 = os.path.join(ROOT, slug, clip['src'])
            if not os.path.exists(mp3):
                problems.append(u'%s บท %s มีรายการเสียงแต่ไม่มีไฟล์ %s'
                                % (slug, key, clip['src']))
                continue
            bytes_ = os.path.getsize(mp3)
            n += 1
            dur += clip['dur']
            size += bytes_
            title = (narration.get(key) or {}).get('s') or ''
            chapters.append((key, title, clip['dur'], bytes_))
            if longest is None or clip['dur'] > longest[2]:
                longest = (slug, key, clip['dur'], bytes_, title,
                           sum(len(c.get('t', []))
                               for c in (narration.get(key) or {}).get('c', [])))

        # บทที่เขียนบทบรรยายไว้แล้วแต่ยังไม่มีรายการเสียงเลย
        for key in narration:
            if key not in clips:
                problems.append(u'%s บท %s มีบทบรรยายแต่ยังไม่มีไฟล์เสียง' % (slug, key))

        rows.append((name, n, secs, dur, size, chapters))
        tot['ch'] += n
        tot['sec'] += secs
        tot['para'] += paras
        tot['dur'] += dur
        tot['size'] += size

    if a.markdown:
        print(u'> **%d บท · รวม %s · %.1f MB**' % (tot['ch'], hhmm(tot['dur']), tot['size'] / MB))
        print(u'>')
        print(u'> | วิชา | จำนวนบท | หัวข้อ | ความยาว | ขนาด |')
        print(u'> |---|---|---|---|---|')
        for name, n, secs, dur, size, _ in rows:
            print(u'> | %s | %d | %d | %s | %.1f MB |' % (name, n, secs, mmss(dur), size / MB))
        if longest:
            print(u'>')
            print(u'> บทที่ยาวที่สุดคือ **%s** ยาว %s %d ย่อหน้า ไฟล์เดียว %.1f MB'
                  % (longest[4] or longest[1], hhmm(longest[2]), longest[5], longest[3] / MB))
        print(u'\nบรรทัดสรุปบทบรรยาย  %d บท %s หัวข้อ %s ย่อหน้า %d นาที'
              % (tot['ch'], '{:,}'.format(tot['sec']), '{:,}'.format(tot['para']),
                 int(round(tot['dur'] / 60.0))))
    else:
        print(u'%-28s %4s %6s %9s %10s' % (u'วิชา', u'บท', u'หัวข้อ', u'ความยาว', u'ขนาด'))
        print(u'-' * 61)
        for name, n, secs, dur, size, chapters in rows:
            print(u'%-28s %4d %6d %9s %9.1f MB' % (name, n, secs, mmss(dur), size / MB))
            if a.chapters:
                for key, title, d, b in chapters:
                    print(u'      %-6s %-34s %8s %8.1f MB'
                          % (key, title[:34], mmss(d), b / MB))
        print(u'-' * 61)
        print(u'%-28s %4d %6d %9s %9.1f MB'
              % (u'รวม', tot['ch'], tot['sec'], mmss(tot['dur']), tot['size'] / MB))
        print(u'\nรวม %d บท · %s · %.1f MB · บทบรรยาย %s ย่อหน้า'
              % (tot['ch'], hhmm(tot['dur']), tot['size'] / MB, '{:,}'.format(tot['para'])))
        if longest:
            print(u'บทที่ยาวที่สุด  %s บท %s · %s · %d ย่อหน้า'
                  % (longest[0], longest[1], hhmm(longest[2]), longest[5]))

    if problems:
        print(u'\nเรื่องที่ต้องดู')
        for p in problems:
            print(u'  · %s' % p)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
