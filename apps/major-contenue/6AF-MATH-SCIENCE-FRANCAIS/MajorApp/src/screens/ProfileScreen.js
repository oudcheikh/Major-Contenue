import React, { useState, useCallback } from 'react';
import { View, Text, ScrollView, TouchableOpacity, StyleSheet, Alert } from 'react-native';
import { useFocusEffect } from '@react-navigation/native';
import { getStudent, getStats, getStreak, resetStats } from '../utils/storage';
import { computeGlobalLevel, computeSubjectLevel } from '../utils/levelDetection';
import { buildWeeklyParentSummary, computeKnowledgeLevel, getKnowledgeProfile } from '../utils/phygitalStorage';
import LevelBadge from '../components/LevelBadge';
import ProgressBar from '../components/ProgressBar';
import { COLORS, LEVELS } from '../theme';
import { SUBJECTS } from '../data/exercises';

export default function ProfileScreen({ navigation }) {
  const [student, setStudent] = useState(null);
  const [stats, setStats] = useState(null);
  const [streak, setStreak] = useState({ count: 0 });
  const [globalLevel, setGlobalLevel] = useState(null);
  const [knowledge, setKnowledge] = useState(null);
  const [knowledgeProfile, setKnowledgeProfile] = useState(null);
  const [parentSummary, setParentSummary] = useState('');

  const load = useCallback(async () => {
    const [s, st, str, kp] = await Promise.all([getStudent(), getStats(), getStreak(), getKnowledgeProfile()]);
    setStudent(s);
    setStats(st);
    setStreak(str);
    setGlobalLevel(computeGlobalLevel(st));
    setKnowledgeProfile(kp);
    setKnowledge(computeKnowledgeLevel(kp));
    if (s?.name) {
      setParentSummary(await buildWeeklyParentSummary(s.name));
    }
  }, []);

  useFocusEffect(useCallback(() => { load(); }, [load]));

  function confirmReset() {
    Alert.alert(
      'Réinitialiser ?',
      'Toute ta progression sera effacée. Cette action est irréversible.',
      [
        { text: 'Annuler', style: 'cancel' },
        {
          text: 'Réinitialiser',
          style: 'destructive',
          onPress: async () => {
            const empty = await resetStats();
            setStats(empty);
            setGlobalLevel(computeGlobalLevel(empty));
          },
        },
      ]
    );
  }

  if (!student || !stats || !globalLevel || !knowledge || !knowledgeProfile) return <View style={styles.loading}><Text>Chargement...</Text></View>;

  const totalDone = Object.values(stats).reduce((s, x) => s + x.done, 0);
  const totalCorrect = Object.values(stats).reduce((s, x) => s + x.correct, 0);

  // Badges earned
  const badges = [];
  if (totalDone >= 10) badges.push({ icon: '🌱', label: 'Premier pas', desc: '10 exercices faits' });
  if (totalDone >= 50) badges.push({ icon: '⭐', label: 'Assidu', desc: '50 exercices faits' });
  if (totalDone >= 100) badges.push({ icon: '🚀', label: 'Travailleur', desc: '100 exercices faits' });
  if (streak.count >= 3) badges.push({ icon: '🔥', label: 'En feu !', desc: `${streak.count} jours de suite` });
  if (streak.count >= 7) badges.push({ icon: '💎', label: 'Régularité', desc: '7 jours de suite' });
  if (globalLevel.pct >= 85) badges.push({ icon: '🏆', label: 'Expert', desc: '85% de réussite globale' });
  if (totalCorrect >= 30) badges.push({ icon: '🎯', label: 'Précis', desc: '30 bonnes réponses' });

  return (
    <ScrollView style={styles.scroll} contentContainerStyle={styles.container}>
      {/* Profile header */}
      <View style={styles.profileCard}>
        <View style={styles.avatar}>
          <Text style={styles.avatarText}>{student.name[0].toUpperCase()}</Text>
        </View>
        <Text style={styles.studentName}>{student.name}</Text>
        <LevelBadge level={globalLevel.level} size="lg" />

        <View style={styles.statsRow}>
          <View style={styles.statItem}>
            <Text style={styles.statNum}>{totalDone}</Text>
            <Text style={styles.statLabel}>Exercices</Text>
          </View>
          <View style={styles.statDivider} />
          <View style={styles.statItem}>
            <Text style={[styles.statNum, { color: COLORS.success }]}>{totalCorrect}</Text>
            <Text style={styles.statLabel}>Corrects</Text>
          </View>
          <View style={styles.statDivider} />
          <View style={styles.statItem}>
            <Text style={[styles.statNum, { color: COLORS.math }]}>{streak.count}🔥</Text>
            <Text style={styles.statLabel}>Jours</Text>
          </View>
        </View>
      </View>

      {/* Global progress */}
      <View style={styles.card}>
        <Text style={styles.cardTitle}>Progression globale</Text>
        <View style={{ gap: 4 }}>
          <View style={styles.globalRow}>
            <Text style={[styles.globalPct, { color: globalLevel.level.color }]}>{globalLevel.pct}%</Text>
            <View style={{ flex: 1 }}>
              <ProgressBar pct={globalLevel.pct} color={globalLevel.level.color} showPct={false} />
            </View>
          </View>
          {globalLevel.nextLevel && (
            <Text style={styles.nextLevelText}>
              {globalLevel.progressToNext}% vers {globalLevel.nextLevel.icon} {globalLevel.nextLevel.label}
            </Text>
          )}
        </View>
      </View>

      <View style={styles.card}>
        <Text style={styles.cardTitle}>Niveau de Savoir (Phygital)</Text>
        <Text style={[styles.globalPct, { color: knowledge.level.color }]}>
          {knowledge.level.icon} {knowledge.level.label} · {knowledge.pct}%
        </Text>
        <Text style={styles.subjectDone}>Credits de Savoir: {knowledgeProfile.credits}</Text>
      </View>

      {/* Par matière */}
      <View style={styles.card}>
        <Text style={styles.cardTitle}>Par matière</Text>
        {SUBJECTS.map((subject) => {
          const subLevel = computeSubjectLevel(stats[subject.id]);
          const done = stats[subject.id].done;
          const correct = stats[subject.id].correct;
          return (
            <TouchableOpacity
              key={subject.id}
              style={styles.subjectRow}
              onPress={() => navigation.navigate('Quiz', { subject })}
            >
              <Text style={styles.subjectIcon}>{subject.icon}</Text>
              <View style={{ flex: 1, gap: 4 }}>
                <View style={styles.subjectRowTop}>
                  <Text style={styles.subjectName}>{subject.label}</Text>
                  <Text style={[styles.subjectPct, { color: subject.color }]}>{subLevel.pct}%</Text>
                </View>
                <ProgressBar pct={subLevel.pct} color={subject.color} showPct={false} />
                <Text style={styles.subjectDone}>{correct}/{done} correct</Text>
              </View>
            </TouchableOpacity>
          );
        })}
      </View>

      {/* Badges */}
      <View style={styles.card}>
        <Text style={styles.cardTitle}>🏅 Badges obtenus ({badges.length})</Text>
        {badges.length === 0 ? (
          <Text style={styles.noBadge}>Fais des exercices pour débloquer des badges !</Text>
        ) : (
          <View style={styles.badgesGrid}>
            {badges.map((b) => (
              <View key={b.label} style={styles.badgeItem}>
                <Text style={styles.badgeIcon}>{b.icon}</Text>
                <Text style={styles.badgeLabel}>{b.label}</Text>
                <Text style={styles.badgeDesc}>{b.desc}</Text>
              </View>
            ))}
          </View>
        )}
      </View>

      <View style={styles.card}>
        <Text style={styles.cardTitle}>Rapport Parent (apercu WhatsApp)</Text>
        <Text style={styles.subjectDone}>{parentSummary}</Text>
      </View>

      {/* Niveaux disponibles */}
      <View style={styles.card}>
        <Text style={styles.cardTitle}>Système de niveaux</Text>
        {LEVELS.map((l) => (
          <View key={l.id} style={styles.levelRow}>
            <Text style={styles.levelIcon}>{l.icon}</Text>
            <View style={{ flex: 1 }}>
              <Text style={[styles.levelName, { color: l.color }]}>{l.label}</Text>
              <Text style={styles.levelRange}>{l.min}% – {l.max}%</Text>
            </View>
            {globalLevel.level.id === l.id && (
              <View style={[styles.currentBadge, { backgroundColor: l.color + '22', borderColor: l.color }]}>
                <Text style={[styles.currentBadgeText, { color: l.color }]}>Actuel</Text>
              </View>
            )}
          </View>
        ))}
      </View>

      <TouchableOpacity style={styles.resetBtn} onPress={confirmReset}>
        <Text style={styles.resetBtnText}>🗑 Réinitialiser la progression</Text>
      </TouchableOpacity>

      <View style={{ height: 20 }} />
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  scroll: { flex: 1, backgroundColor: COLORS.background },
  container: { padding: 18, gap: 14 },
  loading: { flex: 1, alignItems: 'center', justifyContent: 'center' },

  profileCard: {
    backgroundColor: '#fff',
    borderRadius: 22,
    padding: 22,
    alignItems: 'center',
    gap: 12,
    shadowColor: '#0f172a',
    shadowOffset: { width: 0, height: 6 },
    shadowOpacity: 0.1,
    shadowRadius: 14,
    elevation: 6,
  },
  avatar: {
    width: 80,
    height: 80,
    borderRadius: 40,
    backgroundColor: COLORS.primary,
    alignItems: 'center',
    justifyContent: 'center',
  },
  avatarText: { fontSize: 36, fontWeight: '900', color: '#fff' },
  studentName: { fontSize: 22, fontWeight: '900', color: COLORS.ink },

  statsRow: { flexDirection: 'row', width: '100%', marginTop: 6 },
  statItem: { flex: 1, alignItems: 'center', gap: 4 },
  statNum: { fontSize: 22, fontWeight: '900', color: COLORS.ink },
  statLabel: { fontSize: 11, color: COLORS.muted, fontWeight: '700' },
  statDivider: { width: 1, backgroundColor: COLORS.border, marginVertical: 4 },

  card: {
    backgroundColor: '#fff',
    borderRadius: 18,
    padding: 16,
    gap: 12,
    shadowColor: '#0f172a',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.07,
    shadowRadius: 10,
    elevation: 4,
  },
  cardTitle: { fontSize: 15, fontWeight: '900', color: COLORS.ink },

  globalRow: { flexDirection: 'row', alignItems: 'center', gap: 10 },
  globalPct: { fontSize: 24, fontWeight: '900', minWidth: 54 },
  nextLevelText: { fontSize: 11, color: COLORS.muted, fontWeight: '600', textAlign: 'right' },

  subjectRow: { flexDirection: 'row', gap: 12, alignItems: 'flex-start', paddingVertical: 4 },
  subjectIcon: { fontSize: 24, marginTop: 2 },
  subjectRowTop: { flexDirection: 'row', justifyContent: 'space-between' },
  subjectName: { fontSize: 14, fontWeight: '800', color: COLORS.ink },
  subjectPct: { fontSize: 14, fontWeight: '900' },
  subjectDone: { fontSize: 11, color: COLORS.muted, fontWeight: '600' },

  noBadge: { fontSize: 13, color: COLORS.muted, fontStyle: 'italic', textAlign: 'center', paddingVertical: 8 },
  badgesGrid: { flexDirection: 'row', flexWrap: 'wrap', gap: 10 },
  badgeItem: {
    backgroundColor: COLORS.background,
    borderRadius: 14,
    padding: 12,
    alignItems: 'center',
    width: '30%',
    gap: 4,
  },
  badgeIcon: { fontSize: 28 },
  badgeLabel: { fontSize: 11, fontWeight: '800', color: COLORS.ink, textAlign: 'center' },
  badgeDesc: { fontSize: 9, color: COLORS.muted, textAlign: 'center' },

  levelRow: { flexDirection: 'row', alignItems: 'center', gap: 12, paddingVertical: 4 },
  levelIcon: { fontSize: 20 },
  levelName: { fontSize: 13, fontWeight: '800' },
  levelRange: { fontSize: 11, color: COLORS.muted, fontWeight: '600' },
  currentBadge: {
    paddingHorizontal: 10,
    paddingVertical: 4,
    borderRadius: 999,
    borderWidth: 1.5,
  },
  currentBadgeText: { fontSize: 11, fontWeight: '800' },

  resetBtn: {
    backgroundColor: '#fff',
    borderRadius: 14,
    padding: 14,
    alignItems: 'center',
    borderWidth: 1.5,
    borderColor: '#ef444455',
  },
  resetBtnText: { color: '#ef4444', fontWeight: '800', fontSize: 14 },
});
