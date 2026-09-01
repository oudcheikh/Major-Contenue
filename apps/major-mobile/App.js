import { useEffect } from 'react'
import { StatusBar } from 'expo-status-bar'
import { SafeAreaProvider } from 'react-native-safe-area-context'
import { NavigationContainer, DefaultTheme } from '@react-navigation/native'
import { createNativeStackNavigator } from '@react-navigation/native-stack'

import HomeScreen from './src/screens/HomeScreen.js'
import ScannerScreen from './src/screens/ScannerScreen.js'
import SubjectScreen from './src/screens/SubjectScreen.js'
import LessonScreen from './src/screens/LessonScreen.js'
import QuizScreen from './src/screens/QuizScreen.js'
import ActivityScreen from './src/screens/ActivityScreen.js'
import LinkScreen from './src/screens/LinkScreen.js'
import ProgressScreen from './src/screens/ProgressScreen.js'
import { ensureAuth } from './src/firebase/progress.js'
import { COLORS } from './src/theme.js'

const Stack = createNativeStackNavigator()

const navTheme = {
  ...DefaultTheme,
  colors: { ...DefaultTheme.colors, background: COLORS.cream, primary: COLORS.royal },
}

const screenOptions = {
  headerStyle: { backgroundColor: COLORS.cream },
  headerShadowVisible: false,
  headerTintColor: COLORS.royal,
  headerTitleStyle: { color: COLORS.ink, fontWeight: '800', fontSize: 17 },
  headerBackTitleVisible: false,
  contentStyle: { backgroundColor: COLORS.cream },
}

export default function App() {
  // Session anonyme au démarrage (no-op si Firebase non configuré).
  useEffect(() => { ensureAuth() }, [])

  return (
    <SafeAreaProvider>
      <StatusBar style="dark" />
      <NavigationContainer theme={navTheme}>
        <Stack.Navigator screenOptions={screenOptions}>
          <Stack.Screen name="Home" component={HomeScreen} options={{ headerShown: false }} />
          <Stack.Screen name="Scanner" component={ScannerScreen} options={{ headerShown: false, presentation: 'fullScreenModal' }} />
          <Stack.Screen name="Subject" component={SubjectScreen} options={{ title: 'المادة' }} />
          <Stack.Screen name="Lesson" component={LessonScreen} options={{ title: 'الدرس' }} />
          <Stack.Screen name="Quiz" component={QuizScreen} options={{ title: 'الاختبار' }} />
          <Stack.Screen name="Activity" component={ActivityScreen} options={{ title: 'أجرّب بنفسي' }} />
          <Stack.Screen name="Link" component={LinkScreen} options={{ title: 'رمزي' }} />
          <Stack.Screen name="Progress" component={ProgressScreen} options={{ title: 'تقدّمي' }} />
        </Stack.Navigator>
      </NavigationContainer>
    </SafeAreaProvider>
  )
}
