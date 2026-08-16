# -*- coding: utf-8 -*-
"""Unités 16-26 (complément programme officiel 6AF — calcul) :
مضاعفات وقابلية القسمة · كسور متكافئة وجمعها · ×10/100/1000 · تقاسيم غير متساوية ·
الزمن والأعداد الستينية · التناسبية · الحركة المنتظمة · السلم · الفائدة · الفواصل · الكتلة القائمة.
Sources : manuel IPN 2024 (C7, C9, C11, C18, C20, C21, C22, C24, C25, M5) + résumé rimbac."""
from figs_pptx import FIGS
from base_a5 import figure_img
from base_a5 import (badge_row, video_box, exo, consigne, dots, pie, prop_table, formula,
                     objectifs, methode, astuce, attention, defi,
                     clock_svg, bar_model, container_svg, numline, place_discs, draw_model,
                     ans_cells, eq_cells,
                     FR, MX, OVAL, OVS, OVM, SQ)

UM = 'أوقية'


def _mult100_svg(w=58):
    """Petit tableau fléché : la virgule de 2,4 saute deux rangs vers la droite (×100 → 240)."""
    boxes, digits = [], ['2', '4', '0']
    for i, dg in enumerate(digits):
        x = 10 + i * 12
        dash = ' stroke-dasharray="1.6,1.1"' if i == 2 else ''
        col = '#c0392b' if i == 2 else '#26303c'
        boxes.append(f'<rect x="{x}" y="3" width="10" height="10" rx="1.2" fill="#fff" stroke="#d78d33" stroke-width=".7"{dash}/>')
        boxes.append(f'<text x="{x + 5}" y="10.4" text-anchor="middle" font-size="5" font-weight="900" fill="{col}">{dg}</text>')
    arcs = []
    for x in (21, 33):
        arcs.append(f'<path d="M{x},15 Q{x + 6},20.5 {x + 11},15" fill="none" stroke="#1d7fc4" stroke-width=".7"/>')
        arcs.append(f'<path d="M{x + 11},15 l-2.2,.4 l1,2 Z" fill="#1d7fc4"/>')
    parts = (boxes + arcs +
             ['<text x="21" y="14.2" text-anchor="middle" font-size="5" font-weight="900" fill="#e2504c">,</text>',
              '<text x="45" y="14.2" text-anchor="middle" font-size="5" font-weight="900" fill="#33591f">,</text>',
              '<text x="27" y="23.5" text-anchor="middle" font-size="3" font-weight="900" fill="#1d7fc4">×100</text>'])
    return (f'<svg width="{w}mm" height="{w * 25 / 58:.1f}mm" viewBox="0 0 58 25" '
            f'style="display:block;margin:0 auto">{"".join(parts)}</svg>')


def _dvt_triangle(w=25):
    """Triangle masqué م/س/ز : المسافة = السرعة × الزمن."""
    parts = [
        '<polygon points="13,1 25,21 1,21" fill="#fdf1d7" stroke="#c9711a" stroke-width=".9" stroke-linejoin="round"/>',
        '<line x1="7" y1="11" x2="19" y2="11" stroke="#c9711a" stroke-width=".7"/>',
        '<line x1="13" y1="11" x2="13" y2="21" stroke="#c9711a" stroke-width=".7"/>',
        '<text x="13" y="9.4" text-anchor="middle" font-size="4.6" font-weight="900" fill="#b03434">م</text>',
        '<text x="8.6" y="18.4" text-anchor="middle" font-size="4.2" font-weight="900" fill="#1d7fc4">س</text>',
        '<text x="13" y="17.6" text-anchor="middle" font-size="3.2" font-weight="900" fill="#8a4a12">×</text>',
        '<text x="17.6" y="18.4" text-anchor="middle" font-size="4.2" font-weight="900" fill="#33591f">ز</text>',
    ]
    return (f'<svg width="{w}mm" height="{w * 22 / 26:.1f}mm" viewBox="0 0 26 22" '
            f'style="display:block;margin:0 auto">{"".join(parts)}</svg>')


def _scale_lines():
    """Double droite graduée carte ↔ réel pour le sلم 1/3 000 000 (5 cm ↔ 150 km)."""
    tt = lambda t: .04 + .90 * t
    ticks = [tt(i / 5) for i in range(6)]
    top = numline(82, ticks, {tt(i / 5): (f'{i}' if i < 5 else '5 cm') for i in range(6)}, y=2)
    bot = numline(82, ticks, {tt(i / 5): (f'{i * 30}' if i < 5 else '150 km') for i in range(6)}, y=2)
    row = lambda lab, col, nl: (f'<div style="display:flex;align-items:center;gap:2mm;margin-bottom:-1.8mm">'
                                f'<span style="font-size:8.6px;font-weight:900;color:{col};width:13mm;flex-shrink:0">{lab}</span>{nl}</div>')
    return (f'<div style="margin-top:.5mm">{row("الخريطة", "#1f5566", top)}'
            f'{row("الحقيقة", "#33591f", bot)}</div>')


# ═══════════ الوحدة 16 : المضاعفات والقواسم وقابلية القسمة (C7+C9) ═══════════
def u16_p1():
    body = f'''
{objectifs(['أميّز مضاعفات العدد وقواسمه',
            'أطبّق قواعد قابلية القسمة على 2 و3 و4 و5 و6 و9 و10',
            'أستعمل هذه القواعد لحل مسائل من حياتي اليومية'])}
{badge_row('أتعلّم', 'القاعدة والأمثلة', 'fille')}
<div class="frame has-video">
  <ul>
    <li><span class="hl">مضاعفات</span> العدد: نحصل عليها بضربه في 0، 1، 2، 3… مثال: مضاعفات 5 هي {MX('0، 5، 10، 15، 20…')}</li>
    <li><span class="hl">قواسم</span> العدد: الأعداد التي تقسمه قسمة تامة. مثال: {MX('210 ÷ 30 = 7')} ← إذن 30 قاسم لـ 210، و210 مضاعف لـ 30.</li>
  </ul>
  {video_box()}
</div>
{numline(70, [.05, .23, .41, .59, .77, .95], {.05: '0', .23: '5', .41: '10', .59: '15', .77: '20', .95: '25'}, y=4)}
<div class="pie-lab" style="font-size:7.6px">مضاعفات 5 على المستقيم العددي: أقفز 5 في كل مرة!</div>

{badge_row('أتدرّب', 'قواعد قابلية القسمة', 'garcon')}
<div class="frame">
  <ul>
    <li>يقبل القسمة على <b>2</b>: إذا كان زوجيًا (ينتهي بـ 0، 2، 4، 6، 8). مثال: 842 و430.</li>
    <li>يقبل القسمة على <b>3</b>: إذا كان مجموع أرقامه يقبل القسمة على 3.</li>
    <li>يقبل القسمة على <b>4</b>: إذا كان العدد المكوَّن من رقميه الأخيرين يقبل القسمة على 4.</li>
    <li>يقبل القسمة على <b>5</b>: إذا انتهى بـ 0 أو 5.</li>
    <li>يقبل القسمة على <b>6</b>: إذا قبل القسمة على 2 و3 معًا.</li>
    <li>يقبل القسمة على <b>9</b>: إذا كان مجموع أرقامه يقبل القسمة على 9.</li>
    <li>يقبل القسمة على <b>10</b>: إذا انتهى بـ 0.</li>
  </ul>
</div>'''
    return ('مضاعفات الأعداد وقواسمها', body, False)


def u16_p2():
    def vf_table(nums, checks):
        head = ''.join(f'<th style="background:var(--p-yell);color:#7c4a12">يقبل ÷ {c}</th>' for c in checks)
        rows = ''.join(f'<tr><th style="background:var(--p-rose);color:#8a3d2a">{n}</th>' +
                       '<td><span class="cellbox" style="width:11mm">&nbsp;</span></td>' * len(checks) + '</tr>' for n in nums)
        return f'<table class="fam-table" style="width:100%"><tr><th style="background:var(--p-green);color:#33591f">العدد</th>{head}</tr>{rows}</table>'
    body = f'''
{badge_row('تمارين', 'قابلية القسمة', 'garcon')}
{astuce('لأفحص القسمة على 3 أو 9، أجمع أرقام العدد: 414 ← 4 + 1 + 4 = 9، إذن 414 يقبل القسمة على 3 و9 معًا!')}
<div class="exemple"><b class="tag">✏️ مثال محلول:</b> العدد 240: ينتهي بـ 0 ← يقبل ÷ 2 و÷ 5 «صحيح»، ومجموع أرقامه {MX('2 + 4 + 0 = 6')} ← يقبل ÷ 3 «صحيح».</div>
{consigne(1, 'انقل الجدول واملأ كل خانة بـ «صحيح» أو «خطأ»:')}
{vf_table([615, 630, 190, 216], [2, 5, 3])}
{consigne(2, 'أجب مستعينًا بجدول مشابه:')}
<div class="exo-q">هل العدد 495 يقبل القسمة على 2؟ 3؟ 5؟ 6؟ 9؟ {OVAL}<br>
هل العدد 396 يقبل القسمة على 4؟ 5؟ 6؟ 9؟ {OVAL}</div>
{exo(3, '⭐', f'أكتب المضاعفات الخمسة الأولى لكل من: 5 {OVAL} · 9 {OVAL}')}
{exo(4, '⭐⭐', 'كم قارورة حليب سعة 90 cL يمكن ملؤها بـ 270 cL من الحليب؟' + dots(1))}
{exo(5, '⭐⭐', f'اشترى الشيخ 3 kg من اللحم بـ 420 {UM}. كم ثمن الكيلوغرام الواحد؟' + dots(1))}'''
    return ('تمارين — قابلية القسمة', body, False)


def u16_p3():
    body = f'''
{badge_row('تمارين', 'ألعاب الأعداد 🎲', 'fille')}
<div class="exemple"><b class="tag">✏️ مثال محلول:</b> أصغر عدد (غير الصفر) يقبل القسمة على 2 و5 معًا ينتهي بـ 0 ← هو 10.</div>
{exo(6, '⭐⭐⭐', 'أنا أصغر عدد صحيح (غير الصفر) يقبل القسمة على 2 و3 و5 و9 في آن واحد. من أنا؟' + dots(1))}
{exo(7, '⭐⭐⭐', 'أوجد عددًا من ثلاثة أرقام يقبل القسمة على 2 و5 و9 معًا. هل توجد أعداد أخرى؟' + dots(1))}
{exo(8, '⭐⭐', f'''ضع دائرة حول الأعداد التي تقبل القسمة على 3:<br>
{MX('123 · 250 · 414 · 505 · 630 · 731 · 900')}''')}
{exo(9, '⭐⭐', f'''ضع دائرة حول الأعداد التي تقبل القسمة على 9:<br>
{MX('81 · 132 · 234 · 567 · 719 · 900')}''')}
{exo(10, '⭐⭐', 'وزّعت آمنة 240 حبة تمر على مجموعة من 30 طفلًا بالتساوي. كم حبة لكل طفل؟ وهل 30 قاسم لـ 240؟' + dots(2))}
{attention('انتهاء العدد بـ 3 لا يعني أنه يقبل القسمة على 3! مثال: 13 لا يقبل القسمة على 3. القاعدة تخصّ مجموع الأرقام لا الرقم الأخير.')}
{defi(f'جمعت تعاونية للتمور في أطار 630 kg من التمور. هل يمكن توزيعها بالتساوي على 9 عائلات دون أن يبقى شيء؟ وعلى 6 عائلات؟ برهن بقواعد قابلية القسمة!')}'''
    return ('تمارين — ألعاب قابلية القسمة', body, True)


# ═══════ الوحدة 17 : الكسور المتكافئة وجمع الكسور وطرحها (C11 + rimbac) ═══════
def u17_p1():
    pies_row = f'''<div class="pies">
      <div><div>{pie(180, 2)}</div><div class="pie-lab">{FR(1,2)}</div></div>
      <div style="font-weight:900;font-size:14px">=</div>
      <div><div>{pie(180, 4)}</div><div class="pie-lab">{FR(2,4)}</div></div>
      <div style="font-weight:900;font-size:14px">=</div>
      <div><div>{pie(180, 6)}</div><div class="pie-lab">{FR(3,6)}</div></div>
    </div>'''
    body = f'''
{objectifs(['أتعرّف الكسور المتكافئة وأبسّط الكسور',
            'أجمع الكسور وأطرحها ولو اختلفت مقاماتها',
            'آخذ كسرًا من عدد لحل مسائل الشراء'])}
{badge_row('أتعلّم', 'القاعدة والأمثلة', 'fille')}
<div class="frame has-video">
  <ul>
    <li>الكسور <span class="hl">المتكافئة</span> تمثل نفس الجزء من الكل: {MX('1/2 = 2/4 = 3/6')}.</li>
    <li>للحصول على كسر مكافئ: <span class="hl">نضرب</span> (أو <span class="hl">نقسم</span>) البسط والمقام في نفس العدد.</li>
  </ul>
  {video_box()}
</div>
<div class="frame">{pies_row}</div>

{badge_row('أتدرّب', 'جمع الكسور وطرحها', 'garcon')}
<div class="frame">
  <ul>
    <li><b>نفس المقام:</b> نجمع أو نطرح البسطين ونحتفظ بالمقام: <span class="mexp">{FR(2,5)} + {FR(7,5)} = {FR(9,5)}</span> · <span class="mexp">{FR(12,7)} − {FR(9,7)} = {FR(3,7)}</span></li>
    <li><b>مقامان مختلفان:</b> نبحث عن كسور متكافئة لها نفس المقام ثم نجمع:</li>
  </ul>
  <div class="exemple" style="text-align:center">{FR(2,3)} + {FR(3,4)} = {FR('2×4','3×4')} + {FR('3×3','4×3')} = {FR(8,12)} + {FR(9,12)} = {FR(17,12)}</div>
</div>'''
    return ('الكسور المتكافئة وجمع الكسور وطرحها', body, False)


def u17_p2():
    eqs = [f'{FR(1,2)} = {FR("؟",4)} {OVS}', f'{FR(2,3)} = {FR("؟",9)} {OVS}', f'{FR(3,5)} = {FR("؟",10)} {OVS}',
           f'{FR(6,8)} = {FR("؟",4)} {OVS}', f'{FR(10,15)} = {FR("؟",3)} {OVS}', f'{FR(4,12)} = {FR("؟",3)} {OVS}']
    g = '<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:1.8mm">' + ''.join(
        f'<div style="background:#fff;border:1.2px solid #ddd2b8;border-radius:2mm;padding:1.8mm;text-align:center;font-weight:800">{e}</div>' for e in eqs) + '</div>'
    adds = [f'{FR(2,5)} + {FR(1,5)} = {OVS}', f'{FR(7,9)} − {FR(4,9)} = {OVS}', f'{FR(5,8)} + {FR(2,8)} = {OVS}',
            f'{FR(11,12)} − {FR(5,12)} = {OVS}', f'{FR(3,7)} + {FR(6,7)} = {OVS}', f'{FR(13,15)} − {FR(8,15)} = {OVS}']
    g2 = '<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:1.8mm">' + ''.join(
        f'<div style="background:#fff;border:1.2px solid #ddd2b8;border-radius:2mm;padding:1.8mm;text-align:center;font-weight:800">{e}</div>' for e in adds) + '</div>'
    body = f'''
{badge_row('تمارين', 'الكسور المتكافئة', 'garcon')}
{astuce('الكسر لا يتغيّر إذا ضربتُ البسط والمقام في نفس العدد — كأنك تقطّع نفس الكعكة إلى قطع أصغر!')}
<div class="exemple"><b class="tag">✏️ مثال محلول:</b> {FR(1,3)} = {FR('؟',6)} ← أضرب البسط والمقام في 2 ← {FR(1,3)} = {FR(2,6)}.
<div style="width:46mm;margin:.8mm auto 0">
  <div class="fstrip" style="margin:.6mm 0"><div class="fcell fill-b"></div><div class="fcell"></div><div class="fcell"></div></div>
  <div class="fstrip" style="margin:.6mm 0"><div class="fcell fill-b"></div><div class="fcell fill-b"></div><div class="fcell"></div><div class="fcell"></div><div class="fcell"></div><div class="fcell"></div></div>
</div>
<div class="sg-note">نفس المساحة الملوّنة في الشريطين — الكسران متكافئان!</div></div>
{consigne(1, 'أكمل لتحصل على كسور متكافئة:')}
{g}
{consigne(2, 'أنجز عمليات الجمع والطرح (نفس المقام):')}
{g2}
{exo(3, '⭐⭐', 'بسّط إلى أبسط صورة:' + eq_cells([f'{FR(6,8)} = {OVS}', f'{FR(15,20)} = {OVS}', f'{FR(9,27)} = {OVS}']))}'''
    return ('تمارين — الكسور المتكافئة', body, False)


def u17_p3():
    body = f'''
{badge_row('تمارين', 'مقامات مختلفة وكسر من عدد', 'fille')}
{methode('جمع كسرين مقاماهما مختلفان', [
    'أبحث عن مقام مشترك (مثل 3 × 4 = 12)',
    'أحوّل كل كسر إلى كسر مكافئ بالمقام الجديد',
    'أجمع البسطين وأحتفظ بالمقام'])}
{consigne(4, 'أنجز بعد توحيد المقامات:')}
<div style="display:grid;grid-template-columns:repeat(2,1fr);gap:1.8mm">
  <div style="background:#fff;border:1.2px solid #ddd2b8;border-radius:2mm;padding:1.8mm;text-align:center;font-weight:800">{FR(2,3)} + {FR(3,4)} = {OVS}</div>
  <div style="background:#fff;border:1.2px solid #ddd2b8;border-radius:2mm;padding:1.8mm;text-align:center;font-weight:800">{FR(1,2)} + {FR(2,5)} = {OVS}</div>
  <div style="background:#fff;border:1.2px solid #ddd2b8;border-radius:2mm;padding:1.8mm;text-align:center;font-weight:800">{FR(13,15)} − {FR(2,3)} = {OVS}</div>
  <div style="background:#fff;border:1.2px solid #ddd2b8;border-radius:2mm;padding:1.8mm;text-align:center;font-weight:800">{FR(5,6)} − {FR(1,2)} = {OVS}</div>
</div>
<div class="exemple"><b class="tag">💡 أخذ كسر من عدد:</b> أضرب العدد في البسط وأقسم على المقام.<br>
مثال: مع المختار 200 {UM}، أعطى صديقه {FR(2,5)} منها ← <span class="mexp">200 × 2 ÷ 5 = 80</span> {UM}.
{bar_model('الكل = 200 أوقية', [('أعطى', 40, '#f5b34c'), ('', 40, '#f5b34c'), ('بقي', 40, '#fff'), ('', 40, '#fff'), ('', 40, '#fff')], w=60, stagger=False, scale=.7)}</div>
{exo(5, '⭐⭐', f'أوجد {FR(3,4)} من 60 {OVAL} &nbsp;·&nbsp; {FR(2,3)} من 90 {OVAL}')}
{exo(6, '⭐⭐⭐', f'مع مريم 350 {UM}. أنفقت {FR(2,7)} منها. كم أنفقت؟ وكم بقي معها؟' + dots(1))}
{exo(7, '⭐⭐⭐', f'قطعة من قماش الملحفة طولها 12 m. بيع {FR(3,4)} منها. كم مترًا بيع؟ {OVM}')}'''
    return ('تمارين — أجمع الكسور وآخذ كسرًا من عدد', body, False)


def u17_p4():
    body = f'''
{badge_row('تمارين', 'أتحدى نفسي 💪', 'garcon')}
{attention('عند جمع كسرين لا أجمع المقامين أبدًا! ' + MX('1/4 + 2/4 = 3/4') + ' وليس ' + MX('3/8') + '.')}
<div class="exemple"><b class="tag">✏️ مثال محلول:</b> {FR(6,9)}: أقسم البسط والمقام على 3 ← {FR(6,9)} = {FR(2,3)}.</div>
{exo(8, '⭐', 'بسّط إلى أبسط صورة:' + eq_cells([f'{FR(8,12)} = {OVS}', f'{FR(10,15)} = {OVS}', f'{FR(14,21)} = {OVS}']))}
{exo(9, '⭐⭐', 'احسب بعد توحيد المقامات:' + eq_cells([f'{FR(3,10)} + {FR(2,5)} = {OVS}', f'{FR(7,8)} − {FR(3,4)} = {OVS}'], cols=2))}
{exo(10, '⭐⭐⭐', f'قرأت زينب {FR(2,5)} كتابها يوم السبت و{FR(1,5)} يوم الأحد. أي جزء من الكتاب قرأت؟ وأي جزء بقي لها؟' + draw_model(12, 'أرسم شريط الكتاب مقسومًا إلى 5 أجزاء ثم لوّن ما قرأت:'))}
{defi(f'اقتسمت ثلاث نساء من تعاونية في روصو صندوق تمر: أخذت الأولى {FR(1,3)} والثانية {FR(1,4)}. أي جزء بقي للثالثة؟ (وحّد المقامات إلى 12)')}'''
    return ('تمارين — كسور للأبطال', body, True)


# ═══════════ الوحدة 18 : الضرب في 10 و100 و1000 (C18) ═══════════
def u18_p1():
    body = f'''
{objectifs(['أضرب عددًا صحيحًا في 10 و100 و1000 بإضافة الأصفار',
            'أضرب عددًا عشريًا بنقل الفاصلة نحو اليمين',
            'أحسب أثمانًا كبيرة بسرعة ودون آلة حاسبة'])}
{badge_row('أتعلّم', 'القاعدة والأمثلة', 'fille')}
<div class="frame has-video">
  <ul>
    <li>لضرب عدد <span class="hl">صحيح</span> في 10، 100، 1000: نضيف على يمينه صفرًا أو صفرين أو ثلاثة أصفار.</li>
    <li>لضرب عدد <span class="hl">عشري</span> في 10، 100، 1000: ننقل الفاصلة رقمًا أو رقمين أو ثلاثة أرقام نحو <span class="hl">اليمين</span>.</li>
    <li>إذا لم تكفِ الأرقام العشرية، نضيف أصفارًا على اليمين.</li>
  </ul>
  {video_box()}
</div>
<div style="display:flex;gap:3mm;align-items:center">
  <div style="flex:1">{methode('أضرب عددًا عشريًا في 100', [
    'أعدّ أصفار العدد: في 100 صفران',
    'أنقل الفاصلة رقمين نحو اليمين: 2,4 × 100 = 240',
    'إذا نقصت الأرقام أضيف صفرًا على اليمين'])}</div>
  <div style="text-align:center;flex-shrink:0">
    {_mult100_svg(w=44)}
    <div class="pie-lab" style="font-size:7.6px">قفزتان نحو اليمين!</div>
  </div>
</div>

{badge_row('أتدرّب', 'مثال من الحياة', 'garcon')}
<div class="frame">
  <div class="exo-q">🧵 مصنع ملابس في انواكشوط تسلّم طلبية: 1000 فستان و100 سروال و1000 قميص.<br>
  يلزم: 2,225 m من القماش للفستان · 2,4 m للسروال · 1,25 m للقميص.</div>
  <div class="exemple" style="text-align:center">
    الفساتين: 2,225 × 1000 = 2 225 m &nbsp;·&nbsp; السراويل: 2,4 × 100 = 240 m &nbsp;·&nbsp; القمصان: 1,25 × 1000 = 1 250 m
  </div>
  <div class="scallop">أسرع بكثير من وضع العملية عموديًا! ⚡</div>
</div>'''
    return ('الضرب في 10 و100 و1000', body, False)


def u18_p2():
    items = ['19,28 × 10 = 19,28 أم 192,8؟', '534,7 × 100 = 5 347 أم 53 470؟', '0,875 × 1000 = 87,5 أم 875؟']
    calc = ['256,4 × 100 =', '268,87 × 10 =', '878,45 × 100 =', '0,698 × 1000 =',
            '45 × 10 =', '307 × 100 =', '6,5 × 1000 =', '0,04 × 100 =', '12,3 × 10 =']
    g = '<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:1.8mm">' + ''.join(
        f'<div style="background:#fff;border:1.2px solid #ddd2b8;border-radius:2mm;padding:1.8mm;text-align:center;font-weight:800;font-size:9.4px">{MX(c)} {OVS}</div>' for c in calc) + '</div>'
    body = f'''
{badge_row('تمارين', 'أحسب دون وضع العملية', 'garcon')}
{attention('عند الضرب تنتقل الفاصلة نحو اليمين، لا نحو اليسار! ' + MX('0,04 × 100 = 4') + ' وليس 0,0004.')}
<div class="exemple"><b class="tag">✏️ مثال محلول:</b> {MX('3,17 × 100 = 317')} — أنقل الفاصلة رقمين نحو اليمين لأن في 100 صفرين.</div>
{consigne(1, 'ضع إطارًا حول الجواب الصحيح:')}
<div class="exo-q">{'<br>'.join(MX(i) for i in items)}</div>
{consigne(2, 'احسب دون وضع العمليات:')}
{g}
{exo(3, '⭐⭐', f'كم تمرة في 12 علبة تحتوي كل منها على 100 تمرة، و10 علب تحتوي كل منها على 36 تمرة؟' + dots(2))}
{exo(4, '⭐⭐⭐', f'لتر من الزيت ثمنه {MX("54,5")} {UM}. ما ثمن 100 لتر؟ وما ثمن 1000 لتر؟' + dots(2))}'''
    return ('تمارين — الضرب في 10 و100 و1000', body, False)


def u18_p3():
    body = f'''
{badge_row('تمارين', 'أحسب أسرع من الآلة ⚡', 'fille')}
<div class="exemple"><b class="tag">✏️ مثال محلول:</b> {MX('4 × 10 = 40')} · {MX('4 × 100 = 400')} · {MX('4 × 1000 = 4 000')}.
<div style="display:flex;direction:rtl;gap:1.4mm;justify-content:center;align-items:center;margin:.4mm 0 0">{''.join(
    f'''<div style="background:#fff;border:1.2px solid #e3d8ba;border-radius:2.4mm;padding:.8mm 1.2mm;text-align:center">
      <div style="display:flex;flex-wrap:wrap;gap:.4mm;justify-content:center;max-width:10mm">{f'<span class="disc" style="background:{c};width:4.2mm;height:4.2mm;font-size:3.6px">{v}</span>' * 4}</div>
      <div style="font-weight:900;font-size:8.5px;color:#1d7fc4;font-family:Cairo;border-top:1.2px dotted #d8c9a4;margin-top:.5mm">{n}</div>
    </div>''' + ('<span style="font-weight:900;font-size:7.8px;color:#c9711a;white-space:nowrap">×10 ⬅</span>' if i < 3 else '')
    for i, (v, c, n) in enumerate([('1', '#ffd98c', '4'), ('10', '#ffc7ba', '40'), ('100', '#c6e9a4', '400'), ('1000', '#aae4f0', '4 000')]))}</div></div>
{exo(5, '⭐', 'أكمل السلسلة:' + ans_cells([f'{MX("7 × 10")} =', f'{MX("7 × 100")} =', f'{MX("7 × 1000")} =']))}
{exo(6, '⭐⭐', 'علبة عصير سعتها 0,25 L. احسب:' + ans_cells(['سعة 100 علبة', 'سعة 1000 علبة'], cols=2))}
{exo(7, '⭐⭐', 'أكمل العدد الناقص:' + eq_cells([f'{MX("3,5 ×")} {SQ} {MX("= 350")}', f'{MX("0,82 ×")} {SQ} {MX("= 820")}', f'{MX("47,8 ×")} {SQ} {MX("= 4 780")}']))}
{exo(8, '⭐⭐⭐', 'كيس سكر كتلته 2,5 kg. احسب:' + ans_cells(['كتلة 10 أكياس', 'كتلة 100 كيس', 'كتلة 1000 كيس بالطن']))}
{defi(f'في ميناء انواذيبو أُنزل من الباخرة 1000 صندوق سمك، كتلة كل صندوق 22,5 kg، وثمن الكيلوغرام 120 {UM}. ما كتلة الشحنة كلها بالطن؟ وما ثمنها الكامل؟')}'''
    return ('تمارين — الحساب السريع في الميناء', body, True)


# ═══════════ الوحدة 19 : التقاسيم غير المتساوية (C20 + rimbac) ═══════════
def u19_p1():
    body = f'''
{objectifs(['أقسم مبلغًا بين شخصين بينهما فرق معلوم',
            'أقسم عندما تكون حصة ضِعف الأخرى أو أضعافها',
            'أقسم عندما تكون حصة كسرًا من الأخرى'])}
{badge_row('أتعلّم', 'ثلاث حالات', 'fille')}
<div class="frame has-video">
  <ul>
    <li><span class="hl">1. حصتان بينهما فرق:</span> أنزع الفرق، أقسم الباقي على 2، ثم أعيد الفرق للأكبر.</li>
    <li><span class="hl">2. حصة مضاعف للأخرى:</span> أحسب عدد الحصص المتساوية ثم أقسم.</li>
    <li><span class="hl">3. حصة كسر من الأخرى:</span> أجمع أجزاء الكسر لأجد عدد الحصص.</li>
  </ul>
  {video_box()}
</div>

{badge_row('أتدرّب', 'أمثلة محلولة', 'garcon')}
<div class="frame">
  <div class="exemple"><b class="tag">1️⃣ الفرق:</b> يملك سيدي وموسى معًا 550 {UM}، ولسيدي 210 {UM} زيادة على موسى.<br>
  أنزع الفرق: <span class="mexp">550 − 210 = 340</span> ← حصة موسى: <span class="mexp">340 ÷ 2 = 170</span> {UM} ← حصة سيدي: <span class="mexp">170 + 210 = 380</span> {UM}. أتحقق: <span class="mexp">380 + 170 = 550</span> ✔</div>
  {bar_model('معًا 550 أوقية', [('حصة موسى', 170, 'var(--p-blue)'),
                                 ('مثلها لسيدي', 170, 'var(--p-blue)'),
                                 ('الفرق', 210, 'var(--p-rose)')], w=92, stagger=False, scale=.8)}
  <div class="exemple"><b class="tag">2️⃣ المضاعف:</b> عقد وخاتم ثمنهما معًا 8 800 {UM}، والعقد يساوي 3 أضعاف الخاتم.<br>
  العقد 3 حصص والخاتم حصة: <span class="mexp">3 + 1 = 4</span> ← ثمن الخاتم: <span class="mexp">8 800 ÷ 4 = 2 200</span> {UM} ← ثمن العقد: <span class="mexp">2 200 × 3 = 6 600</span> {UM} ✔</div>
  <div class="exemple"><b class="tag">3️⃣ الكسر:</b> اقتسم عبد الله ومختار 2 500 {UM}، وأخذ عبد الله {FR(2,3)} حصة مختار.<br>
  الحصص: <span class="mexp">2 + 3 = 5</span> ← عبد الله: <span class="mexp">2 500 × 2 ÷ 5 = 1 000</span> {UM} ← مختار: <span class="mexp">2 500 × 3 ÷ 5 = 1 500</span> {UM} ✔</div>
</div>'''
    return ('التقاسيم غير المتساوية', body, False)


def u19_p2():
    body = f'''
{badge_row('تمارين', 'حصتان بينهما فرق أو مضاعف', 'garcon')}
{methode('طريقة «الفرق»', [
    'أنزع الفرق من المبلغ الكلي',
    'أقسم الباقي على 2: هذه حصة الأصغر',
    'أعيد الفرق للأكبر ثم أتحقق بالجمع'])}
{astuce('تحقّق دائمًا في النهاية: مجموع الحصص يجب أن يساوي المبلغ الكلي!')}
{exo(1, '⭐⭐', f'''يملك الأخوان محمد الأمين وعبد الله معًا 720 {UM}، ولمحمد الأمين الأكبر 120 {UM} زيادة على عبد الله. ما حصة كل واحد؟ النموذج جاهز — احسب!
{bar_model('معًا 720 أوقية', [('حصة عبد الله', 300, 'var(--p-blue)', '؟'), ('مثلها لأخيه', 300, 'var(--p-blue)', '؟'), ('الفرق', 120, 'var(--p-rose)')], w=76, stagger=False, scale=.8)}''' + dots(1))}
{exo(2, '⭐⭐', f'قلم ودفتر ثمنهما معًا 60 {UM}، والدفتر يساوي ضعفي القلم. ما ثمن كل واحد؟' + draw_model(12, 'أرسم شريطًا للقلم وشريطين مثله للدفتر ثم أحسب:') + dots(1))}
{exo(3, '⭐⭐⭐', f'''حقيبة وحذاء ثمنهما معًا 4 400 {UM}، والحقيبة تساوي 3 أضعاف الحذاء. ما ثمن كل واحد؟ أكمل النموذج ثم احسب:
{bar_model('معًا 4 400 أوقية', [('الحذاء', 1100, 'var(--p-green)', '؟'), ('الحقيبة', 1100, 'var(--p-yell)', '؟'), ('', 1100, 'var(--p-yell)', '؟'), ('', 1100, 'var(--p-yell)', '؟')], w=76, stagger=False, scale=.8)}''' + dots(1))}'''
    return ('تمارين — التقاسيم غير المتساوية (1)', body, False)


def u19_p3():
    body = f'''
{badge_row('تمارين', 'حصة كسر من الأخرى', 'fille')}
<div class="exemple"><b class="tag">✏️ مثال محلول:</b> اقتسمت امرأتان 500 {UM} وأخذت الأولى {FR(1,4)} حصة الثانية ← الحصص: {MX('1 + 4 = 5')} ← الأولى: {MX('500 ÷ 5 = 100')} {UM}، الثانية: {MX('100 × 4 = 400')} {UM}.</div>
{exo(4, '⭐⭐⭐', f'''اقتسمت فاطمة وخديجة 1 500 {UM}، وأخذت فاطمة {FR(2,3)} حصة خديجة. ما حصة كل واحدة؟ أكمل النموذج ثم احسب:
{bar_model('معًا 1 500 أوقية', [('فاطمة', 300, 'var(--p-rose)', '؟'), ('', 300, 'var(--p-rose)', '؟'), ('خديجة', 300, 'var(--p-blue)', '؟'), ('', 300, 'var(--p-blue)', '؟'), ('', 300, 'var(--p-blue)', '؟')], w=76, stagger=False, scale=.8)}''' + dots(1))}
{exo(5, '⭐⭐⭐', f'اقتسم ثلاثة إخوة 900 {UM} بحيث أخذ الأول حصة، والثاني ضعفها، والثالث 3 أضعافها. ما حصة كل واحد؟' + draw_model(12, 'أرسم حصة + حصتين + 3 حصص في شريط واحد ثم أحسب:') + dots(1))}
{exo(6, '⭐⭐⭐', f'قطعة حبل طولها 550 cm قُصّت إلى قطعتين، إحداهما أطول من الأخرى بـ 50 cm. ما طول كل قطعة؟' + dots(1))}
{attention('لا تقسم المبلغ على 2 مباشرة إذا كان بين الحصتين فرق — انزع الفرق أولًا ثم اقسم!')}
{defi(f'اقتسم بحّاران في انواذيبو ثمن صيد اليوم: 12 000 {UM}، وأخذ صاحب الزورق 3 أضعاف ما أخذ مساعده. ما حصة كل واحد؟')}'''
    return ('تمارين — التقاسيم غير المتساوية (2)', body, True)


# ═══════════ الوحدة 20 : الزمن والأعداد الستينية (M5+C21) ═══════════
def u20_p1():
    body = f'''
{objectifs(['أحوّل بين الساعات والدقائق والثواني',
            'أجمع وأطرح الأعداد الستينية مع الحامل والاستلاف',
            'أحسب المدة بين توقيتين'])}
{badge_row('أتعلّم', 'القاعدة والأمثلة', 'fille')}
<div class="frame has-video">
  <ul>
    <li>وحدات الزمن: الثانية (s)، الدقيقة (min)، الساعة (h)، اليوم، الأسبوع، الشهر، السنة.</li>
    <li>{MX('1 h = 60 min = 3600 s')} · {MX('1 min = 60 s')} ← نظام <span class="hl">ستيني</span> أساسه 60.</li>
    <li>ربع ساعة = {MX('60 ÷ 4 = 15')} min · نصف ساعة = {MX('60 ÷ 2 = 30')} min.</li>
    <li><span class="hl">المدة</span> = ساعة الوصول − ساعة الانطلاق.</li>
  </ul>
  {video_box()}
</div>

{badge_row('أتدرّب', 'مثال محلول', 'garcon')}
<div class="frame">
  <div class="exo-q">🚌 انطلق أحمد في رحلة على الساعة 16 h 10 min 37 s ووصل على الساعة 18 h 37 min 51 s. ما مدة الرحلة؟</div>
  <div style="display:flex;gap:8mm;justify-content:center;margin:1mm 0">
    {clock_svg(16, 10, w=20, label='الانطلاق 16 h 10 min')}
    {clock_svg(18, 37, w=20, label='الوصول 18 h 37 min')}
  </div>
  <div class="exemple" style="text-align:center">18 h 37 min 51 s − 16 h 10 min 37 s = <b>2 h 27 min 14 s</b></div>
</div>
{methode('جمع عددين ستينيين', [
    'أجمع الثواني ثم الدقائق ثم الساعات، كلًّا في عموده',
    'إذا بلغ مجموع عمود 60 أو أكثر: أنزع 60 وأحمل 1 للعمود التالي',
    'أكتب الجواب مرتبًا: h ثم min ثم s'])}'''
    return ('قياس الزمن والأعداد الستينية', body, False)


def u20_p2():
    ops = ['2 h 33 min 5 s + 4 h 57 min 18 s =', '3 h 28 min 37 s + 6 h 45 min 23 s =',
           '2 h 05 min 25 s + 1 h 35 min 05 s =', '3 h 40 min 30 s + 2 h 29 min 50 s =',
           '3 h 42 min 5 s − 1 h 18 min 27 s =', '5 h 17 min 12 s − 4 h 48 min 57 s =',
           '7 h 08 min 56 s − 6 h 10 min 20 s =', '6 j 7 h 45 min + 2 j 21 h 57 min =']
    g = '<div style="display:grid;grid-template-columns:1fr 1fr;gap:1.8mm">' + ''.join(
        f'<div style="background:#fff;border:1.2px solid #ddd2b8;border-radius:2mm;padding:1.8mm;font-weight:800;font-size:9px;text-align:center">{o}<div class="dotl" style="height:6.5mm"></div></div>' for o in ops) + '</div>'
    body = f'''
{badge_row('تمارين', 'أضع وأنجز', 'garcon')}
<div class="exemple"><b class="tag">✏️ مثال محلول:</b> {MX('1 h 50 min + 2 h 20 min')} ← الدقائق: {MX('50 + 20 = 70')} ← أنزع 60 وأحمل 1 ساعة ← الجواب: {MX('4 h 10 min')}.</div>
{consigne(1, 'ضَع وأنجز العمليات التالية على الأعداد الستينية:')}
{g}'''
    return ('تمارين — عمليات على الأعداد الستينية', body, False)


def u20_p3():
    tt = lambda t: .05 + .90 * t  # marge pour que les étiquettes ne sortent pas du viewBox
    frise = numline(100, [tt(0), tt(60 / 145), tt(120 / 145), tt(1)],
                    {tt(0): '9 h 15', tt(60 / 145): '10 h 15', tt(120 / 145): '11 h 15', tt(1): '11 h 40'}, y=4)
    body = f'''
{badge_row('تمارين', 'مسائل الزمن ⏰', 'fille')}
{attention('عند الطرح أستلف 60 وليس 100! إذا نقصت الثواني آخذ 1 min وأحوّلها إلى 60 s.')}
<div class="exemple"><b class="tag">✏️ مثال محلول:</b> بدأ درس على {MX('9 h 15 min')} وانتهى على {MX('11 h 40 min')} ← المدة = {MX('11 h 40 min − 9 h 15 min = 2 h 25 min')}.<br>
{frise}
<div class="pie-lab" style="font-size:8.4px">أعدّ بالقفزات على المستقيم: ساعة + ساعة + 25 دقيقة = {MX('2 h 25 min')}</div></div>
{exo(2, '⭐⭐', 'بدأت مباراة على الساعة 16 h 37 min وانتهت على 18 h 21 min، وكل شوط يدوم 45 min. ما مدة الاستراحة بين الشوطين؟' + dots(2))}
{exo(3, '⭐⭐⭐', 'تبدأ مباراة كرة قدم على الساعة 16 h 15 min: شوطان مدة كل منهما 45 min تفصل بينهما استراحة ربع ساعة. متى تنتهي المباراة عاديًّا؟' + dots(2))}
{exo(4, '⭐⭐⭐', 'أشرقت الشمس يوم 27 نوفمبر على 7 h 06 min 35 s وغربت على 18 h 25 min 15 s. احسب مدة النهار.' + dots(2))}
{exo(5, '⭐⭐', 'عادةً يتنفس الطفل حوالي 20 مرة في الدقيقة. كم مرة يتنفس في 24 ساعة؟' + dots(1))}'''
    return ('تمارين — مسائل الزمن', body, False)


def u20_p4():
    body = f'''
{badge_row('تمارين', 'أتقن التحويلات ⏱️', 'garcon')}
{astuce('احفظ: نصف ساعة = 30 min · ربع ساعة = 15 min · ثلث ساعة = 20 min — تُسرِع حسابك كثيرًا!')}
<div class="exemple"><b class="tag">✏️ مثال محلول:</b> {MX('2 h = 2 × 60 = 120 min')} · {MX('3 min = 3 × 60 = 180 s')}.</div>
{exo(6, '⭐', f'حوّل: 3 h = {OVS} min · 5 min = {OVS} s · 120 min = {OVS} h · 2 j = {OVS} h')}
{exo(7, '⭐⭐', f'حوّل إلى صيغة مختلطة: 95 min = {OVS} h {OVS} min &nbsp;·&nbsp; 200 s = {OVS} min {OVS} s')}
{exo(8, '⭐⭐', 'ينطلق باص المدرسة على الساعة 7 h 45 min ويصل على 8 h 20 min. ما مدة الرحلة؟' + dots(1))}
{exo(9, '⭐⭐⭐', 'نام طفل على الساعة 21 h 30 min واستيقظ على 6 h 15 min صباحًا. كم دامت مدة نومه؟ أعدّ بالقفزات على المستقيم:'
     + numline(64, [.05, .31, .95], {.05: '21 h 30', .31: '00 h 00', .95: '6 h 15'}, y=4) + dots(1))}
{defi('ينطلق قطار الحديد من ازويرات على الساعة 6 h 45 min وتدوم الرحلة إلى انواذيبو 16 h 40 min. في أي ساعة يصل القطار؟')}'''
    return ('تمارين — تحويلات الزمن ومسائله', body, True)


# ═══════════ الوحدة 21 : التناسبية (C22) ═══════════
def u21_p1():
    body = f'''
{objectifs(['أتعرّف المقادير المتناسبة',
            'أكمل جدول تناسبية بمعامل الضرب',
            'أستعمل القاعدة الثلاثية لحل المسائل'])}
{badge_row('أتعلّم', 'القاعدة والأمثلة', 'fille')}
<div class="frame has-video">
  <ul>
    <li>مقداران <span class="hl">متناسبان</span> إذا انتقلنا من أحدهما إلى الآخر بالضرب في نفس العدد.</li>
    <li>نستعمل <span class="hl">جدول التناسبية</span> أو <span class="hl">القاعدة الثلاثية</span> (الضرب التقاطعي).</li>
  </ul>
  {video_box()}
</div>
{methode('القاعدة الثلاثية', [
    'أنظّم المعطيات الثلاثة في جدول تناسبية',
    'أضرب العددين المتقاطعين المعلومين',
    'أقسم الناتج على العدد الثالث'])}

{badge_row('أتدرّب', 'مثال محلول', 'garcon')}
<div class="frame">
  <div class="exo-q">🥖 خمس خبزات ثمنها 75 {UM}. ما ثمن 3 خبزات؟ و11 خبزة؟</div>
  {prop_table('عدد الخبزات', f'الثمن بـ{UM}', [5, 3, 11], [75, '?', '?'])}
  <div class="exemple" style="text-align:center">ثمن 3 خبزات = 75 × 3 ÷ 5 = <b>45</b> · ثمن 11 خبزة = 75 × 11 ÷ 5 = <b>165</b></div>
</div>'''
    return ('التناسبية', body, False)


def u21_p2():
    body = f'''
{badge_row('تمارين', 'جداول التناسبية', 'garcon')}
{figure_img(FIGS['etal_marche'], 32, 'في السوق: كلما زاد عدد القطع زاد الثمن بنفس النسبة!')}
<div class="exemple"><b class="tag">✏️ مثال محلول:</b> إذا كان ثمن القطعة 5 {UM} فثمن 4 قطع: {MX('4 × 5 = 20')} {UM}، وبـ 30 {UM} أشتري {MX('30 ÷ 5 = 6')} قطع.</div>
{consigne(1, f'قطعة حلوى ثمنها 5 {UM}. أكمل الجدول:')}
{prop_table('عدد القطع', f'الثمن بـ{UM}', [1, '?', 14, '?'], [5, 25, '?', 100])}
{consigne(2, 'يستعمل مزارع 8 kg من السماد لكل 2 m² من المشتلة. أكمل جدول التناسبية:')}
{prop_table('المساحة بالمتر المربع', 'كمية السماد بـ kg', [1, 2, 5, 10], ['?', 8, '?', '?'])}
{exo(3, '⭐⭐', 'يلزم موسى 6 kg من السماد لتسميد 2 m² من مشتلته. كم كيلوغرامًا يلزمه لتسميد 10 m²؟' + dots(2))}
{exo(4, '⭐⭐⭐', f'اشترت أم سلمة من سوق العاصمة 4 أمتار من قماش الملحفة بـ 480 {UM}. ما ثمن 7 أمتار من نفس القماش؟' + dots(1))}'''
    return ('تمارين — التناسبية', body, False)


def u21_p3():
    body = f'''
{badge_row('تمارين', 'مسائل التناسبية 🧮', 'fille')}
{astuce('ابحث أولًا عن ثمن الوحدة الواحدة: إذا عرفت ثمن القطعة الواحدة سهُل عليك كل شيء!')}
{attention('ليس كل شيء متناسبًا! عمر الطفل وطوله لا يتناسبان: في 12 سنة لا يكون طولك ضِعف طولك في 6 سنوات.')}
<div class="exemple"><b class="tag">✏️ مثال محلول:</b> 4 خبزات ثمنها 60 {UM} ← الخبزة الواحدة: {MX('60 ÷ 4 = 15')} {UM} ← ثمن 7 خبزات: {MX('7 × 15 = 105')} {UM}.
{bar_model('4 خبزات = 60 أوقية', [('خبزة', 15, '#ffd98c'), ('خبزة', 15, '#ffd98c'), ('خبزة', 15, '#ffd98c'), ('خبزة', 15, '#ffd98c')], w=52, stagger=False, scale=.75)}</div>
{exo(5, '⭐', f'3 أقلام ثمنها 45 {UM}. ما ثمن قلم واحد؟ وما ثمن 8 أقلام؟' + dots(2))}
{exo(6, '⭐⭐', 'سيارة تستهلك 8 لترات من الوقود لكل 100 km. كم لترًا تستهلك في 250 km؟' + dots(1))}
{exo(7, '⭐⭐⭐', 'لتحضير الكسكس لـ 5 أشخاص يلزم 750 g من القمح. كم غرامًا يلزم لـ 8 أشخاص؟' + dots(1))}
{defi(f'تعاونية نسوية في كيهيدي تبيع 4 لترات من الحليب بـ 720 {UM}. كم لترًا يمكن شراؤه بـ 1 260 {UM}؟')}'''
    return ('تمارين — التناسبية في السوق', body, True)


# ═══════════ الوحدة 22 : الحركة المنتظمة (C24) ═══════════
def u22_p1():
    body = f'''
{objectifs(['أفهم معنى السرعة المتوسطة (km/h)',
            'أحسب السرعة أو المسافة أو الزمن بالقاعدة المناسبة',
            'أحوّل الزمن إلى وحدة واحدة قبل الحساب'])}
{badge_row('أتعلّم', 'القاعدة والأمثلة', 'fille')}
<div class="frame has-video">
  <ul>
    <li><span class="hl">السرعة المتوسطة</span>: المسافة المقطوعة في ساعة واحدة (km/h أو m/s).</li>
  </ul>
  <div style="display:flex;gap:3mm;align-items:center">
    <div style="flex:1">
      {formula('السرعة = المسافة ÷ الزمن', 'var(--p-yell)')}
      {formula('المسافة = السرعة × الزمن', 'var(--p-green)')}
      {formula('الزمن = المسافة ÷ السرعة', 'var(--p-blue)')}
    </div>
    <div style="text-align:center;flex-shrink:0">
      {_dvt_triangle()}
      <div class="pie-lab" style="font-size:7.6px">غطِّ المطلوب بإصبعك!</div>
    </div>
  </div>
  {video_box()}
</div>

{figure_img(FIGS['train'], 37, 'قطار المعادن ازويرات–انواذيبو: من أطول قطارات العالم!')}
{badge_row('أتدرّب', 'مثال محلول 🚂', 'garcon')}
<div class="frame">
  <div class="exo-q">قطار ازويرات–انواذيبو يسير بسرعة 42 km/h. ما المسافة التي يقطعها في ساعة و40 دقيقة؟</div>
  <div class="exemple" style="text-align:center">1 h 40 min = 100 min ← المسافة = 42 × 100 ÷ 60 = <b>70 km</b></div>
</div>
{methode('أحسب المسافة المقطوعة', [
    'أحوّل الزمن كله إلى دقائق (أو ساعات)',
    'أطبّق القاعدة: المسافة = السرعة × الزمن',
    'أتأكد أن الجواب بالوحدة الصحيحة (km)'])}'''
    return ('الحركة المنتظمة: السرعة والمسافة والزمن', body, False)


def u22_p2():
    body = f'''
{badge_row('تمارين', 'أحسب السرعة والمسافة والزمن', 'garcon')}
{astuce('السرعة 60 km/h تعني: 60 كيلومترًا في كل ساعة، أي 30 km في نصف ساعة و1 km في كل دقيقة!')}
<div class="exemple"><b class="tag">✏️ مثال محلول:</b> قطع راكب دراجة {MX('40 km')} في ساعتين ← السرعة = {MX('40 ÷ 2 = 20 km/h')}.
{numline(60, [.05, .5, .95], {.05: '0', .5: '1 h · 20 km', .95: '2 h · 40 km'}, y=4)}</div>
{exo(1, '⭐', 'يمشي أحمدو 3 ساعات ليقطع 12 km بين قريته والمدينة. ما المسافة التي يقطعها في ساعة واحدة؟' + dots(1))}
{exo(2, '⭐⭐', 'قطار ازويرات–انواذيبو يسير بسرعة 42 km/h. ما المسافة التي قطعها بين 11 h 40 min و14 h 10 min؟' + dots(2))}
{exo(3, '⭐⭐⭐', 'سيارة تسير بسرعة 90 km/h. احسب الزمن اللازم لقطع: 150 km ثم 300 km.' + dots(2))}
{exo(4, '⭐⭐', 'قطع دراج 60 km في ساعتين. ما سرعته المتوسطة؟' + dots(2))}'''
    return ('تمارين — الحركة المنتظمة (1)', body, False)


def u22_p3():
    body = f'''
{badge_row('تمارين', 'مسائل السرعة ✈️', 'fille')}
<div class="exemple"><b class="tag">✏️ مثال محلول:</b> طائرة سرعتها {MX('500 km/h')} تقطع {MX('1 000 km')} في: {MX('1 000 ÷ 500 = 2 h')}.
{numline(60, [.05, .5, .95], {.05: '0', .5: '1 h · 500 km', .95: '2 h · 1 000 km'}, y=4)}</div>
{exo(5, '⭐⭐⭐', 'المسافة الجوية انواكشوط–النعمة 963 km. كم من الوقت تستغرق طائرة سرعتها 642 km/h لربط المدينتين؟' + dots(1))}
{exo(6, '⭐⭐⭐', 'عبر الطريق، المسافة بين المدينتين 1 080 km. كم يومًا كانت تستغرق قافلة تسير بسرعة 4 km/h وتمشي 10 ساعات في اليوم؟<div class="dashcard tall"></div>' + dots(1))}
{exo(7, '⭐⭐', 'يقطع عدّاء 400 m في دقيقتين. ما سرعته بالمتر في الدقيقة؟' + dots(1))}
{attention('لا تخلط الوحدتين: 1 h 40 min ليست 140 دقيقة بل 100 دقيقة! حوّل دائمًا قبل الحساب.')}
{defi('قطار الحديد الشهير — أطول القطارات في العالم — يقطع 704 km بين ازويرات وانواذيبو بسرعة متوسطة 44 km/h. كم ساعة تدوم الرحلة؟')}'''
    return ('تمارين — الحركة المنتظمة (2)', body, True)


# ═══════════ الوحدة 23 : السلم والتصاميم والخرائط (C25) ═══════════
def u23_p1():
    body = f'''
{objectifs([f'أفهم معنى سلم الخريطة مثل {FR(1,100)}',
            'أحسب البعد الحقيقي انطلاقًا من الخريطة وبالعكس',
            'أوحّد الوحدات قبل كل حساب'])}
{badge_row('أتعلّم', 'القاعدة والأمثلة', 'fille')}
<div class="frame has-video">
  <ul>
    <li><span class="hl">السلم</span> كسر (بسطه غالبًا 1) نضرب فيه الأبعاد الحقيقية لنحصل على أبعاد التصميم.</li>
  </ul>
  {formula('البعد على التصميم = البعد الحقيقي × السلم', 'var(--p-yell)')}
  {formula('البعد الحقيقي = البعد على التصميم × مقام السلم', 'var(--p-green)')}
  {formula('السلم = البعد على التصميم ÷ البعد الحقيقي', 'var(--p-blue)')}
  {video_box()}
</div>

{badge_row('أتدرّب', 'مثال محلول 🗺️', 'garcon')}
<div class="frame">
  <div class="exo-q">على خريطة موريتانيا بسلم {FR(1,'3 000 000')}، المسافة انواكشوط–ابوتلميت ممثلة بـ 5 cm. ما المسافة الحقيقية؟</div>
  <div class="exemple" style="text-align:center">5 cm × 3 000 000 = 15 000 000 cm = 150 km</div>
  {_scale_lines()}
</div>
{methode('من الخريطة إلى الحقيقة', [
    'أقيس البعد على الخريطة بالسنتيمتر',
    'أضرب في مقام السلم ثم أحوّل الجواب إلى وحدة مناسبة (m أو km)'])}'''
    return ('السلم: التصاميم والخرائط', body, False)


def u23_p2():
    body = f'''
{badge_row('تمارين', 'أقرأ الخرائط', 'garcon')}
{astuce('السلم ' + FR(1,100) + ' يعني: كل 1 cm على التصميم = 100 cm = 1 m في الحقيقة.')}
{attention('السلم = البعد على التصميم ÷ البعد الحقيقي، بعد توحيد الوحدتين — لا تقسم قبل التحويل!')}
<div class="exemple"><b class="tag">✏️ مثال محلول:</b> طول حقيقي {MX('7 m = 700 cm')} بسلم {FR(1,100)} ← على التصميم: {MX('700 ÷ 100 = 7 cm')}.</div>
{exo(1, '⭐⭐', f'لدى المهندس أحمد أرض مستطيلة أبعادها: 9 m، 11 m، يرسمها بسلم {FR(1,100)}. ما بعدا التصميم بالسنتيمتر؟' + dots(2))}
{exo(2, '⭐⭐', 'على خريطة نقرأ: «1 cm على التصميم يمثل 250 m في الحقيقة». ما سلم هذه الخريطة؟' + dots(2))}
{exo(3, '⭐⭐', f'بسلم {FR(1,50)}، ما البعد الحقيقي الذي تمثله مسافة 3,5 cm على التصميم؟' + dots(2))}
{exo(4, '⭐⭐⭐', f'المسافة الحقيقية بين قريتين 12 km، ومُثّلت على خريطة بـ 6 cm. ما سلم الخريطة؟' + dots(2))}'''
    return ('تمارين — السلم والخرائط', body, False)


def u23_p3():
    body = f'''
{badge_row('تمارين', 'مهندس صغير 📐', 'fille')}
<div class="exemple"><b class="tag">✏️ مثال محلول:</b> بسلم {FR(1,'1 000')}: {MX('2 cm')} على التصميم = {MX('2 × 1 000 = 2 000 cm = 20 m')} في الحقيقة.</div>
{exo(5, '⭐', f'بسلم {FR(1, "1 000")}: ما البعد الحقيقي بالمتر الذي يمثله على التصميم: 1 cm؟ 4 cm؟ 7,5 cm؟' + dots(2))}
{exo(6, '⭐⭐', f'قاعة صفّك طولها 8 m وعرضها 6 m. تريد رسمها بسلم {FR(1,200)}. ما بعدا الرسم بالسنتيمتر؟' + dots(2))}
{exo(7, '⭐⭐⭐', f'على خريطة بسلم {FR(1, "2 000 000")}، المسافة بين انواكشوط وروصو ممثلة بـ 10 cm. ما المسافة الحقيقية بالكيلومتر؟' + dots(2))}
{defi('المسافة على الطريق بين انواكشوط وابوتلميت حوالي 150 km. يريد مهندس تمثيلها بـ 5 cm على خريطة. ما السلم الذي يجب أن يختاره؟')}'''
    return ('تمارين — أرسم تصاميمي', body, True)


# ═══════════ الوحدة 24 : الفائدة السنوية (rimbac) ═══════════
def u24_p1():
    body = f'''
{objectifs(['أحسب الفائدة السنوية من رأس المال والنسبة',
            'أحسب فائدة عدة أشهر',
            'أجد النسبة أو رأس المال عند الحاجة'])}
{badge_row('أتعلّم', 'القاعدة والأمثلة', 'fille')}
<div class="frame has-video">
  <ul>
    <li>من يضع <span class="hl">رأس مال</span> في البنك يحصل على <span class="hl">فائدة سنوية</span> حسب <span class="hl">نسبة التوظيف</span>.</li>
  </ul>
  {formula('الفائدة السنوية = رأس المال × النسبة ÷ 100', 'var(--p-yell)')}
  {formula('فائدة عدة أشهر = الفائدة السنوية × عدد الأشهر ÷ 12', 'var(--p-green)')}
  {formula('النسبة = الفائدة السنوية × 100 ÷ رأس المال', 'var(--p-blue)')}
  {formula('رأس المال = الفائدة السنوية × 100 ÷ النسبة', 'var(--p-rose)')}
  {video_box()}
</div>
<div style="display:flex;gap:3mm;align-items:center;margin:.8mm 0">
  {figure_img(FIGS['fermiere_poules'], 16, '')}
  <div style="flex:1;font-size:9.2px;font-weight:700;line-height:1.45;color:#6b5d3f">تبيع مربّية الدجاج بيضها وتوظّف مدخراتها لتحصل على فائدة سنوية.</div>
</div>
{methode('أحسب فائدة عدة أشهر', [
    'أحسب الفائدة السنوية: رأس المال × النسبة ÷ 100',
    'أضرب في عدد الأشهر ثم أقسم على 12'])}
{attention('النسبة سنوية! لا تطبّقها على الأشهر مباشرة: أحسب فائدة السنة كاملة أولًا ثم خذ نصيب الأشهر.')}
<div class="exemple"><b class="tag">💰 مثال:</b> وظّف تاجر 20 000 {UM} بنسبة 5 %. الفائدة السنوية = <span class="mexp">20 000 × 5 ÷ 100 = 1 000</span> {UM} ← فائدة 6 أشهر = <span class="mexp">1 000 × 6 ÷ 12 = 500</span> {UM}.</div>'''
    return ('الفائدة السنوية', body, False)


def u24_p2():
    body = f'''
{badge_row('تمارين', 'أحسب الفائدة', 'garcon')}
{astuce(f'النسبة 5 % تعني: كل 100 {UM} من رأس المال تُنتج 5 {UM} فائدة في السنة.')}
<div class="exemple"><b class="tag">✏️ مثال محلول:</b> وظّف تاجر 10 000 {UM} بنسبة 6 % ← الفائدة السنوية = {MX('10 000 × 6 ÷ 100 = 600')} {UM}.</div>
{exo(1, '⭐⭐', f'وظّف سيدي محمد 30 000 {UM} بنسبة 4 %. ما فائدته السنوية؟' + dots(2))}
{exo(2, '⭐⭐', f'''وظّفت عيشة 12 000 {UM} بنسبة 5 %. ما فائدتها بعد 3 أشهر؟ أكمل النموذج: أحسب فائدة السنة ثم آخذ ربعها:
{bar_model('الفائدة السنوية = ؟', [('3 أشهر', 150, 'var(--p-green)', '؟'), ('3 أشهر', 150, '#fff', ''), ('3 أشهر', 150, '#fff', ''), ('3 أشهر', 150, '#fff', '')], w=64, stagger=False, scale=.75)}''' + dots(1))}
{exo(3, '⭐⭐⭐', f'رأس مال قدره 50 000 {UM} أعطى فائدة سنوية 2 500 {UM}. ما نسبة التوظيف؟' + dots(2))}
{exo(4, '⭐⭐⭐', f'أعطى رأس مال فائدة سنوية 1 800 {UM} بنسبة 6 %. ما قيمة رأس المال؟' + dots(1))}'''
    return ('تمارين — الفائدة السنوية', body, False)


def u24_p3():
    body = f'''
{badge_row('تمارين', 'تاجر ذكي 💰', 'fille')}
<div class="exemple"><b class="tag">✏️ مثال محلول:</b> وظّفت خديجة 40 000 {UM} بنسبة 2 % ← الفائدة السنوية = {MX('40 000 × 2 ÷ 100 = 800')} {UM}.</div>
{exo(5, '⭐', f'وظّف مزارع من روصو 10 000 {UM} بنسبة 3 %. ما فائدته السنوية؟' + dots(2))}
{exo(6, '⭐⭐', f'وظّف تاجر من سوق العاصمة 24 000 {UM} بنسبة 5 %. ما فائدته بعد 9 أشهر؟' + dots(2))}
{exo(7, '⭐⭐⭐', f'أعطى رأس مال قدره 45 000 {UM} فائدةً عن 6 أشهر قدرها 1 350 {UM}. ما نسبة التوظيف السنوية؟' + draw_model(12))}
{defi(f'باعت تعاونية تمور في أطار محصولها بـ 60 000 {UM} ووظّفت المبلغ في البنك بنسبة 5 %. كم تحصل من فائدة بعد سنة كاملة؟ وبعد 4 أشهر فقط؟')}'''
    return ('تمارين — أوظّف وأربح', body, True)


# ═══════════ الوحدة 25 : الفواصل (rimbac intervalles) ═══════════
def u25_p1():
    def line_svg(closed=False, ends=2):
        if closed:
            dots_ = ''.join(f'<circle cx="{13+9*__import__("math").cos(i*1.047)}" cy="{9+7*__import__("math").sin(i*1.047)}" r="1.1" fill="#c0392b"/>' for i in range(6))
            return f'<svg width="26mm" height="18mm" viewBox="0 0 26 18"><ellipse cx="13" cy="9" rx="9" ry="7" fill="none" stroke="#2f6ea5" stroke-width=".8"/>{dots_}</svg>'
        xs = [3, 8, 13, 18, 23]
        if ends == 0: pts = xs[1:-1]
        elif ends == 1: pts = xs[:-1]
        else: pts = xs
        d = ''.join(f'<circle cx="{x}" cy="6" r="1.1" fill="#c0392b"/>' for x in pts)
        return f'<svg width="26mm" height="12mm" viewBox="0 0 26 12"><line x1="2" y1="6" x2="24" y2="6" stroke="#2f6ea5" stroke-width=".8"/>{d}</svg>'
    body = f'''
{objectifs(['أميّز الخط المغلق والخط المفتوح في مسائل الفواصل',
            'أختار القاعدة الصحيحة: أزيد 1 أو أنقص 1 أو لا شيء',
            'أحل مسائل الأشجار والأعمدة'])}
{badge_row('أتعلّم', 'أربع حالات', 'fille')}
<div class="frame has-video">
  <ul>
    <li><span class="hl">خط مغلق</span> (دائرة): عدد الفواصل = عدد الأشياء.</li>
    <li><span class="hl">خط مفتوح بشيء في الطرفين:</span> عدد الأشياء = عدد الفواصل + 1.</li>
    <li><span class="hl">خط مفتوح دون شيء في الطرفين:</span> عدد الأشياء = عدد الفواصل − 1.</li>
    <li><span class="hl">خط مفتوح بشيء في طرف واحد:</span> عدد الأشياء = عدد الفواصل.</li>
  </ul>
  {video_box()}
</div>

{badge_row('أتدرّب', 'ألاحظ الرسوم', 'garcon')}
<div class="frame">
  <div style="display:flex;gap:2mm;justify-content:center;align-items:flex-end">
    <div style="text-align:center">{line_svg(closed=True)}<div class="pie-lab">مغلق: 6 = 6</div></div>
    <div style="text-align:center">{line_svg(ends=2)}<div class="pie-lab">طرفان: 5 أشياء، 4 فواصل</div></div>
    <div style="text-align:center">{line_svg(ends=0)}<div class="pie-lab">دون طرفين: 3 أشياء، 4 فواصل</div></div>
    <div style="text-align:center">{line_svg(ends=1)}<div class="pie-lab">طرف واحد: 4 = 4</div></div>
  </div>
</div>'''
    return ('الفواصل', body, False)


def u25_p2():
    body = f'''
{badge_row('تمارين', 'مسائل الفواصل 🌴', 'garcon')}
{astuce('قبل أي حساب أرسم رسمًا صغيرًا: خط ونقاط! الرسم يريك القاعدة الصحيحة فورًا.')}
{attention('في الخط المغلق (الدائرة) لا نزيد 1 أبدًا: عدد الأشياء = عدد الفواصل تمامًا.')}
<div class="exemple"><b class="tag">✏️ مثال محلول:</b> طريق طولها {MX('20 m')}، شجرة كل {MX('5 m')} وفي كل طرف شجرة ← الفواصل: {MX('20 ÷ 5 = 4')} ← الأشجار: {MX('4 + 1 = 5')}.
{numline(56, [.05, .275, .5, .725, .95], {.05: '0', .275: '5', .5: '10', .725: '15', .95: '20 m'}, y=4)}
<div class="pie-lab" style="font-size:7.6px">🌴 شجرة عند كل علامة: 4 فواصل ← 5 أشجار</div></div>
{exo(1, '⭐⭐', 'غُرست أشجار نخيل على طول طريق مستقيمة طولها 100 m، بين كل شجرتين 10 m، وفي كل طرف شجرة. كم شجرة غُرست؟' + dots(1))}
{exo(2, '⭐⭐', 'حول حديقة دائرية محيطها 60 m وُضعت أعمدة إنارة، بين كل عمودين 5 m. كم عمودًا وُضع؟' + dots(1))}
{exo(3, '⭐⭐⭐', 'بين عمودين كهربائيين ثابتين مسافة 90 m، نريد وضع أعمدة وسيطة بين كل عمودين 15 m (دون الطرفين). كم عمودًا وسيطًا نضع؟' + dots(2))}
{exo(4, '⭐⭐⭐', 'صفّ من الأشجار يبدأ بشجرة عند باب المدرسة (طرف واحد فقط)، بين كل شجرتين 8 m، وعدد الأشجار 12. ما طول الصف؟' + dots(2))}'''
    return ('تمارين — الفواصل', body, False)


def u25_p3():
    body = f'''
{badge_row('تمارين', 'مهندس الطرق 🛣️', 'fille')}
<div class="exemple"><b class="tag">✏️ مثال محلول:</b> سور طوله {MX('30 m')}، عمود كل {MX('10 m')} وفي الطرفين عمودان ← {MX('30 ÷ 10 = 3')} فواصل ← {MX('3 + 1 = 4')} أعمدة.
{numline(56, [.05, .35, .65, .95], {.05: '0', .35: '10', .65: '20', .95: '30 m'}, y=4)}</div>
{exo(5, '⭐', 'سور مستقيم طوله 40 m، نضع عمودًا كل 8 m وفي كل طرف عمود. كم عمودًا نحتاج؟' + dots(1))}
{exo(6, '⭐⭐', 'ساحة دائرية محيطها 72 m، تُغرس شجرة كل 6 m. كم شجرة تُغرس؟' + dots(1))}
{exo(7, '⭐⭐⭐', 'بين الطابق الأرضي والطابق الثالث من عمارة 45 درجة سُلَّم. كم درجة بين كل طابقين متتاليين؟' + dots(2))}
{defi(f'على طول شارع مستقيم في انواكشوط طوله 240 m، تريد البلدية وضع أعمدة إنارة كل 20 m وفي الطرفين عمودان. كم عمودًا تشتري؟ وإذا كان ثمن العمود 4 500 {UM} فما التكلفة الكاملة؟')}'''
    return ('تمارين — فواصل حول المدينة', body, True)


# ═══════ الوحدة 26 : الكتلة القائمة والصافية والفارغ (rimbac tare) ═══════
def u26_p1():
    body = f'''
{objectifs(['أميّز الكتلة القائمة والكتلة الصافية والفارغ',
            'أستعمل العلاقات الثلاث بينها',
            'أوحّد الوحدات (kg وg) قبل الحساب'])}
{badge_row('أتعلّم', 'القاعدة والأمثلة', 'fille')}
<div class="frame has-video">
  <ul>
    <li><span class="hl">الكتلة القائمة</span>: كتلة المنتوج + كتلة الغلاف (مثال: قارورة الزيت مملوءة).</li>
    <li><span class="hl">الكتلة الصافية</span>: كتلة المنتوج وحده (الزيت).</li>
    <li><span class="hl">الفارغ</span>: كتلة الغلاف وحده (القارورة الفارغة).</li>
  </ul>
  {formula('الكتلة القائمة = الكتلة الصافية + الفارغ', 'var(--p-yell)')}
  {formula('الكتلة الصافية = الكتلة القائمة − الفارغ', 'var(--p-green)')}
  {formula('الفارغ = الكتلة القائمة − الكتلة الصافية', 'var(--p-blue)')}
  {video_box()}
</div>
{methode('أجد الكتلة الصافية', [
    'أوحّد الوحدتين: أحوّل كل شيء إلى g أو إلى kg',
    'أطرح: الكتلة الصافية = الكتلة القائمة − الفارغ'])}
<div class="exemple"><b class="tag">🫙 مثال:</b> قارورة عسل كتلتها القائمة 1,2 kg وفارغها 200 g ← الكتلة الصافية = <span class="mexp">1 200 − 200 = 1 000</span> g = 1 kg.</div>
{container_svg('1,2 kg', '1 000 g', '200 g')}'''
    return ('الكتلة القائمة والكتلة الصافية والفارغ', body, False)


def u26_p2():
    body = f'''
{badge_row('تمارين', 'قائمة، صافية أم فارغ؟', 'garcon')}
{astuce('الكتلة القائمة أكبر دائمًا من الصافية! إذا وجدت «صافية» أكبر من «قائمة» فراجع حسابك.')}
{attention('وحّد الوحدتين قبل الطرح: ' + MX('5 kg − 500 g') + ' تصبح ' + MX('5 000 g − 500 g = 4 500 g') + '.')}
<div class="exemple"><b class="tag">✏️ مثال محلول:</b> قارورة زيت كتلتها القائمة {MX('2 kg = 2 000 g')} وفارغها {MX('300 g')} ← الصافية = {MX('2 000 − 300 = 1 700 g')}.
{bar_model('الكتلة القائمة = 2 000 g', [('الصافية', 1700, 'var(--p-green)'), ('الفارغ', 300, 'var(--p-rose)')], w=64, stagger=False, scale=.75)}</div>
{exo(1, '⭐', 'علبة سمن كتلتها القائمة 5 kg وفارغها 500 g. ما كتلتها الصافية؟' + dots(1))}
{exo(2, '⭐⭐', 'كيس أرز كتلته الصافية 25 kg وفارغه 250 g. ما كتلته القائمة؟' + dots(1))}
{exo(3, '⭐⭐', 'برميل زيت كتلته القائمة 180 kg وكتلته الصافية 165 kg. ما فارغه؟' + dots(1))}
{exo(4, '⭐⭐⭐', f'اشترى تاجر 10 صناديق تمر، الكتلة القائمة لكل صندوق 12 kg وفارغه 1,5 kg. ما الكتلة الصافية للتمر كله؟' + draw_model(12) + dots(1))}'''
    return ('تمارين — الكتلة القائمة والصافية', body, False)


def u26_p3():
    body = f'''
{badge_row('تمارين', 'في المخزن والميناء ⚖️', 'fille')}
<div class="exemple"><b class="tag">✏️ مثال محلول:</b> علبة تمر كتلتها القائمة {MX('800 g')} وفارغها {MX('100 g')} ← الصافية = {MX('800 − 100 = 700 g')}.</div>
{exo(5, '⭐', 'قارورة ماء كتلتها القائمة 1 550 g وفارغها 50 g. ما كتلتها الصافية؟' + dots(1))}
{exo(6, '⭐⭐', f'''علبة حليب مجفف كتلتها الصافية 2,5 kg وفارغها 300 g. ما كتلتها القائمة بالغرام؟ النموذج جاهز — وحّد الوحدتين ثم اجمع:
{bar_model('الكتلة القائمة = ؟', [('الصافية', 2500, 'var(--p-green)', '2,5 kg'), ('الفارغ', 300, 'var(--p-rose)', '300')], w=64, stagger=False, scale=.75)}''' + dots(1))}
{exo(7, '⭐⭐⭐', 'اشترت مريم من دكان الحي 3 أكياس دقيق، الكتلة القائمة لكل كيس 50 kg وفارغه 400 g. ما الكتلة الصافية الإجمالية بالكيلوغرام؟' + dots(2))}
{defi(f'في ميناء انواذيبو، صندوق سمك كتلته القائمة 30 kg وفارغه 2,5 kg. حمل زورق 40 صندوقًا. ما الكتلة الصافية للسمك كله؟ وإذا بيع الكيلوغرام بـ 150 {UM} فما ثمن الحمولة؟')}'''
    return ('تمارين — الكتلة الصافية في السوق', body, True)


UNITS_4 = [
    dict(num=16, title='مضاعفات الأعداد وقابلية القسمة', sub='المضاعفات والقواسم · قواعد 2، 3، 5، 9…', color='var(--p-yell)',
         pages=[u16_p1(), u16_p2(), u16_p3()]),
    dict(num=17, title='الكسور المتكافئة وجمع الكسور', sub='التكافؤ والتبسيط · الجمع والطرح · كسر من عدد', color='var(--p-rose)',
         pages=[u17_p1(), u17_p2(), u17_p3(), u17_p4()]),
    dict(num=18, title='الضرب في 10 و100 و1000', sub='الحساب السريع بنقل الفاصلة', color='var(--p-green)',
         pages=[u18_p1(), u18_p2(), u18_p3()]),
    dict(num=19, title='التقاسيم غير المتساوية', sub='الفرق · المضاعف · الكسر', color='var(--p-blue)',
         pages=[u19_p1(), u19_p2(), u19_p3()]),
    dict(num=20, title='الزمن والأعداد الستينية', sub='h، min، s · حساب المدد', color='var(--p-lila)',
         pages=[u20_p1(), u20_p2(), u20_p3(), u20_p4()]),
    dict(num=21, title='التناسبية', sub='جدول التناسبية والقاعدة الثلاثية', color='var(--p-yell)',
         pages=[u21_p1(), u21_p2(), u21_p3()]),
    dict(num=22, title='الحركة المنتظمة', sub='السرعة والمسافة والزمن', color='var(--p-rose)',
         pages=[u22_p1(), u22_p2(), u22_p3()]),
    dict(num=23, title='السلم والخرائط', sub='من التصميم إلى الحقيقة وبالعكس', color='var(--p-green)',
         pages=[u23_p1(), u23_p2(), u23_p3()]),
    dict(num=24, title='الفائدة السنوية', sub='رأس المال والنسبة والفائدة', color='var(--p-blue)',
         pages=[u24_p1(), u24_p2(), u24_p3()]),
    dict(num=25, title='الفواصل', sub='الأشجار والأعمدة على الخطوط', color='var(--p-lila)',
         pages=[u25_p1(), u25_p2(), u25_p3()]),
    dict(num=26, title='الكتلة القائمة والصافية والفارغ', sub='الغلاف والمنتوج', color='var(--p-yell)',
         pages=[u26_p1(), u26_p2(), u26_p3()]),
]
