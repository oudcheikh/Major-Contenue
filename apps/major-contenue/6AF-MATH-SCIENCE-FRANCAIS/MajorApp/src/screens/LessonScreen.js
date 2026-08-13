import React, { useEffect, useMemo, useRef, useState } from 'react';
import {
  Animated,
  ScrollView,
  StyleSheet,
  Text,
  TouchableOpacity,
  View,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { SafeAreaView } from 'react-native-safe-area-context';

import { COLORS, SHADOWS } from '../theme';
import { SUBJECTS } from '../data/exercises';
import { playErrorSound, playSuccessSound, playTapSound } from '../utils/uiSounds';
import CourseVisualizer from '../components/CourseVisualizer';

// ─── Training cards (unchanged logic) ─────────────────────────────────────────
function buildTrainingCards(lesson) {
  if (lesson.subjectId === 'math') {
    return [
      { question: '1/3 + 1/4 ?', options: ['Dénominateur commun', 'Addition directe', 'Plus grand dessous'], correctIndex: 0, tip: 'Même dénominateur.', why: 'Même taille de parts.' },
      { question: '2/3 × 3/4 ?', options: ['(2×3)/(3×4)', '2+3/3+4', '2×4 et 3×3'], correctIndex: 0, tip: 'Multiplie haut et bas.', why: 'Règle des fractions.' },
      { question: 'Astuce rapide ?', options: ['Simplifier', 'Abandonner', 'Changer de chapitre'], correctIndex: 0, tip: 'Simplifie avant.', why: 'Moins d\'erreurs.' },
    ];
  }
  if (lesson.subjectId === 'science') {
    return [
      { question: 'Plante = ?', options: ['Lumière + eau', 'Sable seul', 'Chaleur seule'], correctIndex: 0, tip: 'Soleil + eau.', why: 'Base de vie.' },
      { question: 'Inspiration ?', options: ['Air entre', 'Air sort', 'Rien'], correctIndex: 0, tip: 'Oxygène entre.', why: 'Le corps en a besoin.' },
      { question: 'Chaîne alimentaire ?', options: ['Plantes', 'Carnivores', 'Pierres'], correctIndex: 0, tip: 'Les producteurs d\'abord.', why: 'Ils sont la base.' },
    ];
  }
  return [
    { question: 'Début analyse ?', options: ['Sujet + verbe', 'Compter lettres', 'Chercher adverbes'], correctIndex: 0, tip: 'Trouve le cœur.', why: 'Structure de la phrase.' },
    { question: '"a" ou "à" accent ?', options: ['Test "avait"', 'Au hasard', 'Toujours accent'], correctIndex: 0, tip: 'Test "avait".', why: 'Verbe ou préposition.' },
    { question: 'Mémoriser vite ?', options: ['Mini exemple + répète', 'Lire une fois', 'Sans exercice'], correctIndex: 0, tip: 'Petit + répétition.', why: 'Le cerveau retient mieux.' },
  ];
}

// ─── Animated Option component ────────────────────────────────────────────────
function OptionButton({ label, state, onPress, color }) {
  const scaleAnim = useRef(new Animated.Value(1)).current;

  function handlePress() {
    Animated.sequence([
      Animated.spring(scaleAnim, { toValue: 0.95, useNativeDriver: true, friction: 8, tension: 200 }),
      Animated.spring(scaleAnim, { toValue: 1, useNativeDriver: true, friction: 6, tension: 120 }),
    ]).start();
    onPress();
  }

  const isGood = state === 'correct';
  const isBad = state === 'wrong';
  const isActive = state === 'selected';

  const bgColor = isGood ? '#dcfce7' : isBad ? '#fee2e2' : isActive ? '#eff6ff' : '#fff';
  const borderColor = isGood ? '#16a34a' : isBad ? '#ef4444' : isActive ? color : '#e2e8f0';
  const textColor = isGood ? '#15803d' : isBad ? '#dc2626' : isActive ? color : '#1e293b';
  const icon = isGood ? '✓' : isBad ? '✕' : null;

  return (
    <Animated.View style={{ transform: [{ scale: scaleAnim }] }}>
      <TouchableOpacity
        style={[styles.option, { backgroundColor: bgColor, borderColor, borderWidth: isActive || isGood || isBad ? 2 : 1.5 }]}
        onPress={handlePress}
        activeOpacity={0.9}
      >
        {icon && (
          <View style={[styles.optionIcon, { backgroundColor: isGood ? '#16a34a' : '#ef4444' }]}>
            <Text style={styles.optionIconText}>{icon}</Text>
          </View>
        )}
        <Text style={[styles.optionText, { color: textColor, fontWeight: isActive || isGood ? '800' : '600' }]}>
          {label}
        </Text>
      </TouchableOpacity>
    </Animated.View>
  );
}

// ─── Key Point card (staggered entrance) ─────────────────────────────────────
function KeyPointCard({ text, index, color }) {
  const anim = useRef(new Animated.Value(0)).current;
  const slideAnim = useRef(new Animated.Value(20)).current;

  useEffect(() => {
    const delay = index * 120;
    Animated.parallel([
      Animated.timing(anim, { toValue: 1, duration: 380, delay, useNativeDriver: true }),
      Animated.spring(slideAnim, { toValue: 0, delay, friction: 9, tension: 65, useNativeDriver: true }),
    ]).start();
  }, []);

  return (
    <Animated.View style={[styles.keyPoint, { opacity: anim, transform: [{ translateY: slideAnim }] }]}>
      <View style={[styles.keyPointBar, { backgroundColor: color }]} />
      <Text style={styles.keyPointText}>{text}</Text>
    </Animated.View>
  );
}

// ─── XP Badge (animates in on success) ───────────────────────────────────────
function XpBadge({ visible, xp = 10 }) {
  const scaleAnim = useRef(new Animated.Value(0)).current;
  const rotateAnim = useRef(new Animated.Value(-8)).current;

  useEffect(() => {
    if (visible) {
      Animated.parallel([
        Animated.spring(scaleAnim, { toValue: 1, friction: 5, tension: 80, useNativeDriver: true }),
        Animated.spring(rotateAnim, { toValue: 0, friction: 6, tension: 60, useNativeDriver: true }),
      ]).start();
    } else {
      scaleAnim.setValue(0);
      rotateAnim.setValue(-8);
    }
  }, [visible]);

  if (!visible) return null;
  const rotate = rotateAnim.interpolate({ inputRange: [-8, 0], outputRange: ['-8deg', '0deg'] });

  return (
    <Animated.View style={[styles.xpBadge, { transform: [{ scale: scaleAnim }, { rotate }] }]}>
      <LinearGradient colors={['#F0B429', '#fb923c']} style={styles.xpBadgeInner} start={{ x: 0, y: 0 }} end={{ x: 1, y: 1 }}>
        <Text style={styles.xpBadgeText}>+{xp} XP</Text>
      </LinearGradient>
    </Animated.View>
  );
}

// ─── Progress Bar ─────────────────────────────────────────────────────────────
function ProgressBar({ current, total, color }) {
  const widthAnim = useRef(new Animated.Value(0)).current;

  useEffect(() => {
    Animated.timing(widthAnim, {
      toValue: total > 0 ? (current / total) * 100 : 0,
      duration: 500,
      useNativeDriver: false,
    }).start();
  }, [current, total]);

  const width = widthAnim.interpolate({ inputRange: [0, 100], outputRange: ['0%', '100%'] });

  return (
    <View style={styles.progressTrack}>
      <Animated.View style={[styles.progressFill, { width, backgroundColor: color }]} />
    </View>
  );
}

// ─── Main Screen ──────────────────────────────────────────────────────────────
export default function LessonScreen({ route, navigation }) {
  const lesson = route?.params?.lesson;

  if (!lesson) {
    return (
      <SafeAreaView style={styles.safe} edges={['top']}>
        <View style={[styles.errorCard]}>
          <Text style={styles.errorTitle}>Mini-cours introuvable.</Text>
          <TouchableOpacity style={[styles.primaryBtn, { backgroundColor: COLORS.primary }]} onPress={() => navigation.navigate('Home')}>
            <Text style={styles.primaryBtnText}>Accueil</Text>
          </TouchableOpacity>
        </View>
      </SafeAreaView>
    );
  }

  const color = lesson.subjectColor || COLORS.primary;
  const gradient = lesson.subjectGradient || ['#2563eb', '#38bdf8'];
  const cards = useMemo(() => buildTrainingCards(lesson), [lesson.id, lesson.subjectId]);
  const miniPoints = useMemo(
    () => (lesson.keyPoints || []).slice(0, 3),
    [lesson.keyPoints]
  );

  const [cardIndex, setCardIndex] = useState(0);
  const [selected, setSelected] = useState(null);
  const [validated, setValidated] = useState(false);
  const [isCorrect, setIsCorrect] = useState(false);
  const [showXp, setShowXp] = useState(false);
  const [correctCount, setCorrectCount] = useState(0);
  const [finished, setFinished] = useState(false);

  // Header entrance
  const headerAnim = useRef(new Animated.Value(-60)).current;
  const headerOpacity = useRef(new Animated.Value(0)).current;
  // Card slide transition
  const cardSlide = useRef(new Animated.Value(0)).current;
  const cardOpacity = useRef(new Animated.Value(1)).current;
  // Feedback shake
  const shakeAnim = useRef(new Animated.Value(0)).current;
  // Success pulse
  const successScale = useRef(new Animated.Value(1)).current;

  const activeCard = cards[cardIndex];

  useEffect(() => {
    Animated.parallel([
      Animated.spring(headerAnim, { toValue: 0, friction: 8, tension: 60, useNativeDriver: true }),
      Animated.timing(headerOpacity, { toValue: 1, duration: 350, useNativeDriver: true }),
    ]).start();
  }, []);

  function animateCardIn() {
    cardSlide.setValue(40);
    cardOpacity.setValue(0);
    Animated.parallel([
      Animated.spring(cardSlide, { toValue: 0, friction: 8, tension: 70, useNativeDriver: true }),
      Animated.timing(cardOpacity, { toValue: 1, duration: 280, useNativeDriver: true }),
    ]).start();
  }

  function animateShake() {
    Animated.sequence([
      Animated.timing(shakeAnim, { toValue: 8, duration: 60, useNativeDriver: true }),
      Animated.timing(shakeAnim, { toValue: -8, duration: 60, useNativeDriver: true }),
      Animated.timing(shakeAnim, { toValue: 6, duration: 60, useNativeDriver: true }),
      Animated.timing(shakeAnim, { toValue: 0, duration: 60, useNativeDriver: true }),
    ]).start();
  }

  function animateSuccessPulse() {
    Animated.sequence([
      Animated.spring(successScale, { toValue: 1.04, friction: 4, tension: 120, useNativeDriver: true }),
      Animated.spring(successScale, { toValue: 1, friction: 6, tension: 80, useNativeDriver: true }),
    ]).start();
  }

  function getOptionState(i) {
    if (!validated) return selected === i ? 'selected' : 'idle';
    if (i === activeCard.correctIndex) return 'correct';
    if (selected === i && i !== activeCard.correctIndex) return 'wrong';
    return 'idle';
  }

  async function onChoose(i) {
    if (validated) return;
    setSelected(i);
    await playTapSound();
  }

  async function onVerify() {
    if (selected === null || validated) return;
    const ok = selected === activeCard.correctIndex;
    setValidated(true);
    setIsCorrect(ok);

    if (ok) {
      await playSuccessSound();
      setCorrectCount((c) => c + 1);
      setShowXp(true);
      animateSuccessPulse();
      setTimeout(() => setShowXp(false), 2000);
    } else {
      await playErrorSound();
      animateShake();
    }
  }

  async function nextCard() {
    if (cardIndex >= cards.length - 1) {
      setFinished(true);
      return;
    }
    await playTapSound();
    // Animate out
    Animated.parallel([
      Animated.timing(cardOpacity, { toValue: 0, duration: 160, useNativeDriver: true }),
    ]).start(() => {
      setCardIndex((v) => v + 1);
      setSelected(null);
      setValidated(false);
      setIsCorrect(false);
      animateCardIn();
    });
  }

  async function retryCard() {
    setSelected(null);
    setValidated(false);
    setIsCorrect(false);
    await playTapSound();
    animateCardIn();
  }

  function handlePractice() {
    const subjectFull = SUBJECTS.find((s) => s.id === lesson.subjectId);
    if (subjectFull) navigation.navigate('Quiz', { subject: subjectFull });
  }

  // ─── FINISHED SCREEN ──────────────────────────────────────────────────────
  if (finished) {
    const pct = Math.round((correctCount / cards.length) * 100);
    const stars = pct >= 100 ? 3 : pct >= 66 ? 2 : pct >= 33 ? 1 : 0;
    return (
      <SafeAreaView style={styles.safe} edges={['top', 'bottom']}>
        <LinearGradient colors={gradient} style={styles.finishGradient} start={{ x: 0.1, y: 0 }} end={{ x: 0.9, y: 1 }}>
          <View style={styles.starsRow}>
            {[1, 2, 3].map((s) => (
              <Text key={s} style={[styles.starEmoji, stars >= s ? {} : styles.starDim]}>⭐</Text>
            ))}
          </View>
          <Text style={styles.finishTitle}>Leçon terminée !</Text>
          <Text style={styles.finishSubtitle}>درس منتهي</Text>
          <View style={styles.finishBadge}>
            <Text style={styles.finishBadgeText}>{correctCount}/{cards.length} correctes</Text>
          </View>
        </LinearGradient>

        <View style={styles.finishCard}>
          <Text style={styles.encouragement}>{lesson.encouragement}</Text>

          <TouchableOpacity
            style={[styles.primaryBtn, { backgroundColor: color }, SHADOWS.button]}
            onPress={handlePractice}
            activeOpacity={0.88}
          >
            <Text style={styles.primaryBtnText}>Quiz complet →</Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={styles.ghostBtn}
            onPress={() => navigation.navigate('Home')}
            activeOpacity={0.88}
          >
            <Text style={[styles.ghostBtnText, { color }]}>Accueil</Text>
          </TouchableOpacity>
        </View>
      </SafeAreaView>
    );
  }

  // ─── MAIN LESSON SCREEN ───────────────────────────────────────────────────
  return (
    <SafeAreaView style={styles.safe} edges={['top']}>
      {/* ── Header ── */}
      <Animated.View style={{ transform: [{ translateY: headerAnim }], opacity: headerOpacity }}>
        <LinearGradient colors={gradient} style={styles.header} start={{ x: 0.1, y: 0 }} end={{ x: 0.9, y: 1 }}>
          <View style={styles.headerRow}>
            <TouchableOpacity onPress={() => navigation.goBack()} style={styles.backBtn} activeOpacity={0.8}>
              <Text style={styles.backBtnText}>←</Text>
            </TouchableOpacity>
            <View style={styles.headerCenter}>
              <Text style={styles.headerTitle} numberOfLines={1}>{lesson.emoji} {lesson.title}</Text>
            </View>
            <View style={styles.xpPill}>
              <Text style={styles.xpPillText}>XP 🏆</Text>
            </View>
          </View>
          <ProgressBar current={cardIndex + (validated ? 1 : 0)} total={cards.length} color="rgba(255,255,255,0.9)" />
          <Text style={styles.progressLabel}>{cardIndex + 1} / {cards.length} questions</Text>
        </LinearGradient>
      </Animated.View>

      <ScrollView
        style={styles.scroll}
        contentContainerStyle={styles.content}
        showsVerticalScrollIndicator={false}
      >
        {/* ── Key Points ── */}
        <View style={styles.sectionHeader}>
          <View style={[styles.sectionDot, { backgroundColor: color }]} />
          <Text style={styles.sectionTitle}>Points clés · النقاط الأساسية</Text>
        </View>

        <View style={styles.keyPointsWrapper}>
          {miniPoints.map((p, i) => (
            <KeyPointCard key={`${lesson.id}-kp-${i}`} text={p} index={i} color={color} />
          ))}
        </View>

        {/* ── Rule Card ── */}
        {!!lesson.rule && (
          <LinearGradient colors={gradient} style={styles.ruleCard} start={{ x: 0, y: 0 }} end={{ x: 1, y: 0 }}>
            <Text style={styles.ruleLabel}>📐 RÈGLE · القاعدة</Text>
            <Text style={styles.ruleText}>{lesson.rule}</Text>
            {!!lesson.tip && <Text style={styles.ruleTip}>{lesson.tip}</Text>}
          </LinearGradient>
        )}

        {/* ── Course Visualizer ── */}
        <CourseVisualizer subjectId={lesson.subjectId} color={color} />

        {/* ── Quiz Card ── */}
        <Animated.View
          style={[
            styles.quizCard,
            SHADOWS.card,
            { transform: [{ translateX: shakeAnim }, { translateY: cardSlide }, { scale: successScale }], opacity: cardOpacity },
          ]}
        >
          {/* Card header */}
          <View style={styles.quizCardHeader}>
            <View style={[styles.quizSubjectPill, { backgroundColor: color + '22' }]}>
              <Text style={[styles.quizSubjectPillText, { color }]}>
                {lesson.emoji} Carte {cardIndex + 1}/{cards.length}
              </Text>
            </View>
            <XpBadge visible={showXp} xp={10} />
          </View>

          <Text style={styles.question}>{activeCard.question}</Text>

          {/* Options */}
          <View style={styles.optionsWrapper}>
            {activeCard.options.map((opt, i) => (
              <OptionButton
                key={`opt-${cardIndex}-${i}`}
                label={opt}
                state={getOptionState(i)}
                onPress={() => onChoose(i)}
                color={color}
              />
            ))}
          </View>

          {/* Feedback (after validation) */}
          {validated && (
            <Animated.View style={[styles.feedback, isCorrect ? styles.feedbackGood : styles.feedbackBad, { transform: [{ scale: successScale }] }]}>
              <Text style={styles.feedbackTitle}>
                {isCorrect ? '🎉 Excellent ! Bonne réponse' : '💪 Presque ! Voici l\'astuce'}
              </Text>
              <Text style={styles.feedbackBody}>💡 {activeCard.tip}</Text>
              <Text style={styles.feedbackWhy}>🔎 {activeCard.why}</Text>
            </Animated.View>
          )}
        </Animated.View>

        {/* Bottom padding for sticky button */}
        <View style={{ height: 100 }} />
      </ScrollView>

      {/* ── Sticky Bottom CTA ── */}
      <View style={styles.stickyBottom}>
        {!validated ? (
          <TouchableOpacity
            style={[styles.primaryBtn, { backgroundColor: selected !== null ? color : '#cbd5e1' }, SHADOWS.button]}
            onPress={onVerify}
            disabled={selected === null}
            activeOpacity={0.88}
          >
            <Text style={styles.primaryBtnText}>
              {selected !== null ? 'VÉRIFIER ✓' : 'Choisis une réponse'}
            </Text>
          </TouchableOpacity>
        ) : isCorrect ? (
          <TouchableOpacity
            style={[styles.primaryBtn, { backgroundColor: '#10b981' }, SHADOWS.button]}
            onPress={nextCard}
            activeOpacity={0.88}
          >
            <Text style={styles.primaryBtnText}>
              {cardIndex >= cards.length - 1 ? 'TERMINER 🏆' : 'SUIVANT →'}
            </Text>
          </TouchableOpacity>
        ) : (
          <View style={styles.retryRow}>
            <TouchableOpacity style={[styles.retryBtn, { borderColor: color }]} onPress={retryCard} activeOpacity={0.88}>
              <Text style={[styles.retryBtnText, { color }]}>Réessayer</Text>
            </TouchableOpacity>
            <TouchableOpacity
              style={[styles.primaryBtn, { backgroundColor: color, flex: 1 }, SHADOWS.button]}
              onPress={nextCard}
              activeOpacity={0.88}
            >
              <Text style={styles.primaryBtnText}>
                {cardIndex >= cards.length - 1 ? 'TERMINER 🏆' : 'SUIVANT →'}
              </Text>
            </TouchableOpacity>
          </View>
        )}
      </View>
    </SafeAreaView>
  );
}

// ─── Styles ────────────────────────────────────────────────────────────────────
const styles = StyleSheet.create({
  safe: { flex: 1, backgroundColor: COLORS.background },

  // Header
  header: { paddingHorizontal: 16, paddingTop: 10, paddingBottom: 14, gap: 10 },
  headerRow: { flexDirection: 'row', alignItems: 'center', gap: 10 },
  backBtn: {
    width: 36, height: 36, borderRadius: 18,
    backgroundColor: 'rgba(255,255,255,0.22)',
    alignItems: 'center', justifyContent: 'center',
  },
  backBtnText: { color: '#fff', fontWeight: '900', fontSize: 18, lineHeight: 22 },
  headerCenter: { flex: 1 },
  headerTitle: { fontSize: 16, fontWeight: '900', color: '#fff' },
  xpPill: {
    backgroundColor: 'rgba(255,255,255,0.22)',
    borderRadius: 999, paddingHorizontal: 10, paddingVertical: 4,
  },
  xpPillText: { color: '#fff', fontWeight: '800', fontSize: 11 },

  // Progress
  progressTrack: {
    height: 6, borderRadius: 999,
    backgroundColor: 'rgba(255,255,255,0.25)',
    overflow: 'hidden',
  },
  progressFill: { height: '100%', borderRadius: 999 },
  progressLabel: { color: 'rgba(255,255,255,0.8)', fontSize: 10, fontWeight: '700', textAlign: 'right' },

  // Scroll
  scroll: { flex: 1 },
  content: { padding: 16, gap: 14 },

  // Section header
  sectionHeader: { flexDirection: 'row', alignItems: 'center', gap: 8, marginBottom: 2 },
  sectionDot: { width: 8, height: 8, borderRadius: 4 },
  sectionTitle: { color: COLORS.muted, fontSize: 11, fontWeight: '800', letterSpacing: 0.8, textTransform: 'uppercase' },

  // Key points
  keyPointsWrapper: { gap: 8 },
  keyPoint: {
    flexDirection: 'row', alignItems: 'flex-start', gap: 10,
    backgroundColor: '#fff', borderRadius: 14, padding: 12,
    ...StyleSheet.flatten({
      shadowColor: '#182b66', shadowOffset: { width: 0, height: 2 },
      shadowOpacity: 0.06, shadowRadius: 8, elevation: 2,
    }),
  },
  keyPointBar: { width: 4, borderRadius: 2, alignSelf: 'stretch', minHeight: 20 },
  keyPointText: { flex: 1, color: '#1e293b', fontSize: 13, lineHeight: 20, fontWeight: '600' },

  // Rule card
  ruleCard: { borderRadius: 20, padding: 18, gap: 8 },
  ruleLabel: { color: 'rgba(255,255,255,0.8)', fontSize: 10, fontWeight: '900', letterSpacing: 1.4, textTransform: 'uppercase' },
  ruleText: { color: '#fff', fontSize: 17, fontWeight: '900', lineHeight: 26 },
  ruleTip: { color: 'rgba(255,255,255,0.88)', fontSize: 12, fontWeight: '700', lineHeight: 18, marginTop: 4 },

  // Quiz card
  quizCard: {
    backgroundColor: '#fff', borderRadius: 24,
    padding: 18, gap: 16,
  },
  quizCardHeader: { flexDirection: 'row', alignItems: 'center', justifyContent: 'space-between' },
  quizSubjectPill: {
    borderRadius: 999, paddingHorizontal: 12, paddingVertical: 5,
  },
  quizSubjectPillText: { fontSize: 11, fontWeight: '800', letterSpacing: 0.6 },

  // XP Badge
  xpBadge: { position: 'absolute', right: 0, top: -4 },
  xpBadgeInner: { borderRadius: 999, paddingHorizontal: 12, paddingVertical: 6 },
  xpBadgeText: { color: '#fff', fontWeight: '900', fontSize: 13 },

  // Question
  question: { color: COLORS.ink, fontSize: 17, fontWeight: '900', lineHeight: 26 },

  // Options
  optionsWrapper: { gap: 10 },
  option: {
    borderRadius: 16, padding: 14,
    flexDirection: 'row', alignItems: 'center', gap: 10,
    borderColor: '#e2e8f0',
  },
  optionIcon: {
    width: 24, height: 24, borderRadius: 12,
    alignItems: 'center', justifyContent: 'center',
  },
  optionIconText: { color: '#fff', fontWeight: '900', fontSize: 12 },
  optionText: { flex: 1, fontSize: 14, lineHeight: 20 },

  // Feedback
  feedback: { borderRadius: 16, padding: 14, gap: 6 },
  feedbackGood: { backgroundColor: '#f0fdf4', borderWidth: 1.5, borderColor: '#86efac' },
  feedbackBad: { backgroundColor: '#fff7ed', borderWidth: 1.5, borderColor: '#fed7aa' },
  feedbackTitle: { color: COLORS.ink, fontWeight: '900', fontSize: 14 },
  feedbackBody: { color: '#334155', fontWeight: '700', fontSize: 13, lineHeight: 20 },
  feedbackWhy: { color: '#64748b', fontWeight: '600', fontSize: 12, lineHeight: 18 },

  // Sticky bottom
  stickyBottom: {
    position: 'absolute', bottom: 0, left: 0, right: 0,
    backgroundColor: '#fff',
    borderTopWidth: 1, borderTopColor: '#f1f5f9',
    paddingHorizontal: 16, paddingVertical: 12, paddingBottom: 24,
  },
  primaryBtn: {
    borderRadius: 18, paddingVertical: 16,
    alignItems: 'center', justifyContent: 'center',
  },
  primaryBtnText: { color: '#fff', fontWeight: '900', fontSize: 15, letterSpacing: 0.4 },
  retryRow: { flexDirection: 'row', gap: 10 },
  retryBtn: {
    borderRadius: 18, paddingVertical: 16, paddingHorizontal: 20,
    borderWidth: 2, alignItems: 'center', justifyContent: 'center',
  },
  retryBtnText: { fontWeight: '900', fontSize: 14 },

  // Finish screen
  finishGradient: {
    paddingTop: 60, paddingBottom: 40, alignItems: 'center', gap: 12,
  },
  starsRow: { flexDirection: 'row', gap: 8 },
  starEmoji: { fontSize: 36 },
  starDim: { opacity: 0.3 },
  finishTitle: { color: '#fff', fontSize: 28, fontWeight: '900', textAlign: 'center' },
  finishSubtitle: { color: 'rgba(255,255,255,0.8)', fontSize: 16, fontWeight: '700', textAlign: 'right' },
  finishBadge: {
    backgroundColor: 'rgba(255,255,255,0.22)',
    borderRadius: 999, paddingHorizontal: 20, paddingVertical: 8,
  },
  finishBadgeText: { color: '#fff', fontWeight: '900', fontSize: 14 },
  finishCard: {
    flex: 1, backgroundColor: '#fff',
    borderTopLeftRadius: 28, borderTopRightRadius: 28,
    padding: 24, gap: 14, marginTop: -20,
  },
  encouragement: {
    color: '#78350f', backgroundColor: '#fef3c7',
    borderRadius: 14, padding: 14,
    fontWeight: '700', lineHeight: 22, fontSize: 14,
    borderWidth: 1, borderColor: '#fde68a',
  },
  ghostBtn: {
    borderRadius: 18, paddingVertical: 14,
    alignItems: 'center', backgroundColor: '#f8fafc',
    borderWidth: 1.5, borderColor: '#e2e8f0',
  },
  ghostBtnText: { fontWeight: '800', fontSize: 14 },

  // Error state
  errorCard: {
    margin: 20, backgroundColor: '#fff', borderRadius: 20,
    padding: 24, gap: 16, alignItems: 'center',
    ...StyleSheet.flatten({ shadowColor: '#182b66', shadowOffset: { width: 0, height: 4 }, shadowOpacity: 0.08, shadowRadius: 12, elevation: 4 }),
  },
  errorTitle: { color: COLORS.ink, fontWeight: '900', fontSize: 16, textAlign: 'center' },
});
