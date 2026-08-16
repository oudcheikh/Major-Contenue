# -*- coding: utf-8 -*-
"""Unités 1-5 : grands nombres · fractions · jointure +/− · multiplication · division.
Contenu repris fidèlement des diapositives 2 à 20 de math_principal_ar_A5.pptx."""
from figs_pptx import FIGS
from base_a5 import (figure_img, badge_row, video_box, exo, consigne, dots, pie, vop_grid,
                     fam_table_empty, wheel, fx, fx_row, numline,
                     objectifs, methode, astuce, attention, defi, bulle,
                     bar_model, bar_compare, number_bond, place_discs, obj_groups,
                     sg_box, draw_model, mult_area,
                     FR, MX, OVAL, OVS, SQ)


# ═══════════════════ الوحدة 1 : الأعداد الكبيرة (D2-D6) ═══════════════════
def u1_p1():
    body = f'''
{objectifs(['أقرأ الأعداد الكبيرة وأكتبها بالأرقام والحروف.',
            'أضع كل رقم في مكانه الصحيح في جدول المنازل.',
            'أقارن الأعداد الكبيرة وأرتّبها.'])}
{badge_row('أتعلّم', 'القاعدة والأمثلة', 'fille')}
<div class="frame has-video">
  <ul>
    <li>الأعداد الكبيرة تمتد من {MX('1 000')} (ألف) إلى {MX('1 000 000')} (مليون) وأكثر.</li>
    <li>نقرؤها بتجميع الأرقام <span class="hl">ثلاثة ثلاثة</span>.</li>
    <li>كل مجموعة تسمى <span class="hl">منزلة</span>: الوحدات، الآلاف، الملايين، المليارات.</li>
    <li>مثال: {MX('245 000')} = مئتان وخمسة وأربعون ألفًا.</li>
    <li>للعدد ثلاث <span class="hl">صيغ</span>: <b>القياسية</b> (بالأرقام) · <b>التفكيكية</b> (بالنشر والجمع) · <b>اللفظية</b> (بالحروف).</li>
  </ul>
  {video_box()}
</div>
{sg_box(place_discs([('1000', 2), ('100', 3), ('10', 4), ('1', 0)]),
        f'أعدّ الأقراص في كل منزلة وأكتب الرقم تحتها ← أقرأ العدد: {MX("2 340")}')}
{methode('كيف أقرأ عددًا كبيرًا؟', [
    'أجمع الأرقام <b>ثلاثة ثلاثة</b> انطلاقًا من اليمين.',
    'أقرأ كل منزلة وأتبعها باسمها: مليار، مليون، ألف.',
    'المنزلة الأخيرة (الوحدات) أقرؤها دون اسم.'])}
{astuce('قبل القراءة، ضع خطًا صغيرًا بعد كل 3 أرقام انطلاقًا من اليمين — هكذا لن تضيع بين المراتب أبدًا!')}'''
    return ('الأعداد الكبيرة: قراءتها وكتابتها', body, False)


def u1_p1b():
    fam_ex = f'''<table class="fam-table" style="direction:ltr">
      <tr>
        <th class="fam-g">المليارات</th><th class="fam-m">الملايين</th>
        <th class="fam-k">الآلاف</th><th class="fam-u">الوحدات</th>
      </tr>
      <tr class="sub">{('<th style="font-size:5.6px"><span style="display:flex;direction:ltr;justify-content:space-around"><span>مئات</span><span>عشرات</span><span>آحاد</span></span></th>') * 4}</tr>
      <tr>
        <td><span class="cellbox">&nbsp;</span><span class="cellbox">3</span><span class="cellbox">2</span></td>
        <td><span class="cellbox">0</span><span class="cellbox">4</span><span class="cellbox">7</span></td>
        <td><span class="cellbox">5</span><span class="cellbox">6</span><span class="cellbox">2</span></td>
        <td><span class="cellbox">0</span><span class="cellbox">7</span><span class="cellbox">3</span></td>
      </tr>
      <tr>
        <td><div class="pink-strip">32 مليارًا</div></td>
        <td><div class="pink-strip">47 مليونًا</div></td>
        <td><div class="pink-strip">562 ألفًا</div></td>
        <td><div class="pink-strip">73</div></td>
      </tr>
    </table>'''
    body = f'''
{badge_row('أتدرّب', 'مثال محلول', 'garcon')}
<div class="frame">
  {fam_ex}
  <div class="scallop">نقرأ: اثنان وثلاثون مليارًا وسبعة وأربعون مليونًا وخمسمائة واثنان وستون ألفًا وثلاثة وسبعون.</div>
  <div class="exemple"><b class="tag">💡 التفكيك باستعمال القوى:</b> {MX('32 047 562 073 = 32 × 1 000 000 000 + 47 × 1 000 000 + 562 × 1 000 + 73')}</div>
</div>
{attention(f'لا تنسَ الأصفار في وسط العدد! «ثلاثة ملايين وخمسة» تُكتب {MX("3 000 005")} وليس {MX("35")}.')}'''
    return ('الأعداد الكبيرة: مثال محلول', body, False)


def u1_p2():
    body = f'''
{badge_row('تمارين', 'قراءة الأعداد وكتابتها', 'garcon')}
<div class="exemple"><b class="tag">✏️ مثال محلول:</b> خمسة وعشرون ألفًا وثلاثمائة وسبعة ← أكتبه بالأرقام: {MX('25 307')} (لا أنسى صفر العشرات!).
{place_discs([('10000', 2), ('1000', 5), ('100', 3), ('10', 0), ('1', 7)], 'منزلة العشرات فارغة ← أكتب 0 تحتها، ولا أحذفها أبدًا!')}</div>
{exo(1, '⭐', f'''اكتب الأعداد بالأرقام:<br>
اثنان وأربعون ألفًا ومئة وثمانية عشر <span class="oval l"></span><br>
مئتا ألف وثمانية عشر <span class="oval l"></span><br>
ستة وثلاثون مليونًا وثمانمائة وخمسة <span class="oval l"></span><br>
ستمائة ألف وثلاثمائة واثنا عشر <span class="oval l"></span>''')}
{exo(2, '⭐⭐', f'اكتب هذه الأعداد بالحروف: {MX("543 608")} · {MX("375 194")} · {MX("42 118")}' + dots(2))}
{exo(3, '⭐⭐⭐', f'''اكتب مستعملًا كل هذه الأرقام: {MX('0، 1، 2، 3، 4، 5، 6')} (كل رقم مرة واحدة):<br>
أكبر عدد صحيح <span class="oval l"></span><br>
أكبر عدد رقمُ ملايينه 4 <span class="oval l"></span><br>
أصغر عدد رقمُ عشراته 5 <span class="oval l"></span>''')}'''
    return ('تمارين — قراءة الأعداد وكتابتها', body, False)


def _fam_exo(number):
    return f'''<div style="margin:1.6mm 0 2.6mm">
      <div style="text-align:center;font-weight:900;font-size:11px;margin-bottom:1mm">{MX(number)}</div>
      {fam_table_empty(4)}
    </div>'''


def u1_p3():
    body = f'''
{badge_row('تمارين', 'جدول المنازل', 'fille')}
{consigne(1, 'ضع كل رقم في الموضع الصحيح داخل الجدول، ثم اكتب قراءة العدد على السطر:')}
<div class="exemple"><b class="tag">✏️ مثال محلول:</b> {MX('4 208 617')}: أضع 4 في منزلة الملايين، و208 في منزلة الآلاف، و617 في منزلة الوحدات — أقرأ: أربعة ملايين ومئتان وثمانية آلاف وستمائة وسبعة عشر.</div>
{_fam_exo('6 521 004')}
{_fam_exo('7 634 598')}
{_fam_exo('2 345 709')}'''
    return ('تمارين — أضع الأعداد في جدول المنازل (1)', body, False)


def u1_p4():
    body = f'''
{badge_row('تمارين', 'جدول المنازل', 'garcon')}
{consigne(2, 'ضع كل رقم في الموضع الصحيح داخل الجدول، ثم اكتب قراءة العدد على السطر:')}
{_fam_exo('982 346')}
{_fam_exo('87 354 254')}
{_fam_exo('980 020')}'''
    return ('تمارين — أضع الأعداد في جدول المنازل (2)', body, False)


def u1_p5():
    comp_pairs = [('4 506 312', '4 560 312'), ('987 654', '1 023 000'),
                  ('12 500 000', '12 050 000'), ('305 214', '305 124')]
    comp = '<div class="cols nosep" style="margin-top:.6mm">' + ''.join(
        f'<div class="exo-q" style="text-align:center">{MX(a)} {SQ} {MX(b)}</div>' for a, b in comp_pairs) + '</div>'
    body = f'''
{badge_row('تمارين', 'المقارنة والترتيب', 'fille')}
{methode('كيف أقارن عددين كبيرين؟', [
    'أعدّ الأرقام: العدد الذي له أرقام أكثر هو الأكبر.',
    'إذا تساوى عدد الأرقام، أقارن رقمًا رقمًا انطلاقًا من اليسار.'])}
<div class="exemple"><b class="tag">✏️ مثال محلول:</b> {MX('7 302 145')} &lt; {MX('7 320 145')} — نفس عدد الأرقام، وعند المقارنة من اليسار أجد 0 أصغر من 2 في مرتبة عشرات الآلاف.</div>
{exo(4, '⭐', 'قارن باستعمال > أو < أو = :' + comp)}
{exo(5, '⭐⭐', f'رتّب الأعداد من الأصغر إلى الأكبر بوضعها على المستقيم العددي:<br>{MX("743 210")} · {MX("734 210")} · {MX("743 120")} · {MX("74 321")}'
     + numline(100, [.1, .37, .63, .9], {.1: '?', .37: '?', .63: '?', .9: '?'}, y=6))}
{exo(6, '⭐⭐⭐', f'''باع تاجر تمر في نواكشوط:<br>
السبت: {MX('124 500')} أوقية · الأحد: {MX('125 400')} أوقية · الجمعة: {MX('99 875')} أوقية.<br>
رتّب الأيام من الأقل مبيعًا إلى الأكثر مبيعًا:''' + dots(1))}
{defi(f'أنا عدد من 7 أرقام: منزلة ملاييني 5، ومنزلة آلافي 340، ومنزلة وحداتي 208. من أنا؟ اكتبني بالأرقام: {OVAL}')}'''
    return ('تمارين — أقارن الأعداد الكبيرة وأرتّبها', body, True)


# ═══════════════════ الوحدة 2 : الكسور (D7-D10) ═══════════════════
def u2_p1():
    pies_row = f'''<div class="pies">
      <div><div>{pie(180, 2)}</div><div class="pie-lab">{FR(1,2)} نصف</div></div>
      <div><div>{pie(120, 3)}</div><div class="pie-lab">{FR(1,3)} ثلث</div></div>
      <div><div>{pie(90, 4)}</div><div class="pie-lab">{FR(1,4)} ربع</div></div>
      <div><div>{pie(270, 4, '#f5b34c')}</div><div class="pie-lab">{FR(3,4)} ثلاثة أرباع</div></div>
      <div><div>{pie(360, 4, '#a9d3a0')}</div><div class="pie-lab">{FR(4,4)} = 1 كلٌّ كامل</div></div>
    </div>'''
    body = f'''
{objectifs(['أتعرّف البسط والمقام في الكسر.',
            'أمثّل الكسور بالرسم وعلى المستقيم العددي.',
            'أقارن الكسور باستعمال > و < و =.'])}
{badge_row('أتعلّم', 'القاعدة والأمثلة', 'fille')}
<div class="frame has-video">
  <ul>
    <li>الكسر = <span class="hl">جزء من كلٍّ كامل</span>. مثال: {FR(1,4)} = حصة واحدة من 4 حصص متساوية.</li>
    <li>كيف يُكتب الكسر؟ في الأعلى: <span class="hl">البسط</span> (الحصص المأخوذة).</li>
    <li>في الأسفل: <span class="hl">المقام</span> (عدد الحصص الكلية).</li>
  </ul>
  {video_box()}
</div>
{bulle('garcon', 'أنا <b>البسط</b> أسكن فوق الخط وأعدّ الحصص المأخوذة، وصديقي <b>المقام</b> يسكن تحته ويعدّ الحصص كلها!')}
{badge_row('أتدرّب', 'قراءة الكسر', 'garcon')}
<div class="frame">
  <div style="font-size:9.4px;font-weight:900;color:#8a4a12;margin-bottom:1mm">🍰 قراءة الكسر:</div>
  {pies_row}
</div>'''
    return ('الكسور', body, False)


def u2_p2():
    def pair(d1, n1, p1_, d2, n2, p2_, f1='#8fd4e8', f2='#f5b34c'):
        return f'''<div style="display:flex;align-items:center;gap:1.6mm;justify-content:center">
          <div style="text-align:center">{pie(360*n1/d1, d1, f1)}<div>{OVS}</div></div>
          <span class="sq"></span>
          <div style="text-align:center">{pie(360*n2/d2, d2, f2)}<div>{OVS}</div></div>
        </div>'''
    body = f'''
{badge_row('تمارين', 'مقارنة الكسور', 'garcon')}
{methode('أقارن كسرين لهما نفس المقام', [
    'أتأكد أولًا أن المقامين متساويان.',
    'أقارن البسطين: صاحب <b>البسط الأكبر</b> هو الكسر الأكبر.'])}
{methode('أقارن كسرين لهما نفس البسط', [
    'أتأكد أن البسطين متساويان.',
    'صاحب <b>المقام الأصغر</b> هو الكسر الأكبر (لأن الحصص أكبر).'])}
<div class="exemple"><b class="tag">✏️ مثال محلول:</b> {FR(5,7)} &gt; {FR(2,7)} لأن المقامين متساويان والبسط 5 أكبر من البسط 2.</div>
{consigne(1, 'اكتب كسر الجزء الملوّن في كل دائرة، ثم قارن باستعمال > أو < أو = :')}
<div class="cols nosep">
  {pair(4, 1, '', 4, 3, '')}
  {pair(3, 2, '', 3, 1, '')}
  {pair(6, 5, '', 6, 2, '')}
  {pair(8, 3, '', 8, 6, '')}
</div>
{consigne(2, 'استعمل < أو > أو = لمقارنة الكسور:')}
<div class="cols">
  <div class="exo-q" style="text-align:center">{FR(3,5)} {SQ} {FR(2,5)}<br><br>{FR(2,3)} {SQ} {FR(1,3)}</div>
  <div class="exo-q" style="text-align:center">{FR(1,6)} {SQ} {FR(4,6)}<br><br>{FR(3,8)} {SQ} {FR(3,6)}</div>
</div>
{attention(f'المقام الأكبر لا يعني كسرًا أكبر! {FR(1,8)} أصغر من {FR(1,2)} لأن تقسيم الكل إلى 8 حصص يعطي حصصًا أصغر.')}'''
    return ('تمارين — الكسور والمقارنة', body, False)


def u2_p3():
    nl1 = numline(56, [0, .25, .5, .75, 1], {0: '0', .25: '¼', .5: '?', .75: '¾', 1: '1'})
    nl2 = numline(56, [0, 1/3, 2/3, 1], {0: '0', 1/3: '⅓', 2/3: '?', 1: '1'})
    nl3 = numline(56, [0, .2, .4, .6, .8, 1], {0: '0', .2: '⅕', .4: '⅖', .6: '?', .8: '⅘', 1: '1'})
    nl4 = numline(56, [0, .125, .25, .375, .5, .625, .75, .875, 1], {0: '0', .125: '⅛', .375: '⅜', .5: '?', .625: '⅝', .875: '⅞', 1: '1'})
    strips = f'''<div style="display:grid;grid-template-columns:1fr 1fr;gap:1.4mm 4mm">
      <div><div class="fstrip"><div class="fcell fill-b"></div><div class="fcell"></div><div class="fcell fill-b"></div><div class="fcell"></div></div><div style="text-align:center">{OVS}</div></div>
      <div><div class="fstrip"><div class="fcell fill-o"></div><div class="fcell fill-o"></div><div class="fcell"></div></div><div style="text-align:center">{OVS}</div></div>
      <div><div class="fstrip"><div class="fcell fill-g"></div><div class="fcell"></div><div class="fcell"></div><div class="fcell"></div><div class="fcell fill-g"></div><div class="fcell"></div></div><div style="text-align:center">{OVS}</div></div>
      <div><div class="fstrip"><div class="fcell fill-v"></div><div class="fcell fill-v"></div><div class="fcell fill-v"></div><div class="fcell"></div><div class="fcell fill-v"></div></div><div style="text-align:center">{OVS}</div></div>
    </div>'''
    empty_strips = f'''<div style="display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:1.4mm 3mm">
      <div><div class="fstrip"><div class="fcell"></div><div class="fcell"></div></div><div class="pie-lab">{FR(1,2)}</div></div>
      <div><div class="fstrip"><div class="fcell"></div><div class="fcell"></div><div class="fcell"></div><div class="fcell"></div></div><div class="pie-lab">{FR(1,4)}</div></div>
      <div><div class="fstrip"><div class="fcell"></div><div class="fcell"></div><div class="fcell"></div><div class="fcell"></div></div><div class="pie-lab">{FR(2,4)}</div></div>
      <div><div class="fstrip"><div class="fcell"></div><div class="fcell"></div><div class="fcell"></div><div class="fcell"></div><div class="fcell"></div><div class="fcell"></div><div class="fcell"></div><div class="fcell"></div></div><div class="pie-lab">{FR(1,8)}</div></div>
    </div>'''
    body = f'''
{badge_row('تمارين', 'المستقيم العددي والتمثيل', 'fille')}
{consigne(1, 'أكمل الكسور الناقصة على كل مستقيم عددي:')}
<div style="display:grid;grid-template-columns:1fr 1fr;gap:0 4mm">{nl1}{nl2}{nl3}{nl4}</div>
{consigne(2, 'اكتب الكسر الذي يمثله كل جزء مظلّل من الشكل:')}
{strips}
{consigne(3, 'لوّن كل شكل لتمثيل الكسر المطلوب:')}
{empty_strips}
{consigne(4, 'أوجد المجموع لكل مسألة من مسائل الجمع التالية:')}
<div class="exo-q" style="text-align:center">
  {FR(1,4)} + {FR(2,4)} = {OVS} &nbsp;&nbsp;·&nbsp;&nbsp; {FR(1,8)} + {FR(3,8)} = {OVS} &nbsp;&nbsp;·&nbsp;&nbsp; {FR(1,2)} + {FR(1,2)} = {OVS}
</div>'''
    return ('تمارين — أمثّل الكسور وأجمعها', body, False)


def u2_p4():
    cards = []
    for i in range(1, 17):
        col = '#a9d3a0' if i <= 12 else ('#fcd77f' if i <= 14 else '#f5a09c')
        cards.append(f'<div style="width:8.4mm;height:11mm;border:1.3px solid #2b2b2b;border-radius:1.4mm;background:{col};display:flex;align-items:center;justify-content:center;font-weight:900;font-size:10px">{i}</div>')
    grid = f'<div style="display:flex;flex-wrap:wrap;gap:1.6mm;justify-content:center;direction:ltr;margin:1.4mm 0">{"".join(cards)}</div>'
    def row(lab, f, d, p):
        c = lambda v: f'<td style="font-weight:900">{v}</td>' if v else f'<td>{OVS}</td>'
        return f'<tr><th style="background:var(--p-yell);color:#7c4a12;font-size:8.4px">{lab}</th>{c(f)}{c(d)}{c(p)}</tr>'
    table = f'''<table class="fam-table" style="width:100%">
      <tr><th style="background:var(--p-rose);color:#8a3d2a">النتائج</th>
          <th style="background:var(--p-green);color:#33591f">بالكسر</th>
          <th style="background:var(--p-green);color:#33591f">بالعدد العشري</th>
          <th style="background:var(--p-green);color:#33591f">بالنسبة المئوية</th></tr>
      {row('بطاقة خضراء', '', '', '75 %')}
      {row('بطاقة صفراء', '', '', '12,5 %')}
      {row('بطاقة وردية', '', '', '')}
      {row('بطاقة لعدد أصغر أو يساوي 12', FR(12,16), '0,75', '')}
      {row('بطاقة لعدد زوجي', '', '0,5', '')}
    </table>'''
    body = f'''
{badge_row('تمارين', 'تحدّي 🌟 الكسر والعدد العشري والنسبة', 'garcon')}
{consigne(1, 'توقّع نتيجة سحب بطاقة عشوائية من مجموعة البطاقات أدناه:')}
{grid}
{consigne(2, 'أكمل مخطط الاحتمالات بملء القيم الناقصة:')}
{table}
{astuce(f'الكسر = {FR("عدد البطاقات الموافقة","عدد البطاقات كلها")} ← أحوّله إلى عدد عشري ثم إلى نسبة مئوية (× 100).')}
{defi(f'''في مقهى في نواكشوط، شرب الزبائن {FR(1,2)} إبريق الشاي صباحًا و{FR(1,4)} الإبريق مساءً. أي كسر من الإبريق بقي؟ {OVS}
<div class="fstrip" style="width:38mm;margin:1mm auto 0"><div class="fcell fill-b"></div><div class="fcell fill-b"></div><div class="fcell fill-o"></div><div class="fcell"></div></div>
<div style="display:flex;justify-content:center;align-items:center;gap:3.5mm;font-size:7.6px;font-weight:800;color:#5c5238;margin-top:.8mm">
<span style="display:inline-flex;align-items:center;gap:1.2mm"><span style="width:3mm;height:3mm;border-radius:.6mm;background:#8fd4e8;border:1px solid #7aa8b8"></span>صباحًا</span>
<span style="display:inline-flex;align-items:center;gap:1.2mm"><span style="width:3mm;height:3mm;border-radius:.6mm;background:#f5b34c;border:1px solid #c98f35"></span>مساءً</span>
<span style="display:inline-flex;align-items:center;gap:1.2mm"><span style="width:3mm;height:3mm;border-radius:.6mm;background:#fff;border:1px solid #9a9078"></span>بقي = ؟</span>
</div>''')}'''
    return ('تحدّي — من الكسر إلى النسبة المئوية', body, True)


# ═══════════════════ الوحدة 3 : الجمع والطرح (D11-D13) ═══════════════════
ADDS = [(203, 400), (5665, 3434), (1238, 5347), (9845, 9847), (5665, 9800), (1982, 4356),
        (2365, 4356), (9854, 9834), (3455, 9843), (982, 5366), (9821, 8712), (9842, 8765),
        (9834, 8732), (708, 4293), (9006, 9721), (2981, 873), (2334, 2314), (9810, 5672),
        (9000, 2000), (2000, 9876), (1009, 7659), (3507, 2486), (6218, 1794), (4067, 3858)]
SUBS = [(9821, 345), (4352, 983), (8732, 1238), (542, 33), (6529, 832), (4356, 1982),
        (1400, 203), (5665, 3434), (3214, 1238), (9847, 432), (800, 132), (6532, 1982),
        (8325, 203), (4253, 231), (5347, 2168), (1632, 845), (8790, 123), (2034, 812),
        (734, 100), (400, 213), (2307, 700), (980, 124), (908, 200), (4320, 1020)]


def u3_p1():
    body = f'''
{objectifs(['أضع عمليات الجمع والطرح عموديًا وأنجزها.',
            'لا أنسى الاحتفاظ في الجمع والاستلاف في الطرح.',
            'أحلّ مسائل من الحياة اليومية بالجمع والطرح.'])}
{badge_row('أتعلّم', 'القاعدة والأمثلة', 'fille')}
<div class="frame has-video">
  <ul>
    <li>الجمع (+) يعطي <span class="hl">المجموع</span>، والطرح (−) يعطي <span class="hl">الفرق</span>.</li>
    <li>سرّ النجاح: <span class="hl">محاذاة الأرقام</span> من نفس المرتبة.</li>
  </ul>
  {video_box()}
</div>
{methode('أضع وأنجز العملية', [
    'أكتب الأعداد بعضها تحت بعض: الآحاد تحت الآحاد، والعشرات تحت العشرات.',
    'أرسم خطًا تحت العدد الأخير.',
    'أحسب انطلاقًا من الآحاد ثم أنتقل نحو اليسار.'])}
{badge_row('أتدرّب', 'مثال محلول', 'garcon')}
<div class="frame">
  <div style="display:flex;gap:5mm;align-items:center;justify-content:center">
    <div class="vop" style="padding-bottom:1.4mm">1238<br><span class="sign">+</span>5347<span class="vline" style="height:auto;padding-top:.7mm">6585</span></div>
    <div class="vop" style="padding-bottom:1.4mm">5347<br><span class="sign">−</span>1238<span class="vline" style="height:auto;padding-top:.7mm">4109</span></div>
    {number_bond('6585', ['1238', '5347'], w=26)}
  </div>
  <div class="sg-note">عائلة أعداد واحدة: الجمع يبني الكلَّ، والطرح يفصل جزءًا منه.</div>
</div>
{attention('في الجمع لا تنسَ <b>الاحتفاظ</b> ⬆️ ، وفي الطرح لا تنسَ <b>الاستلاف</b> عندما يكون الرقم الأعلى أصغر من الرقم الأسفل.')}'''
    return ('الجمع (+) والطرح (−)', body, False)


def u3_p2():
    body = f'''
{badge_row('تمارين', 'الجمع العمودي', 'garcon')}
<div class="exemple"><b class="tag">✏️ مثال محلول:</b> {MX('1456 + 2338')}: أحاذي الآحاد تحت الآحاد وأجمع مع الاحتفاظ ← {MX('1456 + 2338 = 3794')}.</div>
{consigne(1, 'ضَع وأنجز عمليات الجمع التالية:')}
{vop_grid(ADDS[:16], '+', 4)}'''
    return ('تمارين — ضَع وأنجز: الجمع', body, False)


def u3_p3():
    body = f'''
{badge_row('تمارين', 'الطرح العمودي', 'fille')}
<div class="exemple"><b class="tag">✏️ مثال محلول:</b> {MX('7534 − 1263')}: أبدأ بالآحاد وأستلف عند الحاجة ← {MX('7534 − 1263 = 6271')}.</div>
{consigne(2, 'ضَع وأنجز عمليات الطرح التالية:')}
{vop_grid(SUBS[:16], '−', 4)}
{astuce(f'للتحقق من الطرح، أجمع الفرق مع المطروح: {MX("542 − 33 = 509")} صحيحة لأن {MX("509 + 33 = 542")}.')}'''
    return ('تمارين — ضَع وأنجز: الطرح', body, False)


def u3_p4():
    body = f'''
{badge_row('تمارين', 'جمع وطرح', 'garcon')}
<div class="exemple"><b class="tag">✏️ مثال محلول:</b> {MX('2412 + 2331 = 4743')} · وللطرح: {MX('856 − 124 = 732')}.</div>
{consigne(3, 'ضَع وأنجز عمليات الجمع التالية:')}
{vop_grid(ADDS[16:24], '+', 4)}
{consigne(4, 'ضَع وأنجز عمليات الطرح التالية:')}
{vop_grid(SUBS[16:24], '−', 4)}'''
    return ('تمارين — أُتقن الجمع والطرح', body, False)


def u3_p5():
    body = f'''
{badge_row('تمارين', 'مسائل من الحياة اليومية', 'fille')}
<div class="exemple"><b class="tag">✏️ مثال محلول:</b> عند سيدي محمد {MX('320')} تمرة، اشترى {MX('150')} تمرة أخرى: {MX('320 + 150 = 470')} تمرة.
{bar_model('الكل = 470 تمرة', [('عنده', 320, '#8fd4e8'), ('اشترى', 150, '#f5b34c')], w=64, stagger=False, scale=.72)}</div>
{exo(5, '⭐', f'''📚 في مكتبة مدرسة بروصو {MX('1 250')} كتابًا. وصلتها {MX('375')} كتابًا جديدًا.<br>
<b>كم كتابًا صار في المكتبة؟</b> النموذج جاهز — احسب!
{bar_model('؟', [('في المكتبة', 1250, '#aae4f0'), ('وصلها', 375, '#ffd98c')], w=72, stagger=False, scale=.72)}''')}
{exo(6, '⭐⭐', f'''🛒 اشترت فاطمة من السوق تمرًا بـ {MX('2 450')} أوقية وسكّرًا بـ {MX('1 780')} أوقية.<br>
<b>كم دفعت للبائع؟</b>{draw_model(9.5)}''')}
{exo(7, '⭐⭐⭐', f'''🫖 دفع أحمد ورقتين من فئة {MX('1 000')} أوقية ثمن علبة شاي بـ {MX('450')} أوقية وعلبة حليب بـ {MX('975')} أوقية.<br>
<b>كم يُرجع له البائع؟</b> أكمل النموذج ثم احسب:
{bar_model('دفع 2000 أوقية', [('شاي', 450, '#c6e9a4'), ('حليب', 975, '#ffc7ba'), ('يُرجع له', 575, '#fff', '؟')], w=76, stagger=False, scale=.72)}''')}
{defi(f'باستعمال الأرقام 2، 5، 7، 8 (كل رقم مرة واحدة) كوّن عددين من رقمين مجموعهما أكبر ما يمكن. ما هو المجموع؟ {OVAL}')}'''
    return ('تمارين — مسائل الجمع والطرح', body, True)


# ═══════════════════ الوحدة 4 : الضرب (D14-D17) ═══════════════════
WHEELS = [('2x', [12, 0, 6, 2, 1, 7, 11, 8]), ('3x', [4, 7, 8, 0, 1, 6, 12, 5]),
          ('7x', [12, 5, 4, 8, 10, 3, 9, 11]), ('6x', [6, 4, 2, 1, 10, 3, 11, 5]),
          ('1x', [12, 7, 11, 2, 4, 6, 9, 8]), ('8x', [10, 2, 5, 0, 3, 1, 6, 4]),
          ('4x', [10, 2, 7, 3, 11, 6, 12, 9]), ('11x', [3, 7, 12, 5, 9, 2, 10, 6]),
          ('9x', [9, 4, 1, 2, 11, 6, 3, 8])]
MULTS = [(23, 2), (40, 2), (8, 2), (34, 2), (200, 1), (90, 2), (500, 2), (20, 1),
         (9821, 2), (4352, 4), (6529, 7), (4356, 6), (879, 8), (543, 8),
         (213, 9), (876, 3), (987, 3), (87, 9), (67, 4), (309, 5),
         (53, 7), (190, 3), (234, 3), (542, 0)]


def u4_p1():
    body = f'''
{objectifs(['أفهم الضرب على أنه جمع متكرر.',
            'أحفظ جداول الضرب حتى 12.',
            'أضع الضرب عموديًا وأنجزه دون خطأ.'])}
{badge_row('أتعلّم', 'القاعدة والأمثلة', 'fille')}
<div class="frame has-video">
  <ul>
    <li>الضرب يُستعمل <span class="hl">لجمع نفس العدد عدة مرات</span>.</li>
    <li>يُكتب بعاملين ويعطي <span class="hl">جداءً</span>.</li>
    <li>يمكن تغيير ترتيب العددين: {MX('4 × 3 = 3 × 4')}.</li>
    <li>يجب <span class="hl">حفظ جداول الضرب</span> عن ظهر قلب.</li>
  </ul>
  {video_box()}
</div>
{astuce('في جدول 9، مجموع رقمي النتيجة يساوي دائمًا 9: <span class="mexp">18</span>، <span class="mexp">27</span>، <span class="mexp">36</span>، <span class="mexp">45</span>… جرّب بنفسك!')}
{badge_row('أتدرّب', 'من الجمع المتكرر إلى الضرب', 'garcon')}
<div class="frame">
  {obj_groups(4, 3, '🐚')}
  <div class="sg-note">4 مجموعات من 3 أصداف: {MX('3 + 3 + 3 + 3')} = {MX('4 × 3')} = 12</div>
  <div class="exo-q" style="text-align:center;margin-top:1.4mm">
    {MX('3 + 3 + 3 + 3')} = {MX('3 ×')} {SQ} = {SQ}<br>
    {MX('5 + 5 + 5')} = {SQ} {MX('× 5')} = {SQ}<br>
    {MX('7 + 7')} = {SQ} × {SQ} = {SQ}
  </div>
</div>'''
    return ('الضرب (×)', body, False)


def u4_p2():
    tables = []
    for n in range(1, 13):
        rows = ''.join(f'<div style="display:flex;justify-content:space-between;border-bottom:1px dotted #e0d5b8;padding:.25mm 0"><span>{i} × {n} =</span><span style="display:inline-block;width:5.5mm;border-bottom:1.3px solid #b9a06a"></span></div>' for i in range(1, 11))
        tables.append(f'''<div style="background:#fff;border:1.2px solid #ddd2b8;border-radius:2mm;padding:1.2mm 1.8mm;font-size:6.9px;font-weight:800">
          <div style="text-align:center;font-size:7.5px;font-weight:900;color:#c9711a;border-bottom:1.2px solid #f0e3c4;margin-bottom:.5mm">جدول {n}</div>{rows}</div>''')
    body = f'''
{badge_row('تمارين', 'جداول الضرب من 1 إلى 12', 'garcon')}
{consigne(1, 'أكمل جداول الضرب:')}
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:1.6mm">{''.join(tables)}</div>'''
    return ('تمارين — أحفظ جداول الضرب', body, False)


def u4_p3():
    cells = ''.join(f'<div style="text-align:center">{wheel(c, nums)}</div>' for c, nums in WHEELS)
    body = f'''
{badge_row('تمارين', 'عجلات الضرب', 'fille')}
{consigne(2, 'حُلّ كل عجلة ضرب باستعمال تقنيات الحساب الذهني — اكتب الجواب في الأنشوطة الخارجية:')}
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:1mm 2mm;justify-items:center">{cells}</div>'''
    return ('تمارين — عجلات الضرب 🎡', body, False)


def u4_p4():
    ops = ['8 × 1', '8 × 2', '8 × 5', '8 × 4', '8 × 8', '8 × 9', '8 × 11', '8 × 12']
    res = [8, 16, 18, 24, 30, 31, 32, 40, 45, 48, 50, 56, 64, 68, 72, 76, 81, 86, 88, 89, 96, 118]
    op_chips = ''.join(f'<span style="display:inline-block;background:#fff;border:1.4px solid #d78d33;border-radius:2mm;padding:1mm 2.6mm;margin:.7mm;font-weight:900;font-size:9.5px">{MX(o)} =</span>' for o in ops)
    res_chips = ''.join(f'<span style="display:inline-flex;align-items:center;justify-content:center;width:8.6mm;height:8.6mm;background:#fff;border:1.4px solid #2b2b2b;border-radius:50%;margin:.6mm;font-weight:900;font-size:8.8px">{r}</span>' for r in res)
    checks = [('3 × 1', 3), ('5 × 2', 10), ('5 × 5', 25), ('7 × 7', 48), ('0 × 11', 0), ('8 × 1', 8),
              ('12 × 3', 35), ('12 × 2', 24), ('9 × 2', 18), ('9 × 9', 81), ('9 × 8', 74), ('10 × 6', 60),
              ('3 × 9', 27), ('3 × 11', 36), ('11 × 9', 99), ('5 × 9', 44), ('2 × 1', 2), ('6 × 9', 56)]
    check_cells = ''.join(f'<div style="background:#fff;border:1.2px solid #ddd2b8;border-radius:2mm;padding:1.1mm;text-align:center;font-weight:900;font-size:9px">{MX(o)}<div style="color:#2f6ea5;font-size:10.5px">{r}</div></div>' for o, r in checks)
    body = f'''
{badge_row('تمارين', 'ألعاب الضرب', 'garcon')}
{consigne(3, 'لوّن عملية الضرب مع نتيجتها المناسبة. استعمل لونًا مختلفًا لكل عملية:')}
<div style="text-align:center">{op_chips}</div>
<div style="text-align:center;direction:ltr;background:#fdf6e4;border:1.4px dashed #e0b25f;border-radius:3mm;padding:1.4mm;margin-top:1mm">{res_chips}</div>
{consigne(4, 'ضع دائرة حول الأجوبة الصحيحة واشطب الخاطئة:')}
<div style="display:grid;grid-template-columns:repeat(6,1fr);gap:1.4mm">{check_cells}</div>'''
    return ('تمارين — أُلوّن وأتحقق 🎨', body, False)


def u4_p4b():
    body = f'''
{badge_row('أتعلّم', 'الضرب العمودي', 'fille')}
{methode('أضع وأنجز الضرب العمودي', [
    'أكتب العدد الكبير في الأعلى والعدد الصغير تحته، مع المحاذاة.',
    'أضرب رقم الآحاد في أرقام العدد الأعلى، من اليمين إلى اليسار.',
    'أضيف الاحتفاظ إلى نتيجة الضرب الموالية.'])}
{attention(f'كثيرون ينسون <b>الاحتفاظ</b> في الضرب! {MX("7 × 8 = 56")}: أكتب 6 وأحتفظ بـ 5 أضيفها إلى الجداء الموالي.')}
{sg_box(mult_area(70, 6, 4), f'لماذا تنجح الطريقة؟ أفكّك {MX("76")} إلى 70 و6، أضرب كل جزء، ثم أجمع.')}
{consigne(5, 'ضَع وأنجز عمليات الضرب التالية:')}
{vop_grid(MULTS[:8], '×', 4)}'''
    return ('الضرب العمودي — الطريقة', body, False)


def u4_p5():
    body = f'''
{badge_row('تمارين', 'الضرب العمودي', 'fille')}
<div class="exemple"><b class="tag">✏️ مثال محلول:</b> {MX('76 × 4')}: {MX('4 × 6 = 24')} أكتب 4 وأحتفظ بـ 2، ثم {MX('4 × 7 = 28')} زائد 2 يعطي 30 ← {MX('76 × 4 = 304')}.</div>
{consigne(6, 'ضَع وأنجز عمليات الضرب التالية:')}
{vop_grid(MULTS[8:], '×', 4)}
{defi(f'صندوق تمر فيه 12 صفًا، في كل صف 8 تمرات. اشترت خديجة صندوقين من سوق نواكشوط: كم تمرة عندها؟ {OVAL}')}'''
    return ('تمارين — ضَع وأنجز: الضرب', body, True)


# ═══════════════════ الوحدة 5 : القسمة (D18-D20) ═══════════════════
def u5_p1():
    body = f'''
{objectifs(['أفهم القسمة على أنها توزيع بالتساوي.',
            'أستعمل جداول الضرب لأجد خارج القسمة.',
            'أحسب القسمة مع الباقي.'])}
{badge_row('أتعلّم', 'القاعدة والأمثلة', 'fille')}
<div class="frame has-video">
  <ul>
    <li>القسمة تُستعمل <span class="hl">للتوزيع إلى حصص متساوية</span>.</li>
    <li>تُكتب بمقسوم ومقسوم عليه وتعطي <span class="hl">خارج القسمة</span>.</li>
    <li>أحيانًا يتبقى <span class="hl">باقٍ</span> إذا لم تكن القسمة تامة.</li>
  </ul>
  {video_box()}
</div>
{methode('كيف أجد خارج القسمة؟', [
    'أطرح السؤال: في أي جدول ضرب أجد المقسوم؟',
    'أبحث: المقسوم عليه × ؟ = المقسوم.',
    f'مثال: {MX("12 ÷ 3")} ← أفكّر {MX("3 × 4 = 12")}، إذن الخارج هو 4.'])}
{badge_row('أتدرّب', 'أوزّع بالتساوي', 'garcon')}
<div class="frame">
  <div class="exo-q" style="text-align:center">🌰 وزّع 12 تمرة على 3 أطباق بالتساوي — صِل كل تمرة بطبقها بسهم:</div>
  <div style="text-align:center;font-size:10.5px;letter-spacing:1.2mm;margin-top:.8mm">🌰🌰🌰🌰🌰🌰🌰🌰🌰🌰🌰🌰</div>
  <div style="display:flex;gap:4mm;justify-content:center;margin-top:2.6mm">
    <div style="width:22mm;height:14mm;border:1.6px solid #d78d33;border-radius:50%/60%;background:#fff"></div>
    <div style="width:22mm;height:14mm;border:1.6px solid #d78d33;border-radius:50%/60%;background:#fff"></div>
    <div style="width:22mm;height:14mm;border:1.6px solid #d78d33;border-radius:50%/60%;background:#fff"></div>
  </div>
  <div class="exo-q" style="text-align:center;margin-top:1.4mm"><span style="direction:ltr;unicode-bidi:isolate">{MX('12 ÷ 3')} = {SQ}</span> تمرات في كل طبق</div>
</div>'''
    return ('القسمة (÷)', body, False)


def u5_p2():
    items1 = [f'{MX("9 ÷ 1")} = {SQ}', f'{MX("12 ÷ 2")} = {SQ}', f'{MX("8 ÷")} {SQ} = {MX("2")}',
              f'{MX("18 ÷ 2")} = {SQ}', f'{SQ} {MX("÷ 3 = 7")}', f'{MX("20 ÷")} {SQ} = {MX("4")}',
              f'{SQ} {MX("× 4 = 20")}', f'{MX("9 ÷ 3")} = {SQ}', f'{MX("22 ÷ 2")} = {SQ}',
              f'{MX("11 ×")} {SQ} = {MX("22")}', f'{MX("30 ÷ 6")} = {SQ}', f'{SQ} {MX("× 6 = 30")}',
              f'{MX("10 ÷")} {SQ} = {MX("2")}', f'{SQ} {MX("× 2 = 10")}', f'{SQ} {MX("÷ 5 = 3")}',
              f'{SQ} {MX("÷ 9 = 4")}']
    items2 = [f'{SQ} {MX("× 1 = 9")}', f'{SQ} {MX("× 6 = 12")}', f'{SQ} {MX("× 2 = 8")}',
              f'{MX("7 × 3")} = {SQ}', f'{SQ} {MX("× 3 = 9")}', f'{MX("9 × 2")} = {SQ}',
              f'{MX("5 × 3")} = {SQ}', f'{MX("9 × 4")} = {SQ}']
    g = lambda items, c: f'<div style="display:grid;grid-template-columns:repeat({c},1fr);gap:1.6mm">' + ''.join(
        f'<div style="background:#fff;border:1.2px solid #ddd2b8;border-radius:2mm;padding:1.4mm 1mm;text-align:center;font-weight:800;font-size:9px">{it}</div>' for it in items) + '</div>'
    body = f'''
{badge_row('تمارين', 'أكمل الخانات', 'garcon')}
<div class="exemple"><b class="tag">✏️ مثال محلول:</b> {MX('15 ÷ 3')} = 5، لأنني أبحث في جدول 3: {MX('3 × 5 = 15')}.
{obj_groups(3, 5, '🐟')}</div>
{consigne(1, 'اكتب في كل خانة الأعداد التي تُكمل المسائل الرياضية:')}
{g(items1, 4)}
{consigne(2, 'أكمل عمليات الضرب:')}
{g(items2, 4)}
{astuce('كل عدد مقسوم على 1 يبقى كما هو، وكل عدد مقسوم على نفسه يساوي 1.')}
{attention(f'الترتيب مهم في القسمة! {MX("12 ÷ 2")} تعني توزيع 12 على 2، وهي لا تساوي {MX("2 ÷ 12")}.')}'''
    return ('تمارين — القسمة والضرب: أكمل الخانات', body, False)


def u5_p2b():
    rem_items = ['13 ÷ 4', '17 ÷ 5', '22 ÷ 3', '29 ÷ 4', '35 ÷ 6', '50 ÷ 7', '43 ÷ 8', '61 ÷ 9']
    cards = '<div style="display:grid;grid-template-columns:1fr 1fr;gap:1.6mm">' + ''.join(
        f'<div style="background:#fff;border:1.2px solid #ddd2b8;border-radius:2mm;padding:1.6mm 1mm;text-align:center;font-weight:800;font-size:9px">{MX(op)} = {SQ} والباقي {SQ}</div>'
        for op in rem_items) + '</div>'
    body = f'''
{badge_row('تمارين', 'القسمة مع الباقي', 'garcon')}
{figure_img(FIGS['fermier'], 24, 'أوزّع المحصول إلى حصص متساوية — هذه هي القسمة!')}
<div class="exemple"><b class="tag">✏️ مثال:</b> {MX('14 ÷ 3')} = 4 والباقي 2، لأن {MX('3 × 4 = 12')} و {MX('12 + 2 = 14')}.
{bar_model('الكل = 14', [('3', 3, '#c6e9a4'), ('3', 3, '#c6e9a4'), ('3', 3, '#c6e9a4'), ('3', 3, '#c6e9a4'), ('الباقي', 2, '#f5a09c')], w=64, stagger=False, scale=.75)}</div>
{consigne(3, 'أنجز كل قسمة واكتب الخارج والباقي:')}
{cards}
{exo(4, '⭐⭐⭐', f'''🥖 عند الخبّازة زينب في دكان الحي 26 رغيفًا توزعها في أكياس، في كل كيس 4 أرغفة.<br>
<b>كم كيسًا تملأ؟ وكم رغيفًا يبقى؟</b>{draw_model(12, 'أرسم شريط الـ 26 وأقسمه شرائح من 4 — لا أنسى الباقي:')}''')}'''
    return ('تمارين — القسمة مع الباقي', body, False)


def u5_p3():
    body = f'''
{badge_row('تمارين', 'مسائل القسمة', 'fille')}
<div class="exemple"><b class="tag">✏️ مثال محلول:</b> عند مريم 20 تمرة تضعها في أطباق، في كل طبق 5 تمرات: {MX('20 ÷ 5 = 4')} أطباق.
{bar_model('الكل = 20 تمرة', [('5', 5, '#ffd98c'), ('5', 5, '#ffd98c'), ('5', 5, '#ffd98c'), ('5', 5, '#ffd98c')], w=52, stagger=False)}
<div class="sg-note">كم شريحة من 5 في 20؟ أعدّ الشرائح: 4 أطباق!</div></div>
{exo(1, '⭐⭐', f'''🫖 حضّر المختار 24 كأسًا من أتاي لضيوفه في أطار.<br>يريد وضعها في صوانٍ تتسع كل منها لـ 6 كؤوس.<br>
<b>كم صينية يمكنه أن يملأ؟</b>{draw_model(13, 'أرسم شريط الـ 24 وأقسمه شرائح من 6:')}''' + dots(1))}
{exo(2, '⭐⭐', f'''🐟 اصطاد صياد في نواذيبو 128 سمكة.<br>يريد ترتيبها في صناديق يتسع كل منها لـ 8 أسماك.<br>
<b>كم صندوقًا يمكنه أن يملأ؟</b>{draw_model(13)}''' + dots(2))}
{defi(f'عند جدّتك 50 تمرة توزعها على 8 أحفاد بالتساوي. كم تمرة لكل حفيد؟ {OVS} وكم تمرة تبقى لجدّتك؟ {OVS} 😋')}'''
    return ('تمارين — مسائل القسمة', body, True)


UNITS_1 = [
    dict(num=1, title='الأعداد الكبيرة', sub='قراءتها وكتابتها · جدول المنازل · المقارنة والترتيب', color='var(--p-yell)',
         pages=[u1_p1(), u1_p1b(), u1_p2(), u1_p3(), u1_p4(), u1_p5()]),
    dict(num=2, title='الكسور', sub='البسط والمقام · التمثيل والمقارنة', color='var(--p-rose)',
         pages=[u2_p1(), u2_p2(), u2_p3(), u2_p4()]),
    dict(num=3, title='الجمع والطرح', sub='العمليات العمودية بالاحتفاظ والاستلاف', color='var(--p-green)',
         pages=[u3_p1(), u3_p2(), u3_p3(), u3_p4(), u3_p5()]),
    dict(num=4, title='الضرب', sub='الجداول · عجلات الضرب · الضرب العمودي', color='var(--p-blue)',
         pages=[u4_p1(), u4_p2(), u4_p3(), u4_p4(), u4_p4b(), u4_p5()]),
    dict(num=5, title='القسمة', sub='التوزيع بالتساوي · القسمة مع الباقي · مسائل', color='var(--p-lila)',
         pages=[u5_p1(), u5_p2(), u5_p2b(), u5_p3()]),
]
