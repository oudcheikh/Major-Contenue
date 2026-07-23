# -*- coding: utf-8 -*-
"""Narration Sciences 4 — التلوث. Fidèle au cahier (sciences_2.py, u4_*) :
تدهور البيئة بمواد ضارة · ثلاثة أنواع: الهواء والماء والتربة · الأسباب البشرية ·
الحل: تقليل النفايات وإعادة التدوير · مثال محلول: 100 كيس، تقليل 50% = 50 ·
سياق موريتاني: نفايات نواكشوط، دخان السيارات، مياه الصرف."""
import asyncio, json, subprocess
from pathlib import Path

import edge_tts
import imageio_ffmpeg

VOICE = "ar-SA-HamedNeural"
RATE = "-3%"

SEGMENTS = [
    ("intro1", "أهلًا بكم يا أبطال العلوم! درسُ اليوم من مادة العلوم الطبيعية: "
               "التلوث."),
    ("intro2", "في هذا الدرس سنعرف ما هو التلوث، وأنواعه الثلاثة، "
               "وكيف نكافحه في محيطنا."),
    # ── التعريف ──
    ("def1", "التلوث هو تدهور البيئة بسبب مواد ضارة، "
             "وينجم عن أنشطة الإنسان مثل المصانع والسيارات والنفايات."),
    # ── الأنواع الثلاثة ──
    ("air1", "النوع الأول: تلوث الهواء. سببه دخان المصانع والسيارات، "
             "ويؤدي إلى أمراض تنفسية."),
    ("water1", "النوع الثاني: تلوث الماء. سببه الزيوت ومياه الصرف، "
               "ويؤدي إلى اختفاء الأسماك والحيوانات المائية."),
    ("soil1", "النوع الثالث: تلوث التربة. سببه النفايات والأكياس البلاستيكية "
              "التي تبقى في الأرض سنوات طويلة."),
    # ── الحل ──
    ("sol1", "أما الحل فبسيط: نقلّل النفايات، ونفرزها، ونعيد تدويرها "
             "لتصبح موادّ جديدة صالحة للاستعمال."),
    # ── مثال محلول ──
    ("ex1", "لنطبّق مثالًا من كراسك: مدرسة تستعمل مائة كيس بلاستيكي يوميًا، "
            "ثم قلّلت الاستعمال بنسبة خمسين في المائة."),
    ("ex2", "فكم كيسًا وفّرت؟ مائة في خمسين على مائة يساوي خمسين كيسًا في اليوم!"),
    # ── انتبه ──
    ("att1", "انتبه جيدًا! رمي النفايات في أيّ مكان يلوّث الماء والتربة معًا، "
             "ويضرّ بصحتنا جميعًا."),
    # ── السر ──
    ("astuce", "وإليك سرًّا: حولك أمثلة كثيرة للتلوث، مثل نفايات الأسواق في نواكشوط. "
               "لاحظها، ثم فكّر في الحل: قلّل، وافرز، وأعِد التدوير!"),
    ("outro", "والآن افتح كراسك وحلّ تمارين درس التلوث. إلى اللقاء يا أبطال!"),
]

OUT = Path(__file__).parent / "audio_sci4"


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
