# -*- coding: utf-8 -*-
"""Narration PROMO — présentation du دفتر ماجور (avantages + parcours + suivi).
Public : parents / écoles (statuts WhatsApp, 9:16). Voix فصحى (ar-SA-HamedNeural).
Découpage fin : 1 phrase = 1 chunk audio = 1 bloc d'animation.
Règles : jamais nommer une méthode ; دفتر ماجور (comme la couverture) ; ton chaleureux."""
import asyncio, json, subprocess
from pathlib import Path

import edge_tts
import imageio_ffmpeg

VOICE = "ar-SA-HamedNeural"
RATE = "-3%"

SEGMENTS = [
    # ── intro ──
    ("intro1", "أبناؤنا مقبلون على مسابقة السنة السادسة. وهذا دفتر ماجور: الرفيق الذكي للمراجعة."),
    ("intro2", "دفترٌ واحد يجمع الدرسَ والتمارينَ والمتابعة، من أول السنة إلى يوم المسابقة."),
    # ── avantages ──
    ("av_rappel", "في كل وحدة تذكيرٌ قصير بالقاعدة، ومثالٌ محلولٌ خطوةً خطوة."),
    ("av_stars", "ثم تمارين متدرجة بالنجوم: نجمةٌ نموذج، ونجمتان أتدرب، وثلاثُ نجومٍ أتحدى نفسي."),
    ("av_regle", "وقاعدتنا الذهبية في كل مسألة: أشاهد، ثم أرسم، ثم أحسب."),
    ("av_ecrire", "ومساحاتُ كتابةٍ واسعة: يكتب الطفل في الدفتر نفسه، فيبقى أثرُ عمله."),
    # ── parcours quotidien ──
    ("parcours", "كلَّ يومٍ وحدةٌ صغيرة: يقرأ التلميذ التذكير، ثم يحل التمارين نجمةً بعد نجمة."),
    # ── QR → webapp ──
    ("qr1", "وانظروا هنا: في كل وحدة رمزٌ للمسح بالهاتف."),
    ("qr2", "امسحوه، فتظهر بطاقةُ مراجعة، وأسئلةٌ تفاعلية، وفيديو يشرح الدرس بالصوت والصورة."),
    # ── suivi parents ──
    ("parent1", "هكذا يتابع الوالدان بسهولة، ويريان تقدمَ ابنهما يومًا بعد يوم."),
    ("parent2", "لستَ بحاجةٍ لأن تكون معلمًا: الحلول موجودة، ودورُك أن تشجع."),
    # ── prof / école ──
    ("ecole1", "وفي القسم يعتمده المعلم للدعم والواجبات، فالوحدات مرتبةٌ على البرنامج الرسمي."),
    # ── outro ──
    ("outro1", "دفتر ماجور: يتعلم الطفل، ويطمئن الوالدان، ويرتاح المعلم."),
    ("outro2", "ماجور، رفيقُ النجاح حتى يوم المسابقة!"),
]

OUT = Path(__file__).parent / "audio_promo"


async def main():
    OUT.mkdir(exist_ok=True)
    ff = imageio_ffmpeg.get_ffmpeg_exe()
    durations = {}
    for name, text in SEGMENTS:
        mp3 = OUT / f"{name}.mp3"
        await edge_tts.Communicate(text, VOICE, rate=RATE).save(str(mp3))
        r = subprocess.run([ff, "-i", str(mp3), "-f", "null", "-"],
                           capture_output=True, text=True)
        for line in r.stderr.splitlines():
            if "time=" in line:
                t = line.split("time=")[1].split(" ")[0]
                h, m, s = t.split(":")
                durations[name] = round(int(h) * 3600 + int(m) * 60 + float(s), 2)
        print(f"{name}: {durations.get(name, '?')} s")
    (OUT / "durations.json").write_text(json.dumps(durations, indent=2))
    print("total:", round(sum(durations.values()), 1), "s")


if __name__ == "__main__":
    asyncio.run(main())
