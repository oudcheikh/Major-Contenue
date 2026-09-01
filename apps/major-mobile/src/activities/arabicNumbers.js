// Lecture des nombres en lettres arabes (0 → 999 999 999 999),
// suivant la convention du cahier : « 32 مليارًا و47 مليونًا و562 ألفًا و73 »
// → مئتان وخمسة وأربعون ألفًا وسبعة وستون.

const ONES = ['', 'واحد', 'اثنان', 'ثلاثة', 'أربعة', 'خمسة', 'ستة', 'سبعة', 'ثمانية', 'تسعة']
const TEENS = ['عشرة', 'أحد عشر', 'اثنا عشر', 'ثلاثة عشر', 'أربعة عشر', 'خمسة عشر', 'ستة عشر', 'سبعة عشر', 'ثمانية عشر', 'تسعة عشر']
const TENS = ['', '', 'عشرون', 'ثلاثون', 'أربعون', 'خمسون', 'ستون', 'سبعون', 'ثمانون', 'تسعون']
const HUNDREDS = ['', 'مئة', 'مئتان', 'ثلاثمئة', 'أربعمئة', 'خمسمئة', 'ستمئة', 'سبعمئة', 'ثمانمئة', 'تسعمئة']

// Groupes de lecture (مجموعات) : nom selon le nombre (1, 2, 3-10, 11+).
const SCALES = [
  null, // groupe des unités : pas de nom
  { one: 'ألف', two: 'ألفان', few: 'آلاف', many: 'ألفًا' },
  { one: 'مليون', two: 'مليونان', few: 'ملايين', many: 'مليونًا' },
  { one: 'مليار', two: 'ملياران', few: 'مليارات', many: 'مليارًا' },
]

// 1..999 en lettres.
function threeDigits(n) {
  const h = Math.floor(n / 100)
  const r = n % 100
  const parts = []
  if (h) parts.push(HUNDREDS[h])
  if (r) {
    if (r < 10) parts.push(ONES[r])
    else if (r < 20) parts.push(TEENS[r - 10])
    else {
      const u = r % 10
      if (u) parts.push(ONES[u])
      parts.push(TENS[Math.floor(r / 10)])
    }
  }
  return parts.join(' و')
}

// Nom du groupe accordé à son nombre : ألف / ألفان / ثلاثة آلاف / خمسة وأربعون ألفًا.
function scaleWords(count, scale) {
  if (count === 1) return scale.one
  if (count === 2) return scale.two
  const words = threeDigits(count)
  if (count >= 3 && count <= 10) return `${words} ${scale.few}`
  if (count % 100 === 0) return `${words} ${scale.one}`
  return `${words} ${scale.many}`
}

export function toArabicWords(n) {
  if (!Number.isFinite(n) || n < 0) return ''
  if (n === 0) return 'صفر'
  // Découpage en groupes de 3 chiffres à partir de la droite.
  const groups = []
  let rest = Math.floor(n)
  while (rest > 0) {
    groups.push(rest % 1000)
    rest = Math.floor(rest / 1000)
  }
  const parts = []
  for (let i = groups.length - 1; i >= 0; i--) {
    const count = groups[i]
    if (!count) continue
    parts.push(i === 0 ? threeDigits(count) : scaleWords(count, SCALES[i]))
  }
  return parts.join(' و')
}

// « 245067 » → « 245 067 » (groupes de 3, espace fine insécable).
export function groupDigits(str) {
  return str.replace(/\B(?=(\d{3})+(?!\d))/g, ' ')
}
