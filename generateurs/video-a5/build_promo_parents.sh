#!/bin/bash
# Promo PARENTS 9:16 avec la voix de l'utilisateur : durées → rendu 1080×1920 → musique → livraison.
# Voix : ../voix-clone (clone_voix.py textes/promo-parents.txt) ; `--skip-render` = refaire le mix seul.
set -e
cd "$(dirname "$0")"
FF=$(venv/bin/python -c "import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())")
VOIX=../voix-clone/sortie/promo-parents
OUT=/home/pcmahmoud/Documents/Perso/Cahier-Math/livrables/videos/Major-Promo-Parents-voix-9x16-1080p.mp4
QA=${QA_DIR:-/tmp/claude-1000/qa-videos}
mkdir -p "$QA"

# Durées réelles des phrases retenues (une phrase régénérée change de durée).
venv/bin/python - "$VOIX" <<'EOF'
import json, sys, wave
from pathlib import Path
d = Path(sys.argv[1])
dur = {}
for f in sorted(d.glob("phrase-[0-9][0-9].wav")):
    with wave.open(str(f)) as w:
        dur[f.stem] = round(w.getnframes() / w.getframerate(), 2)
(d / "durations.json").write_text(json.dumps(dur, indent=2))
print(f"{len(dur)} phrases, {sum(dur.values()):.1f} s de voix")
EOF

if [ "$1" != "--skip-render" ]; then
  venv/bin/manim --disable_caching scene_promo_parents.py VideoPromoParents 2>&1 | grep -E "ERROR|Traceback|Rendered" || true
fi
V="media/videos/scene_promo_parents/1920p30/VideoPromoParents.mp4"
[ -f "$V" ] || { echo "ÉCHEC RENDU"; exit 1; }

D=$($FF -i "$V" 2>&1 | grep Duration | sed 's/.*Duration: \([0-9:.]*\),.*/\1/')
DS=$(echo "$D" | awk -F: '{print $1*3600+$2*60+$3}')
FADE=$(echo "$DS-3" | bc)
$FF -y -i "$V" -stream_loop -1 -i assets/carefree.mp3 -filter_complex \
  "[1:a]volume=0.14,afade=t=in:d=1.5[m];[0:a][m]amix=inputs=2:duration=first:dropout_transition=0:normalize=0[mix];[mix]afade=t=out:st=${FADE}:d=3[a]" \
  -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 160k -movflags +faststart "$OUT" 2>/dev/null

for P in 8 25 45 62 80 95; do
  T=$(LC_ALL=C printf "%.1f" "$(echo "$DS*$P/100" | bc -l)")   # locale fr : virgule refusée par ffmpeg
  $FF -y -ss "$T" -i "$OUT" -frames:v 1 -vf scale=540:-1 "$QA/qa_promo_parents_${P}.jpg" 2>/dev/null
done
echo "LIVRÉE : $D → $OUT"
