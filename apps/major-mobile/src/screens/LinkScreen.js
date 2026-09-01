import { useState } from 'react'
import { View, Text, TextInput, StyleSheet, KeyboardAvoidingView, Platform } from 'react-native'
import { SafeAreaView } from 'react-native-safe-area-context'
import { linkByCode } from '../firebase/eleve.js'
import { COLORS, SHADOW, RADIUS } from '../theme.js'
import { ChunkyButton, MascotBubble, GAME, buzz } from '../activities/ui.js'

// L'enfant entre son code MAJ-xxxx (donné par le professeur) — pas de login.
export default function LinkScreen({ navigation }) {
  const [code, setCode] = useState('')
  const [state, setState] = useState('idle') // idle | busy | notfound | error

  async function submit() {
    if (!code.trim()) return
    setState('busy')
    try {
      const eleve = await linkByCode(code)
      if (eleve) {
        buzz(true)
        navigation.popToTop()
      } else {
        buzz(false)
        setState('notfound')
      }
    } catch {
      buzz(false)
      setState('error')
    }
  }

  return (
    <SafeAreaView style={styles.safe} edges={['bottom']}>
      <KeyboardAvoidingView behavior={Platform.OS === 'ios' ? 'padding' : undefined} style={{ flex: 1 }}>
        <View style={styles.wrap}>
          <MascotBubble text={'أهلًا! أعطاك أستاذك رمزًا مثل MAJ-0001؟\nاكتبه هنا لأتعرّف عليك وأتابع تقدّمك! 🤝'} />

          <View style={styles.card}>
            <Text style={styles.label}>رمزي هو :</Text>
            <TextInput
              style={styles.input}
              value={code}
              onChangeText={(t) => { setCode(t); if (state !== 'idle') setState('idle') }}
              placeholder="MAJ-0000"
              placeholderTextColor="#c3c8d4"
              autoCapitalize="characters"
              autoCorrect={false}
              maxLength={10}
            />
            {state === 'notfound' && (
              <Text style={styles.err}>لم أجد هذا الرمز 🤔 تأكد منه مع أستاذك.</Text>
            )}
            {state === 'error' && (
              <Text style={styles.err}>تعذّر الاتصال. تأكد من الإنترنت وحاول مجددًا.</Text>
            )}
            <ChunkyButton
              label={state === 'busy' ? '... أبحث عنك' : 'هذا رمزي! ✅'}
              color={GAME.green}
              disabled={!code.trim() || state === 'busy'}
              onPress={submit}
            />
          </View>

          <Text style={styles.note}>
            ليس عندك رمز؟ لا مشكلة — يمكنك استعمال التطبيق بدونه، ويبقى تقدّمك على هذا الهاتف فقط.
          </Text>
        </View>
      </KeyboardAvoidingView>
    </SafeAreaView>
  )
}

const styles = StyleSheet.create({
  safe: { flex: 1, backgroundColor: COLORS.cream },
  wrap: { flex: 1, padding: 20, justifyContent: 'center' },
  card: { backgroundColor: COLORS.card, borderRadius: RADIUS.lg, padding: 18, marginTop: 6, ...SHADOW },
  label: { fontSize: 14, fontWeight: '800', color: COLORS.inkSoft, textAlign: 'right', writingDirection: 'rtl', marginBottom: 8 },
  input: {
    borderWidth: 2, borderColor: COLORS.border, borderRadius: 14, padding: 14,
    fontSize: 24, fontWeight: '900', textAlign: 'center', letterSpacing: 2, color: COLORS.royal,
    backgroundColor: '#fafbfe',
  },
  err: { color: GAME.red, fontSize: 14, fontWeight: '700', textAlign: 'right', writingDirection: 'rtl', marginTop: 10, lineHeight: 23 },
  note: { fontSize: 13, color: COLORS.inkSoft, textAlign: 'center', writingDirection: 'rtl', marginTop: 16, lineHeight: 22 },
})
