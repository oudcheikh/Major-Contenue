# -*- coding: utf-8 -*-
"""Assemble le cahier A5 التاريخ والجغرافيا والتربية المدنية : couverture + فهرس
+ 3 parties (تاريخ ambre · جغرافيا bleu · مدنية vert). Style « carnet relié »,
très illustré (cartes SVG, fonds de carte à compléter, frises).
QR : hg6-uNN (تاريخ+جغرافيا = matière d'examen unique) · civ6-uN (مدنية)."""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.normpath(os.path.join(_HERE, '..', 'math-a5')))

from base_hgc import CSS, CSS_ASSETS, CSS_HGC, DOC_ID, page, unit_banner, spine, tabs3
from qr_major import _qr_b64, unit_id, BASE_URL, COLORS, correction_qr_card, lesson_qr_card
from unites_hist import UNITS_HIST
from unites_geo import UNITS_GEO
from unites_civ import UNITS_CIV

_FAKE_QR = '<span class="im im-qr qr" role="img" aria-label="QR فيديو الدرس"></span>'
_PART2QR = {'hist': 'hg', 'geo': 'hg', 'civ': 'civ'}


def lesson_qr(qr_part, num):
    url = f'{BASE_URL}/#/lesson/{unit_id(qr_part, num)}'
    b64 = _qr_b64(url, COLORS[qr_part])
    return f'<img class="qr" src="data:image/png;base64,{b64}" alt="QR درس {unit_id(qr_part, num)}"/>'


def wire_qr(body, part, num, first=False):
    qp = _PART2QR[part]
    if part == 'geo':  # histoire-géo = une seule matière (hg6) : la géo continue après les 9 unités d'histoire
        num += len(UNITS_HIST)
    has_video = _FAKE_QR in body
    body = body.replace(_FAKE_QR, lesson_qr(qp, num))
    if '<span class="bl">تمارين</span>' in body or '<span class="bl">أتحدّى</span>' in body or '<span class="bl">أراجع</span>' in body:
        body += correction_qr_card(qp, num)
    elif first and not has_video:
        body += lesson_qr_card(qp, num)
    return body


_PART_GRAD = {'hist': 'linear-gradient(150deg,#78350f 0%,#b45309 55%,#f59e0b 100%)',
              'geo': 'linear-gradient(150deg,#1e3a8a 0%,#1d4ed8 55%,#60a5fa 100%)',
              'civ': 'linear-gradient(150deg,#064e2b 0%,#0f7b3a 55%,#34d399 100%)'}


def part_page(num, emoji, kicker, title, sub, chips, part):
    chips_html = ''.join(
        f'<span style="background:rgba(255,255,255,.16);border:.35mm solid rgba(255,255,255,.25);'
        f'border-radius:999px;padding:1.3mm 3.4mm;font-size:7.6px;font-weight:900;color:#fff">{c}</span>'
        for c in chips)
    # emoji param kept for API compat; print-safe label instead
    mark = {'hist': 'تاريخ', 'geo': 'جغرافيا', 'civ': 'مدنية'}.get(part, title)
    return f'''<div class="sheet part-{part}">
  {spine()}
  <div class="page-main" style="background:{_PART_GRAD[part]};color:#fff">
    <div class="page-body" style="display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center">
      <div style="position:absolute;width:46mm;height:46mm;border-radius:50%;background:rgba(255,255,255,.09);top:-16mm;left:-12mm"></div>
      <div style="position:absolute;width:34mm;height:34mm;border-radius:50%;background:rgba(255,255,255,.09);bottom:-10mm;right:-8mm"></div>
      <div style="display:inline-flex;min-width:18mm;height:12mm;align-items:center;justify-content:center;background:rgba(255,255,255,.18);border-radius:999px;font-size:11px;font-weight:900;padding:0 4mm">{mark}</div>
      <div style="display:inline-flex;background:rgba(255,255,255,.16);border:.35mm solid rgba(255,255,255,.25);padding:1.2mm 4mm;border-radius:999px;font-size:8px;font-weight:900;letter-spacing:.6px;margin:2.6mm 0 1.6mm">{kicker}</div>
      <h1 style="font-size:27px;font-weight:900;margin:0 0 2mm;color:#fff">{title}</h1>
      <p style="font-size:8.8px;font-weight:800;color:rgba(255,255,255,.92);margin:0 0 5mm;max-width:100mm;line-height:1.75">{sub}</p>
      <div style="display:flex;gap:2.2mm;flex-wrap:wrap;justify-content:center;max-width:108mm">{chips_html}</div>
      <div style="display:flex;gap:5mm;margin-top:7mm">
        <span class="im im-fille" style="width:15mm;height:13.5mm" role="img"></span>
        <span class="im im-garcon" style="width:15mm;height:13.5mm" role="img"></span>
      </div>
    </div>
    <div class="bottom-number" style="border-color:#fff">{num}</div>
  </div>
  {tabs3(part)}
</div>'''


# ─── pagination ───
toc = {'hist': [], 'geo': [], 'civ': []}
pages_html = []
num = 2
sep_nums = {}

_PART_INFO = {
    'hist': ('🏰', 'الجزء الأول', 'التاريخ',
             'السيرة النبوية · الخلافة · الحضارة الإسلامية · تاريخ موريتانيا من غانا إلى الاستقلال',
             'UNITS', UNITS_HIST, 'الوحدة'),
    'geo': ('🗺️', 'الجزء الثاني', 'الجغرافيا',
            'موقع بلادنا وحدودها · التضاريس والمناخ · السكان والثروات · خرائط تتدرّب عليها بيدك',
            'UNITS', UNITS_GEO, 'الوحدة'),
    'civ': ('🤝', 'الجزء الثالث', 'التربية المدنية',
            'الدولة ورموزها · المؤسسات · الحقوق والواجبات · المنظمات الدولية والسلم',
            'UNITS', UNITS_CIV, 'الوحدة'),
}

for part in ('hist', 'geo', 'civ'):
    emoji, kicker, title, sub, _, units, ulabel = _PART_INFO[part]
    sep_nums[part] = num
    n_units = len(units)
    pages_html.append(part_page(num, emoji, kicker, title, sub,
        [f'{n_units} وحدة', 'خرائط ورسوم في كل درس', 'تمارين متدرّجة (سهل · متوسط · صعب)', 'فيديو لكل درس'], part))
    num += 1
    for u in units:
        toc[part].append((u['num'], u['title'], num))
        first = True
        for ptitle, body, with_eval in u['pages']:
            if first:
                body = unit_banner(u['num'], f"{ulabel} {u['num']} — {u['title']}", u['sub'], u.get('color', '')) + body
            body = wire_qr(body, part, u['num'], first=first)
            first = False
            label_part = {'hist': 'التاريخ', 'geo': 'الجغرافيا', 'civ': 'التربية المدنية'}[part]
            label = f"{label_part} · {ulabel} {u['num']} · {u['title']}"
            pages_html.append(page(num, ptitle, body, unit_label=label, with_eval=with_eval, part=part))
            num += 1

_COVER_CARDS = [
    ('تاريخ', 'التاريخ', 'السيرة النبوية والخلافة · الحضارة الإسلامية · المرابطون والإمارات · المقاومة والاستقلال'),
    ('جغرافيا', 'الجغرافيا', 'الموقع والحدود · التضاريس والمناخ · السكان والمدن · الثروات — مع خرائط تكملها بيدك'),
    ('مدنية', 'التربية المدنية', 'الدولة ورموزها · الدستور والمؤسسات · حقوق الطفل · المنظمات الدولية'),
    ('QR', 'ماجور الذكي', 'رمز QR في كل درس: فيديو الشرح · تصحيح تمارينك بالذكاء الاصطناعي · تدريب فوري'),
]
_cover_cards_html = ''.join(
    f'''<div style="background:rgba(255,255,255,.12);border:.35mm solid rgba(255,255,255,.18);border-radius:4mm;
        padding:2.6mm 3mm;display:flex;flex-direction:column;gap:.8mm;direction:rtl">
      <span style="font-size:9px;font-weight:900;opacity:.9">{e}</span>
      <strong style="font-size:9.5px;font-weight:900">{t}</strong>
      <span style="font-size:6.8px;line-height:1.55;color:rgba(255,255,255,.87)">{s}</span>
    </div>''' for e, t, s in _COVER_CARDS)

_n_hg = len(UNITS_HIST) + len(UNITS_GEO)
_band = ''.join(
    f'<span style="background:#fff;color:#0f172a;padding:1.4mm 3.2mm;border-radius:999px;font-size:7px;font-weight:900">{c}</span>'
    for c in ['موريتانيا · تحضير المسابقة الوطنية', f'{_n_hg} وحدة تاريخ وجغرافيا',
              f'{len(UNITS_CIV)} وحدات مدنية', 'خرائط وفرائز زمنية'])

COVER = f'''<div class="sheet">
  <div class="page-main" style="background:linear-gradient(135deg,#7c2d12 0%,#b45309 46%,#f59e0b 100%);color:#fff">
    <div class="page-body" style="display:flex;flex-direction:column;justify-content:center;padding:7mm 8mm">
      <div style="position:absolute;width:52mm;height:52mm;border-radius:50%;background:rgba(255,255,255,.1);left:-16mm;top:8mm"></div>
      <div style="position:absolute;width:44mm;height:44mm;border-radius:50%;background:rgba(255,255,255,.1);right:-14mm;bottom:-14mm"></div>
      <div style="display:flex;justify-content:space-between;align-items:flex-start">
        <span style="display:inline-flex;background:rgba(255,255,255,.14);border:.35mm solid rgba(255,255,255,.2);padding:1.6mm 3.6mm;border-radius:999px;font-size:7.6px;font-weight:900;letter-spacing:.5px">موريتانيا · 6AF · 2025-2026</span>
        <span class="im im-logo" role="img" aria-label="Major" style="width:17mm;height:17mm;background-color:rgba(255,255,255,.96);padding:1.6mm;border-radius:4mm;box-shadow:0 3px 8px rgba(15,23,42,.25)"></span>
      </div>
      <h1 style="margin:5mm 0 1.6mm;font-size:28px;line-height:1.05;font-weight:900">دفتر <span style="color:#fde68a">ماجور</span></h1>
      <p style="font-size:10.5px;color:rgba(255,255,255,.9);margin:0 0 4mm;font-weight:800">التاريخ والجغرافيا والتربية المدنية · السنة السادسة الأساسية</p>
      <div style="display:flex;gap:2mm;flex-wrap:wrap;margin-bottom:4mm;direction:rtl">{_band}</div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:2.6mm;margin-bottom:4.5mm">{_cover_cards_html}</div>
      <div style="background:rgba(255,255,255,.96);color:#182230;border-radius:3.2mm;padding:2.2mm 3.6mm;font-size:8.4px;font-weight:900;display:flex;align-items:center;gap:2mm">
        هذا الدفتر ملك للتلميذ(ة): <span style="flex:1;border-bottom:.5mm dashed #94a3b8"></span>
        القسم: <span style="width:20mm;border-bottom:.5mm dashed #94a3b8"></span>
      </div>
      <div style="display:flex;justify-content:center;gap:6mm;margin-top:5mm">
        <span class="im im-fille" style="width:17mm;height:15mm" role="img"></span>
        <span class="im im-garcon" style="width:17mm;height:15mm" role="img"></span>
      </div>
    </div>
  </div>
</div>'''


def toc_col(rows, color):
    return '<table style="width:100%;border-collapse:collapse">' + ''.join(
        f'<tr>'
        f'<td style="width:6.5mm;padding:.7mm .6mm"><span style="display:inline-flex;width:5mm;height:5mm;'
        f'border-radius:50%;background:{color};color:#fff;align-items:center;justify-content:center;'
        f'font-size:7px;font-weight:900">{n}</span></td>'
        f'<td style="padding:.7mm .6mm;font-size:7.6px;font-weight:800">{t}</td>'
        f'<td style="padding:.7mm .6mm;font-size:7.6px;font-weight:900;color:{color};text-align:left;'
        f'font-variant-numeric:tabular-nums">{p}</td></tr>'
        for n, t, p in rows) + '</table>'


def toc_section(label, color, page_ref):
    return (f'<div style="display:flex;align-items:center;gap:2mm;margin:1.6mm 0 .6mm">'
            f'<span style="background:{color};border-radius:999px;padding:1mm 4mm;font-size:8.2px;font-weight:900;color:#fff">{label}</span>'
            f'<span style="flex:1;border-bottom:.4mm dotted #cbd5e1"></span>'
            f'<span style="font-size:7.4px;font-weight:900;color:{color}">ص {page_ref}</span></div>')


def _two_cols(rows, color):
    half = (len(rows) + 1) // 2
    return (f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:0 4mm;align-items:start">'
            f'{toc_col(rows[:half], color)}{toc_col(rows[half:], color)}</div>')


_SOM_BODY = f'''
{toc_section('الجزء الأول — التاريخ', '#b45309', sep_nums['hist'])}
{_two_cols(toc['hist'], '#b45309')}
{toc_section('الجزء الثاني — الجغرافيا', '#1d4ed8', sep_nums['geo'])}
{_two_cols(toc['geo'], '#1d4ed8')}
{toc_section('الجزء الثالث — التربية المدنية', '#0f7b3a', sep_nums['civ'])}
{_two_cols(toc['civ'], '#0f7b3a')}
<div class="scallop" style="margin-top:2.4mm">كل وحدة تبدأ بدرس <b>أتعلّم</b> مع خريطة أو رسم يوضح الفكرة ورمز QR لفيديو الشرح، ثم <b>مثال محلول</b>، ثم <b>تمارين</b> متدرّجة (سهل · متوسط · صعب) فيها خرائط تكملها بيدك، وتنتهي بتقييم ذاتي.</div>'''

SOMMAIRE = page(1, 'الفهرس', _SOM_BODY, unit_label='دفتر ماجور · الفهرس')

# Composer A5 : réserve QR + densification douce.
# Jamais de bloc « ألخّص الفكرة » ; jamais toucher fontSize ; ne supprimer
# que d'éventuels .composer-fill résiduels, jamais les dots/wlines d'exercices.
_COMPOSER_JS = r'''
<script>
(function(){
  function composer(){
    document.querySelectorAll('.sheet').forEach(function(sheet){
      var body = sheet.querySelector('.page-body');
      if (!body) return;
      var st = getComputedStyle(body);
      if (st.justifyContent === 'center') return;
      var kids = [].filter.call(body.children, function(c){
        var cs = getComputedStyle(c);
        if (cs.position === 'absolute' || cs.display === 'none') return false;
        if (c.classList.contains('qr-corr') || c.classList.contains('qr-reserve')) return false;
        return c.getBoundingClientRect().height > 2;
      });
      if (kids.length < 2) return;
      var br = body.getBoundingClientRect();
      var padB = parseFloat(st.paddingBottom) || 0;
      var reserve = body.querySelector('.qr-reserve');
      function contentFloor(){
        var floor = br.bottom - padB;
        if (reserve) floor = Math.min(floor, reserve.getBoundingClientRect().top);
        var qrEl = sheet.querySelector('.qr-corr');
        if (qrEl) floor = Math.min(floor, qrEl.getBoundingClientRect().top - 8);
        var pnEl = sheet.querySelector('.bottom-number');
        if (pnEl) floor = Math.min(floor, pnEl.getBoundingClientRect().top - 6);
        return floor;
      }
      function spareNow(){
        var maxB = 0;
        kids.forEach(function(c){ maxB = Math.max(maxB, c.getBoundingClientRect().bottom); });
        return contentFloor() - maxB;
      }
      function refreshKids(){
        kids = [].filter.call(body.children, function(c){
          var cs = getComputedStyle(c);
          if (cs.position === 'absolute' || cs.display === 'none') return false;
          if (c.classList.contains('qr-corr') || c.classList.contains('qr-reserve')) return false;
          return c.getBoundingClientRect().height > 2;
        });
      }
      function trimFillOnly(){
        var fillEl = body.querySelector('.composer-fill');
        if (!fillEl) return false;
        var fl = fillEl.querySelectorAll('.line');
        if (fl.length > 0) fl[fl.length - 1].remove();
        else fillEl.remove();
        refreshKids();
        return true;
      }
      function clearOverlayZones(){
        var qr = sheet.querySelector('.qr-corr');
        var pn = sheet.querySelector('.bottom-number');
        var qrR = qr ? qr.getBoundingClientRect() : null;
        var pnR = pn ? pn.getBoundingClientRect() : null;
        var qrBand = qrR ? (qrR.top - 6) : null;
        var pnBand = pnR ? (pnR.top - 4) : null;
        function invades(el){
          var r = el.getBoundingClientRect();
          if (qrBand != null && r.bottom > qrBand) {
            if (!qrR || r.left < qrR.right + 4) return true;
          }
          if (pnBand != null && r.bottom > pnBand) {
            if (!pnR || !(r.right < pnR.left - 2 || r.left > pnR.right + 2)) return true;
          }
          return false;
        }
        function indentClear(el){
          // Décale hors de la zone QR (gauche) sans toucher police ni lignes
          el.style.marginLeft = '22mm';
          el.style.maxWidth = 'calc(100% - 22mm)';
          el.style.boxSizing = 'border-box';
        }
        for (var guard = 0; guard < 24; guard++) {
          var hit = null;
          for (var i = kids.length - 1; i >= 0; i--) {
            var c = kids[i];
            if (invades(c)) { hit = c; break; }
            var innerHit = null;
            c.querySelectorAll('.line, .dotl, .wline').forEach(function(ln){
              if (!innerHit && invades(ln)) innerHit = ln;
            });
            if (innerHit) { hit = c; break; }
          }
          if (!hit) break;
          if (hit.classList.contains('composer-fill')) {
            var fl = hit.querySelectorAll('.line');
            if (fl.length > 0) fl[fl.length - 1].remove();
            else hit.remove();
            refreshKids();
            continue;
          }
          if (hit.classList.contains('fig')) break;
          // 1) Indenter pour libérer le QR (tip / warn / défi / exo)
          var already = (parseFloat(hit.style.marginLeft) || 0) >= 20;
          if (!already) {
            indentClear(hit);
            refreshKids();
            if (!invades(hit)) continue;
          }
          // 2) Compactage doux des marges / paddings
          var mt = parseFloat(getComputedStyle(hit).marginTop) || 0;
          if (mt > 0) {
            hit.style.marginTop = Math.max(0, mt - 2) + 'px';
            refreshKids();
            continue;
          }
          var pb = parseFloat(getComputedStyle(hit).paddingBottom) || 0;
          if (pb > 2) {
            hit.style.paddingBottom = Math.max(1, pb - 2) + 'px';
            refreshKids();
            continue;
          }
          // 3) Dernier recours : retirer 1 ligne du défi uniquement (pas des exos)
          if (hit.classList.contains('defi-card')) {
            var dlines = hit.querySelectorAll('.lines .line');
            if (dlines.length > 0) {
              dlines[dlines.length - 1].remove();
              refreshKids();
              continue;
            }
          }
          break;
        }
        for (var g2 = 0; g2 < 16 && spareNow() < 2; g2++) {
          if (!trimFillOnly()) break;
        }
      }
      function isHeader(el){
        return el.classList.contains('lesson-title') || el.classList.contains('unit-banner') ||
               el.classList.contains('objectifs') || el.classList.contains('badge-row');
      }
      var spare = spareNow();
      if (spare < -2) {
        for (var pass = 0; pass < 4 && spare < -2; pass++) {
          var share = (-spare) / Math.max(1, kids.length - 1);
          kids.forEach(function(c, i){
            if (i === 0) return;
            // Ne jamais compresser les cartes / figures
            if (c.classList.contains('fig')) return;
            var m = parseFloat(getComputedStyle(c).marginTop) || 0;
            var cutm = Math.min(m, Math.max(share * 0.7, 1.0));
            if (cutm > 0.3) c.style.marginTop = Math.max(0, m - cutm) + 'px';
          });
          kids.forEach(function(c){
            // Jamais toucher padding/taille des cartes — elles restent lisibles
            if (c.classList.contains('fig')) return;
            if (!c.matches('.frame, .exo-card, .exemple, .badge-row, .objectifs, .unit-banner')) return;
            var pb = parseFloat(getComputedStyle(c).paddingBottom) || 0;
            var pt = parseFloat(getComputedStyle(c).paddingTop) || 0;
            var mb = parseFloat(getComputedStyle(c).marginBottom) || 0;
            if (pb > 4) c.style.paddingBottom = (pb - 1) + 'px';
            if (pt > 4) c.style.paddingTop = (pt - 0.8) + 'px';
            if (mb > 3) c.style.marginBottom = (mb - 0.8) + 'px';
          });
          // Ne plus écraser la hauteur des lignes de réponse (écriture élève)
          spare = spareNow();
        }
        clearOverlayZones();
        return;
      }
      function growLines(budget){
        var lines = body.querySelectorAll('.lines .line, .dotl, .wline');
        if (!lines.length || budget < 12) return budget;
        var per = Math.min(budget * 0.55 / lines.length, 7);
        lines.forEach(function(ln){
          var h = ln.getBoundingClientRect().height || 7;
          ln.style.height = (h + per) + 'px';
        });
        var s = spareNow();
        if (s < -1) {
          var back = Math.min(per, (-s) / lines.length + 0.5);
          lines.forEach(function(ln){
            var h = ln.getBoundingClientRect().height || 7;
            ln.style.height = Math.max(5.5, h - back) + 'px';
          });
          s = spareNow();
        }
        return s;
      }
      if (spare > 36) spare = growLines(spare);
      if (spare > 36) {
        var targets = [];
        kids.forEach(function(c, i){
          if (i === 0) return;
          if (isHeader(c) || isHeader(kids[i - 1])) return;
          if (c.classList.contains('self-eval') || c.classList.contains('composer-fill')) return;
          if (c.classList.contains('tip-card') || c.classList.contains('defi-card')) return;
          if (c.classList.contains('attention') || c.classList.contains('warn-card')) return;
          if (c.classList.contains('bulle-row')) return;
          targets.push(c);
        });
        if (targets.length) {
          var extra = Math.min(spare / targets.length, 8);
          targets.forEach(function(c){
            var m = parseFloat(getComputedStyle(c).marginTop) || 0;
            c.style.marginTop = (m + extra) + 'px';
          });
          spare = spareNow();
        }
      }
      for (var fix = 0; fix < 8 && spare < -1; fix++) {
        if (!trimFillOnly()) break;
        spare = spareNow();
      }
      clearOverlayZones();
    });
  }
  function run(){
    function go(){ composer(); }
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(go);
    else go();
  }
  window.__majorComposer = composer;
  window.addEventListener('beforeprint', function(){ composer(); });
  if (document.readyState === 'complete') run();
  else window.addEventListener('load', run);
})();
</script>
'''

HTML = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Cahier Major A5 — التاريخ والجغرافيا والتربية المدنية · 6AF</title>
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&display=swap" rel="stylesheet">
<style>{CSS}{CSS_ASSETS}{CSS_HGC}</style>
</head>
<body>
<div class="toolbar"><button class="action-btn" onclick="window.print()">طباعة / PDF</button></div>
{COVER}
{SOMMAIRE}
{''.join(pages_html)}
{_COMPOSER_JS}
</body>
</html>'''

out = os.path.join(_HERE, '..', '..', 'livrables', 'Cahier-Major-HistGeo-Civique-6AF-A5.SOURCE.html')
out = os.path.normpath(out)
open(out, 'w').write(HTML)
print(f'écrit: {out} ({len(HTML)/1024:.0f} Ko, {2 + len(pages_html)} pages A5)')
