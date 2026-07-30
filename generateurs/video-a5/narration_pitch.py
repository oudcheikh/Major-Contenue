# -*- coding: utf-8 -*-
"""Narration PITCH ÉCOLES — convaincre le directeur (B2B, court et percutant).
16:9, arabe فصحى (ar-SA-HamedNeural). Argumentaire : réputation de l'école aux
résultats du concours → zéro charge pour les profs → digital QR → parents qui
voient la valeur → offre 800 MRU + remise écoles → démo.
1 phrase = 1 chunk audio = 1 bloc d'animation."""
import asyncio, json, subprocess
from pathlib import Path

import edge_tts
import imageio_ffmpeg

VOICE = "ar-MA-JamalNeural"   # choix utilisateur 24/07 (Hamed remplacé pour cette vidéo)
RATE = "-3%"

SEGMENTS = [
    # pitch commerçant (AIDA) : douleur → agitation → retournement+preuve → bénéfices →
    # bouche-à-oreille = inscriptions → urgence → démo GRATUITE (zéro risque).
    # Règles : pas de prix, pas de « directeur », pas de concours, « منصة ذكية » jamais QR.
    ("hook", "سؤالٌ واحد: حين يسألكم وليُّ الأمر: أين وصل مستوى ابني؟ ماذا تجيبونه؟"),
    ("pain", "أغلبُ المدارس تكتشف ضعفَ التلميذ في آخر السنة... حين يفوتُ الأوان، ويغضبُ الأولياء."),
    ("flip", "دفاتر ماجور تقلب المعادلة: مستوى كل تلميذ واضحٌ أمامكم من الأسبوع الأول. "
             "وليست وعودًا: جرّبها تلاميذ ماجور، وأثبتت نتائجَها."),
    ("prof", "معلموكم لن يحضّروا شيئًا: تذكيرٌ ومثالٌ محلول وتمارينُ متدرجة، جاهزةٌ للدعم والواجبات."),
    ("digital", "ومع كل دفترٍ منصةٌ ذكية: بطاقاتُ مراجعة، وأسئلةٌ تفاعلية، وفيديو لكل درس."),
    ("parents", "والأولياء يرون بأعينهم كلَّ يوم ما تقدمه مدرستُكم. "
                "والوليُّ الراضي يحدّث عنكم الجميع، ويجلب لكم أولياءَ جددًا."),
    ("vision", "وأنتم ترون مستوى كل تلميذ بوضوح، فتعالجون الضعفَ في وقته، وتصنعون التفوق."),
    ("urgence", "بلا تكوينٍ ولا تعقيد: دفترٌ ومنصة. كونوا أولَ مدرسةٍ تقدم هذا لتلاميذها."),
    ("cta", "اطلبوا اليومَ عرضًا تجريبيًا مجانيًا في مدرستكم، وشاهدوا الفرقَ بأنفسكم. "
            "ماجور، شريكُ نجاح مدرستكم!"),
]

OUT = Path(__file__).parent / "audio_pitch"


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
