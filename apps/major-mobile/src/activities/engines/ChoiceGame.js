import { useState } from 'react'
import { View, Text, TouchableOpacity, ScrollView, Animated, StyleSheet } from 'react-native'
import {
  GAME, GameHeader, FeedbackBanner, EndScreen, MascotBubble,
  useShake, usePop, buzz, tap, praise, retryTitle,
} from '../ui.js'
import { COLORS } from '../../theme.js'

// Moteur générique « j'observe et je choisis » : question (avec parfois un
// dessin géométrique) + 2-4 réponses. Missions par unité :
// makeMissions → [{ q, choices, correct, hint, visual? }]
// visual: { type: 'angle', deg } | { type: 'lines', kind: 'par'|'sec'|'perp' }
//         | { type: 'big', text }

function AngleVisual({ deg }) {
  return (
    <View style={vis.box}>
      <View style={vis.angleWrap}>
        <View style={[vis.ray, { transform: [{ rotate: '0deg' }] }]} />
        <View style={[vis.ray, { transform: [{ rotate: `-${deg}deg` }] }]} />
        <View style={vis.vertex} />
      </View>
    </View>
  )
}

function LinesVisual({ kind }) {
  return (
    <View style={vis.box}>
      {kind === 'par' && (
        <View style={{ gap: 26 }}>
          <View style={vis.line} />
          <View style={vis.line} />
        </View>
      )}
      {kind === 'sec' && (
        <View style={vis.cross}>
          <View style={[vis.line, { transform: [{ rotate: '20deg' }] }]} />
          <View style={[vis.line, { position: 'absolute', transform: [{ rotate: '-35deg' }] }]} />
        </View>
      )}
      {kind === 'perp' && (
        <View style={vis.cross}>
          <View style={vis.line} />
          <View style={[vis.line, { position: 'absolute', transform: [{ rotate: '90deg' }] }]} />
        </View>
      )}
    </View>
  )
}

function BigVisual({ text }) {
  return (
    <View style={vis.box}>
      <Text style={vis.bigText}>{text}</Text>
    </View>
  )
}

export default function ChoiceGame({ color = COLORS.royal, onExit, makeMissions }) {
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

  function choose(i) {
    if (feedback === 'ok') return
    tap()
    if (i === m.correct) {
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
          <Text style={styles.q}>{m.q}</Text>
        </MascotBubble>

        {m.visual && (
          <Animated.View style={[shakeStyle, popStyle]}>
            {m.visual.type === 'angle' && <AngleVisual deg={m.visual.deg} />}
            {m.visual.type === 'lines' && <LinesVisual kind={m.visual.kind} />}
            {m.visual.type === 'big' && <BigVisual text={m.visual.text} />}
          </Animated.View>
        )}

        <View style={styles.choices}>
          {m.choices.map((c, i) => (
            <TouchableOpacity
              key={i}
              style={[
                styles.choice,
                feedback === 'ok' && i === m.correct && styles.choiceOk,
              ]}
              activeOpacity={0.7}
              disabled={feedback === 'ok'}
              onPress={() => choose(i)}
            >
              <Text style={[styles.choiceText, feedback === 'ok' && i === m.correct && { color: GAME.greenInk }]}>{c}</Text>
            </TouchableOpacity>
          ))}
        </View>
      </ScrollView>

      {feedback === 'ok' && (
        <FeedbackBanner
          ok
          title={okTitle}
          body={`الجواب: ${m.choices[m.correct]}`}
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

const vis = StyleSheet.create({
  box: {
    backgroundColor: GAME.card, borderWidth: 2, borderColor: '#e5e5e5', borderRadius: 18,
    height: 160, alignItems: 'center', justifyContent: 'center', marginBottom: 14, overflow: 'hidden',
  },
  angleWrap: { width: 120, height: 100, justifyContent: 'flex-end' },
  ray: { position: 'absolute', bottom: 8, left: 8, width: 100, height: 4, borderRadius: 2, backgroundColor: '#1cb0f6', transformOrigin: 'left center' },
  vertex: { position: 'absolute', bottom: 4, left: 4, width: 12, height: 12, borderRadius: 6, backgroundColor: '#0a6ea6' },
  cross: { alignItems: 'center', justifyContent: 'center', width: 160, height: 120 },
  line: { width: 150, height: 4, borderRadius: 2, backgroundColor: '#1cb0f6' },
  bigText: { fontSize: 30, fontWeight: '900', color: GAME.ink, textAlign: 'center', writingDirection: 'rtl', lineHeight: 46, paddingHorizontal: 10 },
})

const styles = StyleSheet.create({
  flex: { flex: 1 },
  scroll: { padding: 18, paddingBottom: 30 },
  badge: { fontSize: 12, fontWeight: '800', color: GAME.soft, textAlign: 'right', writingDirection: 'rtl' },
  q: { fontSize: 17, fontWeight: '800', color: GAME.ink, textAlign: 'right', writingDirection: 'rtl', marginTop: 6, lineHeight: 30 },
  choices: { gap: 10 },
  choice: {
    backgroundColor: GAME.card, borderWidth: 2, borderColor: '#e5e5e5', borderBottomWidth: 4,
    borderRadius: 14, paddingVertical: 15, paddingHorizontal: 16, alignItems: 'center',
  },
  choiceOk: { borderColor: GAME.green, backgroundColor: '#f2ffe5' },
  choiceText: { fontSize: 17, fontWeight: '800', color: GAME.ink, writingDirection: 'rtl' },
})
