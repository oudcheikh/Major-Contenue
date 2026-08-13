# Content Pack 6AF Arabe — Major Web

Pack de contenu **arabe** (RTL) pour la webapp **major-web**, correspondant au *Cahier de Mathématiques et Sciences 6AF* en arabe. Il ajoute deux nouvelles matières à la webapp : **Mathématiques 6AF (arabe)** et **Sciences naturelles 6AF (arabe)**.

---

## 1. Contenu du pack

Le pack contient **37 fiches de cours + 185 QCM** répartis en 3 fichiers JS :

| Fichier | Matière | Fiches | QCM | IDs des fiches |
|---|---|---|---|---|
| `math6-lessons-1.js` | Mathématiques 6AF | ~16 | ~80 | `math6-u01` … `math6-u16` |
| `math6-lessons-2.js` | Mathématiques 6AF | ~15 | ~75 | `math6-u17` … `math6-u31` |
| `sci6-lessons.js` | Sciences naturelles 6AF | **6** | **30** | `sci6-u1` … `sci6-u6` |

> **Note :** `math6-lessons-1.js` et `math6-lessons-2.js` sont produits en parallèle par d'autres agents. La répartition exacte des 31 unités math entre les deux fichiers peut varier ; ce qui compte est que l'ensemble couvre `math6-u01` … `math6-u31` (31 fiches + 155 QCM), et que chaque fichier exporte ses tableaux de `lessons` et d'`exercises` (voir les exports réels en tête de chaque fichier).

### Détail des 6 fiches Sciences (`sci6-lessons.js`)

| ID | Titre (ar) | Emoji | Difficulté | QCM |
|---|---|---|---|---|
| `sci6-u1` | التوازن الغذائي | 🍽️ | 1 | `sci6-u1-q1` … `-q5` |
| `sci6-u2` | التوازن الطاقوي | ⚡ | 2 | `sci6-u2-q1` … `-q5` |
| `sci6-u3` | التصحر | 🏜️ | 2 | `sci6-u3-q1` … `-q5` |
| `sci6-u4` | التلوث | 🏭 | 2 | `sci6-u4-q1` … `-q5` |
| `sci6-u5` | الماء والصحة | 💧 | 1 | `sci6-u5-q1` … `-q5` |
| `sci6-u6` | التطعيم | 💉 | 2 | `sci6-u6-q1` … `-q5` |

**Progression des QCM** dans chaque unité : `q1`–`q2` difficulté **1**, `q3`–`q4` difficulté **2**, `q5` difficulté **3** (problème chiffré / raisonnement). Les positions de la bonne réponse (`answer`) varient d'une question à l'autre. Les QCM sont **nouveaux** (non copiés du cahier imprimé), scientifiquement corrects et ancrés dans des contextes mauritaniens (زحف الرمال، نهر السنغال، مركز صحي روصو، نواكشوط…).

Le fichier `sci6-lessons.js` exporte :

```js
export const SCI6_LESSONS   // 6 fiches de cours
export const SCI6_EXERCISES // 30 QCM
```

Chaque fiche a la forme : `id, title, qrCode, emoji, difficulty, duration, isArabic: true, summary, keyPoints[], rule, tip, encouragement, quizIds[]`.
Chaque QCM a la forme : `id, question, options[4], answer (index), explanation, difficulty`.

---

## 2. Intégration dans `major-web/src/data.js`

Fichier cible : `/home/pcmahmoud/Documents/Perso/Cahier-Math/Major-Web/major-web/src/data.js`

### Étape 1 — Copier les fichiers du pack

Copier les 3 fichiers `.js` du pack dans un dossier accessible par `data.js`, par exemple `major-web/src/content-6af/` :

```bash
mkdir -p /home/pcmahmoud/Documents/Perso/Cahier-Math/Major-Web/major-web/src/content-6af
cp math6-lessons-1.js math6-lessons-2.js sci6-lessons.js \
   /home/pcmahmoud/Documents/Perso/Cahier-Math/Major-Web/major-web/src/content-6af/
```

### Étape 2 — Importer les 3 fichiers en tête de `data.js`

```js
import { MATH6_LESSONS_1, MATH6_EXERCISES_1 } from './content-6af/math6-lessons-1.js';
import { MATH6_LESSONS_2, MATH6_EXERCISES_2 } from './content-6af/math6-lessons-2.js';
import { SCI6_LESSONS,   SCI6_EXERCISES }    from './content-6af/sci6-lessons.js';
```

> Vérifier les **noms exacts** des exports dans `math6-lessons-1.js` / `math6-lessons-2.js` (produits par d'autres agents) et ajuster l'`import` en conséquence. Les exports de Sciences sont bien `SCI6_LESSONS` et `SCI6_EXERCISES`.

### Étape 3 — Ajouter deux nouveaux `subjects` dans `COURSES.subjects`

Dans `export const COURSES = { … "subjects": [ … ] }`, ajouter à la fin du tableau `subjects` :

```js
// ── Mathématiques 6AF (arabe) ──
{
  id: 'math6-ar',
  label: 'Mathématiques 6AF',
  labelAr: 'الرياضيات',
  color: '#fb923c',
  gradient: ['#f59e0b', '#fb923c'],
  icon: '📐',
  isArabic: true,
  lessons: [...MATH6_LESSONS_1, ...MATH6_LESSONS_2],
},
// ── Sciences naturelles 6AF (arabe) ──
{
  id: 'sci6-ar',
  label: 'Sciences naturelles',
  labelAr: 'العلوم الطبيعية',
  color: '#34d399',
  gradient: ['#10b981', '#34d399'],
  icon: '🔬',
  isArabic: true,
  lessons: SCI6_LESSONS,
},
```

### Étape 4 — Fusionner les `EXERCISES`

Dans `export const EXERCISES = { … }`, ajouter deux clés correspondant aux `id` des nouveaux subjects :

```js
export const EXERCISES = {
  math: [ /* … existant … */ ],
  // … autres matières existantes …

  // nouvelles matières 6AF arabes :
  'math6-ar': [...MATH6_EXERCISES_1, ...MATH6_EXERCISES_2],
  'sci6-ar':  SCI6_EXERCISES,
};
```

> **Important :** la logique du QCM associe chaque `quizId` d'une fiche à un exercice. Vérifier comment la webapp résout un `quizId` en exercice (recherche globale sur toutes les matières, ou par matière via `subject.id`). Si la résolution se fait **par matière**, veiller à ce que `EXERCISES['sci6-ar']` et `EXERCISES['math6-ar']` soient bien les clés lues pour ces subjects. Les IDs de QCM (`sci6-u1-q1`, `math6-u01-…`) sont **uniques** et sans collision avec l'existant, donc une recherche globale fonctionne aussi.

Vérifier également que le bas de `data.js` (les objets qui exposent `exercises: EXERCISES.xxx` par matière, vers la ligne 2129+) référence bien les nouvelles clés si ce mécanisme est utilisé pour l'affichage.

---

## 3. Déploiement AVANT impression — point critique

Les **QR codes du cahier imprimé** pointent vers l'URL de production :

- Fiche de cours : `https://major-eval.vercel.app/#/lesson/{id}`
- Correction / QCM : `https://major-eval.vercel.app/#/correction/{id}`

où `{id}` vaut `math6-u01` … `math6-u31` et `sci6-u1` … `sci6-u6`.

**Conséquences :**

1. Il faut **DÉPLOYER la webapp major-web avec ce contenu AVANT d'imprimer le cahier.** Sinon les QR pointeront vers des pages vides / 404.
2. Vérifier que la route **`/correction/{id}`** gère bien ces **nouveaux ids** :
   - qu'elle sait retrouver la fiche `sci6-u3` (et ses `quizIds`) et afficher ses QCM/corrections ;
   - qu'elle ne suppose pas un préfixe d'id d'une ancienne matière.
3. Vérifier le rendu **RTL / arabe** (`isArabic: true`) sur les pages `/lesson/{id}` et `/correction/{id}` pour les nouvelles matières.

---

## 4. Test local et URLs à vérifier

Lancer le serveur de dev dans `major-web` :

```bash
cd /home/pcmahmoud/Documents/Perso/Cahier-Math/Major-Web/major-web
npm install   # si nécessaire
npm run dev
```

Puis ouvrir dans le navigateur (le port réel est affiché par Vite, souvent `5173`) :

```
# Fiches de cours Sciences
http://localhost:5173/#/lesson/sci6-u1     # التوازن الغذائي
http://localhost:5173/#/lesson/sci6-u3     # التصحر
http://localhost:5173/#/lesson/sci6-u6     # التطعيم

# Corrections / QCM Sciences
http://localhost:5173/#/correction/sci6-u1
http://localhost:5173/#/correction/sci6-u5

# Fiches / corrections Mathématiques
http://localhost:5173/#/lesson/math6-u01
http://localhost:5173/#/correction/math6-u31
```

**Points à contrôler :**

- Les deux nouvelles matières (`الرياضيات` orange, `العلوم الطبيعية` vert) apparaissent dans la liste des matières.
- Chaque fiche affiche `summary`, `keyPoints`, `rule`, `tip`, `encouragement` en arabe RTL.
- Chaque page de correction affiche les 5 QCM de l'unité avec la bonne réponse et l'explication.
- Aucune erreur console (`quizId` introuvable, exercice manquant…).

Une fois le test local validé, **déployer sur Vercel** (`https://major-eval.vercel.app`) puis **retester les mêmes URLs en production** avant de lancer l'impression du cahier.
