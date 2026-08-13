import React, { useState, useCallback, useRef } from 'react';
import {
  View, Text, ScrollView, TouchableOpacity, StyleSheet,
  RefreshControl, Animated, I18nManager,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { useFocusEffect } from '@react-navigation/native';
import { getStudent, getStats, updateStreak } from '../utils/storage';
import { computeGlobalLevel, computeSubjectLevel } from '../utils/levelDetection';
import { getDailyChallenge, getActiveStudentsCount, getMascotMessage } from '../utils/dailyChallenge';
import { computeKnowledgeLevel, getKnowledgeProfile } from '../utils/phygitalStorage';
import Mascot from '../components/Mascot';
import { COLORS, GRADIENTS } from '../theme';
import { SUBJECTS } from '../data/exercises';

export default function HomeScreen({ navigation }) {
  const [student, setStudent]         = useState(null);
  const [stats, setStats]             = useState(null);
  const [streak, setStreak]           = useState({ count: 0 });
  const [globalLevel, setGlobalLevel] = useState(null);
  const [challenge, setChallenge]     = useState(null);
  const [knowledge, setKnowledge]     = useState(null);
  const [refreshing, setRefreshing]   = useState(false);
  const [activeStudents]              = useState(getActiveStudentsCount);

  // Animations
  const heroOpacity       = useRef(new Animated.Value(0)).current;
  const heroY             = useRef(new Animated.Value(-30)).current;
  const challengeOpacity  = useRef(new Animated.Value(0)).current;
  const challengeScale    = useRef(new Animated.Value(0.9)).current;
  const subjectsOpacity   = useRef(new Animated.Value(0)).current;
  const subjectsY         = useRef(new Animated.Value(20)).current;
  const streakPulse       = useRef(new Animated.Value(1)).current;
  const progressWidth     = useRef(new Animated.Value(0)).current;

  const load = useCallback(async () => {
    const [s, st, str, ch, kp] = await Promise.all([
      getStudent(), getStats(), updateStreak(), getDailyChallenge(), getKnowledgeProfile(),
    ]);
    setStudent(s);
    setStats(st);
    setStreak(str);
    setGlobalLevel(computeGlobalLevel(st));
    setChallenge(ch);
    setKnowledge(computeKnowledgeLevel(kp));

    const pct = computeGlobalLevel(st)?.pct || 0;

    Animated.stagger(100, [
      Animated.parallel([
        Animated.timing(heroOpacity,  { toValue: 1, duration: 500, useNativeDriver: true }),
        Animated.spring(heroY, { toValue: 0, tension: 70, friction: 10, useNativeDriver: true }),
      ]),
      Animated.parallel([
        Animated.timing(challengeOpacity, { toValue: 1, duration: 400, useNativeDriver: true }),
        Animated.spring(challengeScale, { toValue: 1, tension: 65, friction: 9, useNativeDriver: true }),
      ]),
      Animated.parallel([
        Animated.timing(subjectsOpacity, { toValue: 1, duration: 400, useNativeDriver: true }),
        Animated.spring(subjectsY, { toValue: 0, tension: 70, friction: 10, useNativeDriver: true }),
      ]),
    ]).start();

    // Barre de progression animée
    Animated.timing(progressWidth, { toValue: pct, duration: 900, delay: 600, useNativeDriver: false }).start();

    // Pulse sur le streak
    Animated.loop(
      Animated.sequence([
        Animated.timing(streakPulse, { toValue: 1.08, duration: 800, useNativeDriver: true }),
        Animated.timing(streakPulse, { toValue: 1,    duration: 800, useNativeDriver: true }),
      ])
    ).start();
  }, []);

  useFocusEffect(useCallback(() => {
    heroOpacity.setValue(0);
    heroY.setValue(-30);
    challengeOpacity.setValue(0);
    challengeScale.setValue(0.9);
    subjectsOpacity.setValue(0);
    subjectsY.setValue(20);
    progressWidth.setValue(0);
    load();
  }, [load]));

  const onRefresh = async () => { setRefreshing(true); await load(); setRefreshing(false); };

  if (!student || !stats || !challenge || !knowledge) {
    return (
      <View style={styles.loading}>
        <Text style={styles.loadingCamel}>🐪</Text>
        <Text style={styles.loadingText}>Chargement...</Text>
        <View style={styles.loadingDots}>
          {[0, 1, 2].map((i) => <LoadingDot key={i} delay={i * 200} />)}
        </View>
      </View>
    );
  }

  const mascotMsg   = getMascotMessage(student.name, streak.count, challenge.completed);
  const challengePct = challenge.completed ? 100 : (challenge.answeredCount / challenge.questions.length) * 100;
  const subjectMix  = [...new Set(challenge.questions.map((q) => q.subjectIcon))];

  function launchChallenge() {
    navigation.navigate('Quiz', {
      subject: {
        id: 'challenge',
        label: 'Défi du jour',
        labelAr: 'تحدي اليوم',
        icon: '🎯',
        color: '#2563eb',
        colorDark: '#182b66',
        exercises: challenge.questions,
        isChallenge: true,
      },
    });
  }

  const progressWidthStr = progressWidth.interpolate({
    inputRange: [0, 100],
    outputRange: ['0%', '100%'],
  });

  return (
    <ScrollView
      style={styles.scroll}
      contentContainerStyle={styles.container}
      refreshControl={<RefreshControl refreshing={refreshing} onRefresh={onRefresh} tintColor="#2563eb" />}
      showsVerticalScrollIndicator={false}
    >

      {/* ── HERO ── */}
      <Animated.View style={{ opacity: heroOpacity, transform: [{ translateY: heroY }] }}>
        <LinearGradient
          colors={['#182b66', '#2563eb', '#38bdf8']}
          style={styles.hero}
          start={{ x: 0, y: 0 }}
          end={{ x: 1, y: 1 }}
        >
          <View style={styles.heroCircle1} />
          <View style={styles.heroCircle2} />
          <View style={styles.heroCircle3} />

          {/* Top : nom + streak */}
          <View style={styles.heroTop}>
            <View style={{ flex: 1 }}>
              <Text style={styles.heroGreet}>مرحباً · Bonjour 👋</Text>
              <Text style={styles.heroName}>{student.name}</Text>
              <View style={styles.socialRow}>
                <View style={styles.socialDot} />
                <Text style={styles.socialText}>{activeStudents} élèves actifs aujourd'hui</Text>
              </View>
            </View>

            <Animated.View style={[styles.streakWrap, { transform: [{ scale: streakPulse }] }]}>
              <Text style={styles.streakFire}>🔥</Text>
              <Text style={styles.streakNum}>{streak.count}</Text>
              <Text style={styles.streakLabel}>jours</Text>
            </Animated.View>
          </View>

          {/* Mascotte */}
          <View style={styles.mascotRow}>
            <Mascot message={mascotMsg} compact />
          </View>

          {/* Barre de progression globale */}
          {globalLevel && (
            <View style={styles.progressSection}>
              <View style={styles.progressHeader}>
                <Text style={styles.progressLabel}>{globalLevel.level.icon} Niveau global</Text>
                <Text style={styles.progressPct}>{globalLevel.pct}%</Text>
              </View>
              <View style={styles.progressTrack}>
                <Animated.View style={[styles.progressFill, { width: progressWidthStr }]} />
              </View>
            </View>
          )}

          <View style={styles.progressSection}>
            <View style={styles.progressHeader}>
              <Text style={styles.progressLabel}>🧠 Niveau de Savoir</Text>
              <Text style={styles.progressPct}>{knowledge.level.icon} {knowledge.level.label} · {knowledge.pct}%</Text>
            </View>
            <View style={styles.progressTrack}>
              <View style={[styles.progressFill, { width: `${knowledge.pct}%` }]} />
            </View>
          </View>
        </LinearGradient>
      </Animated.View>

      {/* ── DÉFI DU JOUR ── */}
      <Animated.View style={[styles.section, { opacity: challengeOpacity, transform: [{ scale: challengeScale }] }]}>
        {challenge.completed ? (
          <LinearGradient colors={['#059669', '#10b981']} style={styles.challengeCard} start={{ x: 0, y: 0 }} end={{ x: 1, y: 1 }}>
            <View style={styles.doneCircle} />
            <Text style={styles.challengeTag}>DÉFI DU JOUR</Text>
            <Text style={styles.doneTrophy}>⭐</Text>
            <Text style={styles.doneTitle}>Défi complété !</Text>
            <Text style={styles.doneSub}>{challenge.score}/{challenge.questions.length} bonnes réponses · Reviens demain !</Text>
          </LinearGradient>
        ) : (
          <TouchableOpacity onPress={launchChallenge} activeOpacity={0.9}>
            <LinearGradient colors={['#1e1b4b', '#4338ca', '#6366f1']} style={styles.challengeCard} start={{ x: 0, y: 0 }} end={{ x: 1, y: 1 }}>
              <View style={styles.challengeCircle1} />
              <View style={styles.challengeCircle2} />

              <View style={styles.challengeTop}>
                <View>
                  <Text style={styles.challengeTag}>DÉFI DU JOUR · تحدي اليوم</Text>
                  <Text style={styles.challengeTitle}>{challenge.questions.length} questions · ~3 min</Text>
                </View>
                <Text style={styles.challengeEmoji}>🎯</Text>
              </View>

              {/* Mix matières */}
              <View style={styles.challengeMixRow}>
                {subjectMix.map((icon, i) => (
                  <View key={i} style={styles.subjectChip}>
                    <Text style={styles.subjectChipText}>{icon}</Text>
                  </View>
                ))}
                <Text style={styles.mixLabel}>Mix de matières</Text>
              </View>

              {/* Barre si déjà commencé */}
              {challenge.answeredCount > 0 && (
                <View style={styles.challengeProgress}>
                  <View style={styles.challengeTrack}>
                    <View style={[styles.challengeFill, { width: `${challengePct}%` }]} />
                  </View>
                  <Text style={styles.challengeCount}>{challenge.answeredCount}/{challenge.questions.length}</Text>
                </View>
              )}

              <View style={styles.challengeBtn}>
                <Text style={styles.challengeBtnText}>
                  {challenge.answeredCount > 0 ? '▶ Continuer le défi' : '▶ Commencer le défi'}
                </Text>
              </View>
            </LinearGradient>
          </TouchableOpacity>
        )}
      </Animated.View>

      {/* ── MATIÈRES FRANÇAISES ── */}
      <Animated.View style={[styles.section, { opacity: subjectsOpacity, transform: [{ translateY: subjectsY }] }]}>
        <View style={styles.sectionHeader}>
          <Text style={styles.sectionTitle}>Révise par matière</Text>
          <Text style={styles.sectionAr}>راجع حسب المادة</Text>
        </View>
        <View style={styles.subjectsRow}>
          {SUBJECTS.filter((s) => !s.isArabic).map((subject) => {
            const subLevel = computeSubjectLevel(stats[subject.id]);
            return (
              <SubjectCard
                key={subject.id}
                subject={subject}
                pct={subLevel.pct}
                onPress={() => navigation.navigate('Quiz', { subject })}
              />
            );
          })}
        </View>
      </Animated.View>

      {/* ── MATIÈRES ARABES ── */}
      <Animated.View style={[styles.section, { opacity: subjectsOpacity, transform: [{ translateY: subjectsY }] }]}>
        {/* Header section arabe (RTL) */}
        <View style={styles.arabicSectionHeader}>
          <View style={styles.arabicSectionBadge}>
            <Text style={styles.arabicSectionBadgeText}>☪️ مواد عربية</Text>
          </View>
          <Text style={styles.arabicSectionSub}>المواد باللغة العربية</Text>
        </View>

        <View style={styles.arabicSubjectsGrid}>
          {SUBJECTS.filter((s) => s.isArabic).map((subject) => {
            const subLevel = computeSubjectLevel(stats[subject.id]);
            return (
              <ArabicSubjectCard
                key={subject.id}
                subject={subject}
                pct={subLevel.pct}
                onPress={() => navigation.navigate('Quiz', { subject })}
              />
            );
          })}
        </View>
      </Animated.View>

      <View style={{ height: 32 }} />
    </ScrollView>
  );
}

// Dot animé pour le loading
function LoadingDot({ delay }) {
  const y = useRef(new Animated.Value(0)).current;
  React.useEffect(() => {
    Animated.loop(
      Animated.sequence([
        Animated.timing(y, { toValue: -6, duration: 400, delay, useNativeDriver: true }),
        Animated.timing(y, { toValue: 0,  duration: 400, useNativeDriver: true }),
      ])
    ).start();
  }, []);
  return <Animated.View style={[styles.dot, { transform: [{ translateY: y }] }]} />;
}

function ArabicSubjectCard({ subject, pct, onPress }) {
  const scale = useRef(new Animated.Value(1)).current;

  function handlePress() {
    Animated.sequence([
      Animated.timing(scale, { toValue: 0.93, duration: 80, useNativeDriver: true }),
      Animated.spring(scale, { toValue: 1, tension: 200, friction: 10, useNativeDriver: true }),
    ]).start();
    onPress();
  }

  return (
    <Animated.View style={[styles.arabicCardWrap, { transform: [{ scale }] }]}>
      <TouchableOpacity style={[styles.arabicCard, { borderColor: subject.color + '33' }]} onPress={handlePress} activeOpacity={1}>
        <LinearGradient
          colors={[subject.color + '18', subject.color + '08']}
          style={styles.arabicCardGradient}
          start={{ x: 0, y: 0 }} end={{ x: 1, y: 1 }}
        />
        {/* Header RTL */}
        <View style={styles.arabicCardHeader}>
          <View style={[styles.arabicIconWrap, { backgroundColor: subject.color + '22' }]}>
            <Text style={styles.arabicIcon}>{subject.icon}</Text>
          </View>
          <View style={[styles.arabicPctBadge, { backgroundColor: subject.color }]}>
            <Text style={styles.arabicPctText}>{pct}%</Text>
          </View>
        </View>
        {/* Nom arabe (RTL) */}
        <Text style={[styles.arabicCardName, { color: subject.color }]}>{subject.labelAr}</Text>
        <Text style={styles.arabicCardNameFr}>{subject.label}</Text>
        {/* Progress bar */}
        <View style={styles.arabicBarTrack}>
          <View style={[styles.arabicBarFill, { width: `${pct}%`, backgroundColor: subject.color }]} />
        </View>
      </TouchableOpacity>
    </Animated.View>
  );
}

function SubjectCard({ subject, pct, onPress }) {
  const scale   = useRef(new Animated.Value(1)).current;
  const pressed = useRef(new Animated.Value(1)).current;

  function handlePress() {
    Animated.sequence([
      Animated.timing(scale, { toValue: 0.93, duration: 80, useNativeDriver: true }),
      Animated.spring(scale, { toValue: 1, tension: 200, friction: 10, useNativeDriver: true }),
    ]).start();
    onPress();
  }

  return (
    <Animated.View style={[styles.subjectCardWrap, { transform: [{ scale }] }]}>
      <TouchableOpacity style={styles.subjectCard} onPress={handlePress} activeOpacity={1}>
        {/* Gradient accent en haut */}
        <LinearGradient
          colors={[subject.color, subject.color + '99']}
          style={styles.subjectAccent}
          start={{ x: 0, y: 0 }} end={{ x: 1, y: 0 }}
        />
        <View style={[styles.subjectIconWrap, { backgroundColor: subject.color + '18' }]}>
          <Text style={styles.subjectIcon}>{subject.icon}</Text>
        </View>
        <Text style={styles.subjectName}>{subject.label}</Text>
        <Text style={[styles.subjectPct, { color: subject.color }]}>{pct}%</Text>
        <View style={styles.subjectBarTrack}>
          <View style={[styles.subjectBarFill, { width: `${pct}%`, backgroundColor: subject.color }]} />
        </View>
      </TouchableOpacity>
    </Animated.View>
  );
}

const styles = StyleSheet.create({
  scroll: { flex: 1, backgroundColor: COLORS.background },
  container: { gap: 16, paddingBottom: 16 },

  // Loading
  loading: { flex: 1, alignItems: 'center', justifyContent: 'center', gap: 16, backgroundColor: COLORS.background },
  loadingCamel: { fontSize: 56 },
  loadingText: { fontSize: 16, color: COLORS.muted, fontWeight: '700' },
  loadingDots: { flexDirection: 'row', gap: 8 },
  dot: { width: 8, height: 8, borderRadius: 4, backgroundColor: COLORS.primary },

  // Hero
  hero: { paddingTop: 56, paddingBottom: 24, paddingHorizontal: 20, gap: 16, overflow: 'hidden' },
  heroCircle1: { position: 'absolute', width: 280, height: 280, borderRadius: 140, backgroundColor: 'rgba(255,255,255,0.07)', top: -90, right: -70 },
  heroCircle2: { position: 'absolute', width: 160, height: 160, borderRadius: 80,  backgroundColor: 'rgba(56,189,248,0.12)', bottom: -50, left: -30 },
  heroCircle3: { position: 'absolute', width: 80,  height: 80,  borderRadius: 40,  backgroundColor: 'rgba(255,255,255,0.05)', top: 40, left: 20 },

  heroTop: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'flex-start' },
  heroGreet: { fontSize: 12, color: 'rgba(255,255,255,0.7)', fontWeight: '700', marginBottom: 2 },
  heroName: { fontSize: 26, fontWeight: '900', color: '#fff' },
  socialRow: { flexDirection: 'row', alignItems: 'center', gap: 6, marginTop: 4 },
  socialDot: { width: 7, height: 7, borderRadius: 4, backgroundColor: '#34d399' },
  socialText: { fontSize: 12, color: 'rgba(255,255,255,0.7)', fontWeight: '600' },

  streakWrap: {
    backgroundColor: 'rgba(255,255,255,0.15)',
    borderRadius: 20, padding: 12,
    alignItems: 'center', minWidth: 62,
    borderWidth: 1, borderColor: 'rgba(255,255,255,0.22)',
  },
  streakFire: { fontSize: 22 },
  streakNum:  { fontSize: 24, fontWeight: '900', color: '#fde68a' },
  streakLabel:{ fontSize: 10, color: 'rgba(255,255,255,0.65)', fontWeight: '700' },

  mascotRow: { marginTop: -4 },

  progressSection: { gap: 8 },
  progressHeader: { flexDirection: 'row', justifyContent: 'space-between' },
  progressLabel: { fontSize: 12, color: 'rgba(255,255,255,0.85)', fontWeight: '700' },
  progressPct:   { fontSize: 12, color: '#fde68a', fontWeight: '900' },
  progressTrack: { height: 7, borderRadius: 999, backgroundColor: 'rgba(255,255,255,0.18)', overflow: 'hidden' },
  progressFill:  { height: '100%', borderRadius: 999, backgroundColor: '#fde68a' },

  // Section
  section: { paddingHorizontal: 16 },
  sectionHeader: { flexDirection: 'row', alignItems: 'center', justifyContent: 'space-between', marginBottom: 12 },
  sectionTitle: { fontSize: 17, fontWeight: '900', color: COLORS.ink },
  sectionAr:    { fontSize: 13, color: COLORS.muted, fontWeight: '700' },

  // Challenge
  challengeCard: { borderRadius: 26, padding: 22, gap: 16, overflow: 'hidden' },
  doneCircle: { position: 'absolute', width: 200, height: 200, borderRadius: 100, backgroundColor: 'rgba(255,255,255,0.08)', top: -60, right: -40 },
  doneTrophy: { fontSize: 44, textAlign: 'center' },
  doneTitle:  { fontSize: 22, fontWeight: '900', color: '#fff', textAlign: 'center' },
  doneSub:    { fontSize: 14, color: 'rgba(255,255,255,0.85)', fontWeight: '600', textAlign: 'center' },

  challengeCircle1: { position: 'absolute', width: 200, height: 200, borderRadius: 100, backgroundColor: 'rgba(255,255,255,0.07)', top: -60, right: -40 },
  challengeCircle2: { position: 'absolute', width: 110, height: 110, borderRadius: 55,  backgroundColor: 'rgba(99,102,241,0.3)',   bottom: -30, left: -20 },

  challengeTag:   { fontSize: 10, fontWeight: '900', color: 'rgba(255,255,255,0.6)', letterSpacing: 1.5 },
  challengeTop:   { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'flex-start' },
  challengeTitle: { fontSize: 22, fontWeight: '900', color: '#fff', marginTop: 3 },
  challengeEmoji: { fontSize: 44 },

  challengeMixRow: { flexDirection: 'row', alignItems: 'center', gap: 10 },
  subjectChip:     { width: 38, height: 38, borderRadius: 12, backgroundColor: 'rgba(255,255,255,0.18)', alignItems: 'center', justifyContent: 'center' },
  subjectChipText: { fontSize: 18 },
  mixLabel:        { fontSize: 12, color: 'rgba(255,255,255,0.7)', fontWeight: '700' },

  challengeProgress: { flexDirection: 'row', alignItems: 'center', gap: 10 },
  challengeTrack:    { flex: 1, height: 7, borderRadius: 999, backgroundColor: 'rgba(255,255,255,0.2)', overflow: 'hidden' },
  challengeFill:     { height: '100%', borderRadius: 999, backgroundColor: '#fde68a' },
  challengeCount:    { fontSize: 13, color: '#fde68a', fontWeight: '900', minWidth: 32 },

  challengeBtn:     { backgroundColor: 'rgba(255,255,255,0.18)', borderRadius: 18, padding: 16, alignItems: 'center', borderWidth: 1, borderColor: 'rgba(255,255,255,0.28)' },
  challengeBtnText: { color: '#fff', fontWeight: '900', fontSize: 16, letterSpacing: 0.5 },

  // Arabic section
  arabicSectionHeader: { flexDirection: 'row', alignItems: 'center', justifyContent: 'space-between', marginBottom: 12 },
  arabicSectionBadge: { backgroundColor: '#d1fae5', borderRadius: 999, paddingHorizontal: 14, paddingVertical: 6, borderWidth: 1.5, borderColor: '#6ee7b7' },
  arabicSectionBadgeText: { color: '#065f46', fontWeight: '900', fontSize: 13 },
  arabicSectionSub: { color: '#6b7280', fontWeight: '700', fontSize: 12, textAlign: 'right' },
  arabicSubjectsGrid: { flexDirection: 'row', flexWrap: 'wrap', gap: 10 },
  arabicCardWrap: { width: '47%' },
  arabicCard: {
    backgroundColor: '#fff', borderRadius: 20, padding: 14, gap: 8,
    borderWidth: 1.5, overflow: 'hidden',
    shadowColor: '#182b66', shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.08, shadowRadius: 12, elevation: 4,
  },
  arabicCardGradient: { ...StyleSheet.absoluteFillObject },
  arabicCardHeader: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center' },
  arabicIconWrap: { width: 40, height: 40, borderRadius: 12, alignItems: 'center', justifyContent: 'center' },
  arabicIcon: { fontSize: 20 },
  arabicPctBadge: { borderRadius: 999, paddingHorizontal: 8, paddingVertical: 3 },
  arabicPctText: { color: '#fff', fontWeight: '900', fontSize: 11 },
  arabicCardName: { fontSize: 15, fontWeight: '900', textAlign: 'right' },
  arabicCardNameFr: { fontSize: 10, color: '#94a3b8', fontWeight: '700', textAlign: 'right' },
  arabicBarTrack: { width: '100%', height: 4, borderRadius: 999, backgroundColor: '#f1f5f9', overflow: 'hidden' },
  arabicBarFill: { height: '100%', borderRadius: 999 },

  // Subjects
  subjectsRow: { flexDirection: 'row', gap: 10 },
  subjectCardWrap: { flex: 1 },
  subjectCard: {
    backgroundColor: '#fff', borderRadius: 20, overflow: 'hidden',
    paddingHorizontal: 12, paddingBottom: 14, gap: 6,
    shadowColor: '#182b66', shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.08, shadowRadius: 12, elevation: 4,
  },
  subjectAccent:   { height: 4, marginBottom: 8 },
  subjectIconWrap: { width: 42, height: 42, borderRadius: 13, alignItems: 'center', justifyContent: 'center' },
  subjectIcon:     { fontSize: 22 },
  subjectName:     { fontSize: 12, fontWeight: '800', color: COLORS.ink },
  subjectPct:      { fontSize: 20, fontWeight: '900' },
  subjectBarTrack: { width: '100%', height: 5, borderRadius: 999, backgroundColor: '#f1f5f9', overflow: 'hidden' },
  subjectBarFill:  { height: '100%', borderRadius: 999 },
});
