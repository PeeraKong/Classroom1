#!/usr/bin/env python3
# -*- coding: utf-8 -*-
u"""วางบทบรรยายชุดใหม่ลงบล็อก JSON id="cn-data" โดยเรียงตามหัวข้อจริงในหน้า

    python3 tools/make-narration.py marketing tools/marketing-narration-1.py ...
    python3 tools/make-narration.py marketing tools/*.py --check

ต่างจาก tools/patch-narration.py ตรงที่ตัวนั้นแทนที่ได้อย่างเดียวและอ้างด้วยลำดับ
ซึ่งใช้ไม่ได้เมื่อหัวข้อในหน้ามีมากกว่าจำนวนบทพูดที่มีอยู่ ตัวนี้จึง
  อ้างด้วยรหัสหัวข้อ เช่น m1-5 ไม่ใช่ลำดับ จึงไม่เลื่อนเมื่อเพิ่มหัวข้อใหม่
  เพิ่มบทพูดให้หัวข้อที่ยังไม่เคยมีได้
  เรียงลำดับใหม่ตามลำดับหัวข้อที่ปรากฏจริงในหน้า ไม่ใช่ตามลำดับที่เขียนในไฟล์
  ดึงชื่อหัวข้อมาจาก h2 ในหน้า จึงไม่มีทางหลุดจากกัน

รูปแบบไฟล์ข้อมูล
    NARRATION = {'m1': {'mode': 'replace', 'blocks': [('m1-1', [u'...', ...]), ...]}}
  mode replace  ใช้เฉพาะรายการที่ให้มา ทิ้งของเดิมทั้งบท
  mode merge    เอาของใหม่รวมกับของเดิม ของใหม่ทับของเดิมถ้าชี้หัวข้อเดียวกัน
"""

import argparse
import importlib.util
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLOCK_RE = re.compile(r'(<script type="application/json" id="cn-data">\n)(.*?)(\n</script>)', re.S)

# ตัวอ่านออกเสียงอ่านสัญลักษณ์พวกนี้ไม่ออก หรืออ่านแล้วเพี้ยน
BAD_CHARS = u'%$€£¥&@#*/\\<>[]{}|~^+='


def load(path):
    name = os.path.splitext(os.path.basename(path))[0].replace('-', '_')
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return getattr(mod, 'NARRATION', None)


def page_sections(html, ch):
    u"""รหัสหัวข้อกับชื่อหัวข้อตามลำดับที่ปรากฏจริงในหน้า"""
    panel = re.search(r'<div id="%s"[^>]*role="tabpanel".*?(?=\n  <div id="\w+"[^>]*role="tabpanel"|\n  </main>)'
                      % ch, html, re.S)
    if not panel:
        return []
    out = []
    for m in re.finditer(r'<section class="sec" id="(%s-\d+)">.*?<h2>(.*?)</h2>' % ch,
                         panel.group(0), re.S):
        out.append((m.group(1), re.sub(r'<[^>]+>', '', m.group(2)).strip()))
    return out


def check_text(ch, sid, lines):
    bad = 0
    for i, s in enumerate(lines):
        if not s.strip():
            print(u'  %-6s ย่อหน้าที่ %d ว่างเปล่า' % (sid, i + 1)); bad += 1
        hit = [c for c in BAD_CHARS if c in s]
        if hit:
            print(u'  %-6s ย่อหน้าที่ %d มีสัญลักษณ์ที่อ่านออกเสียงไม่ได้ %s'
                  % (sid, i + 1, ' '.join(hit))); bad += 1
        if len(s) > 400:
            print(u'  %-6s ย่อหน้าที่ %d ยาว %d อักษร ควรตัดให้สั้นลง'
                  % (sid, i + 1, len(s))); bad += 1
    return bad


def main():
    ap = argparse.ArgumentParser(description=u'วางบทบรรยายชุดใหม่ลงหน้าวิชา')
    ap.add_argument('course', help=u'โฟลเดอร์ของวิชา เช่น marketing')
    ap.add_argument('files', nargs='+', help=u'ไฟล์ข้อมูลที่มีตัวแปร NARRATION')
    ap.add_argument('--check', action='store_true', help=u'ตรวจอย่างเดียว ไม่เขียนไฟล์')
    a = ap.parse_args()

    path = os.path.join(ROOT, a.course, 'index.html')
    html = io.open(path, encoding='utf-8').read()
    m = BLOCK_RE.search(html)
    if not m:
        print(u'หาบล็อก cn-data ใน %s ไม่เจอ' % path)
        return 1
    data = json.loads(m.group(2))

    patch = {}
    for f in a.files:
        got = load(f)
        if not got:
            continue
        for ch, spec in got.items():
            if ch in patch:
                print(u'บท %s ถูกกำหนดซ้ำในหลายไฟล์' % ch)
                return 1
            patch[ch] = spec

    if not patch:
        print(u'ไม่พบตัวแปร NARRATION ในไฟล์ที่ให้มา')
        return 1

    bad = 0
    for ch, spec in sorted(patch.items()):
        if ch not in data:
            print(u'ไม่มีบท %s ในวิชานี้' % ch); bad += 1; continue
        secs = page_sections(html, ch)
        order = {sid: i for i, (sid, _t) in enumerate(secs)}
        titles = dict(secs)

        new = {}
        for sid, lines in spec['blocks']:
            if sid not in order:
                print(u'  %-6s ไม่มีหัวข้อนี้ในหน้า' % sid); bad += 1; continue
            bad += check_text(ch, sid, lines)
            new[sid] = list(lines)

        keep = {}
        if spec.get('mode', 'merge') == 'merge':
            for b in data[ch]['c']:
                if b['s'] not in new and b['s'] in order:
                    keep.setdefault(b['s'], b['t'])

        merged = dict(keep)
        merged.update(new)
        blocks = [{'h': titles[s], 's': s, 't': merged[s]}
                  for s in sorted(merged, key=lambda x: order[x])]

        before = sum(len(x) for b in data[ch]['c'] for x in b['t'])
        after = sum(len(x) for b in blocks for x in b['t'])
        uncovered = [s for s, _t in secs if s not in merged]
        print(u'%-4s %2d → %2d หัวข้อ · %6d → %6d อักษร · ยังไม่มีบทพูด %s'
              % (ch, len(data[ch]['c']), len(blocks), before, after,
                 ' '.join(uncovered) or u'ครบทุกหัวข้อ'))
        if not a.check:
            data[ch]['c'] = blocks

    if bad:
        print(u'\nตรวจพบปัญหา %d จุด จึงยังไม่เขียนไฟล์' % bad)
        return 1
    if a.check:
        return 0

    out = json.dumps(data, ensure_ascii=False, separators=(',', ':'))
    io.open(path, 'w', encoding='utf-8').write(
        html[:m.start(2)] + out + html[m.end(2):])
    total = sum(len(x) for v in data.values() for b in v['c'] for x in b['t'])
    print(u'\nเขียนบทบรรยายลง %s/index.html แล้ว · รวมทั้งวิชา %d อักษร' % (a.course, total))
    print(u'ไฟล์เสียงเดิมจะไม่ตรงกับบทแล้ว ต้องสร้างใหม่ด้วย tools/make-audio.py')
    return 0


if __name__ == '__main__':
    sys.exit(main())
