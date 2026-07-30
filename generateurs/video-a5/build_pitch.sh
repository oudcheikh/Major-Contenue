#!/bin/bash
# Rend la vidéo pitch écoles 16:9 (1920×1080), mixe la musique, livre + 4 captures QA.
set -e
cd "$(dirname "$0")"
FF=$(venv/bin/python -c "import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())")
OUTDIR=/home/pcmahmoud/Documents/Perso/Cahier-Math/livrables/videos
QA=${QA_DIR:-/tmp/claude-1000/qa-videos}
mkdir -p "$QA"

if [ "$1" != "--skip-render" ]; then
  venv/bin/manim -r 1920,1080 --fps 30 --disable_caching scene_pitch.py VideoPitch 2>&1 | grep -E "ERROR|Traceback|Rendered" || true
fi
V="media/videos/scene_pitch/1080p30/VideoPitch.mp4"
[ -f "$V" ] || { echo "ÉCHEC RENDU PITCH"; exit 1; }

D=$($FF -i "$V" 2>&1 | grep Duration | sed 's/.*Duration: \([0-9:.]*\),.*/\1/')
DS=$(echo "$D" | awk -F: '{print $1*3600+$2*60+$3}')
FADE=$(echo "$DS-4" | bc)
$FF -y -i "$V" -stream_loop -1 -i assets/carefree.mp3 -filter_complex \
  "[1:a]volume=0.16,afade=t=in:d=2[m];[0:a][m]amix=inputs=2:duration=first:dropout_transition=0:normalize=0[mix];[mix]afade=t=out:st=${FADE}:d=4[a]" \
  -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 160k "$OUTDIR/Major-Pitch-Ecoles-16x9-1080p.mp4" 2>/dev/null

T1=$(echo "$DS*0.10/1" | bc); T2=$(echo "$DS*0.35/1" | bc); T3=$(echo "$DS*0.60/1" | bc); T4=$(echo "$DS*0.85/1" | bc)
for T in $T1 $T2 $T3 $T4; do
  $FF -y -ss "$T" -i "$OUTDIR/Major-Pitch-Ecoles-16x9-1080p.mp4" -frames:v 1 -vf scale=960:-1 "$QA/qa_pitch_${T}.jpg" 2>/dev/null
done
echo "PITCH LIVRÉ : $D → Major-Pitch-Ecoles-16x9-1080p.mp4"
