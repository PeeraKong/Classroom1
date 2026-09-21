#!/usr/bin/env python3
# -*- coding: utf-8 -*-
u"""วางบทบรรยายชุดใหม่ทับของเดิมในบล็อก JSON id="cn-data"

บทบรรยายของทุกวิชาฝังอยู่ในหน้า HTML ซึ่งแก้ด้วยมือแล้วพังง่าย
สคริปต์นี้จึงรับชุดแก้จากไฟล์ข้อมูลแยก แล้ววางทับเฉพาะหัวข้อที่ระบุไว้

    python3 tools/patch-narration.py audit tools/audit-narration-1.py ...

ใช้ --check เพื่อดูว่าจะเปลี่ยนอะไรบ้างโดยไม่เขียนไฟล์
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


def load_patch(path):
    name = os.path.splitext(os.path.basename(path))[0].replace('-', '_')
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.PATCH


def main():
    ap = argparse.ArgumentParser(description=u'วางบทบรรยายชุดใหม่ทับของเดิม')
    ap.add_argument('course', help=u'โฟลเดอร์ของวิชา เช่น audit')
    ap.add_argument('patches', nargs='+', help=u'ไฟล์ชุดแก้ที่มีตัวแปร PATCH')
    ap.add_argument('--check', action='store_true', help=u'ดูผลอย่างเดียว ไม่เขียนไฟล์')
    a = ap.parse_args()

    path = os.path.join(ROOT, a.course, 'index.html')
    html = io.open(path, encoding='utf-8').read()
    m = BLOCK_RE.search(html)
    if not m:
        print(u'หาบล็อก cn-data ใน %s ไม่เจอ' % path)
        return 1
    data = json.loads(m.group(2))

    patch = {}
    for p in a.patches:
        for k, v in load_patch(p).items():
            if k in patch:
                print(u'ชุดแก้ซ้ำกันที่ %s หัวข้อ %d' % k)
                return 1
            patch[k] = v

    # ตรวจก่อนแตะข้อมูลว่าทุกคีย์ชี้ไปยังหัวข้อที่มีอยู่จริง
    bad = 0
    for ch, idx in patch:
        if ch not in data:
            print(u'ไม่มีบท %s ในวิชานี้' % ch)
            bad += 1
        elif idx >= len(data[ch]['c']):
            print(u'บท %s มีแค่ %d หัวข้อ แต่ชุดแก้อ้างถึงหัวข้อที่ %d'
                  % (ch, len(data[ch]['c']), idx))
            bad += 1
    if bad:
        return 1

    before = {k: sum(len(x) for s in v['c'] for x in s['t']) for k, v in data.items()}
    hit = 0
    for (ch, idx), lines in sorted(patch.items()):
        sec = data[ch]['c'][idx]
        old = sec['t']
        if old == lines:
            print(u'  %-4s %-44s เหมือนเดิม ไม่ต้องแก้' % (ch, sec['h'][:44]))
            continue
        print(u'  %-4s %-44s %2d → %2d ย่อหน้า · %5d → %5d ตัวอักษร'
              % (ch, sec['h'][:44], len(old), len(lines),
                 sum(len(x) for x in old), sum(len(x) for x in lines)))
        sec['t'] = lines
        hit += 1

    after = {k: sum(len(x) for s in v['c'] for x in s['t']) for k, v in data.items()}
    print('')
    for k in data:
        if before[k] != after[k]:
            print(u'%-4s %-46s %6d → %6d ตัวอักษร  เพิ่ม %d เปอร์เซ็นต์'
                  % (k, data[k]['t'][:46], before[k], after[k],
                     round((after[k] - before[k]) * 100.0 / before[k])))
    tb, ta = sum(before.values()), sum(after.values())
    print(u'\nรวมทั้งวิชา %d → %d ตัวอักษร · แก้ %d หัวข้อ' % (tb, ta, hit))

    if a.check:
        print(u'\nโหมดตรวจอย่างเดียว ยังไม่ได้เขียนไฟล์')
        return 0

    body = json.dumps(data, ensure_ascii=False, separators=(',', ':'))
    html = html[:m.start(2)] + body + html[m.end(2):]
    io.open(path, 'w', encoding='utf-8').write(html)
    print(u'เขียน %s/index.html แล้ว' % a.course)
    return 0


if __name__ == '__main__':
    sys.exit(main())
