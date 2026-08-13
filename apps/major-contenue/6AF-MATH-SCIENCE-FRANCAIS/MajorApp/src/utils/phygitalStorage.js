import AsyncStorage from '@react-native-async-storage/async-storage';
import { getStats } from './storage';

const KEYS = {
  PROFILE: 'major_phygital_profile_v1',
  CHAPTERS: 'major_phygital_chapters_v1',
};

const DEFAULT_PROFILE = {
  credits: 0,
  scans: 0,
  microWins: 0,
  microFails: 0,
  weeklyMinutes: 0,
  preferredLanguage: 'fr',
};

export const KNOWLEDGE_LEVELS = [
  { id: 'apprenti', label: 'Apprenti', min: 0, max: 39, color: '#64748b', icon: 'L1' },
  { id: 'avance', label: 'Avance', min: 40, max: 69, color: '#2563eb', icon: 'L2' },
  { id: 'ingenieur', label: 'Ingenieur', min: 70, max: 89, color: '#fb923c', icon: 'ING' },
  { id: 'genie', label: 'Genie', min: 90, max: 100, color: '#f59e0b', icon: 'GEN' },
];

function computeKnowledgePct(profile) {
  const totalActions = Math.max(1, profile.scans + profile.microWins + profile.microFails);
  const successRate = ((profile.microWins + profile.scans * 0.4) / totalActions) * 100;
  return Math.max(0, Math.min(100, Math.round(successRate)));
}

export async function getKnowledgeProfile() {
  const raw = await AsyncStorage.getItem(KEYS.PROFILE);
  const base = raw ? JSON.parse(raw) : DEFAULT_PROFILE;
  return { ...DEFAULT_PROFILE, ...base };
}

async function saveKnowledgeProfile(profile) {
  await AsyncStorage.setItem(KEYS.PROFILE, JSON.stringify(profile));
  return profile;
}

export async function setPreferredLanguage(lang) {
  const profile = await getKnowledgeProfile();
  profile.preferredLanguage = lang;
  return saveKnowledgeProfile(profile);
}

export async function awardScanPoints() {
  const profile = await getKnowledgeProfile();
  profile.credits += 3;
  profile.scans += 1;
  profile.weeklyMinutes += 2;
  await saveKnowledgeProfile(profile);
  return profile;
}

export async function awardMicroWin(lessonId) {
  const profile = await getKnowledgeProfile();
  profile.credits += 10;
  profile.microWins += 1;
  profile.weeklyMinutes += 4;
  await saveKnowledgeProfile(profile);

  const chapterMap = await getChapterProgressMap();
  const current = chapterMap[lessonId] || { scans: 0, attempts: 0, successes: 0, fails: 0, consecutiveFails: 0 };
  chapterMap[lessonId] = {
    ...current,
    attempts: current.attempts + 1,
    successes: current.successes + 1,
    consecutiveFails: 0,
  };
  await saveChapterProgressMap(chapterMap);

  return profile;
}

export async function recordMicroFail(lessonId) {
  const profile = await getKnowledgeProfile();
  profile.microFails += 1;
  profile.weeklyMinutes += 2;
  await saveKnowledgeProfile(profile);

  const chapterMap = await getChapterProgressMap();
  const current = chapterMap[lessonId] || { scans: 0, attempts: 0, successes: 0, fails: 0, consecutiveFails: 0 };
  chapterMap[lessonId] = {
    ...current,
    attempts: current.attempts + 1,
    fails: current.fails + 1,
    consecutiveFails: current.consecutiveFails + 1,
  };
  await saveChapterProgressMap(chapterMap);

  return { profile, chapter: chapterMap[lessonId] };
}

async function getChapterProgressMap() {
  const raw = await AsyncStorage.getItem(KEYS.CHAPTERS);
  return raw ? JSON.parse(raw) : {};
}

async function saveChapterProgressMap(map) {
  await AsyncStorage.setItem(KEYS.CHAPTERS, JSON.stringify(map));
}

export async function recordChapterScan(lessonId) {
  const chapterMap = await getChapterProgressMap();
  const current = chapterMap[lessonId] || { scans: 0, attempts: 0, successes: 0, fails: 0, consecutiveFails: 0 };
  chapterMap[lessonId] = { ...current, scans: current.scans + 1 };
  await saveChapterProgressMap(chapterMap);
  return chapterMap[lessonId];
}

export async function getChapterInsight(lessonId) {
  const map = await getChapterProgressMap();
  return map[lessonId] || { scans: 0, attempts: 0, successes: 0, fails: 0, consecutiveFails: 0 };
}

export function computeKnowledgeLevel(profile) {
  const pct = computeKnowledgePct(profile);
  const level = KNOWLEDGE_LEVELS.find((l) => pct >= l.min && pct <= l.max) || KNOWLEDGE_LEVELS[0];
  const levelIdx = KNOWLEDGE_LEVELS.indexOf(level);
  const nextLevel = levelIdx < KNOWLEDGE_LEVELS.length - 1 ? KNOWLEDGE_LEVELS[levelIdx + 1] : null;
  return { pct, level, nextLevel };
}

export function shouldSuggestTutor(chapterInsight) {
  return chapterInsight.consecutiveFails >= 5;
}

export async function buildWeeklyParentSummary(studentName) {
  const profile = await getKnowledgeProfile();
  const stats = await getStats();
  const labels = { french: 'Francais', math: 'Maths', science: 'Sciences' };

  const ranked = Object.entries(stats)
    .map(([k, v]) => ({
      key: k,
      pct: v.done > 0 ? Math.round((v.correct / v.done) * 100) : 0,
    }))
    .sort((a, b) => b.pct - a.pct);

  const best = ranked[0];
  const weak = ranked[ranked.length - 1];

  return `${studentName} a revise environ ${profile.weeklyMinutes} min cette semaine. Point fort: ${labels[best.key]} (${best.pct}%). A renforcer: ${labels[weak.key]} (${weak.pct}%).`;
}
