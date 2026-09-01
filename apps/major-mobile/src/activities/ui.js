// Kit UI des activités gamifiées — style « Duolingo » :
// gros boutons à bord épais, barre de progression, bannière de
// feedback vert/rouge, étoiles, confettis, mascotte, écran de victoire.

import { useEffect, useMemo, useRef } from 'react'
import { View, Text, TouchableOpacity, Animated, StyleSheet } from 'react-native'
import * as Haptics from 'expo-haptics'
import { sfxCorrect, sfxWrong, sfxWin, sfxTap, voicePraise } from '../lib/sound.js'

export const GAME = {
  green: '#58cc02',
  greenBg: '#d7ffb8',
  greenInk: '#3f8f00',
  red: '#ff4b4b',
  redBg: '#ffdfe0',
  redInk: '#ea2b2b',
  gold: '#ffc800',
  blue: '#1cb0f6',
  ink: '#3c3c3c',
  soft: '#8a8a8a',
  track: '#e5e5e5',
  card: '#ffffff',
}

// Compliments variés — un enfant ne doit jamais lire deux fois le même.
const PRAISES = ['أحسنت يا بطل! 👏', 'رائع! 🌟', 'ممتاز! 🎉', 'عمل عظيم! 💪', 'أنت نجم حقيقي! ⭐', 'واو! 🤩', 'هكذا يفعل الأبطال! 🦸']
export function praise() {
  return PRAISES[Math.floor(Math.random() * PRAISES.length)]
}

const RETRY_TITLES = ['ليس بعد — حاول مرة أخرى! 💪', 'قريب جدًّا! ركّز قليلًا 🔍', 'لا بأس، الخطأ يعلّمنا! 🌱']
export function retryTitle() {
  return RETRY_TITLES[Math.floor(Math.random() * RETRY_TITLES.length)]
}

// Assombrit une couleur hex pour le bord 3D des boutons.
export function darken(hex, f = 0.72) {
  const v = hex.replace('#', '')
  const n = parseInt(v.length === 3 ? v.split('').map((c) => c + c).join('') : v, 16)
  const d = (x) => Math.round(x * f)
  return `#${[d(n >> 16 & 255), d(n >> 8 & 255), d(n & 255)].map((x) => x.toString(16).padStart(2, '0')).join('')}`
}

export function buzz(ok) {
  try {
    Haptics.notificationAsync(ok ? Haptics.NotificationFeedbackType.Success : Haptics.NotificationFeedbackType.Error)
  } catch {}
  if (ok) sfxCorrect()
  else sfxWrong()
}

export function tap() {
  try { Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Light) } catch {}
  sfxTap()
}

// Secousse horizontale (mauvaise réponse).
export function useShake() {
  const x = useRef(new Animated.Value(0)).current
  const style = { transform: [{ translateX: x }] }
  const shake = () => {
    x.setValue(0)
    Animated.sequence(
      [10, -10, 8, -8, 5, -5, 0].map((to) =>
        Animated.timing(x, { toValue: to, duration: 55, useNativeDriver: true })
      )
    ).start()
  }
  return [style, shake]
}

// Rebond joyeux (bonne réponse).
export function usePop() {
  const s = useRef(new Animated.Value(1)).current
  const style = { transform: [{ scale: s }] }
  const pop = () => {
    s.setValue(0.6)
    Animated.spring(s, { toValue: 1, friction: 3, tension: 160, useNativeDriver: true }).start()
  }
  return [style, pop]
}

// Pluie de confettis emoji — se rejoue à chaque changement de burstKey.
const CONFETTI = ['🎉', '⭐', '✨', '🎊', '💛', '💙', '🧡']
function Particle({ delay, left, emoji, drift }) {
  const t = useRef(new Animated.Value(0)).current
  useEffect(() => {
    Animated.timing(t, { toValue: 1, duration: 1400, delay, useNativeDriver: true }).start()
  }, [])
  return (
    <Animated.Text
      style={{
        position: 'absolute', top: -10, left: `${left}%`, fontSize: 22,
        opacity: t.interpolate({ inputRange: [0, 0.7, 1], outputRange: [1, 1, 0] }),
        transform: [
          { translateY: t.interpolate({ inputRange: [0, 1], outputRange: [-20, 300] }) },
          { translateX: t.interpolate({ inputRange: [0, 1], outputRange: [0, drift] }) },
          { rotate: t.interpolate({ inputRange: [0, 1], outputRange: ['0deg', `${drift * 8}deg`] }) },
        ],
      }}
    >
      {emoji}
    </Animated.Text>
  )
}

export function ConfettiBurst({ burstKey }) {
  const parts = useMemo(
    () =>
      Array.from({ length: 16 }, (_, i) => ({
        id: `${burstKey}-${i}`,
        left: Math.random() * 92,
        delay: Math.random() * 350,
        drift: (Math.random() - 0.5) * 80,
        emoji: CONFETTI[Math.floor(Math.random() * CONFETTI.length)],
      })),
    [burstKey]
  )
  return (
    <View pointerEvents="none" style={StyleSheet.absoluteFill}>
      {parts.map((p) => <Particle key={p.id} {...p} />)}
    </View>
  )
}

// Vraie écriture mathématique : fraction verticale (بسط sur مقام).
export function Fraction({ num, den, size = 22, color = GAME.ink, style }) {
  return (
    <View style={[{ alignItems: 'center', paddingHorizontal: 6 }, style]}>
      <Text style={{ fontSize: size, fontWeight: '900', color, lineHeight: size + 4 }}>{num}</Text>
      <View style={{ alignSelf: 'stretch', height: Math.max(2, size / 9), borderRadius: 2, backgroundColor: color }} />
      <Text style={{ fontSize: size, fontWeight: '900', color: GAME.ink, lineHeight: size + 4 }}>{den}</Text>
    </View>
  )
}

// La mascotte أستاذ ماجور qui parle dans une bulle.
export function MascotBubble({ text, children }) {
  return (
    <View style={styles.mascotRow}>
      <View style={styles.mascotAvatar}>
        <Text style={styles.mascotEmoji}>🧑🏽‍🏫</Text>
      </View>
      <View style={styles.bubble}>
        {!!text && <Text style={styles.bubbleText}>{text}</Text>}
        {children}
      </View>
    </View>
  )
}

// Gros bouton plein avec bord inférieur épais (effet 3D Duolingo).
export function ChunkyButton({ label, color = GAME.green, onPress, disabled, small, textColor = '#fff', style }) {
  return (
    <TouchableOpacity
      style={[
        styles.chunky,
        small && styles.chunkySmall,
        { backgroundColor: color, borderBottomColor: darken(color) },
        disabled && styles.chunkyDisabled,
        style,
      ]}
      activeOpacity={0.8}
      disabled={disabled}
      onPress={() => { tap(); onPress && onPress() }}
    >
      <Text style={[styles.chunkyText, small && styles.chunkyTextSmall, { color: textColor }]}>{label}</Text>
    </TouchableOpacity>
  )
}

// Barre de progression + étoiles + série de bonnes réponses.
export function GameHeader({ index, total, stars, streak = 0 }) {
  const pct = Math.round((index / total) * 100)
  return (
    <View style={styles.headerRow}>
      <Text style={styles.headerStars}>⭐ {stars}</Text>
      <View style={styles.track}>
        <View style={[styles.fill, { width: `${pct}%` }]} />
      </View>
      {streak >= 2 && <Text style={styles.headerStreak}>🔥 {streak}</Text>}
    </View>
  )
}

// Bannière de feedback en bas d'écran (vert = bravo, rouge = réessaie).
export function FeedbackBanner({ ok, title, body, actionLabel, onAction }) {
  return (
    <View style={[styles.banner, { backgroundColor: ok ? GAME.greenBg : GAME.redBg }]}>
      <Text style={[styles.bannerTitle, { color: ok ? GAME.greenInk : GAME.redInk }]}>{title}</Text>
      {!!body && <Text style={[styles.bannerBody, { color: ok ? GAME.greenInk : GAME.redInk }]}>{body}</Text>}
      <ChunkyButton label={actionLabel} color={ok ? GAME.green : GAME.red} onPress={onAction} />
    </View>
  )
}

// Écran de fin : confettis, trophée, étoiles, rejouer / continuer —
// avec le « tada » et la voix d'أستاذ ماجور.
export function EndScreen({ stars, total, onReplay, onExit, color = GAME.green }) {
  const perfect = stars >= total
  useEffect(() => {
    sfxWin()
    if (stars >= Math.max(1, total - 1)) {
      const t = setTimeout(voicePraise, 700)
      return () => clearTimeout(t)
    }
  }, [])
  return (
    <View style={styles.endWrap}>
      <ConfettiBurst burstKey="end" />
      <Text style={styles.endEmoji}>{perfect ? '🏆' : '🎉'}</Text>
      <Text style={styles.endTitle}>{perfect ? 'ممتاز يا بطل!' : 'أتممت التحدي!'}</Text>
      <Text style={styles.endStars}>
        {'⭐'.repeat(Math.max(1, stars))}{'☆'.repeat(Math.max(0, total - Math.max(1, stars)))}
      </Text>
      <Text style={styles.endScore}>{stars} من {total} نجوم</Text>
      <Text style={styles.endBody}>
        {perfect ? 'كل الإجابات صحيحة من المحاولة الأولى! 🇲🇷' : 'واصل التدرّب لتجمع كل النجوم!'}
      </Text>
      <View style={styles.endBtns}>
        <ChunkyButton label="أعيد التحدي 🔄" color={color} onPress={onReplay} />
        {!!onExit && <ChunkyButton label="أكمل" color="#e5e5e5" textColor={GAME.ink} onPress={onExit} />}
      </View>
    </View>
  )
}

const styles = StyleSheet.create({
  chunky: {
    borderRadius: 16, borderBottomWidth: 5,
    paddingVertical: 15, paddingHorizontal: 24, alignItems: 'center', marginTop: 10,
  },
  chunkySmall: { paddingVertical: 10, paddingHorizontal: 16, borderBottomWidth: 4 },
  chunkyDisabled: { opacity: 0.35 },
  chunkyText: { fontSize: 18, fontWeight: '800', writingDirection: 'rtl' },
  chunkyTextSmall: { fontSize: 15 },
  headerRow: { flexDirection: 'row-reverse', alignItems: 'center', gap: 12, marginBottom: 16 },
  headerStars: { fontSize: 16, fontWeight: '800', color: GAME.ink },
  headerStreak: { fontSize: 15, fontWeight: '800', color: '#ff9600' },
  track: { flex: 1, height: 14, borderRadius: 8, backgroundColor: GAME.track, overflow: 'hidden' },
  fill: { height: 14, borderRadius: 8, backgroundColor: GAME.green },
  mascotRow: { flexDirection: 'row-reverse', alignItems: 'flex-end', gap: 10, marginBottom: 14 },
  mascotAvatar: {
    width: 52, height: 52, borderRadius: 26, backgroundColor: '#fff',
    alignItems: 'center', justifyContent: 'center',
    shadowColor: '#101828', shadowOpacity: 0.08, shadowRadius: 8, shadowOffset: { width: 0, height: 3 }, elevation: 2,
  },
  mascotEmoji: { fontSize: 28 },
  bubble: {
    flex: 1, backgroundColor: '#fff', borderRadius: 18, borderBottomRightRadius: 4,
    padding: 14, borderWidth: 2, borderColor: '#e5e5e5',
  },
  bubbleText: { fontSize: 16, fontWeight: '700', color: GAME.ink, textAlign: 'right', writingDirection: 'rtl', lineHeight: 27 },
  banner: { borderTopLeftRadius: 22, borderTopRightRadius: 22, padding: 18, paddingBottom: 26 },
  bannerTitle: { fontSize: 19, fontWeight: '900', textAlign: 'right', writingDirection: 'rtl' },
  bannerBody: { fontSize: 15, fontWeight: '600', textAlign: 'right', writingDirection: 'rtl', marginTop: 4, lineHeight: 24 },
  endWrap: { flex: 1, alignItems: 'center', justifyContent: 'center', padding: 28 },
  endEmoji: { fontSize: 74 },
  endTitle: { fontSize: 28, fontWeight: '900', color: GAME.ink, marginTop: 12, writingDirection: 'rtl' },
  endStars: { fontSize: 34, marginTop: 14, letterSpacing: 4 },
  endScore: { fontSize: 16, fontWeight: '700', color: GAME.soft, marginTop: 6, writingDirection: 'rtl' },
  endBody: { fontSize: 16, color: GAME.soft, textAlign: 'center', marginTop: 10, lineHeight: 26, writingDirection: 'rtl' },
  endBtns: { alignSelf: 'stretch', marginTop: 22 },
})
