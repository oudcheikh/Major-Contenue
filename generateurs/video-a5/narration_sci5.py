# -*- coding: utf-8 -*-
"""Narration Sciences 5 — الماء والصحة. Fidèle au cahier (sciences_2.py, u5_*) :
الماء أساس الحياة · الجسم 60% ماء · نشرب 1,5 لتر · أدوار الماء في الجسم ·
من المصدر إلى الكوب: أغلي أو أضف الجافيل · مثال محلول: 20 لتر، توفير 10% = 2 لتر ·
سياق موريتاني: بئر نظيفة، مياه نهر السنغال تحتاج تصفية."""
import asyncio, json, subprocess
from pathlib import Path

import edge_tts
import imageio_ffmpeg

VOICE = "ar-SA-HamedNeural"
RATE = "-3%"

SEGMENTS = [
    ("intro1", "أهلًا بكم يا أبطال العلوم! درسُ اليوم من مادة العلوم الطبيعية: "
               "الماء والصحة."),
    ("intro2", "في هذا الدرس سنعرف أهمية الماء لأجسامنا، "
               "وكيف نميّز الماء الصالح للشرب من الماء الملوّث."),
    # ── التعريف ──
    ("def1", "الماء ضروري للحياة ولعمل الجسم الجيد. "
             "فبدونه لا تعيش الكائنات الحية."),
    # ── الجسم 60% ──
    ("body1", "هل تعلم؟ يتكوّن جسم الإنسان من حوالي ستين في المائة من الماء. "
              "لذلك يُنصح بشرب لتر ونصف يوميًا."),
    # ── أدوار الماء ──
    ("role1", "للماء أدوار كثيرة: يرطّب الجسم ويزيل النفايات، "
              "وتستعمله الكلية لتصفية الدم، والمعدة لهضم الطعام."),
    # ── من المصدر إلى الكوب ──
    ("clean1", "لكن ليس كل ماء صالحًا للشرب. فماء البئر أو النهر يحتاج إلى معالجة: "
               "أغليه أو أضف إليه قطرات من الجافيل، ثم احفظه في وعاء نظيف مغطّى."),
    # ── خطر الماء الملوث ──
    ("risk1", "أما الماء الملوّث فيمكن أن ينقل أمراضًا خطيرة. "
              "لذلك نحافظ على نظافة الماء دائمًا."),
    # ── مثال محلول ──
    ("ex1", "لنطبّق مثالًا من كراسك: عائلة تستعمل عشرين لترًا يوميًا، "
            "وقرّرت أن توفّر عشرة في المائة."),
    ("ex2", "فكم لترًا توفّر؟ عشرون في عشرة على مائة يساوي لترين كل يوم!"),
    # ── السر ──
    ("astuce", "وإليك سرًّا من بلادنا: في القرية يأتي الماء الصالح من بئر نظيفة أو خزان محمي. "
               "أمّا مياه نهر السنغال فتحتاج إلى تصفية وتعقيم قبل الشرب."),
    ("outro", "والآن افتح كراسك وحلّ تمارين درس الماء والصحة. إلى اللقاء يا أبطال!"),
]

OUT = Path(__file__).parent / "audio_sci5"


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
