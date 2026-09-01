import { useMemo, useState } from 'react'
import { View, Text, TouchableOpacity, ScrollView, Animated, StyleSheet } from 'react-native'
import { toArabicWords, groupDigits } from './arabicNumbers.js'
import {
  GAME, ChunkyButton, GameHeader, FeedbackBanner, EndScreen, ConfettiBurst, MascotBubble,
  useShake, usePop, buzz, tap, praise, retryTitle,
} from './ui.js'
import { COLORS } from '../theme.js'

// Jeu math6-u01 — « اكتب العدد » : أستاذ ماجور dicte un nombre en lettres,
// l'enfant le compose sur le clavier. 5 missions de plus en plus grandes,
// une étoile par mission réussie du premier coup, série 🔥 à entretenir.

const GROUP_META = [
  { label: 'الوحدات', color: '#1cb0f6', bg: '#e5f7ff' },
  { label: 'الآلاف', color: '#ff9600', bg: '#fff3e0' },
  { label: 'الملايين', color: '#58cc02', bg: '#eaffd6' },
  { label: 'المليارات', color: '#ce82ff', bg: '#f7ebff' },
]

// Un nombre aléatoire de `d` chiffres, sans zéro initial.
function randomNumber(d) {
  const first = 1 + Math.floor(Math.random() * 9)
  let s = String(first)
  for (let i = 1; i < d; i++) s += Math.floor(Math.random() * 10)
  return parseInt(s, 10)
}

const LEVELS = [2, 3, 5, 7, 10]
const MAX_DIGITS = 12

export default function NumberBuilder({ color = COLORS.royal, onExit }) {
  const [round, setRound] = useState(0)
  const [targets, setTargets] = useState(() => LEVELS.map(randomNumber))
  const [digits, setDigits] = useState('')
  const [feedback, setFeedback] = useState(null) // null | 'ok' | 'bad'
  const [okTitle, setOkTitle] = useState('')
  const [badTitle, setBadTitle] = useState('')
  const [failedThis, setFailedThis] = useState(false)
  const [stars, setStars] = useState(0)
  const [streak, setStreak] = useState(0)
  const [done, setDone] = useState(false)
  const [shakeStyle, shake] = useShake()
  const [popStyle, pop] = usePop()

  const target = targets[round]
  const words = useMemo(() => toArabicWords(target), [target])
  const clean = digits.replace(/^0+(?=\d)/, '')

  const groups = []
  for (let s = clean, i = 0; s.length > 0; i++) {
    groups.push({ text: s.slice(-3), meta: GROUP_META[i] })
    s = s.slice(0, -3)
  }

  function press(d) {
    if (feedback === 'ok' || digits.length >= MAX_DIGITS) return
    tap()
    setDigits((digits + d).replace(/^0+(?=\d)/, ''))
  }

  function check() {
    const ok = clean !== '' && parseInt(clean, 10) === target
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
    if (round + 1 >= targets.length) { setDone(true); return }
    setRound(round + 1)
    setDigits('')
    setFeedback(null)
    setFailedThis(false)
  }

  function replay() {
    setTargets(LEVELS.map(randomNumber))
    setRound(0)
    setDigits('')
    setFeedback(null)
    setFailedThis(false)
    setStars(0)
    setStreak(0)
    setDone(false)
  }

  if (done) {
    return <EndScreen stars={stars} total={targets.length} onReplay={replay} onExit={onExit} color={color} />
  }

  return (
    <View style={styles.flex}>
      <ScrollView contentContainerStyle={styles.scroll}>
        <GameHeader index={round} total={targets.length} stars={stars} streak={streak} />

        <MascotBubble>
          <Text style={styles.missionBadge}>🎯 المهمة {round + 1} من {targets.length}</Text>
          <Text style={styles.missionTitle}>اكتب هذا العدد بالأرقام :</Text>
          <Text style={styles.missionWords}>« {words} »</Text>
        </MascotBubble>

        <Animated.View style={[styles.display, { borderColor: feedback === 'ok' ? GAME.green : '#e5e5e5' }, shakeStyle, popStyle]}>
          <Text style={[styles.displayText, feedback === 'ok' && { color: GAME.green }]}>
            {clean ? groupDigits(clean) : '· · ·'}
          </Text>
        </Animated.View>

        {groups.length > 0 && (
          <View style={styles.groupsRow}>
            {[...groups].reverse().map((g, i) => (
              <View key={i} style={[styles.groupChip, { backgroundColor: g.meta.bg, borderColor: g.meta.color + '66' }]}>
                <Text style={[styles.groupDigits, { color: g.meta.color }]}>{g.text}</Text>
                <Text style={[styles.groupLabel, { color: g.meta.color }]}>{g.meta.label}</Text>
              </View>
            ))}
          </View>
        )}

        <View style={styles.pad}>
          {['1', '2', '3', '4', '5', '6', '7', '8', '9'].map((d) => (
            <TouchableOpacity key={d} style={styles.key} activeOpacity={0.6} onPress={() => press(d)}>
              <Text style={styles.keyText}>{d}</Text>
            </TouchableOpacity>
          ))}
          <TouchableOpacity style={[styles.key, styles.keyGhost]} activeOpacity={0.6} onPress={() => { tap(); setDigits(digits.slice(0, -1)) }}>
            <Text style={styles.keyGhostText}>⌫</Text>
          </TouchableOpacity>
          <TouchableOpacity style={styles.key} activeOpacity={0.6} onPress={() => press('0')}>
            <Text style={styles.keyText}>0</Text>
          </TouchableOpacity>
          <TouchableOpacity style={[styles.key, styles.keyGhost]} activeOpacity={0.6} onPress={() => { tap(); setDigits('') }}>
            <Text style={styles.keyGhostText}>مسح</Text>
          </TouchableOpacity>
        </View>

        {feedback !== 'ok' && (
          <ChunkyButton label="تحقّق ✅" color={GAME.green} disabled={!clean} onPress={check} />
        )}
      </ScrollView>

      {feedback === 'ok' && (
        <FeedbackBanner
          ok
          title={okTitle}
          body={`${groupDigits(String(target))} = ${words}`}
          actionLabel={round + 1 >= targets.length ? 'أرى نتيجتي 🏁' : 'المهمة التالية ←'}
          onAction={next}
        />
      )}
      {feedback === 'bad' && (
        <FeedbackBanner
          ok={false}
          title={badTitle}
          body={`تذكّر: العدد المطلوب فيه ${String(target).length} أرقام. جمّعها ثلاثة ثلاثة من اليمين!`}
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
  missionTitle: { fontSize: 16, fontWeight: '800', color: GAME.ink, textAlign: 'right', writingDirection: 'rtl', marginTop: 5 },
  missionWords: { fontSize: 19, fontWeight: '800', color: GAME.blue, textAlign: 'right', writingDirection: 'rtl', lineHeight: 32, marginTop: 7 },
  display: { backgroundColor: GAME.card, borderWidth: 2, borderRadius: 18, paddingVertical: 14, alignItems: 'center', marginBottom: 10 },
  displayText: { fontSize: 30, fontWeight: '800', color: GAME.ink, letterSpacing: 1 },
  groupsRow: { flexDirection: 'row-reverse', flexWrap: 'wrap', gap: 8, justifyContent: 'center', marginBottom: 10 },
  groupChip: { borderRadius: 12, borderWidth: 2, paddingVertical: 6, paddingHorizontal: 12, alignItems: 'center', minWidth: 70 },
  groupDigits: { fontSize: 20, fontWeight: '800' },
  groupLabel: { fontSize: 11, fontWeight: '800', marginTop: 1, writingDirection: 'rtl' },
  pad: { flexDirection: 'row', flexWrap: 'wrap', justifyContent: 'center', gap: 9, marginTop: 4 },
  key: {
    width: '30%', backgroundColor: GAME.card, borderWidth: 2, borderColor: '#e5e5e5', borderBottomWidth: 4,
    borderRadius: 14, paddingVertical: 12, alignItems: 'center',
  },
  keyText: { fontSize: 24, fontWeight: '800', color: GAME.ink },
  keyGhost: { backgroundColor: '#f7f7f7' },
  keyGhostText: { fontSize: 17, fontWeight: '800', color: GAME.soft },
})
