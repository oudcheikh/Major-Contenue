import React, { useEffect, useRef } from 'react';
import { Animated, StyleSheet, Text, View } from 'react-native';

export default function MentorScene({ subjectId, isSpeaking, isLoading }) {
  const bob = useRef(new Animated.Value(0)).current;
  const wave = useRef(new Animated.Value(0)).current;
  const glow = useRef(new Animated.Value(0.35)).current;

  useEffect(() => {
    const loopBob = Animated.loop(
      Animated.sequence([
        Animated.timing(bob, { toValue: 1, duration: 900, useNativeDriver: true }),
        Animated.timing(bob, { toValue: 0, duration: 900, useNativeDriver: true }),
      ])
    );
    const loopWave = Animated.loop(
      Animated.sequence([
        Animated.timing(wave, { toValue: 1, duration: 1200, useNativeDriver: true }),
        Animated.timing(wave, { toValue: 0, duration: 1200, useNativeDriver: true }),
      ])
    );
    const loopGlow = Animated.loop(
      Animated.sequence([
        Animated.timing(glow, { toValue: 1, duration: 700, useNativeDriver: true }),
        Animated.timing(glow, { toValue: 0.35, duration: 700, useNativeDriver: true }),
      ])
    );
    loopBob.start();
    loopWave.start();
    if (isSpeaking || isLoading) loopGlow.start();
    return () => {
      loopBob.stop();
      loopWave.stop();
      loopGlow.stop();
    };
  }, [bob, wave, glow, isSpeaking, isLoading]);

  const y = bob.interpolate({ inputRange: [0, 1], outputRange: [0, -8] });
  const x = wave.interpolate({ inputRange: [0, 1], outputRange: [-12, 12] });
  const accent = subjectId === 'math' ? '🍎' : subjectId === 'science' ? '🌱' : '📝';

  return (
    <View style={styles.wrap}>
      <Animated.View style={[styles.robotBubble, { opacity: glow }]}>
        <Text style={styles.robotBubbleText}>
          {isLoading ? 'Major prepare la scene...' : isSpeaking ? 'Major raconte en direct...' : 'Pret pour la suite ?'}
        </Text>
      </Animated.View>
      <View style={styles.row}>
        <Animated.Text style={[styles.icon, { transform: [{ translateX: x }] }]}>☁️</Animated.Text>
        <Animated.Text style={[styles.robot, { transform: [{ translateY: y }] }]}>🤖</Animated.Text>
        <Animated.Text style={[styles.icon, { transform: [{ translateX: Animated.multiply(x, -1) }] }]}>{accent}</Animated.Text>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  wrap: {
    backgroundColor: '#eef2ff',
    borderRadius: 16,
    borderWidth: 1.5,
    borderColor: '#c7d2fe',
    padding: 12,
    gap: 10,
  },
  robotBubble: {
    backgroundColor: '#ffffff',
    borderRadius: 12,
    paddingHorizontal: 10,
    paddingVertical: 8,
    borderWidth: 1,
    borderColor: '#dbeafe',
  },
  robotBubbleText: { color: '#312e81', fontSize: 12, fontWeight: '800' },
  row: { flexDirection: 'row', alignItems: 'center', justifyContent: 'space-around' },
  robot: { fontSize: 44 },
  icon: { fontSize: 28 },
});
