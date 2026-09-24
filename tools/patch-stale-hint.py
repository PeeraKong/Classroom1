#!/usr/bin/env python3
# -*- coding: utf-8 -*-
u"""บอกให้ชัดเมื่อเครื่องเล่นถอยไปใช้เสียงเบราว์เซอร์เพราะไฟล์เสียงยังเป็นบทเก่า

    python3 tools/patch-stale-hint.py            แก้จริง
    python3 tools/patch-stale-hint.py --check    ตรวจอย่างเดียว

ที่มาของปัญหา
  clipOf() ปฏิเสธไฟล์เสียงที่จำนวนช่วงไม่ตรงกับจำนวนย่อหน้า ซึ่งถูกแล้ว
  เพราะกันไม่ให้เสียงพูดคนละเรื่องกับตัวหนังสือ
  แต่ตอนถอยไปใช้เสียงสังเคราะห์ หน้าเว็บขึ้นข้อความว่า
  เครื่องนี้มีแต่เสียงผู้หญิง แล้วแนะให้ไปรันไฟล์สร้างเสียงในเครื่อง
  ซึ่งไม่ใช่สาเหตุจริง และผู้ใช้ก็งงว่าทำไมเสียงเปลี่ยนจากผู้ชายเป็นผู้หญิงเฉย ๆ

สิ่งที่แก้
  clipOf() ตั้งธง clipStale เมื่อไฟล์มีอยู่แต่เป็นของบทรุ่นก่อน
  แล้วเพิ่มข้อความที่ตรงกับสาเหตุนั้นจริง ๆ

เครื่องเล่นเป็นโค้ดชุดเดียวกันทุกวิชา จึงแก้ทั้งแม่แบบและทุกหน้าวิชาพร้อมกัน
"""

import argparse
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TARGETS = ['audio.template.html', 'adv-acctg-1/index.html', 'audit/index.html',
           'erp/index.html', 'marketing/index.html', 'oral-eng/index.html']

OLD_CLIP = u"""  var audioEl = null, clip = null, clipFailed = null;
  function clipOf(key){
    var c = CLIPS[key];
    if (!c || !c.src || !c.cues) return null;
    var n = 0;
    (DATA[key].c || []).forEach(function(q){ n += (q.t || []).length; });
    return c.cues.length === n ? c : null;   // ไฟล์เสียงต้องตรงกับบทบรรยายรุ่นปัจจุบัน
  }"""

NEW_CLIP = u"""  var audioEl = null, clip = null, clipFailed = null, clipStale = false;
  function clipOf(key){
    clipStale = false;
    var c = CLIPS[key];
    if (!c || !c.src || !c.cues) return null;
    var n = 0;
    (DATA[key].c || []).forEach(function(q){ n += (q.t || []).length; });
    if (c.cues.length === n) return c;       // ไฟล์เสียงต้องตรงกับบทบรรยายรุ่นปัจจุบัน
    clipStale = true;                        // มีไฟล์อยู่ แต่สร้างจากบทรุ่นก่อน
    return null;
  }"""

OLD_HINT = u"""          'มันจะเปิดหน้าเว็บผ่าน <code>http://localhost</code> ให้ แล้วเสียงผู้ชายจะเล่นได้ทันที';
        hintEl.hidden = false;
      }
    }"""

NEW_HINT = u"""          'มันจะเปิดหน้าเว็บผ่าน <code>http://localhost</code> ให้ แล้วเสียงผู้ชายจะเล่นได้ทันที';
        hintEl.hidden = false;
      } else if (clipStale){
        // บทถูกแก้หลังจากสร้างไฟล์เสียง ไฟล์เดิมจึงพูดคนละเรื่องกับตัวหนังสือที่เห็น
        // ต้องบอกสาเหตุจริงตรงนี้ ไม่งั้นจะไปโดนข้อความของ loadVoices ที่บอกว่า
        // เครื่องนี้มีแต่เสียงผู้หญิง ซึ่งไม่ใช่สาเหตุ และทำให้เข้าใจผิดว่าเครื่องมีปัญหา
        hintEl.innerHTML = '<b>บทบรรยายของบทนี้เพิ่งถูกแก้ ไฟล์เสียงผู้ชายที่มีอยู่จึงยังเป็นบทเก่า</b><br>' +
          'หน้านี้ตั้งใจไม่เล่นไฟล์เก่าให้ เพราะจะกลายเป็นเสียงพูดคนละเรื่องกับตัวหนังสือ<br>' +
          'ระหว่างนี้จึงใช้เสียงสังเคราะห์ของเบราว์เซอร์ไปก่อน ซึ่งเครื่องส่วนใหญ่มีแต่เสียงผู้หญิง<br>' +
          'พอสร้างไฟล์เสียงชุดใหม่เสร็จ เสียงผู้ชาย Niwat จะกลับมาเองและกล่องนี้จะหายไป';
        hintEl.hidden = false;
      }
    }"""

PAIRS = [(OLD_CLIP, NEW_CLIP), (OLD_HINT, NEW_HINT)]


def main():
    ap = argparse.ArgumentParser(description=u'เพิ่มคำอธิบายกรณีไฟล์เสียงเป็นบทเก่า')
    ap.add_argument('--check', action='store_true', help=u'ตรวจอย่างเดียว ไม่เขียนไฟล์')
    a = ap.parse_args()

    bad = 0
    for rel in TARGETS:
        path = os.path.join(ROOT, rel)
        html = io.open(path, encoding='utf-8').read()
        if 'clipStale' in html:
            print(u'%-26s แก้ไปแล้ว ข้าม' % rel)
            continue
        out, hit = html, 0
        for old, new in PAIRS:
            if out.count(old) != 1:
                print(u'%-26s หาโค้ดเดิมไม่เจอ หรือเจอมากกว่าหนึ่งที่ (%d)'
                      % (rel, out.count(old)))
                bad += 1
                break
            out = out.replace(old, new)
            hit += 1
        if hit != len(PAIRS):
            continue
        if not a.check:
            io.open(path, 'w', encoding='utf-8').write(out)
        print(u'%-26s %s' % (rel, u'ตรวจแล้วแก้ได้' if a.check else u'แก้แล้ว'))

    if bad:
        print(u'\nมี %d ไฟล์ที่โค้ดไม่ตรงกับที่คาด จึงไม่ได้แก้' % bad)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
