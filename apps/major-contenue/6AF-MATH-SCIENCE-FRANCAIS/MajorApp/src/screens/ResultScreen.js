import React, { useEffect, useState, useRef } from 'react';
import { View, Text, TouchableOpacity, ScrollView, StyleSheet, Animated, Dimensions } from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { SafeAreaView } from 'react-native-safe-area-context';
import { updateStats } from '../utils/storage';
import { completeDailyChallenge } from '../utils/dailyChallenge';
import { computeSubjectLevel, getEncouragementMessage } from '../utils/levelDetection';
import LevelBadge from '../components/LevelBadge';
import { COLORS } from '../theme';

const { width } = Dimensions.get('window');
const CONFETTI_COLORS = ['#fde68a', '#38bdf8', '#34d399', '#fb923c', '#a78bfa', '#f472b6', '#fff'];
const NUM_CONFETTI = 22;

function Confetti({ active }) {
  const particles = useRef(
    Array.from({ length: NUM_CONFETTI }, (_, i) => ({
      x: new Animated.Value(Math.random() * width),
      y: new Animated.Value(-20),
      rotate: new Animated.Value(0),
      opacity: new Animated.Value(1),
      color: CONFETTI_COLORS[i % CONFETTI_COLORS.length],
      size: 6 + Math.random() * 8,
      delay: Math.random() * 600,
      duration: 1600 + Math.random() * 1000,
    }))
  ).current;

  useEffect(() => {
    if (!active) return;
    particles.forEach((p) => {
      p.x.setValue(Math.random() * width);
      p.y.setValue(-20);
      p.opacity.setValue(1);
      setTimeout(() => {
        Animated.parallel([
          Animated.timing(p.y, { toValue: 700, duration: p.duration, useNativeDriver: true }),
          Animated.timing(p.rotate, { toValue: 720, duration: p.duration, useNativeDriver: true }),
          Animated.timing(p.opacity, { toValue: 0, duration: p.duration, delay: p.duration * 0.6, useNativeDriver: true }),
        ]).start();
      }, p.delay);
    });
  }, [active]);

  if (!active) return null;

  return (
    <View style={StyleSheet.absoluteFill} pointerEvents="none">
      {particles.map((p, i) => (
        <Animated.View
          key={i}
          style={{
            position: 'absolute',
            width: p.size,
            height: p.size,
            borderRadius: p.size / 4,
            backgroundColor: p.color,
            transform: [
              { translateX: p.x },
              { translateY: p.y },
              { rotate: p.rotate.interpolate({ inputRange: [0, 720], outputRange: ['0deg', '720deg'] }) },
            ],
            opacity: p.opacity,
          }}
        />
      ))}
    </View>
  );
}

function StarRating({ pct, color }) {
  const stars = pct >= 90 ? 3 : pct >= 60 ? 2 : 1;
  const scales = [useRef(new Animated.Value(0)).current, useRef(new Animated.Value(0)).current, useRef(new Animated.Value(0)).current];

  useEffect(() => {
    scales.forEach((s, i) => {
      if (i < stars) {
        setTimeout(() => {
          Animated.spring(s, { toValue: 1, tension: 100, friction: 6, useNativeDriver: true }).start();
        }, 500 + i * 200);
      }
    });
  }, []);

  return (
    <View style={{ flexDirection: 'row', gap: 8, justifyContent: 'center' }}>
      {scales.map((s, i) => (
        <Animated.Text key={i} style={{ fontSize: 36, transform: [{ scale: s }], opacity: i < stars ? 1 : 0.2 }}>
          ⭐
        </Animated.Text>
      ))}
    </View>
  );
}

export default function ResultScreen({ route, navigation }) {
  const { subject, correct, total, exercises } = route.params;
  const pct = Math.round((correct / total) * 100);

  const [stats, setStats] = useState(null);
  const [confettiActive, setConfettiActive] = useState(false);
  const displayLabel = subject.isArabic ? subject.labelAr : subject.label;
  const [message] = useState(() => getEncouragementMessage(pct, displayLabel, subject.isArabic));

  const scaleAnim = useRef(new Animated.Value(0)).current;
  const slideAnim = useRef(new Animated.Value(40)).current;
  const opacityAnim = useRef(new Animated.Value(0)).current;
  const pctAnim = useRef(new Animated.Value(0)).current;

  useEffect(() => {
    (async () => {
      if (subject.id !== 'challenge') {
        const updated = await updateStats(subject.id, correct, total);
        setStats(updated);
      } else {
        await completeDailyChallenge(correct, total);
      }
    })();

    Animated.sequence([
      Animated.parallel([
        Animated.spring(scaleAnim, { toValue: 1, tension: 55, friction: 7, useNativeDriver: true }),
        Animated.timing(opacityAnim, { toValue: 1, duration: 500, useNativeDriver: true }),
      ]),
      Animated.timing(pctAnim, { toValue: pct, duration: 900, useNativeDriver: false }),
    ]).start();

    if (pct >= 60) {
      setTimeout(() => setConfettiActive(true), 400);
    }
  }, []);

  const subjectLevel = stats ? computeSubjectLevel(stats[subject.id]) : null;
  const emoji = pct === 100 ? '🏆' : pct >= 80 ? '🎉' : pct >= 60 ? '💪' : pct >= 40 ? '📚' : '🌱';

  return (
    <SafeAreaView style={styles.safe}>
      <Confetti active={confettiActive} />

      {/* Header coloré */}
      <LinearGradient colors={[subject.color, subject.color + 'BB']} style={styles.header} start={{ x: 0, y: 0 }} end={{ x: 1, y: 1 }}>
        <View style={styles.headerCircle1} />
        <View style={styles.headerCircle2} />
        <Text style={styles.headerSubject}>{subject.icon} {displayLabel}</Text>
        <Text style={[styles.headerTitle, subject.isArabic && { textAlign: 'right' }]}>
          {subject.isArabic ? 'انتهت الجلسة !' : 'Session terminée !'}
        </Text>
      </LinearGradient>

      <ScrollView contentContainerStyle={styles.container} showsVerticalScrollIndicator={false}>

        {/* Score cercle */}
        <Animated.View style={[styles.scoreSection, { opacity: opacityAnim, transform: [{ scale: scaleAnim }] }]}>
          <View style={[styles.scoreCircleOuter, { borderColor: subject.color + '30' }]}>
            <View style={[styles.scoreCircle, { borderColor: subject.color }]}>
              <Text style={styles.scoreEmoji}>{emoji}</Text>
              <Text style={[styles.scorePct, { color: subject.color }]}>{pct}%</Text>
              <Text style={styles.scoreLabel}>
            {subject.isArabic ? `${correct} / ${total} إجابات صحيحة` : `${correct} / ${total} bonnes réponses`}
          </Text>
            </View>
          </View>
          <StarRating pct={pct} color={subject.color} />
        </Animated.View>

        {/* Message encourageant */}
        <Animated.View style={[styles.messageCard, {
          opacity: opacityAnim,
          transform: [{ translateY: slideAnim }],
          borderLeftColor: subject.color,
        }]}>
          <Text style={[styles.messageTitle, { color: subject.color }]}>{message.title}</Text>
          <Text style={styles.messageBody}>{message.body}</Text>
        </Animated.View>

        {/* Niveau mis à jour */}
        {subjectLevel && (
          <Animated.View style={[styles.levelCard, { opacity: opacityAnim }]}>
            <Text style={styles.levelLabel}>
              {subject.isArabic ? `مستواك في ${displayLabel}` : `Ton niveau en ${displayLabel}`}
            </Text>
            <LevelBadge level={subjectLevel.level} size="lg" />
            <View style={styles.levelProgress}>
              <View style={[styles.levelProgressFill, { width: `${subjectLevel.pct}%`, backgroundColor: subjectLevel.level.color }]} />
            </View>
            <Text style={[styles.levelPct, { color: subjectLevel.level.color }]}>
            {subject.isArabic ? `${subjectLevel.pct}٪ نجاح` : `${subjectLevel.pct}% de réussite`}
          </Text>
          </Animated.View>
        )}

        {/* Boutons */}
        <TouchableOpacity
          style={styles.btn}
          onPress={() => navigation.replace('Quiz', { subject })}
          activeOpacity={0.85}
        >
          <LinearGradient colors={[subject.color, subject.color + 'CC']} style={styles.btnGradient} start={{ x: 0, y: 0 }} end={{ x: 1, y: 0 }}>
            <Text style={styles.btnText}>{subject.isArabic ? '🔄 إعادة المحاولة' : '🔄 Recommencer'}</Text>
          </LinearGradient>
        </TouchableOpacity>

        <TouchableOpacity
          style={[styles.btnOutline, { borderColor: subject.color }]}
          onPress={() => navigation.navigate('Home')}
          activeOpacity={0.85}
        >
          <Text style={[styles.btnOutlineText, { color: subject.color }]}>
            {subject.isArabic ? '🏠 العودة للرئيسية' : '🏠 Retour à l\'accueil'}
          </Text>
        </TouchableOpacity>

        <View style={{ height: 24 }} />
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safe: { flex: 1, backgroundColor: COLORS.background },

  header: {
    paddingTop: 16,
    paddingBottom: 30,
    paddingHorizontal: 24,
    gap: 4,
    overflow: 'hidden',
  },
  headerCircle1: {
    position: 'absolute', width: 180, height: 180, borderRadius: 90,
    backgroundColor: 'rgba(255,255,255,0.1)', top: -70, right: -40,
  },
  headerCircle2: {
    position: 'absolute', width: 100, height: 100, borderRadius: 50,
    backgroundColor: 'rgba(255,255,255,0.08)', bottom: -30, left: 30,
  },
  headerSubject: { color: 'rgba(255,255,255,0.85)', fontSize: 14, fontWeight: '800' },
  headerTitle: { color: '#fff', fontSize: 26, fontWeight: '900' },

  container: { padding: 20, gap: 16, alignItems: 'center' },

  scoreSection: { alignItems: 'center', gap: 16, marginTop: 4 },
  scoreCircleOuter: {
    width: 200, height: 200, borderRadius: 100,
    borderWidth: 3, alignItems: 'center', justifyContent: 'center',
  },
  scoreCircle: {
    width: 180, height: 180, borderRadius: 90,
    borderWidth: 5, backgroundColor: '#fff',
    alignItems: 'center', justifyContent: 'center', gap: 4,
    shadowColor: '#0f172a', shadowOffset: { width: 0, height: 10 },
    shadowOpacity: 0.12, shadowRadius: 20, elevation: 8,
  },
  scoreEmoji: { fontSize: 38 },
  scorePct: { fontSize: 44, fontWeight: '900' },
  scoreLabel: { fontSize: 12, color: COLORS.muted, fontWeight: '700' },

  messageCard: {
    backgroundColor: '#fff', borderRadius: 18, padding: 18,
    borderLeftWidth: 4, width: '100%', gap: 6,
    shadowColor: '#0f172a', shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.07, shadowRadius: 10, elevation: 4,
  },
  messageTitle: { fontSize: 18, fontWeight: '900' },
  messageBody: { fontSize: 14, color: COLORS.muted, lineHeight: 22 },

  levelCard: {
    backgroundColor: '#fff', borderRadius: 18, padding: 18,
    alignItems: 'center', gap: 10, width: '100%',
    shadowColor: '#0f172a', shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.07, shadowRadius: 10, elevation: 4,
  },
  levelLabel: { fontSize: 13, color: COLORS.muted, fontWeight: '700' },
  levelProgress: {
    width: '100%', height: 8, borderRadius: 999,
    backgroundColor: '#f1f5f9', overflow: 'hidden',
  },
  levelProgressFill: { height: '100%', borderRadius: 999 },
  levelPct: { fontSize: 13, fontWeight: '800' },

  btn: { width: '100%', borderRadius: 16, overflow: 'hidden', elevation: 6, shadowColor: '#0f172a', shadowOffset: { width: 0, height: 4 }, shadowOpacity: 0.15, shadowRadius: 10 },
  btnGradient: { padding: 17, alignItems: 'center' },
  btnText: { color: '#fff', fontSize: 16, fontWeight: '900' },

  btnOutline: {
    width: '100%', borderRadius: 16, padding: 16,
    alignItems: 'center', borderWidth: 2, backgroundColor: '#fff',
  },
  btnOutlineText: { fontSize: 16, fontWeight: '800' },
});
