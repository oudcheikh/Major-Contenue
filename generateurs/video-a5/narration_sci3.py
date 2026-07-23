# -*- coding: utf-8 -*-
"""Narration Sciences 3 — التصحر. Fidèle au cahier (sciences_1.py, s3_*) :
تحول الأرض الخصبة إلى جافة · الأسباب: جفاف، إزالة الغابات، الرعي الجائر ·
العواقب: فقدان الغطاء النباتي ونقص الغذاء · الحلول: الحزام الأخضر ·
سياق موريتاني: زحف الرمال على نواكشوط وآدرار، السور الأخضر الكبير."""
import asyncio, json, subprocess
from pathlib import Path

import edge_tts
import imageio_ffmpeg

VOICE = "ar-SA-HamedNeural"
RATE = "-3%"

SEGMENTS = [
    ("intro1", "أهلًا بكم يا أبطال العلوم! درسُ اليوم من مادة العلوم الطبيعية: "
               "التصحر."),
    ("intro2", "في هذا الدرس سنعرف ما هو التصحر، وما أسبابه وعواقبه، "
               "وكيف نكافح زحف الرمال في بلادنا."),
    # ── التعريف ──
    ("def1", "التصحر هو تحوّل الأراضي الخصبة إلى أراضٍ جافة وفقيرة، "
             "تشبه في الغالب الصحراء."),
    # ── الأسباب ──
    ("cause1", "من أسبابه: الجفاف وندرة الأمطار، وأنشطة الإنسان مثل إزالة الغابات "
               "والرعي الجائر."),
    # ── العواقب ──
    ("effect1", "ويؤدي التصحر إلى فقدان الغطاء النباتي، وتراجع الإنتاج الزراعي، "
                "ونقص الغذاء والماء عند السكان."),
    # ── سياق موريتاني ──
    ("mr1", "والتصحر يمسّ حياتنا في موريتانيا: زحف الرمال على البيوت والطرق في نواكشوط وآدرار، "
            "وتراجع المراعي والواحات."),
    # ── الحلول ──
    ("sol1", "لمكافحته: نحمي التربة، ونزرع الأشجار، ونستعمل الماء بشكل عقلاني."),
    ("sol2", "فالحزام الأخضر من الأشجار يكسر قوة الرياح، وجذوره تثبّت التربة، "
             "فيوقف زحف الرمال ويحمي القرية."),
    # ── مثال محلول ──
    ("ex1", "لنطبّق مثالًا من كراسك: غطاء نباتي كان يغطي أربعين في المائة، "
            "ثم أصبح خمسة وعشرين في المائة."),
    ("ex2", "فكم انخفض؟ أربعون ناقص خمسة وعشرين يساوي خمسة عشر في المائة!"),
    # ── السر ──
    ("astuce", "وإليك سرًّا: مشروع السور الأخضر الكبير يمرّ عبر موريتانيا "
               "ليوقف زحف الرمال. ومدرستك يمكنها المشاركة بزرع الأشجار!"),
    ("outro", "والآن افتح كراسك وحلّ تمارين درس التصحر. إلى اللقاء يا أبطال!"),
]

OUT = Path(__file__).parent / "audio_sci3"


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
