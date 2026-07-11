import React, { useState, useRef, useEffect } from 'react';
import {
  View, Text, TouchableOpacity, ScrollView, StyleSheet, Animated,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { SafeAreaView } from 'react-native-safe-area-context';
import { COLORS } from '../theme';

const OPTION_LETTERS = ['A', 'B', 'C', 'D'];

export default function QuizScreen({ route, navigation }) {
  const { subject } = route.params;
  const exercises = [...subject.exercises].sort(() => Math.random() - 0.5).slice(0, 10);

  const [index, setIndex] = useState(0);
  const [selected, setSelected] = useState(null);
  const [confirmed, setConfirmed] = useState(false);
  const [answers, setAnswers] = useState([]);
  const [showExplanation, setShowExplanation] = useState(false);

  const progress = useRef(new Animated.Value(0)).current;
  const shake = useRef(new Animated.Value(0)).current;
  const cardScale = useRef(new Animated.Value(0.96)).current;
  const cardOpacity = useRef(new Animated.Value(0)).current;
  const celebScale = useRef(new Animated.Value(0)).current;

  const current = exercises[index];
  const totalQ = exercises.length;
  const correctSoFar = answers.filter((a) => a.correct).length;

  useEffect(() => {
    Animated.timing(progress, {
      toValue: ((index) / totalQ) * 100,
      duration: 500,
      useNativeDriver: false,
    }).start();
    // Entrée question
    cardScale.setValue(0.93);
    cardOpacity.setValue(0);
    Animated.parallel([
      Animated.spring(cardScale, { toValue: 1, tension: 70, friction: 9, useNativeDriver: true }),
      Animated.timing(cardOpacity, { toValue: 1, duration: 300, useNativeDriver: true }),
    ]).start();
  }, [index]);

  function handleSelect(i) {
    if (confirmed) return;
    setSelected(i);
  }

  function handleConfirm() {
    if (selected === null) return;
    const isCorrect = selected === current.answer;
    setConfirmed(true);
    setShowExplanation(true);
    setAnswers((prev) => [...prev, { correct: isCorrect }]);

    if (isCorrect) {
      celebScale.setValue(0);
      Animated.spring(celebScale, { toValue: 1, tension: 100, friction: 6, useNativeDriver: true }).start();
    } else {
      Animated.sequence([
        Animated.timing(shake, { toValue: 10, duration: 55, useNativeDriver: true }),
        Animated.timing(shake, { toValue: -10, duration: 55, useNativeDriver: true }),
        Animated.timing(shake, { toValue: 8, duration: 55, useNativeDriver: true }),
        Animated.timing(shake, { toValue: 0, duration: 55, useNativeDriver: true }),
      ]).start();
    }
  }

  function handleNext() {
    const allAnswers = [...answers, { correct: selected === current.answer }];
    if (index + 1 >= totalQ) {
      const correct = allAnswers.filter((a) => a.correct).length;
      navigation.replace('Result', { subject, correct, total: totalQ, exercises });
      return;
    }
    setIndex((i) => i + 1);
    setSelected(null);
    setConfirmed(false);
    setShowExplanation(false);
  }

  function getOptionStyle(i) {
    if (!confirmed) {
      if (selected === i) return [styles.option, { borderColor: subject.color, backgroundColor: subject.color + '14' }];
      return styles.option;
    }
    if (i === current.answer) return [styles.option, styles.optionCorrect];
    if (i === selected && i !== current.answer) return [styles.option, styles.optionWrong];
    return [styles.option, styles.optionDim];
  }

  function getLetterStyle(i) {
    if (!confirmed) {
      if (selected === i) return [styles.letter, { backgroundColor: subject.color }];
      return styles.letter;
    }
    if (i === current.answer) return [styles.letter, styles.letterCorrect];
    if (i === selected && i !== current.answer) return [styles.letter, styles.letterWrong];
    return [styles.letter, styles.letterDim];
  }

  const progressWidth = progress.interpolate({ inputRange: [0, 100], outputRange: ['0%', '100%'] });

  return (
    <SafeAreaView style={styles.safe} edges={['top']}>

      {/* Header */}
      <LinearGradient colors={[subject.color, subject.color + 'CC']} style={styles.header} start={{ x: 0, y: 0 }} end={{ x: 1, y: 0 }}>
        <TouchableOpacity onPress={() => navigation.goBack()} style={styles.closeBtn}>
          <Text style={styles.closeBtnText}>✕</Text>
        </TouchableOpacity>
        <View style={styles.headerCenter}>
          <View style={styles.progressTrack}>
            <Animated.View style={[styles.progressFill, { width: progressWidth }]} />
          </View>
          <Text style={styles.headerCounter}>{index + 1} / {totalQ}</Text>
        </View>
        <View style={styles.scoreMini}>
          <Text style={styles.scoreMiniText}>✅ {correctSoFar}</Text>
        </View>
      </LinearGradient>

      {/* Dots de progression */}
      <View style={styles.dots}>
        {exercises.map((_, i) => {
          const isPast = i < index;
          const isCurrent = i === index;
          const wasCorrect = isPast && answers[i]?.correct;
          const wasWrong = isPast && !answers[i]?.correct;
          return (
            <View
              key={i}
              style={[
                styles.dot,
                isCurrent && { backgroundColor: subject.color, transform: [{ scale: 1.3 }] },
                wasCorrect && { backgroundColor: '#22c55e' },
                wasWrong && { backgroundColor: '#ef4444' },
                !isPast && !isCurrent && { backgroundColor: '#e2e8f0' },
              ]}
            />
          );
        })}
      </View>

      <ScrollView style={styles.scroll} contentContainerStyle={styles.content} keyboardShouldPersistTaps="handled">

        {/* Carte question */}
        <Animated.View style={[styles.questionCard, { opacity: cardOpacity, transform: [{ scale: cardScale }, { translateX: shake }] }]}>
          <View style={styles.questionMeta}>
            <View style={[styles.subjectTag, { backgroundColor: subject.color + '18' }]}>
              <Text style={[styles.subjectTagText, { color: subject.color }]}>
                {subject.icon} {subject.isArabic ? subject.labelAr : subject.label}
              </Text>
            </View>
            <Text style={styles.diffStars}>{'★'.repeat(current.difficulty)}{'☆'.repeat(3 - current.difficulty)}</Text>
          </View>
          <Text style={[styles.questionText, subject.isArabic && styles.questionTextAr]}>{current.question}</Text>
        </Animated.View>

        {/* Options */}
        <View style={styles.options}>
          {current.options.map((opt, i) => (
            <TouchableOpacity
              key={i}
              style={[getOptionStyle(i), subject.isArabic && styles.optionRtl]}
              onPress={() => handleSelect(i)}
              activeOpacity={confirmed ? 1 : 0.8}
            >
              <View style={getLetterStyle(i)}>
                <Text style={styles.letterText}>{OPTION_LETTERS[i]}</Text>
              </View>
              <Text style={[
                styles.optionText,
                subject.isArabic && styles.optionTextAr,
                confirmed && i === current.answer && { color: '#15803d', fontWeight: '800' },
                confirmed && i === selected && i !== current.answer && { color: '#dc2626', fontWeight: '800' },
                confirmed && i !== current.answer && i !== selected && { color: '#94a3b8' },
              ]}>
                {opt}
              </Text>
              {confirmed && i === current.answer && (
                <Animated.Text style={[styles.checkMark, { transform: [{ scale: celebScale }] }]}>✓</Animated.Text>
              )}
              {confirmed && i === selected && i !== current.answer && (
                <Text style={styles.wrongMark}>✗</Text>
              )}
            </TouchableOpacity>
          ))}
        </View>

        {/* Explication */}
        {showExplanation && (
          <Animated.View style={[
            styles.explanation,
            selected === current.answer ? styles.explanationOk : styles.explanationKo,
            { opacity: cardOpacity },
          ]}>
            <Text style={styles.explanationEmoji}>
              {selected === current.answer ? '🎉' : '💡'}
            </Text>
            <View style={{ flex: 1 }}>
              <Text style={[styles.explanationTitle, subject.isArabic && { textAlign: 'right' }]}>
                {selected === current.answer
                  ? (subject.isArabic ? 'أحسنت !' : 'Bravo !')
                  : (subject.isArabic ? 'الإجابة الصحيحة :' : 'La bonne réponse :')}
              </Text>
              <Text style={[styles.explanationText, subject.isArabic && { textAlign: 'right' }]}>
                {current.explanation}
              </Text>
            </View>
          </Animated.View>
        )}

        {/* Bouton */}
        {!confirmed ? (
          <TouchableOpacity
            style={[styles.actionBtn, selected === null && styles.actionBtnDisabled]}
            onPress={handleConfirm}
            disabled={selected === null}
            activeOpacity={0.85}
          >
            <LinearGradient
              colors={selected !== null ? [subject.color, subject.color + 'CC'] : ['#cbd5e1', '#94a3b8']}
              style={styles.actionBtnGradient}
              start={{ x: 0, y: 0 }} end={{ x: 1, y: 0 }}
            >
              <Text style={styles.actionBtnText}>
                {subject.isArabic ? 'تأكيد الإجابة ✓' : 'Valider ma réponse ✓'}
              </Text>
            </LinearGradient>
          </TouchableOpacity>
        ) : (
          <TouchableOpacity style={styles.actionBtn} onPress={handleNext} activeOpacity={0.85}>
            <LinearGradient colors={[subject.color, subject.color + 'CC']} style={styles.actionBtnGradient} start={{ x: 0, y: 0 }} end={{ x: 1, y: 0 }}>
              <Text style={styles.actionBtnText}>
                {index + 1 >= totalQ
                  ? (subject.isArabic ? 'عرض النتائج 🏆' : 'Voir mes résultats 🏆')
                  : (subject.isArabic ? 'السؤال التالي →' : 'Question suivante →')}
              </Text>
            </LinearGradient>
          </TouchableOpacity>
        )}

        <View style={{ height: 24 }} />
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safe: { flex: 1, backgroundColor: COLORS.background },

  header: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingHorizontal: 16,
    paddingVertical: 12,
    gap: 10,
  },
  closeBtn: {
    width: 34, height: 34, borderRadius: 17,
    backgroundColor: 'rgba(255,255,255,0.22)',
    alignItems: 'center', justifyContent: 'center',
  },
  closeBtnText: { color: '#fff', fontWeight: '900', fontSize: 14 },
  headerCenter: { flex: 1, gap: 5 },
  progressTrack: { height: 7, borderRadius: 999, backgroundColor: 'rgba(255,255,255,0.28)', overflow: 'hidden' },
  progressFill: { height: '100%', borderRadius: 999, backgroundColor: '#fff' },
  headerCounter: { color: 'rgba(255,255,255,0.85)', fontSize: 11, fontWeight: '800', textAlign: 'right' },
  scoreMini: {
    backgroundColor: 'rgba(255,255,255,0.22)',
    paddingHorizontal: 10, paddingVertical: 5, borderRadius: 999,
  },
  scoreMiniText: { color: '#fff', fontWeight: '900', fontSize: 13 },

  dots: { flexDirection: 'row', justifyContent: 'center', gap: 5, paddingVertical: 10, flexWrap: 'wrap', paddingHorizontal: 16 },
  dot: { width: 8, height: 8, borderRadius: 4 },

  scroll: { flex: 1 },
  content: { padding: 16, gap: 14 },

  questionCard: {
    backgroundColor: '#fff',
    borderRadius: 22,
    padding: 20,
    gap: 12,
    shadowColor: '#0f172a',
    shadowOffset: { width: 0, height: 5 },
    shadowOpacity: 0.1,
    shadowRadius: 14,
    elevation: 5,
  },
  questionMeta: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center' },
  subjectTag: { paddingHorizontal: 12, paddingVertical: 5, borderRadius: 999 },
  subjectTagText: { fontSize: 12, fontWeight: '800' },
  diffStars: { fontSize: 14, color: '#f59e0b' },
  questionText: { fontSize: 18, fontWeight: '700', color: COLORS.ink, lineHeight: 28 },
  questionTextAr: { textAlign: 'right', fontWeight: '800', fontSize: 17, lineHeight: 30 },

  options: { gap: 10 },
  option: {
    backgroundColor: '#fff', borderRadius: 16,
    borderWidth: 2, borderColor: '#e2e8f0',
    padding: 14, flexDirection: 'row', alignItems: 'center', gap: 12,
    shadowColor: '#0f172a', shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.04, shadowRadius: 6, elevation: 2,
  },
  optionCorrect: { borderColor: '#22c55e', backgroundColor: '#f0fdf4' },
  optionWrong: { borderColor: '#ef4444', backgroundColor: '#fef2f2' },
  optionDim: { borderColor: '#f1f5f9', backgroundColor: '#fafafa' },

  letter: {
    width: 34, height: 34, borderRadius: 17,
    backgroundColor: '#f1f5f9',
    alignItems: 'center', justifyContent: 'center', flexShrink: 0,
  },
  letterCorrect: { backgroundColor: '#22c55e' },
  letterWrong: { backgroundColor: '#ef4444' },
  letterDim: { backgroundColor: '#e2e8f0' },
  letterText: { fontSize: 13, fontWeight: '900', color: COLORS.ink },

  optionText: { flex: 1, fontSize: 15, color: COLORS.ink, lineHeight: 22, fontWeight: '600' },
  optionTextAr: { textAlign: 'right', fontWeight: '700' },
  optionRtl: { flexDirection: 'row-reverse' },
  checkMark: { fontSize: 20, color: '#22c55e', fontWeight: '900' },
  wrongMark: { fontSize: 20, color: '#ef4444', fontWeight: '900' },

  explanation: {
    borderRadius: 16, padding: 16,
    flexDirection: 'row', gap: 12, alignItems: 'flex-start',
  },
  explanationOk: { backgroundColor: '#f0fdf4', borderLeftWidth: 4, borderLeftColor: '#22c55e' },
  explanationKo: { backgroundColor: '#fef2f2', borderLeftWidth: 4, borderLeftColor: '#ef4444' },
  explanationEmoji: { fontSize: 24 },
  explanationTitle: { fontSize: 15, fontWeight: '900', color: COLORS.ink, marginBottom: 4 },
  explanationText: { fontSize: 13, color: COLORS.muted, lineHeight: 20 },

  actionBtn: { borderRadius: 18, overflow: 'hidden', elevation: 6, shadowColor: '#0f172a', shadowOffset: { width: 0, height: 4 }, shadowOpacity: 0.15, shadowRadius: 10 },
  actionBtnDisabled: { opacity: 0.6 },
  actionBtnGradient: { padding: 17, alignItems: 'center' },
  actionBtnText: { color: '#fff', fontSize: 17, fontWeight: '900' },
});
