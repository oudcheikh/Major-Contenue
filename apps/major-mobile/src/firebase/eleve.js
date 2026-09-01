// Liaison de l'appareil à un élève via son code MAJ-xxxx (pas de login).
// L'élève est créé par l'admin (vitrine major-admin) ; l'enfant tape juste
// son code une fois, et sa progression remonte sous son nom.

import AsyncStorage from '@react-native-async-storage/async-storage'
import { isFirebaseConfigured, db } from './config.js'

const ELEVE_KEY = 'major_eleve_v1'

export async function getEleve() {
  try {
    const raw = await AsyncStorage.getItem(ELEVE_KEY)
    return raw ? JSON.parse(raw) : null
  } catch {
    return null
  }
}

// Cherche le code dans Firestore et lie l'appareil. Retourne l'élève ou null.
export async function linkByCode(code) {
  if (!isFirebaseConfigured || !db) return null
  const cleaned = code.trim().toUpperCase().replace(/\s+/g, '')
  const withPrefix = cleaned.startsWith('MAJ-') ? cleaned : `MAJ-${cleaned}`
  const { collection, query, where, limit, getDocs } = await import('firebase/firestore')
  const snap = await getDocs(query(collection(db, 'eleves'), where('code', '==', withPrefix), limit(1)))
  if (snap.empty) return null
  const d = snap.docs[0]
  const eleve = { id: d.id, ...d.data() }
  await AsyncStorage.setItem(ELEVE_KEY, JSON.stringify(eleve))
  return eleve
}

export async function unlink() {
  await AsyncStorage.removeItem(ELEVE_KEY)
}

// Défis actifs du prof de l'élève (filtre date côté client).
export async function getDefis(eleve) {
  if (!isFirebaseConfigured || !db || !eleve?.profId) return []
  try {
    const { collection, query, where, getDocs } = await import('firebase/firestore')
    const snap = await getDocs(query(collection(db, 'defis'), where('profId', '==', eleve.profId)))
    const now = new Date().toISOString()
    return snap.docs
      .map((d) => ({ id: d.id, ...d.data() }))
      .filter((x) => (!x.classe || x.classe === eleve.classe) && (!x.finLe || x.finLe >= now))
      .sort((a, b) => (b.createdAt || '').localeCompare(a.createdAt || ''))
  } catch {
    return []
  }
}
