import React from 'react';
import { StatusBar } from 'expo-status-bar';
import { NavigationContainer, useNavigation } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { View, Text, TouchableOpacity, StyleSheet } from 'react-native';
import { SafeAreaProvider } from 'react-native-safe-area-context';

import SplashScreen from './src/screens/SplashScreen';
import OnboardingScreen from './src/screens/OnboardingScreen';
import HomeScreen from './src/screens/HomeScreen';
import QuizScreen from './src/screens/QuizScreen';
import ResultScreen from './src/screens/ResultScreen';
import ProfileScreen from './src/screens/ProfileScreen';
import QRScannerScreen from './src/screens/QRScannerScreen';
import LessonScreen from './src/screens/LessonScreen';
import { COLORS } from './src/theme';

const Stack = createNativeStackNavigator();
const Tab = createBottomTabNavigator();

// Placeholder vide pour l'onglet scanner (jamais affiché)
function EmptyScreen() { return <View style={{ flex: 1, backgroundColor: COLORS.background }} />; }

// Bouton scanner flottant — ouvre toujours le stack QRScanner (avec back)
function ScannerTabButton() {
  const navigation = useNavigation();
  return (
    <TouchableOpacity
      style={tabStyles.scanBtn}
      onPress={() => navigation.navigate('QRScanner')}
      activeOpacity={0.88}
    >
      <View style={tabStyles.scanBtnInner}>
        <Text style={tabStyles.scanBtnIcon}>📷</Text>
      </View>
    </TouchableOpacity>
  );
}

function MainTabs() {
  return (
    <Tab.Navigator
      screenOptions={{
        headerShown: false,
        tabBarStyle: tabStyles.bar,
        tabBarLabelStyle: tabStyles.label,
        tabBarActiveTintColor: '#2563eb',
        tabBarInactiveTintColor: '#94a3b8',
      }}
    >
      <Tab.Screen
        name="Home"
        component={HomeScreen}
        options={{
          title: 'Accueil',
          tabBarIcon: ({ focused }) => (
            <Text style={{ fontSize: focused ? 24 : 20, opacity: focused ? 1 : 0.5 }}>🏠</Text>
          ),
        }}
      />
      <Tab.Screen
        name="ScannerTab"
        component={EmptyScreen}
        options={{
          title: '',
          tabBarButton: () => <ScannerTabButton />,
        }}
      />
      <Tab.Screen
        name="Profile"
        component={ProfileScreen}
        options={{
          title: 'Profil',
          tabBarIcon: ({ focused }) => (
            <Text style={{ fontSize: focused ? 24 : 20, opacity: focused ? 1 : 0.5 }}>👤</Text>
          ),
        }}
      />
    </Tab.Navigator>
  );
}

const tabStyles = StyleSheet.create({
  bar: {
    backgroundColor: '#fff',
    borderTopColor: 'rgba(37,99,235,0.08)',
    borderTopWidth: 1,
    height: 72,
    paddingBottom: 10,
    paddingTop: 6,
  },
  label: { fontSize: 11, fontWeight: '800' },
  scanBtn: {
    top: -22,
    justifyContent: 'center',
    alignItems: 'center',
    width: 68,
    height: 68,
  },
  scanBtnInner: {
    width: 62,
    height: 62,
    borderRadius: 31,
    backgroundColor: '#2563eb',
    alignItems: 'center',
    justifyContent: 'center',
    shadowColor: '#182b66',
    shadowOffset: { width: 0, height: 8 },
    shadowOpacity: 0.45,
    shadowRadius: 14,
    elevation: 12,
    borderWidth: 3,
    borderColor: '#fff',
  },
  scanBtnIcon: { fontSize: 26 },
});

export default function App() {
  return (
    <SafeAreaProvider>
      <NavigationContainer>
        <StatusBar style="light" />
        <Stack.Navigator screenOptions={{ headerShown: false }} initialRouteName="Splash">
          <Stack.Screen name="Splash" component={SplashScreen} />
          <Stack.Screen name="Onboarding" component={OnboardingScreen} />
          <Stack.Screen name="Main" component={MainTabs} />
          <Stack.Screen name="Quiz" component={QuizScreen} options={{ animation: 'slide_from_bottom' }} />
          <Stack.Screen name="Result" component={ResultScreen} options={{ animation: 'fade', gestureEnabled: false }} />
          <Stack.Screen name="QRScanner" component={QRScannerScreen} options={{ animation: 'slide_from_bottom' }} />
          <Stack.Screen name="Lesson" component={LessonScreen} options={{ animation: 'slide_from_bottom' }} />
        </Stack.Navigator>
      </NavigationContainer>
    </SafeAreaProvider>
  );
}
