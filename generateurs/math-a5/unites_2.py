# -*- coding: utf-8 -*-
"""Unités 6-10 : الأطوال · المستقيمات · مقارنة الأعداد · الكتل · الزوايا.
Contenu repris fidèlement des diapositives 21 à 48 de math_principal_ar_A5.pptx."""
from figs_pptx import FIGS, RAPPORTEUR_SVG, TERRAIN_FOOT_SVG
from base_a5 import figure_img, figure_svg
from base_a5 import (badge_row, video_box, exo, consigne, dots, angle_svg, lines_svg,
                     conv_table, balance_svg, FR, MX, OVAL, OVS, OVM, SQ,
                     bar_model, bar_compare, number_bond, draw_model, ans_cells, eq_cells, numline,
                     objectifs, methode, astuce, attention, defi)


# ═══════════════════ الوحدة 6 : قياس الأطوال (D21-D25) ═══════════════════
def u6_p1():
    body = f'''
{objectifs(['أميّز وحدات الطول (mm، cm، m، km) وأختار المناسبة.',
            'أحوّل الأطوال من وحدة إلى أخرى بجدول التحويل.',
            'أحلّ مسائل بجمع الأطوال وطرحها.'])}
{badge_row('أتعلّم', 'القاعدة والأمثلة', 'fille')}
<div class="frame has-video">
  <ul>
    <li>قياس الطول = معرفة <span class="hl">عدد وحدات القياس</span> في المسافة.</li>
    <li><b>mm</b>: الأطوال الصغيرة جدًا (سُمك بطاقة).</li>
    <li><b>cm</b>: عرض إصبع.</li>
    <li><b>m</b>: طول مسطرة التلميذ × 3.</li>
    <li><b>km</b>: المسافة بين مدينتين.</li>
  </ul>
  {video_box()}
</div>

{badge_row('أتدرّب', 'التحويل والحساب', 'garcon')}
<div class="frame">
  <ul>
    <li>أجمع القطع لأجد <span class="hl">الطول الكلي</span> · أطرح لأجد <span class="hl">الطول المتبقي</span>.</li>
    <li>محيط المستطيل = (الطول + العرض) <span class="hl">× 2</span>.</li>
    <li>{MX('1 m = 100 cm')} &nbsp;·&nbsp; {MX('1 cm = 10 mm')} &nbsp;·&nbsp; {MX('1 km = 1000 m')}</li>
  </ul>
  {methode('كيف أحوّل بجدول الوحدات', [
      'أضع رقم الآحاد في عمود الوحدة المعروفة.',
      'أكمل بصفر في كل عمود حتى الوحدة المطلوبة.',
      'أقرأ العدد كاملًا.',
      'للتحويل إلى وحدة أكبر: أقسم (أو أحذف أصفارًا).'])}
  <div class="exemple"><b class="tag">📏 مثال:</b> شريط طوله 2 m و35 cm. بالسنتيمتر: {MX('2 × 100 + 35 = 235')} cm.
  {bar_model('الكل = 235 cm', [('2 m', 200, '#8fd4e8'), ('35 cm', 35, '#ffd98c')], w=56, stagger=False, scale=.75)}</div>
</div>'''
    return ('قياس الأطوال وحسابها', body, False)


def u6_p2():
    body = f'''
{badge_row('تمارين', 'التحويلات والمسائل', 'garcon')}
{astuce('كل درجة في سلم الوحدات = ×10 عند النزول، و÷10 عند الصعود.')}
<div class="exemple"><b class="tag">✏️ مثال محلول:</b> حوّل 5 m إلى cm: {MX('5 × 100 = 500')} ← {MX('5 m = 500 cm')}.</div>
{exo(1, '⭐', f'''حوّل 300 cm إلى m {OVAL}<br>
حوّل 4 km إلى أمتار {OVAL}<br>
حوّل 3 m و15 cm إلى cm {OVAL}''')}
{exo(2, '⭐', 'لوح طوله 1 m و75 cm. كم يساوي بالسنتيمتر؟' + dots(1))}
{exo(3, '⭐⭐', f'مضمار سباق طوله 400 m. كم مترًا في 3 دورات؟ {OVM}')}
{exo(4, '⭐⭐⭐', f'''كابل طوله 14 m. نقطع منه 3 قطع طول كل منها 2 m. ما الطول المتبقي؟ أكمل النموذج ثم احسب:
{bar_model('الكل = 14 m', [('قطعة', 2, '#c6e9a4'), ('قطعة', 2, '#c6e9a4'), ('قطعة', 2, '#c6e9a4'), ('الباقي', 8, '#fff', '؟')], w=64, stagger=False, scale=.7)}''')}
{exo(5, '⭐⭐⭐', 'يقطع قطار المعادن 750 m في دقيقة واحدة. ما المسافة التي يقطعها في 4 دقائق؟' + draw_model(8, 'أرسم شريطًا من 4 شرائح (750 m في كل شريحة) ثم أحسب:'))}
{attention('1 m = 100 cm وليس 10! ولا تخلط بين cm و mm: عرض إصبعك 1 cm أي 10 mm.')}'''
    return ('تمارين — أحوّل وأحسب الأطوال', body, False)


def u6_p3():
    def pencil(cm, color):
        w = cm * 7
        return f'''<div style="display:flex;align-items:center;gap:2.6mm;margin:1.6mm 0">
          <svg width="{w}mm" height="7mm" viewBox="0 0 {w} 7" style="direction:ltr">
            <rect x="4.5" y="1.2" width="{w-8}" height="4.6" rx="1" fill="{color}" stroke="#2b2b2b" stroke-width=".5"/>
            <path d="M4.5,1.2 L.6,3.5 L4.5,5.8 Z" fill="#f3d9a4" stroke="#2b2b2b" stroke-width=".5"/>
            <path d="M2.2,2.6 L.6,3.5 L2.2,4.4 Z" fill="#4a4a4a"/>
            <rect x="{w-8}" y="1.2" width="4.5" height="4.6" rx="1.6" fill="#f5a09c" stroke="#2b2b2b" stroke-width=".5"/>
          </svg>
          <span class="oval s"></span><b style="font-size:9px">cm</b>
        </div>'''
    ruler_ticks = ''.join(
        f'<line x1="{4+i*7}" y1="1" x2="{4+i*7}" y2="5" stroke="#2b2b2b" stroke-width=".55"/>'
        f'<text x="{4+i*7}" y="9.5" text-anchor="middle" font-size="2.8" font-weight="900">{i}</text>'
        for i in range(0, 15))
    ruler = f'''<svg width="112mm" height="12mm" viewBox="0 0 112 12" style="direction:ltr;display:block;margin:0 auto;background:#fdf6e4;border:1.2px solid #d78d33;border-radius:1.6mm">{ruler_ticks}
      <text x="107.5" y="9.5" text-anchor="middle" font-size="3" font-weight="900">cm</text></svg>'''
    body = f'''
{badge_row('تمارين', 'أقيس بالمسطرة', 'fille')}
<div class="exemple"><b class="tag">✏️ مثال محلول:</b> قلم يبدأ عند 0 وينتهي عند العلامة 8 على المسطرة ← طوله {MX('8 cm')}.</div>
{consigne(6, 'قِس أقلام الرصاص بالسنتيمتر (إلى أقرب سنتيمتر) واكتب جوابك في الخانة المخصصة لذلك:')}
<div style="background:#fffdf6;border:1.2px solid #e7dfcc;border-radius:3mm;padding:2mm 3mm">
  {ruler}
  {pencil(6, '#f5b34c')}
  {pencil(9, '#8fd4e8')}
  {pencil(4, '#a9d3a0')}
  {pencil(12, '#b79ddb')}
  {pencil(7, '#f5a09c')}
</div>
{exo(7, '⭐⭐', '''رقّم المركبات التالية بـ 1 و2 و3: رتّب من الأقصر (1) إلى الأطول (3):<br>
🚌 حافلة ''' + SQ + ' &nbsp; 🚆 قطار ' + SQ + ' &nbsp; 🚗 سيارة ' + SQ)}'''
    return ('تمارين — أقيس الأطوال 📏', body, False)


def u6_p4():
    filled = {(0, 0): '2', (0, 1): '7', (0, 2): '0', (0, 3): '2'}
    conv = ['600 cm = ................ m', '3,2 km = ................ m', '5 m 8 cm = ................ cm',
            '2,5 km = ................ m', '340 mm = ................ cm', '7 hm = ................ m',
            '1 dm 5 mm = ................ mm', '2 702 m = ................ km']
    g = '<div style="display:grid;grid-template-columns:1fr 1fr;gap:1.8mm">' + ''.join(
        f'<div style="background:#fff;border:1.2px solid #ddd2b8;border-radius:2mm;padding:1.8mm;font-weight:800;font-size:9.2px;text-align:center">{c}</div>' for c in conv) + '</div>'
    body = f'''
{badge_row('أتدرّب', 'جدول التحويل الكامل', 'fille')}
<div class="frame">
  <ul>
    <li>مضاعفات المتر: <b>الكيلومتر (km)</b>، <b>الهكتومتر (hm)</b>، <b>الديكامتر (dam)</b>.</li>
    <li>أجزاء المتر: <b>الديسيمتر (dm)</b>، <b>السنتيمتر (cm)</b>، <b>المليمتر (mm)</b>.</li>
  </ul>
  {conv_table(['km', 'hm', 'dam', 'm', 'dm', 'cm', 'mm'], rows=3, filled=filled, title='جدول تحويل وحدات الطول')}
  <div class="exemple" style="text-align:center">2 km 7 hm 2 m = 2,702 km = 27,02 hm = 2 702 m</div>
</div>
{consigne(8, 'ضع كل عدد في الجدول ثم أكمل التحويلات:')}
{g}'''
    return ('جدول تحويل وحدات الطول', body, False)


def u6_p5():
    body = f'''
{badge_row('تمارين', 'أتحدى نفسي', 'fille')}
<div class="exemple"><b class="tag">✏️ مثال محلول:</b> ثمن المتر الواحد من الحبل 100 أوقية ← ثمن {MX('3 m')}: {MX('3 × 100 = 300')} أوقية.
{bar_model('الكل = 300 أوقية', [('1 m', 100, '#8fd4e8'), ('1 m', 100, '#8fd4e8'), ('1 m', 100, '#8fd4e8')], w=50, stagger=False, scale=.75)}</div>
{exo(9, '⭐', f'''ثمن المتر الواحد من قماش الملحفة في سوق العاصمة 250 أوقية. كم ثمن 4 m؟ النموذج جاهز — احسب!
{bar_model('؟', [('1 m', 250, '#ffd98c'), ('1 m', 250, '#ffd98c'), ('1 m', 250, '#ffd98c'), ('1 m', 250, '#ffd98c')], w=64, stagger=False, scale=.75)}''' + dots(1))}
{exo(10, '⭐⭐', 'يقطع أحمد 1 km و250 m مشيًا من بيته إلى مدرسته في بوتلميت. كم مترًا يقطع ذهابًا وإيابًا؟' + draw_model(11))}
{exo(11, '⭐⭐⭐', 'حبل طوله 30 m قُصّ إلى قطع طول كل واحدة 250 cm. كم قطعة نحصل عليها؟' + dots(2))}
{defi('المسافة بين نواكشوط وروصو حوالي 204 km. قطعت حافلة 150 000 m ثم توقفت للاستراحة. كم كيلومترًا بقي لها للوصول إلى روصو؟')}'''
    return ('تمارين إضافية — تحدّي الأطوال', body, True)


# ═══════════ الوحدة 7 : المستقيمات المتوازية والمتقاطعة (D26-D31) ═══════════
def u7_p1():
    body = f'''
{objectifs(['أتعرّف على المستقيمات المتوازية والمتقاطعة والمتعامدة.',
            'أجد أمثلة لها في القسم والشارع.',
            'أرسمها بدقة بالمسطرة والكوس.'])}
{badge_row('أتعلّم', 'القاعدة والأمثلة', 'fille')}
<div class="frame has-video">
  <ul>
    <li><span class="hl">المتوازيان</span>: لا يلتقيان أبدًا مهما مددناهما.</li>
    <li>يحافظان دائمًا على <span class="hl">نفس المسافة</span> بينهما (سكة القطار).</li>
    <li><span class="hl">المتقاطعان</span>: يلتقيان في نقطة واحدة.</li>
    <li>إذا شكّلا زاوية قائمة فهما <span class="hl">متعامدان</span>.</li>
  </ul>
  {video_box()}
</div>

{badge_row('أتدرّب', 'أمثلة واقعية وطريقة الرسم', 'garcon')}
<div class="frame">
  <div style="display:flex;gap:3mm;justify-content:center;margin-bottom:1mm">
    <div style="text-align:center">{lines_svg('parallel')}<div class="pie-lab">متوازيان</div></div>
    <div style="text-align:center">{lines_svg('perp')}<div class="pie-lab">متعامدان</div></div>
    <div style="text-align:center">{lines_svg('cross')}<div class="pie-lab">متقاطعان</div></div>
  </div>
  <ul>
    <li>سطور الدفتر متوازية · عقارب الساعة متقاطعة · حافتا المستطيل المتقابلتان متوازيتان.</li>
  </ul>
  {figure_img(FIGS['terrain_foot'], 28, '')}
  {methode('كيف أرسم مستقيمين متوازيين', [
      'أرسم المستقيم الأول بالمسطرة.',
      'أسند الكوس على المسطرة.',
      'أُزلق الكوس ثم أرسم المستقيم الثاني.'])}
</div>'''
    return ('المستقيمات المتوازية والمتقاطعة', body, False)


def u7_p2():
    pairs = [lines_svg('parallel', 25, 15), lines_svg('cross', 25, 15), lines_svg('perp', 25, 15), lines_svg('parallel', 25, 15)]
    cells = ''.join(f'''<div style="text-align:center;background:#fff;border:1.2px solid #ddd2b8;border-radius:2.4mm;padding:1.6mm">
        <b style="font-size:9px">{i+1}.</b>{p}<div style="margin-top:1mm">{OVAL}</div></div>''' for i, p in enumerate(pairs))
    body = f'''
{badge_row('تمارين', 'أتعرّف على المستقيمات', 'garcon')}
<div class="exemple"><b class="tag">✏️ مثال محلول:</b> سكة القطار: المستقيمان لا يلتقيان أبدًا ← متوازيان (وحافتا مسطرتك كذلك!).</div>
{consigne(1, 'حدّد ما إذا كان كل زوج من المستقيمات متوازيًا أو متعامدًا أو متقاطعًا بكتابة الاسم في الخانة:')}
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:2mm">{cells}</div>
{exo(2, '⭐', 'اذكر مثالين لمستقيمين متوازيين في قسمك:' + dots(1))}
{exo(3, '⭐', 'اذكر مثالين لمستقيمين متقاطعين في شوارع نواكشوط:' + dots(1))}
{exo(4, '⭐⭐', 'انظر إلى نافذة: أي الجوانب متوازية؟' + dots(1))}
{exo(5, '⭐⭐', 'هل حافتا الباب المتقابلتان متوازيتان أم متقاطعتان؟' + dots(1))}
{attention('ليس كل متقاطعين متعامدين! التعامد يحتاج زاوية قائمة 90° بالضبط — تحقّق منها بالكوس.')}'''
    return ('تمارين — متوازيان أم متقاطعان؟', body, False)


def u7_p3():
    body = f'''
{badge_row('تمارين', 'أرسم وألاحظ', 'fille')}
{exo(6, '⭐⭐', 'ارسم مستقيمين متقاطعين بمسطرتك:<div class="dashcard tall"></div>')}
{exo(7, '⭐⭐⭐', 'ارسم مستقيمين متوازيين المسافة بينهما 2 cm:<div class="dashcard tall"></div>')}
{exo(8, '⭐⭐', 'ارسم مستقيمًا وآخر يقطعه مشكّلًا زاوية قائمة:<div class="dashcard tall"></div>')}
{exo(9, '⭐', f'''هل خطا التماس في ملعب كرة القدم متوازيان أم متقاطعان؟ {OVAL}<br>
سكة القطار: متوازية أم متقاطعة؟ {OVAL}''')}
{exo(10, '⭐⭐', 'ارسم مستطيلًا وضع دائرة حول كل المستقيمات المتوازية، ثم ارسم مثلثًا وضع دائرة حول المستقيمات المتقاطعة:<div class="dashcard tall" style="min-height:16mm"></div>')}'''
    return ('تمارين — أرسم المستقيمات', body, False)


def u7_p4():
    tasks = ['ارسم المستقيمين المتعامدين (أ ب) و(ج د)', 'ارسم مستقيمين متوازيين (هـ و) و(ز ح)',
             'ارسم القطعتين المستقيمتين المتعامدتين [ط ي] و[ك ل]', 'ارسم شعاعين متوازيين [م ن) و[س ع)',
             'ارسم شعاعين متوازيين [أ ب) و[هـ و)', 'ارسم الشعاعين المتعامدين [أ ب) و[ج د)',
             'ارسم القطعتين المستقيمتين المتوازيتين [أ ب] و[ف ص]', 'ارسم شعاعين متوازيين [ك ل) و[ق ر)',
             'ارسم القطعتين المستقيمتين المتعامدتين [م ن] و[س ع]', 'ارسم المستقيمين المتعامدين (د هـ) و(و ز)',
             'ارسم مستقيمين متوازيين (م ن) و(ش ت)', 'ارسم القطعتين المستقيمتين المتوازيتين [ق ر] و[ش ت]']
    cells = ''.join(f'''<div style="background:#fff;border:1.4px dashed var(--red);border-radius:2.6mm;padding:1.4mm;display:flex;flex-direction:column">
        <div style="font-size:7.8px;font-weight:800;line-height:1.45">{t}</div><div style="flex:1;min-height:15mm"></div></div>''' for t in tasks)
    body = f'''
{badge_row('تمارين', 'ورشة الرسم الهندسي', 'garcon')}
{consigne(11, 'اتبع التعليمات في كل خانة لرسم مستقيمات متوازية أو متعامدة (استعمل المسطرة والكوس):')}
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:2mm">{cells}</div>'''
    return ('ورشة — أرسم بالمسطرة والكوس ✏️', body, False)


def u7_p5():
    body = f'''
{badge_row('تمارين', 'أتحدى نفسي', 'fille')}
<div class="exemple"><b class="tag">✏️ مثال محلول:</b> حافتا المسطرة لا تلتقيان مهما مددناهما ← متوازيتان.</div>
{exo(12, '⭐', f'''درجات السلم: متوازية أم متعامدة؟ {OVAL}<br>
ضلعا ركن النافذة: متوازيان أم متعامدان؟ {OVAL}''')}
{exo(13, '⭐⭐', 'ارسم مربعًا ثم لوّن كل ضلعين متوازيين بنفس اللون:<div class="dashcard tall"></div>')}
{exo(14, '⭐⭐⭐', 'ارسم المستقيم (أ ب)، ثم مستقيمًا يعامده في النقطة ج:<div class="dashcard tall"></div>')}
{defi('شباك صياد في نواذيبو: خيوطه الأفقية متوازية وخيوطه العمودية متوازية، وكل خيط أفقي يقطع كل خيط عمودي. إذا كان في الشباك 3 خيوط أفقية و4 خيوط عمودية، فكم نقطة تقاطع نحصل عليها؟')}'''
    return ('تمارين إضافية — تحدّي المستقيمات', body, True)


# ═══════════ الوحدة 8 : مقارنة الأعداد الصحيحة وترتيبها (D32-D37) ═══════════
def u8_p1():
    body = f'''
{objectifs(['أقارن عددين صحيحين بالرموز > و < و =.',
            'أرتّب الأعداد ترتيبًا تصاعديًا وتنازليًا.',
            'أحلّ مسائل مقارنة من الحياة اليومية.'])}
{badge_row('أتعلّم', 'القاعدة والأمثلة', 'fille')}
<div class="frame has-video">
  <ul>
    <li>المقارنة: أحدّد <span class="hl">أيها أكبر وأيها أصغر</span>.</li>
    <li>الرموز: {MX('&gt;')} أكبر من · {MX('&lt;')} أصغر من · {MX('=')} يساوي.</li>
  </ul>
  {video_box()}
</div>
{methode('كيف أقارن عددين', [
    'أعدّ الأرقام: العدد ذو الأرقام الأكثر هو الأكبر.',
    'إذا تساوى عدد الأرقام، أقارن رقمًا رقمًا بدءًا من اليسار.',
    'أول رقم مختلف يحدّد العدد الأكبر.'])}
{badge_row('أتدرّب', 'مثال محلول خطوة بخطوة', 'garcon')}
<div class="frame">
  {bar_compare('3 482', 3482, '2 975', 2975, w=50, diff_label='الفرق')}
  <div class="exemple"><b class="tag">🧩 تمرين محلول:</b> قرأ محمد الأمين {MX('3 482')} صفحة منذ بداية السنة، وقرأت مريم {MX('2 975')} صفحة. من قرأ أكثر؟</div>
  <div class="scallop">العددان يتكونان من 4 أرقام ← نقارن رقمًا رقمًا: 3 &gt; 2 ← {MX('3 482 &gt; 2 975')} ← <b>محمد الأمين قرأ صفحات أكثر</b>. ✔</div>
</div>'''
    return ('مقارنة الأعداد الصحيحة وترتيبها', body, False)


def u8_p2():
    pairs = [('2 134', '8 732'), ('1 093', '6 534'), ('2 347', '7 645'), ('1 093', '9 853'),
             ('9 823', '9 872'), ('9 087', '2 134'), ('3 000', '2 900')]
    comp = '<br>'.join(f'{MX(a)} {SQ} {MX(b)}' for a, b in pairs[:4])
    comp2 = '<br>'.join(f'{MX(a)} {SQ} {MX(b)}' for a, b in pairs[4:])
    body = f'''
{badge_row('تمارين', 'أقارن وأرتب', 'garcon')}
{astuce('ابدأ من اليسار! أول رقم مختلف يحسم المقارنة فورًا.')}
<div class="exemple"><b class="tag">✏️ مثال محلول:</b> نقارن {MX('4 512')} و{MX('4 521')}: 4 = 4 و5 = 5 لكن 1 &lt; 2 ← {MX('4 512 &lt; 4 521')}.</div>
{consigne(1, 'قارن باستعمال > أو < أو = :')}
<div class="cols">
  <div class="exo-q" style="text-align:center">{comp}</div>
  <div class="exo-q" style="text-align:center">{comp2}</div>
</div>
{exo(2, '⭐⭐', f'رتّب ترتيبًا تصاعديًا: {MX("1 204")} – {MX("1 042")} – {MX("1 240")} – {MX("1 402")}' + dots(2))}
{exo(3, '⭐⭐', f'رتّب ترتيبًا تنازليًا: {MX("9 876")} – {MX("9 768")} – {MX("9 867")} – {MX("9 786")}' + dots(2))}
{exo(4, '⭐⭐', f'شركتا نقل تنقلان مسافرين بين نواكشوط وروصو: الأولى نقلت {MX("5 012")} راكبًا هذا الأسبوع، والثانية {MX("5 120")}. أي شركة نقلت أكثر؟' + dots(2))}'''
    return ('تمارين — أقارن الأعداد وأرتبها', body, False)


def u8_p3():
    body = f'''
{badge_row('تمارين', 'مسائل المقارنة', 'fille')}
<div class="exemple"><b class="tag">✏️ مثال محلول:</b> باع الشيخ {MX('1 350')} سمكة وباع عبد الله {MX('1 305')} ← {MX('1 350 &gt; 1 305')} ← الشيخ باع أكثر.</div>
{exo(5, '⭐', f'في سباق، قطعت فاطمة {MX("2 045")} مترًا وقطع سيدي محمد {MX("1 998")} مترًا. من قطع المسافة الأكبر؟' + dots(1))}
{exo(6, '⭐', f'ادّخرت خديجة {MX("6 321")} أوقية، وادّخر المختار أيضًا {MX("6 321")} أوقية. هل ادّخرا نفس المبلغ؟' + dots(1))}
{exo(7, '⭐⭐', f'قرية قرب روصو فيها {MX("8 345")} نسمة وأخرى فيها {MX("8 354")}. أيهما أكثر سكانًا؟' + dots(2))}
{exo(8, '⭐⭐', f'هذه أوزان أربعة أكياس من التمر: {MX("1 350")} g، {MX("1 305")} g، {MX("1 530")} g، {MX("1 035")} g.<br>رتّبها من الأخف إلى الأثقل.' + dots(2))}
{exo(9, '⭐⭐⭐', f'هذه ارتفاعات قمم حقيقية: إفرست {MX("8 849")} m، كي2 {MX("8 611")} m، كلمنجارو {MX("5 895")} m، كديت إجّل (أعلى قمة في موريتانيا) {MX("915")} m.<br>رتّبها من الأعلى إلى الأدنى.' + dots(2))}'''
    return ('تمارين — مسائل المقارنة والترتيب', body, False)


def u8_p4():
    body = f'''
{badge_row('تمارين', 'مسائل الترتيب', 'garcon')}
<div class="exemple"><b class="tag">✏️ مثال محلول:</b> {MX('10 200')} فيه 5 أرقام و{MX('9 900')} فيه 4 أرقام ← {MX('10 200 &gt; 9 900')}.</div>
{exo(10, '⭐⭐', f'مدينة فيها {MX("10 005")} نسمة، وأخرى فيها {MX("9 999")}. أي مدينة هي الأكبر؟ {OVM}')}
{exo(11, '⭐⭐⭐', f'هذه أطوال أربع طرق: {MX("3 045")} m، {MX("3 504")} m، {MX("3 450")} m، {MX("3 054")} m.<br>رتّبها من الأقصر إلى الأطول بوضعها على المستقيم العددي:'
     + numline(96, [.1, .37, .63, .9], {.1: '?', .37: '?', .63: '?', .9: '?'}, y=6))}
{exo(12, '⭐⭐', f'تحلّق طائرة على ارتفاع {MX("10 200")} m وأخرى على {MX("9 850")} m. أيهما أعلى؟' + dots(1))}
{exo(13, '⭐⭐⭐', f'هذه أثمان أربع دراجات نارية: {MX("65 430")} أوقية، {MX("65 340")} أوقية، {MX("64 530")} أوقية، {MX("63 450")} أوقية.<br>رتّبها من الأغلى إلى الأرخص.' + dots(2))}
{attention(f'العدد {MX("10 005")} أكبر من {MX("9 999")} لأن فيه 5 أرقام — تحقّق من عدد الأرقام أولًا!')}
{defi(f'رتّب هذه المدن الموريتانية من الأكثر سكانًا إلى الأقل: كيفة {MX("60 005")} نسمة · نواذيبو {MX("118 167")} نسمة · روصو {MX("57 713")} نسمة · ازويرات {MX("62 000")} نسمة.')}'''
    return ('تمارين — أرتب في وضعيات واقعية', body, True)


# ═══════════════════ الوحدة 9 : الكتل (D38-D43) ═══════════════════
def u9_p1():
    body = f'''
{objectifs(['أميّز وحدات الكتلة: g و kg و t والقنطار.',
            'أحوّل الكتل من وحدة إلى أخرى.',
            'أحسب الكتلة الكلية والكتلة المتبقية في مسائل.'])}
{badge_row('أتعلّم', 'القاعدة والأمثلة', 'fille')}
<div class="frame has-video">
  <ul>
    <li>الكتلة تقيس <span class="hl">كمية المادة</span> في الجسم (نستعملها بالميزان).</li>
    <li><b>kg</b> ← الوحدة الرئيسية · <b>g</b> ← الأصغر · <b>t</b> ← الأكبر.</li>
    <li>لقياس كتلة، نستعمل <span class="hl">الميزان</span> ⚖️.</li>
  </ul>
  {balance_svg('1 kg', '1 000 g')}
  <div class="pie-lab" style="font-size:8.6px">الميزان متوازن: {MX('1 kg = 1 000 g')}</div>
  {video_box()}
</div>

{badge_row('أتدرّب', 'التحويلات', 'garcon')}
<div class="frame">
  <ul>
    <li>{MX('1 kg = 1 000 g')}</li>
    <li>{MX('1 t = 1 000 kg = 1 000 000 g')}</li>
    <li>أجمع لأجد <span class="hl">الكتلة الكلية</span> · أطرح لأجد <span class="hl">الكتلة المتبقية</span>.</li>
  </ul>
  <div class="exemple"><b class="tag">⚖️ مثال:</b> خبزة كتلتها 850 g وكعكة كتلتها 1,25 kg ← الكتلة الكلية: {MX('850 + 1 250 = 2 100')} g = 2,1 kg.
  {bar_model('الكل = 2 100 g', [('خبزة', 850, '#ffd98c'), ('كعكة', 1250, '#ffc7ba')], w=56, stagger=False, scale=.75)}</div>
</div>'''
    return ('الكتل: أقيس وأحوّل', body, False)


def u9_p2():
    body = f'''
{badge_row('تمارين', 'أحوّل وأحسب', 'garcon')}
{methode('كيف أحسب بكتلتين مختلفتي الوحدة', [
    'أحوّل الكتلتين إلى نفس الوحدة.',
    'أجمع أو أطرح، وأكتب الوحدة في الجواب.'])}
{astuce('من kg إلى g ثلاث درجات في السلم: أضرب في 1 000.')}
<div class="exemple"><b class="tag">✏️ مثال محلول:</b> {MX('3 kg = 3 × 1 000 g = 3 000 g')}.</div>
{exo(1, '⭐', f'89 kg = {OVAL} g')}
{exo(2, '⭐⭐', 'محفظة زينب كتلتها 4,8 kg. كم يمثل ذلك بالغرام؟')}
{exo(3, '⭐⭐', 'خنشة تمر كتلتها 16 kg قُسّمت على 8 سلال متساوية. ما كتلة السلة الواحدة؟' + draw_model(9, 'أرسم شريط 16 kg مقسومًا إلى 8 شرائح متساوية:'))}
{exo(4, '⭐⭐', 'يبيع خبّاز خبزة كتلتها 650 g وكعكة كتلتها 1,4 kg. ما الكتلة الكلية لهما؟')}
{exo(5, '⭐⭐', 'قط كتلته 4,3 kg وكلب كتلته 12,8 kg. ما الكتلة الكلية بالغرام؟' + dots(1))}
{exo(6, '⭐', f'لوح شوكولاتة كتلته 125 g. ما كتلة 8 ألواح؟ {OVM}')}'''
    return ('تمارين — الكتل والتحويلات', body, False)


def u9_p3():
    body = f'''
{badge_row('تمارين', 'مسائل الكتل', 'fille')}
{attention('لا تجمع 850 g مع 1,25 kg مباشرة! حوّل أولًا إلى نفس الوحدة ثم اجمع.')}
<div class="exemple"><b class="tag">✏️ مثال محلول:</b> اشترى أحمد 4 خبزات كتلة كل واحدة 250 g ← {MX('4 × 250 = 1 000 g = 1 kg')}.
{bar_model('الكل = 1 000 g = 1 kg', [('خبزة', 250, '#c6e9a4'), ('خبزة', 250, '#c6e9a4'), ('خبزة', 250, '#c6e9a4'), ('خبزة', 250, '#c6e9a4')], w=56, stagger=False, scale=.65)}</div>
{exo(7, '⭐⭐⭐', f'''اشترت آمنة 3 تفاحات كتلة كل واحدة 180 g. ما الكتلة الكلية بالكيلوغرام؟ النموذج جاهز — احسب ثم حوّل:
{bar_model('؟', [('تفاحة', 180, '#f5a09c'), ('تفاحة', 180, '#f5a09c'), ('تفاحة', 180, '#f5a09c')], w=54, stagger=False, scale=.65)}''' + dots(1))}
{exo(8, '⭐⭐', f'ملعقة سكر كتلتها 12 g. كم يساوي ذلك بالسنتيغرام؟ {OVM}')}
{exo(9, '⭐⭐', f'كعكة كتلتها 125 ديكاغرامًا. كم يساوي ذلك بالكيلوغرام؟ {OVM}')}
{exo(10, '⭐⭐', f'كيس الحلوى كتلته 1,5 ديكاغرام. كم يساوي ذلك بالغرام؟ {OVM}')}
{exo(11, '⭐⭐⭐', 'في كيس 250 ديكاغرامًا من الدقيق و1,3 kg من السكر و2,5 هكتوغرام من الملح. ما الكتلة الكلية بالغرام؟' + draw_model(10, 'أحوّل الكتل الثلاث إلى الغرام ثم أرسم نموذج الشريط وأجمع:') + dots(1))}'''
    return ('تمارين — مسائل الكتل ⚖️', body, False)


def u9_p4():
    filled = {(0, 0): '3', (0, 1): '0', (0, 2): '7', (0, 3): '6'}
    conv = ['5 t 208 kg = ................ kg', '8 g 5 dg 2 mg = ................ mg',
            '2 قنطار = ................ kg', '4 500 g = ................ kg',
            '0,5 t = ................ kg', '340 dag = ................ kg']
    g = '<div style="display:grid;grid-template-columns:1fr 1fr;gap:1.8mm">' + ''.join(
        f'<div style="background:#fff;border:1.2px solid #ddd2b8;border-radius:2mm;padding:1.8mm;font-weight:800;font-size:9.2px;text-align:center">{c}</div>' for c in conv) + '</div>'
    body = f'''
{badge_row('أتدرّب', 'جدول التحويل الكامل', 'garcon')}
<div class="frame">
  <ul>
    <li>مضاعفات الغرام: <b>الكيلوغرام (kg)</b>، <b>الهكتوغرام (hg)</b>، <b>الديكاغرام (dag)</b>.</li>
    <li>أجزاء الغرام: <b>الديسيغرام (dg)</b>، <b>السنتيغرام (cg)</b>، <b>الميليغرام (mg)</b>.</li>
    <li>أكبر من الكيلوغرام: <b>الطن</b> = {MX('1000 kg')} و<b>القنطار</b> = {MX('100 kg')}.</li>
    <li>بين <b>q</b> و <b>kg</b> عمود <b>10 kg</b>: لأن {MX('1 q = 10 × 10 kg = 100 kg')} (وليس 10 kg!).</li>
  </ul>
  {conv_table(['t', 'q', '10 kg', 'kg', 'hg', 'dag', 'g', 'dg', 'cg', 'mg'], rows=3, filled=filled, title='جدول تحويل وحدات الكتلة')}
  <div class="exemple" style="text-align:center">3 t 76 kg = 3,076 t = 30,76 q = 3 076 kg<br>
  <span style="font-size:9.5px;font-weight:700;color:#6b7280">الأرقام في الجدول: 3 تحت t · 0 تحت q · 7 تحت 10 kg · 6 تحت kg ← أي 70 kg + 6 kg</span></div>
</div>
{consigne(12, 'أكمل التحويلات مستعينًا بالجدول:')}
{g}'''
    return ('جدول تحويل وحدات الكتلة', body, False)


def u9_p5():
    body = f'''
{badge_row('تمارين', 'أتحدى نفسي', 'garcon')}
<div class="exemple"><b class="tag">✏️ مثال محلول:</b> كيسا أرز كتلة كل واحد 2 kg ← الكتلة الكلية: {MX('2 × 2 = 4 kg = 4 000 g')}.
{bar_model('الكل = 4 kg = 4 000 g', [('كيس', 2, '#aae4f0'), ('كيس', 2, '#aae4f0')], w=44, stagger=False, scale=.75)}</div>
{exo(13, '⭐', f'''اشترت مريم 3 أكياس أرز، كتلة كل كيس 5 kg. ما الكتلة الكلية بالغرام؟ النموذج جاهز — احسب ثم حوّل!
{bar_model('؟', [('كيس', 5, '#ffd98c'), ('كيس', 5, '#ffd98c'), ('كيس', 5, '#ffd98c')], w=52, stagger=False, scale=.75)}''' + dots(1))}
{exo(14, '⭐⭐', f'باعت بائعة سمك في سوق نواذيبو 2 kg و500 g لزبون، و{MX("1 750")} g لزبون آخر. كم غرامًا باعت في المجموع؟' + draw_model(11))}
{exo(15, '⭐⭐⭐', f'''شاحنة حمولتها القصوى 3 t، حُمّلت بـ 45 كيسًا كتلة كل كيس 50 kg. كم كيلوغرامًا بقي قبل بلوغ الحمولة القصوى؟ أكمل النموذج ثم احسب:
{bar_model('الحمولة القصوى = 3 t', [('الأكياس', 2250, '#aae4f0', '45 × 50'), ('الباقي', 750, '#fff', '؟')], w=64, stagger=False, scale=.75)}''' + dots(1))}
{defi(f'جمل كبير كتلته 600 kg. كم ماعزًا كتلة كل واحدة {MX("30 000")} g نحتاج لموازنته على ميزان عملاق؟')}'''
    return ('تمارين إضافية — تحدّي الكتل', body, True)


# ═══════════════════ الوحدة 10 : الزوايا (D44-D48) ═══════════════════
def u10_p1():
    types_row = f'''<div style="display:flex;gap:2mm;justify-content:center;align-items:flex-end;margin-top:1mm">
      <div style="text-align:center">{angle_svg(90, '', 20, 16)}<div class="pie-lab">قائمة = 90°</div></div>
      <div style="text-align:center">{angle_svg(45, '', 20, 16)}<div class="pie-lab">حادة &lt; 90°</div></div>
      <div style="text-align:center">{angle_svg(135, '', 22, 16)}<div class="pie-lab">منفرجة بين 90° و180°</div></div>
      <div style="text-align:center">{angle_svg(180, '', 24, 16)}<div class="pie-lab">مستقيمة = 180°</div></div>
    </div>'''
    body = f'''
{objectifs(['أميّز الزوايا: حادة، قائمة، منفرجة، مستقيمة، منعكسة.',
            'أقيس زاوية بالمنقلة بالدرجات (°).',
            'أرسم زاوية بقياس معلوم.'])}
{badge_row('أتعلّم', 'القاعدة والأمثلة', 'fille')}
<div class="frame has-video">
  <ul>
    <li>الزاوية: <span class="hl">انفراج بين ضلعين</span> يلتقيان في نقطة تسمى الرأس.</li>
    <li>تقاس الزوايا <span class="hl">بالدرجات (°)</span> بواسطة المنقلة.</li>
  </ul>
  {video_box()}
</div>
{methode('كيف أقيس زاوية بالمنقلة', [
    'أضع مركز المنقلة على رأس الزاوية.',
    'أُطابق أحد الضلعين مع الصفر.',
    'أقرأ القياس عند الضلع الآخر.'])}
<div class="figv" style="width:21mm;margin:.6mm auto">{RAPPORTEUR_SVG}</div>
{badge_row('أتدرّب', 'أنواع الزوايا', 'garcon')}
<div class="frame">
  {types_row}
  <div class="scallop">تذكّر: القائمة = 90° · الحادة أقل من 90° · المنفرجة بين 90° و180° · المستقيمة = 180° · <b>المنعكسة</b> أكثر من 180°.</div>
</div>'''
    return ('قياس الزوايا', body, False)


def u10_p2():
    degs = [(26, 'a'), (155, 'b'), (90, 'c'), (240, 'd'), (64, 'e'), (110, 'f')]
    cls_cells = ''.join(f'''<div style="text-align:center;background:#fff;border:1.2px solid #ddd2b8;border-radius:2.4mm;padding:1.4mm">
        {angle_svg(d, l, 22, 17)}<div style="margin-top:.8mm">{OVS}</div></div>''' for d, l in degs)
    comp = [('a', 26), ('b', 43), ('c', 64), ('d', 76)]
    comp_cells = ''.join(f'''<div style="text-align:center;background:#fff;border:1.2px solid #ddd2b8;border-radius:2.4mm;padding:1.4mm">
        {angle_svg(90, '', 18, 15)}<div style="font-size:8.6px;font-weight:800">الجزء المعلوم: {v}°<br>الزاوية {l} = {OVS}</div></div>''' for l, v in comp)
    body = f'''
{badge_row('تمارين', 'أصنّف وأحسب', 'garcon')}
{consigne(1, 'حدّد الزوايا أدناه وصنّف كلًّا منها: حادة، منفرجة، منعكسة أو قائمة:')}
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:2mm">{cls_cells}</div>
{consigne(2, 'مجموع كل زاويتين يساوي 90 درجة. أوجد الزاوية المجهولة:')}
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:2mm">{comp_cells}</div>
<div class="exemple"><b class="tag">💡 الزاوية المنعكسة:</b> أوجد قياسها بحساب الزاوية الحادة أو المنفرجة أولًا، ثم اطرحه من 360°. مثال: {MX('360 − 100 = 260°')}</div>'''
    return ('تمارين — أصنّف الزوايا', body, False)


def u10_p3():
    meas = [(45, '1'), (145, '2'), (30, '3'), (75, '4'), (120, '5'), (60, '6')]
    meas_cells = ''.join(f'''<div style="text-align:center;background:#fff;border:1.2px solid #ddd2b8;border-radius:2.4mm;padding:1.4mm">
        <b style="font-size:8.5px">{l}.</b>{angle_svg(d, '', 24, 17)}<div>{OVS} °</div></div>''' for d, l in meas)
    todraw = ['25°', '90°', '37°', '45°', '80°', '27°', '120°', '60°']
    draw_cells = ''.join(f'''<div style="background:#fff;border:1.4px dashed var(--red);border-radius:2.4mm;min-height:16mm;position:relative">
        <b style="position:absolute;top:1mm;right:2mm;font-size:9px;color:#c9711a">{t}</b></div>''' for t in todraw)
    body = f'''
{badge_row('تمارين', 'المنقلة: أقيس وأرسم', 'fille')}
{consigne(3, 'استعمل المنقلة لقياس كل زاوية:')}
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:2mm">{meas_cells}</div>
{consigne(4, 'استعمل المنقلة لرسم كل زاوية من الزوايا التالية:')}
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:2mm">{draw_cells}</div>'''
    return ('تمارين — أقيس وأرسم بالمنقلة 📐', body, False)


def u10_p4():
    def line_angle(known, unk='x'):
        return f'''<div style="text-align:center;background:#fff;border:1.2px solid #ddd2b8;border-radius:2.4mm;padding:1.4mm">
          <svg width="26mm" height="14mm" viewBox="0 0 26 14" style="display:block;margin:0 auto">
            <line x1="1.5" y1="12" x2="24.5" y2="12" stroke="#33475e" stroke-width="1"/>
            <line x1="13" y1="12" x2="19" y2="2" stroke="#e2504c" stroke-width="1"/>
            <text x="8.6" y="10" text-anchor="middle" font-size="3" font-weight="900" fill="#26303c">{unk}°</text>
            <text x="18.5" y="10" text-anchor="middle" font-size="3" font-weight="900" fill="#2f6ea5">{known}</text>
          </svg>
          <div style="font-size:8.8px;font-weight:800">{unk} = {OVS} °</div></div>'''
    items = [('155°', 'a'), ('53°', 'b'), ('32°', 'c'), ('52° + 58°', 'd'), ('70°', 'e'), ('50°', 'f'),
             ('22°', 'g'), ('60° + 60°', 'h')]
    cells = ''.join(line_angle(k, u) for k, u in items)
    body = f'''
{badge_row('تمارين', 'الزوايا المتجاورة', 'garcon')}
<div class="exemple"><b class="tag">📌 مثال:</b> مجموع الزوايا المتجاورة على مستقيم يساوي 180°. إذا كانت الزاوية المعلومة 80° ← {MX('180 − 80 = 100')} ← x = 100°.</div>
{consigne(5, 'أوجد قياس الزاوية المجهولة في كل شكل:')}
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:2mm">{cells}</div>
{exo(6, '⭐⭐⭐', f'''زاويتان متجاورتان على مستقيم: الأولى {MX("54°")} والثانية مقسومة إلى زاويتين {MX("24°")} و{MX("28°")} وزاوية مجهولة f. أوجد f. أكمل النموذج ثم احسب:
{bar_model('المجموع على المستقيم = 180°', [('', 54, '#aae4f0'), ('', 24, '#ffd98c'), ('', 28, '#c6e9a4'), ('f', 74, '#fff', '؟')], w=64, stagger=False, scale=.75)}''' + dots(1))}'''
    return ('تمارين — الزوايا على مستقيم', body, False)


def u10_p5():
    body = f'''
{badge_row('تمارين', 'أتحدى نفسي', 'fille')}
{astuce('قارن الزاوية بركن ورقة (90°): أصغر من الركن = حادة، أكبر منه = منفرجة.')}
{attention('في المنقلة تدريجان! ابدأ القراءة دائمًا من الصفر الموجود على ضلع الزاوية.')}
<div class="exemple"><b class="tag">✏️ مثال محلول:</b> زاوية قياسها 40° أصغر من 90° ← زاوية حادة.</div>
{exo(7, '⭐', 'صنّف كل زاوية (حادة / قائمة / منفرجة / مستقيمة):' + ans_cells([MX('89°'), MX('90°'), MX('91°'), MX('180°')], cols=4))}
{exo(8, '⭐⭐', 'زاويتان مجموعهما 90°: الأولى قياسها 35°. ما قياس الثانية؟ أكمل مخطط الجزء والكل:' + number_bond('90°', ['35°', '؟'], w=24))}
{exo(9, '⭐⭐⭐', 'زاوية منعكسة، الجزء المتبقي من الدورة الكاملة (360°) يقيس 140°. ما قياس الزاوية المنعكسة؟ أكمل النموذج ثم احسب:' + bar_model('دورة كاملة = 360°', [('المتبقي', 140, '#aae4f0'), ('المنعكسة', 220, '#fff', '؟')], w=56, stagger=False, scale=.75))}
{defi('انظر إلى ساعة الحائط: عند الساعة الثالثة تمامًا يصنع العقربان زاوية قائمة. ما نوع الزاوية التي يصنعانها عند السادسة تمامًا؟ وكم قياسها بالدرجات؟')}'''
    return ('تمارين إضافية — تحدّي الزوايا', body, True)


UNITS_2 = [
    dict(num=6, title='قياس الأطوال وحسابها', sub='mm · cm · m · km والتحويل بينها', color='var(--p-yell)',
         pages=[u6_p1(), u6_p2(), u6_p3(), u6_p4(), u6_p5()]),
    dict(num=7, title='المستقيمات المتوازية والمتقاطعة', sub='التعرف عليها ورسمها', color='var(--p-rose)',
         pages=[u7_p1(), u7_p2(), u7_p3(), u7_p4(), u7_p5()]),
    dict(num=8, title='مقارنة الأعداد الصحيحة وترتيبها', sub='> و < و = · الترتيب التصاعدي والتنازلي', color='var(--p-green)',
         pages=[u8_p1(), u8_p2(), u8_p3(), u8_p4()]),
    dict(num=9, title='الكتل', sub='g · kg · t · القنطار والتحويل بينها', color='var(--p-blue)',
         pages=[u9_p1(), u9_p2(), u9_p3(), u9_p4(), u9_p5()]),
    dict(num=10, title='قياس الزوايا', sub='المنقلة · حادة، قائمة، منفرجة، منعكسة', color='var(--p-lila)',
         pages=[u10_p1(), u10_p2(), u10_p3(), u10_p4(), u10_p5()]),
]
