# -*- coding: utf-8 -*-
"""Partie SCIENCES (العلوم الطبيعية) — unités 1-3 : التوازن الغذائي · التوازن الطاقوي · التصحر.
Contenu repris fidèlement des diapositives 2 à 16 du pptx sciences,
avec ancrage mauritanien (prénoms locaux, aliments locaux, زحف الرمال…)."""
import math
from base_a5 import (badge_row, video_box, exo, consigne, dots,
                     MX, OVAL, OVS, SQ,
                     objectifs, methode, astuce, attention, defi, bulle, formula,
                     balance_svg, flow_chips, figure_img)
from figs_sciences import FIGS_SCI


# ─────────────────────────── helpers sciences ───────────────────────────
def _plate():
    """Assiette équilibrée : disque en 4 secteurs (نشويات، خضروات وفواكه، بروتينات وألبان، سكريات قليلة)."""
    def pt(deg):
        a = math.radians(deg - 90)
        return f'{20 + 17.5 * math.cos(a):.1f},{20 + 17.5 * math.sin(a):.1f}'
    sect = lambda a0, a1, col: (f'<path d="M20,20 L{pt(a0)} A17.5,17.5 0 {1 if a1 - a0 > 180 else 0} 1 {pt(a1)} Z" '
                                f'fill="{col}" stroke="#8a7a5c" stroke-width=".5"/>')
    svg = f'''<svg width="23mm" height="23mm" viewBox="0 0 40 40" style="overflow:visible;flex-shrink:0">
      <circle cx="20" cy="20" r="19" fill="#fff" stroke="#8a7a5c" stroke-width=".9"/>
      {sect(0, 140, '#ffd98c')}{sect(140, 260, '#c6e9a4')}{sect(260, 330, '#ffc7ba')}{sect(330, 360, '#e6c7f2')}
    </svg>'''
    leg = lambda col, txt: (f'<div style="display:flex;align-items:center;gap:1.4mm;font-size:8.2px;font-weight:800">'
                            f'<span style="width:3.4mm;height:3.4mm;border-radius:1mm;background:{col};'
                            f'border:1px solid rgba(0,0,0,.25);flex-shrink:0"></span><span>{txt}</span></div>')
    return f'''<div style="display:flex;gap:3.5mm;align-items:center;justify-content:center;margin:.6mm 0">
      {svg}
      <div style="display:flex;flex-direction:column;gap:.7mm">
        {leg('#ffd98c', '🍚 النشويات — الطاقة')}
        {leg('#c6e9a4', '🥕 الخضروات والفواكه — الحماية')}
        {leg('#ffc7ba', '🐟 البروتينات والألبان — النمو')}
        {leg('#e6c7f2', '🍬 قليل جدًا من السكر والدهون')}
      </div>
    </div>'''
def choix(*opts):
    """Choix de QCM, chaque option précédée d'une case à cocher."""
    return '<br>'.join(f'{SQ} {o}' for o in opts)


def vf_lines(items):
    """Lignes vrai/faux : deux cases صح / خطأ par affirmation."""
    return '<br>'.join(
        f'{t} &nbsp;<b style="color:#33591f">صح</b>{SQ}<b style="color:#b03434">خطأ</b>{SQ}'
        for t in items)


def relie(right_items, left_items):
    """Exercice de liaison : colonne droite (éléments) ↔ colonne gauche (réponses mélangées)."""
    r = ''.join(f'<div style="background:#fff;border:1.2px solid #ddd2b8;border-radius:2mm;padding:1.2mm 2mm;font-weight:800;font-size:8.6px;text-align:center;margin-bottom:1.2mm">{x} ●</div>' for x in right_items)
    l = ''.join(f'<div style="background:#fdf1d7;border:1.2px solid #e6cc93;border-radius:2mm;padding:1.2mm 2mm;font-weight:800;font-size:8.6px;text-align:center;margin-bottom:1.2mm">● {x}</div>' for x in left_items)
    return f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:1mm 12mm;align-items:start;margin-top:1mm"><div>{r}</div><div>{l}</div></div>'


# ═══════════════ الوحدة 1 : التوازن الغذائي (D2-D7) ═══════════════
def s1_p1():
    body = f'''
{objectifs(['أذكر المجموعات الغذائية الست وأمثلة عليها',
            'أفهم دور كل مجموعة: الطاقة والنمو وحماية الجسم',
            'أركّب وجبة متوازنة وأتناول ثلاث وجبات يومياً'])}
{badge_row('أتعلّم', 'التوازن الغذائي وأهميته', 'fille')}
<div class="frame has-video">
  <ul>
    <li>التوازن الغذائي هو تناول <span class="hl">أطعمة متنوعة بكميات مناسبة</span> للحفاظ على الصحة.</li>
    <li>تُقسم الأطعمة إلى مجموعات: <span class="hl">الفواكه والخضروات</span> · <span class="hl">النشويات</span> · <span class="hl">منتجات الألبان</span> · <span class="hl">اللحوم والأسماك والبيض</span> · <span class="hl">الدهون</span> · <span class="hl">المنتجات السكرية</span>.</li>
    <li>لكل مجموعة دور فعال: <span class="hl">الطاقة</span> و<span class="hl">النمو</span> و<span class="hl">حماية الجسم</span>.</li>
    <li>من الضروري تناول ثلاث وجبات يومياً: <span class="hl">الإفطار</span> و<span class="hl">الغداء</span> و<span class="hl">العشاء</span>، مع شرب <span class="hl">الماء</span> الكافي.</li>
  </ul>
  {video_box()}
</div>
<div class="frame" style="background:#f2fbf4;border-color:#9ed3ab">
  <div style="text-align:center;font-weight:900;font-size:9.6px;color:#2f6e46">🍽️ صحني المتوازن</div>
  <div style="display:flex;gap:4mm;align-items:center;justify-content:center">
    {_plate()}
    {figure_img(FIGS_SCI['repas_equilibre'], 21, 'وجبة متوازنة من مائدتنا')}
  </div>
</div>
{methode('كيف أعرف أن وجبتي متوازنة؟', ['أتأكد أن فيها نشويات (أرز، خبز، كسكس)',
                                          'أضيف خضروات أو فواكه وبروتينات أو ألبان',
                                          'أقلّل السكر والدهون وأشرب الماء'])}
{astuce('من مائدتنا الموريتانية: <b>الأرز بالسمك</b> يجمع النشويات والبروتينات — أضف الخضروات وكوب حليب فتكتمل وجبتك!')}'''
    return ('التوازن الغذائي', body, False)


def s1_p2():
    classify = '''<table class="fam-table" style="width:100%;margin-top:1mm">
  <tr><th style="background:var(--p-yell);color:#7c4a12;width:34%">نشويات</th>
      <th style="background:var(--p-green);color:#33591f;width:33%">بروتينات وألبان</th>
      <th style="background:var(--p-rose);color:#8a3d2a">دهون / سكريات</th></tr>
  <tr><td style="height:6mm"></td><td></td><td></td></tr>
  <tr><td style="height:6mm"></td><td></td><td></td></tr>
</table>'''
    body = f'''
{badge_row('تمارين', 'المجموعات الغذائية', 'garcon')}
<div style="display:flex;gap:3mm;align-items:center">
  <div class="exemple" style="flex:1"><b class="tag">✏️ مثال محلول:</b> السكريات تستخدم لـ: النمو {SQ} · <b>إعطاء الطاقة</b> <span class="sq">✓</span> · النوم {SQ}</div>
  {figure_img(FIGS_SCI['groupes_aliments'], 14, '')}
</div>
{exo(1, '⭐', 'اختر الإجابة الصحيحة — لماذا من المهم الحصول على تغذية متوازنة؟<br>'
      + choix('أ) للنمو الجيد والحفاظ على الصحة',
              'ب) لأكل كل ما نريد بدون حدود',
              'ج) لأن الأغذية لا تؤثر على الصحة'))}
{exo(2, '⭐', f'من بين هذه الأغذية، أيها ينتمي إلى مجموعة منتجات الألبان؟<br>{SQ} أ) السمك &nbsp;·&nbsp; {SQ} ب) اللبن الرائب (الزبادي) &nbsp;·&nbsp; {SQ} ج) الخبز')}
{exo(3, '⭐', 'ما هو المشروب الأكثر موصى به للترطيب؟<br>'
      + choix('أ) عصير الفواكه', 'ب) المشروبات الغازية', 'ج) الماء'))}
{exo(4, '⭐⭐', 'صنّف الأغذية التالية في الجدول: <b>أرز · بيض · زيت نباتي · سمك</b>' + classify)}
{exo(5, '⭐⭐', 'ما هو الغذاء الرئيسي في مجموعة النشويات عندنا في موريتانيا؟' + dots(1))}'''
    return ('تمارين — المجموعات الغذائية', body, False)


def s1_p3():
    vf = vf_lines(['الأكل المتوازن يعني تناول الخضروات فقط.',
                   'البروتينات تساعد على بناء العضلات.',
                   'السكر غذاء لا غنى عنه للصحة.',
                   'شرب الماء مهم للبقاء بصحة جيدة.',
                   'النشويات كالخبز والأرز مهمة في التغذية.',
                   'يجب تناول 5 فواكه وخضروات على الأقل يومياً.'])
    body = f'''
{badge_row('تمارين', 'أتحقّق من معلوماتي', 'fille')}
<div class="exemple"><b class="tag">✏️ مثال محلول:</b> الخضروات وحدها تكفي الجسم. <b style="color:#33591f">صح</b>{SQ}<b style="color:#b03434">خطأ</b><span class="sq">✓</span> — لأن الجسم يحتاج كل المجموعات الغذائية.</div>
{exo(6, '⭐', 'ضع علامة ✓ أمام صح أو خطأ:<br>' + vf)}
{exo(7, '⭐⭐', f'''أكمل الجمل:<br>
الأغذية التي تمنح الطاقة لجسمنا هي {OVAL}.<br>
للحصول على عظام قوية، من المهم تناول {OVAL}.<br>
الماء ضروري لجسمنا لأنه يسمح بـ {OVAL}.<br>
يجب تقليل الأغذية الكثيرة {OVS} والكثيرة {OVS}.''')}
{exo(8, '⭐⭐', 'اربط كل غذاء بمجموعته الغذائية (ارسم خطاً):'
      + relie(['تفاحة', 'حليب', 'دجاج', 'معكرونة'],
              ['منتجات الألبان', 'النشويات', 'الفواكه والخضروات', 'اللحوم والأسماك']))}'''
    return ('تمارين — صح أم خطأ؟', body, False)


def s1_p4():
    foods = [('🍚 كوب أرز', '200'), ('🍗 قطعة دجاج', '250'), ('🍎 تفاحة', '80'),
             ('🥛 كوب حليب', '150'), ('🍕 قطعة بيتزا', '300'), ('🍟 بطاطا مقلية', '400'),
             ('🍫 لوح شوكولاتة (100 غ)', '500')]
    head = ''.join(f'<th style="background:var(--p-yell);color:#7c4a12">{n}</th>' for n, _ in foods)
    row = ''.join(f'<td style="font-weight:800">{MX(v + " kcal")}</td>' for _, v in foods)
    cal = f'<table class="fam-table" style="width:100%"><tr>{head}</tr><tr>{row}</tr></table>'
    body = f'''
{badge_row('مسائل', 'وضعيات غذائية', 'garcon')}
{bulle('fille', f'يجب أن يستهلك طفل في السنة السادسة حوالي {MX('2 000 kcal')} يومياً. إليك الطاقة التي توفرها بعض الأغذية:')}
{cal}
<div class="exemple"><b class="tag">✏️ مثال محلول:</b> تفاحة + كوب حليب = {MX('80 + 150 = 230 kcal')}</div>
{exo(9, '⭐⭐', 'أكل أحمد كوب أرز وقطعة دجاج ولوح شوكولاتة. كم سعرة حرارية استهلك؟' + dots(2))}
{exo(10, '⭐⭐', 'ما النصيحة التي ستقدمها لأحمد لتوازن وجبته؟' + dots(1))}
{exo(11, '⭐⭐⭐', 'مريم تأكل كل يوم خبزاً ومعكرونة وحلويات، وتشرب المشروبات الغازية ونادراً ما تأكل الفواكه والخضروات. هل تغذيتها متوازنة؟ لماذا؟' + dots(2))}
{defi('تخيّل أنك طبيب تغذية! أنشئ قائمة متوازنة ليوم كامل (إفطار، غداء، وجبة خفيفة، عشاء) من أطعمتنا المحلية: التمر، الحليب، السمك، الأرز، الكسكس، الخضروات… يجب أن تحتوي على جميع المجموعات الغذائية وتجنب الإفراط في السكر والدهون.' + dots(2))}'''
    return ('مسائل — التوازن الغذائي', body, True)


# ═══════════════ الوحدة 2 : التوازن الطاقوي (D8-D12) ═══════════════
def s2_p1():
    body = f'''
{objectifs(['أعرّف التوازن الطاقوي بين ما نأكل وما ننفق',
            'أفهم ماذا يحدث عند فائض الطاقة أو نقصها',
            'أوازن بين الأكل والنشاط البدني'])}
{badge_row('أتعلّم', 'التوازن الطاقوي', 'garcon')}
<div class="frame has-video">
  <ul>
    <li>التوازن الطاقوي هو العلاقة بين <span class="hl">الطاقة المستهلكة</span> و<span class="hl">الطاقة التي ينفقها الجسم</span>.</li>
    <li>الطاقة تأتي من <span class="hl">الأغذية والمشروبات</span> التي نستهلكها.</li>
    <li>الجسم يستخدم هذه الطاقة للعمل: <span class="hl">التنفس</span> و<span class="hl">الحركة</span> و<span class="hl">التفكير</span>.</li>
    <li>إذا لم يكن متوازناً، قد نكتسب وزناً (<span class="hl">فائض</span>) أو نفقده (<span class="hl">نقص</span>).</li>
  </ul>
  {video_box()}
</div>
<div style="display:flex;align-items:center;justify-content:center;gap:2.6mm;margin:.6mm 0">
  {figure_img(FIGS_SCI['petit_dejeuner'], 17, 'نأكل: طاقة تدخل')}
  {balance_svg('🏃 ننفق', '🍽️ نأكل', w=34)}
  {figure_img(FIGS_SCI['famille_sport'], 19, 'ننفق: طاقة تخرج')}
</div>
<div class="sg-note">الكفّتان متساويتان ← الوزن ثابت والجسم بصحة جيدة!</div>
{formula('⚖️ الطاقة المستهلكة = الطاقة المنفقة ← الوزن ثابت', 'var(--p-green)')}
{formula('📈 المستهلكة أكبر من المنفقة ← اكتساب وزن وأمراض', 'var(--p-rose)')}
{formula('📉 المستهلكة أصغر من المنفقة ← نقص وزن وتعب', 'var(--p-blue)')}
{astuce('الجري واللعب في الساحة والسباحة والمشي إلى المدرسة كلها أنشطة <b>تنفق الطاقة</b> وتحافظ على توازنك الطاقوي!')}'''
    return ('التوازن الطاقوي', body, False)


def s2_p2():
    vf = vf_lines(['الطاقة المقدمة يجب أن تكون مساوية لتلك المنفقة.',
                   'الإفراط في الدهون يؤدي إلى أمراض قلبية.',
                   'الحصة الغذائية هي نفسها للجميع.'])
    body = f'''
{badge_row('تمارين', 'أختبر فهمي', 'fille')}
<div class="exemple" style="margin-top:0"><b class="tag">✏️ مثال محلول:</b> التوازن الطاقوي = الطاقة المستهلكة تساوي الطاقة المنفقة ✓</div>
{exo(1, '⭐', 'عندما نأكل أكثر مما ينفقه جسمنا، يمكن أن يؤدي ذلك إلى:<br>'
      + choix('أ) اكتساب وزن وأمراض', 'ب) صحة جيدة', 'ج) نقص الطاقة'))}
{exo(2, '⭐⭐', f'الدهون عناصر مهمة في التغذية، لكن بكميات كبيرة جداً يمكن أن:<br>{SQ} أ) تعطي مزيداً من العضلات &nbsp;·&nbsp; {SQ} ب) تسبب أمراضاً قلبية &nbsp;·&nbsp; {SQ} ج) تحسن الهضم')}
{exo(3, '⭐⭐', 'للحفاظ على توازن طاقوي جيد، يجب:<br>'
      + choix('أ) الأكل بكميات كبيرة دون حركة',
              'ب) تجنب النشويات بشكل كامل',
              'ج) ممارسة النشاط البدني والأكل الجيد'))}
{exo(4, '⭐', 'ضع علامة ✓ أمام صح أو خطأ:<br>' + vf)}
{exo(5, '⭐⭐', 'لماذا يعد الإفطار وجبة مهمة قبل الذهاب إلى المدرسة؟' + dots(1))}'''
    return ('تمارين — التوازن الطاقوي', body, False)


def s2_p3():
    body = f'''
{badge_row('تمارين', 'أكمل واربط', 'garcon')}
<div class="exemple"><b class="tag">✏️ مثال محلول:</b> الطاقة التي نستخدمها تأتي من <b>الأغذية</b> التي نأكلها.</div>
{exo(6, '⭐⭐', f'''أكمل الجمل:<br>
إذا أكلنا طاقة أكثر مما ننفق، نخاطر بـ {OVAL}.<br>
الشخص الذي يمارس الرياضة كثيراً يحتاج إلى {OVS} طاقة من الشخص الجالس طوال اليوم.<br>
الدهون ضرورية للجسم، لكن بكميات كبيرة جداً يمكن أن تسبب {OVAL}.<br>
التوازن الطاقوي يعني أن الطاقة {OVS} يجب أن تساوي الطاقة {OVS}.''')}
{exo(7, '⭐⭐', 'اربط كل مصطلح بتعريفه (ارسم خطاً):'
      + relie(['الطاقة المنفقة', 'الحصة الغذائية', 'الدهون', 'أمراض قلبية'],
              ['مجموع الأغذية المستهلكة في يوم',
               'مشاكل صحية مرتبطة بتغذية سيئة',
               'كمية السعرات التي تُصرف بالحركة',
               'مواد تعطي الطاقة لكنها تسبب أمراضاً إذا استُهلكت بإفراط']))}
{exo(8, '⭐⭐⭐', 'في رأيك، ما هي الوجبة المتوازنة؟ أعطِ مثالاً من مائدتنا.' + dots(2))}
{attention('النشاط البدني ليس اختيارياً! الجلوس الطويل أمام الشاشات مع أكل كثير يكسر التوازن الطاقوي.')}'''
    return ('تمارين — أكمل واربط', body, False)


def s2_p4():
    body = f'''
{badge_row('مسائل', 'وضعيات للتحليل', 'fille')}
<div class="exemple"><b class="tag">✏️ مثال محلول:</b> ساعة رياضة واحدة تنفق {MX('300 kcal')} ← ساعتان تنفقان {MX('2 × 300 = 600 kcal')}</div>
{exo(9, '⭐⭐', 'المختار يحب أكل الهامبورغر والبطاطا المقلية كل يوم. لا يمارس الرياضة كثيراً ويفضل اللعب بالألعاب الإلكترونية طوال اليوم.<br>ما النشاط الذي تنصح به المختار ليوازن طاقته؟ اقترح نشاطين ومدتهما.' + dots(2))}
{exo(10, '⭐⭐', 'ما هي النصائح التي يمكنك تقديمها للمختار للحفاظ على توازن طاقوي جيد؟' + dots(2))}
{exo(11, '⭐⭐⭐', f'''يصرف الطفل حوالي {MX('300 kcal')} في الساعة عند ممارسة الرياضة و{MX('100 kcal')} في الساعة عند الجلوس.<br>
سيدي محمد يأكل {MX('1 800 kcal')} يومياً. يمارس الرياضة ساعتين ويجلس 6 ساعات.<br>
أ) كم سعرة حرارية ينفق بفضل الرياضة؟ &nbsp; ب) كم سعرة ينفق بالجلوس؟<br>
ج) ما هو إجمالي إنفاقه خلال هاتين الفترتين (الرياضة + الجلوس)؟<br>
د) قارن هذا الإنفاق بـ {MX('1 800 kcal')} المستهلكة — هل يتساويان <b>لهذه الفترات فقط</b>؟''' + dots(2))}
{defi('اقترح للمختار برنامج يوم كامل: وجبات متوازنة من أطعمتنا المحلية + نشاط بدني ينفق به طاقته بدل الألعاب الإلكترونية.' + dots(2))}'''
    return ('مسائل — التوازن الطاقوي', body, True)


# ═══════════════ الوحدة 3 : التصحر (D13-D16) ═══════════════
def s3_p1():
    body = f'''
{objectifs(['أعرّف التصحر وأذكر أسبابه',
            'أشرح عواقبه على الإنسان والبيئة',
            'أقترح حلولاً لمكافحة زحف الرمال'])}
{badge_row('أتعلّم', 'التصحر', 'garcon')}
<div class="frame has-video">
  <ul>
    <li>التصحر هو تحول <span class="hl">الأراضي الخصبة</span> إلى أراضٍ <span class="hl">جافة وفقيرة</span>، تشبه في الغالب الصحراء.</li>
    <li>ينجم عن <span class="hl">الجفاف</span> و<span class="hl">ندرة الأمطار</span> والأنشطة البشرية كـ<span class="hl">إزالة الغابات</span> و<span class="hl">الرعي الجائر</span>.</li>
    <li>يؤدي إلى فقدان <span class="hl">الغطاء النباتي</span> وتراجع <span class="hl">الإنتاج الزراعي</span> واختفاء بعض الأنواع.</li>
    <li>له عواقب وخيمة على السكان: <span class="hl">نقص الغذاء والماء</span>.</li>
    <li>لمكافحته: <span class="hl">حماية التربة</span> و<span class="hl">زراعة الأشجار</span> واستخدام الماء <span class="hl">بشكل عقلاني</span>.</li>
  </ul>
  {video_box()}
</div>
<svg width="96mm" height="17mm" viewBox="0 0 120 21" style="overflow:visible;display:block;margin:.8mm auto 0">
  <path d="M96,13 Q102,7 108,13 T120,13 L120,16 L96,16 Z" fill="#f5d9a8" stroke="#d8b26a" stroke-width=".5"/>
  <path d="M100,10 Q104,6.5 108,10" fill="none" stroke="#c9975a" stroke-width=".5"/>
  <text x="108" y="20" text-anchor="middle" font-size="3.4" font-weight="900" fill="#8a4a12">زحف الرمال</text>
  <text x="88" y="12" text-anchor="middle" font-size="5" font-weight="900" fill="#c0392b">⬅</text>
  <g stroke="#2b6e3a" stroke-width=".8">
    <line x1="62" y1="16" x2="62" y2="10"/><line x1="70" y1="16" x2="70" y2="9"/><line x1="78" y1="16" x2="78" y2="10"/>
  </g>
  <circle cx="62" cy="8" r="3.4" fill="#5aa868"/><circle cx="70" cy="6.6" r="4" fill="#3f8f50"/><circle cx="78" cy="8" r="3.4" fill="#5aa868"/>
  <text x="70" y="20" text-anchor="middle" font-size="3.4" font-weight="900" fill="#2b6e3a">الحزام الأخضر يوقف الرمال</text>
  <rect x="20" y="9" width="9" height="7" fill="#ffd98c" stroke="#8a4a12" stroke-width=".5"/>
  <path d="M18.5,9 L24.5,4.5 L30.5,9 Z" fill="#e2914c" stroke="#8a4a12" stroke-width=".5"/>
  <rect x="34" y="10" width="7" height="6" fill="#ffd98c" stroke="#8a4a12" stroke-width=".5"/>
  <path d="M33,10 L37.5,6.5 L42,10 Z" fill="#e2914c" stroke="#8a4a12" stroke-width=".5"/>
  <path d="M4,15 Q8,12 12,14" fill="none" stroke="#5aa868" stroke-width=".9"/>
  <text x="26" y="20" text-anchor="middle" font-size="3.4" font-weight="900" fill="#4a3a1c">القرية والمزارع محميّة ✅</text>
  <line x1="0" y1="16" x2="120" y2="16" stroke="#c9b98a" stroke-width=".5"/>
</svg>
<div style="display:flex;gap:5mm;justify-content:center;margin:.6mm 0">
  {figure_img(FIGS_SCI['deforestation'], 22, 'إزالة الأشجار: سبب بشري')}
  {figure_img(FIGS_SCI['terre_craquelee'], 26, 'أرض جفّت وتشققت: هذه هي النتيجة')}
</div>
{bulle('fille', 'التصحر يمسّ حياتنا في موريتانيا: زحف الرمال على البيوت والطرق في نواكشوط وآدرار، وتراجع المراعي والواحات!')}
{astuce('<b>الرعي الجائر</b> يعني كثرة الحيوانات على أرض واحدة، فتأكل كل الغطاء النباتي ولا تترك للتربة ما يحميها من الرياح.')}'''
    return ('التصحر', body, False)


def s3_p2():
    body = f'''
{badge_row('تمارين', 'أختبر فهمي', 'fille')}
<div class="exemple"><b class="tag">✏️ مثال محلول:</b> ما هو التصحر؟ <b>توسع الصحاري بسبب الأنشطة البشرية والمناخ</b> <span class="sq">✓</span></div>
{exo(1, '⭐', 'ما هو أحد الأسباب الرئيسية للتصحر؟<br>'
      + choix('أ) إزالة الغابات والزراعة المكثفة',
              'ب) زراعة الأشجار بشكل مفرط',
              'ج) بناء السدود'))}
{exo(2, '⭐', 'ما هي عواقب التصحر؟<br>'
      + choix('أ) زيادة الأراضي الزراعية',
              'ب) تراجع المياه والتربة الخصبة',
              'ج) ظهور أنواع حيوانية جديدة'))}
{exo(3, '⭐', 'كيف يمكن مكافحة التصحر؟<br>'
      + choix('أ) بقطع المزيد من الأشجار لاستخدام الخشب',
              'ب) باستخدام مزيد من المبيدات',
              'ج) بإعادة التشجير وحماية التربة'))}
{exo(4, '⭐⭐', 'اربط كل سبب بعواقبه (ارسم خطاً):'
      + relie(['إزالة الغابات', 'الاحترار المناخي', 'الزراعة المكثفة'],
              ['جفاف أكثر تكراراً', 'إفقار التربة وتدهورها', 'زحف الرمال']))}'''
    return ('تمارين — التصحر', body, False)


def s3_p3():
    body = f'''
{badge_row('تمارين', 'أكمل وأقترح', 'garcon')}
<div class="exemple"><b class="tag">✏️ مثال محلول:</b> عندما يكون الغطاء النباتي ضعيفاً، تصبح التربة <b>هشّة</b> ولا تحتجز الماء.</div>
{exo(5, '⭐⭐', f'''أكمل الجمل:<br>
التصحر ناتج عن عوامل {OVS} و{OVS}.<br>
عندما يكون الغطاء النباتي ضعيفاً، تصبح التربة {OVAL} ولا تحتجز الماء.<br>
الزراعة المكثفة والقطع المفرط للأشجار يمكن أن يؤديا إلى {OVAL}.<br>
لمكافحة التصحر، يمكن زراعة {OVS} والحد من {OVS}.''')}
{exo(6, '⭐⭐', 'اذكر أربعة أسباب للتصحر:' + dots(3))}
{exo(7, '⭐⭐⭐', 'قريتك في آدرار مهددة بزحف الرمال. اقترح إجراءين لحمايتها:' + dots(2))}
{astuce('السياج النباتي حول القرية يوقف زحف الرمال: الأشجار تكسر قوة الرياح وجذورها تثبّت التربة.')}'''
    return ('تمارين — أكمل وأقترح', body, False)


def s3_p4():
    body = f'''
{badge_row('مسائل', 'وضعيات للتحليل', 'fille')}
<div class="exemple"><b class="tag">✏️ مثال محلول:</b> غطاء نباتي انخفض من {MX('40 %')} إلى {MX('25 %')} ← الانخفاض = {MX('40 − 25 = 15 %')}</div>
{exo(8, '⭐⭐', f'''كانت منطقة ما تغطي {MX('30 %')} من مساحتها بالأشجار عام 1990. في 2020 لم يتبق سوى {MX('10 %')}.<br>
أ) بكم انخفضت نسبة الغطاء النباتي؟{dots(1)}
ب) من 1990 إلى 2020 انخفض الغطاء بمقدار {MX('20')} نقطة مئوية كل 30 سنة. إذا استمر <b>نفس الانخفاض</b>، فماذا سيبقى عام 2050؟ (هل يمكن أن تكون النسبة سالبة؟){dots(1)}
ج) اقترح حلولاً لوقف هذا التراجع.{dots(1)}''')}
{exo(9, '⭐⭐⭐', '''في منطقة من بلادنا، يلاحظ السكان أن أراضيهم تزداد جفافاً. نادراً ما تمطر والمحاصيل لم تعد تنمو بشكل جيد. يقطع المزارعون الأشجار للحصول على حطب الوقود، وتأكل الحيوانات كل الغطاء النباتي.<br>
أ) ما هي أسباب هذه المشكلة؟''' + dots(2) + 'ب) ماذا يمكن فعله لتحسين الوضع؟' + dots(2))}
{defi('مشروع «السور الأخضر الكبير» يمر عبر موريتانيا لوقف زحف الرمال. اقترح ثلاثة أعمال يمكن لمدرستك القيام بها للمشاركة في مكافحة التصحر.' + dots(2))}'''
    return ('مسائل — التصحر', body, True)


# ─────────────────────────── export ───────────────────────────
UNITS_S1 = [
    dict(num=1, title='التوازن الغذائي', sub='المجموعات الغذائية · الوجبات المتوازنة', color='var(--p-green)',
         pages=[s1_p1(), s1_p2(), s1_p3(), s1_p4()]),
    dict(num=2, title='التوازن الطاقوي', sub='الطاقة المستهلكة والطاقة المنفقة', color='var(--p-yell)',
         pages=[s2_p1(), s2_p2(), s2_p3(), s2_p4()]),
    dict(num=3, title='التصحر', sub='الأسباب والعواقب ومكافحة زحف الرمال 🇲🇷', color='var(--p-rose)',
         pages=[s3_p1(), s3_p2(), s3_p3(), s3_p4()]),
]
