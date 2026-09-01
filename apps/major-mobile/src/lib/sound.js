// Sons du jeu — effets synthétisés maison + voix d'أستاذ ماجور
// (ar-SA-HamedNeural, la même voix que les vidéos explicatives).
// Tous les appels sont best-effort : jamais de crash si l'audio échoue.

import { createAudioPlayer } from 'expo-audio'

const players = {}

function play(key, source, volume = 1) {
  try {
    if (!players[key]) {
      players[key] = createAudioPlayer(source)
    }
    const p = players[key]
    p.volume = volume
    p.seekTo(0)
    p.play()
  } catch {}
}

export function sfxCorrect() {
  play('ding', require('../../assets/sounds/ding.wav'), 0.8)
}

export function sfxWrong() {
  play('boing', require('../../assets/sounds/boing.wav'), 0.55)
}

export function sfxWin() {
  play('tada', require('../../assets/sounds/tada.wav'), 0.9)
}

export function sfxTap() {
  play('pop', require('../../assets/sounds/pop.wav'), 0.35)
}

const PRAISE_VOICES = [
  () => play('v-ahsant', require('../../assets/sounds/voice-ahsant.mp3')),
  () => play('v-momtaz', require('../../assets/sounds/voice-momtaz.mp3')),
]

export function voicePraise() {
  PRAISE_VOICES[Math.floor(Math.random() * PRAISE_VOICES.length)]()
}

export function voiceRetry() {
  play('v-hawil', require('../../assets/sounds/voice-hawil.mp3'))
}

// Musique d'encouragement (boucle balafon pentatonique originale) —
// jouée en fond discret pendant les activités, jamais par-dessus les voix.
// L'enfant peut la couper avec le bouton 🎵/🔇 (préférence mémorisée).
import AsyncStorage from '@react-native-async-storage/async-storage'

let musicPlayer = null
let musicEnabled = true
AsyncStorage.getItem('major.musicEnabled')
  .then((v) => { if (v === '0') musicEnabled = false })
  .catch(() => {})

export function isMusicEnabled() {
  return musicEnabled
}

export function setMusicEnabled(on) {
  musicEnabled = on
  AsyncStorage.setItem('major.musicEnabled', on ? '1' : '0').catch(() => {})
  if (!on) stopMusic()
}

export function startMusic() {
  if (!musicEnabled) return
  try {
    if (!musicPlayer) {
      musicPlayer = createAudioPlayer(require('../../assets/sounds/music-loop.wav'))
      musicPlayer.loop = true
    }
    musicPlayer.volume = 0.2
    musicPlayer.seekTo(0)
    musicPlayer.play()
  } catch {}
}

export function stopMusic() {
  try { musicPlayer && musicPlayer.pause() } catch {}
}
