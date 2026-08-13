import * as FileSystem from 'expo-file-system';
import { createAudioPlayer, setAudioModeAsync } from 'expo-audio';

const CACHE = {};
let activePlayer = null;

function bytesToBase64(bytes) {
  const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=';
  let output = '';
  for (let i = 0; i < bytes.length; i += 3) {
    const a = bytes[i];
    const b = i + 1 < bytes.length ? bytes[i + 1] : NaN;
    const c = i + 2 < bytes.length ? bytes[i + 2] : NaN;

    const b1 = a >> 2;
    const b2 = ((a & 3) << 4) | (Number.isNaN(b) ? 0 : b >> 4);
    const b3 = Number.isNaN(b) ? 64 : (((b & 15) << 2) | (Number.isNaN(c) ? 0 : c >> 6));
    const b4 = Number.isNaN(c) ? 64 : (c & 63);
    output += chars[b1] + chars[b2] + chars[b3] + chars[b4];
  }
  return output;
}

function buildToneWavBase64({ frequency = 660, durationMs = 110, volume = 0.35, sampleRate = 22050 }) {
  const samples = Math.floor((sampleRate * durationMs) / 1000);
  const dataBytes = samples * 2;
  const totalBytes = 44 + dataBytes;
  const buf = new ArrayBuffer(totalBytes);
  const view = new DataView(buf);

  function writeStr(offset, str) {
    for (let i = 0; i < str.length; i += 1) {
      view.setUint8(offset + i, str.charCodeAt(i));
    }
  }

  writeStr(0, 'RIFF');
  view.setUint32(4, 36 + dataBytes, true);
  writeStr(8, 'WAVE');
  writeStr(12, 'fmt ');
  view.setUint32(16, 16, true);
  view.setUint16(20, 1, true);
  view.setUint16(22, 1, true);
  view.setUint32(24, sampleRate, true);
  view.setUint32(28, sampleRate * 2, true);
  view.setUint16(32, 2, true);
  view.setUint16(34, 16, true);
  writeStr(36, 'data');
  view.setUint32(40, dataBytes, true);

  const attack = Math.floor(samples * 0.08);
  const release = Math.floor(samples * 0.2);

  for (let i = 0; i < samples; i += 1) {
    const t = i / sampleRate;
    let env = 1;
    if (i < attack) env = i / Math.max(1, attack);
    if (i > samples - release) env = Math.max(0, (samples - i) / Math.max(1, release));
    const s = Math.sin(2 * Math.PI * frequency * t) * volume * env;
    const pcm = Math.max(-1, Math.min(1, s));
    view.setInt16(44 + i * 2, pcm * 32767, true);
  }

  return bytesToBase64(new Uint8Array(buf));
}

async function getToneUri(name, config) {
  if (CACHE[name]) return CACHE[name];
  const uri = `${FileSystem.cacheDirectory}${name}.wav`;
  const info = await FileSystem.getInfoAsync(uri);
  if (!info.exists) {
    const b64 = buildToneWavBase64(config);
    await FileSystem.writeAsStringAsync(uri, b64, { encoding: FileSystem.EncodingType.Base64 });
  }
  CACHE[name] = uri;
  return uri;
}

async function play(uri) {
  try {
    await setAudioModeAsync({
      playsInSilentMode: true,
      interruptionMode: 'duckOthers',
      shouldPlayInBackground: false,
      allowsRecording: false,
      shouldRouteThroughEarpiece: false,
    });
    if (activePlayer) {
      try {
        activePlayer.pause();
        activePlayer.remove();
      } catch {}
      activePlayer = null;
    }
    const player = createAudioPlayer({ uri }, { keepAudioSessionActive: false });
    activePlayer = player;
    player.volume = 0.95;
    const sub = player.addListener('playbackStatusUpdate', (status) => {
      if (!status?.isLoaded || !status.didJustFinish) return;
      try {
        sub.remove();
      } catch {}
      try {
        player.remove();
      } catch {}
      if (activePlayer === player) activePlayer = null;
    });
    player.play();
  } catch {}
}

export async function playTapSound() {
  const uri = await getToneUri('ui-tap', { frequency: 640, durationMs: 70, volume: 0.22 });
  await play(uri);
}

export async function playSuccessSound() {
  const uri = await getToneUri('ui-success', { frequency: 920, durationMs: 130, volume: 0.28 });
  await play(uri);
}

export async function playErrorSound() {
  const uri = await getToneUri('ui-error', { frequency: 320, durationMs: 120, volume: 0.24 });
  await play(uri);
}
