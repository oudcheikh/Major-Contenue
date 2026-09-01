import { useState } from 'react'
import { View, Text, TouchableOpacity, ScrollView, Animated, StyleSheet } from 'react-native'
import {
  GAME, ChunkyButton, GameHeader, FeedbackBanner, EndScreen, ConfettiBurst, MascotBubble,
  useShake, usePop, buzz, tap, praise, retryTitle,
} from './ui.js'
import { COLORS } from '../theme.js'

// Jeu math6-u03 — « الجمع بالاحتفاظ » : addition posée en colonnes,
// remplie chiffre par chiffre en partant des unités (comme dans le cahier).
// La retenue (الاحتفاظ) apparaît en rouge au-dessus de la colonne suivante.

// Deux nombres dont l'addition comporte au moins une retenue.
function makeMission(digits) {
  for (let tries = 0; tries < 60; tries++) {
    const min = Math.pow(10, digits - 1)
    const a = min + Math.floor(Math.random() * 9 * min)
    const b = min + Math.floor(Math.random() * 9 * min)
    const hasCarry = String(a).split('').reverse().some((da, i) => {
      const db = String(b).split('').reverse()[i]
      return parseInt(da, 10) + parseInt(db || '0', 10) >= 10
    })
    if (hasCarry) return { a, b }
  }
  return { a: 57, b: 68 }
}

const LEVELS = [2, 2, 3, 3, 4]

// Décomposition en colonnes (r = 0 → unités) : chiffres, retenues, somme.
function buildColumns(a, b) {
  const sum = String(a + b)
  const L = sum.length
  const ar = String(a).split('').reverse()
  const br = String(b).split('').reverse()
  const cols = []
  let carry = 0
  for (let r = 0; r < L; r++) {
    const da = parseInt(ar[r] || '0', 10)
    const db = parseInt(br[r] || '0', 10)
    const s = da + db + carry
    cols.push({
      da: ar[r] ?? '', db: br[r] ?? '',
      carryIn: carry, digit: s % 10,
    })
    carry = Math.floor(s / 10)
  }
  return { cols, sum }
}

const COL_NAMES = ['الآحاد', 'العشرات', 'المئات', 'الآلاف', 'عشرات الآلاف']

export default function AdditionGame({ color = COLORS.royal, onExit }) {
  const [round, setRound] = useState(0)
  const [missions, setMissions] = useState(() => LEVELS.map(makeMission))
  const [colIdx, setColIdx] = useState(0)
  const [entered, setEntered] = useState([])
  const [feedback, setFeedback] = useState(null) // null | 'ok' | 'bad'
  const [okTitle, setOkTitle] = useState('')
  const [badTitle, setBadTitle] = useState('')
  const [failedThis, setFailedThis] = useState(false)
  const [stars, setStars] = useState(0)
  const [streak, setStreak] = useState(0)
  const [done, setDone] = useState(false)
  const [shakeStyle, shake] = useShake()
  const [popStyle, pop] = usePop()

  const m = missions[round]
  const { cols, sum } = buildColumns(m.a, m.b)
  const L = cols.length
  const finished = colIdx >= L
  const cur = cols[Math.min(colIdx, L - 1)]

  // Indice pédagogique de la colonne en cours.
  const hint = finished
    ? ''
    : `${COL_NAMES[Math.min(colIdx, COL_NAMES.length - 1)]}: ${cur.da || 0} + ${cur.db || 0}${cur.carryIn ? ` + ${cur.carryIn} (الاحتفاظ)` : ''} = ${parseInt(cur.da || '0', 10) + parseInt(cur.db || '0', 10) + cur.carryIn}`

  function press(d) {
    if (finished || feedback === 'ok') return
    if (d === cur.digit) {
      tap()
      const nextEntered = [...entered, d]
      setEntered(nextEntered)
      if (nextEntered.length >= L) {
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
      }
      setColIdx(colIdx + 1)
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
    if (round + 1 >= missions.length) { setDone(true); return }
    setRound(round + 1)
    setColIdx(0)
    setEntered([])
    setFeedback(null)
    setFailedThis(false)
  }

  function replay() {
    setMissions(LEVELS.map(makeMission))
    setRound(0)
    setColIdx(0)
    setEntered([])
    setFeedback(null)
    setFailedThis(false)
    setStars(0)
    setStreak(0)
    setDone(false)
  }

  if (done) {
    return <EndScreen stars={stars} total={missions.length} onReplay={replay} onExit={onExit} color={color} />
  }

  // Colonnes affichées de gauche à droite (grand → petit), unités à droite.
  const display = Array.from({ length: L }, (_, i) => {
    const r = L - 1 - i
    return { r, ...cols[r] }
  })

  return (
    <View style={styles.flex}>
      <ScrollView contentContainerStyle={styles.scroll}>
        <GameHeader index={round} total={missions.length} stars={stars} streak={streak} />

        <MascotBubble>
          <Text style={styles.missionBadge}>🎯 المهمة {round + 1} من {missions.length}</Text>
          <Text style={styles.missionTitle}>
            أحسب <Text style={styles.missionOp}>{m.a} + {m.b}</Text> — أبدأ من الآحاد (اليمين) ولا أنسى الاحتفاظ!
          </Text>
        </MascotBubble>

        <Animated.View style={[styles.operation, shakeStyle, popStyle]}>
          <View style={styles.opGrid}>
            <View style={styles.opRow}>
              <View style={styles.opSign} />
              {display.map((c) => (
                <View key={`c${c.r}`} style={styles.cell}>
                  {c.carryIn > 0 && c.r <= colIdx && (
                    <Text style={styles.carry}>{c.carryIn}</Text>
                  )}
                </View>
              ))}
            </View>
            <View style={styles.opRow}>
              <View style={styles.opSign} />
              {display.map((c) => (
                <View key={`a${c.r}`} style={styles.cell}><Text style={styles.opDigit}>{c.da}</Text></View>
              ))}
            </View>
            <View style={styles.opRow}>
              <View style={styles.opSign}><Text style={styles.plus}>+</Text></View>
              {display.map((c) => (
                <View key={`b${c.r}`} style={styles.cell}><Text style={styles.opDigit}>{c.db}</Text></View>
              ))}
            </View>
            <View style={styles.opLine} />
            <View style={styles.opRow}>
              <View style={styles.opSign} />
              {display.map((c) => {
                const isDone = c.r < colIdx
                const isActive = c.r === colIdx && !finished
                return (
                  <View
                    key={`s${c.r}`}
                    style={[styles.cell, styles.resultCell, isActive && { borderColor: color, backgroundColor: color + '10' }, isDone && styles.resultDone]}
                  >
                    <Text style={[styles.resultDigit, isDone && { color: GAME.green }]}>
                      {isDone ? c.digit : ''}
                    </Text>
                  </View>
                )
              })}
            </View>
          </View>
        </Animated.View>

        {!finished && (
          <View style={styles.hintCard}>
            <Text style={styles.hintText}>👉 {hint}</Text>
          </View>
        )}

        <View style={styles.pad}>
          {['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'].map((d) => (
            <TouchableOpacity key={d} style={styles.key} activeOpacity={0.6} onPress={() => press(parseInt(d, 10))}>
              <Text style={styles.keyText}>{d}</Text>
            </TouchableOpacity>
          ))}
        </View>
      </ScrollView>

      {feedback === 'ok' && (
        <FeedbackBanner
          ok
          title={okTitle}
          body={`${m.a} + ${m.b} = ${sum} ✔`}
          actionLabel={round + 1 >= missions.length ? 'أرى نتيجتي 🏁' : 'المهمة التالية ←'}
          onAction={next}
        />
      )}
      {feedback === 'bad' && (
        <FeedbackBanner
          ok={false}
          title={badTitle}
          body={hint}
          actionLabel="أحاول من جديد"
          onAction={() => setFeedback(null)}
        />
      )}
    </View>
  )
}

const CELL = 46

const styles = StyleSheet.create({
  flex: { flex: 1 },
  scroll: { padding: 18, paddingBottom: 30 },
  missionBadge: { fontSize: 12, fontWeight: '800', color: GAME.soft, textAlign: 'right', writingDirection: 'rtl' },
  missionTitle: { fontSize: 16, fontWeight: '800', color: GAME.ink, textAlign: 'right', writingDirection: 'rtl', marginTop: 5, lineHeight: 28 },
  missionOp: { color: GAME.blue, fontSize: 18 },
  operation: { backgroundColor: GAME.card, borderRadius: 18, borderWidth: 2, borderColor: '#e5e5e5', paddingVertical: 16, alignItems: 'center', marginBottom: 12 },
  opGrid: { alignItems: 'center' },
  opRow: { flexDirection: 'row', alignItems: 'center' },
  opSign: { width: 30, alignItems: 'center', justifyContent: 'center' },
  plus: { fontSize: 26, fontWeight: '900', color: GAME.soft },
  cell: { width: CELL, height: 40, alignItems: 'center', justifyContent: 'center' },
  carry: { fontSize: 15, fontWeight: '900', color: GAME.red },
  opDigit: { fontSize: 28, fontWeight: '800', color: GAME.ink },
  opLine: { alignSelf: 'stretch', height: 3, borderRadius: 2, backgroundColor: GAME.ink, marginVertical: 6, marginRight: 4 },
  resultCell: {
    borderWidth: 2, borderColor: '#e5e5e5', borderRadius: 10, height: CELL, margin: 1,
  },
  resultDone: { borderColor: '#d7ffb8', backgroundColor: '#f6ffee' },
  resultDigit: { fontSize: 26, fontWeight: '900', color: GAME.ink },
  hintCard: { backgroundColor: '#eef7ff', borderRadius: 14, borderWidth: 2, borderColor: '#bfdcff', padding: 12, marginBottom: 12 },
  hintText: { fontSize: 15, fontWeight: '700', color: '#1e40af', textAlign: 'right', writingDirection: 'rtl', lineHeight: 25 },
  pad: { flexDirection: 'row', flexWrap: 'wrap', justifyContent: 'center', gap: 9 },
  key: {
    width: '17.5%', backgroundColor: GAME.card, borderWidth: 2, borderColor: '#e5e5e5', borderBottomWidth: 4,
    borderRadius: 14, paddingVertical: 12, alignItems: 'center',
  },
  keyText: { fontSize: 22, fontWeight: '800', color: GAME.ink },
})
