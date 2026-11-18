"""Génère N candidats (graines différentes) pour certaines phrases, avec la voix clonée.
Usage : voix-clone/venv/bin/python gen_candidats.py <texte.txt> <n> <i1> [i2 ...]
-> sortie/<nom>/candidats/phrase-NN-sK.wav
LANGUE=fr pour un texte français (ex. « Major » prononcé à la française), défaut ar."""
import os
import sys
from pathlib import Path

VC = Path(__file__).parent
sys.path.insert(0, str(VC))
import clone_voix as cv  # noqa: E402  (lit sys.argv[1] = le texte)

import soundfile as sf  # noqa: E402
import torch  # noqa: E402
from chatterbox.mtl_tts import ChatterboxMultilingualTTS  # noqa: E402

n = int(sys.argv[2])
quels = [int(a) for a in sys.argv[3:]]
dest = cv.SORTIE / "candidats"
dest.mkdir(parents=True, exist_ok=True)
torch.set_num_threads(int(os.environ.get("THREADS", 6)))
LANGUE = os.environ.get("LANGUE", "ar")
model = ChatterboxMultilingualTTS.from_pretrained(device="cpu")
for i in quels:
    texte = cv.PHRASES[i - 1]
    for k in range(n):
        out = dest / f"phrase-{i:02d}-s{k}.wav"
        if out.exists():
            continue
        torch.manual_seed(1000 + 37 * i + k)
        wav = model.generate(texte, language_id=LANGUE, audio_prompt_path=str(cv.REF),
                             exaggeration=0.5, cfg_weight=0.5)
        propre = cv.nettoyer(wav.squeeze(0).numpy(), model.sr)
        sf.write(out, propre, model.sr)
        duree = len(propre) / model.sr
        if LANGUE == "ar":
            print(f"{out.name} rapport {cv.rapport_duree(texte, duree):.2f}", flush=True)
        else:
            print(f"{out.name} {duree:.2f} s", flush=True)
