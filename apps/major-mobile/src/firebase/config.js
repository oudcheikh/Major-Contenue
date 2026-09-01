// ─────────────────────────────────────────────────────────────────────────────
// Configuration Firebase.
//
// 1. Crée un projet sur https://console.firebase.google.com
// 2. Ajoute une app « Web » (l'icône </>) — le SDK JS marche en Expo managé.
// 3. Active Authentication → méthode « Anonyme ».
// 4. Active Firestore Database (mode production, règles ci-dessous).
// 5. Copie les valeurs de firebaseConfig ici (ou dans app.json → extra,
//    puis lis-les via expo-constants si tu préfères ne pas commiter les clés).
//
// Règles Firestore recommandées (chaque élève ne lit/écrit que sa progression) :
//   rules_version = '2';
//   service cloud.firestore {
//     match /databases/{db}/documents {
//       match /progress/{uid}/{document=**} {
//         allow read, write: if request.auth != null && request.auth.uid == uid;
//       }
//     }
//   }
// ─────────────────────────────────────────────────────────────────────────────

import { initializeApp } from 'firebase/app'
import { getFirestore } from 'firebase/firestore'
import { initializeAuth, getReactNativePersistence } from 'firebase/auth'
import AsyncStorage from '@react-native-async-storage/async-storage'

export const firebaseConfig = {
  apiKey: 'AIzaSyCFoHQPvKVJr7df1Bq6nC4qgcN7eZnOt9s',
  authDomain: 'ncars-80f44.firebaseapp.com',
  projectId: 'ncars-80f44',
  storageBucket: 'ncars-80f44.appspot.com',
  messagingSenderId: '16467823009',
  appId: '1:16467823009:web:122ddb013f5c2bf55d63e0',
}

export const isFirebaseConfigured = firebaseConfig.apiKey !== 'REMPLACER'

let app = null
let db = null
let auth = null

if (isFirebaseConfigured) {
  app = initializeApp(firebaseConfig)
  db = getFirestore(app)
  // Persistance de la session entre les lancements de l'app.
  // getReactNativePersistence n'existe pas dans le build web → auth facultative.
  try {
    auth = initializeAuth(app, {
      persistence: getReactNativePersistence(AsyncStorage),
    })
  } catch {
    auth = null
  }
}

export { app, db, auth }
