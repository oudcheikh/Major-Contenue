import AsyncStorage from '@react-native-async-storage/async-storage';
import { EXERCISES } from '../data/exercises';

const KEY = 'major_daily_challenge_v2';

function generateChallenge() {
  const pick = (arr, n) => [...arr].sort(() => Math.random() - 0.5).slice(0, n);
  return [
    ...pick(EXERCISES.french,  2).map((q) => ({ ...q, subjectId: 'french',  subjectIcon: '📖', subjectColor: '#1D8BE0' })),
    ...pick(EXERCISES.math,    2).map((q) => ({ ...q, subjectId: 'math',    subjectIcon: '📐', subjectColor: '#F07020' })),
    ...pick(EXERCISES.science, 2).map((q) => ({ ...q, subjectId: 'science', subjectIcon: '🔬', subjectColor: '#1AAF72' })),
  ].sort(() => Math.random() - 0.5);
}

export async function getDailyChallenge() {
  const today = new Date().toDateString();
  const raw = await AsyncStorage.getItem(KEY);
  if (raw) {
    const saved = JSON.parse(raw);
    if (saved.date === today) return saved;
  }
  const challenge = {
    date: today,
    questions: generateChallenge(),
    completed: false,
    score: null,
    answeredCount: 0,
  };
  await AsyncStorage.setItem(KEY, JSON.stringify(challenge));
  return challenge;
}

export async function completeDailyChallenge(score, total) {
  const raw = await AsyncStorage.getItem(KEY);
  if (!raw) return;
  const ch = JSON.parse(raw);
  ch.completed = true;
  ch.score = score;
  ch.answeredCount = total;
  await AsyncStorage.setItem(KEY, JSON.stringify(ch));
}

export function getActiveStudentsCount() {
  const d = new Date();
  const seed = d.getDate() * 13 + d.getMonth() * 7;
  return 240 + (seed % 150);
}

// Messages bilingues français/arabe selon contexte
export function getMascotMessage(studentName, streak, challengeDone) {
  const hour = new Date().getHours();
  const name = studentName?.split(' ')[0] || '';

  if (challengeDone) return {
    arabic: '!أحسنت، أنت بطل',
    french: `Défi du jour terminé, ${name} ! ⭐`,
    text: `أحسنت ! Bravo ${name} ! Défi complété ! ⭐`,
  };
  if (streak >= 7) return {
    arabic: `!${streak} أيام متواصلة، ماشاءالله`,
    french: `${streak} jours de suite ! Tu es exceptionnel !`,
    text: `ماشاءالله ! ${streak} jours de suite 🔥`,
  };
  if (streak >= 3) return {
    arabic: '!واصل، أنت في الطريق الصحيح',
    french: `${streak} jours consécutifs, continue !`,
    text: `واصل ! ${streak} jours de suite 🔥`,
  };
  if (hour < 12) return {
    arabic: '!صباح الخير، حان وقت المراجعة',
    french: 'Bonjour ! Parfait moment pour réviser.',
    text: 'صباح الخير ! Bonjour ! 🌅',
  };
  if (hour < 18) return {
    arabic: '!تحديك اليومي بانتظارك',
    french: `${name}, ton défi t'attend !`,
    text: 'تحديك اليومي بانتظارك 💪',
  };
  return {
    arabic: '!مساء الخير، مراجعة أخيرة؟',
    french: 'Bonne soirée ! Une dernière révision ?',
    text: 'مساء الخير ! Bonne soirée 🌙',
  };
}
