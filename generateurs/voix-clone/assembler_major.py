"""Assemble les phrases où « Major » est prononcé À LA FRANÇAISE (demande utilisateur 12/11).

Le modèle arabe déforme مَاجُورْ (« مجور », « ماجورة ») : on génère « Major » à part en français
avec la même voix clonée, puis on le colle entre les morceaux arabes.

Usage : venv/bin/python assembler_major.py textes/promo-parents.txt textes/promo-parents-morceaux.txt
Entrées : sortie/<morceaux>/phrase-KK.wav (meilleures prises, cf. verif_prononciation.py --candidats)
          sortie/major-fr/phrase-01.wav (LANGUE=fr gen_candidats.py textes/major-fr.txt …)
Sortie  : sortie/<texte>/phrase-NN.wav pour chaque phrase contenant {MAJOR} ou présente telle quelle
          dans les morceaux ; les autres phrase-NN.wav déjà générées ne sont pas touchées."""
import sys
from pathlib import Path

import numpy as np
import soundfile as sf

ICI = Path(__file__).parent
SORTIE = ICI / "sortie"
MAJOR = "{MAJOR}"
PAUSE_PONCTUATION = 0.30   # après « : » ou « ، »
PAUSE_LIAISON = 0.10       # إضافة (« دَفْتَرُ Major ») : simple souffle


def lignes(f):
    return [l.strip() for l in Path(f).read_text(encoding="utf-8").splitlines()
            if l.strip() and not l.lstrip().startswith("#")]


def fondu(x, sr, ms=10):
    n = int(sr * ms / 1000)
    x = x.copy()
    x[:n] *= np.linspace(0, 1, n)
    x[-n:] *= np.linspace(1, 0, n)
    return x


def serrer(x, sr, marge=0.03):
    """Coupe le silence de bord laissé par nettoyer() pour que les pauses ci-dessus soient
    les vraies pauses entendues."""
    trame = int(0.01 * sr)
    n = len(x) // trame
    e = 20 * np.log10(np.sqrt((x[: n * trame].reshape(n, trame) ** 2).mean(axis=1)) + 1e-9)
    voix = np.where(e > e.max() - 40)[0]
    a = max(voix[0] * trame - int(marge * sr), 0)
    b = min((voix[-1] + 1) * trame + int(marge * sr), len(x))
    return x[a:b]


def rms(x):
    return float(np.sqrt(np.mean(x ** 2)))


def main():
    texte, morceaux_txt = Path(sys.argv[1]), Path(sys.argv[2])
    phrases, morceaux = lignes(texte), lignes(morceaux_txt)
    dossier_m = SORTIE / morceaux_txt.stem
    audio_m = {}
    for k, m in enumerate(morceaux, 1):
        a, sr_m = sf.read(dossier_m / f"phrase-{k:02d}.wav")
        audio_m[m] = (serrer(a, sr_m), sr_m)
    major, sr = sf.read(SORTIE / "major-fr" / "phrase-01.wav")
    major = serrer(major, sr)
    # même niveau que la voix arabe
    major = major * (np.median([rms(a) for a, _ in audio_m.values()]) / rms(major))
    dest = SORTIE / texte.stem
    dest.mkdir(exist_ok=True)

    for i, phrase in enumerate(phrases, 1):
        if MAJOR not in phrase and phrase not in audio_m:
            continue
        bouts = []
        for j, morceau in enumerate(phrase.split(MAJOR)):
            if j > 0:   # un « Major » avant ce morceau
                avant = phrase.split(MAJOR)[j - 1].rstrip()
                p = PAUSE_PONCTUATION if avant.endswith((":", "،")) else PAUSE_LIAISON
                if bouts:
                    bouts.append(np.zeros(int(p * sr)))
                bouts.append(fondu(major, sr))
                if morceau.strip().startswith("،"):
                    bouts.append(np.zeros(int(PAUSE_PONCTUATION * sr)))
            m = morceau.strip().lstrip("،").strip()
            if m in ("", "!", ".", "؟"):
                continue
            if m not in audio_m:
                sys.exit(f"phrase {i} : morceau absent de {morceaux_txt.name} : {m}")
            a, sr_m = audio_m[m]
            assert sr_m == sr
            if bouts and not morceau.strip().startswith("،"):
                bouts.append(np.zeros(int(PAUSE_LIAISON * sr)))
            bouts.append(fondu(a, sr))
        sortie = np.concatenate(bouts)
        sf.write(dest / f"phrase-{i:02d}.wav", sortie, sr)
        print(f"phrase-{i:02d}.wav : {len(sortie) / sr:.2f} s")


if __name__ == "__main__":
    main()
