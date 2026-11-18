"""Narration avec la voix de l'utilisateur (clonage local, Chatterbox multilingue, CPU).

Usage :
    venv/bin/python separer_voix.py <video.mp4>     # -> ref/voix_ref.wav
    venv/bin/python clone_voix.py                    # -> sortie/phrase-NN.wav + narration-complete.wav

Reprise : une phrase déjà générée n'est pas refaite (supprimer le .wav pour la refaire).
"""
import json
import os
import re
import sys
import time
from pathlib import Path

import numpy as np
import soundfile as sf
import torch
import torchaudio as ta

ICI = Path(__file__).parent
REF = ICI / "ref" / "voix_ref.wav"
SORTIE = ICI / "sortie"

# Graphie choisie par l'utilisateur (29/10) : prononcée « Major » par le modèle.
MAJOR = "مَاجُورْ"

# Texte de la vidéo « قاعة الشرف — أساتذة ماجور », 1 phrase = 1 fichier.
PHRASES = [
    "مَنْ يَقِفُ وَرَاءَ أَكْثَرَ مِنْ سَبْعَةِ آلَافِ دَرْسٍ؟",
    f"قَاعَةُ الشَّرَفْ. أَسَاتِذَةُ {MAJOR}.",
    "هُمُ الَّذِينَ حَمَلُوا الأَمَانَةَ، دَرْسًا بَعْدَ دَرْسْ.",
    "صَحَّحُوا الأَخْطَاءْ، وَأَنَارُوا العُقُولْ.",
    "وَرَافَقُوا كُلَّ تِلْمِيذْ، حَتَّى يَبْلُغَ الفَهْمْ.",
    "مِئَةٌ وَتِسْعَةُ أَسَاتِذَةْ!",
    "أَكْثَرُ مِنْ سَبْعَةِ آلَافِ دَرْسْ!",
    "فَرِيقٌ وَاحِدْ، وَهَدَفٌ وَاحِدْ: نَجَاحُ أَبْنَائِنَا.",
    f"شُكْرًا، أَسَاتِذَةَ {MAJOR}.",
    f"{MAJOR}، مَعَكُمْ حَتَّى النَّجَاحْ.",
]

# Autre texte : `clone_voix.py textes/<nom>.txt` (1 ligne = 1 phrase, # = commentaire)
# -> sortie/<nom>/phrase-NN.wav + durations.json.
if len(sys.argv) > 1:
    _texte = Path(sys.argv[1])
    PHRASES = [l.strip() for l in _texte.read_text(encoding="utf-8").splitlines()
               if l.strip() and not l.lstrip().startswith("#")]
    SORTIE = SORTIE / _texte.stem
PAUSE_ENTRE_PHRASES = 0.6  # secondes

# Contrôle qualité : ~0,16 s par lettre arabe avec cette voix. Une phrase bien plus
# longue contient un silence, un bourdonnement ou un mot inventé -> nouvel essai.
SECONDES_PAR_LETTRE = 0.16
RAPPORT_ACCEPTE = (0.7, 1.3)
ESSAIS_MAX = 4


def rapport_duree(texte, duree):
    lettres = len(re.findall(r"[ء-ي]", texte))
    return duree / (lettres * SECONDES_PAR_LETTRE)


def nettoyer(wav, sr):
    """Retire les silences de bord et le bruit parasite que le modèle ajoute parfois
    après la phrase : un bout de son < 0,6 s isolé par ≥ 0,4 s de silence en fin."""
    trame = int(0.05 * sr)
    n = len(wav) // trame
    rms = np.sqrt((wav[: n * trame].reshape(n, trame) ** 2).mean(axis=1))
    voisee = 20 * np.log10(rms + 1e-9) > 20 * np.log10(rms.max()) - 35
    segments, debut = [], None
    for i, v in enumerate(np.append(voisee, False)):
        if v and debut is None:
            debut = i
        elif not v and debut is not None:
            segments.append((debut, i))
            debut = None
    while (len(segments) > 1 and segments[-1][1] - segments[-1][0] < 12
           and segments[-1][0] - segments[-2][1] >= 8):
        segments.pop()
    a = max(segments[0][0] - 2, 0) * trame
    b = min(segments[-1][1] + 3, n) * trame
    propre = wav[a:b].copy()
    fondu = int(0.03 * sr)
    propre[-fondu:] *= np.linspace(1, 0, fondu)
    return propre


def assembler(sr):
    blanc = np.zeros(int(PAUSE_ENTRE_PHRASES * sr))
    morceaux, durees = [], {}
    for i in range(1, len(PHRASES) + 1):
        wav = sf.read(SORTIE / f"phrase-{i:02d}.wav")[0]
        durees[f"phrase-{i:02d}"] = round(len(wav) / sr, 2)
        morceaux += [wav, blanc]
    sf.write(SORTIE / "narration-complete.wav", np.concatenate(morceaux[:-1]), sr)
    (SORTIE / "durations.json").write_text(json.dumps(durees, indent=2))


def main():
    if not REF.exists():
        sys.exit(f"Référence absente : {REF} (lancer separer_voix.py d'abord)")
    SORTIE.mkdir(exist_ok=True)
    a_faire = [i for i in range(1, len(PHRASES) + 1)
               if not (SORTIE / f"phrase-{i:02d}.wav").exists()]
    if a_faire:
        from chatterbox.mtl_tts import ChatterboxMultilingualTTS
        torch.set_num_threads(int(os.environ.get("THREADS", os.cpu_count())))
        model = ChatterboxMultilingualTTS.from_pretrained(device="cpu")
        for i in a_faire:
            t0 = time.time()
            texte = PHRASES[i - 1]
            meilleur = None  # (écart au rapport idéal, brut, propre, rapport)
            for essai in range(ESSAIS_MAX):
                torch.manual_seed(7 + 100 * i + essai)
                wav = model.generate(texte, language_id="ar", audio_prompt_path=str(REF),
                                     exaggeration=0.5, cfg_weight=0.5)
                propre = nettoyer(wav.squeeze(0).numpy(), model.sr)
                r = rapport_duree(texte, len(propre) / model.sr)
                if meilleur is None or abs(r - 1) < meilleur[0]:
                    meilleur = (abs(r - 1), wav, propre, r)
                if RAPPORT_ACCEPTE[0] <= r <= RAPPORT_ACCEPTE[1]:
                    break
            _, wav, propre, r = meilleur
            ta.save(str(SORTIE / f"brut-{i:02d}.wav"), wav, model.sr)
            sf.write(SORTIE / f"phrase-{i:02d}.wav", propre, model.sr)
            alerte = "" if RAPPORT_ACCEPTE[0] <= r <= RAPPORT_ACCEPTE[1] else "  ⚠ à écouter"
            print(f"phrase {i:02d} : {time.time() - t0:.0f} s, {essai + 1} essai(s), "
                  f"rapport {r:.2f}{alerte}", flush=True)
    assembler(sf.info(SORTIE / "phrase-01.wav").samplerate)
    print("narration-complete.wav prête", flush=True)


if __name__ == "__main__":
    main()
