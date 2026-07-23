# -*- coding: utf-8 -*-
"""Petits effets sonores synthétisés (libres de droits par construction)."""
import struct
import wave
from pathlib import Path

import numpy as np

SR = 44100
OUT = Path(__file__).parent / "sfx"
OUT.mkdir(exist_ok=True)


def save(name, sig, gain=0.28):
    sig = np.clip(sig * gain, -1, 1)
    data = (sig * 32767).astype(np.int16)
    with wave.open(str(OUT / f"{name}.wav"), "w") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(data.tobytes())
    print(name, round(len(sig) / SR, 2), "s")


def env(n, attack=0.005, decay=None):
    t = np.arange(n) / SR
    decay = decay or (n / SR)
    e = np.minimum(t / attack, 1.0) * np.exp(-t / (decay / 4))
    return e


def tone(freq, dur, harmonics=((1, 1.0), (2, 0.25), (3, 0.08))):
    t = np.arange(int(SR * dur)) / SR
    s = sum(a * np.sin(2 * np.pi * freq * h * t) for h, a in harmonics)
    return s * env(len(t), decay=dur)


# pop — apparition d'un élément
t = np.arange(int(SR * 0.09)) / SR
sweep = np.sin(2 * np.pi * (420 + 1800 * t / 0.09) * t)
save("pop", sweep * env(len(t), decay=0.09), gain=0.20)

# ding — révélation / bonne réponse (clochette douce)
save("ding", tone(1046.5, 0.45, ((1, 1.0), (2.76, 0.35), (5.4, 0.12))), gain=0.16)

# boing — erreur gentille (le « 35 » barré)
t = np.arange(int(SR * 0.30)) / SR
fr = 220 - 90 * t / 0.30
save("boing", np.sin(2 * np.pi * fr * t) * env(len(t), decay=0.30), gain=0.22)

# whoosh — transition
n = int(SR * 0.35)
noise = np.random.default_rng(7).standard_normal(n)
k = 40
lp = np.convolve(noise, np.ones(k) / k, "same")
save("whoosh", lp * np.hanning(n) * 2.2, gain=0.15)

# tada — célébration finale (arpège + accord)
notes = [523.25, 659.25, 783.99, 1046.5]
parts = [tone(f, 0.14) for f in notes]
chord = sum(tone(f, 0.9, ((1, 1.0), (2, 0.2))) for f in notes)
sig = np.concatenate(parts + [chord])
save("tada", sig, gain=0.20)
