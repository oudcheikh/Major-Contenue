import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

export default function ProgressBar({ pct = 0, color = '#2563eb', label, showPct = true }) {
  return (
    <View style={styles.wrap}>
      {label && (
        <View style={styles.row}>
          <Text style={styles.label}>{label}</Text>
          {showPct && <Text style={[styles.pct, { color }]}>{pct}%</Text>}
        </View>
      )}
      <View style={styles.track}>
        <View style={[styles.fill, { width: `${Math.min(100, pct)}%`, backgroundColor: color }]} />
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  wrap: { width: '100%' },
  row: { flexDirection: 'row', justifyContent: 'space-between', marginBottom: 5 },
  label: { fontSize: 12, fontWeight: '700', color: '#64748b' },
  pct: { fontSize: 12, fontWeight: '900' },
  track: {
    height: 8,
    borderRadius: 999,
    backgroundColor: '#e2e8f0',
    overflow: 'hidden',
  },
  fill: {
    height: '100%',
    borderRadius: 999,
  },
});
