import { useCallback, useState } from 'react'
import { View, Text, ScrollView, TouchableOpacity, StyleSheet } from 'react-native'
import { SafeAreaView } from 'react-native-safe-area-context'
import { useFocusEffect } from '@react-navigation/native'
import { getProgress } from '../firebase/progress.js'
import { getLessonById } from '../lib/lessons.js'
import { COLORS, SHADOW, RADIUS, getLevel } from '../theme.js'
import { isFirebaseConfigured } from '../firebase/config.js'

export default function ProgressScreen({ navigation }) {
  const [progress, setProgress] = useState({})
  const [loaded, setLoaded] = useState(false)

  useFocusEffect(
    useCallback(() => {
      let alive = true
      getProgress().then((p) => { if (alive) { setProgress(p); setLoaded(true) } })
      return () => { alive = false }
    }, [])
  )

  const entries = Object.values(progress).sort((a, b) => (b.updatedAt || '').localeCompare(a.updatedAt || ''))
  const done = entries.length
  const avg = done ? Math.round(entries.reduce((s, e) => s + (e.bestPct || 0), 0) / done) : 0
  const level = getLevel(avg)

  return (
    <SafeAreaView style={styles.safe} edges={['bottom']}>
      <ScrollView contentContainerStyle={styles.scroll} showsVerticalScrollIndicator={false}>
        <View style={styles.hero}>
          <View style={[styles.heroBadge, { backgroundColor: level.bg }]}>
            <Text style={styles.heroIcon}>{level.icon}</Text>
          </View>
          <Text style={styles.heroPct}>{avg}%</Text>
          <View style={[styles.levelPill, { backgroundColor: level.bg }]}>
            <Text style={[styles.levelPillText, { color: level.color }]}>{level.labelAr}</Text>
          </View>
          <Text style={styles.heroSub}>{done} {done > 1 ? 'دروس مكتملة' : 'درس مكتمل'}</Text>
          <View style={styles.heroTrack}>
            <View style={[styles.heroFill, { width: `${avg}%`, backgroundColor: level.color }]} />
          </View>
        </View>

        {!isFirebaseConfigured && (
          <Text style={styles.note}>💾 تقدّمك محفوظ على هذا الجهاز.</Text>
        )}

        {loaded && done === 0 && (
          <Text style={styles.empty}>لم تكمل أي درس بعد. أمسح رمز QR من الدفتر لتبدأ! 🚀</Text>
        )}

        {entries.map((e) => {
          const lesson = getLessonById(e.lessonId)
          const lv = getLevel(e.bestPct || 0)
          return (
            <TouchableOpacity
              key={e.lessonId}
              style={styles.row}
              activeOpacity={0.85}
              onPress={() => lesson && navigation.navigate('Lesson', { lessonId: e.lessonId })}
            >
              <View style={[styles.rowIcon, { backgroundColor: (lesson?.subjectColor || COLORS.royal) + '16' }]}>
                <Text style={styles.rowEmoji}>{lesson?.emoji || '📘'}</Text>
              </View>
              <View style={{ flex: 1 }}>
                <Text style={[styles.rowTitle, styles.rtl]} numberOfLines={1}>
                  {lesson?.title || e.lessonId}
                </Text>
                <Text style={[styles.rowMeta, styles.rtl]}>
                  {e.attempts} {e.attempts > 1 ? 'محاولات' : 'محاولة'} · أفضل نتيجة {e.bestScore}/{e.total}
                </Text>
              </View>
              <View style={[styles.pct, { backgroundColor: lv.color }]}>
                <Text style={styles.pctText}>{e.bestPct}%</Text>
              </View>
            </TouchableOpacity>
          )
        })}
      </ScrollView>
    </SafeAreaView>
  )
}

const styles = StyleSheet.create({
  safe: { flex: 1, backgroundColor: COLORS.cream },
  scroll: { padding: 18, paddingBottom: 40 },
  hero: { backgroundColor: COLORS.card, borderRadius: RADIUS.xl, padding: 24, alignItems: 'center', marginBottom: 14, ...SHADOW },
  heroBadge: { width: 64, height: 64, borderRadius: 22, alignItems: 'center', justifyContent: 'center' },
  heroIcon: { fontSize: 32 },
  heroPct: { fontSize: 46, fontWeight: '900', color: COLORS.ink, marginTop: 8 },
  levelPill: { borderRadius: 10, paddingVertical: 5, paddingHorizontal: 12, marginTop: 4 },
  levelPillText: { fontSize: 13, fontWeight: '800', writingDirection: 'rtl' },
  heroSub: { fontSize: 14, fontWeight: '600', color: COLORS.inkSoft, marginTop: 8, writingDirection: 'rtl' },
  heroTrack: { alignSelf: 'stretch', height: 10, borderRadius: 5, backgroundColor: '#eef0f5', marginTop: 14, overflow: 'hidden' },
  heroFill: { height: 10, borderRadius: 5 },
  note: {
    fontSize: 13, fontWeight: '600', color: '#92400e', backgroundColor: '#fffaeb',
    borderRadius: RADIUS.md, borderWidth: 1.5, borderColor: '#fde68a', padding: 12, marginBottom: 14,
    lineHeight: 21, textAlign: 'right', writingDirection: 'rtl',
  },
  empty: { fontSize: 15, fontWeight: '600', color: COLORS.inkSoft, textAlign: 'center', marginTop: 20, lineHeight: 25, writingDirection: 'rtl' },
  row: {
    flexDirection: 'row-reverse', alignItems: 'center', gap: 12,
    backgroundColor: COLORS.card, borderRadius: RADIUS.md, padding: 13, marginBottom: 10, ...SHADOW,
  },
  rowIcon: { width: 44, height: 44, borderRadius: 14, alignItems: 'center', justifyContent: 'center' },
  rowEmoji: { fontSize: 22 },
  rowTitle: { fontSize: 15, fontWeight: '800', color: COLORS.ink },
  rtl: { textAlign: 'right', writingDirection: 'rtl' },
  rowMeta: { fontSize: 12, fontWeight: '600', color: COLORS.inkSoft, marginTop: 3 },
  pct: { minWidth: 46, borderRadius: 12, paddingVertical: 6, paddingHorizontal: 8, alignItems: 'center' },
  pctText: { color: '#fff', fontWeight: '800', fontSize: 13 },
})
