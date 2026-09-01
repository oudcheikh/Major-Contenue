// ─────────────────────────────────────────────────────────────────────────────
// Service de progression — offline-first.
//
// Source de vérité locale : AsyncStorage (l'app marche 100% hors-ligne et
// même sans Firebase configuré). Quand Firebase EST configuré et l'élève
// authentifié (anonyme), chaque résultat est aussi poussé dans Firestore
// pour sauvegarde / synchro multi-appareils.
// ─────────────────────────────────────────────────────────────────────────────

import AsyncStorage from '@react-native-async-storage/async-storage'
import { isFirebaseConfigured, auth, db } from './config.js'
import { getEleve } from './eleve.js'

const LOCAL_KEY = 'major_progress_v1'

let authReadyPromise = null

// Assure une session anonyme. No-op (résout null) si Firebase non configuré.
export function ensureAuth() {
  if (!isFirebaseConfigured || !auth) return Promise.resolve(null)
  if (authReadyPromise) return authReadyPromise
  authReadyPromise = (async () => {
    const { onAuthStateChanged, signInAnonymously } = await import('firebase/auth')
    return new Promise((resolve) => {
      const unsub = onAuthStateChanged(auth, (user) => {
        if (user) {
          unsub()
          resolve(user)
        }
      })
      signInAnonymously(auth).catch((e) => {
        console.warn('Auth anonyme échouée, mode local seul:', e?.message)
        unsub()
        resolve(null)
      })
    })
  })()
  return authReadyPromise
}

async function readLocal() {
  try {
    const raw = await AsyncStorage.getItem(LOCAL_KEY)
    return raw ? JSON.parse(raw) : {}
  } catch {
    return {}
  }
}

async function writeLocal(map) {
  try {
    await AsyncStorage.setItem(LOCAL_KEY, JSON.stringify(map))
  } catch (e) {
    console.warn('Écriture locale échouée:', e?.message)
  }
}

// Enregistre le résultat d'un quiz de leçon. Garde le MEILLEUR score par leçon
// mais incrémente le nombre de tentatives.
export async function recordQuiz({ lessonId, subjectId, score, total }) {
  const pct = total > 0 ? Math.round((score / total) * 100) : 0
  const map = await readLocal()
  const prev = map[lessonId]
  const entry = {
    lessonId,
    subjectId,
    bestScore: prev ? Math.max(prev.bestScore, score) : score,
    lastScore: score,
    total,
    bestPct: prev ? Math.max(prev.bestPct, pct) : pct,
    attempts: (prev?.attempts || 0) + 1,
    updatedAt: new Date().toISOString(),
  }
  map[lessonId] = entry
  await writeLocal(map)

  // Miroir Firestore sous l'id de l'ÉLÈVE lié par code MAJ-xxxx
  // (best-effort, n'interrompt jamais l'UX ; sans code → local seul).
  if (isFirebaseConfigured && db) {
    try {
      const eleve = await getEleve()
      if (eleve) {
        const { doc, setDoc } = await import('firebase/firestore')
        await setDoc(doc(db, 'progress', eleve.id, 'lessons', lessonId), entry, { merge: true })
      }
    } catch (e) {
      console.warn('Synchro Firestore échouée (gardé en local):', e?.message)
    }
  }
  return entry
}

// Toute la progression : { lessonId: entry }. Local d'abord ; si Firestore
// dispo et local vide (nouvel appareil), on rapatrie le distant.
export async function getProgress() {
  let local = await readLocal()
  if (Object.keys(local).length === 0 && isFirebaseConfigured && db) {
    try {
      const eleve = await getEleve()
      if (eleve) {
        const { collection, getDocs } = await import('firebase/firestore')
        const snap = await getDocs(collection(db, 'progress', eleve.id, 'lessons'))
        const remote = {}
        snap.forEach((d) => { remote[d.id] = d.data() })
        if (Object.keys(remote).length) {
          await writeLocal(remote)
          local = remote
        }
      }
    } catch (e) {
      console.warn('Lecture Firestore échouée:', e?.message)
    }
  }
  return local
}

export async function getLessonProgress(lessonId) {
  const map = await readLocal()
  return map[lessonId] || null
}
