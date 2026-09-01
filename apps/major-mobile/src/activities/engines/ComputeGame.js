import { useMemo, useState } from 'react'
import { View, Text, TouchableOpacity, ScrollView, Animated, StyleSheet } from 'react-native'
import {
  GAME, ChunkyButton, GameHeader, FeedbackBanner, EndScreen, MascotBubble,
  useShake, usePop, buzz, tap, praise, retryTitle,
} from '../ui.js'
import { COLORS } from '../../theme.js'

// Moteur générique « je calcule et je réponds » : أستاذ ماجور pose un
// problème, l'enfant tape la réponse au clavier. Missions fournies par
// unité (makeMissions → [{ q, a, hint, suffix?, dec? }]).

export default function ComputeGame({ color = COLORS.royal, onExit, makeMissions }) {
  const [missions, setMissions] = useState(() => makeMissions())
  const [round, setRound] = useState(0)
  const [input, setInput] = useState('')
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
  const hasDecimal = !!m.dec

  function press(k) {
    if (feedback === 'ok') return
    tap()
    if (k === '.' && input.includes('.')) return
    if (input.length >= 8) return
    setInput(input + k)
  }

  function check() {
    const val = parseFloat(input)
    const ok = input !== '' && Number.isFinite(val) && Math.abs(val - m.a) < 0.001
    if (ok) {
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
    setRound(round + 1); setInput(''); setFeedback(null); setFailedThis(false)
  }

  function replay() {
    setMissions(makeMissions())
    setRound(0); setInput(''); setFeedback(null); setFailedThis(false)
    setStars(0); setStreak(0); setDone(false)
  }

  if (done) return <EndScreen stars={stars} total={missions.length} onReplay={replay} onExit={onExit} color={color} />

  const keys = hasDecimal
    ? ['1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '0', '⌫']
    : ['1', '2', '3', '4', '5', '6', '7', '8', '9', '⌫', '0', 'مسح']

  return (
    <View style={styles.flex}>
      <ScrollView contentContainerStyle={styles.scroll}>
        <GameHeader index={round} total={missions.length} stars={stars} streak={streak} />

        <MascotBubble>
          <Text style={styles.badge}>🎯 المهمة {round + 1} من {missions.length}</Text>
          <Text style={styles.q}>{m.q}</Text>
        </MascotBubble>

        <Animated.View style={[styles.display, { borderColor: feedback === 'ok' ? GAME.green : '#e5e5e5' }, shakeStyle, popStyle]}>
          <Text style={[styles.displayText, feedback === 'ok' && { color: GAME.green }]}>
            {input || '؟'}{m.suffix ? `  ${m.suffix}` : ''}
          </Text>
        </Animated.View>

        <View style={styles.pad}>
          {keys.map((k) => (
            <TouchableOpacity
              key={k}
              style={[styles.key, (k === '⌫' || k === 'مسح') && styles.keyGhost]}
              activeOpacity={0.6}
              onPress={() => {
                if (k === '⌫') { tap(); setInput(input.slice(0, -1)) }
                else if (k === 'مسح') { tap(); setInput('') }
                else press(k)
              }}
            >
              <Text style={[styles.keyText, (k === '⌫' || k === 'مسح') && styles.keyGhostText]}>{k}</Text>
            </TouchableOpacity>
          ))}
        </View>

        {feedback !== 'ok' && (
          <ChunkyButton label="تحقّق ✅" color={GAME.green} disabled={!input} onPress={check} />
        )}
      </ScrollView>

      {feedback === 'ok' && (
        <FeedbackBanner
          ok
          title={okTitle}
          body={`الجواب: ${m.a}${m.suffix ? ` ${m.suffix}` : ''}`}
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
  q: { fontSize: 17, fontWeight: '800', color: GAME.ink, textAlign: 'right', writingDirection: 'rtl', marginTop: 6, lineHeight: 30 },
  display: { backgroundColor: GAME.card, borderWidth: 2, borderRadius: 18, paddingVertical: 16, alignItems: 'center', marginBottom: 12 },
  displayText: { fontSize: 30, fontWeight: '800', color: GAME.ink, letterSpacing: 1 },
  pad: { flexDirection: 'row', flexWrap: 'wrap', justifyContent: 'center', gap: 9, marginBottom: 4 },
  key: {
    width: '30%', backgroundColor: GAME.card, borderWidth: 2, borderColor: '#e5e5e5', borderBottomWidth: 4,
    borderRadius: 14, paddingVertical: 12, alignItems: 'center',
  },
  keyText: { fontSize: 22, fontWeight: '800', color: GAME.ink },
  keyGhost: { backgroundColor: '#f7f7f7' },
  keyGhostText: { fontSize: 17, fontWeight: '800', color: GAME.soft },
})
