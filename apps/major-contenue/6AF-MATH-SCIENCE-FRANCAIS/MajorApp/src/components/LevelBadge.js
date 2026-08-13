import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

export default function LevelBadge({ level, size = 'md' }) {
  if (!level) return null;

  const isLg = size === 'lg';

  return (
    <View style={[styles.badge, { backgroundColor: level.color + '22', borderColor: level.color + '55' }, isLg && styles.badgeLg]}>
      <Text style={isLg ? styles.iconLg : styles.icon}>{level.icon}</Text>
      <Text style={[styles.label, { color: level.color }, isLg && styles.labelLg]}>{level.label}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  badge: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 5,
    paddingHorizontal: 10,
    paddingVertical: 4,
    borderRadius: 999,
    borderWidth: 1.5,
  },
  badgeLg: {
    paddingHorizontal: 16,
    paddingVertical: 8,
  },
  icon: { fontSize: 14 },
  iconLg: { fontSize: 20 },
  label: { fontSize: 12, fontWeight: '800' },
  labelLg: { fontSize: 16 },
});
