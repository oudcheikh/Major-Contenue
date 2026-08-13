import AsyncStorage from '@react-native-async-storage/async-storage';

const KEYS = {
  STUDENT: 'major_student',
  STATS: 'major_stats',
  STREAK: 'major_streak',
};

// ─── Student profile ────────────────────────────────────────────────────────
export async function getStudent() {
  const raw = await AsyncStorage.getItem(KEYS.STUDENT);
  return raw ? JSON.parse(raw) : null;
}

export async function saveStudent(student) {
  await AsyncStorage.setItem(KEYS.STUDENT, JSON.stringify(student));
}

// ─── Stats per subject ───────────────────────────────────────────────────────
const DEFAULT_STATS = {
  french:       { done: 0, correct: 0 },
  math:         { done: 0, correct: 0 },
  science:      { done: 0, correct: 0 },
  arabe:        { done: 0, correct: 0 },
  histoire_geo: { done: 0, correct: 0 },
  islamique:    { done: 0, correct: 0 },
};

export async function getStats() {
  const raw = await AsyncStorage.getItem(KEYS.STATS);
  if (!raw) return { ...DEFAULT_STATS };
  // Merge pour ajouter les nouvelles matières si absentes (upgrade)
  const saved = JSON.parse(raw);
  return { ...DEFAULT_STATS, ...saved };
}

export async function updateStats(subjectId, correct, total) {
  const stats = await getStats();
  if (!stats[subjectId]) stats[subjectId] = { done: 0, correct: 0 };
  stats[subjectId].done += total;
  stats[subjectId].correct += correct;
  await AsyncStorage.setItem(KEYS.STATS, JSON.stringify(stats));
  return stats;
}

export async function resetStats() {
  await AsyncStorage.setItem(KEYS.STATS, JSON.stringify({ ...DEFAULT_STATS }));
  return { ...DEFAULT_STATS };
}

// ─── Streak ──────────────────────────────────────────────────────────────────
export async function getStreak() {
  const raw = await AsyncStorage.getItem(KEYS.STREAK);
  return raw ? JSON.parse(raw) : { count: 0, lastDate: null };
}

export async function updateStreak() {
  const streak = await getStreak();
  const today = new Date().toDateString();
  if (streak.lastDate === today) return streak;
  const yesterday = new Date(Date.now() - 86400000).toDateString();
  const newCount = streak.lastDate === yesterday ? streak.count + 1 : 1;
  const updated = { count: newCount, lastDate: today };
  await AsyncStorage.setItem(KEYS.STREAK, JSON.stringify(updated));
  return updated;
}
