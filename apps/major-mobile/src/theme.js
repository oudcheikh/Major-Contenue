// Thème Major 6AF — design system de l'app (style moderne, enfant, RTL).
// Tokens : couleurs, espacements, rayons, ombres, typo — utilisés partout.

export const COLORS = {
  cream: '#f6f7fb',      // fond de page (gris très clair, moderne)
  ink: '#252a37',        // texte principal
  inkSoft: '#7a8194',    // texte secondaire
  royal: '#2563eb',      // bleu Major
  border: '#e9ecf2',     // traits fins
  card: '#ffffff',
  good: '#58cc02',
  bad: '#ff4b4b',
  gold: '#ffc800',
}

// Ombre douce commune à toutes les cartes.
export const SHADOW = {
  shadowColor: '#101828',
  shadowOpacity: 0.06,
  shadowRadius: 12,
  shadowOffset: { width: 0, height: 4 },
  elevation: 3,
}

export const RADIUS = { md: 16, lg: 20, xl: 24 }

export const SUBJECT_META = {
  math:         { color: '#fb923c', bg: '#fff7ed', icon: '📐', label: 'Mathématiques',    labelAr: 'الرياضيات',          isArabic: false },
  french:       { color: '#2563eb', bg: '#eff6ff', icon: '📖', label: 'Français',          labelAr: 'الفرنسية',           isArabic: false },
  science:      { color: '#34d399', bg: '#ecfdf5', icon: '🔬', label: 'Sciences',          labelAr: 'العلوم',             isArabic: false },
  arabe:        { color: '#06803C', bg: '#d1fae5', icon: '🕌', label: 'Arabe',             labelAr: 'اللغة العربية',      isArabic: true },
  histoire_geo: { color: '#8b5cf6', bg: '#ede9fe', icon: '🌍', label: 'Histoire-Géo',      labelAr: 'التاريخ والجغرافيا', isArabic: true },
  islamique:    { color: '#059669', bg: '#ecfdf5', icon: '☪️', label: 'Islamique',         labelAr: 'التربية الإسلامية',  isArabic: true },
  'math6-ar':   { color: '#fb923c', bg: '#fff7ed', icon: '📐', label: 'Mathématiques 6AF', labelAr: 'الرياضيات',          isArabic: true },
  'sci6-ar':    { color: '#34d399', bg: '#ecfdf5', icon: '🔬', label: 'Sciences 6AF',      labelAr: 'العلوم الطبيعية',    isArabic: true },
  ar6:          { color: '#7c3aed', bg: '#f3f0ff', icon: '📘', label: 'Arabe 6AF',         labelAr: 'اللغة العربية',      isArabic: true },
  isl6:         { color: '#0d9488', bg: '#e7f8f4', icon: '☪️', label: 'Islamique 6AF',     labelAr: 'التربية الإسلامية',  isArabic: true },
  hg6:          { color: '#b45309', bg: '#fdf3e3', icon: '🏰', label: 'Histoire-Géo 6AF',  labelAr: 'التاريخ والجغرافيا', isArabic: true },
  civ6:         { color: '#0f7b3a', bg: '#e8f7ee', icon: '🤝', label: 'Civique 6AF',       labelAr: 'التربية المدنية',    isArabic: true },
}

export const LEVELS = [
  { min: 0,  max: 39,  label: 'Débutant',      labelAr: 'مبتدئ',  color: '#94a3b8', bg: '#f1f5f9', icon: '🌱', stars: 1 },
  { min: 40, max: 69,  label: 'Intermédiaire', labelAr: 'متوسط',  color: '#fb923c', bg: '#fff7ed', icon: '⭐', stars: 2 },
  { min: 70, max: 84,  label: 'Avancé',        labelAr: 'متقدم',  color: '#2563eb', bg: '#eff6ff', icon: '🚀', stars: 2 },
  { min: 85, max: 100, label: 'Expert',        labelAr: 'خبير',   color: '#eab308', bg: '#fefce8', icon: '🏆', stars: 3 },
]

export function getLevel(pct) {
  return LEVELS.find((l) => pct >= l.min && pct <= l.max) || LEVELS[0]
}

export function getEncouragement(pct, isArabic) {
  if (isArabic) {
    if (pct === 100) return { title: 'ممتاز ! 🏆', body: 'نتيجة مثالية! أنت جاهز للمسابقة 🇲🇷' }
    if (pct >= 80)   return { title: 'رائع ! 🚀',  body: 'عمل ممتاز! واصل هذا المستوى.' }
    if (pct >= 60)   return { title: 'أحسنت ! ⭐', body: 'أنت تتقدم بشكل جيد، استمر!' }
    if (pct >= 40)   return { title: 'جيد ! 💪',   body: 'راجع الأخطاء وأعد المحاولة.' }
    return           { title: 'لا تستسلم ! ❤️',   body: 'المراجعة تصنع الفرق. أنت قادر!' }
  }
  if (pct === 100) return { title: 'Parfait ! 🏆',   body: 'Score parfait ! Tu es prêt pour le concours 🇲🇷' }
  if (pct >= 80)   return { title: 'Excellent ! 🚀',  body: 'Très bon travail ! Continue comme ça.' }
  if (pct >= 60)   return { title: 'Bien joué ! ⭐',  body: 'Tu progresses bien. Encore un effort !' }
  if (pct >= 40)   return { title: 'Bon effort ! 💪', body: 'Revois les erreurs et réessaie !' }
  return           { title: 'Ne lâche pas ! ❤️',      body: 'Chaque tentative te rend plus fort !' }
}
