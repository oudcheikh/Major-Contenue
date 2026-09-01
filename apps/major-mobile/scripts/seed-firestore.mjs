// Modèle de données Major dans Firestore : ecoles / profs / eleves / parents.
// Crée les collections avec une école de démonstration complète.
// Usage :  node scripts/seed-firestore.mjs

import { initializeApp } from 'firebase/app'
import { getFirestore, doc, setDoc, getDocs, collection } from 'firebase/firestore'

const firebaseConfig = {
  apiKey: 'AIzaSyCFoHQPvKVJr7df1Bq6nC4qgcN7eZnOt9s',
  authDomain: 'ncars-80f44.firebaseapp.com',
  projectId: 'ncars-80f44',
  storageBucket: 'ncars-80f44.appspot.com',
  messagingSenderId: '16467823009',
  appId: '1:16467823009:web:122ddb013f5c2bf55d63e0',
}

const app = initializeApp(firebaseConfig)
const db = getFirestore(app)

const now = new Date().toISOString()

// Code élève court et lisible — c'est lui qui remplace le login.
function codeEleve(n) {
  return `MAJ-${String(n).padStart(4, '0')}`
}

const ECOLE = {
  id: 'ecole-demo',
  nom: 'مدرسة النجاح الخاصة',
  ville: 'انواكشوط',
  quartier: 'تفرغ زينة',
  telephone: '+222 00 00 00 00',
  directeur: 'المدير التجريبي',
  actif: true,
  createdAt: now,
}

const PROF = {
  id: 'prof-demo',
  nom: 'الأستاذ التجريبي',
  telephone: '+222 11 11 11 11',
  ecoleId: 'ecole-demo',
  classes: ['6AF-A'],
  actif: true,
  createdAt: now,
}

const PARENT = {
  id: 'parent-demo',
  nom: 'وليّ الأمر التجريبي',
  telephone: '+222 22 22 22 22',
  enfants: ['eleve-demo-1', 'eleve-demo-2'],
  createdAt: now,
}

const ELEVES = [
  {
    id: 'eleve-demo-1',
    prenom: 'أحمد',
    nom: 'التجريبي',
    genre: 'ذكر',
    classe: '6AF-A',
    ecoleId: 'ecole-demo',
    profId: 'prof-demo',
    parentId: 'parent-demo',
    code: codeEleve(1),
    actif: true,
    createdAt: now,
  },
  {
    id: 'eleve-demo-2',
    prenom: 'فاطمة',
    nom: 'التجريبية',
    genre: 'أنثى',
    classe: '6AF-A',
    ecoleId: 'ecole-demo',
    profId: 'prof-demo',
    parentId: 'parent-demo',
    code: codeEleve(2),
    actif: true,
    createdAt: now,
  },
]

async function main() {
  console.log('→ Création du modèle dans', firebaseConfig.projectId)

  await setDoc(doc(db, 'ecoles', ECOLE.id), ECOLE)
  console.log('  ✓ ecoles/' + ECOLE.id)

  await setDoc(doc(db, 'profs', PROF.id), PROF)
  console.log('  ✓ profs/' + PROF.id)

  await setDoc(doc(db, 'parents', PARENT.id), PARENT)
  console.log('  ✓ parents/' + PARENT.id)

  for (const e of ELEVES) {
    await setDoc(doc(db, 'eleves', e.id), e)
    console.log(`  ✓ eleves/${e.id} (code: ${e.code})`)
  }

  // Un résultat de quiz d'exemple pour voir le lien élève → progression.
  await setDoc(doc(db, 'progress', 'eleve-demo-1', 'lessons', 'math6-u01'), {
    lessonId: 'math6-u01',
    subjectId: 'math6-ar',
    bestScore: 4,
    lastScore: 4,
    total: 5,
    bestPct: 80,
    attempts: 1,
    updatedAt: now,
  })
  console.log('  ✓ progress/eleve-demo-1/lessons/math6-u01')

  // Relecture de contrôle.
  const snap = await getDocs(collection(db, 'eleves'))
  console.log(`\n→ Vérification : ${snap.size} élève(s) dans la base.`)
  snap.forEach((d) => console.log('   -', d.data().code, d.data().prenom, d.data().nom))
  process.exit(0)
}

main().catch((e) => {
  console.error('✗ Échec :', e.message)
  process.exit(1)
})
