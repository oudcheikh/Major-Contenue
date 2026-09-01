import { useState } from 'react'
import { View, Text, TouchableOpacity, ScrollView, Animated, StyleSheet } from 'react-native'
import {
  GAME, ChunkyButton, GameHeader, FeedbackBanner, EndScreen, ConfettiBurst, MascotBubble, Fraction,
  useShake, usePop, buzz, tap, praise, retryTitle,
} from './ui.js'
import { COLORS } from '../theme.js'

// Jeu math6-u02 — « لوّن الكسر » : le نموذج الشريط du cahier, en missions.
// أستاذ ماجور demande une fraction, l'enfant colorie les parts.

const FRACTION_NAMES = {
  2: { one: 'نصف', two: 'نصفان', few: 'أنصاف' },
  3: { one: 'ثلث', two: 'ثلثان', few: 'أثلاث' },
  4: { one: 'ربع', two: 'ربعان', few: 'أرباع' },
  5: { one: 'خُمس', two: 'خُمسان', few: 'أخماس' },
  6: { one: 'سُدس', two: 'سُدسان', few: 'أسداس' },
  8: { one: 'ثُمن', two: 'ثُمنان', few: 'أثمان' },
  10: { one: 'عُشر', two: 'عُشران', few: 'أعشار' },
}

const COUNT_WORDS = ['', '', '', 'ثلاثة', 'أربعة', 'خمسة', 'ستة', 'سبعة', 'ثمانية', 'تسعة']

export function fractionName(num, den) {
  if (num === den) return 'الكلّ الكامل'
  const f = FRACTION_NAMES[den]
  if (num === 1) return f.one
  if (num === 2) return f.two
  return `${COUNT_WORDS[num]} ${f.few}`
}

const MISSIONS = [
  { num: 1, den: 2 },
  { num: 3, den: 4 },
  { num: 2, den: 3 },
  { num: 5, den: 8 },
  { num: 7, den: 10 },
]

export default function FractionBar({ color = COLORS.royal, onExit }) {
  const [round, setRound] = useState(0)
  const [filled, setFilled] = useState([])
  const [feedback, setFeedback] = useState(null) // null | 'ok' | 'bad'
  const [okTitle, setOkTitle] = useState('')
  const [badTitle, setBadTitle] = useState('')
  const [failedThis, setFailedThis] = useState(false)
  const [stars, setStars] = useState(0)
  const [streak, setStreak] = useState(0)
  const [done, setDone] = useState(false)
  const [shakeStyle, shake] = useShake()
  const [popStyle, pop] = usePop()

  const m = MISSIONS[round]
  const name = fractionName(m.num, m.den)

  function toggle(i) {
    if (feedback === 'ok') return
    tap()
    setFilled(filled.includes(i) ? filled.filter((x) => x !== i) : [...filled, i])
  }

  function check() {
    const ok = filled.length === m.num
    if (ok) {
      buzz(true)
      pop()
      if (!failedThis) {
        setStars((s) => s + 1)
        setStreak((s) => s + 1)
        setOkTitle(praise())
      } else {
        setOkTitle('أحسنت! 👏')
      }
      setFeedback('ok')
    } else {
      buzz(false)
      shake()
      setFailedThis(true)
      setStreak(0)
      setBadTitle(retryTitle())
      setFeedback('bad')
    }
  }

  function next() {
    if (round + 1 >= MISSIONS.length) { setDone(true); return }
    setRound(round + 1)
    setFilled([])
    setFeedback(null)
    setFailedThis(false)
  }

  function replay() {
    setRound(0)
    setFilled([])
    setFeedback(null)
    setFailedThis(false)
    setStars(0)
    setStreak(0)
    setDone(false)
  }

  if (done) {
    return <EndScreen stars={stars} total={MISSIONS.length} onReplay={replay} onExit={onExit} color={color} />
  }

  return (
    <View style={styles.flex}>
      <ScrollView contentContainerStyle={styles.scroll}>
        <GameHeader index={round} total={MISSIONS.length} stars={stars} streak={streak} />

        <MascotBubble>
          <Text style={styles.missionBadge}>🎯 المهمة {round + 1} من {MISSIONS.length}</Text>
          <View style={styles.missionRow}>
            <Text style={styles.missionTitle}>لوّن الكسر</Text>
            <Fraction num={m.num} den={m.den} size={22} color={GAME.blue} />
            <Text style={styles.missionTitle}>
              (<Text style={styles.missionName}>{name}</Text>) من الشريط 👇
            </Text>
          </View>
        </MascotBubble>

        <Animated.View style={[styles.barWrap, shakeStyle, popStyle]}>
          <View style={styles.bar}>
            {Array.from({ length: m.den }, (_, i) => (
              <TouchableOpacity
                key={i}
                style={[
                  styles.slice,
                  { borderColor: color },
                  filled.includes(i) && { backgroundColor: color },
                ]}
                activeOpacity={0.7}
                onPress={() => toggle(i)}
              />
            ))}
          </View>
          <Text style={styles.barCaption}>الشريط مقسوم إلى {m.den} حصص متساوية</Text>
        </Animated.View>

        <View style={styles.resultRow}>
          <Fraction num={filled.length} den={m.den} size={26} color={color} />
          <View style={{ flex: 1 }}>
            <Text style={styles.fracLabel}>
              {filled.length === 0 ? 'اضغط على الحصص لتلوينها' : `لوّنت ${filled.length} من ${m.den} حصص`}
            </Text>
          </View>
        </View>

        {feedback !== 'ok' && (
          <ChunkyButton label="تحقّق ✅" color={GAME.green} disabled={filled.length === 0} onPress={check} />
        )}
      </ScrollView>

      {feedback === 'ok' && (
        <FeedbackBanner
          ok
          title={okTitle}
          body={`${m.num}/${m.den} = ${name}`}
          actionLabel={round + 1 >= MISSIONS.length ? 'أرى نتيجتي 🏁' : 'المهمة التالية ←'}
          onAction={next}
        />
      )}
      {feedback === 'bad' && (
        <FeedbackBanner
          ok={false}
          title={badTitle}
          body={`لوّنت ${filled.length} والمطلوب ${m.num}. تذكّر: البسط يعدّ الحصص الملوّنة!`}
          actionLabel="أحاول من جديد"
          onAction={() => setFeedback(null)}
        />
      )}
    </View>
  )
}

const styles = StyleSheet.create({
  flex: { flex: 1 },
  scroll: { padding: 18, paddingBottom: 30 },
  missionBadge: { fontSize: 12, fontWeight: '800', color: GAME.soft, textAlign: 'right', writingDirection: 'rtl' },
  missionRow: { flexDirection: 'row-reverse', alignItems: 'center', flexWrap: 'wrap', gap: 4, marginTop: 6 },
  missionTitle: { fontSize: 17, fontWeight: '800', color: GAME.ink, textAlign: 'right', writingDirection: 'rtl', lineHeight: 29 },
  missionName: { color: GAME.blue },
  barWrap: { marginBottom: 16 },
  bar: { flexDirection: 'row-reverse', height: 84, borderRadius: 16, overflow: 'hidden', backgroundColor: GAME.card, gap: 3, padding: 3, borderWidth: 2, borderColor: '#e5e5e5' },
  slice: { flex: 1, borderWidth: 2, borderRadius: 8 },
  barCaption: { fontSize: 13, fontWeight: '700', color: GAME.soft, textAlign: 'center', writingDirection: 'rtl', marginTop: 8 },
  resultRow: { flexDirection: 'row-reverse', alignItems: 'center', gap: 16, backgroundColor: GAME.card, borderRadius: 16, borderWidth: 2, borderColor: '#e5e5e5', padding: 14, marginBottom: 6 },
  fraction: { alignItems: 'center', minWidth: 50 },
  fracNum: { fontSize: 24, fontWeight: '900' },
  fracLine: { alignSelf: 'stretch', height: 3, borderRadius: 2, backgroundColor: GAME.ink, marginVertical: 3 },
  fracDen: { fontSize: 24, fontWeight: '900', color: GAME.ink },
  fracLabel: { fontSize: 15, fontWeight: '700', color: GAME.ink, textAlign: 'right', writingDirection: 'rtl', lineHeight: 25 },
})
