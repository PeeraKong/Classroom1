#!/usr/bin/env python3
# -*- coding: utf-8 -*-
u"""วางแท็บแบบฝึกฟังแนว CU-TEP ลงหน้าวิชาภาษาอังกฤษ

แยกจาก tools/make-cutep.py เพราะคนละหน้าที่กัน
  make-cutep  สร้างไฟล์เสียงและฝังข้อมูลข้อสอบ
  cutep-tab   วางปุ่มแท็บ สารบัญข้าง เนื้อหา สไตล์ และสคริปต์ของหน้า

    python3 tools/cutep-tab.py            วางลงหน้าเว็บ
    python3 tools/cutep-tab.py --check    ดูผลอย่างเดียว

รันซ้ำได้ ส่วนที่วางไปแล้วจะถูกข้าม
"""

import argparse
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGE = os.path.join(ROOT, 'oral-eng', 'index.html')

TAB = (u'    <button class="tab" role="tab" id="t-ct" aria-controls="ct" aria-selected="false">'
       u'<span class="tnum">C</span>CU-TEP</button>\n')
TAB_ANCHOR = u'    <button class="tab" role="tab" id="t-vc"'

RAIL = u'''    <nav id="rail-ct" class="hidden" aria-label="ชุดข้อสอบ CU-TEP">
      <div class="rail-h">CU-TEP · 5 ชุด</div>
      <ol>
        <li><a href="#cts-C1"><i>1</i>ชุดที่ 1 · 30 ข้อ</a></li>
        <li><a href="#cts-C2"><i>2</i>ชุดที่ 2 · 30 ข้อ</a></li>
        <li><a href="#cts-C3"><i>3</i>ชุดที่ 3 · 30 ข้อ</a></li>
        <li><a href="#cts-C4"><i>4</i>ชุดที่ 4 · 30 ข้อ</a></li>
        <li><a href="#cts-C5"><i>5</i>ชุดที่ 5 · 30 ข้อ</a></li>
      </ol>
    </nav>
'''
RAIL_ANCHOR = u'    <nav id="rail-vc"'

SECTION = u'''  <div id="ct" class="hidden" role="tabpanel" aria-labelledby="t-ct" style="--accent:var(--steel); --accent-soft:var(--steel-soft)">
    <p class="lede">แบบฝึกฟัง<b>แนว CU-TEP</b> · <b>5 ชุด ชุดละ 30 ข้อ 30 คะแนน รวม 150 ข้อ</b> · โครงสร้างตามข้อสอบจริง คือ <b>บทสนทนาสั้น 15 ข้อ · บทสนทนายาว 9 ข้อ · บรรยายเดี่ยว 6 ข้อ</b></p>

    <div class="note key" style="margin-bottom:18px"><span class="nh">จุดที่ต่างจากแท็บฝึกฟังของวิชา</span>ในข้อสอบจริง <b>คำถามถูกพูดอยู่ในไฟล์เสียง ไม่ได้พิมพ์ไว้ให้อ่านก่อน</b> ผู้สอบเห็นแต่ตัวเลือกสี่ข้อ แท็บนี้จึง<b>ซ่อนคำถามไว้ตามค่าเริ่มต้น</b> ให้ฟังเอาเองเหมือนของจริง · และ<b>ฟังได้รอบเดียว</b> ปุ่มเล่นจะล็อกหลังเล่นจบ ถ้าอยากฝึกแบบผ่อนคลายกว่านั้นให้กดปุ่มด้านล่างเพื่อปลดล็อก</div>

    <div class="ct-bar">
      <div class="ct-row">
        <span class="ct-lab">โหมด</span>
        <button type="button" id="ct-exam" aria-pressed="true">เหมือนสอบจริง · ฟังรอบเดียว</button>
        <button type="button" id="ct-showq" aria-pressed="false">แสดงคำถามเป็นตัวหนังสือ</button>
        <button type="button" id="ct-script" aria-pressed="false">เปิดบทพูด</button>
      </div>
      <div class="ct-row">
        <span class="ct-lab">ชุด</span>
        <span class="ct-sets" id="ct-sets"></span>
        <span class="ct-count" id="ct-count"></span>
      </div>
    </div>

    <div id="ct-root"></div>
  </div>

'''
SECTION_ANCHOR = u'  <div id="vc" class="hidden" role="tabpanel"'

CSS = u'''
/* ---------- แท็บ CU-TEP ---------- */
.ct-bar{border:1px solid var(--rule); border-radius:5px; background:var(--surface);
  padding:11px 14px; margin-bottom:20px; display:flex; flex-direction:column; gap:8px}
.ct-row{display:flex; flex-wrap:wrap; gap:6px; align-items:center}
.ct-lab{font-family:"IBM Plex Mono",monospace; font-size:.67rem; letter-spacing:.12em;
  text-transform:uppercase; color:var(--ink-3); margin-right:3px}
.ct-bar button{appearance:none; font:inherit; font-size:.78rem; cursor:pointer; padding:4px 11px;
  border:1px solid var(--rule-strong); background:var(--paper); color:var(--ink-2); border-radius:3px}
.ct-bar button:hover{border-color:var(--accent); color:var(--accent)}
.ct-bar button[aria-pressed="true"]{background:var(--accent); border-color:var(--accent);
  color:var(--paper); font-weight:600}
.ct-count{margin-left:auto; font-family:"IBM Plex Mono",monospace; font-size:.75rem;
  color:var(--ink-3); font-variant-numeric:tabular-nums}

.ct-set{border:1px solid var(--rule); border-radius:6px; background:var(--surface);
  margin:0 0 22px; overflow:hidden; box-shadow:var(--shadow)}
.ct-sh{display:flex; align-items:baseline; gap:12px; flex-wrap:wrap;
  padding:13px 18px; background:var(--surface-2); border-bottom:1px solid var(--rule)}
.ct-sh h3{font-family:"Noto Serif Thai",Georgia,serif; font-size:1.05rem; font-weight:700; margin:0}
.ct-sh .sc{margin-left:auto; font-family:"IBM Plex Mono",monospace; font-size:.78rem;
  color:var(--ink-2); font-variant-numeric:tabular-nums}
.ct-sh .sc b{color:var(--ink)}

.ct-sec{padding:14px 18px 6px}
.ct-sec + .ct-sec{border-top:1px solid var(--rule)}
.ct-sech{display:flex; align-items:baseline; gap:10px; flex-wrap:wrap; margin-bottom:4px}
.ct-kind{font-family:"IBM Plex Mono",monospace; font-size:.64rem; letter-spacing:.12em;
  text-transform:uppercase; color:var(--paper); background:var(--accent);
  border-radius:3px; padding:2px 8px}
.ct-sech h4{font-family:"IBM Plex Sans Thai",sans-serif; font-size:.97rem; font-weight:700; margin:0}
.ct-sech .n{margin-left:auto; font-family:"IBM Plex Mono",monospace; font-size:.72rem; color:var(--ink-3)}
.ct-dir{font-size:.85rem; color:var(--ink-2); font-style:italic; margin:0 0 10px}

.ct-item{border-top:1px solid var(--rule); padding:12px 0 14px}
.ct-item:first-of-type{border-top:0}
.ct-head{display:flex; align-items:center; gap:10px; flex-wrap:wrap; margin-bottom:8px}
.ct-no{font-family:"IBM Plex Mono",monospace; font-size:.74rem; font-weight:600; color:var(--accent)}
.ct-title{font-size:.9rem; font-weight:600}
.ct-ctx{font-size:.83rem; color:var(--ink-3); flex:1 1 100%}
.ct-item audio{width:100%; display:block; margin:4px 0 10px}
.ct-missing{font-size:.85rem; color:var(--ink-3); border:1px dashed var(--rule-strong);
  border-radius:4px; padding:11px 13px; margin-bottom:10px}

.ct-q{margin-top:11px}
.ct-q + .ct-q{border-top:1px dashed var(--rule); padding-top:11px}
.ct-qt{font-size:.9rem; font-weight:600; margin-bottom:7px; display:flex; gap:9px}
.ct-qt i{font-style:normal; font-family:"IBM Plex Mono",monospace; font-size:.74rem;
  color:var(--accent); padding-top:2px; flex:0 0 auto}
.ct-qt.hidden-q span{color:var(--ink-3); font-weight:400; font-style:italic}
.ct-opts{display:flex; flex-direction:column; gap:5px}
.ct-opt{appearance:none; font:inherit; font-size:.87rem; text-align:left; cursor:pointer;
  padding:7px 12px; border:1px solid var(--rule); background:var(--paper);
  color:var(--ink-2); border-radius:4px; line-height:1.5}
.ct-opt:hover:not(:disabled){border-color:var(--accent); color:var(--ink)}
.ct-opt:disabled{cursor:default}
.ct-opt.ok{border-color:var(--teal); background:var(--teal-soft); color:var(--ink); font-weight:600}
.ct-opt.no{border-color:var(--red-ink); background:var(--red-soft); color:var(--ink)}
.ct-exp{margin-top:7px; font-size:.83rem; color:var(--ink-2);
  border-left:2px solid var(--rule-strong); padding-left:11px; line-height:1.6}

.ct-script{margin-top:10px; font-size:.86rem; line-height:1.75}
.ct-line{margin-bottom:6px; display:flex; gap:10px; align-items:baseline}
.ct-who{flex:0 0 74px; font-family:"IBM Plex Mono",monospace; font-size:.72rem;
  font-weight:600; color:var(--accent); text-align:right}
.ct-said{color:var(--ink-2)}
.ct-line.cur .ct-said{color:var(--ink); background:var(--accent-soft); border-radius:3px;
  box-shadow:0 0 0 3px var(--accent-soft)}

.ct-foot{display:flex; flex-wrap:wrap; gap:8px; align-items:center;
  padding:12px 18px; background:var(--surface-2); border-top:1px solid var(--rule)}
.ct-foot button{appearance:none; font:inherit; font-size:.78rem; font-weight:600; cursor:pointer;
  padding:5px 12px; border:1px solid var(--rule-strong); background:var(--paper);
  color:var(--ink-2); border-radius:3px}
.ct-foot button:hover{border-color:var(--accent); color:var(--accent)}
.ct-foot .hint{font-size:.83rem; color:var(--ink-3)}

@media print{
  .ct-bar,.ct-foot,.ct-item audio{display:none !important}
  .ct-exp{display:none !important}
  .ct-set{break-inside:auto; box-shadow:none}
  .ct-item{break-inside:avoid}
}
'''
CSS_ANCHOR = u'\n/* ---------- แท็บข้อสอบเสมือนจริง ---------- */'

SCRIPT = u'''
  /* ---------------------------------------------------------
     แท็บแบบฝึกฟังแนว CU-TEP
     ข้อมูลอยู่ในบล็อก JSON id="ct-data" และดัชนีไฟล์เสียงอยู่ใน id="ct-audio"
     ซึ่ง tools/make-cutep.py เขียนให้ทั้งคู่

     ต่างจากแท็บฝึกฟังของวิชาตรงที่ของจริงพูดคำถามในไฟล์เสียง ไม่ได้พิมพ์ไว้
     หน้านี้จึงซ่อนคำถามไว้ก่อน และล็อกให้ฟังได้รอบเดียวตามค่าเริ่มต้น
     --------------------------------------------------------- */
  var ctRoot = document.getElementById('ct-root');
  if (ctRoot && document.getElementById('ct-data')){
    var CT = JSON.parse(document.getElementById('ct-data').textContent);
    var CTA = {};
    var ctaEl = document.getElementById('ct-audio');
    if (ctaEl){ try { CTA = JSON.parse(ctaEl.textContent) || {}; } catch(e){ CTA = {}; } }

    function ce(s){
      return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
    }
    function ctShuffle(n){
      var a = [], i, j, t;
      for (i = 0; i < n; i++) a.push(i);
      for (i = n-1; i > 0; i--){ j = Math.floor(Math.random()*(i+1)); t=a[i]; a[i]=a[j]; a[j]=t; }
      return a;
    }

    var examMode = true, showQ = false, showScript = false, curSet = CT[0].id;

    var KINDS = {
      short: {label: 'Section 1 · Short dialogues',
              dir: 'You will hear short dialogues between two people, after which a question will be asked. You will hear each dialogue only once.'},
      long:  {label: 'Section 2 · Long dialogues',
              dir: 'You will hear longer dialogues between two people. After each dialogue three questions will be asked. You will hear each dialogue only once.'},
      mono:  {label: 'Section 3 · Monologues',
              dir: 'You will hear one person speaking, after which three questions will be asked. You will hear each monologue only once.'}
    };

    /* ---- ปุ่มเลือกชุด ---- */
    var setsRow = document.getElementById('ct-sets');
    CT.forEach(function(st){
      var b = document.createElement('button');
      b.type = 'button'; b.dataset.set = st.id;
      b.setAttribute('aria-pressed', String(st.id === curSet));
      b.textContent = st.title;
      b.addEventListener('click', function(){
        curSet = st.id;
        Array.prototype.forEach.call(setsRow.children, function(x){
          x.setAttribute('aria-pressed', String(x.dataset.set === curSet));
        });
        build();
      });
      setsRow.appendChild(b);
    });

    function build(){
      var st = CT.filter(function(s){ return s.id === curSet; })[0];
      var answered = 0, right = 0, total = 0;
      st.items.forEach(function(it){ total += it.qs.length; });

      ctRoot.innerHTML = '';
      var sec = document.createElement('section');
      sec.className = 'ct-set'; sec.id = 'cts-' + st.id;
      var head = document.createElement('div'); head.className = 'ct-sh';
      head.innerHTML = '<h3>' + ce(st.title) + '</h3>' +
                       '<span class="sc">ตอบถูก <b>0</b> จาก ' + total + ' ข้อ</span>';
      sec.appendChild(head);
      var scoreEl = head.querySelector('.sc b');

      var number = 1;
      ['short', 'long', 'mono'].forEach(function(kind){
        var items = st.items.filter(function(i){ return i.kind === kind; });
        if (!items.length) return;
        var n = items.reduce(function(a, i){ return a + i.qs.length; }, 0);
        var box = document.createElement('div'); box.className = 'ct-sec';
        box.innerHTML = '<div class="ct-sech"><span class="ct-kind">' + KINDS[kind].label +
                        '</span><span class="n">' + n + ' ข้อ</span></div>' +
                        '<p class="ct-dir">' + ce(KINDS[kind].dir) + '</p>';

        items.forEach(function(it){
          var from = number;
          number += it.qs.length;
          box.appendChild(renderItem(it, from, function(ok){
            answered++; if (ok) right++;
            scoreEl.textContent = String(right);
          }));
        });
        sec.appendChild(box);
      });

      var foot = document.createElement('div'); foot.className = 'ct-foot';
      foot.innerHTML = '<span class="hint">ทำเสร็จแล้วกดเริ่มใหม่เพื่อสลับตัวเลือกและล้างคำตอบ</span>';
      var reset = document.createElement('button');
      reset.type = 'button'; reset.textContent = 'เริ่มทำชุดนี้ใหม่';
      reset.style.marginLeft = 'auto';
      reset.addEventListener('click', build);
      foot.appendChild(reset);
      sec.appendChild(foot);

      ctRoot.appendChild(sec);
      document.getElementById('ct-count').textContent = 'ชุดนี้ ' + total + ' ข้อ · ทั้งหมด ' +
        CT.reduce(function(a, s){
          return a + s.items.reduce(function(b, i){ return b + i.qs.length; }, 0); }, 0) + ' ข้อ';
    }

    function renderItem(it, from, onAnswer){
      var wrap = document.createElement('div'); wrap.className = 'ct-item';
      var clip = CTA[it.id];

      var head = document.createElement('div'); head.className = 'ct-head';
      var label = it.qs.length > 1 ? ('ข้อ ' + from + ' ถึง ' + (from + it.qs.length - 1))
                                   : ('ข้อ ' + from);
      head.innerHTML = '<span class="ct-no">' + label + '</span>' +
                       (it.title ? '<span class="ct-title">' + ce(it.title) + '</span>' : '') +
                       (showScript && it.context ? '<span class="ct-ctx">' + ce(it.context) + '</span>' : '');
      wrap.appendChild(head);

      if (clip){
        var audio = document.createElement('audio');
        audio.controls = true; audio.preload = 'none'; audio.src = clip.src;
        // โหมดเหมือนสอบจริง ฟังจบแล้วล็อก ให้ฟังได้รอบเดียวเหมือนห้องสอบ
        if (examMode){
          audio.addEventListener('ended', function(){
            audio.controls = false;
            var done = document.createElement('div');
            done.className = 'ct-missing';
            done.textContent = 'ฟังครบรอบเดียวแล้ว · ปลดล็อกได้ที่ปุ่มโหมดด้านบน';
            audio.parentNode.insertBefore(done, audio.nextSibling);
          });
        }
        wrap.appendChild(audio);
      } else {
        var miss = document.createElement('div'); miss.className = 'ct-missing';
        miss.innerHTML = 'ยังไม่มีไฟล์เสียงของคลิปนี้ · สร้างได้ด้วย <code>python3 tools/make-cutep.py</code>';
        wrap.appendChild(miss);
      }

      it.qs.forEach(function(q, qi){
        var qb = document.createElement('div'); qb.className = 'ct-q';
        var qt = document.createElement('div');
        qt.className = 'ct-qt' + (showQ ? '' : ' hidden-q');
        qt.innerHTML = '<i>' + (from + qi) + '</i><span>' +
                       (showQ ? ce(q.q) : 'ฟังคำถามจากไฟล์เสียง') + '</span>';
        var opts = document.createElement('div'); opts.className = 'ct-opts';
        var exp = document.createElement('div'); exp.className = 'ct-exp'; exp.hidden = true;

        var order = ctShuffle(q.o.length);
        var at = order.indexOf(0);
        order.forEach(function(src, j){
          var b = document.createElement('button');
          b.type = 'button'; b.className = 'ct-opt'; b.textContent = q.o[src];
          b.addEventListener('click', function(){
            Array.prototype.forEach.call(opts.children, function(x, k){
              x.disabled = true;
              if (k === at) x.classList.add('ok');
              else if (k === j) x.classList.add('no');
            });
            exp.innerHTML = (showQ ? '' : '<b>' + ce(q.q) + '</b><br>') + ce(q.e);
            exp.hidden = false;
            onAnswer(j === at);
          });
          opts.appendChild(b);
        });

        qb.appendChild(qt); qb.appendChild(opts); qb.appendChild(exp);
        wrap.appendChild(qb);
      });

      if (showScript && it.turns && it.turns.length){
        var sc = document.createElement('div'); sc.className = 'ct-script';
        it.turns.forEach(function(t){
          var line = document.createElement('div'); line.className = 'ct-line';
          line.innerHTML = '<span class="ct-who">' + ce(t[0]) + '</span>' +
                           '<span class="ct-said">' + ce(t[1]) + '</span>';
          sc.appendChild(line);
        });
        wrap.appendChild(sc);
      }
      return wrap;
    }

    function toggle(id, get, set){
      var b = document.getElementById(id);
      b.addEventListener('click', function(){
        set(!get());
        b.setAttribute('aria-pressed', String(get()));
        build();
      });
    }
    toggle('ct-exam', function(){ return examMode; }, function(v){ examMode = v; });
    toggle('ct-showq', function(){ return showQ; }, function(v){ showQ = v; });
    toggle('ct-script', function(){ return showScript; }, function(v){ showScript = v; });

    build();
  }
'''
SCRIPT_ANCHOR = u'''  /* ---------------------------------------------------------
     แท็บข้อสอบเสมือนจริง · Part I และ Part II'''


def apply(html):
    steps = [
        (u'ปุ่มแท็บ', TAB_ANCHOR, TAB),
        (u'สารบัญข้าง', RAIL_ANCHOR, RAIL),
        (u'เนื้อหาแท็บ', SECTION_ANCHOR, SECTION),
        (u'สไตล์', CSS_ANCHOR, CSS),
        (u'สคริปต์', SCRIPT_ANCHOR, SCRIPT),
    ]
    for label, anchor, payload in steps:
        if payload.strip()[:80] in html:
            print(u'  %s มีอยู่แล้ว ข้าม' % label)
            continue
        at = html.find(anchor)
        if at < 0:
            raise SystemExit(u'หาจุดวาง %s ไม่เจอ' % label)
        html = html[:at] + payload + html[at:]
        print(u'  วาง%sแล้ว · %d ตัวอักษร' % (label, len(payload)))

    if u"ct:'rail-ct'" not in html:
        old = u"var rails = {np:'rail-np'"
        html = html.replace(old, u"var rails = {ct:'rail-ct', np:'rail-np'")
        print(u'  ผูกแท็บเข้ากับสารบัญข้างแล้ว')
    return html


def main():
    ap = argparse.ArgumentParser(description=u'วางแท็บ CU-TEP ลงหน้าวิชาภาษาอังกฤษ')
    ap.add_argument('--check', action='store_true', help=u'ดูผลอย่างเดียว ไม่เขียนไฟล์')
    a = ap.parse_args()

    html = io.open(PAGE, encoding='utf-8').read()
    before = len(html)
    html = apply(html)
    print(u'\nหน้าเว็บ %d → %d ตัวอักษร' % (before, len(html)))
    if not a.check:
        io.open(PAGE, 'w', encoding='utf-8').write(html)
        print(u'เขียน oral-eng/index.html แล้ว')
    return 0


if __name__ == '__main__':
    sys.exit(main())
