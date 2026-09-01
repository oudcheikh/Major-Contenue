// Accès au contenu embarqué (offline). Les QR des cahiers imprimés
// encodent « major://lesson/<lessonId> ».

import { COURSES, EXERCISES } from '../content/data.js'

// Index plat de toutes les leçons, avec leur matière parente.
const LESSON_INDEX = {}
for (const subject of COURSES.subjects) {
  for (const lesson of subject.lessons || []) {
    LESSON_INDEX[lesson.id] = { ...lesson, subjectId: subject.id, subjectLabel: subject.labelAr || subject.label, subjectLabelAr: subject.labelAr, subjectColor: subject.color }
  }
}

// Seuls les 6 packs 6AF des cahiers imprimés sont visibles dans l'app ;
// les anciennes matières de démo (contenu français) restent dans l'index
// pour les vieux QR mais n'apparaissent pas à l'accueil.
const PACK_IDS = ['math6-ar', 'sci6-ar', 'ar6', 'isl6', 'hg6', 'civ6']

export function getAllSubjects() {
  return COURSES.subjects
    .filter((s) => PACK_IDS.includes(s.id))
    .map((s) => ({
      id: s.id,
      label: s.labelAr || s.label,
      labelAr: s.labelAr,
      color: s.color,
      icon: s.icon,
      isArabic: !!(s.lessons || []).some((l) => l.isArabic),
      lessonCount: (s.lessons || []).length,
    }))
}

export function getSubject(subjectId) {
  return COURSES.subjects.find((s) => s.id === subjectId) || null
}

// Périmètre du lancement : seules les premières unités de chaque matière
// sont ouvertes à la navigation libre ; les suivantes s'affichent
// verrouillées « قريبًا » et s'ouvriront par mises à jour OTA au fil de
// l'année. Les QR des cahiers imprimés ouvrent TOUTES les leçons (le
// scanner passe par un deep-link) : le cahier acheté est la clé complète.
export const OPEN_UNITS_PER_SUBJECT = 8

export function isLessonOpen(lessonId) {
  const lesson = LESSON_INDEX[lessonId]
  if (!lesson) return false
  const subject = COURSES.subjects.find((s) => s.id === lesson.subjectId)
  const i = (subject?.lessons || []).findIndex((l) => l.id === lessonId)
  return i >= 0 && i < OPEN_UNITS_PER_SUBJECT
}

export function getLessonById(lessonId) {
  return LESSON_INDEX[lessonId] || null
}

// Le drapeau suivant dans la même matière — pour que le compagnon
// propose « on continue ? » après un quiz. Ne propose jamais une
// leçon encore verrouillée au lancement.
export function getNextLesson(lessonId) {
  const lesson = LESSON_INDEX[lessonId]
  if (!lesson) return null
  const subject = COURSES.subjects.find((s) => s.id === lesson.subjectId)
  const lessons = subject?.lessons || []
  const i = lessons.findIndex((l) => l.id === lessonId)
  const next = i >= 0 && i + 1 < lessons.length ? LESSON_INDEX[lessons[i + 1].id] : null
  return next && isLessonOpen(next.id) ? next : null
}

// Extrait la cible d'un texte de QR / deep-link.
// Les cahiers imprimés encodent deux formats (qr_major.py) :
//   « …/#/lesson/xxx »     → page أتعلّم  → écran Leçon
//   « …/#/correction/xxx » → pages تمارين → écran Quiz
// Accepte aussi « major://lesson/xxx » et l'id nu « xxx ».
export function parseQr(raw) {
  if (!raw) return null
  const text = String(raw).trim()
  const m = text.match(/(lesson|correction)\/([A-Za-z0-9_-]+)/)
  if (m) return { lessonId: m[2], mode: m[1] === 'correction' ? 'quiz' : 'lesson' }
  if (LESSON_INDEX[text]) return { lessonId: text, mode: 'lesson' }
  return null
}

// QCM d'une leçon : d'abord via quizIds, sinon toutes les questions
// de la matière dont l'id commence par le préfixe de la leçon.
export function getQuizForLesson(lesson) {
  if (!lesson) return []
  const pool = collectPool(lesson.subjectId)
  if (Array.isArray(lesson.quizIds) && lesson.quizIds.length) {
    const byId = new Map(pool.map((q) => [q.id, q]))
    const picked = lesson.quizIds.map((id) => byId.get(id)).filter(Boolean)
    if (picked.length) return picked
  }
  return pool
}

// EXERCISES est indexé par le même id que la matière dans COURSES.
function collectPool(subjectId) {
  return EXERCISES[subjectId] || []
}
