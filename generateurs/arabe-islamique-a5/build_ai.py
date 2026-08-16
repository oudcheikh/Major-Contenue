# -*- coding: utf-8 -*-
"""Assemble le cahier A5 عربية/إسلامية : couverture + فهرس + partie اللغة العربية (18 unités)
+ partie التربية الإسلامية (8 فصول). Style « dfatir Major » du cahier A4 original
(dos relié bleu nuit, onglets, cartes d'exercices à lignes d'écriture)."""
import os

from base_ai import CSS, CSS_ASSETS, DOC_ID, page, unit_banner, spine, tabs, print_sanitize
from qr_major import _qr_b64, unit_id, BASE_URL, COLORS, correction_qr_card, lesson_qr_card
from unites_ar_1 import UNITS_AR_1
from unites_ar_2 import UNITS_AR_2
from unites_ar_3 import UNITS_AR_3
from unites_isl import UNITS_ISL

_FAKE_QR = '<span class="im im-qr qr" role="img" aria-label="QR فيديو الدرس"></span>'


def lesson_qr(part, num):
    """<img> du QR leçon aux dimensions du .video-box (17mm, via CSS)."""
    url = f'{BASE_URL}/#/lesson/{unit_id(part, num)}'
    b64 = _qr_b64(url, COLORS[part])
    return f'<img class="qr" src="data:image/png;base64,{b64}" alt="QR درس {unit_id(part, num)}"/>'


def wire_qr(body, part, num, first=False):
    """QR leçon réel dans le video_box + carte QR correction sur les pages تمارين.
    Si la 1re page de l'unité n'a pas de video_box (cadre trop dense), une carte
    QR « leçon » est posée dans le coin inférieur gauche à la place."""
    has_video = _FAKE_QR in body
    body = body.replace(_FAKE_QR, lesson_qr(part, num))
    if '<span class="bl">تمارين</span>' in body or '<span class="bl">أتحدّى</span>' in body or '<span class="bl">أراجع</span>' in body:
        body += correction_qr_card(part, num)
    elif first and not has_video:
        body += lesson_qr_card(part, num)
    return body


AR_UNITS = UNITS_AR_1 + UNITS_AR_2 + UNITS_AR_3
ISL_UNITS = UNITS_ISL

_PART_GRAD = {'ar': 'linear-gradient(150deg,#5b21b6 0%,#7c3aed 55%,#a78bfa 100%)',
              'isl': 'linear-gradient(150deg,#047857 0%,#059669 55%,#34d399 100%)'}


def part_page(num, emoji, kicker, title, sub, chips, part):
    chips_html = ''.join(
        f'<span style="background:rgba(255,255,255,.16);border:.35mm solid rgba(255,255,255,.25);'
        f'border-radius:999px;padding:1.3mm 3.4mm;font-size:7.6px;font-weight:900;color:#fff">{c}</span>'
        for c in chips)
    emoji_html = f'<div style="font-size:28px;font-weight:900;opacity:.95">{emoji}</div>' if emoji else ''
    return f'''<div class="sheet part-{part}">
  {spine()}
  <div class="page-main" style="background:{_PART_GRAD[part]};color:#fff">
    <div class="page-body" style="display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:8mm 7mm">
      <div style="position:absolute;width:46mm;height:46mm;border-radius:50%;background:rgba(255,255,255,.09);top:-16mm;left:-12mm"></div>
      <div style="position:absolute;width:34mm;height:34mm;border-radius:50%;background:rgba(255,255,255,.09);bottom:-10mm;right:-8mm"></div>
      {emoji_html}
      <div style="display:inline-flex;background:rgba(255,255,255,.16);border:.35mm solid rgba(255,255,255,.25);padding:1.2mm 4mm;border-radius:999px;font-size:8px;font-weight:900;letter-spacing:.6px;margin:2.6mm 0 1.6mm">{kicker}</div>
      <h1 style="font-size:26px;font-weight:900;margin:0 0 2mm;color:#fff">{title}</h1>
      <p style="font-size:9px;font-weight:800;color:rgba(255,255,255,.92);margin:0 0 5mm;max-width:100mm;line-height:1.75">{sub}</p>
      <div style="display:flex;gap:2.2mm;flex-wrap:wrap;justify-content:center;max-width:108mm">{chips_html}</div>
      <div style="display:flex;gap:5mm;margin-top:7mm">
        <span class="im im-fille" style="width:15mm;height:13.5mm" role="img"></span>
        <span class="im im-garcon" style="width:15mm;height:13.5mm" role="img"></span>
      </div>
    </div>
    <div class="bottom-number" style="border-color:#fff">{num}</div>
  </div>
  {tabs(part)}
</div>'''


# ─── pagination : couverture = page de garde, فهرس = p.1 ───
toc_ar, toc_isl = [], []
pages_html = []
num = 2

# séparateur partie 1 — اللغة العربية
sep_ar_num = num
pages_html.append(part_page(num, '', 'الجزء الأول', 'اللغة العربية',
    'النحو والصرف · الإملاء · المفردات · القراءة والفهم · التعبير الكتابي',
    [f'{len(AR_UNITS)} وحدة', 'تمارين متدرّجة (سهل → صعب)', 'أمثلة محلولة', 'فيديو لكل درس'], 'ar'))
num += 1

for u in AR_UNITS:
    toc_ar.append((u['num'], u['title'], num))
    first = True
    for title, body, with_eval in u['pages']:
        if first:
            body = unit_banner(u['num'], f"الوحدة {u['num']} — {u['title']}", u['sub'], u['color']) + body
        body = wire_qr(body, 'ar', u['num'], first=first)
        first = False
        label = f"اللغة العربية · الوحدة {u['num']} · {u['title']}"
        pages_html.append(page(num, title, body, unit_label=label, with_eval=with_eval, part='ar'))
        num += 1

# séparateur partie 2 — التربية الإسلامية
sep_isl_num = num
pages_html.append(part_page(num, '', 'الجزء الثاني', 'التربية الإسلامية',
    'العقيدة · الفقه · السيرة النبوية · الأخلاق والقيم',
    [f'{len(ISL_UNITS)} فصول', 'تمارين متدرّجة (سهل → صعب)', 'الأدلة من الكتاب والسنة', 'فيديو لكل درس'], 'isl'))
num += 1

for u in ISL_UNITS:
    toc_isl.append((u['num'], u['title'], num))
    first = True
    for title, body, with_eval in u['pages']:
        if first:
            body = unit_banner(u['num'], f"الفصل {u['num']} — {u['title']}", u['sub'], u['color']) + body
        body = wire_qr(body, 'isl', u['num'], first=first)
        first = False
        label = f"التربية الإسلامية · الفصل {u['num']} · {u['title']}"
        pages_html.append(page(num, title, body, unit_label=label, with_eval=with_eval, part='isl'))
        num += 1

_COVER_CARDS = [
    ('1', 'النحو والصرف', 'أنواع الكلمة · الإعراب · الجملتان · الأفعال الخمسة · النواسخ · الحال والتمييز'),
    ('2', 'الإملاء والمفردات', 'الهمزات · التاء والألف · الشدة والتنوين · المعنى والضد والمرادف'),
    ('3', 'القراءة والتعبير', 'نصوص موريتانية بأسئلة المسابقة · منهجية الفقرة · نموذج امتحان كامل'),
    ('4', 'التربية الإسلامية', 'الأركان · الطهارة والصلاة · الزكاة والصوم والحج · السيرة · الأخلاق'),
]
_cover_cards_html = ''.join(
    f'''<div style="background:rgba(255,255,255,.12);border:.35mm solid rgba(255,255,255,.18);border-radius:4mm;
        padding:2.6mm 3mm;display:flex;flex-direction:column;gap:.8mm;direction:rtl">
      <span style="display:inline-flex;width:7mm;height:7mm;border-radius:50%;background:rgba(255,255,255,.22);
        align-items:center;justify-content:center;font-size:9px;font-weight:900">{e}</span>
      <strong style="font-size:9.5px;font-weight:900">{t}</strong>
      <span style="font-size:7px;line-height:1.55;color:rgba(255,255,255,.9)">{s}</span>
    </div>''' for e, t, s in _COVER_CARDS)

_band = ''.join(
    f'<span style="background:#fff;color:#0f172a;padding:1.4mm 3.2mm;border-radius:999px;font-size:7px;font-weight:900">{c}</span>'
    for c in ['موريتانيا · تحضير المسابقة الوطنية', f'{len(AR_UNITS)} وحدة عربية',
              f'{len(ISL_UNITS)} فصول إسلامية', 'تمارين: سهل / متوسط / صعب'])

COVER = f'''<div class="sheet">
  <div class="page-main" style="background:linear-gradient(135deg,#1e3a8a 0%,#2563eb 48%,#38bdf8 100%);color:#fff">
    <div class="page-body" style="display:flex;flex-direction:column;justify-content:center;padding:7mm 8mm">
      <div style="position:absolute;width:52mm;height:52mm;border-radius:50%;background:rgba(255,255,255,.1);left:-16mm;top:8mm"></div>
      <div style="position:absolute;width:44mm;height:44mm;border-radius:50%;background:rgba(255,255,255,.1);right:-14mm;bottom:-14mm"></div>
      <div style="display:flex;justify-content:space-between;align-items:flex-start">
        <span style="display:inline-flex;background:rgba(255,255,255,.14);border:.35mm solid rgba(255,255,255,.2);padding:1.6mm 3.6mm;border-radius:999px;font-size:7.6px;font-weight:900;letter-spacing:.5px">موريتانيا · 6AF · 2025-2026</span>
        <span class="im im-logo" role="img" aria-label="Major" style="width:17mm;height:17mm;background-color:rgba(255,255,255,.96);padding:1.6mm;border-radius:4mm"></span>
      </div>
      <h1 style="margin:5mm 0 1.6mm;font-size:30px;line-height:1.05;font-weight:900">دفتر <span style="color:#fde68a">ماجور</span></h1>
      <p style="font-size:11px;color:rgba(255,255,255,.9);margin:0 0 4mm;font-weight:800">اللغة العربية والتربية الإسلامية · السنة السادسة الأساسية</p>
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
        f'<td style="width:6.5mm;padding:.8mm .6mm"><span style="display:inline-flex;width:5mm;height:5mm;'
        f'border-radius:50%;background:{color};color:#fff;align-items:center;justify-content:center;'
        f'font-size:7px;font-weight:900">{n}</span></td>'
        f'<td style="padding:.8mm .6mm;font-size:7.8px;font-weight:800">{t}'
        f'<span style="display:inline-block;min-width:6mm"></span></td>'
        f'<td style="padding:.8mm .6mm;font-size:7.8px;font-weight:900;color:{color};text-align:left;'
        f'font-variant-numeric:tabular-nums">{p}</td></tr>'
        for n, t, p in rows) + '</table>'


def toc_section(label, color, page_ref):
    return (f'<div style="display:flex;align-items:center;gap:2mm;margin:2mm 0 .8mm">'
            f'<span style="background:{color};border-radius:999px;padding:1mm 4mm;font-size:8.4px;font-weight:900;color:#fff">{label}</span>'
            f'<span style="flex:1;border-bottom:.4mm dotted #cbd5e1"></span>'
            f'<span style="font-size:7.6px;font-weight:900;color:{color}">ص {page_ref}</span></div>')


half = (len(toc_ar) + 1) // 2
half_i = (len(toc_isl) + 1) // 2
_SOM_BODY = f'''
{toc_section('الجزء الأول — اللغة العربية', 'var(--ar)', sep_ar_num)}
<div style="display:grid;grid-template-columns:1fr 1fr;gap:0 4mm;align-items:start">
  {toc_col(toc_ar[:half], 'var(--ar)')}
  {toc_col(toc_ar[half:], 'var(--ar)')}
</div>
{toc_section('الجزء الثاني — التربية الإسلامية', 'var(--is)', sep_isl_num)}
<div style="display:grid;grid-template-columns:1fr 1fr;gap:0 4mm;align-items:start">
  {toc_col(toc_isl[:half_i], 'var(--is)')}
  {toc_col(toc_isl[half_i:], 'var(--is)')}
</div>
<div class="scallop" style="margin-top:3mm">كل وحدة تبدأ بدرس <b>أتعلّم</b> مع رمز QR لفيديو الشرح، ثم <b>مثال محلول</b>، ثم <b>تمارين</b> متدرّجة (سهل / متوسط / صعب) يكتب فيها التلميذ بيده، وتنتهي بتقييم ذاتي.</div>'''

SOMMAIRE = page(1, 'الفهرس', _SOM_BODY, unit_label='دفتر ماجور · الفهرس')

HTML = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Cahier Major A5 — اللغة العربية والتربية الإسلامية · 6AF</title>
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&display=swap" rel="stylesheet">
<style>{CSS}{CSS_ASSETS}</style>
</head>
<body>
<div class="toolbar"><button class="action-btn" onclick="window.print()">🖨️ طباعة / PDF</button></div>
{COVER}
{SOMMAIRE}
{''.join(pages_html)}
<script>
/* Composition verticale A5 arabe/islamique : remplit les pages creuses,
   resserre les pages trop pleines, avant export PDF. */
(function(){{
  function composer(){{
    document.querySelectorAll('.sheet').forEach(function(sheet){{
      var body = sheet.querySelector('.page-body');
      if (!body) return;
      var st = getComputedStyle(body);
      if (st.justifyContent === 'center') return; /* couverture / ouvreurs */
      var kids = [].filter.call(body.children, function(c){{
        var cs = getComputedStyle(c);
        if (cs.position === 'absolute' || cs.display === 'none') return false;
        if (c.classList.contains('qr-corr') || c.classList.contains('qr-reserve')) return false;
        return c.getBoundingClientRect().height > 2;
      }});
      if (kids.length < 2) return;
      var br = body.getBoundingClientRect();
      var padB = parseFloat(st.paddingBottom) || 0;
      var reserve = body.querySelector('.qr-reserve');
      function contentFloor(){{
        /* bas utile = min(padding, réserve, haut QR, haut n° page) */
        var floor = br.bottom - padB;
        if (reserve) floor = Math.min(floor, reserve.getBoundingClientRect().top);
        var qrEl = sheet.querySelector('.qr-corr');
        if (qrEl) floor = Math.min(floor, qrEl.getBoundingClientRect().top - 8);
        var pnEl = sheet.querySelector('.bottom-number');
        if (pnEl) floor = Math.min(floor, pnEl.getBoundingClientRect().top - 6);
        return floor;
      }}
      function spareNow(){{
        var maxB = 0;
        kids.forEach(function(c){{ maxB = Math.max(maxB, c.getBoundingClientRect().bottom); }});
        return contentFloor() - maxB;
      }}
      function refreshKids(){{
        kids = [].filter.call(body.children, function(c){{
          var cs = getComputedStyle(c);
          if (cs.position === 'absolute' || cs.display === 'none') return false;
          if (c.classList.contains('qr-corr') || c.classList.contains('qr-reserve')) return false;
          return c.getBoundingClientRect().height > 2;
        }});
      }}
      function overlapsRect(el, zone, minArea){{
        if (!el || !zone) return false;
        var r = el.getBoundingClientRect();
        var left = Math.max(r.left, zone.left), top = Math.max(r.top, zone.top);
        var right = Math.min(r.right, zone.right), bottom = Math.min(r.bottom, zone.bottom);
        if (right <= left || bottom <= top) return false;
        return (right - left) * (bottom - top) >= (minArea || 40);
      }}
      function clearOverlayZones(){{
        var qr = sheet.querySelector('.qr-corr');
        var pn = sheet.querySelector('.bottom-number');
        var qrR = qr ? qr.getBoundingClientRect() : null;
        var pnR = pn ? pn.getBoundingClientRect() : null;
        /* bande verticale QR + marge (évite lignes sous le QR même sans collision H) */
        var qrBand = qrR ? (qrR.top - 6) : null;
        var pnBand = pnR ? (pnR.top - 4) : null;
        function invades(el){{
          var r = el.getBoundingClientRect();
          if (qrBand != null && r.bottom > qrBand) {{
            /* si l'élément est au-dessus du QR horizontalement, ok; sinon collision */
            if (!qrR || r.left < qrR.right + 4) return true;
          }}
          if (pnBand != null && r.bottom > pnBand) {{
            if (!pnR || !(r.right < pnR.left - 2 || r.left > pnR.right + 2)) return true;
          }}
          return false;
        }}
        for (var guard = 0; guard < 24; guard++) {{
          var hit = null;
          for (var i = kids.length - 1; i >= 0; i--) {{
            var c = kids[i];
            if (invades(c)) {{ hit = c; break; }}
            var innerHit = null;
            c.querySelectorAll('.line, .dotl, .wline').forEach(function(ln){{
              if (!innerHit && invades(ln)) innerHit = ln;
            }});
            if (innerHit) {{ hit = c; break; }}
          }}
          if (!hit) break;
          if (hit.classList.contains('composer-fill')) {{
            var fl = hit.querySelectorAll('.line');
            if (fl.length > 0) fl[fl.length - 1].remove();
            else hit.remove();
          }} else {{
            var lines = hit.querySelectorAll('.lines .line, .dotl, .wline');
            if (lines.length > 0) {{
              lines[lines.length - 1].remove();
            }} else {{
              var lh = hit.querySelectorAll('.line, .dotl, .wline');
              if (lh.length) {{
                lh.forEach(function(ln){{
                  var hh = ln.getBoundingClientRect().height || 8;
                  if (hh > 5.2) ln.style.height = Math.max(5, hh - 1.4) + 'px';
                }});
              }} else {{
                var mt = parseFloat(getComputedStyle(hit).marginTop) || 0;
                if (mt > 0) hit.style.marginTop = Math.max(0, mt - 2) + 'px';
                else {{
                  /* dernier recours : décaler hors bande QR */
                  hit.style.marginLeft = '22mm';
                  hit.style.maxWidth = 'calc(100% - 22mm)';
                  /* et réduire padding bas interne */
                  var pb = parseFloat(getComputedStyle(hit).paddingBottom) || 0;
                  if (pb > 2) hit.style.paddingBottom = Math.max(1, pb - 2) + 'px';
                }}
              }}
            }}
          }}
          refreshKids();
        }}
        /* garantir spare ≥ 2 au-dessus de la réserve */
        for (var g2 = 0; g2 < 16 && spareNow() < 2; g2++) {{
          var fillEl = body.querySelector('.composer-fill');
          if (fillEl) {{
            var fl2 = fillEl.querySelectorAll('.line');
            if (fl2.length) fl2[fl2.length - 1].remove();
            else fillEl.remove();
            refreshKids();
            continue;
          }}
          var cut = false;
          for (var j = kids.length - 1; j >= 0 && !cut; j--) {{
            var lines2 = kids[j].querySelectorAll('.lines .line, .dotl, .wline');
            if (lines2.length > 1) {{ lines2[lines2.length - 1].remove(); cut = true; }}
          }}
          if (!cut) {{
            body.querySelectorAll('.lines .line, .dotl, .wline').forEach(function(ln){{
              var h = ln.getBoundingClientRect().height || 8;
              if (h > 5.5) ln.style.height = Math.max(5.2, h - 1.2) + 'px';
            }});
          }}
          refreshKids();
        }}
      }}
      function isHeader(el){{
        return el.classList.contains('lesson-title') || el.classList.contains('unit-banner') ||
               el.classList.contains('objectifs') || el.classList.contains('badge-row');
      }}
      function isStretchable(el){{
        return el.matches('.frame, .exemple, .exo-card, .methode, .rule-box, .scallop, .ayah') ||
               (el.tagName === 'DIV' && !isHeader(el) &&
                !el.classList.contains('self-eval') &&
                !el.classList.contains('tip-card') &&
                !el.classList.contains('defi-card') &&
                !el.classList.contains('attention') &&
                !el.classList.contains('bulle-row'));
      }}
      var spare = spareNow();

      /* pages trop pleines */
      if (spare < -2) {{
        for (var pass = 0; pass < 4 && spare < -2; pass++) {{
          var share = (-spare) / Math.max(1, kids.length - 1);
          kids.forEach(function(c, i){{
            if (i === 0) return;
            var m = parseFloat(getComputedStyle(c).marginTop) || 0;
            var cut = Math.min(m, Math.max(share * 1.1, 1.5));
            if (cut > 0.3) c.style.marginTop = Math.max(0, m - cut) + 'px';
          }});
          kids.forEach(function(c){{
            if (!c.matches('.frame, .exo-card, .exemple, .badge-row, .objectifs, .unit-banner')) return;
            var pb = parseFloat(getComputedStyle(c).paddingBottom) || 0;
            var pt = parseFloat(getComputedStyle(c).paddingTop) || 0;
            var mb = parseFloat(getComputedStyle(c).marginBottom) || 0;
            if (pb > 3) c.style.paddingBottom = (pb - 1.5) + 'px';
            if (pt > 3) c.style.paddingTop = (pt - 1) + 'px';
            if (mb > 2) c.style.marginBottom = (mb - 1) + 'px';
          }});
          body.querySelectorAll('.lines .line, .dotl, .dots .dotl').forEach(function(ln){{
            var h = ln.getBoundingClientRect().height || 8;
            if (h > 7) ln.style.height = Math.max(5.5, h - 1.2) + 'px';
          }});
          spare = spareNow();
        }}
        return;
      }}

      /* pages creuses : remplir par lignes d'écriture (pas de gros vides entre blocs) */
      function growLines(budget){{
        var lines = body.querySelectorAll('.lines .line, .dotl, .wline');
        if (!lines.length || budget < 12) return budget;
        var per = Math.min(budget * 0.55 / lines.length, 7);
        lines.forEach(function(ln){{
          var h = ln.getBoundingClientRect().height || 7;
          ln.style.height = (h + per) + 'px';
        }});
        var s = spareNow();
        if (s < -1) {{
          var back = Math.min(per, (-s) / lines.length + 0.5);
          lines.forEach(function(ln){{
            var h = ln.getBoundingClientRect().height || 7;
            ln.style.height = Math.max(5.5, h - back) + 'px';
          }});
          s = spareNow();
        }}
        return s;
      }}
      function injectFillLines(budget){{
        if (budget < 70) return budget;
        if (body.querySelector('.composer-fill')) return spareNow();
        var lineH = 22; /* ~5.8mm */
        var n = Math.min(10, Math.max(4, Math.floor((budget - 36) / lineH)));
        var fill = document.createElement('div');
        fill.className = 'composer-fill';
        var linesHtml = '';
        for (var li = 0; li < n; li++) linesHtml += '<div class="line"></div>';
        fill.innerHTML = '<div class="consigne">أطبّق ما تعلّمتُ في جملة مفيدة :</div><div class="lines">' + linesHtml + '</div>';
        var anchor = null;
        for (var i = kids.length - 1; i >= 0; i--) {{
          var c = kids[i];
          if (c.classList.contains('bulle-row') || c.classList.contains('tip-card') ||
              c.classList.contains('self-eval') || c.classList.contains('attention') ||
              c.classList.contains('warn-card') || c.classList.contains('defi-card')) {{
            anchor = c; break;
          }}
        }}
        if (anchor) body.insertBefore(fill, anchor);
        else if (reserve) body.insertBefore(fill, reserve);
        else body.appendChild(fill);
        refreshKids();
        return spareNow();
      }}
      if (spare > 36) {{
        spare = growLines(spare);
      }}
      var hasQR = !!sheet.querySelector('.qr-corr');
      var existingLines = body.querySelectorAll('.lines .line, .dotl, .wline').length;
      var injectMin = hasQR ? 150 : 95;
      if (spare > injectMin && existingLines < 6) {{
        spare = injectFillLines(spare);
        spare = growLines(spare);
      }}
      /* 2e passe si encore très creux (sans QR serré) */
      if (spare > (hasQR ? 130 : 90)) {{
        var fill2 = body.querySelector('.composer-fill .lines');
        if (fill2) {{
          var add = Math.min(hasQR ? 3 : 6, Math.floor(spare / 26));
          for (var ai = 0; ai < add; ai++) {{
            var d = document.createElement('div');
            d.className = 'line';
            fill2.appendChild(d);
          }}
          spare = spareNow();
          spare = growLines(spare);
        }}
      }}
      if (spare > 36) {{
        /* marges modestes uniquement entre blocs de contenu (pas les en-têtes) */
        var targets = [];
        kids.forEach(function(c, i){{
          if (i === 0) return;
          if (isHeader(c) || isHeader(kids[i - 1])) return;
          if (c.classList.contains('self-eval') || c.classList.contains('composer-fill')) return;
          if (c.classList.contains('tip-card') || c.classList.contains('defi-card')) return;
          if (c.classList.contains('attention') || c.classList.contains('warn-card')) return;
          if (c.classList.contains('bulle-row')) return;
          targets.push(c);
        }});
        if (targets.length) {{
          var extra = Math.min(spare / targets.length, 8);
          targets.forEach(function(c){{
            var m = parseFloat(getComputedStyle(c).marginTop) || 0;
            c.style.marginTop = (m + extra) + 'px';
          }});
          spare = spareNow();
        }}
      }}
      /* ne pas étirer le fill sous la zone QR */
      if (spare > 40 && !hasQR) {{
        var stretch = body.querySelector('.composer-fill');
        if (stretch) stretch.style.flexGrow = '1';
      }}
      if (spare > 28 && spare < 200 && !hasQR) {{
        var cushion = Math.min(14, Math.max(4, spare * 0.2));
        body.style.paddingBottom = (padB + cushion) + 'px';
        padB += cushion;
        spare = spareNow();
      }}

      /* passe finale : jamais chevaucher zone QR / bas de page */
      for (var fix = 0; fix < 8 && spare < -1; fix++) {{
        var fillEl = body.querySelector('.composer-fill');
        if (fillEl) {{
          var flines = fillEl.querySelectorAll('.line');
          if (flines.length > 2) {{
            flines[flines.length - 1].remove();
          }} else {{
            fillEl.remove();
          }}
          refreshKids();
          spare = spareNow();
          continue;
        }}
        body.querySelectorAll('.lines .line, .dotl, .wline').forEach(function(ln){{
          var h = ln.getBoundingClientRect().height || 8;
          if (h > 6) ln.style.height = Math.max(5.5, h - 1.5) + 'px';
        }});
        var pbNow = parseFloat(getComputedStyle(body).paddingBottom) || 0;
        var floorPad = hasQR ? 40 : 32;
        if (pbNow > floorPad) {{
          body.style.paddingBottom = Math.max(floorPad, pbNow - 8) + 'px';
          padB = parseFloat(getComputedStyle(body).paddingBottom) || padB;
        }}
        spare = spareNow();
      }}

      /* dernière touche : pages encore un peu creuses */
      if (spare > 58) {{
        var fillMore = body.querySelector('.composer-fill .lines');
        if (fillMore) {{
          var nAdd = Math.min(hasQR ? 2 : 4, Math.floor((spare - 20) / 24));
          for (var bi = 0; bi < nAdd; bi++) {{
            var ld = document.createElement('div');
            ld.className = 'line';
            fillMore.appendChild(ld);
          }}
          spare = spareNow();
        }} else if (!hasQR && spare > 90) {{
          spare = injectFillLines(spare);
        }}
        spare = growLines(spare);
        for (var fix2 = 0; fix2 < 4 && spare < -1; fix2++) {{
          var fm = body.querySelector('.composer-fill');
          if (!fm) break;
          var fls = fm.querySelectorAll('.line');
          if (fls.length > 2) fls[fls.length - 1].remove();
          else fm.remove();
          spare = spareNow();
        }}
      }}
      clearOverlayZones();
    }});
  }}
  function run(){{
    function go(){{ composer(); }}
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(go);
    else go();
  }}
  window.__majorComposer = composer;
  window.addEventListener('beforeprint', function(){{ composer(); }});
  if (document.readyState === 'complete') run();
  else window.addEventListener('load', run);
}})();
</script>
</body>
</html>'''

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'livrables', 'Cahier-Major-Arabe-Islamique-6AF-A5.SOURCE.html')
out = os.path.normpath(out)
open(out, 'w').write(HTML)
print(f'écrit: {out} ({len(HTML)/1024:.0f} Ko, {2 + len(pages_html)} pages A5)')
