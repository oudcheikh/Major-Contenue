# -*- coding: utf-8 -*-
"""Assemble le cahier A5 combiné : couverture + sommaire + partie رياضيات (31 unités)
+ partie علوم (6 chapitres du pptx كراسة العلوم الطبيعية)."""
import re
from base_a5 import (CSS, CSS_ASSETS, WAVE_SVG, page, unit_banner, edge_band,
                     bar_model, bar_compare, number_bond, obj_groups, sg_box, bulle, MX,
                     logo_img, print_sanitize)
from qr_major import lesson_qr_img, correction_qr_card, _qr_b64, BASE_URL

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
    is_math = part == 'math'
    grad = ('linear-gradient(170deg,#fff6dd 0%,#ffe4a6 55%,#ffd082 100%)' if is_math
            else 'linear-gradient(170deg,#eff9e5 0%,#d6efbf 55%,#c0e7a3 100%)')
    accent = '#e07b00' if is_math else '#3e8e41'
    deep = '#7c4a00' if is_math else '#2c5f2f'
    mascot = 'im-fille' if is_math else 'im-garcon'
    chips = [print_sanitize(c) for c in chips]
    chips_html = ''.join(
        f'<span style="background:#fff;border-radius:999px;padding:1.7mm 4mm;'
        f'font-size:8.8px;font-weight:900;color:{deep}">{c}</span>' for c in chips)
    emoji_html = f'<div class="part-emoji" style="font-size:28px;font-weight:900;opacity:.9">{emoji}</div>' if emoji else ''
    body = f'''<div class="sheet">
  <div class="sheet-inner" style="padding:5mm 6mm 12mm">
    <div class="part-hero" style="background:{grad}">
      <div class="part-orb o1"></div><div class="part-orb o2"></div><div class="part-orb o3"></div>
      {emoji_html}
      <div class="part-kicker" style="background:{accent}">{kicker}</div>
      <h1 class="part-title" style="color:{deep}">{title}</h1>
      <p class="part-sub" style="color:{deep}">{sub}</p>
      <div class="part-chips">{chips_html}</div>
      <div class="part-mascots"><span class="im {mascot}" role="img" aria-label=""></span></div>
    </div>
  </div>
  {edge_band(part)}
  <div class="page-footer"><span>دفتر ماجور · الرياضيات والعلوم</span><span>السنة السادسة الأساسية 6AF</span></div>
  <div class="pageno {part}">{num}</div>
</div>'''
    return body


# ─── pagination : couverture = page de garde (non numérotée), sommaire = p.1 ───
toc_math, toc_sci = [], []
pages_html = []
num = 2  # 1 = sommaire

# séparateur partie 1
sep_math_num = num
pages_html.append(part_page(num, '1', 'الجزء الأول', 'الرياضيات',
    'الأعداد والعمليات · الكسور والأعداد العشرية · المسائل العملية · القياس والهندسة',
    [f'{len(MATH_UNITS)} وحدة', 'أُشاهد · أرسم · أحسب', 'تمارين: سهل / متوسط / صعب', 'فيديو لكل درس'], 'var(--p-yell)', part='math'))
num += 1

# ─── page méthode : أُشاهد ← أرسم ← أحسب, dans la voix du maître (sans nommer de méthode) ───
def sg_method_page():
    def step_card(n, word, sub, color):
        return f'''<div style="background:{color};border-radius:4mm;padding:2.2mm 1.6mm 1.8mm;text-align:center">
          <div style="width:7mm;height:7mm;border-radius:50%;background:#fff;margin:0 auto .8mm;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:11px;color:#c9711a;box-shadow:inset 0 -1.5px 0 rgba(0,0,0,.1)">{n}</div>
          <div style="font-weight:900;font-size:13.5px;color:#3a2f18;margin-top:.6mm">{word}</div>
          <div style="font-size:8.4px;font-weight:800;color:#6b5d3f;line-height:1.5">{sub}</div>
        </div>'''
    arrow = '<div style="display:flex;align-items:center;justify-content:center;font-size:15px;font-weight:900;color:#f28a15">←</div>'
    GRID3 = 'display:grid;grid-template-columns:1fr 6.5mm 1fr 6.5mm 1fr;gap:1mm;align-items:center'
    steps = f'''<div style="{GRID3};align-items:stretch;margin:1.4mm 0">
      {step_card(1, 'أُشاهد', 'أقرأ المسألة جيدًا وأتخيّلها', 'var(--p-yell)')}{arrow}
      {step_card(2, 'أرسم', 'أحوّلها إلى نموذج الشريط', 'var(--p-blue)')}{arrow}
      {step_card(3, 'أحسب', 'النموذج يدلّني على العملية', 'var(--p-green)')}
    </div>'''
    demo = f'''<div style="background:#fff;border:1.4px solid #eadfc4;border-radius:4mm;padding:2mm 2.4mm;margin:1.4mm 0">
      <div style="text-align:center;font-weight:900;font-size:10.5px;color:#8a4a12">نجرّب معًا: عندنا 3 أطباق، في كل طبق 4 تمرات. كم تمرة عندنا؟</div>
      <div style="{GRID3}">
        <div>{obj_groups(3, 4, '•')}</div><div></div>
        <div>{bar_model('المجموع ؟', [('طبق', 4, '#aae4f0'), ('طبق', 4, '#c6e9a4'), ('طبق', 4, '#ffd98c')], w=40)}</div><div></div>
        <div style="text-align:center;font-weight:900">
          <div style="font-size:16px">{MX('3 × 4 = 12')}</div>
          <div style="font-size:9.4px;color:#2f8f5b;margin-top:1mm">صح — عندنا 12 تمرة</div>
        </div>
      </div>
    </div>'''
    def model_card(chip, chipbg, content):
        return f'''<div style="background:#fff;border:1.4px solid #eadfc4;border-radius:4mm;padding:1.6mm 2mm 1mm;text-align:center">
          <span style="display:inline-block;background:{chipbg};border-radius:999px;padding:.6mm 3.6mm;font-weight:900;font-size:8.8px;color:#3a2f18">{chip}</span>
          {content}
        </div>'''
    models = f'''<div style="display:flex;align-items:center;gap:2.4mm;margin:2mm 0 1.2mm">
      <span class="sg-pill" style="font-size:8.6px">نموذج الشريط — صديقك في كل مسألة</span>
      <span style="flex:1;border-bottom:1.4px dotted #d8c9a4"></span>
    </div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:2mm">
      {model_card('أبحث عن الكل', 'var(--p-blue)',
                  bar_model('الكل = ؟', [('عندي', 320, '#8fd4e8'), ('اشتريت', 150, '#f5b34c')], w=52, stagger=False))}
      {model_card('أبحث عن الفرق', 'var(--p-rose)', bar_compare('أحمد', 470, 'مريم', 320, w=52))}
      {model_card('حصص متساوية', 'var(--p-green)',
                  bar_model('؟', [('حصة', 8, '#c6e9a4'), ('حصة', 8, '#c6e9a4'), ('حصة', 8, '#c6e9a4'), ('حصة', 8, '#c6e9a4')], w=52, stagger=False))}
      {model_card('أوزّع الكل بالتساوي', 'var(--p-lila)',
                  bar_model('الكل = 24', [('', 6, '#e6c7f2', '؟'), ('', 6, '#e6c7f2', '؟'), ('', 6, '#e6c7f2', '؟'), ('', 6, '#e6c7f2', '؟')], w=52, stagger=False))}
    </div>'''
    body = f'''
{bulle('garcon', 'يقول أستاذ ماجور: يا أبطالي، المسألة ليست كلمات صعبة — إنها <b>صورة</b>! قاعدتنا الذهبية في ثلاث خطوات:')}
{steps}
{demo}
{models}
{bulle('fille', 'أضع ما أعرفه في الشريط، وأضع <b style="color:#c0392b">؟</b> مكان ما أبحث عنه — ثم يظهر الحل أمامي!')}'''
    return page(num, 'كيف أحلّ أي مسألة؟', body, unit_label='طريقتنا في التعلّم', part='math')

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
pages_html.append(part_page(num, '2', 'الجزء الثاني', 'العلوم الطبيعية',
    'التوازن الغذائي والطاقوي · التصحر والتلوث · الماء والصحة · التطعيم',
    [f'{len(SCI_UNITS)} فصول', 'تمارين: سهل / متوسط / صعب', 'أمثلة محلولة', 'فيديو لكل درس'], 'var(--p-green)', part='sci'))
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
    <div class="cover-head">
      <div class="cover-brand-row">
        {logo_img('cover-logo')}
        <div class="cover-brand-name">MAJOR</div>
      </div>
      <div class="cover-titles">
        <p class="eyebrow">دفتر النجاح المدرسي · موريتانيا</p>
        <h1><span class="t1">الرياضيات</span><span class="t2">والعلوم</span></h1>
      </div>
      <div class="ribbon-concours">جوازُك للنجاح في الكونكور</div>
    </div>
    <div class="cover-stage">
      <div class="cover-rosette"><b>مطابق 100٪</b><span>للبرنامج الرسمي<br>الموريتاني</span></div>
      <div class="cover-app">
        <span class="app-ic">▶</span>
        <div class="app-txt">
          <b>دفتر ذكيّ</b>
          <span>فيديوهات شرح ومحتوى إضافي على تطبيق MAJOR عبر رموز QR</span>
        </div>
      </div>
      <div class="cover-chips" aria-hidden="true">
        <span class="cover-chip math">+ − × ÷</span>
        <span class="cover-chip win">يفهم · يتمرّن · ينجح</span>
      </div>
      <div class="cover-mascots">
        <span class="im im-fille" role="img" aria-label=""></span>
        <span class="im im-garcon" role="img" aria-label=""></span>
      </div>
      <div class="owner-line">اسم التلميذ(ة): <i></i> &nbsp; القسم: <i style="max-width:18mm;min-width:14mm"></i></div>
    </div>
  </div>
  <div class="corner-ribbon" aria-hidden="true"><span>6AF · السنة السادسة</span></div>
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
      {logo_img('logo')}
      <div class="brand-text">
        <div class="brand-title">دفتر ماجور</div>
        <div class="brand-sub">الرياضيات والعلوم · السنة السادسة الأساسية 6AF</div>
      </div>
    </div>
    <h2 class="lesson-title">الفهرس</h2>
    {toc_section('الجزء الأول — الرياضيات', 'var(--p-yell)', sep_math_num)}
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:0 4mm;align-items:start">
      {toc_col(toc_math[:half])}
      {toc_col(toc_math[half:])}
    </div>
    {toc_section('الجزء الثاني — العلوم الطبيعية', 'var(--p-green)', sep_sci_num)}
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:0 4mm;align-items:start">
      {toc_col(toc_sci[:half_s])}
      {toc_col(toc_sci[half_s:])}
    </div>
    <div class="scallop" style="margin-top:auto">كل وحدة تبدأ بدرس <b>أتعلّم</b> مع رمز QR لفيديو الشرح، ثم <b>مثال محلول</b>، ثم <b>تمارين</b> متدرّجة (سهل / متوسط / صعب)، وتنتهي بتقييم ذاتي — وتذكّر قاعدتنا الذهبية: أُشاهد ← أرسم نموذج الشريط ← أحسب.</div>
  </div>
  <div class="pageno">1</div>
</div>'''

# ─── page ملاحظاتي (garde le total de pages pair) + 4e de couverture ───
# sheet-inner centré → le composeur JS ignore ces deux pages.
NOTES_PAGE = '''<div class="sheet">
  <div class="sheet-inner" style="justify-content:center;padding:8mm 9mm">
    <span style="align-self:flex-start;background:#9a3412;color:#fff;border-radius:999px;padding:1.6mm 4.5mm;font-size:9.5px;font-weight:900;margin-bottom:4mm">📝 ملاحظاتي</span>
    <div style="flex:1;background:repeating-linear-gradient(to bottom,transparent 0,transparent 7.1mm,#cbd5e1 7.1mm,#cbd5e1 7.4mm)"></div>
  </div>
</div>'''

_PACK_CARDS_AR = [
    ('📐', 'الرياضيات والعلوم', '31 وحدة + 6 فصول', True),
    ('📘', 'اللغة العربية والتربية الإسلامية', '18 وحدة + 8 فصول', False),
    ('🏰', 'التاريخ والجغرافيا والتربية المدنية', '25 وحدة', False),
    ('📖', 'الفرنسية Français', '29 درسًا', False),
]
_pack_cards_ar = ''.join(
    f'''<div style="background:rgba(255,255,255,.12);border:.35mm solid rgba(255,255,255,{'.55' if cur else '.18'});border-radius:4mm;
        padding:2.4mm 3mm;display:flex;align-items:center;gap:2.2mm">
      <span style="font-size:13px">{e}</span>
      <span style="display:flex;flex-direction:column;gap:.4mm;flex:1">
        <strong style="font-size:8.4px;font-weight:900">{t}</strong>
        <span style="font-size:6.6px;color:rgba(255,255,255,.85)">{s}</span>
      </span>
      {'<span style="background:#fde68a;color:#78350f;border-radius:999px;padding:.8mm 2.4mm;font-size:6.2px;font-weight:900">هذا الدفتر</span>' if cur else ''}
    </div>''' for e, t, s, cur in _PACK_CARDS_AR)

_PITCH_AR = ''.join(
    f'''<div style="display:flex;align-items:flex-start;gap:2.4mm;background:rgba(255,255,255,.12);
        border:.35mm solid rgba(255,255,255,.18);border-radius:4mm;padding:2.4mm 3mm">
      <span style="font-size:11px">{e}</span>
      <span style="font-size:8.2px;line-height:1.75;font-weight:700">{t}</span>
    </div>''' for e, t in [
        ('📖', 'أراجعُ القاعدة بشرح بسيط وأمثلة من بلادي موريتانيا.'),
        ('✏️', 'أتدرّبُ بتمارين متدرّجة: ⭐ سهل، ⭐⭐ متوسط، ⭐⭐⭐ تحدٍّ.'),
        ('📱', 'أمسحُ رمز QR في كل درس: فيديو الشرح، ألعاب تفاعلية وتصحيح فوري.'),
    ])

_back_qr = _qr_b64(BASE_URL, '#9a3412')
BACK_COVER = f'''<div class="sheet" style="background:linear-gradient(135deg,#9a3412 0%,#ea580c 48%,#fdba74 100%);color:#fff">
  <div style="position:absolute;width:52mm;height:52mm;border-radius:50%;background:rgba(255,255,255,.1);left:-16mm;top:8mm"></div>
  <div style="position:absolute;width:44mm;height:44mm;border-radius:50%;background:rgba(255,255,255,.1);right:-14mm;bottom:-14mm"></div>
  <div class="sheet-inner" style="position:relative;justify-content:center;padding:7mm 8mm">
    <div style="display:flex;justify-content:space-between;align-items:center">
      <span style="display:inline-flex;background:rgba(255,255,255,.14);border:.35mm solid rgba(255,255,255,.2);padding:1.6mm 3.6mm;border-radius:999px;font-size:7.6px;font-weight:900">المجموعة الكاملة · السنة السادسة</span>
      <span style="display:inline-flex;background:rgba(255,255,255,.96);padding:1.4mm;border-radius:3.5mm"><img src="logo-major.png" alt="Major" style="width:10mm;height:10mm;object-fit:contain"/></span>
    </div>
    <h2 style="margin:4.5mm 0 1.2mm;font-size:19px;line-height:1.3;font-weight:900">مع دفاتر <span style="color:#fde68a">ماجور</span> أراجعُ وأفهمُ وأنجح</h2>
    <p style="font-size:9px;color:rgba(255,255,255,.9);margin:0 0 3.6mm;font-weight:700">أربعة دفاتر تغطي البرنامج الرسمي كاملًا للسنة السادسة الأساسية.</p>
    <div style="display:flex;flex-direction:column;gap:2mm;margin-bottom:3.6mm">{_PITCH_AR}</div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:2.2mm;margin-bottom:4mm">{_pack_cards_ar}</div>
    <div style="background:rgba(255,255,255,.96);color:#182230;border-radius:3.6mm;padding:2.8mm 3.6mm;display:flex;align-items:center;gap:3.4mm">
      <img src="data:image/png;base64,{_back_qr}" alt="QR Major" style="width:16.5mm;height:16.5mm"/>
      <div style="display:flex;flex-direction:column;gap:.9mm;flex:1">
        <strong style="font-size:9px;font-weight:900;color:#9a3412">امسح وادخل عالم ماجور</strong>
        <span style="font-size:7.4px;line-height:1.7;color:#334155">فيديوهات الشرح، ألعاب تفاعلية، اختبارات وتصحيح فوري — مجانًا مع دفترك.</span>
        <span style="font-size:7.4px;font-weight:900;color:#ea580c;direction:ltr;text-align:right">major-eval.vercel.app</span>
      </div>
    </div>
    <p style="text-align:center;font-size:7.4px;font-weight:800;color:rgba(255,255,255,.92);margin:4mm 0 0">صُنع بحبّ في موريتانيا 🇲🇷 · دفاتر ماجور · 2025-2026</p>
  </div>
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
<div class="toolbar"><button class="action-btn" onclick="window.print()">طباعة / PDF</button></div>
{COVER}
{SOMMAIRE}
{''.join(pages_html)}
{NOTES_PAGE}
{BACK_COVER}
<script>
/* Composition verticale : remplit les pages creuses, resserre les pages trop pleines,
   avant l'export PDF. */
(function(){{
  function composer(){{
    document.querySelectorAll('.sheet').forEach(function(sheet){{
      if (sheet.classList.contains('cover')) return;
      var inner = sheet.querySelector('.sheet-inner');
      if (!inner) return;
      var st = getComputedStyle(inner);
      if (st.justifyContent === 'center') return;
      var reserve = inner.querySelector('.qr-reserve');
      var kids = [].filter.call(inner.children, function(c){{
        var cs = getComputedStyle(c);
        if (cs.position === 'absolute' || cs.display === 'none') return false;
        if (c.classList.contains('qr-reserve')) return false;
        return c.getBoundingClientRect().height > 2;
      }});
      if (kids.length < 2) return;
      var ir = inner.getBoundingClientRect();
      var padB = parseFloat(st.paddingBottom) || 0;
      var hasQR = !!sheet.querySelector('.qr-corr');
      function contentFloor(){{
        var floor = ir.bottom - padB;
        if (reserve) floor = Math.min(floor, reserve.getBoundingClientRect().top);
        var qrEl = sheet.querySelector('.qr-corr');
        if (qrEl) floor = Math.min(floor, qrEl.getBoundingClientRect().top - 8);
        var pnEl = sheet.querySelector('.pageno');
        if (pnEl) floor = Math.min(floor, pnEl.getBoundingClientRect().top - 6);
        return floor;
      }}
      function spareNow(){{
        var maxB = 0;
        kids.forEach(function(c){{ var b = c.getBoundingClientRect().bottom; if (b > maxB) maxB = b; }});
        return contentFloor() - maxB;
      }}
      function refreshKids(){{
        kids = [].filter.call(inner.children, function(c){{
          var cs = getComputedStyle(c);
          if (cs.position === 'absolute' || cs.display === 'none') return false;
          if (c.classList.contains('qr-reserve')) return false;
          return c.getBoundingClientRect().height > 2;
        }});
      }}
      function isHeader(el){{
        return el.classList.contains('head') || el.classList.contains('lesson-title') ||
               el.classList.contains('unit-banner') || el.classList.contains('objectifs') ||
               !!el.querySelector(':scope > .unit-chip');
      }}
      function isStretchable(el){{
        return el.matches('.frame, .exemple, .methode, .exo, .cols, .vgrid, .figv')
          || (el.tagName === 'DIV' && !isHeader(el)
              && !el.classList.contains('self-eval')
              && !el.classList.contains('badge-row')
              && !el.classList.contains('bulle-row')
              && !el.classList.contains('attention')
              && !el.classList.contains('astuce')
              && !el.classList.contains('defi'));
      }}
      var spare = spareNow();

      /* ── pages trop pleines : resserrer ── */
      if (spare < -2) {{
        for (var pass = 0; pass < 6 && spare < -2; pass++) {{
          var deficit = -spare;
          var share = deficit / Math.max(1, kids.length - 1);
          kids.forEach(function(c, i){{
            if (i === 0) return;
            var m = parseFloat(getComputedStyle(c).marginTop) || 0;
            var cut = Math.min(m, Math.max(share * 1.15, 2));
            if (cut > 0.3) c.style.marginTop = Math.max(0, m - cut) + 'px';
          }});
          kids.forEach(function(c){{
            if (!c.matches('.frame, .exemple, .methode, .defi, .exo, .badge-row')) return;
            var pb = parseFloat(getComputedStyle(c).paddingBottom) || 0;
            var pt = parseFloat(getComputedStyle(c).paddingTop) || 0;
            var mb = parseFloat(getComputedStyle(c).marginBottom) || 0;
            if (pb > 3) c.style.paddingBottom = (pb - 1.8) + 'px';
            if (pt > 3) c.style.paddingTop = (pt - 1.2) + 'px';
            if (mb > 2) c.style.marginBottom = (mb - 1) + 'px';
          }});
          inner.querySelectorAll('.dashcard').forEach(function(d){{
            var h = d.getBoundingClientRect().height;
            if (h > 32) d.style.minHeight = Math.max(24, h - 10) + 'px';
          }});
          inner.querySelectorAll('.dotl, .line').forEach(function(ln){{
            var h = ln.getBoundingClientRect().height || 8;
            if (h > 6) ln.style.height = Math.max(5.5, h - 1.2) + 'px';
          }});
          spare = spareNow();
        }}
      }}

      /* ── pages creuses : redistribuer (sans QR stretch agressif) ── */
      if (spare > 28 && !hasQR) {{
        var cushion = Math.min(14, Math.max(6, spare * 0.08));
        inner.style.paddingBottom = (padB + cushion) + 'px';
        padB += cushion;
        spare -= cushion;
      }}
      if (spare > 28) {{
        var targets = [];
        kids.forEach(function(c, i){{
          if (i === 0) return;
          if (isHeader(kids[i-1]) && isHeader(c)) return;
          if (c.classList.contains('self-eval')) return;
          if (c.classList.contains('attention') || c.classList.contains('astuce')) return;
          targets.push(c);
        }});
        if (targets.length) {{
          var cap = hasQR ? 18 : (spare > 280 ? 72 : spare > 180 ? 48 : spare > 100 ? 32 : 22);
          var extra = Math.min(spare / targets.length, cap);
          targets.forEach(function(c){{
            var m = parseFloat(getComputedStyle(c).marginTop) || 0;
            c.style.marginTop = (m + extra) + 'px';
          }});
          spare = spareNow();
        }}
      }}
      if (spare > 40 && !hasQR) {{
        var stretch = null;
        for (var i = kids.length - 1; i >= 0; i--) {{
          if (isStretchable(kids[i])) {{ stretch = kids[i]; break; }}
        }}
        if (stretch) stretch.style.flexGrow = '1';
      }}
      /* garantir dégagement QR / n° page */
      for (var g = 0; g < 12 && spareNow() < 2; g++) {{
        var cut = false;
        for (var j = kids.length - 1; j >= 0 && !cut; j--) {{
          var lines = kids[j].querySelectorAll('.dotl, .line, .dashcard');
          if (lines.length > 1) {{ lines[lines.length - 1].remove(); cut = true; }}
        }}
        if (!cut) {{
          inner.querySelectorAll('.dotl, .line').forEach(function(ln){{
            var h = ln.getBoundingClientRect().height || 8;
            if (h > 5.5) ln.style.height = Math.max(5.2, h - 1.2) + 'px';
          }});
        }}
        refreshKids();
      }}
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

HTML = bidi_wrap(HTML)

import os
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'livrables', 'Cahier-Major-Math-Sciences-6AF-A5.SOURCE.html')
out = os.path.normpath(out)
open(out, 'w').write(HTML)
print(f'écrit: {out} ({len(HTML)/1024:.0f} Ko, {2 + len(pages_html)} pages A5)')
