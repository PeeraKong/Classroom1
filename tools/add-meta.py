#!/usr/bin/env python3
# -*- coding: utf-8 -*-
u"""เติม meta ที่ขาดให้ทุกหน้า แล้วสร้าง sitemap.xml กับ robots.txt

    python3 tools/add-meta.py            แก้จริง
    python3 tools/add-meta.py --check    ตรวจอย่างเดียว ไม่เขียนไฟล์

ที่มาของปัญหา
  ทุกหน้าไม่มี meta viewport เลย ซึ่งบนมือถือจริงจะทำให้เบราว์เซอร์
  วางหน้าเว็บที่ความกว้างราว 980px แล้วย่อลงมาทั้งหน้า ตัวหนังสือจึงเล็กจนอ่านไม่ออก
  ที่ทดสอบแล้วดูปกติเพราะเครื่องมือทดสอบตั้งความกว้างให้โดยตรง ไม่ได้อ่าน meta ตัวนี้

  และไม่มี meta description เลย ทำให้ผลการค้นหาบน search engine
  ไปหยิบข้อความช่วงต้นของหน้ามาแสดงแทน ซึ่งมักเป็นข้อความที่ไม่ได้อธิบายว่าหน้านี้คืออะไร

สิ่งที่เติม  viewport · description · robots · canonical · Open Graph · lang ที่แท็ก html
คร่อมด้วยคอมเมนต์หัวท้าย จึงรันซ้ำได้ไม่ซ้อน และแก้ข้อความแล้วรันใหม่ได้
"""

import argparse
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = u'https://peerakong.github.io/Classroom1/'

START = u'<!-- meta:start -->'
END = u'<!-- meta:end -->'

# หน้า · คำโปรยสำหรับผลการค้นหา · ความถี่ที่เนื้อหาเปลี่ยน · น้ำหนักใน sitemap
PAGES = [
    ('index.html', u'หน้ารวม',
     u'คลังสื่อประกอบการเรียนระดับปริญญาตรี คณะพาณิชยศาสตร์และการบัญชี '
     u'ครอบคลุมการบัญชีขั้นสูง 1 การสอบบัญชี ระบบ ERP หลักการตลาด และภาษาอังกฤษเพื่อการสื่อสาร '
     u'สรุปเป็นภาษาไทย พร้อมแบบทดสอบ เครื่องมือคำนวณ และเสียงบรรยายทุกบท', '1.0'),

    ('adv-acctg-1/index.html', u'การบัญชีขั้นสูง 1',
     u'สื่อประกอบการเรียนการบัญชีขั้นสูง 1 (2601-421) ครบ 10 บท '
     u'บัญชีสำนักงานใหญ่และสาขา การรวมธุรกิจตาม TFRS 3 งบการเงินรวม งบรวมกรณีขาดทุน '
     u'รายการระหว่างบริษัทในเครือ การด้อยค่าของค่าความนิยมตาม TAS 36 กิจการร่วมค้าตาม TFRS 11 '
     u'และบุคคลหรือกิจการที่เกี่ยวข้องกันตาม TAS 24 พร้อมสมุดรายวันคู่ กระดาษทำการ และแบบทดสอบสามชุด', '0.9'),

    ('adv-acctg-1/sheet-4-3.html', u'สรุปชีท 4_3',
     None, '0.9'),   # หน้านี้เขียน meta ครบมาตั้งแต่ต้น จึงข้ามการเติม

    ('audit/index.html', u'การสอบบัญชี',
     u'สื่อประกอบการเรียนวิชาการสอบบัญชี 7 บท มาตรฐานการสอบบัญชี การวางแผนงาน '
     u'การประเมินความเสี่ยง งานให้ความเชื่อมั่น จรรยาบรรณและ IESBA และการเลือกตัวอย่าง '
     u'สรุปเป็นภาษาไทยพร้อมแบบทดสอบและเสียงบรรยาย', '0.8'),

    ('erp/index.html', u'ระบบวางแผนทรัพยากรองค์กร ERP',
     u'สื่อประกอบการเรียนระบบวางแผนทรัพยากรองค์กร ERP และ SAP '
     u'ครอบคลุมแนวคิด ERP สถาปัตยกรรมและผังโมดูล และการใช้งาน SAP '
     u'สรุปเป็นภาษาไทยพร้อมภาพหน้าจอจริงและแบบทดสอบ', '0.8'),

    ('marketing/index.html', u'หลักการตลาด',
     u'สื่อประกอบการเรียนหลักการตลาด อ้างอิง Kotler และ Armstrong 7 บท '
     u'กระบวนการการตลาด 5 ขั้น สภาพแวดล้อมและ PESTLE การวิจัยตลาด พฤติกรรมผู้บริโภค '
     u'กลยุทธ์ STP ผลิตภัณฑ์และตราสินค้า และการพัฒนาสินค้าใหม่กับวงจรชีวิตผลิตภัณฑ์ '
     u'สรุปเป็นภาษาไทยพร้อมแบบทดสอบสองชุดและเสียงบรรยาย', '0.8'),

    ('oral-eng/index.html', u'ภาษาอังกฤษเพื่อการสื่อสาร',
     u'สื่อประกอบการเรียนภาษาอังกฤษเพื่อการสื่อสาร อ้างอิง Market Leader Upper Intermediate '
     u'พร้อมคลังศัพท์ แบบฝึกการฟัง และแนวข้อสอบ CU-TEP', '0.7'),
]


def url_of(rel):
    return BASE + ('' if rel == 'index.html' else rel.replace('index.html', ''))


def block_for(rel, desc):
    u"""ประกอบก้อน meta ของหน้าหนึ่ง"""
    url = url_of(rel)
    title = re.search(r'<title>(.*?)</title>', io.open(
        os.path.join(ROOT, rel), encoding='utf-8').read(), re.S)
    title = title.group(1).strip() if title else u''
    return (START + u'\n'
            u'<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            u'<meta name="description" content="%s">\n'
            u'<meta name="robots" content="index, follow">\n'
            u'<link rel="canonical" href="%s">\n'
            u'<meta property="og:type" content="website">\n'
            u'<meta property="og:locale" content="th_TH">\n'
            u'<meta property="og:title" content="%s">\n'
            u'<meta property="og:description" content="%s">\n'
            u'<meta property="og:url" content="%s">\n'
            % (desc, url, title, desc, url)
            + END)


def patch(rel, desc):
    path = os.path.join(ROOT, rel)
    html = io.open(path, encoding='utf-8').read()
    before = html

    # แท็ก html ที่มี lang ช่วยทั้ง search engine และโปรแกรมอ่านหน้าจอ
    if not re.match(r'\s*<!doctype', html, re.I):
        html = u'<!doctype html>\n<html lang="th">\n' + html
    elif '<html' not in html:
        html = re.sub(r'(<!doctype html>\s*)', r'\1<html lang="th">\n', html, count=1, flags=re.I)

    body = block_for(rel, desc) if desc else None
    if body:
        old = re.search(re.escape(START) + r'.*?' + re.escape(END), html, re.S)
        if old:
            if old.group(0) != body:
                html = html[:old.start()] + body + html[old.end():]
        else:
            anchor = u'<meta charset="utf-8">'
            if html.count(anchor) != 1:
                raise SystemExit(u'หา meta charset ใน %s ไม่เจอ' % rel)
            html = html.replace(anchor, anchor + u'\n' + body)
    return path, html, (html != before)


SITEMAP_HEAD = u'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

ROBOTS = u"""# เปิดให้ search engine เก็บไปทำดัชนีได้ทั้งเว็บ
User-agent: *
Allow: /

Sitemap: %ssitemap.xml
""" % BASE


def build_sitemap(stamp):
    out = [SITEMAP_HEAD]
    for rel, _, _, prio in PAGES:
        out.append(u'  <url>\n    <loc>%s</loc>\n    <lastmod>%s</lastmod>\n'
                   u'    <priority>%s</priority>\n  </url>\n'
                   % (url_of(rel), stamp, prio))
    out.append(u'</urlset>\n')
    return u''.join(out)


def verify(pairs):
    bad = 0
    for rel, html in pairs:
        for need in ('name="viewport"', 'name="description"', 'rel="canonical"', 'lang="th"'):
            if need not in html:
                print(u'  %-28s ขาด %s' % (rel, need)); bad += 1
        # คำโปรยที่ยาวเกินราว 160 ตัวอักษร search engine จะตัดท้ายทิ้ง
        m = re.search(r'<meta name="description" content="([^"]*)"', html)
        if m:
            n = len(m.group(1))
            flag = u'' if n <= 320 else u'  <<< ยาวไป อาจถูกตัด'
            print(u'  %-28s คำโปรย %3d อักษร%s' % (rel, n, flag))
        if html.count('name="viewport"') != 1:
            print(u'  %-28s viewport ซ้ำ %d ครั้ง' % (rel, html.count('name="viewport"'))); bad += 1
    return bad


def main():
    ap = argparse.ArgumentParser(description=u'เติม meta และสร้าง sitemap')
    ap.add_argument('--check', action='store_true', help=u'ตรวจอย่างเดียว ไม่เขียนไฟล์')
    a = ap.parse_args()

    import datetime
    stamp = datetime.date.today().isoformat()

    writes, pairs, changed = [], [], 0
    for rel, name, desc, _ in PAGES:
        path, html, did = patch(rel, desc)
        writes.append((path, html))
        pairs.append((rel, html))
        changed += 1 if did else 0
        print(u'%-28s %s' % (rel, u'เติมแล้ว' if did else u'ครบอยู่แล้ว'))

    print(u'\nตรวจหลังแก้')
    bad = verify(pairs)
    if bad:
        print(u'\nตรวจพบปัญหา %d จุด จึงยังไม่เขียนไฟล์' % bad)
        return 1
    if a.check:
        print(u'\nตรวจผ่าน · ยังไม่เขียนไฟล์เพราะสั่ง --check')
        return 0
    for path, html in writes:
        io.open(path, 'w', encoding='utf-8').write(html)
    io.open(os.path.join(ROOT, 'sitemap.xml'), 'w', encoding='utf-8').write(build_sitemap(stamp))
    io.open(os.path.join(ROOT, 'robots.txt'), 'w', encoding='utf-8').write(ROBOTS)
    print(u'\nแก้ %d หน้า · เขียน sitemap.xml (%d url) และ robots.txt แล้ว'
          % (changed, len(PAGES)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
