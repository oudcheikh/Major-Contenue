"""Contrôle de prononciation : retranscrit chaque phrase clonée (Whisper) et la compare au texte.
Venv dédié (faster-whisper, modèle medium ~1,5 Go au 1er lancement) :
    python3 -m venv asr-venv && asr-venv/bin/pip install faster-whisper
Usage : asr-venv/bin/python verif_prononciation.py <dossier_sortie> <texte.txt> [n1 n2 ...]
        python verif_prononciation.py <dossier_sortie> <texte.txt> --candidats
        (classe les candidats/phrase-NN-sK.wav et copie le meilleur en phrase-NN.wav)
LANGUE=fr pour un texte français (défaut ar)."""
import difflib
import os
import re
import shutil
import sys
import wave
from pathlib import Path

import numpy as np
from faster_whisper import WhisperModel

LANGUE = os.environ.get("LANGUE", "ar")
TASHKIL = re.compile(r"[ً-ْٰـ]")


def charger(wav):
    """WAV PCM 16 bits -> float32 mono 16 kHz (évite PyAV, incompatible ici)."""
    with wave.open(str(wav)) as w:
        sr, n, ch = w.getframerate(), w.getnframes(), w.getnchannels()
        x = np.frombuffer(w.readframes(n), dtype=np.int16).astype(np.float32) / 32768
    x = x.reshape(-1, ch).mean(axis=1)
    t = np.arange(0, len(x) / sr, 1 / 16000)
    return np.interp(t, np.arange(len(x)) / sr, x).astype(np.float32)


def norm(s):
    if LANGUE != "ar":
        return " ".join(re.sub(r"[^a-zà-ÿ ]", " ", s.lower()).split())
    s = TASHKIL.sub("", s)
    s = re.sub(r"[أإآٱ]", "ا", s)
    s = s.replace("ى", "ي").replace("ة", "ه")
    s = re.sub(r"[^ء-ي ]", " ", s)
    return " ".join(s.split())


def evaluer(model, wav, phrase):
    segs, _ = model.transcribe(charger(wav), language=LANGUE, beam_size=5)
    entendu = " ".join(s.text for s in segs).strip()
    a, b = norm(phrase).split(), norm(entendu).split()
    sm = difflib.SequenceMatcher(None, a, b)
    diff = [f"{' '.join(a[i1:i2]) or '∅'} → {' '.join(b[j1:j2]) or '∅'}"
            for op, i1, i2, j1, j2 in sm.get_opcodes() if op != "equal"]
    return sm.ratio(), entendu, diff


def main():
    sortie, texte = Path(sys.argv[1]), Path(sys.argv[2])
    phrases = [l.strip() for l in texte.read_text(encoding="utf-8").splitlines()
               if l.strip() and not l.lstrip().startswith("#")]
    model = WhisperModel("medium", device="cpu", compute_type="int8", cpu_threads=4)
    if sys.argv[3:] == ["--candidats"]:
        par_phrase = {}
        for wav in sorted((sortie / "candidats").glob("phrase-*-s*.wav")):
            i = int(wav.name.split("-")[1])
            score, entendu, diff = evaluer(model, wav, phrases[i - 1])
            print(f"{wav.name}  {score:.2f}  {entendu}  {' | '.join(diff)}", flush=True)
            par_phrase.setdefault(i, []).append((score, wav))
        for i, cands in sorted(par_phrase.items()):
            score, wav = max(cands)
            shutil.copy(wav, sortie / f"phrase-{i:02d}.wav")
            print(f"→ phrase {i:02d} : {wav.name} retenu ({score:.2f})")
        return
    quels = [int(a) for a in sys.argv[3:]] or range(1, len(phrases) + 1)
    for i in quels:
        wav = sortie / f"phrase-{i:02d}.wav"
        if wav.exists():
            score, entendu, diff = evaluer(model, wav, phrases[i - 1])
            print(f"phrase {i:02d}  {score:.2f}  entendu : {entendu}")
            for d in diff:
                print(f"           ≠ {d}")


if __name__ == "__main__":
    main()
