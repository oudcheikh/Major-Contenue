import { useCallback, useState } from 'react'
import { View, Text, ScrollView, TouchableOpacity, StyleSheet } from 'react-native'
import { SafeAreaView } from 'react-native-safe-area-context'
import { useFocusEffect } from '@react-navigation/native'
import { getAllSubjects, getLessonById, getNextLesson } from '../lib/lessons.js'
import { getProgress } from '../firebase/progress.js'
import { getEleve, getDefis } from '../firebase/eleve.js'
import { COLORS, SHADOW, RADIUS, getLevel } from '../theme.js'
import { darken, MascotBubble, ChunkyButton } from '../activities/ui.js'

const SUBJECTS = getAllSubjects()

// Le compagnon أستاذ ماجور : un message contextuel selon la progression
// (aucun appel réseau — tout est scripté, coût zéro).
function companionAdvice(progress) {
  const entries = Object.values(progress).sort((a, b) => (b.updatedAt || '').localeCompare(a.updatedAt || ''))
  if (entries.length === 0) {
    return {
      text: 'أهلًا! أنا أستاذ ماجور، رفيقك في المراجعة 🤝\nأمسح رمز QR من دفترك أو اختر مادة، وسنراجع معًا خطوة خطوة!',
      cta: null,
    }
  }
  const last = entries[0]
  const lesson = getLessonById(last.lessonId)
  if (last.bestPct < 60 && lesson) {
    return {
      text: `في درس «${lesson.title}» حصلت على ${last.bestPct}%. لا بأس! أعد قراءة الملخص ثم أعد الاختبار — سترى الفرق 💪`,
      cta: { label: 'أراجع الدرس ←', lessonId: lesson.id },
    }
  }
  const nextL = lesson && getNextLesson(lesson.id)
  if (nextL) {
    return {
      text: `أتقنت درس «${lesson.title}» بنتيجة ${last.bestPct}% 👏\nجاهز للدرس التالي: «${nextL.title}»؟`,
      cta: { label: 'هيا نبدأ ←', lessonId: nextL.id },
    }
  }
  return {
    text: 'مستواك رائع! اختر مادة جديدة اليوم لنوسّع المعرفة 🌟',
    cta: null,
  }
}

export default function HomeScreen({ navigation }) {
  const [progress, setProgress] = useState({})
  const [eleve, setEleve] = useState(null)
  const [defis, setDefis] = useState([])

  useFocusEffect(
    useCallback(() => {
      let alive = true
      getProgress().then((p) => { if (alive) setProgress(p) })
      getEleve().then((e) => {
        if (!alive) return
        setEleve(e)
        if (e) getDefis(e).then((d) => { if (alive) setDefis(d) })
      })
      return () => { alive = false }
    }, [])
  )

  const done = Object.keys(progress).length
  const avg = done
    ? Math.round(Object.values(progress).reduce((s, e) => s + (e.bestPct || 0), 0) / done)
    : 0
  const level = getLevel(avg)
  const advice = companionAdvice(progress)

  return (
    <SafeAreaView style={styles.safe} edges={['top']}>
      <ScrollView contentContainerStyle={styles.scroll} showsVerticalScrollIndicator={false}>
        <View style={styles.header}>
          <View style={{ flex: 1, alignItems: 'flex-end' }}>
            <Text style={styles.hello}>{eleve ? `أهلًا يا ${eleve.prenom} 👋` : 'أهلًا بك 👋'}</Text>
            <Text style={styles.brand}>ماجور</Text>
          </View>
        </View>

        {!eleve && (
          <TouchableOpacity style={styles.linkCard} activeOpacity={0.85} onPress={() => navigation.navigate('Link')}>
            <Text style={styles.linkIcon}>🎟️</Text>
            <View style={{ flex: 1 }}>
              <Text style={styles.linkTitle}>عندي رمز من أستاذي</Text>
              <Text style={styles.linkSub}>أدخل رمزك MAJ-xxxx ليتابع أستاذك تقدّمك</Text>
            </View>
            <Text style={styles.linkArrow}>‹</Text>
          </TouchableOpacity>
        )}

        {defis.length > 0 && (
          <TouchableOpacity
            style={styles.defiCard}
            activeOpacity={0.85}
            onPress={() => defis[0].lessonId && navigation.navigate('Lesson', { lessonId: defis[0].lessonId })}
          >
            <Text style={styles.defiIcon}>🏆</Text>
            <View style={{ flex: 1 }}>
              <Text style={styles.defiTitle}>تحدي الأستاذ!</Text>
              <Text style={styles.defiText}>
                {defis[0].titre}{defis[0].objectifPct ? ` — الهدف: ${defis[0].objectifPct}%` : ''}
              </Text>
            </View>
            <Text style={styles.linkArrow}>‹</Text>
          </TouchableOpacity>
        )}

        <MascotBubble text={advice.text}>
          {!!advice.cta && (
            <ChunkyButton
              small
              label={advice.cta.label}
              color={COLORS.royal}
              onPress={() => navigation.navigate('Lesson', { lessonId: advice.cta.lessonId })}
            />
          )}
        </MascotBubble>

        <TouchableOpacity
          style={styles.scanCard}
          activeOpacity={0.85}
          onPress={() => navigation.navigate('Scanner')}
        >
          <View style={styles.scanIconWrap}>
            <Text style={styles.scanIcon}>📷</Text>
          </View>
          <View style={{ flex: 1 }}>
            <Text style={styles.scanTitle}>أمسح رمز الدفتر</Text>
            <Text style={styles.scanSub}>وجّه الكاميرا نحو رمز QR في الصفحة</Text>
          </View>
        </TouchableOpacity>

        {done > 0 && (
          <TouchableOpacity
            style={styles.progressCard}
            activeOpacity={0.85}
            onPress={() => navigation.navigate('Progress')}
          >
            <View style={[styles.levelBadge, { backgroundColor: level.bg }]}>
              <Text style={styles.levelIcon}>{level.icon}</Text>
            </View>
            <View style={{ flex: 1 }}>
              <Text style={styles.progressLabel}>تقدّمي</Text>
              <Text style={styles.progressValue}>{done} {done > 1 ? 'دروس' : 'درس'} · المعدل {avg}%</Text>
              <View style={styles.progressTrack}>
                <View style={[styles.progressFill, { width: `${avg}%`, backgroundColor: level.color }]} />
              </View>
            </View>
            <View style={[styles.levelPill, { backgroundColor: level.bg }]}>
              <Text style={[styles.levelPillText, { color: level.color }]}>{level.labelAr}</Text>
            </View>
          </TouchableOpacity>
        )}

        <Text style={styles.sectionTitle}>المواد</Text>
        <View style={styles.grid}>
          {SUBJECTS.map((s) => (
            <TouchableOpacity
              key={s.id}
              style={styles.subjectCard}
              activeOpacity={0.85}
              onPress={() => navigation.navigate('Subject', { subjectId: s.id })}
            >
              <View style={[styles.subjectIconWrap, { backgroundColor: s.color + '1a' }]}>
                <Text style={styles.subjectIcon}>{s.icon}</Text>
              </View>
              <Text style={styles.subjectLabel} numberOfLines={1}>{s.label}</Text>
              <View style={[styles.countPill, { backgroundColor: s.color + '14' }]}>
                <Text style={[styles.countPillText, { color: darken(s.color) }]}>{s.lessonCount} درسًا</Text>
              </View>
            </TouchableOpacity>
          ))}
        </View>
        <Text style={styles.versionText}>الإصدار 1.0.3 📓</Text>
      </ScrollView>
    </SafeAreaView>
  )
}

const styles = StyleSheet.create({
  safe: { flex: 1, backgroundColor: COLORS.cream },
  scroll: { padding: 20, paddingBottom: 44 },
  header: { flexDirection: 'row-reverse', alignItems: 'center', gap: 14, marginBottom: 20 },
  avatar: {
    width: 52, height: 52, borderRadius: 26, backgroundColor: COLORS.card,
    alignItems: 'center', justifyContent: 'center', ...SHADOW,
  },
  avatarEmoji: { fontSize: 26 },
  hello: { fontSize: 14, fontWeight: '600', color: COLORS.inkSoft, writingDirection: 'rtl' },
  brand: { fontSize: 30, fontWeight: '900', color: COLORS.ink, writingDirection: 'rtl', marginTop: 1 },
  linkCard: {
    flexDirection: 'row-reverse', alignItems: 'center', gap: 12,
    backgroundColor: COLORS.card, borderRadius: RADIUS.lg, borderWidth: 2, borderColor: '#ffd54f',
    padding: 14, marginBottom: 14, ...SHADOW,
  },
  linkIcon: { fontSize: 26 },
  linkTitle: { fontSize: 15, fontWeight: '800', color: COLORS.ink, textAlign: 'right', writingDirection: 'rtl' },
  linkSub: { fontSize: 12, fontWeight: '600', color: COLORS.inkSoft, marginTop: 2, textAlign: 'right', writingDirection: 'rtl' },
  linkArrow: { fontSize: 24, color: '#c6cbd6', fontWeight: '300' },
  defiCard: {
    flexDirection: 'row-reverse', alignItems: 'center', gap: 12,
    backgroundColor: '#fff8e1', borderRadius: RADIUS.lg, borderWidth: 2, borderColor: '#ffd54f',
    padding: 14, marginBottom: 14, ...SHADOW,
  },
  defiIcon: { fontSize: 28 },
  defiTitle: { fontSize: 13, fontWeight: '900', color: '#92400e', textAlign: 'right', writingDirection: 'rtl' },
  defiText: { fontSize: 15, fontWeight: '800', color: '#78350f', marginTop: 2, textAlign: 'right', writingDirection: 'rtl', lineHeight: 24 },
  scanCard: {
    flexDirection: 'row-reverse', alignItems: 'center', gap: 16,
    backgroundColor: COLORS.royal, borderRadius: RADIUS.xl, padding: 20, marginBottom: 14,
    borderBottomWidth: 5, borderBottomColor: darken(COLORS.royal), ...SHADOW,
  },
  scanIconWrap: {
    width: 58, height: 58, borderRadius: 20, backgroundColor: 'rgba(255,255,255,0.2)',
    alignItems: 'center', justifyContent: 'center',
  },
  scanIcon: { fontSize: 30 },
  scanTitle: { color: '#fff', fontSize: 19, fontWeight: '800', textAlign: 'right', writingDirection: 'rtl' },
  scanSub: { color: 'rgba(255,255,255,0.85)', fontSize: 13, fontWeight: '600', marginTop: 3, textAlign: 'right', writingDirection: 'rtl' },
  progressCard: {
    flexDirection: 'row-reverse', alignItems: 'center', gap: 14,
    backgroundColor: COLORS.card, borderRadius: RADIUS.lg, padding: 16, marginBottom: 8, ...SHADOW,
  },
  levelBadge: { width: 48, height: 48, borderRadius: 16, alignItems: 'center', justifyContent: 'center' },
  levelIcon: { fontSize: 24 },
  progressLabel: { fontSize: 12, fontWeight: '700', color: COLORS.inkSoft, textAlign: 'right', writingDirection: 'rtl' },
  progressValue: { fontSize: 15, fontWeight: '800', color: COLORS.ink, marginTop: 2, textAlign: 'right', writingDirection: 'rtl' },
  progressTrack: { height: 8, borderRadius: 4, backgroundColor: '#eef0f5', marginTop: 8, overflow: 'hidden' },
  progressFill: { height: 8, borderRadius: 4 },
  levelPill: { borderRadius: 10, paddingVertical: 6, paddingHorizontal: 10 },
  levelPillText: { fontSize: 12, fontWeight: '800', writingDirection: 'rtl' },
  sectionTitle: { fontSize: 20, fontWeight: '900', color: COLORS.ink, marginTop: 14, marginBottom: 12, textAlign: 'right', writingDirection: 'rtl' },
  grid: { flexDirection: 'row-reverse', flexWrap: 'wrap', justifyContent: 'space-between' },
  subjectCard: {
    width: '48%', backgroundColor: COLORS.card, borderRadius: RADIUS.lg, padding: 16, marginBottom: 14,
    alignItems: 'flex-end', ...SHADOW,
  },
  subjectIconWrap: { width: 54, height: 54, borderRadius: 18, alignItems: 'center', justifyContent: 'center' },
  subjectIcon: { fontSize: 28 },
  subjectLabel: { fontSize: 15, fontWeight: '800', color: COLORS.ink, marginTop: 10, textAlign: 'right', writingDirection: 'rtl' },
  countPill: { borderRadius: 8, paddingVertical: 4, paddingHorizontal: 8, marginTop: 8 },
  countPillText: { fontSize: 11, fontWeight: '800', writingDirection: 'rtl' },
  versionText: { fontSize: 11, fontWeight: '600', color: '#c0c6d4', textAlign: 'center', marginTop: 18 },
})
