# -*- coding: utf-8 -*-
"""แยกข้อความผสมไทย-อังกฤษออกเป็นช่วง ๆ เพื่อให้แต่ละช่วงอ่านด้วยเสียงของภาษานั้น

หลักการ
  ตัวอักษรไทย        → ช่วงภาษาไทย
  ตัวอักษรละติน       → ช่วงภาษาอังกฤษ
  ตัวเลข วรรค เครื่องหมาย → เป็นกลาง เกาะไปกับช่วงที่อยู่ติดกัน

ช่วงอังกฤษที่สั้นมากและไม่ใช่ตัวย่อ จะถูกยุบกลับเข้าช่วงไทย
เพราะการสลับเสียงไปมาถี่เกินไปทำให้ฟังขาดเป็นท่อน ๆ
"""
import re

TH = re.compile(u'[฀-๿]')
EN = re.compile(u'[A-Za-z]')

# คำอังกฤษสั้น ๆ ที่ยังอยากให้อ่านด้วยเสียงอังกฤษ เพราะเป็นศัพท์เฉพาะหรือตัวย่อ
KEEP_SHORT = {
    'by', 'at', 'of', 'to', 'in', 'on', 'if', 'or', 'be', 'is', 'am', 'do',
    'a', 'an', 'the', 'will', 'may', 'can', 'must', 'might', 'could',
    'should', 'would', 'shall', 'from', 'all', 'and', 'not', 'no',
}


def _cls(ch):
    if TH.match(ch):
        return 'th'
    if EN.match(ch):
        return 'en'
    return None


def split_lang(text, min_en_chars=2):
    """คืนลิสต์ของ (lang, ข้อความ) โดย lang เป็น 'th' หรือ 'en'

    min_en_chars คือความยาวขั้นต่ำของช่วงอังกฤษที่จะแยกออกมาจริง
    ถ้าสั้นกว่านี้และไม่ได้เป็นตัวพิมพ์ใหญ่ทั้งหมด จะถูกยุบกลับเข้าช่วงไทย
    """
    if not text:
        return []

    # 1 · ไล่ทีละตัวอักษร เก็บเป็นช่วงดิบ โดยตัวเป็นกลางยังไม่ตัดสิน
    runs = []                      # [lang or None, ข้อความ]
    for ch in text:
        c = _cls(ch)
        if runs and runs[-1][0] == c:
            runs[-1][1] += ch
        else:
            runs.append([c, ch])

    # 2 · ยกช่วงเป็นกลางไปเกาะกับเพื่อนบ้าน
    #     ถ้าฝั่งใดฝั่งหนึ่งเป็นไทย ให้เกาะไทยไว้ก่อน เพราะตัวเลขที่ขนาบด้วยไทย
    #     อย่าง NCI 35,000 หัก ควรอ่านจำนวนเป็นไทย ไม่ใช่ thirty-five thousand
    #     ส่วนตัวเลขที่อยู่กลางประโยคอังกฤษล้วนอย่าง By 2050 จะยังเป็นอังกฤษ
    merged = []
    for i, (lang, s) in enumerate(runs):
        if lang is None:
            left = merged[-1][0] if merged else None
            right = next((l for l, _ in runs[i + 1:] if l is not None), None)
            pick = 'th' if 'th' in (left, right) else (left or right or 'th')
            if merged and merged[-1][0] == pick:
                merged[-1] = (pick, merged[-1][1] + s)
            else:
                merged.append((pick, s))
            continue
        if merged and merged[-1][0] == lang:
            merged[-1] = (lang, merged[-1][1] + s)
        else:
            merged.append((lang, s))

    # 3 · ยุบช่วงอังกฤษที่สั้นเกินไปกลับเข้าไทย เพื่อไม่ให้สลับเสียงถี่จนฟังขาด
    out = []
    for lang, s in merged:
        if lang == 'en':
            letters = ''.join(EN.findall(s))
            word = letters.lower()
            too_short = len(letters) < min_en_chars
            worth_keeping = letters.isupper() or word in KEEP_SHORT
            if too_short and not worth_keeping:
                lang = 'th'
        if out and out[-1][0] == lang:
            out[-1] = (lang, out[-1][1] + s)
        else:
            out.append((lang, s))

    # 4 · ตัดช่วงที่ไม่มีเนื้อเสียงทิ้ง แล้วผนวกอักขระที่เหลือเข้าช่วงก่อนหน้า
    final = []
    for lang, s in out:
        if not s.strip():
            if final:
                final[-1] = (final[-1][0], final[-1][1] + s)
            continue
        if final and final[-1][0] == lang:
            final[-1] = (lang, final[-1][1] + s)
        else:
            final.append((lang, s))
    return final


def preview(text):
    return ' | '.join(u'%s:%s' % (l, s.strip()) for l, s in split_lang(text))
