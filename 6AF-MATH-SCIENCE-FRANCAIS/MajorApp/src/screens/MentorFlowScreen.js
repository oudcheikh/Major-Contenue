import React, { useEffect, useMemo, useRef, useState } from 'react';
import {
  Animated,
  ScrollView,
  StyleSheet,
  Text,
  TextInput,
  TouchableOpacity,
  ActivityIndicator,
  View,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { SafeAreaView } from 'react-native-safe-area-context';

import { COLORS, SHADOWS } from '../theme';
import { getStudent } from '../utils/storage';
import {
  chatWithMentorSimple,
  generateMentorNudge,
  generateMentorSession,
  getLastMentorError,
  isMentorLLMConfigured,
} from '../utils/mentorLLM';
import {
  startMentorRecording,
  stopMentorRecordingAndTranscribe,
  speakWithOpenAITTS,
  stopMentorVoice,
} from '../utils/mentorVoice';
import MentorScene from '../components/MentorScene';
import {
  awardMicroWin,
  awardScanPoints,
  buildWeeklyParentSummary,
  computeKnowledgeLevel,
  getChapterInsight,
  recordChapterScan,
  recordMicroFail,
  setPreferredLanguage,
  shouldSuggestTutor,
} from '../utils/phygitalStorage';

// ─── Step Progress Bar ────────────────────────────────────────────────────────
function StepBar({ step, total = 3, color }) {
  const widthAnim = useRef(new Animated.Value((1 / total) * 100)).current;

  useEffect(() => {
    Animated.timing(widthAnim, {
      toValue: (step / total) * 100,
      duration: 450,
      useNativeDriver: false,
    }).start();
  }, [step]);

  const width = widthAnim.interpolate({ inputRange: [0, 100], outputRange: ['0%', '100%'] });

  return (
    <View style={stepBarStyles.track}>
      <Animated.View style={[stepBarStyles.fill, { width, backgroundColor: color || 'rgba(255,255,255,0.9)' }]} />
    </View>
  );
}
const stepBarStyles = StyleSheet.create({
  track: { height: 5, borderRadius: 999, backgroundColor: 'rgba(255,255,255,0.25)', overflow: 'hidden' },
  fill: { height: '100%', borderRadius: 999 },
});

// ─── Summary Point (staggered) ────────────────────────────────────────────────
function SummaryPoint({ text, index, color }) {
  const opacity = useRef(new Animated.Value(0)).current;
  const slide = useRef(new Animated.Value(16)).current;

  useEffect(() => {
    Animated.parallel([
      Animated.timing(opacity, { toValue: 1, duration: 360, delay: index * 140, useNativeDriver: true }),
      Animated.spring(slide, { toValue: 0, delay: index * 140, friction: 9, tension: 60, useNativeDriver: true }),
    ]).start();
  }, []);

  return (
    <Animated.View style={[spStyles.row, { opacity, transform: [{ translateY: slide }] }]}>
      <View style={[spStyles.num, { backgroundColor: color }]}>
        <Text style={spStyles.numText}>{index + 1}</Text>
      </View>
      <Text style={spStyles.text}>{text}</Text>
    </Animated.View>
  );
}
const spStyles = StyleSheet.create({
  row: { flexDirection: 'row', alignItems: 'flex-start', gap: 12, backgroundColor: '#fff', borderRadius: 16, padding: 14, ...StyleSheet.flatten({ shadowColor: '#182b66', shadowOffset: { width: 0, height: 2 }, shadowOpacity: 0.06, shadowRadius: 8, elevation: 2 }) },
  num: { width: 28, height: 28, borderRadius: 14, alignItems: 'center', justifyContent: 'center', marginTop: 1 },
  numText: { color: '#fff', fontWeight: '900', fontSize: 12 },
  text: { flex: 1, color: '#1e293b', fontSize: 13, lineHeight: 20, fontWeight: '600' },
});

// ─── Option Button (quiz) ─────────────────────────────────────────────────────
function OptionButton({ label, state, onPress, color }) {
  const scaleAnim = useRef(new Animated.Value(1)).current;

  function handlePress() {
    Animated.sequence([
      Animated.spring(scaleAnim, { toValue: 0.96, useNativeDriver: true, friction: 8, tension: 200 }),
      Animated.spring(scaleAnim, { toValue: 1, useNativeDriver: true, friction: 6, tension: 120 }),
    ]).start();
    onPress();
  }

  const isGood = state === 'correct';
  const isBad = state === 'wrong';
  const isActive = state === 'selected';
  const bgColor = isGood ? '#f0fdf4' : isBad ? '#fef2f2' : isActive ? '#eff6ff' : '#fff';
  const borderColor = isGood ? '#16a34a' : isBad ? '#ef4444' : isActive ? color : '#e2e8f0';
  const textColor = isGood ? '#15803d' : isBad ? '#dc2626' : isActive ? color : '#1e293b';
  const icon = isGood ? '✓' : isBad ? '✕' : null;

  return (
    <Animated.View style={{ transform: [{ scale: scaleAnim }] }}>
      <TouchableOpacity
        style={[optStyles.btn, { backgroundColor: bgColor, borderColor, borderWidth: isActive || isGood || isBad ? 2 : 1.5 }]}
        onPress={handlePress}
        activeOpacity={0.9}
      >
        {icon && <View style={[optStyles.icon, { backgroundColor: isGood ? '#16a34a' : '#ef4444' }]}><Text style={optStyles.iconText}>{icon}</Text></View>}
        <Text style={[optStyles.text, { color: textColor, fontWeight: isActive || isGood ? '800' : '600' }]}>{label}</Text>
      </TouchableOpacity>
    </Animated.View>
  );
}
const optStyles = StyleSheet.create({
  btn: { borderRadius: 16, padding: 14, flexDirection: 'row', alignItems: 'center', gap: 10 },
  icon: { width: 24, height: 24, borderRadius: 12, alignItems: 'center', justifyContent: 'center' },
  iconText: { color: '#fff', fontWeight: '900', fontSize: 12 },
  text: { flex: 1, fontSize: 14, lineHeight: 20 },
});

// ─── Main Screen ──────────────────────────────────────────────────────────────
const STEP_LABELS = ['Discussion', 'Résumé', 'Défi'];
const STEP_LABELS_AR = ['نقاش', 'ملخص', 'تحدي'];

export default function MentorFlowScreen({ route, navigation }) {
  const lesson = route?.params?.lesson;

  if (!lesson) {
    return (
      <SafeAreaView style={styles.safe} edges={['top']}>
        <View style={styles.errorCard}>
          <Text style={styles.errorTitle}>Session mentor introuvable.</Text>
          <Text style={styles.errorBody}>Reviens à l'accueil puis rescane une page pour relancer la session.</Text>
          <TouchableOpacity style={[styles.primaryBtn, { backgroundColor: COLORS.primary }]} onPress={() => navigation.navigate('Home')}>
            <Text style={styles.primaryBtnText}>Retour à l'accueil</Text>
          </TouchableOpacity>
        </View>
      </SafeAreaView>
    );
  }

  const color = lesson.subjectColor || COLORS.primary;
  const gradient = lesson.subjectGradient || ['#182b66', '#2563eb'];

  // ── State (unchanged logic) ──────────────────────────────────────────────
  const [step, setStep] = useState(1);
  const [student, setStudent] = useState(null);
  const [profile, setProfile] = useState(null);
  const [selected, setSelected] = useState(null);
  const [validated, setValidated] = useState(false);
  const [isCorrect, setIsCorrect] = useState(false);
  const [chapterInsight, setChapterInsight] = useState(null);
  const [parentSummary, setParentSummary] = useState('');
  const [audioStatus, setAudioStatus] = useState('idle');
  const [autoPlayed, setAutoPlayed] = useState(false);
  const [mentorSession, setMentorSession] = useState(null);
  const [isGeneratingMentor, setIsGeneratingMentor] = useState(true);
  const [coachReply, setCoachReply] = useState('');
  const [attemptCount, setAttemptCount] = useState(0);
  const [llmError, setLlmError] = useState('');
  const [chatInput, setChatInput] = useState('');
  const [chatLoading, setChatLoading] = useState(false);
  const [isRecordingVoice, setIsRecordingVoice] = useState(false);
  const [voiceError, setVoiceError] = useState('');
  const [chatMessages, setChatMessages] = useState([
    { role: 'assistant', text: 'Salam ! Pose ta question en une phrase. Je réponds simplement.' },
  ]);

  const llmReady = isMentorLLMConfigured();

  // ── Step transition animation ────────────────────────────────────────────
  const stepOpacity = useRef(new Animated.Value(1)).current;
  const stepSlide = useRef(new Animated.Value(0)).current;

  function animateStepTransition(nextStep) {
    Animated.parallel([
      Animated.timing(stepOpacity, { toValue: 0, duration: 180, useNativeDriver: true }),
      Animated.timing(stepSlide, { toValue: -20, duration: 180, useNativeDriver: true }),
    ]).start(() => {
      setStep(nextStep);
      stepSlide.setValue(20);
      Animated.parallel([
        Animated.timing(stepOpacity, { toValue: 1, duration: 280, useNativeDriver: true }),
        Animated.spring(stepSlide, { toValue: 0, friction: 8, tension: 60, useNativeDriver: true }),
      ]).start();
    });
  }

  // ── Init (unchanged logic) ───────────────────────────────────────────────
  useEffect(() => {
    (async () => {
      const st = await getStudent();
      setStudent(st);
      const afterScan = await awardScanPoints();
      await recordChapterScan(lesson.id);
      setProfile(afterScan);
      await setPreferredLanguage('fr');
      const insight = await getChapterInsight(lesson.id);
      setChapterInsight(insight);

      const instantSession = {
        hook: `Salam ${st?.name || 'champion'} ! On commence tout de suite. ${lesson.summary} Quel point veux-tu comprendre en premier ?`,
        summaryPoints: (lesson?.keyPoints || []).slice(0, 3),
        microChallenge: {
          question: `Quel est le point central de "${lesson.title}" ?`,
          options: [
            lesson?.keyPoints?.[0] || 'Revoir le résumé',
            lesson?.keyPoints?.[1] || 'Ignorer les étapes',
            lesson?.keyPoints?.[2] || 'Tout mémoriser sans comprendre',
            'Attendre plus tard',
          ],
          correctIndex: 0,
          hint: 'Commence par l\'idée principale de la leçon.',
        },
      };
      setMentorSession(instantSession);

      setIsGeneratingMentor(true);
      const llmContent = await generateMentorSession({ lesson, studentName: st?.name, failCount: insight?.consecutiveFails || 0 });
      if (llmContent) setMentorSession(llmContent);
      setLlmError(getLastMentorError());
      setIsGeneratingMentor(false);
    })();
    return () => { stopMentorVoice(); };
  }, [lesson.id]);

  const activeHookText = useMemo(() => mentorSession?.hook || '', [mentorSession]);
  const activeSummary = useMemo(() => mentorSession?.summaryPoints || [], [mentorSession]);
  const microChallenge = useMemo(() => mentorSession?.microChallenge || null, [mentorSession]);

  // ── Audio (unchanged logic) ───────────────────────────────────────────────
  async function speakHook() {
    await stopMentorVoice();
    if (!activeHookText) { setAudioStatus('error'); setVoiceError('Aucun texte à lire.'); return; }
    setVoiceError('');
    setAudioStatus('playing');
    const played = await speakWithOpenAITTS(activeHookText, { onDone: () => setAudioStatus('done'), onError: () => setAudioStatus('error'), voice: 'nova' });
    if (!played) { setAudioStatus('error'); setVoiceError('Voix IA indisponible. Vérifie la clé API, le réseau, et ton quota OpenAI.'); }
  }

  useEffect(() => {
    if (!profile || step !== 1 || autoPlayed || !activeHookText) return;
    const t = setTimeout(() => { speakHook(); setAutoPlayed(true); }, 300);
    return () => clearTimeout(t);
  }, [profile, step, autoPlayed, activeHookText]);

  // ── Chat (unchanged logic) ────────────────────────────────────────────────
  async function askMentor(questionText) {
    const q = String(questionText || '').trim();
    if (!q || chatLoading) return;
    const userMsg = { role: 'user', text: q };
    const history = [...chatMessages, userMsg];
    setChatMessages(history);
    setChatInput('');
    setChatLoading(true);
    setVoiceError('');
    const reply = await chatWithMentorSimple({ lesson, studentName: student?.name, question: q, recentHistory: history });
    const safeReply = reply || 'D\'accord. Quelle étape te bloque exactement ?';
    setChatMessages((prev) => [...prev, { role: 'assistant', text: safeReply }]);
    setChatLoading(false);
    const played = await speakWithOpenAITTS(safeReply, { onDone: () => setAudioStatus('done'), onError: () => setAudioStatus('error'), voice: 'nova' });
    if (!played) setVoiceError('Réponse générée, mais voix IA non jouée. Vérifie ton quota OpenAI.');
  }

  async function sendSimpleQuestion() { await askMentor(chatInput); }
  async function sendQuick(label) { await askMentor(label); }

  async function startVoiceQuestion() {
    if (chatLoading || isRecordingVoice) return;
    const ok = await startMentorRecording();
    if (!ok) { setVoiceError('Micro indisponible. Autorise le micro puis réessaie.'); return; }
    setVoiceError('');
    setIsRecordingVoice(true);
  }

  async function stopVoiceQuestion() {
    if (!isRecordingVoice) return;
    setIsRecordingVoice(false);
    const transcript = await stopMentorRecordingAndTranscribe();
    if (!transcript) { setVoiceError('Je n\'ai pas compris ta voix. Réessaie en parlant 2-4 secondes.'); return; }
    await askMentor(transcript);
  }

  // ── Quiz (unchanged logic) ────────────────────────────────────────────────
  async function handleValidate() {
    if (selected === null || validated || !microChallenge) return;
    const newAttempt = attemptCount + 1;
    setAttemptCount(newAttempt);
    const correct = selected === microChallenge.correctIndex;
    setValidated(true);
    setIsCorrect(correct);

    if (correct) {
      const updated = await awardMicroWin(lesson.id);
      setProfile(updated);
      setChapterInsight(await getChapterInsight(lesson.id));
      if (student?.name) setParentSummary(await buildWeeklyParentSummary(student.name));
      const nudge = await generateMentorNudge({ lesson, studentName: student?.name, isCorrect: true, attempts: newAttempt, selectedOption: microChallenge.options[selected], question: microChallenge.question });
      setCoachReply(nudge || 'Zine ! Quelle est la prochaine étape selon toi ?');
      return;
    }
    const failState = await recordMicroFail(lesson.id);
    setProfile(failState.profile);
    setChapterInsight(failState.chapter);
    const nudge = await generateMentorNudge({ lesson, studentName: student?.name, isCorrect: false, attempts: newAttempt, selectedOption: microChallenge.options[selected], question: microChallenge.question });
    setCoachReply(nudge || 'On va très simple. Quelle partie te semble confuse ?');
  }

  function getOptionState(i) {
    if (!validated) return selected === i ? 'selected' : 'idle';
    if (i === microChallenge?.correctIndex) return 'correct';
    if (selected === i) return 'wrong';
    return 'idle';
  }

  const knowledge = profile ? computeKnowledgeLevel(profile) : null;
  const suggestTutor = chapterInsight ? shouldSuggestTutor(chapterInsight) : false;

  // ── RENDER ────────────────────────────────────────────────────────────────
  return (
    <SafeAreaView style={styles.safe} edges={['top']}>

      {/* ── Header ── */}
      <LinearGradient colors={gradient} style={styles.header} start={{ x: 0.1, y: 0 }} end={{ x: 0.9, y: 1 }}>
        <View style={styles.headerRow}>
          <TouchableOpacity onPress={() => navigation.goBack()} style={styles.backBtn} activeOpacity={0.8}>
            <Text style={styles.backBtnText}>←</Text>
          </TouchableOpacity>
          <View style={styles.headerCenter}>
            <Text style={styles.headerTitle}>{lesson.emoji} Mentor IA</Text>
            <Text style={styles.headerStepLabel}>
              {STEP_LABELS[step - 1]} · {STEP_LABELS_AR[step - 1]}
            </Text>
          </View>
          {knowledge && (
            <View style={styles.xpBadge}>
              <Text style={styles.xpBadgeText}>{knowledge.level.icon} {knowledge.pct}%</Text>
            </View>
          )}
        </View>
        <StepBar step={step} total={3} />
        <View style={styles.stepDotsRow}>
          {[1, 2, 3].map((n) => (
            <View key={n} style={[styles.stepDot, step >= n && { backgroundColor: 'rgba(255,255,255,0.9)' }]}>
              <Text style={[styles.stepDotText, step >= n && { color: gradient[1] || '#2563eb' }]}>{n}</Text>
            </View>
          ))}
        </View>
      </LinearGradient>

      {/* ── Alerts ── */}
      {!llmReady && (
        <View style={styles.alertCard}>
          <Text style={styles.alertTitle}>⚠️ LLM non configuré</Text>
          <Text style={styles.alertBody}>Ajoute EXPO_PUBLIC_OPENAI_API_KEY puis redémarre Expo.</Text>
        </View>
      )}
      {llmReady && isGeneratingMentor && (
        <View style={[styles.alertCard, { backgroundColor: '#eff6ff', borderColor: '#bfdbfe' }]}>
          <ActivityIndicator size="small" color={color} />
          <Text style={[styles.alertTitle, { color: color }]}>Major prépare ta session...</Text>
        </View>
      )}

      {/* ── Step Content ── */}
      <Animated.View style={[{ flex: 1 }, { opacity: stepOpacity, transform: [{ translateY: stepSlide }] }]}>

        {/* ── STEP 1 : Discussion ── */}
        {step === 1 && (
          <ScrollView style={styles.scroll} contentContainerStyle={styles.content} showsVerticalScrollIndicator={false}>

            {/* Mascot hero */}
            <View style={[styles.mascotHero, { borderColor: color + '33' }]}>
              <MentorScene subjectId={lesson.subjectId} isSpeaking={audioStatus === 'playing'} isLoading={isGeneratingMentor} />
              {audioStatus === 'playing' && (
                <View style={[styles.speakingBadge, { backgroundColor: color }]}>
                  <Text style={styles.speakingBadgeText}>🔊 En train de parler...</Text>
                </View>
              )}
            </View>

            {/* Hook text bubble */}
            {!!activeHookText && (
              <View style={[styles.hookBubble, { borderLeftColor: color }]}>
                <Text style={styles.hookText}>{activeHookText}</Text>
              </View>
            )}

            {/* Voice replay */}
            <TouchableOpacity style={[styles.voiceReplayBtn, { borderColor: color }]} onPress={speakHook} activeOpacity={0.85}>
              <Text style={[styles.voiceReplayText, { color }]}>
                {audioStatus === 'playing' ? '🔊 En lecture...' : '▶ Rejouer la voix du mentor'}
              </Text>
            </TouchableOpacity>

            {/* Voice error */}
            {!!voiceError && <View style={styles.errorPill}><Text style={styles.errorPillText}>⚠️ {voiceError}</Text></View>}

            {/* Chat */}
            <View style={styles.chatCard}>
              <Text style={styles.chatTitle}>💬 Pose ta question</Text>

              <ScrollView style={styles.chatList} contentContainerStyle={{ gap: 8 }} showsVerticalScrollIndicator={false}>
                {chatMessages.slice(-6).map((m, i) => (
                  <View key={`${m.role}-${i}`} style={[styles.bubble, m.role === 'user' ? styles.bubbleUser : styles.bubbleBot]}>
                    <Text style={[styles.bubbleText, m.role === 'user' ? styles.bubbleTextUser : {}]}>{m.text}</Text>
                  </View>
                ))}
                {chatLoading && (
                  <View style={[styles.bubble, styles.bubbleBot]}>
                    <ActivityIndicator size="small" color={color} />
                  </View>
                )}
              </ScrollView>

              {/* Quick actions */}
              <View style={styles.quickRow}>
                {['Explique plus simple', 'Donne un exemple', 'Je comprends !'].map((label) => (
                  <TouchableOpacity key={label} style={[styles.quickChip, { borderColor: color + '55' }]} onPress={() => sendQuick(label)} activeOpacity={0.85}>
                    <Text style={[styles.quickChipText, { color }]}>{label}</Text>
                  </TouchableOpacity>
                ))}
              </View>

              {/* Text input */}
              <View style={styles.inputRow}>
                <TextInput
                  value={chatInput}
                  onChangeText={setChatInput}
                  placeholder="Ex: Je bloque sur cette étape…"
                  placeholderTextColor="#94a3b8"
                  style={[styles.chatInput, { borderColor: color + '55' }]}
                  onSubmitEditing={sendSimpleQuestion}
                  returnKeyType="send"
                />
                <TouchableOpacity
                  style={[styles.sendBtn, { backgroundColor: color }]}
                  onPress={sendSimpleQuestion}
                  activeOpacity={0.88}
                >
                  {chatLoading ? <ActivityIndicator color="#fff" size="small" /> : <Text style={styles.sendBtnText}>→</Text>}
                </TouchableOpacity>
              </View>

              {/* Voice button */}
              <TouchableOpacity
                style={[styles.voiceHoldBtn, isRecordingVoice && { backgroundColor: color }]}
                onPressIn={startVoiceQuestion}
                onPressOut={stopVoiceQuestion}
                activeOpacity={0.85}
              >
                <Text style={[styles.voiceHoldText, isRecordingVoice && { color: '#fff' }]}>
                  {isRecordingVoice ? '🎙 Parle maintenant… relâche pour envoyer' : '🎙 Maintiens pour parler'}
                </Text>
              </TouchableOpacity>
            </View>

            <View style={{ height: 90 }} />
          </ScrollView>
        )}

        {/* ── STEP 2 : Résumé ── */}
        {step === 2 && (
          <ScrollView style={styles.scroll} contentContainerStyle={styles.content} showsVerticalScrollIndicator={false}>
            <View style={styles.sectionHeader}>
              <Text style={styles.sectionEmoji}>📋</Text>
              <View>
                <Text style={styles.sectionTitle}>Résumé du cours</Text>
                <Text style={styles.sectionSubtitle}>ملخص الدرس</Text>
              </View>
            </View>

            <View style={{ gap: 10 }}>
              {activeSummary.map((point, idx) => (
                <SummaryPoint key={`${lesson.id}-sum-${idx}`} text={point} index={idx} color={color} />
              ))}
            </View>

            {!!lesson.tip && (
              <LinearGradient colors={gradient} style={styles.tipCard} start={{ x: 0, y: 0 }} end={{ x: 1, y: 0 }}>
                <Text style={styles.tipLabel}>🧠 ASTUCE DU CHAMPION</Text>
                <Text style={styles.tipText}>{lesson.tip}</Text>
              </LinearGradient>
            )}

            <View style={{ height: 90 }} />
          </ScrollView>
        )}

        {/* ── STEP 3 : Défi ── */}
        {step === 3 && (
          <ScrollView style={styles.scroll} contentContainerStyle={styles.content} showsVerticalScrollIndicator={false}>
            <View style={styles.sectionHeader}>
              <Text style={styles.sectionEmoji}>⚡</Text>
              <View>
                <Text style={styles.sectionTitle}>Micro-Défi</Text>
                <Text style={styles.sectionSubtitle}>تحدي صغير</Text>
              </View>
            </View>

            <View style={[styles.quizCard, SHADOWS.card]}>
              <Text style={styles.quizQuestion}>{microChallenge?.question || 'Chargement...'}</Text>

              <View style={{ gap: 10 }}>
                {(microChallenge?.options || []).map((opt, i) => (
                  <OptionButton
                    key={`mf-opt-${i}`}
                    label={opt}
                    state={getOptionState(i)}
                    onPress={() => !validated && setSelected(i)}
                    color={color}
                  />
                ))}
              </View>

              {validated && (
                <View style={[styles.feedbackBox, isCorrect ? styles.feedbackGood : styles.feedbackBad]}>
                  <Text style={styles.feedbackTitle}>
                    {isCorrect ? '🎉 Bravo ! +10 crédits' : '💪 On continue ensemble'}
                  </Text>
                  <Text style={styles.feedbackBody}>{coachReply || microChallenge?.hint || 'On va étape par étape.'}</Text>
                </View>
              )}
            </View>

            {suggestTutor && (
              <View style={styles.tutorCard}>
                <Text style={styles.tutorTitle}>📚 Ce chapitre semble difficile.</Text>
                <Text style={styles.tutorBody}>Veux-tu qu'un de nos profs passe t'expliquer ça samedi ?</Text>
                <TouchableOpacity style={[styles.tutorBtn, { backgroundColor: '#ea580c' }]} activeOpacity={0.88}>
                  <Text style={styles.tutorBtnText}>Demander un prof à domicile</Text>
                </TouchableOpacity>
              </View>
            )}

            {!!parentSummary && (
              <View style={styles.parentCard}>
                <Text style={styles.parentTitle}>👨‍👩‍👧 Aperçu rapport parent</Text>
                <Text style={styles.parentBody}>{parentSummary}</Text>
              </View>
            )}

            <View style={{ height: 100 }} />
          </ScrollView>
        )}
      </Animated.View>

      {/* ── Sticky Bottom CTA ── */}
      <View style={styles.stickyBottom}>
        {step === 1 && (
          <TouchableOpacity
            style={[styles.primaryBtn, { backgroundColor: color }, SHADOWS.button]}
            onPress={() => animateStepTransition(2)}
            activeOpacity={0.88}
          >
            <Text style={styles.primaryBtnText}>Voir le résumé →</Text>
          </TouchableOpacity>
        )}
        {step === 2 && (
          <TouchableOpacity
            style={[styles.primaryBtn, { backgroundColor: color }, SHADOWS.button]}
            onPress={() => animateStepTransition(3)}
            activeOpacity={0.88}
          >
            <Text style={styles.primaryBtnText}>Passer au défi ⚡</Text>
          </TouchableOpacity>
        )}
        {step === 3 && !validated && (
          <TouchableOpacity
            style={[styles.primaryBtn, { backgroundColor: selected !== null ? color : '#cbd5e1' }, SHADOWS.button]}
            onPress={handleValidate}
            disabled={selected === null}
            activeOpacity={0.88}
          >
            <Text style={styles.primaryBtnText}>
              {selected !== null ? 'VÉRIFIER ✓' : 'Choisis une réponse'}
            </Text>
          </TouchableOpacity>
        )}
        {step === 3 && validated && (
          <View style={{ gap: 10 }}>
            <TouchableOpacity
              style={[styles.primaryBtn, { backgroundColor: isCorrect ? '#10b981' : color }, SHADOWS.button]}
              onPress={() => navigation.replace('Lesson', { lesson })}
              activeOpacity={0.88}
            >
              <Text style={styles.primaryBtnText}>Voir le mini-cours complet →</Text>
            </TouchableOpacity>
            <TouchableOpacity style={styles.ghostBtn} onPress={() => navigation.navigate('Home')} activeOpacity={0.88}>
              <Text style={[styles.ghostBtnText, { color }]}>Accueil</Text>
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
  header: { paddingHorizontal: 16, paddingTop: 10, paddingBottom: 14, gap: 8 },
  headerRow: { flexDirection: 'row', alignItems: 'center', gap: 10 },
  backBtn: { width: 36, height: 36, borderRadius: 18, backgroundColor: 'rgba(255,255,255,0.22)', alignItems: 'center', justifyContent: 'center' },
  backBtnText: { color: '#fff', fontWeight: '900', fontSize: 18, lineHeight: 22 },
  headerCenter: { flex: 1 },
  headerTitle: { fontSize: 16, fontWeight: '900', color: '#fff' },
  headerStepLabel: { color: 'rgba(255,255,255,0.75)', fontSize: 11, fontWeight: '700', marginTop: 1 },
  xpBadge: { backgroundColor: 'rgba(255,255,255,0.22)', borderRadius: 999, paddingHorizontal: 10, paddingVertical: 4 },
  xpBadgeText: { color: '#fff', fontWeight: '800', fontSize: 11 },
  stepDotsRow: { flexDirection: 'row', justifyContent: 'center', gap: 8, marginTop: 6 },
  stepDot: { width: 24, height: 24, borderRadius: 12, backgroundColor: 'rgba(255,255,255,0.25)', alignItems: 'center', justifyContent: 'center' },
  stepDotText: { color: 'rgba(255,255,255,0.6)', fontWeight: '900', fontSize: 11 },

  // Scroll
  scroll: { flex: 1 },
  content: { padding: 16, gap: 14 },

  // Alerts
  alertCard: { flexDirection: 'row', alignItems: 'center', gap: 10, backgroundColor: '#fff7ed', borderRadius: 12, padding: 12, margin: 12, borderWidth: 1, borderColor: '#fdba74' },
  alertTitle: { color: '#9a3412', fontWeight: '900', fontSize: 13 },
  alertBody: { color: '#7c2d12', lineHeight: 18, fontSize: 12 },

  // Step 1 — Discussion
  mascotHero: {
    backgroundColor: '#fff', borderRadius: 24, borderWidth: 1.5,
    padding: 16, alignItems: 'center', gap: 8,
    ...StyleSheet.flatten({ shadowColor: '#182b66', shadowOffset: { width: 0, height: 4 }, shadowOpacity: 0.08, shadowRadius: 14, elevation: 4 }),
  },
  speakingBadge: { borderRadius: 999, paddingHorizontal: 14, paddingVertical: 5 },
  speakingBadgeText: { color: '#fff', fontWeight: '800', fontSize: 12 },
  hookBubble: {
    backgroundColor: '#fff', borderRadius: 16, padding: 16,
    borderLeftWidth: 4,
    ...StyleSheet.flatten({ shadowColor: '#182b66', shadowOffset: { width: 0, height: 2 }, shadowOpacity: 0.06, shadowRadius: 8, elevation: 2 }),
  },
  hookText: { color: '#1e293b', fontSize: 14, lineHeight: 22, fontWeight: '600' },
  voiceReplayBtn: { borderRadius: 14, borderWidth: 1.5, paddingVertical: 12, alignItems: 'center' },
  voiceReplayText: { fontWeight: '800', fontSize: 13 },
  errorPill: { backgroundColor: '#fee2e2', borderRadius: 10, padding: 10, borderWidth: 1, borderColor: '#fecaca' },
  errorPillText: { color: '#991b1b', fontWeight: '700', fontSize: 12 },

  // Chat
  chatCard: {
    backgroundColor: '#fff', borderRadius: 20, padding: 14, gap: 10,
    ...StyleSheet.flatten({ shadowColor: '#182b66', shadowOffset: { width: 0, height: 2 }, shadowOpacity: 0.06, shadowRadius: 10, elevation: 3 }),
  },
  chatTitle: { color: COLORS.ink, fontWeight: '900', fontSize: 13 },
  chatList: { maxHeight: 200 },
  bubble: { borderRadius: 14, paddingHorizontal: 12, paddingVertical: 9, maxWidth: '85%' },
  bubbleBot: { backgroundColor: '#f1f5f9', alignSelf: 'flex-start' },
  bubbleUser: { backgroundColor: '#eff6ff', alignSelf: 'flex-end' },
  bubbleText: { color: '#1e293b', fontWeight: '600', fontSize: 13, lineHeight: 19 },
  bubbleTextUser: { color: '#1e40af' },
  quickRow: { flexDirection: 'row', gap: 6, flexWrap: 'wrap' },
  quickChip: { borderRadius: 999, paddingHorizontal: 12, paddingVertical: 6, borderWidth: 1.5, backgroundColor: '#f8fafc' },
  quickChipText: { fontSize: 11, fontWeight: '800' },
  inputRow: { flexDirection: 'row', gap: 8, alignItems: 'center' },
  chatInput: {
    flex: 1, borderWidth: 1.5, borderRadius: 12,
    backgroundColor: '#f8fafc', color: COLORS.ink,
    paddingHorizontal: 12, paddingVertical: 10,
    fontWeight: '600', fontSize: 13,
  },
  sendBtn: { width: 42, height: 42, borderRadius: 12, alignItems: 'center', justifyContent: 'center' },
  sendBtnText: { color: '#fff', fontWeight: '900', fontSize: 18 },
  voiceHoldBtn: {
    borderRadius: 14, paddingVertical: 12, alignItems: 'center',
    backgroundColor: '#f1f5f9', borderWidth: 1.5, borderColor: '#e2e8f0',
  },
  voiceHoldText: { color: '#475569', fontWeight: '800', fontSize: 12 },

  // Step 2 — Summary
  sectionHeader: { flexDirection: 'row', alignItems: 'center', gap: 12 },
  sectionEmoji: { fontSize: 32 },
  sectionTitle: { color: COLORS.ink, fontSize: 18, fontWeight: '900' },
  sectionSubtitle: { color: COLORS.muted, fontSize: 13, fontWeight: '700', textAlign: 'right' },
  tipCard: { borderRadius: 18, padding: 16, gap: 8 },
  tipLabel: { color: 'rgba(255,255,255,0.8)', fontSize: 10, fontWeight: '900', letterSpacing: 1.2, textTransform: 'uppercase' },
  tipText: { color: '#fff', fontSize: 14, fontWeight: '800', lineHeight: 22 },

  // Step 3 — Quiz
  quizCard: { backgroundColor: '#fff', borderRadius: 24, padding: 18, gap: 14 },
  quizQuestion: { color: COLORS.ink, fontSize: 16, fontWeight: '900', lineHeight: 26 },
  feedbackBox: { borderRadius: 14, padding: 14, gap: 6 },
  feedbackGood: { backgroundColor: '#f0fdf4', borderWidth: 1.5, borderColor: '#86efac' },
  feedbackBad: { backgroundColor: '#fff7ed', borderWidth: 1.5, borderColor: '#fed7aa' },
  feedbackTitle: { color: COLORS.ink, fontWeight: '900', fontSize: 14 },
  feedbackBody: { color: '#475569', fontWeight: '600', fontSize: 13, lineHeight: 20 },

  // Tutor suggestion
  tutorCard: {
    backgroundColor: '#fff7ed', borderRadius: 16, padding: 14, gap: 8,
    borderWidth: 1, borderColor: '#fdba74',
  },
  tutorTitle: { color: '#9a3412', fontWeight: '900', fontSize: 14 },
  tutorBody: { color: '#7c2d12', fontSize: 13, lineHeight: 20 },
  tutorBtn: { borderRadius: 12, paddingVertical: 12, alignItems: 'center' },
  tutorBtnText: { color: '#fff', fontWeight: '900' },

  // Parent summary
  parentCard: {
    backgroundColor: '#ecfeff', borderRadius: 14, padding: 12, gap: 6,
    borderWidth: 1, borderColor: '#67e8f9',
  },
  parentTitle: { color: '#155e75', fontWeight: '900', fontSize: 12 },
  parentBody: { color: '#0f766e', lineHeight: 20, fontSize: 13 },

  // Sticky CTA
  stickyBottom: {
    position: 'absolute', bottom: 0, left: 0, right: 0,
    backgroundColor: '#fff',
    borderTopWidth: 1, borderTopColor: '#f1f5f9',
    paddingHorizontal: 16, paddingVertical: 12, paddingBottom: 24,
  },
  primaryBtn: { borderRadius: 18, paddingVertical: 16, alignItems: 'center', justifyContent: 'center' },
  primaryBtnText: { color: '#fff', fontWeight: '900', fontSize: 15, letterSpacing: 0.4 },
  ghostBtn: { borderRadius: 18, paddingVertical: 14, alignItems: 'center', backgroundColor: '#f8fafc', borderWidth: 1.5, borderColor: '#e2e8f0' },
  ghostBtnText: { fontWeight: '800', fontSize: 14 },

  // Error state
  errorCard: { margin: 20, backgroundColor: '#fff', borderRadius: 20, padding: 24, gap: 16 },
  errorTitle: { color: COLORS.ink, fontWeight: '900', fontSize: 16 },
  errorBody: { color: COLORS.muted, fontSize: 14, lineHeight: 22 },
});
