import React, { useEffect, useMemo, useRef, useState } from 'react';
import { Animated, PanResponder, StyleSheet, Text, TouchableOpacity, View, Vibration } from 'react-native';

function Floating({ children, delay = 0, distance = 8, duration = 1300 }) {
  const y = useRef(new Animated.Value(0)).current;
  useEffect(() => {
    const anim = Animated.loop(
      Animated.sequence([
        Animated.timing(y, { toValue: -distance, duration, delay, useNativeDriver: true }),
        Animated.timing(y, { toValue: 0, duration, useNativeDriver: true }),
      ])
    );
    anim.start();
    return () => anim.stop();
  }, [delay, distance, duration, y]);
  return <Animated.View style={{ transform: [{ translateY: y }] }}>{children}</Animated.View>;
}

function useDraggableToken(onDrop) {
  const pan = useRef(new Animated.ValueXY({ x: 0, y: 0 })).current;
  const responder = useMemo(
    () =>
      PanResponder.create({
        onStartShouldSetPanResponder: () => true,
        onMoveShouldSetPanResponder: () => true,
        onPanResponderMove: Animated.event([null, { dx: pan.x, dy: pan.y }], { useNativeDriver: false }),
        onPanResponderRelease: (_, gesture) => {
          onDrop(gesture.dx, gesture.dy);
          Animated.spring(pan, { toValue: { x: 0, y: 0 }, useNativeDriver: false }).start();
        },
      }),
    [onDrop, pan]
  );
  return { pan, responder };
}

function DraggableToken({ emoji, onDrop }) {
  const { pan, responder } = useDraggableToken(onDrop);
  return (
    <Animated.View
      {...responder.panHandlers}
      style={[styles.token, { transform: [{ translateX: pan.x }, { translateY: pan.y }] }]}
    >
      <Text style={styles.tokenEmoji}>{emoji}</Text>
    </Animated.View>
  );
}

function InteractiveMath({ color }) {
  const [left, setLeft] = useState(0);
  const [right, setRight] = useState(0);
  const fruits = ['🍎', '🍊', '🍌'];

  function onDrop(dx) {
    if (dx < -40) setLeft((v) => v + 1);
    if (dx > 40) setRight((v) => v + 1);
    if (Math.abs(dx) > 40) Vibration.vibrate(18);
  }

  return (
    <View style={styles.box}>
      <View style={styles.headerRow}>
        <Text style={styles.headEmoji}>➗</Text>
        <Text style={styles.headTiny}>Glisse</Text>
      </View>
      <View style={styles.dragRow}>
        {fruits.map((f, i) => (
          <Floating key={f + i} delay={i * 120}>
            <DraggableToken emoji={f} onDrop={onDrop} />
          </Floating>
        ))}
      </View>
      <View style={styles.dropRow}>
        <View style={[styles.dropZone, { borderColor: color }]}>
          <Text style={styles.dropIcon}>🚣</Text>
          <Text style={styles.dropCount}>{left}</Text>
        </View>
        <View style={[styles.dropZone, { borderColor: color }]}>
          <Text style={styles.dropIcon}>🚣</Text>
          <Text style={styles.dropCount}>{right}</Text>
        </View>
      </View>
      <TouchableOpacity style={styles.resetBtn} onPress={() => { setLeft(0); setRight(0); }}>
        <Text style={styles.resetText}>↺</Text>
      </TouchableOpacity>
    </View>
  );
}

function InteractiveFrench({ color }) {
  const [score, setScore] = useState(0);
  const words = [
    { label: 'Manger', target: 'V' },
    { label: 'Table', target: 'N' },
    { label: 'Grand', target: 'A' },
  ];
  const zones = ['N', 'V', 'A'];

  function tryDrop(word, dx) {
    const selected = dx < -40 ? zones[0] : dx > 40 ? zones[2] : zones[1];
    if (selected === word.target) {
      setScore((v) => v + 1);
      Vibration.vibrate(16);
    }
  }

  return (
    <View style={styles.box}>
      <View style={styles.headerRow}>
        <Text style={styles.headEmoji}>📝</Text>
        <Text style={styles.headTiny}>Classe</Text>
      </View>
      <View style={styles.dragRow}>
        {words.map((w, i) => (
          <Floating key={w.label} delay={i * 120}>
            <DraggableToken emoji={w.label} onDrop={(dx) => tryDrop(w, dx)} />
          </Floating>
        ))}
      </View>
      <View style={styles.legendRow}>
        {zones.map((z) => (
          <View key={z} style={[styles.legendChip, { borderColor: color }]}>
            <Text style={[styles.legendText, { color }]}>{z}</Text>
          </View>
        ))}
      </View>
      <Text style={[styles.scoreText, { color }]}>⭐ {score}</Text>
    </View>
  );
}

function InteractiveScience({ color }) {
  const [cycle, setCycle] = useState(0);
  const steps = ['☀️', '💧', '🌱'];
  const pulse = useRef(new Animated.Value(1)).current;

  useEffect(() => {
    const anim = Animated.loop(
      Animated.sequence([
        Animated.timing(pulse, { toValue: 1.08, duration: 500, useNativeDriver: true }),
        Animated.timing(pulse, { toValue: 1, duration: 500, useNativeDriver: true }),
      ])
    );
    anim.start();
    return () => anim.stop();
  }, [pulse]);

  return (
    <View style={styles.box}>
      <View style={styles.headerRow}>
        <Text style={styles.headEmoji}>🔬</Text>
        <Text style={styles.headTiny}>Cycle</Text>
      </View>
      <TouchableOpacity
        style={[styles.cycleCard, { borderColor: color }]}
        onPress={() => {
          setCycle((v) => (v + 1) % steps.length);
          Vibration.vibrate(14);
        }}
      >
        <Animated.Text style={[styles.cycleEmoji, { transform: [{ scale: pulse }] }]}>
          {steps[cycle]}
        </Animated.Text>
      </TouchableOpacity>
    </View>
  );
}

export default function CourseVisualizer({ subjectId, color }) {
  if (subjectId === 'math') return <InteractiveMath color={color} />;
  if (subjectId === 'science') return <InteractiveScience color={color} />;
  return <InteractiveFrench color={color} />;
}

const styles = StyleSheet.create({
  box: {
    backgroundColor: '#ffffff',
    borderRadius: 18,
    borderWidth: 1.5,
    borderColor: '#dbeafe',
    padding: 12,
    gap: 10,
  },
  headerRow: { flexDirection: 'row', alignItems: 'center', justifyContent: 'space-between' },
  headEmoji: { fontSize: 22 },
  headTiny: { color: '#64748b', fontWeight: '800', fontSize: 11 },
  dragRow: { flexDirection: 'row', justifyContent: 'space-between', gap: 8 },
  token: {
    minWidth: 74,
    backgroundColor: '#eff6ff',
    borderWidth: 1.5,
    borderColor: '#93c5fd',
    borderRadius: 14,
    paddingHorizontal: 10,
    paddingVertical: 10,
    alignItems: 'center',
  },
  tokenEmoji: { fontSize: 18, fontWeight: '900', color: '#1e3a8a' },
  dropRow: { flexDirection: 'row', gap: 10 },
  dropZone: {
    flex: 1,
    borderWidth: 1.5,
    borderRadius: 12,
    backgroundColor: '#f8fafc',
    paddingVertical: 10,
    alignItems: 'center',
  },
  dropIcon: { fontSize: 18 },
  dropCount: { fontSize: 20, fontWeight: '900', color: '#1d4ed8' },
  resetBtn: {
    alignSelf: 'flex-end',
    width: 30,
    height: 30,
    borderRadius: 15,
    backgroundColor: '#e2e8f0',
    alignItems: 'center',
    justifyContent: 'center',
  },
  resetText: { color: '#334155', fontWeight: '900', fontSize: 14 },
  legendRow: { flexDirection: 'row', gap: 6 },
  legendChip: {
    flex: 1,
    alignItems: 'center',
    borderWidth: 1.5,
    borderRadius: 999,
    paddingVertical: 6,
    backgroundColor: '#f8fafc',
  },
  legendText: { fontSize: 11, fontWeight: '900' },
  scoreText: { fontSize: 14, fontWeight: '900', textAlign: 'right' },
  cycleCard: {
    borderWidth: 1.5,
    borderRadius: 16,
    backgroundColor: '#f8fafc',
    alignItems: 'center',
    paddingVertical: 20,
  },
  cycleEmoji: { fontSize: 50 },
});
