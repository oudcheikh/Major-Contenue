import { EXERCISES } from '../data/exercises';

function getLocalExample(subjectId) {
  if (subjectId === 'math') return 'au marche, quand on partage des fruits ou qu on calcule des prix';
  if (subjectId === 'science') return 'dans le desert, a la peche ou en observant la nature';
  return 'dans une conversation a la maison, a l ecole ou dans la rue';
}

export function buildMentorHook(lesson, studentName) {
  const name = studentName || 'champion';
  const context = getLocalExample(lesson.subjectId);

  const fr = `Salam ${name} ! Super idee de reviser ${lesson.subjectLabel}. Regarde, ce chapitre sert tous les jours, ${context}. On va le rendre simple en moins de 30 secondes, puis tu testes ton niveau.`;
  const ar = `سلام ${name} ! ممتاز أنك تراجع ${lesson.subjectLabel}. هذا الدرس مفيد في حياتنا اليومية. سنبسطه بسرعة ثم تختبر نفسك.`;
  const hassanya = `${name}, salam! had dars yesser mhem, nhawlouh b tariqa sahla shwiya b shwiya.`;

  return { fr, ar, hassanya };
}

export function buildInteractiveSummary(lesson) {
  const base = Array.isArray(lesson.keyPoints) ? lesson.keyPoints : [];
  return base.slice(0, 3);
}

export function buildMicroChallenge(lesson) {
  const pool = EXERCISES[lesson.subjectId] || [];
  const easy = pool.filter((q) => q.difficulty <= 2);
  const source = easy.length ? easy : pool;
  if (!source.length) {
    return {
      id: `fallback-${lesson.id}`,
      question: `Quel est le point cle du chapitre: ${lesson.title} ?`,
      options: ['Relire le resume', 'Ignorer la lecon', 'Attendre le weekend', 'Ne pas pratiquer'],
      answer: 0,
      explanation: 'Le plus utile est de relire et pratiquer tout de suite.',
      difficulty: 1,
    };
  }

  const pick = source[Math.floor(Math.random() * source.length)];
  return pick;
}
