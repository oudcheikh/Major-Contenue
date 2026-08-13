import React, { useState, useRef, useEffect } from 'react';
import {
  View, Text, TextInput, TouchableOpacity, StyleSheet,
  KeyboardAvoidingView, Platform, ScrollView, Animated, Image,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { saveStudent, updateStreak } from '../utils/storage';

const SUBJECTS = [
  { icon: '📖', label: 'Français', ar: 'الفرنسية', color: '#38bdf8' },
  { icon: '📐', label: 'Maths',    ar: 'الرياضيات', color: '#fb923c' },
  { icon: '🔬', label: 'Sciences', ar: 'العلوم',   color: '#34d399' },
];

export default function OnboardingScreen({ navigation }) {
  const [name, setName]   = useState('');
  const [error, setError] = useState('');

  const logoScale    = useRef(new Animated.Value(0)).current;
  const titleOpacity = useRef(new Animated.Value(0)).current;
  const titleY       = useRef(new Animated.Value(30)).current;
  const formOpacity  = useRef(new Animated.Value(0)).current;
  const formY        = useRef(new Animated.Value(30)).current;
  const chipScales   = SUBJECTS.map(() => useRef(new Animated.Value(0)).current);
  const pulse        = useRef(new Animated.Value(1)).current;

  useEffect(() => {
    Animated.sequence([
      Animated.spring(logoScale, { toValue: 1, tension: 50, friction: 7, useNativeDriver: true }),
      Animated.parallel([
        Animated.timing(titleOpacity, { toValue: 1, duration: 400, useNativeDriver: true }),
        Animated.spring(titleY, { toValue: 0, tension: 70, friction: 10, useNativeDriver: true }),
      ]),
      Animated.stagger(100, chipScales.map((s) =>
        Animated.spring(s, { toValue: 1, tension: 80, friction: 8, useNativeDriver: true })
      )),
      Animated.parallel([
        Animated.timing(formOpacity, { toValue: 1, duration: 400, useNativeDriver: true }),
        Animated.spring(formY, { toValue: 0, tension: 70, friction: 10, useNativeDriver: true }),
      ]),
    ]).start();

    // Pulse bouton
    Animated.loop(
      Animated.sequence([
        Animated.timing(pulse, { toValue: 1.03, duration: 900, useNativeDriver: true }),
        Animated.timing(pulse, { toValue: 1,    duration: 900, useNativeDriver: true }),
      ])
    ).start();
  }, []);

  async function handleStart() {
    const trimmed = name.trim();
    if (!trimmed) { setError('أدخل اسمك · Entre ton prénom !'); return; }
    await saveStudent({ name: trimmed, createdAt: Date.now() });
    await updateStreak();
    navigation.replace('Main');
  }

  return (
    <LinearGradient
      colors={['#182b66', '#2563eb', '#38bdf8']}
      style={{ flex: 1 }}
      start={{ x: 0.1, y: 0 }}
      end={{ x: 0.9, y: 1 }}
    >
      {/* Décorations */}
      <View style={styles.circle1} />
      <View style={styles.circle2} />
      {/* Bande rouge mauritanienne en haut */}
      <View style={styles.flagBand} />

      <KeyboardAvoidingView style={{ flex: 1 }} behavior={Platform.OS === 'ios' ? 'padding' : undefined}>
        <ScrollView contentContainerStyle={styles.container} keyboardShouldPersistTaps="handled">

          {/* Logo */}
          <Animated.View style={[styles.logoWrap, { transform: [{ scale: logoScale }] }]}>
            <View style={styles.logoBg}>
              <Image source={require('../../Logo.png')} style={styles.logoImg} />
            </View>
            <Text style={styles.appName}>MAJOR · ماجور</Text>
            <View style={styles.flagRow}>
              <Text style={styles.flagEmoji}>🇲🇷</Text>
              <Text style={styles.flagLabel}>Mauritanie · موريتانيا</Text>
            </View>
          </Animated.View>

          {/* Titre bilingue */}
          <Animated.View style={[styles.titleWrap, { opacity: titleOpacity, transform: [{ translateY: titleY }] }]}>
            <Text style={styles.titleAr}>مرحباً بك في المسابقة ! 🏆</Text>
            <Text style={styles.titleFr}>Bienvenue dans l'aventure Major !</Text>
            <Text style={styles.sub}>Prépare le concours 6AF avec{'\n'}des exercices adaptés à ton niveau.</Text>
          </Animated.View>

          {/* Matières */}
          <View style={styles.chips}>
            {SUBJECTS.map((s, i) => (
              <Animated.View key={s.label} style={[
                styles.chip,
                { borderColor: s.color + '80', backgroundColor: s.color + '25', transform: [{ scale: chipScales[i] }] }
              ]}>
                <Text style={styles.chipIcon}>{s.icon}</Text>
                <View>
                  <Text style={[styles.chipLabel, { color: '#fff' }]}>{s.label}</Text>
                  <Text style={[styles.chipAr, { color: s.color }]}>{s.ar}</Text>
                </View>
              </Animated.View>
            ))}
          </View>

          {/* Formulaire */}
          <Animated.View style={[styles.card, { opacity: formOpacity, transform: [{ translateY: formY }] }]}>

            {/* Mascotte chameau */}
            <View style={styles.mascotRow}>
              <Text style={styles.camel}>🐪</Text>
              <View style={styles.bubble}>
                <Text style={styles.bubbleAr}>ما اسمك؟</Text>
                <Text style={styles.bubbleFr}>Comment tu t'appelles ?</Text>
              </View>
            </View>

            <TextInput
              style={[styles.input, error ? styles.inputError : null]}
              placeholder="Ton prénom / اسمك..."
              placeholderTextColor="#94a3b8"
              value={name}
              onChangeText={(t) => { setName(t); setError(''); }}
              maxLength={30}
              autoFocus
            />
            {error ? <Text style={styles.error}>{error}</Text> : null}

            <Animated.View style={{ transform: [{ scale: pulse }] }}>
              <TouchableOpacity onPress={handleStart} activeOpacity={0.85} style={styles.btn}>
                <LinearGradient colors={['#2563eb', '#38bdf8']} style={styles.btnGradient} start={{ x: 0, y: 0 }} end={{ x: 1, y: 0 }}>
                  <Text style={styles.btnText}>انطلق ! Commencer 🚀</Text>
                </LinearGradient>
              </TouchableOpacity>
            </Animated.View>

            <View style={styles.socialRow}>
              <View style={styles.socialDot} />
              <Text style={styles.joinText}>Rejoins les élèves mauritaniens qui réussissent</Text>
            </View>
          </Animated.View>

        </ScrollView>
      </KeyboardAvoidingView>
    </LinearGradient>
  );
}

const styles = StyleSheet.create({
  container: { flexGrow: 1, padding: 24, gap: 24, justifyContent: 'center', alignItems: 'center' },

  circle1: { position: 'absolute', width: 300, height: 300, borderRadius: 150, backgroundColor: 'rgba(255,255,255,0.06)', top: -80, right: -80 },
  circle2: { position: 'absolute', width: 200, height: 200, borderRadius: 100, backgroundColor: 'rgba(56,189,248,0.12)', bottom: -60, left: -60 },
  flagBand: { position: 'absolute', top: 0, left: 0, right: 0, height: 4, backgroundColor: '#CC1A1A', opacity: 0.8 },

  logoWrap: { alignItems: 'center', gap: 10 },
  logoBg: {
    width: 110, height: 110, borderRadius: 30, backgroundColor: '#fff',
    alignItems: 'center', justifyContent: 'center',
    shadowColor: '#000', shadowOffset: { width: 0, height: 14 }, shadowOpacity: 0.3, shadowRadius: 22, elevation: 14,
  },
  logoImg: { width: 90, height: 90, borderRadius: 22 },
  appName: { fontSize: 20, fontWeight: '900', color: '#fff', letterSpacing: 2 },
  flagRow: { flexDirection: 'row', alignItems: 'center', gap: 7 },
  flagEmoji: { fontSize: 20 },
  flagLabel: { fontSize: 13, color: '#fde68a', fontWeight: '700' },

  titleWrap: { alignItems: 'center', gap: 6 },
  titleAr: { fontSize: 20, fontWeight: '900', color: '#fde68a', textAlign: 'center' },
  titleFr: { fontSize: 17, fontWeight: '900', color: '#fff', textAlign: 'center' },
  sub: { fontSize: 13, color: 'rgba(255,255,255,0.8)', textAlign: 'center', lineHeight: 20 },

  chips: { flexDirection: 'row', gap: 8 },
  chip: { paddingHorizontal: 12, paddingVertical: 8, borderRadius: 16, borderWidth: 1.5, alignItems: 'center', gap: 3 },
  chipIcon: { fontSize: 20 },
  chipLabel: { fontSize: 11, fontWeight: '800' },
  chipAr: { fontSize: 10, fontWeight: '700', textAlign: 'center' },

  card: {
    backgroundColor: 'rgba(255,255,255,0.97)', borderRadius: 28,
    padding: 22, gap: 16, width: '100%',
    shadowColor: '#182b66', shadowOffset: { width: 0, height: 14 }, shadowOpacity: 0.22, shadowRadius: 24, elevation: 12,
  },
  mascotRow: { flexDirection: 'row', alignItems: 'flex-end', gap: 12 },
  camel: { fontSize: 44 },
  bubble: {
    flex: 1, backgroundColor: '#f0f4ff', borderRadius: 16,
    borderBottomLeftRadius: 4, padding: 12, gap: 3,
  },
  bubbleAr: { fontSize: 15, fontWeight: '800', color: '#2563eb', textAlign: 'right' },
  bubbleFr: { fontSize: 12, fontWeight: '600', color: '#0f172a' },

  input: {
    backgroundColor: '#f8faff', borderRadius: 16, borderWidth: 2,
    borderColor: '#dbeafe', padding: 16, fontSize: 16,
    color: '#0f172a', fontWeight: '700',
  },
  inputError: { borderColor: '#ef4444' },
  error: { color: '#ef4444', fontSize: 13, fontWeight: '700', textAlign: 'center' },

  btn: { borderRadius: 18, overflow: 'hidden' },
  btnGradient: { padding: 18, alignItems: 'center' },
  btnText: { color: '#fff', fontSize: 17, fontWeight: '900' },

  socialRow: { flexDirection: 'row', alignItems: 'center', gap: 7, justifyContent: 'center' },
  socialDot: { width: 7, height: 7, borderRadius: 4, backgroundColor: '#34d399' },
  joinText: { fontSize: 12, color: '#64748b', fontWeight: '600' },
});
