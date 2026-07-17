# -*- coding: utf-8 -*-
"""Assemble le cahier A5 combiné : couverture + sommaire + partie رياضيات (31 unités)
+ partie علوم (6 chapitres du pptx كراسة العلوم الطبيعية)."""
import re
from base_a5 import (CSS, CSS_ASSETS, WAVE_SVG, page, unit_banner, edge_band,
                     bar_model, bar_compare, number_bond, obj_groups, sg_box, bulle, MX)
from qr_major import lesson_qr_img, correction_qr_card

_FAKE_QR = '<span class="im im-qr qr" role="img" aria-label="QR فيديو الدرس"></span>'


def wire_qr(body, part, num):
    """Remplace le QR décoratif du video_box par le QR leçon réel de l'unité,
    et ajoute la carte QR correction sur les pages تمارين/مسائل."""
    body = body.replace(_FAKE_QR, lesson_qr_img(part, num))
    if '<div class="badge">تمارين' in body or '<div class="badge">مسائل' in body:
        body += correction_qr_card(part, num)
    return body

# ─── isolation bidi : « 4 km = … m » doit rester un bloc LTR dans le flux RTL ───
_UNIT = r'(?:km/h|m/s|km[²³]|hm[²³]|dam[²³]|dm[²³]|cm[²³]|mm[²³]|m[²³]|km|hm|dam|dm|cm|mm|kg|hg|dag|dg|cg|mg|hL|daL|dL|cL|mL|ha|ca|min|[mgtqLhsaj])'
_NUM = r'(?:\d{1,3}(?: \d{3})+(?:,\d+)?|\d+(?:[.,]\d+)?)'
_ITEM = rf'{_NUM}\s*{_UNIT}(?![A-Za-z0-9²³])'
_GROUPED = r'\d{1,3}(?: \d{3})+(?:,\d+)?'  # 12 000 · 3 000 000 : sans isolation LTR, le RTL inverse les groupes
_ATOM = rf'(?:{_ITEM}|{_NUM}|{_UNIT}(?![A-Za-z0-9²³])|\.{{2,}}|[=+−×÷])'
_START = rf'(?:{_ITEM}|{_GROUPED}|{_UNIT}(?![A-Za-z0-9²³]) *(?==))'
_CHAIN = re.compile(rf'(?<![A-Za-z0-9²³.,]){_START}(?: *{_ATOM})*')

def bidi_wrap(html):
    """Enveloppe chaque expression nombre+unité (et ses suites =, +, …, unités) dans
    un span.mexp (direction:ltr isolé) — hors <style>/<svg>/<script> et hors .mexp existants."""
    parts = re.split(r'(<[^>]+>)', html)
    out, skip, in_mexp = [], 0, 0
    for p in parts:
        if p.startswith('<'):
            low = p.lower()
            if low.startswith(('<style', '<svg', '<script')):
                skip += 1
            elif low.startswith(('</style', '</svg', '</script')):
                skip -= 1
            elif in_mexp:
                if low.startswith('<span'):
                    in_mexp += 1
                elif low.startswith('</span'):
                    in_mexp -= 1
            elif low.startswith('<span class="mexp"'):
                in_mexp = 1
            out.append(p)
        else:
            out.append(p if (skip or in_mexp) else
                       _CHAIN.sub(lambda m: f'<span class="mexp">{m.group(0)}</span>', p))
    return ''.join(out)
from unites_1 import UNITS_1
from unites_2 import UNITS_2
from unites_3 import UNITS_3
from unites_4 import UNITS_4
from unites_5 import UNITS_5
from sciences_1 import UNITS_S1
from sciences_2 import UNITS_S2

MATH_UNITS = UNITS_1 + UNITS_2 + UNITS_3 + UNITS_4 + UNITS_5
SCI_UNITS = UNITS_S1 + UNITS_S2


def part_page(num, emoji, kicker, title, sub, chips, color, part=''):
    """Page séparatrice de partie (numérotée, pagination continue)."""
    chips_html = ''.join(f'<span style="background:#fff;border:1.2px solid rgba(0,0,0,.12);border-radius:999px;padding:1.4mm 3.6mm;font-size:8.6px;font-weight:900;color:#4a3a1c">{c}</span>' for c in chips)
    body = f'''<div class="sheet">
  <div class="sheet-inner" style="justify-content:center;align-items:center;text-align:center">
    <div style="font-size:34px">{emoji}</div>
    <div style="font-size:10px;font-weight:900;color:#8a7a5c;letter-spacing:.5px;margin:2mm 0 1mm">{kicker}</div>
    <h1 style="font-size:27px;color:var(--orange);font-weight:900;margin:0 0 2mm">{title}</h1>
    <p style="font-size:9.6px;font-weight:800;color:#6b5d3f;margin:0 0 5mm;max-width:110mm;line-height:1.7">{sub}</p>
    <div style="display:flex;gap:2.4mm;flex-wrap:wrap;justify-content:center;max-width:118mm">{chips_html}</div>
    <div style="width:60mm;height:2.2mm;border-radius:999px;background:{color};margin-top:7mm"></div>
  </div>
  {edge_band(part)}
  <div class="page-footer"><span>دفتر ماجور · الرياضيات والعلوم</span><span>🇲🇷 السنة السادسة الأساسية 6AF</span></div>
  <div class="pageno {part}">{num}</div>
</div>'''
    return body


# ─── pagination : couverture = page de garde (non numérotée), sommaire = p.1 ───
toc_math, toc_sci = [], []
pages_html = []
num = 2  # 1 = sommaire

# séparateur partie 1
sep_math_num = num
pages_html.append(part_page(num, '🔢', 'الجزء الأول', 'الرياضيات',
    'الأعداد والعمليات · الكسور والأعداد العشرية · المسائل العملية · القياس والهندسة',
    [f'{len(MATH_UNITS)} وحدة', 'أُشاهد · أرسم · أحسب 🧩', 'تمارين متدرّجة ⭐⭐⭐', 'فيديو لكل درس 📱'], 'var(--p-yell)', part='math'))
num += 1

# ─── page méthode : أُشاهد ← أرسم ← أحسب, dans la voix du maître (sans nommer de méthode) ───
def sg_method_page():
    def step_card(n, emoji, word, sub, color):
        return f'''<div style="background:{color};border-radius:4mm;padding:2.2mm 1.6mm 1.8mm;text-align:center">
          <div style="width:7mm;height:7mm;border-radius:50%;background:#fff;margin:0 auto .8mm;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:11px;color:#c9711a;box-shadow:inset 0 -1.5px 0 rgba(0,0,0,.1)">{n}</div>
          <div style="font-size:16px;line-height:1">{emoji}</div>
          <div style="font-weight:900;font-size:13.5px;color:#3a2f18;margin-top:.6mm">{word}</div>
          <div style="font-size:8.4px;font-weight:800;color:#6b5d3f;line-height:1.5">{sub}</div>
        </div>'''
    arrow = '<div style="display:flex;align-items:center;justify-content:center;font-size:15px;font-weight:900;color:#f28a15">⬅</div>'
    GRID3 = 'display:grid;grid-template-columns:1fr 6.5mm 1fr 6.5mm 1fr;gap:1mm;align-items:center'
    steps = f'''<div style="{GRID3};align-items:stretch;margin:1.4mm 0">
      {step_card(1, '👀', 'أُشاهد', 'أقرأ المسألة جيدًا وأتخيّلها', 'var(--p-yell)')}{arrow}
      {step_card(2, '✏️', 'أرسم', 'أحوّلها إلى نموذج الشريط', 'var(--p-blue)')}{arrow}
      {step_card(3, '🔢', 'أحسب', 'النموذج يدلّني على العملية', 'var(--p-green)')}
    </div>'''
    demo = f'''<div style="background:#fff;border:1.4px solid #eadfc4;border-radius:4mm;padding:2mm 2.4mm;margin:1.4mm 0">
      <div style="text-align:center;font-weight:900;font-size:10.5px;color:#8a4a12">🌰 نجرّب معًا: عندنا 3 أطباق، في كل طبق 4 تمرات. كم تمرة عندنا؟</div>
      <div style="{GRID3}">
        <div>{obj_groups(3, 4, '🌰')}</div><div></div>
        <div>{bar_model('المجموع ؟', [('طبق', 4, '#aae4f0'), ('طبق', 4, '#c6e9a4'), ('طبق', 4, '#ffd98c')], w=40)}</div><div></div>
        <div style="text-align:center;font-weight:900">
          <div style="font-size:16px">{MX('3 × 4 = 12')}</div>
          <div style="font-size:9.4px;color:#2f8f5b;margin-top:1mm">✅ عندنا 12 تمرة</div>
        </div>
      </div>
    </div>'''
    def model_card(chip, chipbg, content):
        return f'''<div style="background:#fff;border:1.4px solid #eadfc4;border-radius:4mm;padding:1.6mm 2mm 1mm;text-align:center">
          <span style="display:inline-block;background:{chipbg};border-radius:999px;padding:.6mm 3.6mm;font-weight:900;font-size:8.8px;color:#3a2f18">{chip}</span>
          {content}
        </div>'''
    models = f'''<div style="display:flex;align-items:center;gap:2.4mm;margin:2mm 0 1.2mm">
      <span class="sg-pill" style="font-size:8.6px">🧩 نموذج الشريط — صديقك في كل مسألة</span>
      <span style="flex:1;border-bottom:1.4px dotted #d8c9a4"></span>
    </div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:2mm">
      {model_card('➕ أبحث عن الكل', 'var(--p-blue)',
                  bar_model('الكل = ؟', [('عندي', 320, '#8fd4e8'), ('اشتريت', 150, '#f5b34c')], w=52, stagger=False))}
      {model_card('➖ أبحث عن الفرق', 'var(--p-rose)', bar_compare('أحمد', 470, 'مريم', 320, w=52))}
      {model_card('✖️ حصص متساوية', 'var(--p-green)',
                  bar_model('؟', [('حصة', 8, '#c6e9a4'), ('حصة', 8, '#c6e9a4'), ('حصة', 8, '#c6e9a4'), ('حصة', 8, '#c6e9a4')], w=52, stagger=False))}
      {model_card('➗ أوزّع الكل بالتساوي', 'var(--p-lila)',
                  bar_model('الكل = 24', [('؟', 6, '#e6c7f2', '؟'), ('؟', 6, '#e6c7f2', '؟'), ('؟', 6, '#e6c7f2', '؟'), ('؟', 6, '#e6c7f2', '؟')], w=52, stagger=False))}
    </div>'''
    body = f'''
{bulle('garcon', 'يقول أستاذ ماجور: يا أبطالي، المسألة ليست كلمات صعبة — إنها <b>صورة</b>! قاعدتنا الذهبية في ثلاث خطوات:')}
{steps}
{demo}
{models}
{bulle('fille', 'أضع ما أعرفه في الشريط، وأضع <b style="color:#c0392b">؟</b> مكان ما أبحث عنه — ثم يظهر الحل أمامي!')}'''
    return page(num, 'كيف أحلّ أي مسألة؟ 🧩', body, unit_label='طريقتنا في التعلّم', part='math')

pages_html.append(sg_method_page())
num += 1

for u in MATH_UNITS:
    toc_math.append((u['num'], u['title'], num))
    first = True
    for title, body, with_eval in u['pages']:
        if first:
            body = unit_banner(u['num'], f"الوحدة {u['num']} — {u['title']}", u['sub'], u['color']) + body
            first = False
        body = wire_qr(body, 'math', u['num'])
        label = f"الوحدة {u['num']} · {u['title']}"
        pages_html.append(page(num, title, body, unit_label=label, with_eval=with_eval, part='math'))
        num += 1

# séparateur partie 2
sep_sci_num = num
pages_html.append(part_page(num, '🌿', 'الجزء الثاني', 'العلوم الطبيعية',
    'التوازن الغذائي والطاقوي · التصحر والتلوث · الماء والصحة · التطعيم',
    [f'{len(SCI_UNITS)} فصول', 'تمارين متدرّجة ⭐⭐⭐', 'أمثلة محلولة ✏️', 'فيديو لكل درس 📱'], 'var(--p-green)', part='sci'))
num += 1

for u in SCI_UNITS:
    toc_sci.append((u['num'], u['title'], num))
    first = True
    for title, body, with_eval in u['pages']:
        if first:
            body = unit_banner(u['num'], f"الفصل {u['num']} — {u['title']}", u['sub'], u['color']) + body
            first = False
        body = wire_qr(body, 'sci', u['num'])
        label = f"العلوم · الفصل {u['num']} · {u['title']}"
        pages_html.append(page(num, title, body, unit_label=label, with_eval=with_eval, part='sci'))
        num += 1

COVER = f'''<div class="sheet cover">
  <div class="sheet-inner">
    <span class="im im-logo cover-logo" role="img" aria-label="Major"></span>
    <h1 style="font-size:29px">الرياضيات والعلوم</h1>
    <p class="sub">دفتر ماجور · السنة السادسة الأساسية 6AF</p>
    <div class="cover-band">
      <span>🇲🇷 موريتانيا · البرنامج الرسمي كاملًا</span>
      <span>🧩 أُشاهد · أرسم · أحسب</span>
      <span>31 وحدة رياضيات</span>
      <span>6 فصول علوم</span>
      <span>تمارين متدرّجة ⭐⭐⭐</span>
    </div>
    <div class="cover-cards">
      <div class="cover-card" style="background:var(--p-yell)">
        <b>🔢 الأعداد والعمليات</b>
        <span>الأعداد الكبيرة · الجمع والطرح · الضرب والقسمة · قابلية القسمة · ×10 و100 و1000</span>
      </div>
      <div class="cover-card" style="background:var(--p-rose)">
        <b>🍰 الكسور والأعداد العشرية</b>
        <span>الكسور ومقارنتها · المتكافئة · ضربها وقسمتها · الأعداد العشرية والنسب المئوية</span>
      </div>
      <div class="cover-card" style="background:var(--p-blue)">
        <b>💰📐 المسائل · القياس والهندسة</b>
        <span>الشراء والبيع بالأوقية · التناسبية · السرعة · الأطوال والكتل والزمن · المساحات والحجوم</span>
      </div>
      <div class="cover-card" style="background:var(--p-green)">
        <b>🌿 العلوم الطبيعية</b>
        <span>التوازن الغذائي والطاقوي · التصحر · التلوث · الماء والصحة · التطعيم</span>
      </div>
    </div>
    <div class="owner-line">✏️ هذا الدفتر ملك للتلميذ(ة): <i></i> القسم: <i style="max-width:22mm"></i></div>
    <div class="cover-mascots">
      <span class="im im-fille" role="img"></span>
      <span class="im im-garcon" role="img"></span>
    </div>
  </div>
  <div class="wave">{WAVE_SVG}</div>
</div>'''

def toc_col(rows):
    return '<table class="toc" style="font-size:8.2px">' + ''.join(
        f'<tr><td style="width:7mm;padding:1mm 1mm"><span class="tno" style="width:5mm;height:5mm;font-size:7.5px">{n}</span></td>'
        f'<td style="padding:1mm 1mm;font-size:8.2px">{t}</td>'
        f'<td class="tp" style="padding:1mm 1mm">{p}</td></tr>'
        for n, t, p in rows) + '</table>'

def toc_section(label, color, page_ref):
    return (f'<div style="display:flex;align-items:center;gap:2mm;margin:1.6mm 0 .6mm">'
            f'<span style="background:{color};border-radius:999px;padding:.8mm 4mm;font-size:9px;font-weight:900;color:#4a3a1c">{label}</span>'
            f'<span style="flex:1;border-bottom:1.4px dotted #d8c9a4"></span>'
            f'<span style="font-size:8.5px;font-weight:900;color:var(--blue)">ص {page_ref}</span></div>')

half = (len(toc_math) + 1) // 2
half_s = (len(toc_sci) + 1) // 2
SOMMAIRE = f'''<div class="sheet">
  <div class="sheet-inner">
    <div class="head">
      <div class="doc-id">دفتر ماجور · الرياضيات والعلوم<br>السنة السادسة الأساسية 6AF</div>
      <span class="im im-logo logo" role="img" aria-label="Major"></span>
    </div>
    <h2 class="lesson-title">📖 الفهرس</h2>
    {toc_section('🔢 الجزء الأول — الرياضيات', 'var(--p-yell)', sep_math_num)}
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:0 4mm;align-items:start">
      {toc_col(toc_math[:half])}
      {toc_col(toc_math[half:])}
    </div>
    {toc_section('🌿 الجزء الثاني — العلوم الطبيعية', 'var(--p-green)', sep_sci_num)}
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:0 4mm;align-items:start">
      {toc_col(toc_sci[:half_s])}
      {toc_col(toc_sci[half_s:])}
    </div>
    <div class="scallop" style="margin-top:auto">كل وحدة تبدأ بدرس <b>أتعلّم</b> مع رمز QR لفيديو الشرح 📱، ثم <b>مثال محلول</b> ✏️، ثم <b>تمارين</b> متدرّجة من ⭐ إلى ⭐⭐⭐، وتنتهي بتقييم ذاتي 🌟 — وتذكّر قاعدتنا الذهبية 🧩: أُشاهد ← أرسم نموذج الشريط ← أحسب.</div>
  </div>
  <div class="pageno">1</div>
</div>'''

HTML = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Cahier Major A5 — الرياضيات والعلوم · 6AF</title>
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&family=Lateef:wght@400;600;700;800&display=swap" rel="stylesheet">
<style>{CSS}{CSS_ASSETS}</style>
</head>
<body>
<div class="toolbar"><button class="action-btn" onclick="window.print()">🖨️ طباعة / PDF</button></div>
{COVER}
{SOMMAIRE}
{''.join(pages_html)}
</body>
</html>'''

HTML = bidi_wrap(HTML)

import os
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'livrables', 'Cahier-Major-Math-Sciences-6AF-A5.SOURCE.html')
out = os.path.normpath(out)
open(out, 'w').write(HTML)
print(f'écrit: {out} ({len(HTML)/1024:.0f} Ko, {2 + len(pages_html)} pages A5)')
