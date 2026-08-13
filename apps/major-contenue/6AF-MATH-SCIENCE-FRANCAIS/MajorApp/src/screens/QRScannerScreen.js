import React, { useState, useEffect } from 'react';
import {
  View, Text, StyleSheet, TouchableOpacity, Animated, Vibration,
} from 'react-native';
import { CameraView, useCameraPermissions } from 'expo-camera';
import { SafeAreaView } from 'react-native-safe-area-context';
import coursesData from '../data/courses.json';

const ALL_LESSONS = coursesData.subjects.flatMap((s) =>
  s.lessons.map((l) => ({ ...l, subjectId: s.id, subjectLabel: s.label, subjectColor: s.color, subjectGradient: s.gradient }))
);

export default function QRScannerScreen({ navigation }) {
  const [permission, requestPermission] = useCameraPermissions();
  const [scanned, setScanned] = useState(false);
  const [scanError, setScanError] = useState(null);
  const scanLine = new Animated.Value(0);

  useEffect(() => {
    Animated.loop(
      Animated.sequence([
        Animated.timing(scanLine, { toValue: 1, duration: 1800, useNativeDriver: true }),
        Animated.timing(scanLine, { toValue: 0, duration: 1800, useNativeDriver: true }),
      ])
    ).start();
  }, []);

  function handleBarCodeScanned({ data }) {
    if (scanned) return;
    setScanned(true);
    Vibration.vibrate(120);

    if (!data.startsWith('major://lesson/')) {
      setScanError('Ce QR code ne vient pas du cahier Major.');
      setTimeout(() => { setScanned(false); setScanError(null); }, 2500);
      return;
    }

    const lessonId = data.replace('major://lesson/', '');
    const lesson = ALL_LESSONS.find((l) => l.id === lessonId);

    if (!lesson) {
      setScanError('Leçon introuvable. Mets l\'app à jour.');
      setTimeout(() => { setScanned(false); setScanError(null); }, 2500);
      return;
    }

    setTimeout(() => {
      navigation.replace('Lesson', { lesson });
    }, 250);
  }

  if (!permission) return <View style={styles.center}><Text>Chargement...</Text></View>;

  if (!permission.granted) {
    return (
      <SafeAreaView style={styles.permissionScreen}>
        <Text style={styles.permEmoji}>📷</Text>
        <Text style={styles.permTitle}>Accès à la caméra</Text>
        <Text style={styles.permText}>
          Pour scanner les QR codes du cahier Major, l'app a besoin d'accéder à ta caméra.
        </Text>
        <TouchableOpacity style={styles.permBtn} onPress={requestPermission}>
          <Text style={styles.permBtnText}>Autoriser la caméra</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.backLink} onPress={() => navigation.goBack()}>
          <Text style={styles.backLinkText}>Retour</Text>
        </TouchableOpacity>
      </SafeAreaView>
    );
  }

  const scanLineY = scanLine.interpolate({ inputRange: [0, 1], outputRange: [0, 220] });

  return (
    <View style={styles.container}>
      <CameraView
        style={StyleSheet.absoluteFill}
        barcodeScannerSettings={{ barcodeTypes: ['qr'] }}
        onBarcodeScanned={scanned ? undefined : handleBarCodeScanned}
      />

      {/* Overlay sombre autour du cadre */}
      <View style={styles.overlay}>
        <View style={styles.overlayTop} />
        <View style={styles.overlayMiddle}>
          <View style={styles.overlaySide} />
          <View style={styles.scanFrame}>
            {/* Coins */}
            <View style={[styles.corner, styles.cornerTL]} />
            <View style={[styles.corner, styles.cornerTR]} />
            <View style={[styles.corner, styles.cornerBL]} />
            <View style={[styles.corner, styles.cornerBR]} />
            {/* Ligne de scan animée */}
            {!scanned && (
              <Animated.View style={[styles.scanLineAnim, { transform: [{ translateY: scanLineY }] }]} />
            )}
          </View>
          <View style={styles.overlaySide} />
        </View>
        <View style={styles.overlayBottom}>
          {scanError ? (
            <View style={styles.errorBubble}>
              <Text style={styles.errorText}>⚠️ {scanError}</Text>
            </View>
          ) : (
            <Text style={styles.hint}>
              {scanned ? '✅ QR detecte ! Chargement du mini-cours...' : '📖 Pointe la camera vers un QR code du cahier'}
            </Text>
          )}
          <TouchableOpacity style={styles.closeBtn} onPress={() => navigation.goBack()}>
            <Text style={styles.closeBtnText}>✕ Fermer</Text>
          </TouchableOpacity>
        </View>
      </View>
    </View>
  );
}

const FRAME = 240;

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#000' },
  center: { flex: 1, alignItems: 'center', justifyContent: 'center' },

  permissionScreen: {
    flex: 1,
    backgroundColor: '#055C2B',
    alignItems: 'center',
    justifyContent: 'center',
    padding: 32,
    gap: 16,
  },
  permEmoji: { fontSize: 64 },
  permTitle: { fontSize: 24, fontWeight: '900', color: '#fff', textAlign: 'center' },
  permText: { fontSize: 15, color: 'rgba(255,255,255,0.8)', textAlign: 'center', lineHeight: 24 },
  permBtn: {
    backgroundColor: '#06803C',
    paddingHorizontal: 32,
    paddingVertical: 16,
    borderRadius: 999,
    marginTop: 8,
  },
  permBtnText: { color: '#fff', fontWeight: '900', fontSize: 16 },
  backLink: { marginTop: 8 },
  backLinkText: { color: 'rgba(255,255,255,0.5)', fontSize: 14, fontWeight: '700' },

  overlay: { flex: 1 },
  overlayTop: { flex: 1, backgroundColor: 'rgba(0,0,0,0.62)' },
  overlayMiddle: { flexDirection: 'row', height: FRAME },
  overlaySide: { flex: 1, backgroundColor: 'rgba(0,0,0,0.62)' },
  overlayBottom: {
    flex: 1,
    backgroundColor: 'rgba(0,0,0,0.62)',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 20,
  },

  scanFrame: {
    width: FRAME,
    height: FRAME,
    overflow: 'hidden',
  },
  corner: {
    position: 'absolute',
    width: 28,
    height: 28,
    borderColor: '#38bdf8',
    borderWidth: 3.5,
  },
  cornerTL: { top: 0, left: 0, borderRightWidth: 0, borderBottomWidth: 0, borderTopLeftRadius: 6 },
  cornerTR: { top: 0, right: 0, borderLeftWidth: 0, borderBottomWidth: 0, borderTopRightRadius: 6 },
  cornerBL: { bottom: 0, left: 0, borderRightWidth: 0, borderTopWidth: 0, borderBottomLeftRadius: 6 },
  cornerBR: { bottom: 0, right: 0, borderLeftWidth: 0, borderTopWidth: 0, borderBottomRightRadius: 6 },

  scanLineAnim: {
    position: 'absolute',
    left: 0,
    right: 0,
    height: 2.5,
    backgroundColor: '#38bdf8',
    shadowColor: '#38bdf8',
    shadowOffset: { width: 0, height: 0 },
    shadowOpacity: 0.9,
    shadowRadius: 6,
  },

  hint: { color: '#fff', fontSize: 14, fontWeight: '700', textAlign: 'center', paddingHorizontal: 32 },
  errorBubble: {
    backgroundColor: '#fee2e2',
    paddingHorizontal: 20,
    paddingVertical: 10,
    borderRadius: 999,
  },
  errorText: { color: '#dc2626', fontWeight: '800', fontSize: 13 },
  closeBtn: {
    backgroundColor: 'rgba(255,255,255,0.15)',
    paddingHorizontal: 28,
    paddingVertical: 12,
    borderRadius: 999,
    borderWidth: 1,
    borderColor: 'rgba(255,255,255,0.25)',
  },
  closeBtnText: { color: '#fff', fontWeight: '800', fontSize: 14 },
});
