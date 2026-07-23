# -*- coding: utf-8 -*-
"""Narration U4 — الضرب. Fidèle au cahier :
جمع متكرر · عاملان وجداء · 4×3=3×4 · جداول الضرب حتى 12 · الضرب العمودي · سر جدول 9."""
import asyncio, json, subprocess
from pathlib import Path

import edge_tts
import imageio_ffmpeg

VOICE = "ar-SA-HamedNeural"
RATE = "-3%"

SEGMENTS = [
    ("intro1", "أهلًا بكم يا أبطال الرياضيات! درسُ اليوم من الوحدة الرابعة: الضرب."),
    ("intro2", "في هذا الدرس سنفهم الضرب على أنه جمع متكرر، وسنتعلم وضع الضرب عموديًا وإنجازه دون خطأ."),
    # ── المفهوم : جمع متكرر ──
    ("conc1", "الضرب يُستعمل لجمع نفس العدد عدة مرات. انظروا إلى هذه الأصداف."),
    ("conc2", "عندنا أربع مجموعات، في كل مجموعة ثلاث أصداف: "
              "ثلاثة زائد ثلاثة زائد ثلاثة زائد ثلاثة: اثنا عشر."),
    ("conc3", "بدل هذا الجمع الطويل، نكتب ببساطة: أربعة في ثلاثة يساوي اثني عشر. "
              "الضرب جمع متكرر!"),
    ("conc4", "العددان المضروبان يسميان: عاملين. والنتيجة تسمى: الجداء."),
    # ── الخاصية ──
    ("comm1", "وإليكم خاصية جميلة: يمكن تغيير ترتيب العاملين دون أن يتغير الجداء: "
              "أربعة في ثلاثة يساوي ثلاثة في أربعة."),
    ("tab1", "ولكي تصبح بطلًا في الضرب، احفظ جداول الضرب من واحد إلى اثني عشر عن ظهر قلب!"),
    # ── الضرب العمودي : 234 × 3 ──
    ("mult1", "والآن، الضرب العمودي. لنضرب معًا مئتين وأربعة وثلاثين في ثلاثة."),
    ("mult2", "أبدأ من الآحاد: ثلاثة في أربعة: اثنا عشر. أكتب اثنين، وأحتفظ بواحد."),
    ("mult3", "في العشرات: ثلاثة في ثلاثة: تسعة، زائد الاحتفاظ واحد: عشرة. "
              "أكتب صفرًا، وأحتفظ بواحد."),
    ("mult4", "في المئات: ثلاثة في اثنين: ستة، زائد الاحتفاظ واحد: سبعة. "
              "فالجداء هو: سبعمائة واثنان."),
    # ── السر : جدول 9 ──
    ("astuce", "وقبل أن نفترق، إليك سرّ جدول التسعة: مجموع رقمي النتيجة يساوي دائمًا تسعة! "
               "ثمانية عشر: واحد زائد ثمانية: تسعة. وسبعة وعشرون: اثنان زائد سبعة: تسعة. جرّب بنفسك!"),
    ("outro", "والآن افتح كراسك وحلّ تمارين الوحدة الرابعة. إلى اللقاء يا أبطال!"),
]

OUT = Path(__file__).parent / "audio_u4"


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
