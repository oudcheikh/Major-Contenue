# -*- coding: utf-8 -*-
"""Leçons 1-8 : unité Nombres & opérations + unité Fractions."""
from cahier_base import badge_row, video_box, exo, dots, pie, numbond

FR = lambda a, b: f'<span class="mfrac"><span>{a}</span><span>{b}</span></span>'
MX = lambda s: f'<span class="mexp">{s}</span>'
CPA = '<div class="cpa"><b>طريقة سنغافورة:</b><span>🧊 محسوس</span><span>🖼️ مصوّر</span><span>🔢 مجرّد</span></div>'


def L1():
    body = f'''
{badge_row('أتعلّم', 'القاعدة والأمثلة', 'fille')}
<div class="frame has-video">
  <ul>
    <li>الأعداد الكبيرة تمتد من {MX('1 000')} (ألف) إلى {MX('1 000 000')} (مليون) وأكثر.</li>
    <li>نقرؤها بتجميعها <span class="hl">ثلاثة أرقام ثلاثة أرقام</span>: الوحدات، الآلاف، الملايين، المليارات.</li>
    <li>مثال: {MX('245 000')} = مئتان وخمسة وأربعون ألفًا.</li>
    <li>نستعمل الأصفار لتحديد المراتب (الآحاد، العشرات، المئات) فلا نحذفها أبدًا.</li>
  </ul>
  {video_box()}
</div>
{CPA}

{badge_row('أمثّل', 'أقراص المراتب وجدول الفصائل', 'garcon')}
<div class="frame">
  <div style="display:flex;flex-direction:row-reverse;gap:6mm;align-items:center;justify-content:space-between">
    <div style="text-align:center">
      <div style="font-size:10px;font-weight:900;color:#8a4a12;margin-bottom:1mm">العدد {MX('2 314')} بالأقراص</div>
      <div style="direction:ltr">
        <span class="pv-disc pv-1000">1000</span><span class="pv-disc pv-1000">1000</span>
        <span class="pv-disc pv-100">100</span><span class="pv-disc pv-100">100</span><span class="pv-disc pv-100">100</span>
        <span class="pv-disc pv-10">10</span>
        <span class="pv-disc pv-1">1</span><span class="pv-disc pv-1">1</span><span class="pv-disc pv-1">1</span><span class="pv-disc pv-1">1</span>
      </div>
    </div>
    <table class="fam-table" style="max-width:88mm">
      <tr>
        <th class="fam-g" style="background:var(--p-blue)">فصيلة المليارات</th>
        <th class="fam-m" style="background:var(--p-green)">فصيلة الملايين</th>
        <th class="fam-k" style="background:var(--p-rose)">فصيلة الآلاف</th>
        <th class="fam-u" style="background:var(--p-yell)">فصيلة الوحدات</th>
      </tr>
      <tr>
        <td><div class="mini-cells"><span class="mini-cell">3</span><span class="mini-cell g">2</span><span class="mini-cell">&nbsp;</span></div></td>
        <td><div class="mini-cells"><span class="mini-cell">0</span><span class="mini-cell g">4</span><span class="mini-cell">7</span></div></td>
        <td><div class="mini-cells"><span class="mini-cell">5</span><span class="mini-cell g">6</span><span class="mini-cell">2</span></div></td>
        <td><div class="mini-cells"><span class="mini-cell">0</span><span class="mini-cell g">7</span><span class="mini-cell">3</span></div></td>
      </tr>
      <tr>
        <td><div class="pink-strip">32 مليارًا</div></td>
        <td><div class="pink-strip">47 مليونًا</div></td>
        <td><div class="pink-strip">562 ألفًا</div></td>
        <td><div class="pink-strip">73</div></td>
      </tr>
    </table>
  </div>
  <div class="scallop">نقرأ: اثنان وثلاثون مليارًا وسبعة وأربعون مليونًا وخمسمائة واثنان وستون ألفًا وثلاثة وسبعون.</div>
</div>

{badge_row('تمارين', 'من السهل ⭐ إلى الصعب ⭐⭐⭐', 'garcon')}
<div class="cols">
  {exo(1, '⭐ سهل', f'اكتب بالأرقام:<br>خمسون ألفًا وثمانمائة وأربعة وستون <span class="oval"></span><br>ستة آلاف وأربعة وعشرون <span class="oval"></span><br>مئتا ألف وثمانية عشر <span class="oval"></span>')}
  {exo(2, '⭐ سهل', f'اكتب بالحروف: {MX("9 832")} · {MX("42 118")} · {MX("324")}' + dots(3))}
  {exo(3, '⭐⭐ متوسط', f'ضع كل عدد في جدول الفصائل ثم اقرأه:<br>{MX("6 521 004")} · {MX("2 345 709")}<div class="dashcard tall"></div>')}
  {exo(4, '⭐⭐ متوسط', f'مثّل العدد {MX("1 203")} بأقراص المراتب (ارسمها):<div class="dashcard tall"></div>')}
  {exo(5, '⭐⭐⭐ صعب', 'باستعمال الأرقام 0، 1، 2، 3، 4، 5، 6 (كل رقم مرة واحدة):<br>أ) أكبر عدد ممكن <span class="oval"></span><br>ب) أصغر عدد رقمُ عشراته 5 <span class="oval"></span>')}
  {exo(6, '⭐⭐⭐ صعب', f'مسألة: مدرستان فيهما {MX("15 432")} و{MX("15 342")} تلميذًا. أي مدرسة فيها تلاميذ أكثر؟ اشرح.' + dots(2))}
</div>'''
    return ('الدرس 1 — الأعداد الكبيرة: قراءتها وكتابتها', body, 'الوحدة 1 · الأعداد والعمليات')


def L2():
    body = f'''
{badge_row('أتعلّم', 'القاعدة والأمثلة', 'fille')}
<div class="frame has-video">
  <ul>
    <li>لمقارنة عددين ننظر أولًا إلى <span class="hl">عدد الأرقام</span>: الذي فيه أرقام أكثر هو الأكبر.</li>
    <li>إذا تساوى عدد الأرقام، نقارن <span class="hl">رقمًا رقمًا بدءًا من اليسار</span>.</li>
    <li>الرموز: {MX('&gt;')} أكبر من · {MX('&lt;')} أصغر من · {MX('=')} يساوي.</li>
    <li>الترتيب التصاعدي: من الأصغر إلى الأكبر · الترتيب التنازلي: من الأكبر إلى الأصغر.</li>
  </ul>
  {video_box()}
</div>
{CPA}

{badge_row('أمثّل', 'نموذج الشريط للمقارنة', 'garcon')}
<div class="frame">
  <div style="font-size:11px;font-weight:800;margin-bottom:1mm">أي مدرسة فيها تلاميذ أكثر؟ {MX('15 432')} أم {MX('15 342')}؟</div>
  <div class="barmodel">
    <div class="bm-row"><div class="bm-seg c1" style="flex:15432">المدرسة أ : 15 432</div></div>
    <div style="height:1.4mm"></div>
    <div class="bm-row"><div class="bm-seg c2" style="flex:15342">المدرسة ب : 15 342</div><div class="bm-seg empty" style="flex:90">؟</div></div>
  </div>
  <div class="scallop">نفس عدد الأرقام → نقارن من اليسار: 1=1 ثم 5=5 ثم <b>4 &gt; 3</b> إذن {MX('15 432 &gt; 15 342')} ، والفرق هو الجزء المخطّط.</div>
</div>

{badge_row('تمارين', 'من السهل ⭐ إلى الصعب ⭐⭐⭐', 'garcon')}
<div class="cols">
  {exo(1, '⭐ سهل', f'ضع {MX("&gt;")} أو {MX("&lt;")} أو {MX("=")} :<br>{MX("5 432")} <span class="oval s"></span> {MX("5 423")}<br>{MX("98 430")} <span class="oval s"></span> {MX("98 430")}<br>{MX("87 553")} <span class="oval s"></span> {MX("90 876")}')}
  {exo(2, '⭐ سهل', f'أحِط بدائرة العدد الأكبر:<br>{MX("324")} · {MX("2 190")} · {MX("988")}<br>ثم العدد الأصغر:<br>{MX("65 342")} · {MX("9 832")} · {MX("65 243")}')}
  {exo(3, '⭐⭐ متوسط', f'رتّب تصاعديًا:<br>{MX("98 034")} · {MX("90 876")} · {MX("98 430")} · {MX("87 553")}' + dots(2))}
  {exo(4, '⭐⭐ متوسط', f'رتّب تنازليًا:<br>{MX("342 657")} · {MX("398 426")} · {MX("324 000")} · {MX("343 000")}' + dots(2))}
  {exo(5, '⭐⭐⭐ صعب', f'أكمل بعدد مناسب:<br>{MX("45 200")} &lt; <span class="oval s"></span> &lt; {MX("45 300")}<br>{MX("99 998")} &lt; <span class="oval s"></span> &lt; {MX("100 002")}')}
  {exo(6, '⭐⭐⭐ صعب', f'مسألة: ثلاث مدن سكانها {MX("125 640")} و{MX("125 460")} و{MX("126 000")}. مثّلها بنموذج الشريط ثم رتّبها من الأكثر إلى الأقل.<div class="dashcard tall"></div>')}
</div>'''
    return ('الدرس 2 — مقارنة الأعداد الصحيحة وترتيبها', body, 'الوحدة 1 · الأعداد والعمليات')


def L3():
    body = f'''
{badge_row('أتعلّم', 'القاعدة والأمثلة', 'fille')}
<div class="frame has-video">
  <ul>
    <li>اكتب الأعداد بعضها تحت بعض مع <span class="hl">محاذاة المراتب</span> (الآحاد تحت الآحاد، والعشرات تحت العشرات…).</li>
    <li>ارسم خطًا تحت العدد الأخير وابدأ الحساب من الآحاد.</li>
    <li>لا تنسَ <span class="hl">الاحتفاظ</span> في الجمع، و<span class="hl">الاستلاف</span> في الطرح.</li>
  </ul>
  {video_box()}
</div>
{CPA}

{badge_row('أمثّل', 'رابط العدد ونموذج الشريط', 'garcon')}
<div class="frame">
  <div style="display:flex;flex-direction:row-reverse;gap:6mm;align-items:center;justify-content:space-around;flex-wrap:wrap">
    <div style="text-align:center">
      <div style="font-size:10px;font-weight:900;color:#8a4a12">رابط العدد: الكل والجزآن</div>
      {numbond('725', '457', '268')}
      <div style="font-size:10px;font-weight:700">{MX('457 + 268 = 725')} · {MX('725 − 268 = 457')}</div>
    </div>
    <div style="flex:1;min-width:70mm">
      <div style="font-size:10px;font-weight:900;color:#8a4a12;text-align:center;margin-bottom:1mm">نموذج الشريط: الكل = جزء + جزء</div>
      <div class="barmodel">
        <div class="bm-row"><div class="bm-seg c3" style="flex:457">457</div><div class="bm-seg c4" style="flex:268">268</div></div>
        <div class="bm-brace"><span>الكل = 725</span></div>
      </div>
      <div style="height:4mm"></div>
      <div style="display:flex;flex-direction:row-reverse;justify-content:space-around;gap:4mm">
        <div class="vop">4 5 7<br>+ 2 6 8<br><span class="vline">7 2 5</span></div>
        <div class="vop">7 2 5<br>− 2 6 8<br><span class="vline">4 5 7</span></div>
      </div>
    </div>
  </div>
</div>

{badge_row('تمارين', 'من السهل ⭐ إلى الصعب ⭐⭐⭐', 'garcon')}
<div class="cols">
  {exo(1, '⭐ سهل', f'انجز عموديًا:<br>{MX("4 235 + 1 342")} = <span class="oval"></span><br>{MX("6 578 − 2 314")} = <span class="oval"></span><div class="dashcard"></div>')}
  {exo(2, '⭐ سهل', f'أكمل رابط العدد: الكل 500، الجزء الأول 150، الجزء الثاني <span class="oval s"></span><br>ثم اكتب العمليتين: ' + dots(2))}
  {exo(3, '⭐⭐ متوسط', f'انجز عموديًا (انتبه للاحتفاظ):<br>{MX("45 678 + 27 845")} = <span class="oval"></span><br>{MX("80 000 − 34 562")} = <span class="oval"></span><div class="dashcard"></div>')}
  {exo(4, '⭐⭐ متوسط', f'أكمل الرقم الناقص:<br>{MX("3 _ 5 + 2 4 _ = 6 0 2")}<br>{MX("7 _ 4 − 3 2 _ = 4 5 1")}' + dots(1))}
  {exo(5, '⭐⭐⭐ صعب', f'مسألة: باعت مكتبة {MX("1 250")} كتابًا في الشهر الأول و{MX("1 875")} في الثاني. مثّل بنموذج الشريط ثم احسب المجموع.<div class="dashcard tall"></div>')}
  {exo(6, '⭐⭐⭐ صعب', f'مسألة بخطوتين: مع أحمد {MX("5 000")} أوقية. اشترى قميصًا بـ {MX("1 800")} وحذاءً بـ {MX("2 350")}. كم بقي معه؟' + dots(3))}
</div>'''
    return ('الدرس 3 — الجمع (+) والطرح (−)', body, 'الوحدة 1 · الأعداد والعمليات')


def L4():
    body = f'''
{badge_row('أتعلّم', 'القاعدة والأمثلة', 'fille')}
<div class="frame has-video">
  <ul>
    <li>الضرب يُستعمل لجمع نفس العدد عدة مرات، ويُكتب بعاملين ويعطي <span class="hl">جداءً</span>.</li>
    <li>يمكن تغيير ترتيب العددين: {MX('4 × 3 = 3 × 4')}.</li>
    <li>يجب <span class="hl">حفظ جداول الضرب حتى 10</span>، ونضع الضرب عموديًا للأعداد الكبيرة.</li>
    <li>الضرب في 10، 100، 1000: نضيف صفرًا أو صفرين أو ثلاثة أصفار على اليمين.</li>
  </ul>
  {video_box()}
</div>
{CPA}

{badge_row('أمثّل', 'مجموعات متساوية ونموذج الشريط', 'garcon')}
<div class="frame">
  <div style="display:flex;flex-direction:row-reverse;gap:6mm;align-items:center;justify-content:space-around;flex-wrap:wrap">
    <div style="text-align:center">
      <div style="font-size:10px;font-weight:900;color:#8a4a12;margin-bottom:1mm">3 مجموعات في كل واحدة 4 أقراص</div>
      <div style="direction:ltr">
        <span class="pv-disc pv-10">●</span><span class="pv-disc pv-10">●</span><span class="pv-disc pv-10">●</span><span class="pv-disc pv-10">●</span>&nbsp;&nbsp;
        <span class="pv-disc pv-100">●</span><span class="pv-disc pv-100">●</span><span class="pv-disc pv-100">●</span><span class="pv-disc pv-100">●</span>&nbsp;&nbsp;
        <span class="pv-disc pv-1000">●</span><span class="pv-disc pv-1000">●</span><span class="pv-disc pv-1000">●</span><span class="pv-disc pv-1000">●</span>
      </div>
      <div style="font-size:11px;font-weight:800;margin-top:1mm">{MX('4 + 4 + 4 = 4 × 3 = 12')}</div>
    </div>
    <div style="flex:1;min-width:66mm">
      <div style="font-size:10px;font-weight:900;color:#8a4a12;text-align:center;margin-bottom:1mm">نموذج الشريط: 3 أجزاء متساوية</div>
      <div class="barmodel">
        <div class="bm-row"><div class="bm-seg c1" style="flex:1">4</div><div class="bm-seg c1" style="flex:1">4</div><div class="bm-seg c1" style="flex:1">4</div></div>
        <div class="bm-brace"><span>الجداء = 12</span></div>
      </div>
      <div style="height:4mm"></div>
      <div style="text-align:center"><div class="vop">2 4 3<br>× &nbsp;&nbsp; 6<br><span class="vline">1 4 5 8</span></div></div>
    </div>
  </div>
</div>

{badge_row('تمارين', 'من السهل ⭐ إلى الصعب ⭐⭐⭐', 'garcon')}
<div class="cols">
  {exo(1, '⭐ سهل', f'أكمل من جداول الضرب:<br>{MX("7 × 8")} = <span class="oval s"></span> · {MX("6 × 9")} = <span class="oval s"></span><br>{MX("9 × 9")} = <span class="oval s"></span> · {MX("8 × 6")} = <span class="oval s"></span>')}
  {exo(2, '⭐ سهل', f'احسب:<br>{MX("34 × 10")} = <span class="oval s"></span> · {MX("34 × 100")} = <span class="oval s"></span><br>{MX("50 × 1000")} = <span class="oval"></span>')}
  {exo(3, '⭐⭐ متوسط', f'ارسم نموذج الشريط لـ {MX("5 × 35")} ثم احسب.<div class="dashcard tall"></div>')}
  {exo(4, '⭐⭐ متوسط', f'انجز عموديًا:<br>{MX("507 × 8")} = <span class="oval"></span><br>{MX("425 × 32")} = <span class="oval"></span><div class="dashcard"></div>')}
  {exo(5, '⭐⭐⭐ صعب', f'أكمل الرقم الناقص:<br>{MX("_ × 7 = 63")} · {MX("8 × _ = 72")}<br>{MX("12 × _ = 480")} · {MX("_ × 25 = 100")}')}
  {exo(6, '⭐⭐⭐ صعب', 'مسألة: في المدرسة 24 قسمًا، في كل قسم 35 تلميذًا. مثّل بنموذج الشريط ثم احسب عدد التلاميذ.' + dots(3))}
</div>'''
    return ('الدرس 4 — الضرب (×)', body, 'الوحدة 1 · الأعداد والعمليات')


def L5():
    body = f'''
{badge_row('أتعلّم', 'القاعدة والأمثلة', 'fille')}
<div class="frame has-video">
  <ul>
    <li>القسمة تُستعمل للتقسيم أو التوزيع إلى <span class="hl">حصص متساوية</span>.</li>
    <li>تُكتب بـ <span class="hl">مقسوم</span> و<span class="hl">مقسوم عليه</span> وتعطي <span class="hl">خارج القسمة</span>.</li>
    <li>أحيانًا يتبقى <span class="hl">باقٍ</span> إذا لم تكن القسمة تامة.</li>
    <li>للتحقق: الخارج × المقسوم عليه + الباقي = المقسوم.</li>
  </ul>
  {video_box()}
</div>
{CPA}

{badge_row('أمثّل', 'نموذج شريط التوزيع', 'garcon')}
<div class="frame">
  <div style="font-size:11px;font-weight:800;margin-bottom:1mm;text-align:center">نوزّع 12 قرصًا على 3 حصص متساوية: {MX('12 ÷ 3 = 4')}</div>
  <div class="barmodel">
    <div class="bm-brace" style="border-bottom:none;border-top:1.6px solid #33475e;margin:0 0 1mm"><span style="top:-4mm">الكل = 12</span></div>
    <div class="bm-row"><div class="bm-seg c3" style="flex:1">4</div><div class="bm-seg c3" style="flex:1">4</div><div class="bm-seg c3" style="flex:1">4</div></div>
  </div>
  <div class="scallop">مع باقٍ: {MX('17 ÷ 5 = 3')} والباقي {MX('2')} ، لأن {MX('5 × 3 + 2 = 17')}.</div>
</div>

{badge_row('تمارين', 'من السهل ⭐ إلى الصعب ⭐⭐⭐', 'garcon')}
<div class="cols">
  {exo(1, '⭐ سهل', f'احسب:<br>{MX("24 ÷ 6")} = <span class="oval s"></span> · {MX("45 ÷ 9")} = <span class="oval s"></span><br>{MX("63 ÷ 7")} = <span class="oval s"></span> · {MX("81 ÷ 9")} = <span class="oval s"></span>')}
  {exo(2, '⭐ سهل', f'أوجد:<br>نصف {MX("86")} = <span class="oval s"></span> · ثلث {MX("96")} = <span class="oval s"></span><br>ربع {MX("120")} = <span class="oval s"></span>')}
  {exo(3, '⭐⭐ متوسط', f'ارسم نموذج الشريط لتوزيع 96 دفترًا على 8 مجموعات، ثم احسب حصة كل مجموعة.<div class="dashcard tall"></div>')}
  {exo(4, '⭐⭐ متوسط', f'احسب الخارج والباقي ثم تحقق:<br>{MX("75 ÷ 8")} → الخارج <span class="oval s"></span> والباقي <span class="oval s"></span><br>{MX("100 ÷ 7")} → الخارج <span class="oval s"></span> والباقي <span class="oval s"></span>')}
  {exo(5, '⭐⭐⭐ صعب', f'انجز القسمة عموديًا: {MX("156 ÷ 12")}<div class="dashcard tall"></div>')}
  {exo(6, '⭐⭐⭐ صعب', 'مسألة: عند بائع 250 برتقالة يضعها في أكياس، في كل كيس 12 برتقالة. كم كيسًا كاملًا يملأ؟ وكم برتقالة تبقى؟' + dots(3))}
</div>'''
    return ('الدرس 5 — القسمة (÷)', body, 'الوحدة 1 · الأعداد والعمليات')


def L6():
    pies_ex = f'''<div class="pies">
      <div><{pie(240, 6)[1:-6]}></div>
    </div>'''
    body = f'''
{badge_row('أتعلّم', 'القاعدة والأمثلة', 'fille')}
<div class="frame has-video">
  <ul>
    <li>الكسر = <span class="hl">جزء من كلٍّ كامل</span>. مثال: {FR(1,4)} = حصة واحدة من 4 حصص متساوية.</li>
    <li>في الأعلى: <span class="hl">البسط</span> (الحصص المأخوذة) · في الأسفل: <span class="hl">المقام</span> (عدد الحصص الكلية).</li>
    <li>قراءة الكسر: {FR(1,2)} نصف · {FR(1,3)} ثلث · {FR(1,4)} ربع · {FR(3,4)} ثلاثة أرباع · {FR(4,4)} = 1 (كلٌّ كامل).</li>
  </ul>
  {video_box()}
</div>
{CPA}

{badge_row('أمثّل', 'الدوائر والأشرطة الكسرية', 'garcon')}
<div class="frame">
  <div style="display:flex;flex-direction:row-reverse;gap:7mm;align-items:center;justify-content:space-around;flex-wrap:wrap">
    <div style="text-align:center">
      {pie(180, 2)}<div class="pie-lab">{FR(1,2)}</div>
    </div>
    <div style="text-align:center">
      {pie(120, 3, '#b79ddb')}<div class="pie-lab">{FR(1,3)}</div>
    </div>
    <div style="text-align:center">
      {pie(270, 4, '#f5b34c')}<div class="pie-lab">{FR(3,4)}</div>
    </div>
    <div style="flex:1;min-width:60mm">
      <div style="font-size:10px;font-weight:900;color:#8a4a12;text-align:center">الشريط الكسري: {FR(3,4)}</div>
      <div class="fstrip"><div class="fcell fill-o"></div><div class="fcell fill-o"></div><div class="fcell fill-o"></div><div class="fcell"></div></div>
      <div style="font-size:10px;font-weight:900;color:#8a4a12;text-align:center">و {FR(4,4)} = كلٌّ كامل</div>
      <div class="fstrip"><div class="fcell fill-g"></div><div class="fcell fill-g"></div><div class="fcell fill-g"></div><div class="fcell fill-g"></div></div>
    </div>
  </div>
</div>

{badge_row('تمارين', 'من السهل ⭐ إلى الصعب ⭐⭐⭐', 'garcon')}
<div class="cols">
  {exo(1, '⭐ سهل', f'اكتب كسر الجزء الملوّن:<div class="fstrip" style="max-width:44mm"><div class="fcell fill-b"></div><div class="fcell fill-b"></div><div class="fcell"></div></div>= <span class="oval s"></span><div class="fstrip" style="max-width:44mm"><div class="fcell fill-v"></div><div class="fcell"></div><div class="fcell"></div><div class="fcell fill-v"></div><div class="fcell"></div><div class="fcell"></div></div>= <span class="oval s"></span>')}
  {exo(2, '⭐ سهل', f'لوّن حسب الكسر المطلوب:<br>{FR(1,2)}<div class="fstrip" style="max-width:44mm"><div class="fcell"></div><div class="fcell"></div></div>{FR(5,8)}<div class="fstrip" style="max-width:56mm"><div class="fcell"></div><div class="fcell"></div><div class="fcell"></div><div class="fcell"></div><div class="fcell"></div><div class="fcell"></div><div class="fcell"></div><div class="fcell"></div></div>')}
  {exo(3, '⭐⭐ متوسط', f'قارن باستعمال {MX("&gt;")} أو {MX("&lt;")} أو {MX("=")} :<br>{FR(1,2)} <span class="oval s"></span> {FR(2,3)} &nbsp;·&nbsp; {FR(2,5)} <span class="oval s"></span> {FR(2,3)}<br>{FR(1,3)} <span class="oval s"></span> {FR(1,6)} &nbsp;·&nbsp; {FR(4,6)} <span class="oval s"></span> {FR(2,3)}')}
  {exo(4, '⭐⭐ متوسط', f'أكمل الكسور الناقصة على المستقيم العددي:<br>{MX("0 — ¼ — ___ — ¾ — 1")}<br>{MX("0 — ⅕ — ⅖ — ___ — ⅘ — 1")}' + dots(1))}
  {exo(5, '⭐⭐⭐ صعب', f'أوجد المجموع (نفس المقام):<br>{FR(1,4)} + {FR(2,4)} = <span class="oval s"></span> &nbsp;·&nbsp; {FR(3,8)} + {FR(4,8)} = <span class="oval s"></span>')}
  {exo(6, '⭐⭐⭐ صعب', f'مسألة: أكل أحمد {FR(3,8)} من البيتزا وأخته {FR(2,8)}. لوّن الدائرة، ثم اكتب الكسر المأكول والكسر الباقي.<div style="margin-top:1.5mm">{pie(0, 8)}</div>' + dots(1))}
</div>'''
    return ('الدرس 6 — مفهوم الكسر ومقارنته', body, 'الوحدة 2 · الكسور')


def L7():
    body = f'''
{badge_row('أتعلّم', 'القاعدة والأمثلة', 'fille')}
<div class="frame has-video">
  <ul>
    <li>ضرب الكسور يعني ضرب <span class="hl">البسط في البسط</span> و<span class="hl">المقام في المقام</span>.</li>
    <li>ثم <span class="hl">نبسّط</span> إن أمكن.</li>
    <li>لضرب كسر في عدد صحيح نكتب العدد كسرًا مقامه 1: {MX('5 =')} {FR(5,1)}.</li>
  </ul>
  {video_box()}
</div>
{CPA}

{badge_row('أمثّل', 'جزء من جزء: نصف الثلثين', 'garcon')}
<div class="frame">
  <div style="display:flex;flex-direction:row-reverse;gap:7mm;align-items:center;justify-content:space-around;flex-wrap:wrap">
    <div style="flex:1;min-width:62mm">
      <div style="font-size:10.5px;font-weight:800;text-align:center;margin-bottom:1mm">{FR(1,2)} × {FR(2,3)} : آخذ ثلثين ثم آخذ نصفهما</div>
      <div class="fstrip"><div class="fcell fill-g"></div><div class="fcell fill-g"></div><div class="fcell"></div></div>
      <div class="fstrip"><div class="fcell fill-b"></div><div class="fcell"></div><div class="fcell" style="background:repeating-linear-gradient(45deg,#fff,#fff 4px,#eee 4px,#eee 7px)"></div></div>
      <div style="font-size:10px;font-weight:700;text-align:center">النتيجة: {FR(2,6)} = {FR(1,3)}</div>
    </div>
    <div class="scallop" style="flex:1;min-width:58mm;margin:0">
      {FR('2','3')} × {FR('3','4')} = {FR('2 × 3','3 × 4')} = {FR('6','12')} = <b>{FR('1','2')}</b><br>
      نبسّط بقسمة البسط والمقام على 6.
    </div>
  </div>
</div>

{badge_row('تمارين', 'من السهل ⭐ إلى الصعب ⭐⭐⭐', 'garcon')}
<div class="cols">
  {exo(1, '⭐ سهل', f'احسب:<br>{FR(1,2)} × {FR(1,3)} = <span class="oval s"></span> &nbsp;·&nbsp; {FR(1,4)} × {FR(1,2)} = <span class="oval s"></span>')}
  {exo(2, '⭐ سهل', f'احسب:<br>{FR(2,5)} × {FR(3,4)} = <span class="oval s"></span> &nbsp;·&nbsp; {FR(3,7)} × {FR(2,3)} = <span class="oval s"></span>')}
  {exo(3, '⭐⭐ متوسط', f'احسب ثم بسّط:<br>{FR(2,3)} × {FR(3,8)} = <span class="oval"></span><br>{FR(4,5)} × {FR(5,6)} = <span class="oval"></span>')}
  {exo(4, '⭐⭐ متوسط', f'اضرب الكسر في العدد الصحيح:<br>{FR(2,7)} × 3 = <span class="oval s"></span> &nbsp;·&nbsp; {FR(3,4)} × 8 = <span class="oval s"></span>')}
  {exo(5, '⭐⭐⭐ صعب', f'لوّن الشريطين لتمثيل {FR(1,2)} × {FR(1,4)} ثم اكتب النتيجة.<div class="fstrip" style="max-width:52mm"><div class="fcell"></div><div class="fcell"></div><div class="fcell"></div><div class="fcell"></div></div><div class="fstrip" style="max-width:52mm"><div class="fcell"></div><div class="fcell"></div><div class="fcell"></div><div class="fcell"></div><div class="fcell"></div><div class="fcell"></div><div class="fcell"></div><div class="fcell"></div></div>= <span class="oval s"></span>')}
  {exo(6, '⭐⭐⭐ صعب', f'مسألة: أعطت الأم نصف الكعكة لأولادها، فأكل يوسف نصف ما أخذوه. ما الكسر الذي أكله يوسف من الكعكة كلها؟ مثّل بالرسم.' + dots(3))}
</div>'''
    return ('الدرس 7 — ضرب الكسور', body, 'الوحدة 2 · الكسور')


def L8():
    body = f'''
{badge_row('أتعلّم', 'القاعدة والأمثلة', 'fille')}
<div class="frame has-video">
  <ul>
    <li>قسمة كسرين تعني ضرب الكسر الأول في <span class="hl">مقلوب</span> الكسر الثاني.</li>
    <li>📌 مقلوب الكسر: نبدّل بين البسط والمقام. مقلوب {FR(3,4)} هو {FR(4,3)}.</li>
  </ul>
  {video_box()}
</div>
{CPA}

{badge_row('أمثّل', 'كم ربعًا في 3 وحدات؟', 'garcon')}
<div class="frame">
  <div style="font-size:10.5px;font-weight:800;text-align:center;margin-bottom:1mm">{MX('3 ÷')} {FR(1,4)} : كل وحدة فيها 4 أرباع → في 3 وحدات 12 ربعًا</div>
  <div style="display:flex;flex-direction:row-reverse;gap:2mm;justify-content:center">
    <div class="fstrip" style="width:34mm;margin:0"><div class="fcell fill-o"></div><div class="fcell fill-o"></div><div class="fcell fill-o"></div><div class="fcell fill-o"></div></div>
    <div class="fstrip" style="width:34mm;margin:0"><div class="fcell fill-o"></div><div class="fcell fill-o"></div><div class="fcell fill-o"></div><div class="fcell fill-o"></div></div>
    <div class="fstrip" style="width:34mm;margin:0"><div class="fcell fill-o"></div><div class="fcell fill-o"></div><div class="fcell fill-o"></div><div class="fcell fill-o"></div></div>
  </div>
  <div class="scallop">{FR(1,2)} ÷ {FR(3,4)} = {FR(1,2)} × {FR(4,3)} = {FR(4,6)} = <b>{FR(2,3)}</b></div>
</div>

{badge_row('تمارين', 'من السهل ⭐ إلى الصعب ⭐⭐⭐', 'garcon')}
<div class="cols">
  {exo(1, '⭐ سهل', f'اكتب مقلوب كل كسر:<br>{FR(2,3)} → <span class="oval s"></span> · {FR(5,7)} → <span class="oval s"></span> · {MX("4")} → <span class="oval s"></span>')}
  {exo(2, '⭐ سهل', f'احسب: {FR(1,2)} ÷ {FR(1,4)} = <span class="oval s"></span>' + dots(1))}
  {exo(3, '⭐⭐ متوسط', f'احسب ثم بسّط:<br>{FR(3,5)} ÷ {FR(2,3)} = <span class="oval"></span><br>{FR(4,7)} ÷ {FR(2,7)} = <span class="oval"></span>')}
  {exo(4, '⭐⭐ متوسط', f'اقسم العدد الصحيح على الكسر:<br>{MX("6")} ÷ {FR(2,3)} = <span class="oval s"></span> · {MX("4")} ÷ {FR(1,2)} = <span class="oval s"></span>')}
  {exo(5, '⭐⭐⭐ صعب', f'مسألة: عند فاطمة 3 لترات من العصير تصبّها في أكواب سعة الواحد {FR(1,4)} لتر. ارسم الأشرطة ثم احسب عدد الأكواب.<div class="dashcard tall"></div>')}
  {exo(6, '⭐⭐⭐ صعب', f'احسب التعبير المركّب:<br>( {FR(1,2)} × {FR(2,5)} ) ÷ {FR(3,10)} = <span class="oval"></span>' + dots(2))}
</div>'''
    return ('الدرس 8 — قسمة الكسور', body, 'الوحدة 2 · الكسور')


LESSONS_A = [L1, L2, L3, L4, L5, L6, L7, L8]
