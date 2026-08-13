import React, { useRef, useEffect } from 'react';
import { View, Text, StyleSheet, Animated } from 'react-native';

export default function Mascot({ message, compact = false }) {
  const bounce = useRef(new Animated.Value(0)).current;
  const scale = useRef(new Animated.Value(0.85)).current;

  useEffect(() => {
    Animated.spring(scale, { toValue: 1, tension: 60, friction: 7, useNativeDriver: true }).start();
    Animated.loop(
      Animated.sequence([
        Animated.timing(bounce, { toValue: -5, duration: 800, useNativeDriver: true }),
        Animated.timing(bounce, { toValue: 0, duration: 800, useNativeDriver: true }),
      ])
    ).start();
  }, []);

  if (compact) {
    return (
      <View style={styles.compactRow}>
        <Animated.Text style={[styles.camelCompact, { transform: [{ translateY: bounce }] }]}>🐪</Animated.Text>
        <Text style={styles.compactText} numberOfLines={2}>{message?.text}</Text>
      </View>
    );
  }

  return (
    <Animated.View style={[styles.wrap, { transform: [{ scale }] }]}>
      <Animated.Text style={[styles.camel, { transform: [{ translateY: bounce }] }]}>🐪</Animated.Text>
      <View style={styles.bubble}>
        <View style={styles.tail} />
        <Text style={styles.arabicText}>{message?.arabic}</Text>
        <Text style={styles.frenchText}>{message?.french}</Text>
      </View>
    </Animated.View>
  );
}

const styles = StyleSheet.create({
  wrap: { flexDirection: 'row', alignItems: 'flex-end', gap: 8, paddingHorizontal: 16 },
  camel: { fontSize: 50 },
  bubble: {
    flex: 1, backgroundColor: '#fff', borderRadius: 18,
    borderBottomLeftRadius: 4, padding: 12,
    shadowColor: '#000', shadowOffset: { width: 0, height: 3 },
    shadowOpacity: 0.07, shadowRadius: 8, elevation: 3,
    gap: 2, position: 'relative',
  },
  tail: {
    position: 'absolute', bottom: 0, left: -7,
    width: 0, height: 0,
    borderTopWidth: 10, borderRightWidth: 8,
    borderBottomWidth: 0, borderLeftWidth: 0,
    borderTopColor: '#fff', borderRightColor: 'transparent',
  },
  arabicText: { fontSize: 14, fontWeight: '800', color: '#06803C', textAlign: 'right' },
  frenchText: { fontSize: 13, fontWeight: '600', color: '#1A1A2E' },

  compactRow: { flexDirection: 'row', alignItems: 'center', gap: 8 },
  camelCompact: { fontSize: 28 },
  compactText: { fontSize: 13, fontWeight: '700', color: 'rgba(255,255,255,0.92)', flex: 1, lineHeight: 18 },
});
