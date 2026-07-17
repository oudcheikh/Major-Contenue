# -*- coding: utf-8 -*-
"""Assemble le cahier complet : couverture + 16 pages leçons."""
from cahier_base import ASSETS, CSS, CSS_ASSETS, WAVE_SVG, page
from lessons_a import LESSONS_A
from lessons_b import LESSONS_B

COVER = f'''<div class="sheet cover">
  <div class="sheet-inner">
    <span class="im im-logo cover-logo" role="img" aria-label="Major"></span>
    <h1>الرياضيات</h1>
    <p class="sub">دفتر ماجور · السنة السادسة الأساسية 6AF · بطريقة سنغافورة</p>
    <div class="cover-band">
      <span>🇲🇷 موريتانيا · تحضير المسابقة الوطنية</span>
      <span>16 درسًا</span>
      <span>تمارين متدرّجة ⭐⭐⭐</span>
    </div>
    <div class="cover-cards">
      <div class="cover-card" style="background:var(--p-yell)">
        <b>🔢 الأعداد والعمليات</b>
        <span>الأعداد الكبيرة · المقارنة والترتيب · الجمع والطرح · الضرب · القسمة</span>
      </div>
      <div class="cover-card" style="background:var(--p-rose)">
        <b>🍰 الكسور</b>
        <span>مفهوم الكسر ومقارنته · ضرب الكسور · قسمة الكسور</span>
      </div>
      <div class="cover-card" style="background:var(--p-green)">
        <b>💰 الأعداد العشرية والنسب</b>
        <span>الأعداد العشرية · النسبة المئوية · الشراء والبيع والربح</span>
      </div>
      <div class="cover-card" style="background:var(--p-blue)">
        <b>📐 القياس والهندسة</b>
        <span>الأطوال · الكتل · الزوايا · المستقيمات المتوازية والمتعامدة</span>
      </div>
    </div>
    <div class="frame" style="width:150mm;text-align:right">
      <ul style="font-size:11.5px">
        <li><b>طريقة سنغافورة:</b> نبدأ بالمحسوس 🧊 (أشياء حقيقية)، ثم المصوّر 🖼️ (نموذج الشريط، رابط العدد، الأقراص)، ثم المجرّد 🔢 (الأرقام والعمليات).</li>
        <li>كل درس: <b>أتعلّم</b> (القاعدة) ← <b>أمثّل</b> (الرسم والنماذج) ← <b>تمارين</b> متدرّجة من ⭐ إلى ⭐⭐⭐.</li>
        <li>امسح رمز QR في كل درس لمشاهدة فيديو الشرح، وقيّم نفسك في أسفل كل صفحة. 📱</li>
      </ul>
    </div>
    <div class="cover-mascots">
      <span class="im im-fille" role="img"></span>
      <span class="im im-garcon" role="img"></span>
    </div>
  </div>
  <div class="wave">{WAVE_SVG}</div>
</div>'''

pages_html = [COVER]
num = 1
for fn in LESSONS_A + LESSONS_B:
    title, body, foot = fn()
    pages_html.append(page(num, title, body, foot))
    num += 1

HTML = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Cahier Major — الرياضيات · 6AF · طريقة سنغافورة</title>
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&display=swap" rel="stylesheet">
<style>{CSS}{CSS_ASSETS}</style>
</head>
<body>
<div class="toolbar"><button class="action-btn" onclick="window.print()">🖨️ طباعة / PDF</button></div>
{''.join(pages_html)}
</body>
</html>'''

import os
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'archives', 'Cahier-Major-Math-6AF.SOURCE.html')
out = os.path.normpath(out)
open(out, 'w').write(HTML)
print(f'écrit: {out} ({len(HTML)/1024:.0f} Ko, {len(pages_html)} pages)')
