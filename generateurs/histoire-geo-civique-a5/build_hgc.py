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
    return f'''<div class="sheet part-{part}">
  {spine()}
  <div class="page-main" style="background:{_PART_GRAD[part]};color:#fff">
    <div class="page-body" style="display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center">
      <div style="position:absolute;width:46mm;height:46mm;border-radius:50%;background:rgba(255,255,255,.09);top:-16mm;left:-12mm"></div>
      <div style="position:absolute;width:34mm;height:34mm;border-radius:50%;background:rgba(255,255,255,.09);bottom:-10mm;right:-8mm"></div>
      <div style="font-size:33px">{emoji}</div>
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
        [f'{n_units} وحدة', 'خرائط ورسوم في كل درس 🗺️', 'تمارين متدرّجة ⭐⭐⭐', 'فيديو لكل درس 📱'], part))
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
    ('🏰', 'التاريخ', 'السيرة النبوية والخلافة · الحضارة الإسلامية · المرابطون والإمارات · المقاومة والاستقلال'),
    ('🗺️', 'الجغرافيا', 'الموقع والحدود · التضاريس والمناخ · السكان والمدن · الثروات — مع خرائط تكملها بيدك'),
    ('🤝', 'التربية المدنية', 'الدولة ورموزها · الدستور والمؤسسات · حقوق الطفل · المنظمات الدولية'),
    ('📱', 'ماجور الذكي', 'رمز QR في كل درس: فيديو الشرح · تصحيح تمارينك بالذكاء الاصطناعي · تدريب فوري'),
]
_cover_cards_html = ''.join(
    f'''<div style="background:rgba(255,255,255,.12);border:.35mm solid rgba(255,255,255,.18);border-radius:4mm;
        padding:2.6mm 3mm;display:flex;flex-direction:column;gap:.8mm;direction:rtl">
      <span style="font-size:14px">{e}</span>
      <strong style="font-size:9.5px;font-weight:900">{t}</strong>
      <span style="font-size:6.8px;line-height:1.55;color:rgba(255,255,255,.87)">{s}</span>
    </div>''' for e, t, s in _COVER_CARDS)

_n_hg = len(UNITS_HIST) + len(UNITS_GEO)
_band = ''.join(
    f'<span style="background:#fff;color:#0f172a;padding:1.4mm 3.2mm;border-radius:999px;font-size:7px;font-weight:900">{c}</span>'
    for c in ['🇲🇷 موريتانيا · تحضير المسابقة الوطنية', f'{_n_hg} وحدة تاريخ وجغرافيا',
              f'{len(UNITS_CIV)} وحدات مدنية', 'خرائط وفرائز زمنية 🗺️'])

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
        ✏️ هذا الدفتر ملك للتلميذ(ة): <span style="flex:1;border-bottom:.5mm dashed #94a3b8"></span>
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
{toc_section('🏰 الجزء الأول — التاريخ', '#b45309', sep_nums['hist'])}
{_two_cols(toc['hist'], '#b45309')}
{toc_section('🗺️ الجزء الثاني — الجغرافيا', '#1d4ed8', sep_nums['geo'])}
{_two_cols(toc['geo'], '#1d4ed8')}
{toc_section('🤝 الجزء الثالث — التربية المدنية', '#0f7b3a', sep_nums['civ'])}
{_two_cols(toc['civ'], '#0f7b3a')}
<div class="scallop" style="margin-top:2.4mm">كل وحدة تبدأ بدرس <b>أتعلّم</b> مع خريطة أو رسم يوضح الفكرة ورمز QR لفيديو الشرح 📱، ثم <b>مثال محلول</b> ✏️، ثم <b>تمارين</b> متدرّجة من ⭐ إلى ⭐⭐⭐ فيها خرائط تكملها بيدك، وتنتهي بتقييم ذاتي. 🌟</div>'''

SOMMAIRE = page(1, '📖 الفهرس', _SOM_BODY, unit_label='دفتر ماجور · الفهرس')

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
<div class="toolbar"><button class="action-btn" onclick="window.print()">🖨️ طباعة / PDF</button></div>
{COVER}
{SOMMAIRE}
{''.join(pages_html)}
</body>
</html>'''

out = os.path.join(_HERE, '..', '..', 'livrables', 'Cahier-Major-HistGeo-Civique-6AF-A5.SOURCE.html')
out = os.path.normpath(out)
open(out, 'w').write(HTML)
print(f'écrit: {out} ({len(HTML)/1024:.0f} Ko, {2 + len(pages_html)} pages A5)')
