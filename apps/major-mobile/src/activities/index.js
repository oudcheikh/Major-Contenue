// Registre des activités interactives « أجرّب بنفسي », par id de leçon.
// 3 jeux sur mesure (u01-u03) + 2 moteurs génériques (calcul / choix visuel)
// alimentés par des missions propres à chaque unité → les 31 unités maths.
// Les autres matières reçoivent un jeu automatique nourri par les QCM de
// la leçon : « صحيح أم خطأ » ou « أختار الصواب » selon la matière.

import DigitDropGame from './DigitDropGame.js'
import FractionBar from './FractionBar.js'
import AdditionGame from './AdditionGame.js'
import ComputeGame from './engines/ComputeGame.js'
import ChoiceGame from './engines/ChoiceGame.js'
import TrueFalseGame from './engines/TrueFalseGame.js'
import * as M from './missions/math.js'
import { getLessonById, getQuizForLesson } from '../lib/lessons.js'

const compute = (title, makeMissions) => ({ component: ComputeGame, title, props: { makeMissions } })
const choice = (title, makeMissions) => ({ component: ChoiceGame, title, props: { makeMissions } })

const ACTIVITIES = {
  'math6-u01': { component: DigitDropGame, title: 'أملأ الخانات' },
  'math6-u02': { component: FractionBar, title: 'ألوّن الكسر' },
  'math6-u03': { component: AdditionGame, title: 'أجمع بالاحتفاظ' },
  'math6-u04': compute('أتقن الضرب', M.u04),
  'math6-u05': compute('أتقن القسمة', M.u05),
  'math6-u06': compute('أحوّل الأطوال', M.u06),
  'math6-u07': choice('أميّز المستقيمات', M.u07),
  'math6-u08': choice('أقارن الأعداد', M.u08),
  'math6-u09': compute('أحوّل الكتل', M.u09),
  'math6-u10': choice('أميّز الزوايا', M.u10),
  'math6-u11': choice('أضرب الكسور', M.u11),
  'math6-u12': choice('أقسم الكسور', M.u12),
  'math6-u13': compute('أحسب الربح', M.u13),
  'math6-u14': compute('أحسب بالفاصلة', M.u14),
  'math6-u15': compute('أحسب النسبة المئوية', M.u15),
  'math6-u16': choice('أختبر قابلية القسمة', M.u16),
  'math6-u17': compute('أكمل الكسر المكافئ', M.u17),
  'math6-u18': compute('أضرب في 10 و100 و1000', M.u18),
  'math6-u19': compute('أقسم بعدل', M.u19),
  'math6-u20': compute('أحسب الزمن', M.u20),
  'math6-u21': compute('أحسب بالتناسب', M.u21),
  'math6-u22': compute('السرعة والمسافة والزمن', M.u22),
  'math6-u23': compute('أقرأ الخريطة بالسلم', M.u23),
  'math6-u24': compute('أحسب الفائدة', M.u24),
  'math6-u25': compute('أغرس وأحسب الفواصل', M.u25),
  'math6-u26': compute('القائمة والصافية والفارغ', M.u26),
  'math6-u27': compute('مساحة المثلث', M.u27),
  'math6-u28': compute('المستطيل: مساحة ومحيط', M.u28),
  'math6-u29': compute('أقيس الحقول', M.u29),
  'math6-u30': compute('المحيط والمساحة للدائرة', M.u30),
  'math6-u31': compute('أحسب الحجم', M.u31),
}

const shuffle = (arr) => {
  const a = [...arr]
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1))
    ;[a[i], a[j]] = [a[j], a[i]]
  }
  return a
}

// « أختار الصواب » : 5 QCM de la leçon, mélangés à chaque partie.
const quizChoiceMissions = (lesson) => () =>
  shuffle(getQuizForLesson(lesson)).slice(0, 5).map((q) => ({
    q: q.question,
    choices: q.options,
    correct: q.answer,
    hint: q.explanation,
  }))

// « صحيح أم خطأ » : la question + une réponse proposée (vraie ou piégée).
const quizTrueFalseMissions = (lesson) => () =>
  shuffle(getQuizForLesson(lesson)).slice(0, 6).map((q) => {
    const isTrue = Math.random() < 0.5
    const wrong = q.options.filter((_, i) => i !== q.answer)
    const shown = isTrue ? q.options[q.answer] : wrong[Math.floor(Math.random() * wrong.length)]
    return { q: q.question, statement: `«${shown}»`, isTrue, hint: q.explanation }
  })

// Un style de jeu différent par matière — l'enfant change d'ambiance.
const SUBJECT_GAMES = {
  'sci6-ar': (l) => ({ component: TrueFalseGame, title: 'مختبر العالِم الصغير 🔬', props: { makeMissions: quizTrueFalseMissions(l) } }),
  ar6:       (l) => ({ component: ChoiceGame,    title: 'أختار الصواب 📘',          props: { makeMissions: quizChoiceMissions(l) } }),
  isl6:      (l) => ({ component: TrueFalseGame, title: 'صحيح أم خطأ؟ ⭐',          props: { makeMissions: quizTrueFalseMissions(l) } }),
  hg6:       (l) => ({ component: ChoiceGame,    title: 'رحلة عبر الزمن 🏰',        props: { makeMissions: quizChoiceMissions(l) } }),
  civ6:      (l) => ({ component: TrueFalseGame, title: 'المواطن الصغير 🤝',        props: { makeMissions: quizTrueFalseMissions(l) } }),
}

export function getActivityForLesson(lessonId) {
  if (ACTIVITIES[lessonId]) return ACTIVITIES[lessonId]
  const lesson = getLessonById(lessonId)
  const generic = lesson && SUBJECT_GAMES[lesson.subjectId]
  if (generic && getQuizForLesson(lesson).length >= 3) return generic(lesson)
  return null
}
