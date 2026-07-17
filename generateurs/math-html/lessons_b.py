# -*- coding: utf-8 -*-
"""Leçons 9-15 + bilan : décimaux/pourcentages/commerce + mesures/géométrie."""
from cahier_base import badge_row, video_box, exo, dots, pie

FR = lambda a, b: f'<span class="mfrac"><span>{a}</span><span>{b}</span></span>'
MX = lambda s: f'<span class="mexp">{s}</span>'
CPA = '<div class="cpa"><b>طريقة سنغافورة:</b><span>🧊 محسوس</span><span>🖼️ مصوّر</span><span>🔢 مجرّد</span></div>'


def L9():
    body = f'''
{badge_row('أتعلّم', 'القاعدة والأمثلة', 'fille')}
<div class="frame has-video">
  <ul>
    <li>العدد العشري عدد يُكتب <span class="hl">بفاصلة</span>: قبلها <span class="hl">الجزء الصحيح</span> وبعدها <span class="hl">الجزء العشري</span>.</li>
    <li>نقرأ الجزء الصحيح أولًا ثم الجزء العشري: {MX('12,36')} = 12 وحدة و36 جزءًا من المئة.</li>
    <li>💡 نستعملها كل يوم: النقود ({MX('3,50')} أوقية)، القياسات ({MX('1,75')} م)، الوقت ({MX('1,5')} سا).</li>
  </ul>
  {video_box()}
</div>
{CPA}

{badge_row('أمثّل', 'جدول المراتب العشرية', 'garcon')}
<div class="frame">
  <table class="fam-table" style="max-width:120mm;margin:0 auto 2mm">
    <tr>
      <th class="fam-m" style="background:var(--p-green)">العشرات</th>
      <th class="fam-u" style="background:var(--p-yell)">الآحاد</th>
      <th style="background:#2b2b2b;color:#fff;width:6mm">,</th>
      <th class="fam-k" style="background:var(--p-rose)">الأعشار {FR(1,10)}</th>
      <th class="fam-g" style="background:var(--p-blue)">أجزاء المئة {FR(1,100)}</th>
    </tr>
    <tr>
      <td style="font-size:14px;font-weight:900">1</td>
      <td style="font-size:14px;font-weight:900">2</td>
      <td style="font-size:16px;font-weight:900">,</td>
      <td style="font-size:14px;font-weight:900">3</td>
      <td style="font-size:14px;font-weight:900">6</td>
    </tr>
  </table>
  <div style="text-align:center;direction:ltr">
    <span class="pv-disc pv-10">10</span><span class="pv-disc pv-1">1</span><span class="pv-disc pv-1">1</span>
    <span style="font-weight:900;font-size:16px;vertical-align:middle">,</span>
    <span class="pv-disc pv-p10">0,1</span><span class="pv-disc pv-p10">0,1</span><span class="pv-disc pv-p10">0,1</span>
    <span class="pv-disc pv-p100">0,01</span><span class="pv-disc pv-p100">0,01</span><span class="pv-disc pv-p100">0,01</span><span class="pv-disc pv-p100">0,01</span><span class="pv-disc pv-p100">0,01</span><span class="pv-disc pv-p100">0,01</span>
  </div>
  <div class="scallop">{MX('12,36')} = {MX('10 + 2 + 0,3 + 0,06')} — الفاصلة تفصل الوحدات عن الأعشار.</div>
</div>

{badge_row('تمارين', 'من السهل ⭐ إلى الصعب ⭐⭐⭐', 'garcon')}
<div class="cols">
  {exo(1, '⭐ سهل', f'اكتب بالحروف:<br>{MX("3,5")} ' + dots(1) + f'{MX("7,25")} ' + dots(1))}
  {exo(2, '⭐ سهل', f'اكتب بالأرقام:<br>خمس وحدات وثلاثة أعشار <span class="oval s"></span><br>12 وحدة و36 جزءًا من المئة <span class="oval s"></span>')}
  {exo(3, '⭐⭐ متوسط', f'ضع كل عدد في جدول المراتب: {MX("4,07")} · {MX("15,3")}<div class="dashcard tall"></div>')}
  {exo(4, '⭐⭐ متوسط', f'قارن ثم رتّب تصاعديًا:<br>{MX("2,5")} · {MX("2,05")} · {MX("2,55")} · {MX("2,15")}' + dots(2))}
  {exo(5, '⭐⭐⭐ صعب', f'انجز عموديًا (الفاصلة تحت الفاصلة):<br>{MX("12,45 + 7,80")} = <span class="oval"></span><br>{MX("20,5 − 8,75")} = <span class="oval"></span><div class="dashcard"></div>')}
  {exo(6, '⭐⭐⭐ صعب', f'مسألة: اشترت مريم خبزًا بـ {MX("15,5")} أوقية وحليبًا بـ {MX("22,75")} أوقية. دفعت 50 أوقية. مثّل بنموذج الشريط ثم احسب الباقي.<div class="dashcard tall"></div>')}
</div>'''
    return ('الدرس 9 — الأعداد العشرية', body, 'الوحدة 3 · الأعداد العشرية والنسب')


def L10():
    body = f'''
{badge_row('أتعلّم', 'القاعدة والأمثلة', 'fille')}
<div class="frame has-video">
  <ul>
    <li>النسبة المئوية طريقة لقول <span class="hl">« من 100 »</span>.</li>
    <li>{MX('50 %')} = النصف · {MX('25 %')} = الربع · {MX('10 %')} = العُشر.</li>
    <li>👉 لحساب نسبة مئوية من عدد: <span class="hl">نضرب العدد في النسبة ونقسم على 100</span>.</li>
  </ul>
  {video_box()}
</div>
{CPA}

{badge_row('أمثّل', 'شبكة المئة ونموذج الشريط', 'garcon')}
<div class="frame">
  <div style="display:flex;flex-direction:row-reverse;gap:7mm;align-items:center;justify-content:space-around;flex-wrap:wrap">
    <div style="text-align:center">
      <div style="font-size:10px;font-weight:900;color:#8a4a12;margin-bottom:1mm">{MX('25 %')} من الشبكة ملوّنة</div>
      <div class="grid100"><div class="gfill" style="width:25%"></div></div>
    </div>
    <div style="flex:1;min-width:70mm">
      <div style="font-size:10px;font-weight:900;color:#8a4a12;text-align:center;margin-bottom:1mm">{MX('25 %')} من 200: أقسم الشريط إلى 4 أجزاء</div>
      <div class="barmodel">
        <div class="bm-row"><div class="bm-seg c1" style="flex:1">50</div><div class="bm-seg" style="flex:1">50</div><div class="bm-seg" style="flex:1">50</div><div class="bm-seg" style="flex:1">50</div></div>
        <div class="bm-brace"><span>الكل = 200</span></div>
      </div>
      <div class="scallop" style="margin-top:4mm">{MX('25 %')} من {MX('200')} = {MX('200 × 25 ÷ 100 = 50')} ✓</div>
    </div>
  </div>
</div>

{badge_row('تمارين', 'من السهل ⭐ إلى الصعب ⭐⭐⭐', 'garcon')}
<div class="cols">
  {exo(1, '⭐ سهل', f'صل كل نسبة بما يناسبها:<br>{MX("50 %")} · {MX("25 %")} · {MX("10 %")}<br>العُشر · النصف · الربع' + dots(1))}
  {exo(2, '⭐ سهل', f'احسب:<br>{MX("50 %")} من {MX("60")} = <span class="oval s"></span><br>{MX("25 %")} من {MX("80")} = <span class="oval s"></span>')}
  {exo(3, '⭐⭐ متوسط', f'لوّن {MX("40 %")} من شبكة المئة:<div style="margin-top:1.5mm"><div class="grid100"></div></div>')}
  {exo(4, '⭐⭐ متوسط', f'احسب بالقاعدة:<br>{MX("10 %")} من {MX("350")} = <span class="oval s"></span><br>{MX("20 %")} من {MX("150")} = <span class="oval s"></span><br>ثم حوّل: {FR(3,4)} = <span class="oval s"></span> %')}
  {exo(5, '⭐⭐⭐ صعب', f'مسألة: قميص ثمنه {MX("2 000")} أوقية عليه تخفيض {MX("30 %")}. مثّل بنموذج الشريط ثم احسب الثمن الجديد.<div class="dashcard tall"></div>')}
  {exo(6, '⭐⭐⭐ صعب', f'مسألة: في قسم فيه 40 تلميذًا نجح {MX("85 %")}. كم تلميذًا نجح؟ وكم لم ينجح؟' + dots(3))}
</div>'''
    return ('الدرس 10 — النسبة المئوية %', body, 'الوحدة 3 · الأعداد العشرية والنسب')


def L11():
    body = f'''
{badge_row('أتعلّم', 'القاعدة والأمثلة', 'fille')}
<div class="frame has-video">
  <ul>
    <li><span class="hl">ثمن الشراء</span>: المدفوع للحصول على الشيء · <span class="hl">ثمن البيع</span>: الذي نبيع به.</li>
    <li><span class="hl">الربح</span> إذا بعنا بأعلى من ثمن الشراء · <span class="hl">الخسارة</span> إذا بعنا بأقل.</li>
    <li>الربح = ثمن البيع − ثمن الشراء · ثمن البيع = ثمن الشراء + الربح.</li>
  </ul>
  {video_box()}
</div>
{CPA}

{badge_row('أمثّل', 'نموذج شريط الربح', 'garcon')}
<div class="frame">
  <div style="font-size:11px;font-weight:800;text-align:center;margin-bottom:1mm">اشترى تاجر سلعة بـ {MX('800')} أوقية وباعها بـ {MX('950')} أوقية</div>
  <div class="barmodel">
    <div class="bm-row"><div class="bm-seg c4" style="flex:800">ثمن الشراء : 800</div><div class="bm-seg c3" style="flex:150">الربح ؟</div></div>
    <div class="bm-brace"><span>ثمن البيع = 950</span></div>
  </div>
  <div class="scallop" style="margin-top:4mm">الربح = {MX('950 − 800 = 150')} أوقية ✅ — الشريط يوضح أن البيع = الشراء + الربح.</div>
</div>

{badge_row('تمارين', 'من السهل ⭐ إلى الصعب ⭐⭐⭐', 'garcon')}
<div class="cols">
  {exo(1, '⭐ سهل', 'ربح أم خسارة؟ ضع ✔ :<br>شراء بـ 500 وبيع بـ 650 → ربح ☐ خسارة ☐<br>شراء بـ 900 وبيع بـ 750 → ربح ☐ خسارة ☐')}
  {exo(2, '⭐ سهل', f'احسب الربح:<br>ثمن الشراء {MX("1 200")} أوقية، ثمن البيع {MX("1 500")} أوقية.<br>الربح = <span class="oval"></span>')}
  {exo(3, '⭐⭐ متوسط', f'احسب ثمن البيع (ارسم الشريط):<br>شراء دراجة بـ {MX("4 500")} أوقية + ربح {MX("800")} أوقية.<div class="dashcard tall"></div>')}
  {exo(4, '⭐⭐ متوسط', f'احسب الخسارة:<br>شراء بضاعة بـ {MX("6 000")} أوقية وبيعها بـ {MX("5 250")} أوقية.<br>الخسارة = <span class="oval"></span>' + dots(1))}
  {exo(5, '⭐⭐⭐ صعب', f'مسألة: اشترى تاجر 20 قلمًا بـ {MX("50")} أوقية للقلم، وباعها كلها بـ {MX("1 300")} أوقية. احسب ثمن الشراء الكلي ثم الربح.' + dots(3))}
  {exo(6, '⭐⭐⭐ صعب', f'مسألة مركّبة: اشترى بائع سلعة بـ {MX("2 000")} أوقية وباعها بربح {MX("15 %")} من ثمن الشراء. احسب الربح ثم ثمن البيع.' + dots(3))}
</div>'''
    return ('الدرس 11 — الشراء والبيع: الربح والخسارة', body, 'الوحدة 3 · الأعداد العشرية والنسب')


def L12():
    body = f'''
{badge_row('أتعلّم', 'القاعدة والأمثلة', 'fille')}
<div class="frame has-video">
  <ul>
    <li>قياس الطول = معرفة عدد وحدات القياس الموافقة للمسافة.</li>
    <li><span class="hl">مم</span>: الأطوال الصغيرة جدًا (سُمك بطاقة) · <span class="hl">سم</span>: عرض إصبع.</li>
    <li><span class="hl">م</span>: طول مسطرة التلميذ × 3 · <span class="hl">كم</span>: المسافة بين مدينتين.</li>
    <li>{MX('1 كم = 1000 م')} · {MX('1 م = 100 سم')} · {MX('1 سم = 10 مم')}.</li>
  </ul>
  {video_box()}
</div>
{CPA}

{badge_row('أمثّل', 'جدول التحويل ونموذج الشريط', 'garcon')}
<div class="frame">
  <table class="fam-table" style="max-width:130mm;margin:0 auto 2mm">
    <tr>
      <th class="fam-g" style="background:var(--p-blue)">كم</th>
      <th style="background:#eee">هم</th>
      <th style="background:#eee">دام</th>
      <th class="fam-m" style="background:var(--p-green)">م</th>
      <th style="background:#eee">دم</th>
      <th class="fam-k" style="background:var(--p-rose)">سم</th>
      <th class="fam-u" style="background:var(--p-yell)">مم</th>
    </tr>
    <tr>
      <td>2</td><td>5</td><td>0</td><td>0</td><td></td><td></td><td></td>
    </tr>
  </table>
  <div class="scallop">{MX('2,5 كم = 2 500 م')} — أنزل كل رقم في عموده ثم أكمل بالأصفار حتى الوحدة المطلوبة.</div>
  <div class="barmodel">
    <div class="bm-row"><div class="bm-seg c1" style="flex:1200">مشيًا : 1 200 م</div><div class="bm-seg c3" style="flex:800">بالحافلة : 800 م</div></div>
    <div class="bm-brace"><span>المسافة الكلية = 2 000 م = 2 كم</span></div>
  </div>
</div>

{badge_row('تمارين', 'من السهل ⭐ إلى الصعب ⭐⭐⭐', 'garcon')}
<div class="cols">
  {exo(1, '⭐ سهل', 'اختر الوحدة المناسبة (مم / سم / م / كم):<br>طول قلم: 15 <span class="oval s"></span> ارتفاع باب: 2 <span class="oval s"></span><br>المسافة بين نواكشوط وروصو: 204 <span class="oval s"></span>')}
  {exo(2, '⭐ سهل', f'حوّل:<br>{MX("3 م")} = <span class="oval s"></span> سم · {MX("5 سم")} = <span class="oval s"></span> مم<br>{MX("2 كم")} = <span class="oval s"></span> م')}
  {exo(3, '⭐⭐ متوسط', f'استعمل جدول التحويل:<br>{MX("450 سم")} = <span class="oval s"></span> م و <span class="oval s"></span> سم<br>{MX("3 250 م")} = <span class="oval s"></span> كم و <span class="oval s"></span> م<div class="dashcard"></div>')}
  {exo(4, '⭐⭐ متوسط', f'قارن (وحّد الوحدة أولًا):<br>{MX("2 م")} <span class="oval s"></span> {MX("180 سم")}<br>{MX("1,5 كم")} <span class="oval s"></span> {MX("1 600 م")}')}
  {exo(5, '⭐⭐⭐ صعب', f'مسألة: ملعب مستطيل طوله {MX("50 م")} وعرضه {MX("30 م")}. ارسم شكلًا واحسب محيطه.<div class="dashcard tall"></div>')}
  {exo(6, '⭐⭐⭐ صعب', f'مسألة: قطع مسافر {MX("1,2 كم")} مشيًا ثم {MX("800 م")} بالحافلة. مثّل بنموذج الشريط ثم أوجد المسافة الكلية بالمتر وبالكيلومتر.' + dots(3))}
</div>'''
    return ('الدرس 12 — قياس الأطوال وحسابها', body, 'الوحدة 4 · القياس والهندسة')


def L13():
    body = f'''
{badge_row('أتعلّم', 'القاعدة والأمثلة', 'fille')}
<div class="frame has-video">
  <ul>
    <li>الكتلة تسمح بمعرفة وزن الجسم.</li>
    <li><span class="hl">غ</span> (الغرام) → الأصغر · <span class="hl">كغ</span> (الكيلوغرام) → الوحدة الرئيسية · <span class="hl">طن</span> → الأكبر.</li>
    <li>{MX('1 كغ = 1000 غ')} · {MX('1 طن = 1000 كغ')}.</li>
  </ul>
  {video_box()}
</div>
{CPA}

{badge_row('أمثّل', 'الميزان ونموذج الشريط', 'garcon')}
<div class="frame">
  <div style="font-size:11px;font-weight:800;text-align:center;margin-bottom:1mm">شاحنة فارغة {MX('3,5 طن')} + حمولة {MX('1 800 كغ')} — أُحوّل أولًا إلى نفس الوحدة</div>
  <div class="barmodel">
    <div class="bm-row"><div class="bm-seg c4" style="flex:3500">الشاحنة : 3 500 كغ</div><div class="bm-seg c2" style="flex:1800">الحمولة : 1 800 كغ</div></div>
    <div class="bm-brace"><span>الكتلة الكلية = 5 300 كغ</span></div>
  </div>
  <div class="scallop" style="margin-top:4mm">{MX('3,5 طن = 3 500 كغ')} ثم {MX('3 500 + 1 800 = 5 300 كغ')}.</div>
</div>

{badge_row('تمارين', 'من السهل ⭐ إلى الصعب ⭐⭐⭐', 'garcon')}
<div class="cols">
  {exo(1, '⭐ سهل', 'اختر الوحدة المناسبة (غ / كغ / طن):<br>كتلة تفاحة: 150 <span class="oval s"></span> كتلة تلميذ: 35 <span class="oval s"></span><br>كتلة شاحنة محمّلة: 12 <span class="oval s"></span>')}
  {exo(2, '⭐ سهل', f'حوّل:<br>{MX("2 كغ")} = <span class="oval s"></span> غ · {MX("5 000 غ")} = <span class="oval s"></span> كغ<br>{MX("3 طن")} = <span class="oval s"></span> كغ')}
  {exo(3, '⭐⭐ متوسط', f'قارن:<br>{MX("2,5 كغ")} <span class="oval s"></span> {MX("2 400 غ")}<br>{MX("0,5 طن")} <span class="oval s"></span> {MX("600 كغ")}' + dots(1))}
  {exo(4, '⭐⭐ متوسط', f'اجمع الكتل (وحّد الوحدة أولًا):<br>{MX("1,5 كغ + 750 غ")} = <span class="oval"></span> غ<br>{MX("2 كغ + 250 غ + 1,25 كغ")} = <span class="oval"></span> غ')}
  {exo(5, '⭐⭐⭐ صعب', f'مسألة: وصفة خبز تحتاج {MX("750 غ")} من الدقيق. مثّل بنموذج الشريط ثم احسب كم كيلوغرامًا يلزم لصنع 8 أرغفة.<div class="dashcard tall"></div>')}
  {exo(6, '⭐⭐⭐ صعب', f'مسألة: ميزان كفّتاه متوازنتان: في الأولى كيس دقيق، وفي الثانية {MX("2 كغ")} و{MX("500 غ")}. ما كتلة الكيس بالغرام؟' + dots(2))}
</div>'''
    return ('الدرس 13 — الكتل', body, 'الوحدة 4 · القياس والهندسة')


def L14():
    angle_svg = '''<svg width="110" height="72" viewBox="0 0 110 72" style="display:block;margin:0 auto">
      <path d="M14,62 L96,62" stroke="#33475e" stroke-width="2.6"/>
      <path d="M14,62 L78,12" stroke="#33475e" stroke-width="2.6"/>
      <path d="M40,62 A26,26 0 0 0 34.5,46" fill="none" stroke="#e2504c" stroke-width="2.4"/>
      <text x="48" y="50" font-size="11" font-weight="900" fill="#c0392b" font-family="Cairo">38°</text>
    </svg>'''
    body = f'''
{badge_row('أتعلّم', 'القاعدة والأمثلة', 'fille')}
<div class="frame has-video">
  <ul>
    <li>الزاوية هي الانفراج الناتج عن خطين يلتقيان في نقطة. نقيسها <span class="hl">بالمنقلة</span>.</li>
    <li>① ضع مركز المنقلة على رأس الزاوية · ② طابِق ضلعًا مع الصفر · ③ اقرأ القياس بالدرجات (°).</li>
    <li>حادة &lt; 90° · <span class="hl">قائمة = 90°</span> · منفرجة بين 90° و180° · مستقيمة = 180°.</li>
  </ul>
  {video_box()}
</div>
{CPA}

{badge_row('أمثّل', 'أنواع الزوايا', 'garcon')}
<div class="frame">
  <div style="display:flex;flex-direction:row-reverse;gap:5mm;align-items:center;justify-content:space-around;flex-wrap:wrap">
    <div style="text-align:center">{angle_svg}<div style="font-size:10px;font-weight:900">زاوية حادة</div></div>
    <div style="text-align:center">
      <svg width="80" height="72" viewBox="0 0 80 72" style="display:block;margin:0 auto">
        <path d="M14,62 L72,62" stroke="#33475e" stroke-width="2.6"/>
        <path d="M14,62 L14,8" stroke="#33475e" stroke-width="2.6"/>
        <rect x="14" y="46" width="16" height="16" fill="none" stroke="#e2504c" stroke-width="2.2"/>
      </svg>
      <div style="font-size:10px;font-weight:900">زاوية قائمة 90°</div>
    </div>
    <div style="text-align:center">
      <svg width="120" height="72" viewBox="0 0 120 72" style="display:block;margin:0 auto">
        <path d="M76,62 L116,62" stroke="#33475e" stroke-width="2.6"/>
        <path d="M76,62 L34,20" stroke="#33475e" stroke-width="2.6"/>
        <path d="M94,62 A18,18 0 0 0 63.3,49.3" fill="none" stroke="#e2504c" stroke-width="2.4"/>
        <text x="86" y="44" font-size="10" font-weight="900" fill="#c0392b" font-family="Cairo">135°</text>
      </svg>
      <div style="font-size:10px;font-weight:900">زاوية منفرجة</div>
    </div>
  </div>
  <div class="scallop">💡 مجموع الزوايا المتجاورة على مستقيم يساوي <b>180°</b>.</div>
</div>

{badge_row('تمارين', 'من السهل ⭐ إلى الصعب ⭐⭐⭐', 'garcon')}
<div class="cols">
  {exo(1, '⭐ سهل', f'صنّف كل زاوية (حادة / قائمة / منفرجة / مستقيمة):<br>{MX("45°")} <span class="oval s"></span> {MX("90°")} <span class="oval s"></span><br>{MX("120°")} <span class="oval s"></span> {MX("180°")} <span class="oval s"></span>')}
  {exo(2, '⭐ سهل', 'أعطِ مثالًا من القسم أو البيت لزاوية قائمة، ثم لزاوية حادة.' + dots(2))}
  {exo(3, '⭐⭐ متوسط', 'قدّر قياس كل زاوية قبل قياسها بالمنقلة ثم تحقق:<br>زاوية أصغر قليلًا من القائمة ≈ <span class="oval s"></span><br>زاوية تساوي ثلثي المستقيمة ≈ <span class="oval s"></span>')}
  {exo(4, '⭐⭐ متوسط', f'استعمل المنقلة لرسم الزوايا:<br>{MX("30°")} · {MX("60°")} · {MX("135°")}<div class="dashcard tall"></div>')}
  {exo(5, '⭐⭐⭐ صعب', f'زاويتان متجاورتان على مستقيم، قياس الأولى {MX("65°")}. ما قياس الثانية؟ اشرح.' + dots(2))}
  {exo(6, '⭐⭐⭐ صعب', f'ثلاث زوايا متجاورة على مستقيم: {MX("40°")} و{MX("90°")} والثالثة مجهولة. احسبها.' + dots(2))}
</div>'''
    return ('الدرس 14 — الزوايا وقياسها', body, 'الوحدة 4 · القياس والهندسة')


def L15():
    lines_svg = '''<div style="display:flex;flex-direction:row-reverse;gap:6mm;align-items:center;justify-content:space-around;flex-wrap:wrap">
    <div style="text-align:center">
      <svg width="110" height="60" viewBox="0 0 110 60">
        <line x1="8" y1="18" x2="102" y2="18" stroke="#2f6ea5" stroke-width="3"/>
        <line x1="8" y1="42" x2="102" y2="42" stroke="#2f6ea5" stroke-width="3"/>
      </svg>
      <div style="font-size:10px;font-weight:900">متوازيان (سكة القطار)</div>
    </div>
    <div style="text-align:center">
      <svg width="90" height="70" viewBox="0 0 90 70">
        <line x1="8" y1="60" x2="82" y2="60" stroke="#2f6ea5" stroke-width="3"/>
        <line x1="45" y1="66" x2="45" y2="6" stroke="#e2504c" stroke-width="3"/>
        <rect x="45" y="46" width="14" height="14" fill="none" stroke="#33475e" stroke-width="2"/>
      </svg>
      <div style="font-size:10px;font-weight:900">متعامدان (زاوية قائمة)</div>
    </div>
    <div style="text-align:center">
      <svg width="100" height="70" viewBox="0 0 100 70">
        <line x1="6" y1="58" x2="94" y2="16" stroke="#2f6ea5" stroke-width="3"/>
        <line x1="10" y1="12" x2="90" y2="62" stroke="#5f9e62" stroke-width="3"/>
      </svg>
      <div style="font-size:10px;font-weight:900">متقاطعان (نقطة التقاء)</div>
    </div>
  </div>'''
    body = f'''
{badge_row('أتعلّم', 'القاعدة والأمثلة', 'fille')}
<div class="frame has-video">
  <ul>
    <li>المستقيمان <span class="hl">المتوازيان</span> لا يلتقيان أبدًا ويحافظان على نفس المسافة بينهما.</li>
    <li>المستقيمان <span class="hl">المتقاطعان</span> يلتقيان في نقطة.</li>
    <li>إذا شكّلا زاوية قائمة كانا <span class="hl">متعامدين</span>.</li>
    <li>أمثلة: حافتا المسطرة (توازٍ) · ذراعا الصليب (تعامد) · قطرا المربع (تقاطع).</li>
  </ul>
  {video_box()}
</div>
{CPA}

{badge_row('أمثّل', 'الأوضاع الثلاثة للمستقيمات', 'garcon')}
<div class="frame">
  {lines_svg}
</div>

{badge_row('تمارين', 'من السهل ⭐ إلى الصعب ⭐⭐⭐', 'garcon')}
<div class="cols">
  {exo(1, '⭐ سهل', 'أكمل:<br>مستقيمان لا يلتقيان أبدًا هما <span class="oval"></span><br>مستقيمان يلتقيان بزاوية قائمة هما <span class="oval"></span>')}
  {exo(2, '⭐ سهل', 'أعطِ مثالين من محيطك: مستقيمين متوازيين، ثم مستقيمين متعامدين.' + dots(2))}
  {exo(3, '⭐⭐ متوسط', 'ارسم بالمسطرة مستقيمًا (د)، ثم ارسم مستقيمًا (د′) موازيًا له.<div class="dashcard tall"></div>')}
  {exo(4, '⭐⭐ متوسط', 'ارسم بالكوس مستقيمين متعامدين يلتقيان في النقطة أ.<div class="dashcard tall"></div>')}
  {exo(5, '⭐⭐⭐ صعب', 'ارسم مستطيلًا، لوّن ضلعيه المتوازيين بالأزرق وعلّم أركانه القائمة.<div class="dashcard tall"></div>')}
  {exo(6, '⭐⭐⭐ صعب', 'صح أم خطأ؟ علّل:<br>أ) كل مستقيمين متعامدين متقاطعان. <span class="oval s"></span><br>ب) كل مستقيمين متقاطعين متعامدان. <span class="oval s"></span>' + dots(1))}
</div>'''
    return ('الدرس 15 — المستقيمات المتوازية والمتقاطعة', body, 'الوحدة 4 · القياس والهندسة')


def L16():
    body = f'''
{badge_row('بطولة الرياضيات', 'مراجعة كل الوحدات قبل المسابقة', 'fille')}
<div class="frame has-video">
  <ul>
    <li>تمارين من كل الوحدات الأربع: اعمل وحدك ثم امسح رمز QR ليصحّح لك التطبيق.</li>
    <li>استعمل أدوات سنغافورة: <span class="hl">نموذج الشريط</span> · <span class="hl">رابط العدد</span> · <span class="hl">الرسم</span> قبل الحساب.</li>
    <li>عُد إلى صفحات «أحتاج مراجعة» وأعد حل تمارينها. بالتوفيق! 🌟</li>
  </ul>
  {video_box()}
</div>

{badge_row('تمارين', 'البطولة الكبرى 🏆', 'garcon')}
<div class="cols">
  {exo(1, '🔢 ⭐⭐', f'اكتب بالحروف: {MX("1 025 467")}' + dots(2) + f'ثم رتّب تنازليًا: {MX("98 034")} · {MX("98 430")} · {MX("90 876")}' + dots(1))}
  {exo(2, '🔢 ⭐⭐', f'انجز عموديًا:<br>{MX("4 507 × 8")} = <span class="oval"></span><br>{MX("336 ÷ 8")} = <span class="oval"></span><div class="dashcard"></div>')}
  {exo(3, '🍰 ⭐⭐', f'احسب ثم بسّط:<br>{FR(2,3)} × {FR(3,4)} = <span class="oval s"></span> &nbsp;·&nbsp; {FR(1,2)} ÷ {FR(3,4)} = <span class="oval s"></span>')}
  {exo(4, '💰 ⭐⭐⭐', f'حاسوب ثمنه {MX("12 000")} أوقية عليه تخفيض {MX("25 %")}. مثّل بنموذج الشريط ثم احسب الثمن الجديد.<div class="dashcard tall"></div>')}
  {exo(5, '📐 ⭐⭐⭐', f'حديقة مستطيلة طولها {MX("1,2 كم")} وعرضها {MX("800 م")}. احسب محيطها بالمتر.' + dots(3))}
  {exo(6, '📐 ⭐⭐⭐', 'زاويتان متجاورتان على مستقيم، الأولى ضعف الثانية. ارسم شكلًا واحسب قياس كل منهما.<div class="dashcard tall"></div>')}
</div>'''
    return ('المراجعة الشاملة — بطولة الرياضيات 🏆', body, 'كل الوحدات · استعدادًا للمسابقة الوطنية')


LESSONS_B = [L9, L10, L11, L12, L13, L14, L15, L16]
