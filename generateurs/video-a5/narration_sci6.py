# -*- coding: utf-8 -*-
"""Narration Sciences 6 — التطعيم. Fidèle au cahier (sciences_2.py, u6_*) :
اللقاح يهيّئ الجهاز المناعي · تدريب لجيش الدفاع · القضاء على الجدري ·
يحمي الطفل والآخرين · جدول التطعيم · مثال محلول: 200 تلميذ، 50% = 100 مطعَّم ·
سياق موريتاني: المركز الصحي، دفتر التطعيم."""
import asyncio, json, subprocess
from pathlib import Path

import edge_tts
import imageio_ffmpeg

VOICE = "ar-SA-HamedNeural"
RATE = "-3%"

SEGMENTS = [
    ("intro1", "أهلًا بكم يا أبطال العلوم! درسُ اليوم من مادة العلوم الطبيعية: "
               "التطعيم."),
    ("intro2", "في هذا الدرس سنعرف ما هو التطعيم، وكيف يحمي اللقاح أجسامنا "
               "ويحمي الآخرين من حولنا."),
    # ── التعريف ──
    ("def1", "التطعيم هو حماية الجسم من بعض الأمراض بواسطة اللقاحات. "
             "واللقاح يهيّئ الجهاز المناعي للدفاع عن نفسه."),
    # ── التدريب ──
    ("train1", "تخيّل اللقاح تدريبًا لجيش الدفاع في جسمك: "
               "يأخذ جزءًا ضعيفًا جدًا من الميكروب، فيتدرّب الجسم ويصنع أجسامًا مضادة."),
    ("train2", "فإذا جاء المرض حقًّا، وجد جسمك مستعدًّا للدفاع عنه!"),
    # ── الفائدة ──
    ("use1", "يقينا اللقاح من أمراض خطيرة كالحصبة وشلل الأطفال. "
             "وبفضل التطعيم قُضي نهائيًا على مرض الجدري في العالم."),
    # ── يحمي الآخرين ──
    ("others1", "والتطعيم لا يحميك وحدك، بل يحمي الآخرين أيضًا "
                "بالحدّ من انتشار الأمراض بين الناس."),
    # ── جدول التطعيم ──
    ("card1", "لذلك من المهم احترام جدول التطعيم. "
              "ففي المركز الصحي يسجّل الممرض مواعيد لقاحاتك في دفتر التطعيم، فاحتفظ به دائمًا."),
    # ── مثال محلول ──
    ("ex1", "لنطبّق مثالًا من كراسك: مدرسة فيها مائتا تلميذ، "
            "طُعّم منهم خمسون في المائة."),
    ("ex2", "فكم تلميذًا طُعّم؟ مائتان في خمسين على مائة يساوي مائة تلميذ!"),
    # ── السر ──
    ("astuce", "وإليك سرًّا: اللقاح لا يعالج المرض بعد وقوعه، بل يقي منه قبل حدوثه. "
               "فالوقاية خير من العلاج!"),
    ("outro", "والآن افتح كراسك وحلّ تمارين درس التطعيم. إلى اللقاء يا أبطال!"),
]

OUT = Path(__file__).parent / "audio_sci6"


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
