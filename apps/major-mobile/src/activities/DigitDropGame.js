import { useRef, useState } from 'react'
import { View, Text, ScrollView, Animated, PanResponder, TouchableOpacity, StyleSheet } from 'react-native'
import { toArabicWords, groupDigits } from './arabicNumbers.js'
import {
  GAME, ChunkyButton, GameHeader, FeedbackBanner, EndScreen, MascotBubble,
  useShake, buzz, tap, praise, retryTitle,
} from './ui.js'
import { COLORS } from '../theme.js'

// Jeu math6-u01 — « أملأ الخانات » : le tableau des خانات du cahier, vivant.
// أستاذ ماجور dicte le nombre en lettres ; l'enfant ATTRAPE les tuiles-chiffres
// et les DÉPOSE dans les cases (drag & drop), comme des aimants sur un tableau.

const GROUPS = [
  { label: 'الوحدات', color: '#1cb0f6', bg: '#e5f7ff' },
  { label: 'الآلاف', color: '#ff9600', bg: '#fff3e0' },
  { label: 'الملايين', color: '#58cc02', bg: '#eaffd6' },
]

// Règle d'or de l'accroche : la 1re mission doit être gagnée en 10 secondes.
const LEVELS = [2, 3, 4, 5, 7]

function randomNumber(d) {
  const first = 1 + Math.floor(Math.random() * 9)
  let s = String(first)
  for (let i = 1; i < d; i++) s += Math.floor(Math.random() * 10)
  return s
}

// Tuile-chiffre draggable (PanResponder — aucun lib externe).
function Tile({ tile, onDrop, onTap, dragging, setDragging }) {
  const pan = useRef(new Animated.ValueXY()).current
  const start = useRef({ x: 0, y: 0 })

  const responder = useRef(
    PanResponder.create({
      onStartShouldSetPanResponder: () => true,
      onMoveShouldSetPanResponder: () => true,
      // Le glissement de la tuile garde la priorité sur le scroll de la page.
      onPanResponderTerminationRequest: () => false,
      onPanResponderGrant: (evt) => {
        start.current = { x: evt.nativeEvent.pageX, y: evt.nativeEvent.pageY }
        setDragging(tile.id)
        tap()
      },
      onPanResponderMove: Animated.event([null, { dx: pan.x, dy: pan.y }], { useNativeDriver: false }),
      onPanResponderRelease: (evt, g) => {
        const moved = Math.abs(g.dx) + Math.abs(g.dy) > 12
        const page = { x: evt.nativeEvent.pageX, y: evt.nativeEvent.pageY }
        pan.setValue({ x: 0, y: 0 })
        setDragging(null)
        if (moved) onDrop(tile.id, page)
        else onTap(tile.id)
      },
      onPanResponderTerminate: () => {
        pan.setValue({ x: 0, y: 0 })
        setDragging(null)
      },
    })
  ).current

  return (
    <Animated.View
      {...responder.panHandlers}
      style={[
        styles.tile,
        { transform: pan.getTranslateTransform() },
        dragging === tile.id && styles.tileDragging,
      ]}
    >
      <Text style={styles.tileText}>{tile.digit}</Text>
    </Animated.View>
  )
}

export default function DigitDropGame({ color = COLORS.royal, onExit }) {
  const [round, setRound] = useState(0)
  const [targets, setTargets] = useState(() => LEVELS.map(randomNumber))
  const [cells, setCells] = useState({}) // { cellIndex: tileId }
  const [wrongCells, setWrongCells] = useState([])
  const [dragging, setDragging] = useState(null)
  const [feedback, setFeedback] = useState(null)
  const [okTitle, setOkTitle] = useState('')
  const [badTitle, setBadTitle] = useState('')
  const [failedThis, setFailedThis] = useState(false)
  const [stars, setStars] = useState(0)
  const [streak, setStreak] = useState(0)
  const [done, setDone] = useState(false)
  const [shakeStyle, shake] = useShake()
  const cellRefs = useRef({})

  const target = targets[round] // chaîne de chiffres, ex. "245067"
  const L = target.length
  const words = toArabicWords(parseInt(target, 10))

  // Tuiles : les chiffres du nombre, mélangés (stables par round).
  const tiles = useRef(null)
  const tilesRound = useRef(-1)
  if (tilesRound.current !== round) {
    tilesRound.current = round
    tiles.current = target
      .split('')
      .map((digit, i) => ({ id: `t${round}-${i}`, digit }))
      .sort(() => Math.random() - 0.5)
  }

  const placedIds = new Set(Object.values(cells))
  const trayTiles = tiles.current.filter((t) => !placedIds.has(t.id))
  const allPlaced = Object.keys(cells).length === L

  // Dépôt : trouve la case sous le doigt (mesure des cases à la volée).
  function handleDrop(tileId, page) {
    const entries = Object.entries(cellRefs.current).filter(([k]) => parseInt(k, 10) < L)
    let placed = false
    let pending = entries.length
    if (!pending) return
    entries.forEach(([idxStr, ref]) => {
      if (!ref || !ref.measureInWindow) { if (--pending === 0 && !placed) buzz(false); return }
      ref.measureInWindow((x, y, w, h) => {
        const idx = parseInt(idxStr, 10)
        if (!placed && page.x >= x - 6 && page.x <= x + w + 6 && page.y >= y - 10 && page.y <= y + h + 10) {
          placed = true
          setCells((c) => {
            const next = { ...c }
            // La case était occupée → l'ancienne tuile repart au plateau.
            Object.keys(next).forEach((k) => { if (next[k] === tileId) delete next[k] })
            next[idx] = tileId
            return next
          })
          setWrongCells([])
          tap()
        }
        if (--pending === 0 && !placed) buzz(false)
      })
    })
  }

  // Tap simple : la tuile va dans la première case vide (depuis la gauche).
  function handleTap(tileId) {
    for (let i = 0; i < L; i++) {
      if (cells[i] === undefined) {
        setCells((c) => ({ ...c, [i]: tileId }))
        setWrongCells([])
        return
      }
    }
  }

  function removeFromCell(idx) {
    if (feedback === 'ok') return
    tap()
    setCells((c) => {
      const next = { ...c }
      delete next[idx]
      return next
    })
    setWrongCells([])
  }

  function check() {
    const bad = []
    for (let i = 0; i < L; i++) {
      const tile = tiles.current.find((t) => t.id === cells[i])
      if (!tile || tile.digit !== target[i]) bad.push(i)
    }
    if (bad.length === 0) {
      buzz(true)
      if (!failedThis) { setStars((s) => s + 1); setStreak((s) => s + 1); setOkTitle(praise()) }
      else setOkTitle('أحسنت! 👏')
      setFeedback('ok')
    } else {
      buzz(false); shake()
      setWrongCells(bad)
      setFailedThis(true); setStreak(0)
      setBadTitle(retryTitle())
      setFeedback('bad')
    }
  }

  function retry() {
    // Les tuiles mal placées repartent au plateau.
    setCells((c) => {
      const next = { ...c }
      wrongCells.forEach((i) => delete next[i])
      return next
    })
    setWrongCells([])
    setFeedback(null)
  }

  function next() {
    if (round + 1 >= targets.length) { setDone(true); return }
    setRound(round + 1)
    setCells({}); setWrongCells([]); setFeedback(null); setFailedThis(false)
  }

  function replay() {
    setTargets(LEVELS.map(randomNumber))
    setRound(0); setCells({}); setWrongCells([]); setFeedback(null)
    setFailedThis(false); setStars(0); setStreak(0); setDone(false)
  }

  if (done) return <EndScreen stars={stars} total={targets.length} onReplay={replay} onExit={onExit} color={color} />

  // Cases : index 0 = chiffre de gauche (grand) … affichées naturellement LTR,
  // groupées par 3 EN PARTANT DE LA DROITE (comme la règle du cahier).
  const groupOf = (i) => Math.floor((L - 1 - i) / 3) // 0=وحدات, 1=آلاف, 2=ملايين

  return (
    <View style={styles.flex}>
      <ScrollView contentContainerStyle={styles.scroll} scrollEnabled={dragging === null}>
        <GameHeader index={round} total={targets.length} stars={stars} streak={streak} />

        <MascotBubble>
          <Text style={styles.badge}>🎯 المهمة {round + 1} من {targets.length}</Text>
          <Text style={styles.q}>ضع كل رقم في خانته لتكوّن العدد:</Text>
          <Text style={styles.words}>« {words} »</Text>
        </MascotBubble>

        <Animated.View style={[styles.board, shakeStyle]}>
          <View style={styles.groupLabels}>
            {[...new Set(Array.from({ length: L }, (_, i) => groupOf(i)))].sort((a, b) => b - a).map((g) => {
              const count = Array.from({ length: L }, (_, i) => groupOf(i)).filter((x) => x === g).length
              return (
                <View key={g} style={[styles.groupLabel, { backgroundColor: GROUPS[g].bg, flex: count }]}>
                  <Text style={[styles.groupLabelText, { color: GROUPS[g].color }]}>{GROUPS[g].label}</Text>
                </View>
              )
            })}
          </View>
          <View style={styles.cellsRow}>
            {Array.from({ length: L }, (_, i) => {
              const tile = tiles.current.find((t) => t.id === cells[i])
              const g = GROUPS[groupOf(i)]
              const isWrong = wrongCells.includes(i)
              return (
                <TouchableOpacity
                  key={i}
                  ref={(r) => { cellRefs.current[i] = r }}
                  activeOpacity={tile ? 0.6 : 1}
                  onPress={() => tile && removeFromCell(i)}
                  style={[
                    styles.cell,
                    { borderColor: g.color + '66' },
                    i > 0 && groupOf(i) !== groupOf(i - 1) && { marginLeft: 10 },
                    tile && { backgroundColor: g.bg, borderStyle: 'solid' },
                    isWrong && styles.cellWrong,
                    feedback === 'ok' && styles.cellOk,
                  ]}
                >
                  <Text style={[styles.cellText, feedback === 'ok' && { color: GAME.greenInk }]}>
                    {tile ? tile.digit : ''}
                  </Text>
                </TouchableOpacity>
              )
            })}
          </View>
          {feedback === 'ok' && (
            <Text style={styles.readBack}>{groupDigits(target)} ✓</Text>
          )}
        </Animated.View>

        <Text style={styles.trayLabel}>
          {trayTiles.length ? 'اسحب الأرقام إلى خاناتها 👆 (أو اضغط عليها)' : 'كل الأرقام في مكانها — تحقّق!'}
        </Text>
        <View style={styles.tray}>
          {trayTiles.map((t) => (
            <Tile key={t.id} tile={t} onDrop={handleDrop} onTap={handleTap} dragging={dragging} setDragging={setDragging} />
          ))}
        </View>

        {feedback !== 'ok' && (
          <ChunkyButton label="تحقّق ✅" color={GAME.green} disabled={!allPlaced} onPress={check} />
        )}
      </ScrollView>

      {feedback === 'ok' && (
        <FeedbackBanner
          ok
          title={okTitle}
          body={`${groupDigits(target)} = ${words}`}
          actionLabel={round + 1 >= targets.length ? 'أرى نتيجتي 🏁' : 'المهمة التالية ←'}
          onAction={next}
        />
      )}
      {feedback === 'bad' && (
        <FeedbackBanner
          ok={false}
          title={badTitle}
          body={`${wrongCells.length} ${wrongCells.length === 1 ? 'خانة ليست' : 'خانات ليست'} في مكانها الصحيح — الخانات الحمراء. تذكّر: أقرأ المجموعات من اليمين!`}
          actionLabel="أحاول من جديد"
          onAction={retry}
        />
      )}
    </View>
  )
}

const CELL = 42

const styles = StyleSheet.create({
  flex: { flex: 1 },
  scroll: { padding: 18, paddingBottom: 30 },
  badge: { fontSize: 12, fontWeight: '800', color: GAME.soft, textAlign: 'right', writingDirection: 'rtl' },
  q: { fontSize: 16, fontWeight: '800', color: GAME.ink, textAlign: 'right', writingDirection: 'rtl', marginTop: 6 },
  words: { fontSize: 18, fontWeight: '800', color: GAME.blue, textAlign: 'right', writingDirection: 'rtl', lineHeight: 31, marginTop: 6 },
  board: {
    backgroundColor: GAME.card, borderRadius: 18, borderWidth: 2, borderColor: '#e5e5e5',
    padding: 14, marginBottom: 14, alignItems: 'center',
  },
  groupLabels: { flexDirection: 'row', gap: 10, alignSelf: 'stretch', justifyContent: 'center', marginBottom: 8 },
  groupLabel: { borderRadius: 8, paddingVertical: 4, alignItems: 'center' },
  groupLabelText: { fontSize: 12, fontWeight: '800', writingDirection: 'rtl' },
  cellsRow: { flexDirection: 'row', gap: 5, justifyContent: 'center' },
  cell: {
    width: CELL, height: CELL + 8, borderRadius: 10, borderWidth: 2, borderStyle: 'dashed',
    alignItems: 'center', justifyContent: 'center', backgroundColor: '#fafafa',
  },
  cellWrong: { borderColor: GAME.red, backgroundColor: '#fff1f1', borderStyle: 'solid' },
  cellOk: { borderColor: GAME.green, borderStyle: 'solid' },
  cellText: { fontSize: 22, fontWeight: '900', color: GAME.ink },
  readBack: { marginTop: 10, fontSize: 16, fontWeight: '800', color: GAME.greenInk },
  trayLabel: { fontSize: 13, fontWeight: '700', color: GAME.soft, textAlign: 'center', writingDirection: 'rtl', marginBottom: 10 },
  tray: {
    flexDirection: 'row', flexWrap: 'wrap', gap: 10, justifyContent: 'center',
    minHeight: 60, marginBottom: 12,
  },
  tile: {
    width: 50, height: 54, borderRadius: 12, backgroundColor: '#fff',
    borderWidth: 2, borderColor: '#d8dbe2', borderBottomWidth: 5,
    alignItems: 'center', justifyContent: 'center',
    shadowColor: '#101828', shadowOpacity: 0.08, shadowRadius: 6, shadowOffset: { width: 0, height: 3 }, elevation: 3,
    zIndex: 10,
  },
  tileDragging: { borderColor: '#1cb0f6', zIndex: 100, elevation: 10, transform: [{ scale: 1.15 }] },
  tileText: { fontSize: 24, fontWeight: '900', color: GAME.ink },
})
