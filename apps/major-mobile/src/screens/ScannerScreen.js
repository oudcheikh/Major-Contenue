import { useState, useEffect } from 'react'
import { View, Text, TouchableOpacity, StyleSheet, ActivityIndicator } from 'react-native'
import { SafeAreaView } from 'react-native-safe-area-context'
import { CameraView, useCameraPermissions } from 'expo-camera'
import { parseQr, getLessonById } from '../lib/lessons.js'
import { COLORS } from '../theme.js'

export default function ScannerScreen({ navigation }) {
  const [permission, requestPermission] = useCameraPermissions()
  const [scanned, setScanned] = useState(false)
  const [error, setError] = useState('')

  // Sortie fiable du modal plein écran : goBack si possible, sinon l'accueil.
  function exit() {
    if (navigation.canGoBack()) navigation.goBack()
    else navigation.navigate('Home')
  }

  useEffect(() => {
    if (permission && !permission.granted && permission.canAskAgain) {
      requestPermission()
    }
  }, [permission])

  function onScan({ data }) {
    if (scanned) return
    setScanned(true)
    const target = parseQr(data)
    const lesson = target && getLessonById(target.lessonId)
    if (lesson) {
      // replace : après la leçon, « retour » ramène à l'accueil, pas au scanner.
      // QR leçon → écran Leçon ; QR correction (pages تمارين) → directement le Quiz.
      navigation.replace(target.mode === 'quiz' ? 'Quiz' : 'Lesson', { lessonId: target.lessonId })
    } else {
      setError('لم أتعرّف على هذا الرمز. أمسح رمز QR الموجود في صفحة دفتر ماجور.')
      setTimeout(() => { setScanned(false); setError('') }, 2200)
    }
  }

  // ✕ toujours présent, sur fond clair comme sur la caméra.
  const closeBtn = (dark) => (
    <TouchableOpacity
      onPress={exit}
      style={[styles.close, !dark && styles.closeLight]}
      hitSlop={{ top: 12, bottom: 12, left: 12, right: 12 }}
    >
      <Text style={[styles.closeText, !dark && { color: COLORS.ink }]}>✕</Text>
    </TouchableOpacity>
  )

  if (!permission) {
    return (
      <SafeAreaView style={styles.center}>
        <View style={styles.cornerClose}>{closeBtn(false)}</View>
        <ActivityIndicator color={COLORS.royal} />
      </SafeAreaView>
    )
  }

  if (!permission.granted) {
    return (
      <SafeAreaView style={styles.center}>
        <View style={styles.cornerClose}>{closeBtn(false)}</View>
        <Text style={styles.msgIcon}>📷</Text>
        <Text style={styles.msgTitle}>نحتاج إلى الكاميرا</Text>
        <Text style={styles.msgBody}>
          يستعمل ماجور الكاميرا ليقرأ رمز QR في صفحات الدفتر.
        </Text>
        <TouchableOpacity style={styles.btn} onPress={requestPermission}>
          <Text style={styles.btnText}>أسمح بالكاميرا</Text>
        </TouchableOpacity>
        <TouchableOpacity onPress={exit} style={styles.backLink}>
          <Text style={styles.backLinkText}>الرجوع →</Text>
        </TouchableOpacity>
      </SafeAreaView>
    )
  }

  return (
    <View style={styles.flex}>
      <CameraView
        style={StyleSheet.absoluteFill}
        facing="back"
        barcodeScannerSettings={{ barcodeTypes: ['qr'] }}
        onBarcodeScanned={scanned ? undefined : onScan}
      />
      <SafeAreaView style={styles.overlay} edges={['top', 'bottom']}>
        <View style={styles.topBar}>
          {closeBtn(true)}
          <Text style={styles.topTitle}>أمسح الدفتر</Text>
          <View style={{ width: 40 }} />
        </View>

        <View style={styles.frameWrap}>
          <View style={styles.frame} />
          <Text style={styles.hint}>ضَعْ رمز QR داخل المربّع</Text>
        </View>

        {!!error && (
          <View style={styles.errorBox}>
            <Text style={styles.errorText}>{error}</Text>
          </View>
        )}
      </SafeAreaView>
    </View>
  )
}

const styles = StyleSheet.create({
  flex: { flex: 1, backgroundColor: '#000' },
  center: { flex: 1, backgroundColor: COLORS.cream, alignItems: 'center', justifyContent: 'center', padding: 30 },
  overlay: { flex: 1, justifyContent: 'space-between' },
  topBar: { flexDirection: 'row-reverse', alignItems: 'center', justifyContent: 'space-between', paddingHorizontal: 16, paddingTop: 8 },
  close: { width: 40, height: 40, borderRadius: 20, backgroundColor: 'rgba(0,0,0,0.45)', alignItems: 'center', justifyContent: 'center', zIndex: 10 },
  closeLight: { backgroundColor: '#e9ecf2' },
  closeText: { color: '#fff', fontSize: 20 },
  cornerClose: { position: 'absolute', top: 14, right: 16, zIndex: 10 },
  backLink: { marginTop: 16, padding: 10 },
  backLinkText: { fontSize: 15, fontWeight: '700', color: COLORS.royal, writingDirection: 'rtl' },
  topTitle: { color: '#fff', fontSize: 17, fontWeight: '700', writingDirection: 'rtl' },
  frameWrap: { alignItems: 'center', gap: 18 },
  frame: { width: 240, height: 240, borderRadius: 28, borderWidth: 3, borderColor: '#fff', backgroundColor: 'rgba(255,255,255,0.06)' },
  hint: { color: '#fff', fontSize: 15, fontWeight: '600', writingDirection: 'rtl', textShadowColor: 'rgba(0,0,0,0.6)', textShadowRadius: 4 },
  errorBox: { margin: 20, backgroundColor: COLORS.bad, borderRadius: 14, padding: 14 },
  errorText: { color: '#fff', fontSize: 14, textAlign: 'center', fontWeight: '600', writingDirection: 'rtl' },
  msgIcon: { fontSize: 48, marginBottom: 12 },
  msgTitle: { fontSize: 20, fontWeight: '800', color: COLORS.ink, marginBottom: 8, writingDirection: 'rtl' },
  msgBody: { fontSize: 15, color: COLORS.inkSoft, textAlign: 'center', marginBottom: 22, lineHeight: 24, writingDirection: 'rtl' },
  btn: { backgroundColor: COLORS.royal, borderRadius: 14, paddingVertical: 14, paddingHorizontal: 28 },
  btnText: { color: '#fff', fontSize: 16, fontWeight: '700', writingDirection: 'rtl' },
})
