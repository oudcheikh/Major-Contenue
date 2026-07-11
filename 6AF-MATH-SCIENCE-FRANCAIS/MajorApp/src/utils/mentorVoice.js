import * as FileSystem from 'expo-file-system';
import {
  AudioModule,
  RecordingPresets,
  createAudioPlayer,
  requestRecordingPermissionsAsync,
  setAudioModeAsync,
} from 'expo-audio';

let currentPlayer = null;
let currentSub = null;
let currentRecorder = null;

function cleanupSubscription() {
  if (!currentSub) return;
  try {
    currentSub.remove();
  } catch {}
  currentSub = null;
}

export async function stopMentorVoice() {
  cleanupSubscription();
  if (!currentPlayer) return;
  try {
    currentPlayer.pause();
  } catch {}
  try {
    currentPlayer.remove();
  } catch {}
  currentPlayer = null;
}

export async function startMentorRecording() {
  const apiKey = process.env.EXPO_PUBLIC_OPENAI_API_KEY;
  if (!apiKey) return false;

  try {
    const perm = await requestRecordingPermissionsAsync();
    if (!perm?.granted) return false;

    await setAudioModeAsync({
      allowsRecording: true,
      playsInSilentMode: true,
      shouldPlayInBackground: false,
      shouldRouteThroughEarpiece: false,
      interruptionMode: 'duckOthers',
    });

    const recorder = new AudioModule.AudioRecorder(RecordingPresets.HIGH_QUALITY);
    await recorder.prepareToRecordAsync();
    recorder.record();
    currentRecorder = recorder;
    return true;
  } catch {
    currentRecorder = null;
    return false;
  }
}

async function transcribeWithModel(uri, apiKey, model) {
  const form = new FormData();
  form.append('model', model);
  form.append('language', 'fr');
  form.append('file', {
    uri,
    name: 'mentor-input.m4a',
    type: 'audio/m4a',
  });

  const res = await fetch('https://api.openai.com/v1/audio/transcriptions', {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${apiKey}`,
    },
    body: form,
  });

  if (!res.ok) return null;
  const data = await res.json();
  const text = String(data?.text || '').trim();
  return text || null;
}

export async function stopMentorRecordingAndTranscribe() {
  const apiKey = process.env.EXPO_PUBLIC_OPENAI_API_KEY;
  if (!apiKey || !currentRecorder) return null;

  let uri = '';
  try {
    await currentRecorder.stop();
    const status = currentRecorder.getStatus();
    uri = status?.url || currentRecorder.uri || '';
  } catch {
    uri = '';
  } finally {
    currentRecorder = null;
    try {
      await setAudioModeAsync({
        allowsRecording: false,
        playsInSilentMode: true,
        shouldPlayInBackground: false,
        shouldRouteThroughEarpiece: false,
        interruptionMode: 'duckOthers',
      });
    } catch {}
  }

  if (!uri) return null;

  try {
    let text = await transcribeWithModel(uri, apiKey, 'gpt-4o-mini-transcribe');
    if (!text) {
      text = await transcribeWithModel(uri, apiKey, 'gpt-4o-transcribe');
    }
    return text || null;
  } catch {
    return null;
  }
}

async function fetchTTSBase64(text, apiKey, voice = 'nova') {
  const res = await fetch('https://api.openai.com/v1/audio/speech', {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${apiKey}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'gpt-4o-mini-tts',
      voice,
      input: text,
      response_format: 'mp3',
      speed: 0.94,
    }),
  });

  if (!res.ok) return null;
  const buf = await res.arrayBuffer();
  if (!buf || buf.byteLength === 0) return null;

  const bytes = new Uint8Array(buf);
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

export async function speakWithOpenAITTS(text, { onDone, onError, voice = 'nova' } = {}) {
  const apiKey = process.env.EXPO_PUBLIC_OPENAI_API_KEY;
  if (!apiKey || !text) return false;

  try {
    await setAudioModeAsync({
      playsInSilentMode: true,
      interruptionMode: 'duckOthers',
      shouldPlayInBackground: false,
      allowsRecording: false,
      shouldRouteThroughEarpiece: false,
    });

    const b64 = await fetchTTSBase64(text, apiKey, voice);
    if (!b64) return false;

    const uri = `${FileSystem.cacheDirectory}mentor-${Date.now()}.mp3`;
    await FileSystem.writeAsStringAsync(uri, b64, { encoding: FileSystem.EncodingType.Base64 });

    await stopMentorVoice();
    const player = createAudioPlayer({ uri }, { keepAudioSessionActive: true });
    player.volume = 1.0;
    currentPlayer = player;

    currentSub = player.addListener('playbackStatusUpdate', (status) => {
      if (!status?.isLoaded) return;
      if (status.didJustFinish) {
        stopMentorVoice();
        if (onDone) onDone();
      }
    });

    player.play();
    return true;
  } catch {
    if (onError) onError();
    return false;
  }
}
