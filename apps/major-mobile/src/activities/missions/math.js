// Missions des activités maths u04 → u31 — générées aléatoirement à chaque
// partie (rejouables). Énoncés mauritanisés (MRU), terminologie du cahier.
// Chaque générateur → 5 missions { q, a, hint, suffix?, dec? } (ComputeGame)
// ou { q, choices, correct, hint, visual? } (ChoiceGame).

const ri = (a, b) => a + Math.floor(Math.random() * (b - a + 1))
const pick = (arr) => arr[ri(0, arr.length - 1)]

// u04 — الضرب (multiplication posée)
export function u04() {
  return Array.from({ length: 5 }, (_, i) => {
    const a = ri(12, i < 2 ? 99 : 499)
    const b = ri(3, i < 3 ? 9 : 12)
    return {
      q: `أحسب: ${a} × ${b}`,
      a: a * b,
      hint: `فكّك العدد: ${a} × ${b} = (${Math.floor(a / 10) * 10} × ${b}) + (${a % 10} × ${b})`,
    }
  })
}

// u05 — القسمة (division exacte)
export function u05() {
  return Array.from({ length: 5 }, (_, i) => {
    const b = ri(3, i < 2 ? 9 : 12)
    const q = ri(6, i < 3 ? 40 : 90)
    return {
      q: `أحسب: ${b * q} ÷ ${b}`,
      a: q,
      hint: `ابحث عن العدد الذي إذا ضربته في ${b} تحصل على ${b * q}`,
    }
  })
}

// u06 — قياس الأطوال (conversions)
export function u06() {
  const convs = [
    () => { const n = ri(2, 9); return { q: `حوّل: ${n} km = ؟ m`, a: n * 1000, suffix: 'm', hint: '1 km = 1000 m — أضرب في 1000' } },
    () => { const n = ri(2, 9); return { q: `حوّل: ${n} m = ؟ cm`, a: n * 100, suffix: 'cm', hint: '1 m = 100 cm — أضرب في 100' } },
    () => { const n = ri(2, 50); return { q: `حوّل: ${n} cm = ؟ mm`, a: n * 10, suffix: 'mm', hint: '1 cm = 10 mm — أضرب في 10' } },
    () => { const n = ri(2, 9); return { q: `حوّل: ${n}000 m = ؟ km`, a: n, suffix: 'km', hint: '1000 m = 1 km — أقسم على 1000' } },
    () => { const n = ri(2, 9); return { q: `حوّل: ${n} km و ${ri(1, 9)}00 m... بل الأسهل: ${n * 100} cm = ؟ m`, a: n, suffix: 'm', hint: '100 cm = 1 m — أقسم على 100' } },
  ]
  return convs.map((f) => f())
}

// u07 — المستقيمات (visuel)
export function u07() {
  const kinds = ['par', 'sec', 'perp', pick(['par', 'sec']), pick(['perp', 'par'])]
  return kinds.map((kind) => ({
    q: 'انظر إلى المستقيمين — ما وضعهما؟',
    visual: { type: 'lines', kind },
    choices: ['متوازيان', 'متقاطعان', 'متعامدان'],
    correct: kind === 'par' ? 0 : kind === 'sec' ? 1 : 2,
    hint: kind === 'par' ? 'لا يلتقيان أبدًا مهما امتدّا' : kind === 'perp' ? 'يتقاطعان ويكوّنان زاوية قائمة' : 'يلتقيان في نقطة واحدة',
  }))
}

// u08 — مقارنة الأعداد
export function u08() {
  return Array.from({ length: 5 }, (_, i) => {
    const d = i < 2 ? 4 : 6
    let a = ri(Math.pow(10, d - 1), Math.pow(10, d) - 1)
    let b = i === 2 ? a : ri(Math.pow(10, d - 1), Math.pow(10, d) - 1)
    const correct = a > b ? 0 : a < b ? 1 : 2
    return {
      q: 'قارن بين العددين:',
      visual: { type: 'big', text: `${a}  ؟  ${b}` },
      choices: ['>', '<', '='],
      correct,
      hint: 'أقارن عدد الأرقام أولًا، فإن تساوى قارنت رقمًا رقمًا من اليسار',
    }
  })
}

// u09 — الكتل
export function u09() {
  const convs = [
    () => { const n = ri(2, 9); return { q: `حوّل: ${n} kg = ؟ g`, a: n * 1000, suffix: 'g', hint: '1 kg = 1000 g' } },
    () => { const n = ri(2, 9); return { q: `حوّل: ${n} طن = ؟ kg`, a: n * 1000, suffix: 'kg', hint: '1 طن = 1000 kg' } },
    () => { const n = ri(2, 9); return { q: `حوّل: ${n} قنطار = ؟ kg`, a: n * 100, suffix: 'kg', hint: '1 قنطار = 100 kg' } },
    () => { const n = ri(2, 9); return { q: `حوّل: ${n}000 g = ؟ kg`, a: n, suffix: 'kg', hint: '1000 g = 1 kg — أقسم على 1000' } },
    () => { const n = ri(1, 5); return { q: `اشترت أمّ سلمى ${n} kg و500 g من اللحم. كم غرامًا اشترت؟`, a: n * 1000 + 500, suffix: 'g', hint: `${n} kg = ${n * 1000} g ثم أضف 500` } },
  ]
  return convs.map((f) => f())
}

// u10 — الزوايا (visuel)
export function u10() {
  const degs = [ri(20, 60), 90, ri(110, 160), ri(25, 70), pick([90, ri(115, 150)])]
  return degs.map((deg) => ({
    q: 'انظر إلى الزاوية — ما نوعها؟',
    visual: { type: 'angle', deg },
    choices: ['حادة', 'قائمة', 'منفرجة'],
    correct: deg < 90 ? 0 : deg === 90 ? 1 : 2,
    hint: 'الحادة أصغر من القائمة (90°)، والمنفرجة أكبر منها',
  }))
}

// 3 choix uniques : la bonne réponse + 2 distracteurs (dédupliqués).
function fractionChoices(goodN, goodD, candidates) {
  const good = `${goodN}/${goodD}`
  const opts = [good]
  const fallbacks = [`${goodN + 1}/${goodD}`, `${goodN}/${goodD + 1}`, `${goodN + 2}/${goodD}`, `${goodN}/${goodD + 2}`]
  for (const cand of [...candidates, ...fallbacks]) {
    if (opts.length >= 3) break
    if (!opts.includes(cand)) opts.push(cand)
  }
  const shuffled = opts.map((o, i) => ({ o, i })).sort(() => Math.random() - 0.5)
  return { choices: shuffled.map((x) => x.o), correct: shuffled.findIndex((x) => x.i === 0) }
}

// u11 — ضرب الكسور
export function u11() {
  return Array.from({ length: 5 }, () => {
    const n1 = ri(1, 3), d1 = ri(n1 + 1, 5), n2 = ri(1, 3), d2 = ri(n2 + 1, 5)
    const { choices, correct } = fractionChoices(n1 * n2, d1 * d2, [`${n1 * d2}/${d1 * n2}`, `${n1 + n2}/${d1 + d2}`])
    return {
      q: `أحسب: ${n1}/${d1} × ${n2}/${d2}`,
      choices,
      correct,
      hint: 'البسط × البسط، والمقام × المقام',
    }
  })
}

// u12 — قسمة الكسور
export function u12() {
  return Array.from({ length: 5 }, () => {
    const n1 = ri(1, 3), d1 = ri(n1 + 1, 5), n2 = ri(1, 3), d2 = ri(n2 + 1, 5)
    const { choices, correct } = fractionChoices(n1 * d2, d1 * n2, [`${n1 * n2}/${d1 * d2}`, `${d1 * d2}/${n1 * n2}`])
    return {
      q: `أحسب: ${n1}/${d1} ÷ ${n2}/${d2}`,
      choices,
      correct,
      hint: 'القسمة = الضرب في مقلوب الكسر الثاني',
    }
  })
}

// u13 — الشراء والبيع (prix MRU réalistes)
export function u13() {
  const items = ['كيس أرز', 'ثوب', 'خروف', 'هاتف', 'صندوق تمر']
  return Array.from({ length: 5 }, (_, i) => {
    const achat = ri(15, 80) * 100
    const gain = ri(5, 30) * 100
    const vente = achat + gain
    if (i % 2 === 0) {
      return {
        q: `اشترى تاجر ${pick(items)} بـ ${achat} أوقية وباعه بـ ${vente} أوقية. ما ربحه؟`,
        a: gain, suffix: 'أوقية',
        hint: 'الربح = ثمن البيع − ثمن الشراء',
      }
    }
    return {
      q: `باع تاجر ${pick(items)} بـ ${vente} أوقية وكان ربحه ${gain} أوقية. بكم اشتراه؟`,
      a: achat, suffix: 'أوقية',
      hint: 'ثمن الشراء = ثمن البيع − الربح',
    }
  })
}

// u14 — الأعداد العشرية
export function u14() {
  return Array.from({ length: 5 }, (_, i) => {
    if (i < 2) {
      const a = ri(1, 9) + ri(1, 9) / 10, b = ri(1, 9) + ri(1, 9) / 10
      const s = Math.round((a + b) * 10) / 10
      return { q: `أحسب: ${a} + ${b}`, a: s, dec: true, hint: 'أصفّ الفاصلة تحت الفاصلة ثم أجمع' }
    }
    if (i < 4) {
      const n = ri(1, 9) + ri(1, 9) / 10
      return { q: `أحسب: ${n} × 10`, a: Math.round(n * 100) / 10, dec: true, hint: 'الضرب في 10 يزحزح الفاصلة رقمًا واحدًا نحو اليمين' }
    }
    const a = ri(5, 9) + ri(5, 9) / 10, b = ri(1, 4) + ri(1, 4) / 10
    return { q: `أحسب: ${a} − ${b}`, a: Math.round((a - b) * 10) / 10, dec: true, hint: 'أصفّ الفاصلة تحت الفاصلة ثم أطرح' }
  })
}

// u15 — النسب المئوية
export function u15() {
  return Array.from({ length: 5 }, () => {
    const pct = pick([10, 20, 25, 50, 75])
    const base = ri(2, 9) * (pct === 25 || pct === 75 ? 40 : 20)
    return {
      q: `أحسب ${pct}% من ${base}`,
      a: (base * pct) / 100,
      hint: `${pct}% من العدد = العدد × ${pct} ÷ 100`,
    }
  })
}

// u16 — قابلية القسمة
export function u16() {
  return Array.from({ length: 5 }, () => {
    const div = pick([2, 3, 5, 9])
    const yes = Math.random() < 0.5
    let n = ri(100, 999)
    if (div === 2) n = yes ? n - (n % 2) : n - (n % 2) + 1
    if (div === 5) n = yes ? n - (n % 5) : n - (n % 5) + pick([1, 2, 3, 4])
    if (div === 3 || div === 9) n = yes ? n - (n % div) : (n % div === 0 ? n + 1 : n)
    const isDiv = n % div === 0
    return {
      q: `هل العدد ${n} يقبل القسمة على ${div}؟`,
      choices: ['نعم ✅', 'لا ❌'],
      correct: isDiv ? 0 : 1,
      hint: div === 2 ? 'يقبل القسمة على 2 إذا كان آخر رقم زوجيًا'
        : div === 5 ? 'يقبل القسمة على 5 إذا انتهى بـ 0 أو 5'
        : `يقبل القسمة على ${div} إذا كان مجموع أرقامه يقبل القسمة على ${div}`,
    }
  })
}

// u17 — الكسور المتكافئة
export function u17() {
  return Array.from({ length: 5 }, () => {
    const n = ri(1, 4), d = ri(n + 1, 6), k = ri(2, 5)
    return {
      q: `أكمل الكسر المكافئ: ${n}/${d} = ؟/${d * k}`,
      a: n * k,
      hint: `المقام ضُرب في ${k}، فاضرب البسط في ${k} أيضًا`,
    }
  })
}

// u18 — الضرب في 10 و100 و1000
export function u18() {
  return Array.from({ length: 5 }, () => {
    const n = ri(3, 99)
    const m = pick([10, 100, 1000])
    return {
      q: `أحسب: ${n} × ${m}`,
      a: n * m,
      hint: `أضيف ${String(m).length - 1} ${String(m).length - 1 === 1 ? 'صفرًا' : 'أصفار'} على يمين العدد`,
    }
  })
}

// u19 — التقاسيم غير المتساوية
export function u19() {
  const pairs = ['أحمد وفاطمة', 'سيدي ومريم', 'المختار وزينب']
  return Array.from({ length: 5 }, () => {
    const small = ri(10, 40) * 10
    const diff = ri(2, 8) * 10
    const total = 2 * small + diff
    const [n1] = pairs
    const who = pick(pairs)
    return {
      q: `مع ${who} معًا ${total} أوقية، والأول عنده ${diff} أوقية أكثر من الثاني. كم عند الأول؟`,
      a: small + diff, suffix: 'أوقية',
      hint: `(المجموع + الفرق) ÷ 2 = (${total} + ${diff}) ÷ 2`,
    }
  })
}

// u20 — الزمن
export function u20() {
  return Array.from({ length: 5 }, (_, i) => {
    if (i < 2) {
      const h = ri(1, 4)
      const extra = pick([0, 15, 30, 45])
      return {
        q: `كم دقيقة في ${h} ${h === 1 ? 'ساعة' : 'ساعات'}${extra ? ` و${extra} دقيقة` : ''}؟`,
        a: h * 60 + extra, suffix: 'min',
        hint: '1 ساعة = 60 دقيقة',
      }
    }
    if (i < 4) {
      const m = pick([120, 150, 180, 240])
      return { q: `${m} دقيقة = ؟ ساعة${m % 60 ? ' (بالفاصلة)' : ''}`, a: m / 60, dec: m % 60 !== 0, suffix: 'h', hint: 'أقسم على 60' }
    }
    const start = ri(8, 10), dur = pick([20, 30, 40])
    return {
      q: `بدأ الدرس الساعة ${start}:00 ودام ${dur} دقيقة. في أي دقيقة انتهى؟ (أكتب الدقائق فقط)`,
      a: dur, suffix: `أي ${start}:${dur}`,
      hint: `أضف ${dur} دقيقة إلى ${start}:00`,
    }
  })
}

// u21 — التناسبية
export function u21() {
  const items = ['أقلام', 'دفاتر', 'كراريس', 'خبزات']
  return Array.from({ length: 5 }, () => {
    const unit = ri(2, 9) * 10
    const n1 = ri(2, 5), n2 = ri(n1 + 1, 9)
    const item = pick(items)
    return {
      q: `${n1} ${item} ثمنها ${n1 * unit} أوقية. ما ثمن ${n2} ${item}؟`,
      a: n2 * unit, suffix: 'أوقية',
      hint: `أجد ثمن الواحد أولًا: ${n1 * unit} ÷ ${n1} = ${unit}`,
    }
  })
}

// u22 — السرعة والمسافة والزمن
export function u22() {
  return Array.from({ length: 5 }, (_, i) => {
    const v = pick([60, 70, 80, 90, 100])
    const t = ri(2, 5)
    if (i % 3 === 0) return { q: `قطعت سيارة ${v * t} km في ${t} ساعات. ما سرعتها؟`, a: v, suffix: 'km/h', hint: 'السرعة = المسافة ÷ الزمن' }
    if (i % 3 === 1) return { q: `سيارة سرعتها ${v} km/h سارت ${t} ساعات. كم قطعت؟`, a: v * t, suffix: 'km', hint: 'المسافة = السرعة × الزمن' }
    return { q: `قطعت شاحنة ${v * t} km بسرعة ${v} km/h. كم ساعة استغرقت؟`, a: t, suffix: 'h', hint: 'الزمن = المسافة ÷ السرعة' }
  })
}

// u23 — السلم
export function u23() {
  return Array.from({ length: 5 }, () => {
    const cm = ri(2, 8)
    const scale = pick([100000, 200000, 500000])
    return {
      q: `خريطة سلمها 1/${scale}. المسافة عليها ${cm} cm — كم km في الواقع؟`,
      a: (cm * scale) / 100000, suffix: 'km',
      hint: `المسافة الحقيقية = ${cm} × ${scale} cm، ثم أحوّل إلى km (÷ 100000)`,
    }
  })
}

// u24 — الفائدة السنوية
export function u24() {
  return Array.from({ length: 5 }, () => {
    const cap = ri(2, 9) * 10000
    const rate = pick([2, 3, 5, 10])
    return {
      q: `رأسمال ${cap} أوقية بفائدة ${rate}% في السنة. ما الفائدة السنوية؟`,
      a: (cap * rate) / 100, suffix: 'أوقية',
      hint: `الفائدة = رأس المال × ${rate} ÷ 100`,
    }
  })
}

// u25 — الفواصل (arbres et intervalles)
export function u25() {
  return Array.from({ length: 5 }, (_, i) => {
    const gap = pick([5, 10, 20, 25])
    const n = ri(4, 12)
    if (i % 2 === 0) {
      return {
        q: `طريق مستقيم طوله ${gap * n} m، نغرس نخلة كل ${gap} m (مع الطرفين). كم نخلة نغرس؟`,
        a: n + 1,
        hint: 'عدد الأشجار = عدد الفواصل + 1 (بسبب الطرفين)',
      }
    }
    return {
      q: `حول حديقة دائرية محيطها ${gap * n} m نغرس شجرة كل ${gap} m. كم شجرة؟`,
      a: n,
      hint: 'في الشكل المغلق: عدد الأشجار = عدد الفواصل',
    }
  })
}

// u26 — الكتلة القائمة والصافية والفارغ
export function u26() {
  return Array.from({ length: 5 }, (_, i) => {
    const tare = ri(1, 5) * 50
    const net = ri(4, 18) * 50
    if (i % 3 === 0) return { q: `صندوق تمر: الكتلة القائمة ${net + tare} g والفارغ ${tare} g. ما الكتلة الصافية؟`, a: net, suffix: 'g', hint: 'الصافية = القائمة − الفارغ' }
    if (i % 3 === 1) return { q: `الكتلة الصافية ${net} g والفارغ ${tare} g. ما الكتلة القائمة؟`, a: net + tare, suffix: 'g', hint: 'القائمة = الصافية + الفارغ' }
    return { q: `الكتلة القائمة ${net + tare} g والصافية ${net} g. ما كتلة الفارغ؟`, a: tare, suffix: 'g', hint: 'الفارغ = القائمة − الصافية' }
  })
}

// u27 — المثلثات
export function u27() {
  return Array.from({ length: 5 }, () => {
    const b = ri(3, 12) * 2
    const h = ri(3, 10)
    return {
      q: `مثلث قاعدته ${b} cm وارتفاعه ${h} cm. ما مساحته؟`,
      a: (b * h) / 2, suffix: 'cm²',
      hint: 'مساحة المثلث = (القاعدة × الارتفاع) ÷ 2',
    }
  })
}

// u28 — الأشكال الرباعية
export function u28() {
  return Array.from({ length: 5 }, (_, i) => {
    const L = ri(6, 15), l = ri(3, L - 1)
    if (i % 2 === 0) return { q: `مستطيل طوله ${L} cm وعرضه ${l} cm. ما مساحته؟`, a: L * l, suffix: 'cm²', hint: 'المساحة = الطول × العرض' }
    return { q: `مستطيل طوله ${L} cm وعرضه ${l} cm. ما محيطه؟`, a: 2 * (L + l), suffix: 'cm', hint: 'المحيط = (الطول + العرض) × 2' }
  })
}

// u29 — القياسات الزراعية
export function u29() {
  const convs = [
    () => { const n = ri(2, 9); return { q: `حوّل: ${n} هكتار = ؟ آر`, a: n * 100, suffix: 'آر', hint: '1 هكتار = 100 آر' } },
    () => { const n = ri(2, 9); return { q: `حوّل: ${n} آر = ؟ m²`, a: n * 100, suffix: 'm²', hint: '1 آر = 100 m²' } },
    () => { const n = ri(2, 9); return { q: `حوّل: ${n} هكتار = ؟ m²`, a: n * 10000, suffix: 'm²', hint: '1 هكتار = 10000 m²' } },
    () => { const n = ri(2, 9); return { q: `حقل مستطيل ${n * 100} m × 100 m. ما مساحته بالهكتار؟`, a: n, suffix: 'هكتار', hint: 'المساحة بالـ m² ÷ 10000 = هكتار' } },
    () => { const n = ri(200, 900); return { q: `حوّل: ${n * 100} m² = ؟ آر`, a: n, suffix: 'آر', hint: '100 m² = 1 آر' } },
  ]
  return convs.map((f) => f())
}

// u30 — الدائرة والقرص
export function u30() {
  return Array.from({ length: 5 }, (_, i) => {
    const r = pick([10, 20, 5, 100])
    if (i % 2 === 0) {
      return {
        q: `دائرة نصف قطرها ${r} cm (π = 3.14). ما محيطها؟`,
        a: Math.round(2 * 3.14 * r * 100) / 100, dec: true, suffix: 'cm',
        hint: 'المحيط = 2 × π × نصف القطر',
      }
    }
    return {
      q: `قرص نصف قطره ${r} cm (π = 3.14). ما مساحته؟`,
      a: Math.round(3.14 * r * r * 100) / 100, dec: true, suffix: 'cm²',
      hint: 'المساحة = π × نصف القطر × نصف القطر',
    }
  })
}

// u31 — المجسمات والحجوم
export function u31() {
  return Array.from({ length: 5 }, (_, i) => {
    if (i < 3) {
      const L = ri(3, 8), l = ri(2, 6), h = ri(2, 5)
      return { q: `متوازي مستطيلات: الطول ${L} cm، العرض ${l} cm، الارتفاع ${h} cm. ما حجمه؟`, a: L * l * h, suffix: 'cm³', hint: 'الحجم = الطول × العرض × الارتفاع' }
    }
    if (i === 3) {
      const c = ri(2, 6)
      return { q: `مكعب حرفه ${c} cm. ما حجمه؟`, a: c * c * c, suffix: 'cm³', hint: 'حجم المكعب = الحرف × الحرف × الحرف' }
    }
    const n = ri(2, 9)
    return { q: `حوّل: ${n} لتر = ؟ cm³`, a: n * 1000, suffix: 'cm³', hint: '1 لتر = 1000 cm³ = 1 dm³' }
  })
}
