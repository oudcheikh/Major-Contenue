import React, { useEffect, useRef } from 'react';
import { View, Text, StyleSheet, Animated, Image } from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { getStudent } from '../utils/storage';

export default function SplashScreen({ navigation }) {
  const logoScale    = useRef(new Animated.Value(0)).current;
  const logoOpacity  = useRef(new Animated.Value(0)).current;
  const textOpacity  = useRef(new Animated.Value(0)).current;
  const textY        = useRef(new Animated.Value(20)).current;
  const camelY       = useRef(new Animated.Value(0)).current;
  const shimmer      = useRef(new Animated.Value(0)).current;

  useEffect(() => {
    // Entrée logo
    Animated.parallel([
      Animated.spring(logoScale, { toValue: 1, tension: 50, friction: 7, useNativeDriver: true }),
      Animated.timing(logoOpacity, { toValue: 1, duration: 500, useNativeDriver: true }),
    ]).start(() => {
      // Texte glisse
      Animated.parallel([
        Animated.timing(textOpacity, { toValue: 1, duration: 400, useNativeDriver: true }),
        Animated.spring(textY, { toValue: 0, tension: 70, friction: 10, useNativeDriver: true }),
      ]).start();

      // Chameau bounce infini
      Animated.loop(
        Animated.sequence([
          Animated.timing(camelY, { toValue: -10, duration: 700, useNativeDriver: true }),
          Animated.timing(camelY, { toValue: 0,   duration: 700, useNativeDriver: true }),
        ])
      ).start();

      // Shimmer sur le nom
      Animated.loop(
        Animated.sequence([
          Animated.timing(shimmer, { toValue: 1, duration: 1200, useNativeDriver: true }),
          Animated.timing(shimmer, { toValue: 0, duration: 1200, useNativeDriver: true }),
        ])
      ).start();
    });

    const timer = setTimeout(async () => {
      const student = await getStudent();
      navigation.replace(student ? 'Main' : 'Onboarding');
    }, 2600);

    return () => clearTimeout(timer);
  }, []);

  const shimmerOpacity = shimmer.interpolate({ inputRange: [0, 1], outputRange: [0.7, 1] });

  return (
    <LinearGradient
      colors={['#182b66', '#2563eb', '#38bdf8']}
      style={styles.container}
      start={{ x: 0.1, y: 0 }}
      end={{ x: 0.9, y: 1 }}
    >
      {/* Cercles déco */}
      <View style={styles.circle1} />
      <View style={styles.circle2} />
      <View style={styles.circle3} />

      {/* Logo */}
      <Animated.View style={[styles.logoWrap, { opacity: logoOpacity, transform: [{ scale: logoScale }] }]}>
        <View style={styles.logoBg}>
          <Image source={require('../../Logo.png')} style={styles.logoImg} />
        </View>
      </Animated.View>

      {/* Texte + chameau */}
      <Animated.View style={[styles.textBlock, { opacity: textOpacity, transform: [{ translateY: textY }] }]}>
        <Animated.Text style={[styles.appName, { opacity: shimmerOpacity }]}>MAJOR</Animated.Text>
        <Text style={styles.appNameAr}>ماجور</Text>

        <View style={styles.flagRow}>
          <Text style={styles.flag}>🇲🇷</Text>
          <Text style={styles.country}>Mauritanie · موريتانيا</Text>
        </View>

        <Animated.Text style={[styles.camel, { transform: [{ translateY: camelY }] }]}>🐪</Animated.Text>

        <View style={styles.chips}>
          {[
            { icon: '📖', label: 'Français' },
            { icon: '📐', label: 'Maths' },
            { icon: '🔬', label: 'Sciences' },
          ].map((s) => (
            <View key={s.label} style={styles.chip}>
              <Text>{s.icon}</Text>
              <Text style={styles.chipLabel}>{s.label}</Text>
            </View>
          ))}
        </View>

        <Text style={styles.tagline}>Prépare ton concours 6AF 🏆</Text>
        <Text style={styles.taglineAr}>استعد لامتحان السادسة ابتدائي</Text>
      </Animated.View>

      {/* Barre de chargement animée */}
      <View style={styles.loaderTrack}>
        <Animated.View style={[styles.loaderFill, {
          width: shimmer.interpolate({ inputRange: [0, 1], outputRange: ['30%', '90%'] })
        }]} />
      </View>
    </LinearGradient>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, alignItems: 'center', justifyContent: 'center', gap: 20, overflow: 'hidden' },

  circle1: { position: 'absolute', width: 340, height: 340, borderRadius: 170, backgroundColor: 'rgba(255,255,255,0.06)', top: -100, right: -100 },
  circle2: { position: 'absolute', width: 220, height: 220, borderRadius: 110, backgroundColor: 'rgba(255,255,255,0.05)', bottom: -60, left: -60 },
  circle3: { position: 'absolute', width: 120, height: 120, borderRadius: 60,  backgroundColor: 'rgba(56,189,248,0.15)', top: '40%', left: -20 },

  logoWrap: { alignItems: 'center' },
  logoBg: {
    width: 110, height: 110, borderRadius: 30, backgroundColor: '#fff',
    alignItems: 'center', justifyContent: 'center',
    shadowColor: '#000', shadowOffset: { width: 0, height: 16 },
    shadowOpacity: 0.35, shadowRadius: 24, elevation: 16,
  },
  logoImg: { width: 90, height: 90, borderRadius: 22 },

  textBlock: { alignItems: 'center', gap: 8 },

  appName: { fontSize: 40, fontWeight: '900', color: '#fff', letterSpacing: 8 },
  appNameAr: { fontSize: 22, fontWeight: '800', color: '#fde68a', letterSpacing: 2, marginTop: -4 },

  flagRow: { flexDirection: 'row', alignItems: 'center', gap: 8, marginTop: 4 },
  flag: { fontSize: 22 },
  country: { fontSize: 13, color: 'rgba(255,255,255,0.85)', fontWeight: '700' },

  camel: { fontSize: 58, marginVertical: 4 },

  chips: { flexDirection: 'row', gap: 10 },
  chip: {
    flexDirection: 'row', alignItems: 'center', gap: 6,
    backgroundColor: 'rgba(255,255,255,0.14)',
    paddingHorizontal: 14, paddingVertical: 8,
    borderRadius: 999, borderWidth: 1, borderColor: 'rgba(255,255,255,0.22)',
  },
  chipLabel: { fontSize: 12, fontWeight: '800', color: '#fff' },

  tagline: { fontSize: 14, color: 'rgba(255,255,255,0.9)', fontWeight: '700', marginTop: 4 },
  taglineAr: { fontSize: 13, color: '#fde68a', fontWeight: '700' },

  loaderTrack: {
    position: 'absolute', bottom: 50, left: 40, right: 40,
    height: 3, borderRadius: 999, backgroundColor: 'rgba(255,255,255,0.18)',
    overflow: 'hidden',
  },
  loaderFill: { height: '100%', borderRadius: 999, backgroundColor: '#fde68a' },
});
