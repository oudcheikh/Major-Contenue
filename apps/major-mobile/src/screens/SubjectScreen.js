import { useCallback, useLayoutEffect, useState } from 'react'
import { View, Text, ScrollView, TouchableOpacity, StyleSheet, Alert } from 'react-native'
import { SafeAreaView } from 'react-native-safe-area-context'
import { useFocusEffect } from '@react-navigation/native'
import { getSubject, isLessonOpen } from '../lib/lessons.js'
import { getActivityForLesson } from '../activities/index.js'
import { getProgress } from '../firebase/progress.js'
import { tap } from '../activities/ui.js'
import { COLORS, SHADOW, RADIUS } from '../theme.js'

export default function SubjectScreen({ route, navigation }) {
  const { subjectId } = route.params
  const subject = getSubject(subjectId)
  const [progress, setProgress] = useState({})

  useLayoutEffect(() => {
    navigation.setOptions({ title: subject?.labelAr || subject?.label || 'المادة' })
  }, [navigation, subject])

  useFocusEffect(
    useCallback(() => {
      let alive = true
      getProgress().then((p) => { if (alive) setProgress(p) })
      return () => { alive = false }
    }, [])
  )

  if (!subject) {
    return (
      <SafeAreaView style={styles.safe}><Text style={styles.empty}>لم أجد هذه المادة.</Text></SafeAreaView>
    )
  }

  const color = subject.color || COLORS.royal
  const lessons = subject.lessons || []
  const doneCount = lessons.filter((l) => progress[l.id]).length

  return (
    <SafeAreaView style={styles.safe} edges={['bottom']}>
      <ScrollView contentContainerStyle={styles.scroll} showsVerticalScrollIndicator={false}>
        <View style={styles.summary}>
          <Text style={styles.summaryText}>أكملت {doneCount} من {lessons.length} درسًا</Text>
          <View style={styles.summaryTrack}>
            <View style={[styles.summaryFill, { width: `${lessons.length ? Math.round((doneCount / lessons.length) * 100) : 0}%`, backgroundColor: color }]} />
          </View>
        </View>

        {lessons.map((lesson, i) => {
          const p = progress[lesson.id]
          const open = isLessonOpen(lesson.id)
          if (!open) {
            return (
              <TouchableOpacity
                key={lesson.id}
                style={[styles.card, styles.cardLocked]}
                activeOpacity={0.7}
                onPress={() => {
                  tap()
                  Alert.alert('قريبًا 🔒', 'هذا الدرس سيُفتح قريبًا مع التحديث القادم.\nيمكنك دائمًا فتحه بمسح رمز QR من كرّاسك.')
                }}
              >
                <View style={[styles.num, { backgroundColor: '#e8eaf0' }]}>
                  <Text style={styles.numEmoji}>🔒</Text>
                </View>
                <View style={{ flex: 1 }}>
                  <Text style={[styles.cardTitle, styles.rtl, styles.titleLocked]} numberOfLines={2}>{lesson.title}</Text>
                  <Text style={[styles.cardMeta, styles.rtl]}>قريبًا · الدرس {i + 1}</Text>
                </View>
              </TouchableOpacity>
            )
          }
          return (
            <TouchableOpacity
              key={lesson.id}
              style={styles.card}
              activeOpacity={0.85}
              onPress={() => navigation.navigate('Lesson', { lessonId: lesson.id })}
            >
              <View style={[styles.num, { backgroundColor: color + '16' }]}>
                <Text style={styles.numEmoji}>{lesson.emoji || '📘'}</Text>
              </View>
              <View style={{ flex: 1 }}>
                <Text style={[styles.cardTitle, styles.rtl]} numberOfLines={2}>{lesson.title}</Text>
                <Text style={[styles.cardMeta, styles.rtl]}>
                  🕐 {(lesson.duration || '5 min').replace('min', 'دقائق')} · الدرس {i + 1}
                </Text>
              </View>
              {!!getActivityForLesson(lesson.id) && (
                <TouchableOpacity
                  style={[styles.playBtn, { borderColor: color }]}
                  activeOpacity={0.7}
                  onPress={() => { tap(); navigation.navigate('Activity', { lessonId: lesson.id }) }}
                >
                  <Text style={styles.playBtnEmoji}>🎮</Text>
                </TouchableOpacity>
              )}
              {p ? (
                <View style={[styles.badge, { backgroundColor: color }]}>
                  <Text style={styles.badgeText}>{p.bestPct}%</Text>
                </View>
              ) : (
                <Text style={styles.chevron}>‹</Text>
              )}
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
  empty: { padding: 24, color: COLORS.inkSoft, textAlign: 'right', writingDirection: 'rtl' },
  summary: { backgroundColor: COLORS.card, borderRadius: RADIUS.md, padding: 14, marginBottom: 14, ...SHADOW },
  summaryText: { fontSize: 13, fontWeight: '800', color: COLORS.inkSoft, textAlign: 'right', writingDirection: 'rtl' },
  summaryTrack: { height: 8, borderRadius: 4, backgroundColor: '#eef0f5', marginTop: 8, overflow: 'hidden' },
  summaryFill: { height: 8, borderRadius: 4 },
  card: {
    flexDirection: 'row-reverse', alignItems: 'center', gap: 14,
    backgroundColor: COLORS.card, borderRadius: RADIUS.md, padding: 14, marginBottom: 10, ...SHADOW,
  },
  cardLocked: { opacity: 0.55 },
  titleLocked: { color: COLORS.inkSoft },
  num: { width: 48, height: 48, borderRadius: 16, alignItems: 'center', justifyContent: 'center' },
  numEmoji: { fontSize: 24 },
  cardTitle: { fontSize: 16, fontWeight: '800', color: COLORS.ink },
  rtl: { textAlign: 'right', writingDirection: 'rtl' },
  cardMeta: { fontSize: 12, fontWeight: '600', color: COLORS.inkSoft, marginTop: 3 },
  playBtn: {
    width: 42, height: 42, borderRadius: 21, borderWidth: 2, borderBottomWidth: 4,
    alignItems: 'center', justifyContent: 'center', backgroundColor: '#fff',
  },
  playBtnEmoji: { fontSize: 20 },
  badge: { minWidth: 46, borderRadius: 12, paddingVertical: 7, paddingHorizontal: 9, alignItems: 'center' },
  badgeText: { color: '#fff', fontWeight: '800', fontSize: 13 },
  chevron: { fontSize: 26, color: '#c6cbd6', fontWeight: '300' },
})
