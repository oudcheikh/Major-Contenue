"""Extrait la voix seule d'une vidéo (musique retirée par Demucs) -> ref/voix_ref.wav.

Chatterbox n'utilise que ~10 s de référence : on garde la fenêtre de 12 s
où la voix est la plus continue (le moins de silences).
"""
import subprocess
import sys
from pathlib import Path

import numpy as np
import soundfile as sf

ICI = Path(__file__).parent
VIDEO_PY = ICI.parent / "video-a5" / "venv" / "bin" / "python"  # imageio-ffmpeg y est installé


def ffmpeg_exe():
    return subprocess.check_output(
        [str(VIDEO_PY), "-c", "import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())"],
        text=True).strip()


def main(video):
    travail = ICI / "ref"
    travail.mkdir(exist_ok=True)
    brut = travail / "audio_brut.wav"
    subprocess.run([ffmpeg_exe(), "-hide_banner", "-loglevel", "error", "-y", "-i", video,
                    "-vn", "-ac", "2", "-ar", "44100", str(brut)], check=True)
    subprocess.run([sys.executable, "-m", "demucs", "--two-stems=vocals", "-n", "htdemucs",
                    "-o", str(travail / "demucs"), str(brut)], check=True)
    voix, sr = sf.read(travail / "demucs" / "htdemucs" / "audio_brut" / "vocals.wav")
    voix = voix.mean(axis=1)
    sf.write(travail / "voix_complete.wav", voix, sr)

    # Énergie par trame de 50 ms ; trame « voisée » = au-dessus de -35 dB du pic.
    trame = int(0.05 * sr)
    rms = np.sqrt(np.mean(voix[: len(voix) // trame * trame].reshape(-1, trame) ** 2, axis=1))
    voisee = 20 * np.log10(rms + 1e-9) > 20 * np.log10(rms.max()) - 35
    largeur = int(12 / 0.05)
    score = np.convolve(voisee, np.ones(largeur), "valid")
    debut = int(score.argmax())
    extrait = voix[debut * trame:(debut + largeur) * trame]
    extrait = extrait / np.abs(extrait).max() * 0.9
    sf.write(travail / "voix_ref.wav", extrait, sr)
    print(f"référence : {debut * 0.05:.1f} s -> {(debut + largeur) * 0.05:.1f} s, "
          f"voix présente {score.max() / largeur:.0%} du temps")


if __name__ == "__main__":
    main(sys.argv[1])
