import { useEffect, useLayoutEffect, useMemo, useState } from 'react'
import { Text, TouchableOpacity, StyleSheet } from 'react-native'
import { SafeAreaView } from 'react-native-safe-area-context'
import { getLessonById } from '../lib/lessons.js'
import { getActivityForLesson } from '../activities/index.js'
import { startMusic, stopMusic, isMusicEnabled, setMusicEnabled } from '../lib/sound.js'
import { COLORS } from '../theme.js'

export default function ActivityScreen({ route, navigation }) {
  const { lessonId } = route.params
  const lesson = getLessonById(lessonId)
  const activity = useMemo(() => getActivityForLesson(lessonId), [lessonId])
  const [musicOn, setMusicOn] = useState(isMusicEnabled())

  // Bouton 🎵/🔇 dans l'en-tête : l'enfant met pause quand il veut,
  // le choix est mémorisé pour les prochaines activités.
  useLayoutEffect(() => {
    navigation.setOptions({
      title: activity?.title || 'أجرّب بنفسي',
      headerRight: () => (
        <TouchableOpacity
          style={styles.musicBtn}
          hitSlop={{ top: 8, bottom: 8, left: 8, right: 8 }}
          onPress={() => {
            const on = !musicOn
            setMusicOn(on)
            setMusicEnabled(on)
            if (on) startMusic()
          }}
        >
          <Text style={styles.musicBtnEmoji}>{musicOn ? '🎵' : '🔇'}</Text>
        </TouchableOpacity>
      ),
    })
  }, [navigation, activity, musicOn])

  // Musique d'encouragement en fond, coupée en quittant l'activité.
  useEffect(() => {
    startMusic()
    return stopMusic
  }, [])

  if (!activity) {
    return <SafeAreaView style={styles.safe}><Text style={styles.empty}>لا توجد أنشطة لهذا الدرس بعد.</Text></SafeAreaView>
  }

  const Component = activity.component
  return (
    <SafeAreaView style={styles.safe} edges={['bottom']}>
      <Component
        color={lesson?.subjectColor || COLORS.royal}
        onExit={() => navigation.goBack()}
        {...(activity.props || {})}
      />
    </SafeAreaView>
  )
}

const styles = StyleSheet.create({
  safe: { flex: 1, backgroundColor: COLORS.cream },
  empty: { padding: 24, color: COLORS.inkSoft, textAlign: 'right', writingDirection: 'rtl' },
  musicBtn: { paddingHorizontal: 10, paddingVertical: 4, pointerEvents: 'auto' },
  musicBtnEmoji: { fontSize: 20 },
})
