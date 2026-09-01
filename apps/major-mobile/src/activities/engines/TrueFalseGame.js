import { useState } from 'react'
import { View, Text, TouchableOpacity, ScrollView, Animated, StyleSheet } from 'react-native'
import {
  GAME, GameHeader, FeedbackBanner, EndScreen, MascotBubble,
  useShake, usePop, buzz, tap, praise, retryTitle,
} from '../ui.js'
import { COLORS } from '../../theme.js'

// Moteur « صحيح أم خطأ » : une affirmation + deux gros boutons.
// Rapide, rejouable, alimenté par les QCM de la leçon.
// makeMissions → [{ q, statement, isTrue, hint }]

export default function TrueFalseGame({ color = COLORS.royal, onExit, makeMissions }) {
  const [missions, setMissions] = useState(() => makeMissions())
  const [round, setRound] = useState(0)
  const [feedback, setFeedback] = useState(null)
  const [okTitle, setOkTitle] = useState('')
  const [badTitle, setBadTitle] = useState('')
  const [failedThis, setFailedThis] = useState(false)
  const [stars, setStars] = useState(0)
  const [streak, setStreak] = useState(0)
  const [done, setDone] = useState(false)
  const [shakeStyle, shake] = useShake()
  const [popStyle, pop] = usePop()

  const m = missions[round]

  function answer(saidTrue) {
    if (feedback === 'ok') return
    tap()
    if (saidTrue === m.isTrue) {
      buzz(true); pop()
      if (!failedThis) { setStars((s) => s + 1); setStreak((s) => s + 1); setOkTitle(praise()) }
      else setOkTitle('أحسنت! 👏')
      setFeedback('ok')
    } else {
      buzz(false); shake()
      setFailedThis(true); setStreak(0)
      setBadTitle(retryTitle())
      setFeedback('bad')
    }
  }

  function next() {
    if (round + 1 >= missions.length) { setDone(true); return }
    setRound(round + 1); setFeedback(null); setFailedThis(false)
  }

  function replay() {
    setMissions(makeMissions())
    setRound(0); setFeedback(null); setFailedThis(false)
    setStars(0); setStreak(0); setDone(false)
  }

  if (done) return <EndScreen stars={stars} total={missions.length} onReplay={replay} onExit={onExit} color={color} />

  return (
    <View style={styles.flex}>
      <ScrollView contentContainerStyle={styles.scroll}>
        <GameHeader index={round} total={missions.length} stars={stars} streak={streak} />

        <MascotBubble>
          <Text style={styles.badge}>🎯 المهمة {round + 1} من {missions.length}</Text>
          {!!m.q && <Text style={styles.q}>{m.q}</Text>}
        </MascotBubble>

        <Animated.View style={[styles.statementCard, shakeStyle, popStyle, { borderColor: `${color}44` }]}>
          <Text style={styles.statementText}>{m.statement}</Text>
        </Animated.View>

        <View style={styles.btnRow}>
          <TouchableOpacity
            style={[styles.tfBtn, styles.tfTrue, feedback === 'ok' && m.isTrue && styles.tfWin]}
            activeOpacity={0.75}
            disabled={feedback === 'ok'}
            onPress={() => answer(true)}
          >
            <Text style={styles.tfEmoji}>✅</Text>
            <Text style={[styles.tfText, { color: GAME.greenInk }]}>صحيح</Text>
          </TouchableOpacity>
          <TouchableOpacity
            style={[styles.tfBtn, styles.tfFalse, feedback === 'ok' && !m.isTrue && styles.tfWin]}
            activeOpacity={0.75}
            disabled={feedback === 'ok'}
            onPress={() => answer(false)}
          >
            <Text style={styles.tfEmoji}>❌</Text>
            <Text style={[styles.tfText, { color: GAME.redInk }]}>خطأ</Text>
          </TouchableOpacity>
        </View>
      </ScrollView>

      {feedback === 'ok' && (
        <FeedbackBanner
          ok
          title={okTitle}
          body={m.hint}
          actionLabel={round + 1 >= missions.length ? 'أرى نتيجتي 🏁' : 'المهمة التالية ←'}
          onAction={next}
        />
      )}
      {feedback === 'bad' && (
        <FeedbackBanner
          ok={false}
          title={badTitle}
          body={m.hint}
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
  badge: { fontSize: 12, fontWeight: '800', color: GAME.soft, textAlign: 'right', writingDirection: 'rtl' },
  q: { fontSize: 16, fontWeight: '800', color: GAME.ink, textAlign: 'right', writingDirection: 'rtl', marginTop: 6, lineHeight: 28 },
  statementCard: {
    backgroundColor: GAME.card, borderWidth: 2, borderRadius: 18,
    padding: 18, marginBottom: 16, minHeight: 110, justifyContent: 'center',
  },
  statementText: { fontSize: 18, fontWeight: '800', color: GAME.ink, textAlign: 'center', writingDirection: 'rtl', lineHeight: 34 },
  btnRow: { flexDirection: 'row-reverse', gap: 12 },
  tfBtn: {
    flex: 1, alignItems: 'center', gap: 4,
    borderRadius: 16, borderWidth: 2, borderBottomWidth: 5, paddingVertical: 16,
    backgroundColor: GAME.card,
  },
  tfTrue: { borderColor: GAME.green },
  tfFalse: { borderColor: GAME.red },
  tfWin: { backgroundColor: '#f2ffe5' },
  tfEmoji: { fontSize: 28 },
  tfText: { fontSize: 18, fontWeight: '900', writingDirection: 'rtl' },
})
