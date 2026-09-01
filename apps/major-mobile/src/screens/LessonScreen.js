import { useEffect, useLayoutEffect, useMemo, useRef, useState } from 'react'
import { View, Text, ScrollView, TouchableOpacity, Animated, StyleSheet, ActivityIndicator, Linking } from 'react-native'
import { SafeAreaView } from 'react-native-safe-area-context'
import { useEvent } from 'expo'
import { useVideoPlayer, VideoView } from 'expo-video'
import { getLessonById, getQuizForLesson } from '../lib/lessons.js'
import { getVideoUrl } from '../lib/videos.js'
import { getActivityForLesson } from '../activities/index.js'
import { COLORS, RADIUS } from '../theme.js'
import { ChunkyButton, MascotBubble, tap } from '../activities/ui.js'

// Leçon façon Brilliant : une idée par écran, un seul geste à la fois.
// vidéo → l'idée → les points → la règle → agir (activité / quiz).
// Présentation « pour enfant » : la mascotte raconte le résumé en bulles
// de dialogue animées, les points sont des cartes à badges qui tombent
// en cascade, la règle est une carte dorée.

// Lecteur avec états visibles : jamais d'écran noir muet — l'enfant voit
// « chargement », ou une erreur claire avec réessayer / secours navigateur.
function VideoCard({ url }) {
  const player = useVideoPlayer(url)
  const { status } = useEvent(player, 'statusChange', { status: player.status })
  return (
    <View style={styles.videoCard}>
      <VideoView player={player} style={styles.video} contentFit="contain" nativeControls />
      {status === 'loading' && (
        <View style={styles.videoOverlay} pointerEvents="none">
          <ActivityIndicator color="#fff" size="large" />
          <Text style={styles.videoOverlayText}>جاري تحميل الفيديو…</Text>
        </View>
      )}
      {status === 'error' && (
        <View style={styles.videoOverlay}>
          <Text style={styles.videoOverlayText}>تعذّر تشغيل الفيديو 😕{'\n'}تأكّد من الاتصال بالإنترنت</Text>
          <TouchableOpacity style={styles.videoRetryBtn} activeOpacity={0.8} onPress={() => { tap(); player.replace(url) }}>
            <Text style={styles.videoRetryText}>🔄 إعادة المحاولة</Text>
          </TouchableOpacity>
          <TouchableOpacity activeOpacity={0.8} onPress={() => Linking.openURL(url)}>
            <Text style={styles.videoBrowserText}>أشاهده في المتصفح 🌐</Text>
          </TouchableOpacity>
        </View>
      )}
    </View>
  )
}

// Apparition douce (fondu + glissement) avec délai — pour la cascade.
function Reveal({ delay = 0, children, style }) {
  const t = useRef(new Animated.Value(0)).current
  useEffect(() => {
    Animated.timing(t, { toValue: 1, duration: 420, delay, useNativeDriver: true }).start()
  }, [])
  return (
    <Animated.View
      style={[
        style,
        {
          opacity: t,
          transform: [{ translateY: t.interpolate({ inputRange: [0, 1], outputRange: [16, 0] }) }],
        },
      ]}
    >
      {children}
    </Animated.View>
  )
}

// Découpe le résumé en petites bulles de dialogue (1-2 phrases chacune) —
// un enfant lit des messages courts, jamais un pavé.
function toBubbles(text) {
  const sentences = (String(text).match(/[^.!؟]+[.!؟]*/g) || [text]).map((s) => s.trim()).filter(Boolean)
  const bubbles = []
  for (const s of sentences) {
    const last = bubbles[bubbles.length - 1]
    if (last && (last.length + s.length < 90 || s.length < 25)) bubbles[bubbles.length - 1] = `${last} ${s}`
    else bubbles.push(s)
  }
  return bubbles
}

const POINT_EMOJIS = ['🎯', '⭐', '🚀', '💡', '🏆', '🔑']

export default function LessonScreen({ route, navigation }) {
  const { lessonId } = route.params
  const lesson = getLessonById(lessonId)
  const [idx, setIdx] = useState(0)

  useLayoutEffect(() => {
    navigation.setOptions({ title: lesson?.subjectLabel || 'الدرس' })
  }, [navigation, lesson])

  const steps = useMemo(() => {
    if (!lesson) return []
    const s = []
    const videoUrl = getVideoUrl(lessonId)
    if (videoUrl) s.push({ type: 'video', videoUrl })
    if (lesson.summary) s.push({ type: 'summary' })
    if (Array.isArray(lesson.keyPoints) && lesson.keyPoints.length) s.push({ type: 'points' })
    if (lesson.rule || lesson.tip) s.push({ type: 'rule' })
    s.push({ type: 'actions' })
    return s
  }, [lessonId, lesson])

  const bubbles = useMemo(() => (lesson?.summary ? toBubbles(lesson.summary) : []), [lesson])

  if (!lesson) {
    return <SafeAreaView style={styles.safe}><Text style={styles.empty}>لم أجد هذا الدرس.</Text></SafeAreaView>
  }

  const color = lesson.subjectColor || COLORS.royal
  const tint = `${color}16`
  const quiz = getQuizForLesson(lesson)
  const activity = getActivityForLesson(lessonId)
  const tip = (lesson.tip || '').replace(/^💡\s*أستاذ ماجور ينصح\s*[::]\s*/, '')
  const step = steps[idx]
  const last = idx === steps.length - 1

  const STEP_TITLES = {
    video: 'أشاهد الشرح 🎬',
    summary: 'الفكرة 💡',
    points: 'أتذكّر 🧠',
    rule: 'القاعدة الذهبية',
    actions: 'جاهز؟ 🚀',
  }

  return (
    <SafeAreaView style={styles.safe} edges={['bottom']}>
      <View style={styles.progressWrap}>
        {steps.map((_, i) => (
          <View key={i} style={[styles.progressSeg, i <= idx && { backgroundColor: color }]} />
        ))}
      </View>

      <ScrollView contentContainerStyle={styles.scroll} showsVerticalScrollIndicator={false}>
        <View style={styles.titleRow}>
          <View style={[styles.emojiChip, { backgroundColor: tint }]}>
            <Text style={styles.emojiChipText}>{lesson.emoji}</Text>
          </View>
          <Text style={styles.lessonTitle}>{lesson.title}</Text>
        </View>
        <Text style={[styles.stepTitle, { color: step.type === 'rule' ? '#b45309' : color }]}>
          {STEP_TITLES[step.type]}
        </Text>

        {step.type === 'video' && (
          <>
            <VideoCard url={step.videoUrl} />
            <Text style={styles.caption}>دقيقتان من الشرح — ثم نتدرّب معًا</Text>
          </>
        )}

        {step.type === 'summary' && (
          <View key={`summary-${idx}`}>
            {bubbles.map((b, i) => (
              <Reveal key={i} delay={200 + i * 650}>
                <View style={styles.talkRow}>
                  {i === 0 ? (
                    <View style={styles.talkAvatar}>
                      <Text style={styles.talkAvatarEmoji}>🧑🏽‍🏫</Text>
                    </View>
                  ) : (
                    <View style={styles.talkAvatarSpace} />
                  )}
                  <View style={[styles.talkBubble, i === 0 && styles.talkBubbleFirst, { borderColor: `${color}44` }]}>
                    <Text style={styles.talkText}>{b}</Text>
                  </View>
                </View>
              </Reveal>
            ))}
          </View>
        )}

        {step.type === 'points' && (
          <View key={`points-${idx}`}>
            {lesson.keyPoints.map((kp, i) => (
              <Reveal key={i} delay={150 + i * 220}>
                <View style={[styles.pointCard, { borderColor: `${color}33` }]}>
                  <View style={[styles.pointBadge, { backgroundColor: tint }]}>
                    <Text style={styles.pointBadgeEmoji}>{POINT_EMOJIS[i % POINT_EMOJIS.length]}</Text>
                    <Text style={[styles.pointBadgeNum, { color }]}>{i + 1}</Text>
                  </View>
                  <Text style={styles.pointText}>{kp}</Text>
                </View>
              </Reveal>
            ))}
          </View>
        )}

        {step.type === 'rule' && (
          <View key={`rule-${idx}`}>
            {!!lesson.rule && (
              <Reveal>
                <View style={styles.ruleCard}>
                  <Text style={styles.ruleEmoji}>📜</Text>
                  <Text style={styles.ruleText}>{lesson.rule}</Text>
                  <View style={styles.ruleStars}>
                    <Text style={styles.ruleStarsText}>⭐ ⭐ ⭐</Text>
                  </View>
                </View>
              </Reveal>
            )}
            {!!tip && (
              <Reveal delay={500} style={{ marginTop: 18 }}>
                <MascotBubble text={`💡 ${tip}`} />
              </Reveal>
            )}
          </View>
        )}

        {step.type === 'actions' && (
          <View style={styles.actionsWrap} key={`actions-${idx}`}>
            <Reveal>
              <Text style={styles.actionsEmoji}>🚀</Text>
              {!!lesson.encouragement && <MascotBubble text={lesson.encouragement} />}
            </Reveal>
            <Reveal delay={350}>
              {!!activity && (
                <ChunkyButton
                  label="أجرّب بنفسي 🎮"
                  color={COLORS.card}
                  textColor={color}
                  style={{ borderWidth: 1.5, borderColor: color, borderBottomWidth: 4, borderBottomColor: color }}
                  onPress={() => navigation.navigate('Activity', { lessonId })}
                />
              )}
              <ChunkyButton
                label={quiz.length ? 'أبدأ الاختبار' : 'الاختبار قريبًا'}
                color={color}
                disabled={quiz.length === 0}
                onPress={() => navigation.navigate('Quiz', { lessonId })}
              />
            </Reveal>
          </View>
        )}
      </ScrollView>

      {!last && (
        <View style={styles.footer}>
          {idx > 0 && (
            <TouchableOpacity style={styles.backBtn} onPress={() => { tap(); setIdx(idx - 1) }}>
              <Text style={styles.backText}>السابق</Text>
            </TouchableOpacity>
          )}
          <ChunkyButton
            label="متابعة"
            color={color}
            style={{ flex: 1, marginTop: 0 }}
            onPress={() => setIdx(idx + 1)}
          />
          {!!activity && (
            <TouchableOpacity
              style={[styles.practiceBtn, { borderColor: color }]}
              activeOpacity={0.7}
              onPress={() => { tap(); navigation.navigate('Activity', { lessonId }) }}
            >
              <Text style={styles.practiceBtnEmoji}>🎮</Text>
            </TouchableOpacity>
          )}
        </View>
      )}
    </SafeAreaView>
  )
}

const styles = StyleSheet.create({
  safe: { flex: 1, backgroundColor: '#fdfdfe' },
  empty: { padding: 24, color: COLORS.inkSoft, textAlign: 'right', writingDirection: 'rtl' },
  progressWrap: { flexDirection: 'row-reverse', gap: 5, paddingHorizontal: 18, paddingTop: 12 },
  progressSeg: { flex: 1, height: 4, borderRadius: 2, backgroundColor: '#eceef3' },
  scroll: { padding: 22, paddingBottom: 28, flexGrow: 1 },
  titleRow: { flexDirection: 'row-reverse', alignItems: 'center', gap: 10 },
  emojiChip: {
    width: 42, height: 42, borderRadius: 14,
    alignItems: 'center', justifyContent: 'center',
  },
  emojiChipText: { fontSize: 22 },
  lessonTitle: { flex: 1, fontSize: 17, fontWeight: '800', color: COLORS.ink, textAlign: 'right', writingDirection: 'rtl' },
  stepTitle: { fontSize: 24, fontWeight: '800', textAlign: 'right', writingDirection: 'rtl', marginTop: 14, marginBottom: 18 },
  videoCard: { borderRadius: RADIUS.md, overflow: 'hidden', backgroundColor: '#000' },
  video: { width: '100%', aspectRatio: 16 / 9 },
  videoOverlay: {
    ...StyleSheet.absoluteFillObject, backgroundColor: 'rgba(0,0,0,0.65)',
    alignItems: 'center', justifyContent: 'center', gap: 10, padding: 16,
  },
  videoOverlayText: { color: '#fff', fontSize: 15, fontWeight: '700', textAlign: 'center', writingDirection: 'rtl', lineHeight: 26 },
  videoRetryBtn: {
    backgroundColor: '#fff', borderRadius: 14, paddingVertical: 10, paddingHorizontal: 22, marginTop: 4,
  },
  videoRetryText: { fontSize: 15, fontWeight: '800', color: COLORS.ink, writingDirection: 'rtl' },
  videoBrowserText: { color: '#cbd5f5', fontSize: 14, fontWeight: '700', textDecorationLine: 'underline', writingDirection: 'rtl', marginTop: 2 },
  caption: { fontSize: 13, color: COLORS.inkSoft, textAlign: 'center', writingDirection: 'rtl', marginTop: 12 },

  talkRow: { flexDirection: 'row-reverse', alignItems: 'flex-start', gap: 10, marginBottom: 12 },
  talkAvatar: {
    width: 46, height: 46, borderRadius: 23, backgroundColor: '#fff',
    alignItems: 'center', justifyContent: 'center',
    shadowColor: '#101828', shadowOpacity: 0.08, shadowRadius: 8, shadowOffset: { width: 0, height: 3 }, elevation: 2,
  },
  talkAvatarEmoji: { fontSize: 26 },
  talkAvatarSpace: { width: 46 },
  talkBubble: {
    flex: 1, backgroundColor: '#fff', borderRadius: 18, borderWidth: 2,
    padding: 14, paddingHorizontal: 16,
  },
  talkBubbleFirst: { borderTopRightRadius: 4 },
  talkText: { fontSize: 16, fontWeight: '600', lineHeight: 30, color: COLORS.ink, textAlign: 'right', writingDirection: 'rtl' },

  pointCard: {
    flexDirection: 'row-reverse', alignItems: 'center', gap: 14,
    backgroundColor: '#fff', borderRadius: 18, borderWidth: 2,
    padding: 14, paddingHorizontal: 16, marginBottom: 12,
    shadowColor: '#101828', shadowOpacity: 0.05, shadowRadius: 8, shadowOffset: { width: 0, height: 3 }, elevation: 2,
  },
  pointBadge: {
    width: 46, height: 46, borderRadius: 16,
    alignItems: 'center', justifyContent: 'center',
  },
  pointBadgeEmoji: { fontSize: 18, lineHeight: 22 },
  pointBadgeNum: { fontSize: 12, fontWeight: '900', lineHeight: 14 },
  pointText: { flex: 1, fontSize: 15, fontWeight: '600', lineHeight: 27, color: COLORS.ink, textAlign: 'right', writingDirection: 'rtl' },

  ruleCard: {
    backgroundColor: '#fffbeb', borderRadius: 22, borderWidth: 2.5, borderColor: COLORS.gold,
    padding: 22, alignItems: 'center',
    shadowColor: '#b45309', shadowOpacity: 0.12, shadowRadius: 12, shadowOffset: { width: 0, height: 5 }, elevation: 3,
  },
  ruleEmoji: { fontSize: 44 },
  ruleText: {
    fontSize: 18, fontWeight: '800', lineHeight: 34, color: '#78350f',
    textAlign: 'center', writingDirection: 'rtl', marginTop: 10,
  },
  ruleStars: { marginTop: 12 },
  ruleStarsText: { fontSize: 16, letterSpacing: 2 },

  actionsWrap: { flex: 1, justifyContent: 'center', gap: 4 },
  actionsEmoji: { fontSize: 52, textAlign: 'center', marginBottom: 10 },
  footer: { flexDirection: 'row-reverse', alignItems: 'center', gap: 12, padding: 16, paddingTop: 8 },
  practiceBtn: {
    width: 50, height: 50, borderRadius: 25, borderWidth: 2, borderBottomWidth: 4,
    alignItems: 'center', justifyContent: 'center', backgroundColor: '#fff',
  },
  practiceBtnEmoji: { fontSize: 22 },
  backBtn: { paddingHorizontal: 6, paddingVertical: 12 },
  backText: { fontSize: 15, fontWeight: '700', color: COLORS.inkSoft, writingDirection: 'rtl' },
})
