"""Remplace la voix d'une vidéo par la narration clonée, en gardant images + musique.

Usage :
    venv/bin/python assembler_video.py <video.mp4> <sortie.mp4>

Pré-requis : separer_voix.py (fournit la musique seule) puis clone_voix.py (phrases).
"""
import subprocess
import sys

import numpy as np
import soundfile as sf
import torch
import torchaudio.functional as AF

from clone_voix import PHRASES, SORTIE
from separer_voix import ICI, ffmpeg_exe

MUSIQUE = ICI / "ref" / "demucs" / "htdemucs" / "audio_brut" / "no_vocals.wav"
VOIX_ORIGINALE = ICI / "ref" / "voix_complete.wav"

# Début (s) de chaque phrase, relevé sur la voix originale de la vidéo « قاعة الشرف ».
# Si une phrase déborde sur la suivante, celle-ci est décalée juste après.
DEBUTS = [0.1, 3.0, 6.15, 10.9, 16.4, 27.9, 30.4, 39.4, 45.15, 49.8]
ECART_MIN = 0.25


def niveau_parole(x, sr):
    """RMS moyen des trames où l'on parle (ignore les silences)."""
    t = int(0.05 * sr)
    n = len(x) // t
    rms = np.sqrt((x[: n * t].reshape(n, t) ** 2).mean(axis=1))
    return rms[rms > rms.max() * 0.1].mean()


def main(video, sortie):
    musique, sr = sf.read(MUSIQUE)
    piste = np.zeros(len(musique))
    fin_precedente = 0.0
    for i, debut in enumerate(DEBUTS, 1):
        voix, sr_voix = sf.read(SORTIE / f"phrase-{i:02d}.wav")
        voix = AF.resample(torch.from_numpy(voix).float(), sr_voix, sr).numpy()
        debut = max(debut, fin_precedente + ECART_MIN)
        a = int(debut * sr)
        b = min(a + len(voix), len(piste))
        piste[a:b] += voix[: b - a]
        fin_precedente = debut + len(voix) / sr
        print(f"phrase {i:02d} : {debut:5.2f} s -> {fin_precedente:5.2f} s", flush=True)
    if fin_precedente > len(piste) / sr:
        print("⚠ la dernière phrase est coupée par la fin de la vidéo")

    # Même volume de voix que l'original, musique inchangée.
    originale, _ = sf.read(VOIX_ORIGINALE)
    piste *= niveau_parole(originale, sr) / niveau_parole(piste, sr)
    mix = musique + piste[:, None]
    mix /= max(1.0, np.abs(mix).max() / 0.98)
    wav = SORTIE / "mix-video.wav"
    sf.write(wav, mix, sr)

    subprocess.run([ffmpeg_exe(), "-hide_banner", "-loglevel", "error", "-y",
                    "-i", video, "-i", str(wav), "-map", "0:v", "-map", "1:a",
                    "-c:v", "copy", "-c:a", "aac", "-b:a", "160k", "-shortest",
                    "-movflags", "+faststart", sortie], check=True)
    print("vidéo :", sortie)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
