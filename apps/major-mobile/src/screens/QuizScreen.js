import { useLayoutEffect, useMemo, useState } from 'react'
import { View, Text, ScrollView, TouchableOpacity, StyleSheet } from 'react-native'
import { SafeAreaView } from 'react-native-safe-area-context'
import { getLessonById, getQuizForLesson, getNextLesson } from '../lib/lessons.js'
import { recordQuiz } from '../firebase/progress.js'
import { COLORS, SHADOW, RADIUS, getEncouragement } from '../theme.js'
import { GAME, ChunkyButton, buzz, tap } from '../activities/ui.js'

export default function QuizScreen({ route, navigation }) {
  const { lessonId } = route.params
  const lesson = getLessonById(lessonId)
  const questions = useMemo(() => getQuizForLesson(lesson), [lessonId])
  const color = lesson?.subjectColor || COLORS.royal

  const [idx, setIdx] = useState(0)
  const [selected, setSelected] = useState(null)
  const [score, setScore] = useState(0)
  const [finished, setFinished] = useState(false)

  useLayoutEffect(() => {
    navigation.setOptions({ title: 'الاختبار' })
  }, [navigation])

  if (!lesson || questions.length === 0) {
    return <SafeAreaView style={styles.safe}><Text style={styles.empty}>لا توجد أسئلة بعد.</Text></SafeAreaView>
  }

  if (finished) {
    return <Results lesson={lesson} score={score} total={questions.length} color={color} navigation={navigation} />
  }

  const q = questions[idx]
  const answered = selected !== null

  function choose(i) {
    if (answered) return
    const ok = i === q.answer
    buzz(ok)
    setSelected(i)
    if (ok) setScore((s) => s + 1)
  }

  function next() {
    tap()
    if (idx + 1 < questions.length) {
      setIdx((n) => n + 1)
      setSelected(null)
    } else {
      recordQuiz({ lessonId, subjectId: lesson.subjectId, score, total: questions.length })
      setFinished(true)
    }
  }

  return (
    <SafeAreaView style={styles.safe} edges={['bottom']}>
      <View style={styles.headerRow}>
        <Text style={styles.counter}>⭐ {score}</Text>
        <View style={styles.track}>
          <View style={[styles.fill, { width: `${(idx / questions.length) * 100}%`, backgroundColor: color }]} />
        </View>
      </View>
      <ScrollView contentContainerStyle={styles.scroll} showsVerticalScrollIndicator={false}>
        <Text style={styles.qNum}>السؤال {idx + 1} من {questions.length}</Text>
        <View style={styles.questionCard}>
          <Text style={styles.question}>{q.question}</Text>
        </View>

        {q.options.map((opt, i) => {
          const isCorrect = i === q.answer
          const isChosen = i === selected
          let extra = null
          if (answered && isCorrect) extra = styles.optCorrect
          else if (answered && isChosen && !isCorrect) extra = styles.optWrong
          return (
            <TouchableOpacity
              key={i}
              style={[styles.option, extra]}
              activeOpacity={0.75}
              onPress={() => choose(i)}
              disabled={answered}
            >
              <Text style={[styles.optionText, answered && (isCorrect || isChosen) && styles.optTextStrong, { flex: 1 }]}>
                {opt}
              </Text>
              {answered && isCorrect && <Text style={styles.mark}>✓</Text>}
              {answered && isChosen && !isCorrect && <Text style={styles.markBad}>✗</Text>}
            </TouchableOpacity>
          )
        })}

        {answered && !!q.explanation && (
          <View style={styles.explain}>
            <Text style={styles.explainText}>💡 {q.explanation}</Text>
          </View>
        )}
      </ScrollView>

      {answered && (
        <View style={styles.footer}>
          <ChunkyButton
            label={idx + 1 < questions.length ? 'التالي ←' : 'أرى نتيجتي 🏁'}
            color={selected === q.answer ? GAME.green : color}
            onPress={next}
          />
        </View>
      )}
    </SafeAreaView>
  )
}

function Results({ lesson, score, total, color, navigation }) {
  const pct = total > 0 ? Math.round((score / total) * 100) : 0
  const enc = getEncouragement(pct, true)
  const nextL = pct >= 60 ? getNextLesson(lesson.id) : null
  return (
    <SafeAreaView style={[styles.safe, styles.resultWrap]} edges={['bottom']}>
      <View style={styles.resultCard}>
        <Text style={styles.resultEmoji}>{pct >= 80 ? '🏆' : pct >= 60 ? '🎉' : '💪'}</Text>
        <Text style={[styles.resultPct, { color }]}>{pct}%</Text>
        <Text style={styles.resultScore}>{score} من {total} إجابات صحيحة</Text>
        <Text style={styles.resultTitle}>{enc.title}</Text>
        <Text style={styles.resultBody}>{enc.body}</Text>
      </View>
      <View style={styles.resultBtns}>
        {nextL ? (
          <ChunkyButton
            label={`الدرس التالي: ${nextL.title} ←`}
            color={color}
            onPress={() => navigation.replace('Lesson', { lessonId: nextL.id })}
          />
        ) : (
          <ChunkyButton label="أعيد المحاولة 🔄" color={color} onPress={() => navigation.replace('Quiz', { lessonId: lesson.id })} />
        )}
        {nextL && (
          <ChunkyButton label="أعيد المحاولة 🔄" color="#e5e7ee" textColor={COLORS.ink} onPress={() => navigation.replace('Quiz', { lessonId: lesson.id })} />
        )}
        <ChunkyButton label="الرئيسية" color="#e5e7ee" textColor={COLORS.ink} onPress={() => navigation.popToTop()} />
      </View>
    </SafeAreaView>
  )
}

const styles = StyleSheet.create({
  safe: { flex: 1, backgroundColor: COLORS.cream },
  empty: { padding: 24, color: COLORS.inkSoft, textAlign: 'right', writingDirection: 'rtl' },
  headerRow: { flexDirection: 'row-reverse', alignItems: 'center', gap: 12, paddingHorizontal: 18, paddingTop: 12 },
  counter: { fontSize: 15, fontWeight: '800', color: COLORS.ink },
  track: { flex: 1, height: 12, borderRadius: 6, backgroundColor: '#e8eaf0', overflow: 'hidden' },
  fill: { height: 12, borderRadius: 6 },
  scroll: { padding: 18, paddingBottom: 30 },
  qNum: { fontSize: 13, fontWeight: '700', color: COLORS.inkSoft, marginBottom: 10, textAlign: 'right', writingDirection: 'rtl' },
  questionCard: { backgroundColor: COLORS.card, borderRadius: RADIUS.md, padding: 18, marginBottom: 16, ...SHADOW },
  question: { fontSize: 19, fontWeight: '800', color: COLORS.ink, lineHeight: 31, textAlign: 'right', writingDirection: 'rtl' },
  option: {
    flexDirection: 'row-reverse', alignItems: 'center',
    backgroundColor: COLORS.card, borderWidth: 2, borderColor: '#e8eaf0', borderBottomWidth: 4,
    borderRadius: RADIUS.md, padding: 16, marginBottom: 10,
  },
  optCorrect: { borderColor: GAME.green, backgroundColor: '#f2ffe5' },
  optWrong: { borderColor: GAME.red, backgroundColor: '#fff1f1' },
  optionText: { fontSize: 16, color: COLORS.ink, fontWeight: '600', lineHeight: 26, textAlign: 'right', writingDirection: 'rtl' },
  optTextStrong: { fontWeight: '800' },
  mark: { color: GAME.green, fontSize: 20, fontWeight: '800', marginLeft: 4 },
  markBad: { color: GAME.red, fontSize: 20, fontWeight: '800', marginLeft: 4 },
  explain: { marginTop: 6, backgroundColor: '#fffaeb', borderRadius: RADIUS.md, borderWidth: 1.5, borderColor: '#fde68a', padding: 14 },
  explainText: { fontSize: 14, lineHeight: 25, color: '#92400e', fontWeight: '600', textAlign: 'right', writingDirection: 'rtl' },
  footer: { padding: 16, backgroundColor: COLORS.cream },
  resultWrap: { padding: 24, justifyContent: 'center' },
  resultCard: { backgroundColor: COLORS.card, borderRadius: RADIUS.xl, padding: 28, alignItems: 'center', ...SHADOW },
  resultEmoji: { fontSize: 56 },
  resultPct: { fontSize: 56, fontWeight: '900', marginTop: 6 },
  resultScore: { fontSize: 16, fontWeight: '700', color: COLORS.inkSoft, marginTop: 4, writingDirection: 'rtl' },
  resultTitle: { fontSize: 24, fontWeight: '900', color: COLORS.ink, marginTop: 18, textAlign: 'center', writingDirection: 'rtl' },
  resultBody: { fontSize: 15, color: COLORS.inkSoft, marginTop: 8, textAlign: 'center', lineHeight: 25, writingDirection: 'rtl', fontWeight: '600' },
  resultBtns: { marginTop: 18 },
})
