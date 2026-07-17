# -*- coding: utf-8 -*-
"""Assemble le cahier A5 عربية/إسلامية : couverture + فهرس + partie اللغة العربية (18 unités)
+ partie التربية الإسلامية (8 فصول). Style « dfatir Major » du cahier A4 original
(dos relié bleu nuit, onglets, cartes d'exercices à lignes d'écriture)."""
import os

from base_ai import CSS, CSS_ASSETS, DOC_ID, page, unit_banner, spine, tabs
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

_PART_GRAD = {'ar': 'linear-gradient(150deg,#4c1d95 0%,#7c3aed 55%,#a78bfa 100%)',
              'isl': 'linear-gradient(150deg,#064e3b 0%,#059669 55%,#34d399 100%)'}


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
  {tabs(part)}
</div>'''


# ─── pagination : couverture = page de garde, فهرس = p.1 ───
toc_ar, toc_isl = [], []
pages_html = []
num = 2

# séparateur partie 1 — اللغة العربية
sep_ar_num = num
pages_html.append(part_page(num, '🔤', 'الجزء الأول', 'اللغة العربية',
    'النحو والصرف · الإملاء · المفردات · القراءة والفهم · التعبير الكتابي',
    [f'{len(AR_UNITS)} وحدة', 'تمارين متدرّجة ⭐⭐⭐', 'أمثلة محلولة ✏️', 'فيديو لكل درس 📱'], 'ar'))
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
pages_html.append(part_page(num, '☪️', 'الجزء الثاني', 'التربية الإسلامية',
    'العقيدة · الفقه · السيرة النبوية · الأخلاق والقيم',
    [f'{len(ISL_UNITS)} فصول', 'تمارين متدرّجة ⭐⭐⭐', 'الأدلة من الكتاب والسنة 📖', 'فيديو لكل درس 📱'], 'isl'))
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
    ('📘', 'النحو والصرف', 'أنواع الكلمة · الإعراب · الجملتان · الأفعال الخمسة · النواسخ · الحال والتمييز'),
    ('✍️', 'الإملاء والمفردات', 'الهمزات · التاء والألف · الشدة والتنوين · المعنى والضد والمرادف'),
    ('📖', 'القراءة والتعبير', 'نصوص موريتانية بأسئلة المسابقة · منهجية الفقرة · نموذج امتحان كامل'),
    ('☪️', 'التربية الإسلامية', 'الأركان · الطهارة والصلاة · الزكاة والصوم والحج · السيرة · الأخلاق'),
]
_cover_cards_html = ''.join(
    f'''<div style="background:rgba(255,255,255,.12);border:.35mm solid rgba(255,255,255,.18);border-radius:4mm;
        padding:2.6mm 3mm;display:flex;flex-direction:column;gap:.8mm;direction:rtl">
      <span style="font-size:14px">{e}</span>
      <strong style="font-size:9.5px;font-weight:900">{t}</strong>
      <span style="font-size:6.8px;line-height:1.55;color:rgba(255,255,255,.87)">{s}</span>
    </div>''' for e, t, s in _COVER_CARDS)

_band = ''.join(
    f'<span style="background:#fff;color:#0f172a;padding:1.4mm 3.2mm;border-radius:999px;font-size:7px;font-weight:900">{c}</span>'
    for c in ['🇲🇷 موريتانيا · تحضير المسابقة الوطنية', f'{len(AR_UNITS)} وحدة عربية',
              f'{len(ISL_UNITS)} فصول إسلامية', 'تمارين متدرّجة ⭐⭐⭐'])

COVER = f'''<div class="sheet">
  <div class="page-main" style="background:linear-gradient(135deg,#182b66 0%,#2563eb 48%,#38bdf8 100%);color:#fff">
    <div class="page-body" style="display:flex;flex-direction:column;justify-content:center;padding:7mm 8mm">
      <div style="position:absolute;width:52mm;height:52mm;border-radius:50%;background:rgba(255,255,255,.1);left:-16mm;top:8mm"></div>
      <div style="position:absolute;width:44mm;height:44mm;border-radius:50%;background:rgba(255,255,255,.1);right:-14mm;bottom:-14mm"></div>
      <div style="display:flex;justify-content:space-between;align-items:flex-start">
        <span style="display:inline-flex;background:rgba(255,255,255,.14);border:.35mm solid rgba(255,255,255,.2);padding:1.6mm 3.6mm;border-radius:999px;font-size:7.6px;font-weight:900;letter-spacing:.5px">موريتانيا · 6AF · 2025-2026</span>
        <span class="im im-logo" role="img" aria-label="Major" style="width:17mm;height:17mm;background-color:rgba(255,255,255,.96);padding:1.6mm;border-radius:4mm;box-shadow:0 3px 8px rgba(15,23,42,.25)"></span>
      </div>
      <h1 style="margin:5mm 0 1.6mm;font-size:30px;line-height:1.05;font-weight:900">دفتر <span style="color:#fde68a">ماجور</span></h1>
      <p style="font-size:11px;color:rgba(255,255,255,.9);margin:0 0 4mm;font-weight:800">اللغة العربية والتربية الإسلامية · السنة السادسة الأساسية</p>
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
{toc_section('🔤 الجزء الأول — اللغة العربية', 'var(--ar)', sep_ar_num)}
<div style="display:grid;grid-template-columns:1fr 1fr;gap:0 4mm;align-items:start">
  {toc_col(toc_ar[:half], 'var(--ar)')}
  {toc_col(toc_ar[half:], 'var(--ar)')}
</div>
{toc_section('☪️ الجزء الثاني — التربية الإسلامية', 'var(--is)', sep_isl_num)}
<div style="display:grid;grid-template-columns:1fr 1fr;gap:0 4mm;align-items:start">
  {toc_col(toc_isl[:half_i], 'var(--is)')}
  {toc_col(toc_isl[half_i:], 'var(--is)')}
</div>
<div class="scallop" style="margin-top:3mm">كل وحدة تبدأ بدرس <b>أتعلّم</b> مع رمز QR لفيديو الشرح 📱، ثم <b>مثال محلول</b> ✏️، ثم <b>تمارين</b> متدرّجة من ⭐ إلى ⭐⭐⭐ يكتب فيها التلميذ بيده، وتنتهي بتقييم ذاتي. 🌟</div>'''

SOMMAIRE = page(1, '📖 الفهرس', _SOM_BODY, unit_label='دفتر ماجور · الفهرس')

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
</body>
</html>'''

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'livrables', 'Cahier-Major-Arabe-Islamique-6AF-A5.SOURCE.html')
out = os.path.normpath(out)
open(out, 'w').write(HTML)
print(f'écrit: {out} ({len(HTML)/1024:.0f} Ko, {2 + len(pages_html)} pages A5)')
