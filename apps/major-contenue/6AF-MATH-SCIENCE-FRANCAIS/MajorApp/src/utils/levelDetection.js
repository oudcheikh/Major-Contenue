import { LEVELS } from '../theme';

/**
 * Calcule le score global à partir des stats toutes matières confondues.
 * Retourne un objet { pct, level, nextLevel, progressToNext }
 */
export function computeGlobalLevel(stats) {
  const subjects = Object.values(stats);
  const totalDone = subjects.reduce((s, x) => s + x.done, 0);
  const totalCorrect = subjects.reduce((s, x) => s + x.correct, 0);

  if (totalDone === 0) return { pct: 0, level: LEVELS[0], nextLevel: LEVELS[1], progressToNext: 0 };

  const pct = Math.round((totalCorrect / totalDone) * 100);
  const level = LEVELS.find((l) => pct >= l.min && pct <= l.max) || LEVELS[0];
  const levelIdx = LEVELS.indexOf(level);
  const nextLevel = levelIdx < LEVELS.length - 1 ? LEVELS[levelIdx + 1] : null;

  let progressToNext = 100;
  if (nextLevel) {
    const range = nextLevel.min - level.min;
    const done = pct - level.min;
    progressToNext = Math.min(100, Math.round((done / range) * 100));
  }

  return { pct, level, nextLevel, progressToNext };
}

/**
 * Calcule le score pour une matière spécifique.
 */
export function computeSubjectLevel(subjectStats) {
  const { done, correct } = subjectStats;
  if (done === 0) return { pct: 0, level: LEVELS[0] };
  const pct = Math.round((correct / done) * 100);
  const level = LEVELS.find((l) => pct >= l.min && pct <= l.max) || LEVELS[0];
  return { pct, level };
}

/**
 * Retourne un message d'encouragement personnalisé selon le score.
 */
export function getEncouragementMessage(pct, subjectLabel, isArabic = false) {
  if (isArabic) {
    if (pct === 100) return { title: 'ممتاز ! 🏆', body: `نتيجة مثالية في ${subjectLabel}! أنت جاهز للمسابقة.` };
    if (pct >= 85) return { title: 'رائع ! 🚀', body: `عمل ممتاز في ${subjectLabel}! واصل هذا المستوى.` };
    if (pct >= 70) return { title: 'أحسنت ! ⭐', body: `أنت تتقن ${subjectLabel} جيداً. مزيد من الجهد للوصول إلى التميز.` };
    if (pct >= 50) return { title: 'جيد ! 💪', body: `أنت تتقدم في ${subjectLabel}. راجع الأخطاء وأعد المحاولة.` };
    if (pct >= 30) return { title: 'استمر ! 🌱', body: `${subjectLabel} يحتاج مزيداً من التدريب. كل تمرين يجعلك أفضل.` };
    return { title: 'لا تستسلم ! ❤️', body: `${subjectLabel} صعب لكن المراجعة تصنع الفرق. أنت قادر!` };
  }
  if (pct === 100) return { title: 'Parfait ! 🏆', body: `Score parfait en ${subjectLabel} ! Tu es prêt pour le concours.` };
  if (pct >= 85) return { title: 'Excellent ! 🚀', body: `Très bon travail en ${subjectLabel} ! Continue sur cette lancée.` };
  if (pct >= 70) return { title: 'Bien joué ! ⭐', body: `Tu maîtrises bien ${subjectLabel}. Encore un peu d'effort pour atteindre l'excellence.` };
  if (pct >= 50) return { title: 'Bon effort ! 💪', body: `Tu progresses en ${subjectLabel}. Revois les exercices ratés et réessaie.` };
  if (pct >= 30) return { title: 'Continue ! 🌱', body: `${subjectLabel} demande encore de la pratique. Chaque exercice te fait progresser.` };
  return { title: 'Ne lâche pas ! ❤️', body: `${subjectLabel} peut sembler difficile, mais révise tes cours et tu verras la différence.` };
}

/**
 * Donne une liste de conseils de révision selon les sujets faibles.
 */
export function getRevisionTips(stats) {
  const tips = [];
  const labels = {
    french:       { fr: 'Français',              ar: 'الفرنسية',           isArabic: false },
    math:         { fr: 'Mathématiques',          ar: 'الرياضيات',          isArabic: false },
    science:      { fr: 'Sciences',               ar: 'العلوم',             isArabic: false },
    arabe:        { fr: 'Arabe',                  ar: 'اللغة العربية',     isArabic: true },
    histoire_geo: { fr: 'Histoire-Géo',           ar: 'التاريخ والجغرافيا', isArabic: true },
    islamique:    { fr: 'Islamique',              ar: 'التربية الإسلامية', isArabic: true },
  };

  for (const [key, data] of Object.entries(stats)) {
    const meta = labels[key];
    if (!meta) continue;
    const displayLabel = meta.isArabic ? meta.ar : meta.fr;
    if (data.done === 0) {
      tips.push({ subject: key, label: displayLabel, isArabic: meta.isArabic, tip: meta.isArabic ? 'لم تبدأ بعد في هذه المادة. ابدأ الآن!' : 'Tu n\'as pas encore pratiqué cette matière. Lance-toi !' });
      continue;
    }
    const pct = Math.round((data.correct / data.done) * 100);
    if (pct < 60) {
      tips.push({ subject: key, label: displayLabel, isArabic: meta.isArabic, tip: meta.isArabic ? `نتيجتك في ${displayLabel} هي ${pct}٪. راجع الدروس وأعد التمارين.` : `Ton score en ${displayLabel} est de ${pct}%. Révise les cours et refais des exercices.` });
    }
  }

  return tips;
}
