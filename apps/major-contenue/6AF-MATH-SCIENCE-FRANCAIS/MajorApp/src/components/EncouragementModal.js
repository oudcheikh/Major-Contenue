import React from 'react';
import { Modal, View, Text, TouchableOpacity, StyleSheet } from 'react-native';
import { COLORS } from '../theme';

export default function EncouragementModal({ visible, message, onClose, color = COLORS.primary }) {
  if (!message) return null;
  return (
    <Modal visible={visible} transparent animationType="fade">
      <View style={styles.overlay}>
        <View style={styles.card}>
          <View style={[styles.iconWrap, { backgroundColor: color + '22' }]}>
            <Text style={styles.icon}>🎯</Text>
          </View>
          <Text style={[styles.title, { color }]}>{message.title}</Text>
          <Text style={styles.body}>{message.body}</Text>
          <TouchableOpacity style={[styles.btn, { backgroundColor: color }]} onPress={onClose}>
            <Text style={styles.btnText}>Continuer</Text>
          </TouchableOpacity>
        </View>
      </View>
    </Modal>
  );
}

const styles = StyleSheet.create({
  overlay: {
    flex: 1,
    backgroundColor: 'rgba(15,23,42,0.55)',
    justifyContent: 'center',
    alignItems: 'center',
    padding: 24,
  },
  card: {
    backgroundColor: '#fff',
    borderRadius: 24,
    padding: 28,
    alignItems: 'center',
    width: '100%',
    maxWidth: 340,
    shadowColor: '#0f172a',
    shadowOffset: { width: 0, height: 12 },
    shadowOpacity: 0.18,
    shadowRadius: 24,
    elevation: 12,
  },
  iconWrap: {
    width: 72,
    height: 72,
    borderRadius: 36,
    alignItems: 'center',
    justifyContent: 'center',
    marginBottom: 16,
  },
  icon: { fontSize: 36 },
  title: {
    fontSize: 22,
    fontWeight: '900',
    marginBottom: 10,
    textAlign: 'center',
  },
  body: {
    fontSize: 14,
    color: '#64748b',
    textAlign: 'center',
    lineHeight: 22,
    marginBottom: 24,
  },
  btn: {
    paddingHorizontal: 32,
    paddingVertical: 12,
    borderRadius: 999,
  },
  btnText: {
    color: '#fff',
    fontWeight: '800',
    fontSize: 15,
  },
});
