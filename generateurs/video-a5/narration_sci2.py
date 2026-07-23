# -*- coding: utf-8 -*-
"""Narration Sciences 2 — التوازن الطاقوي. Fidèle au cahier (sciences_1.py, s2_*) :
الطاقة تدخل بالأكل وتخرج بالنشاط · الكفّتان · فائض ← وزن، نقص ← تعب ·
مثال محلول: ساعة رياضة = 300 kcal، ساعتان = 600 · الجري والمشي ينفقان الطاقة."""
import asyncio, json, subprocess
from pathlib import Path

import edge_tts
import imageio_ffmpeg

VOICE = "ar-SA-HamedNeural"
RATE = "-3%"

SEGMENTS = [
    ("intro1", "أهلًا بكم يا أبطال العلوم! درسُ اليوم من مادة العلوم الطبيعية: "
               "التوازن الطاقوي."),
    ("intro2", "في هذا الدرس سنفهم العلاقة بين الطاقة التي نأكلها والطاقة التي ينفقها جسمنا."),
    # ── التعريف ──
    ("def1", "التوازن الطاقوي هو العلاقة بين الطاقة التي نأخذها من الطعام، "
             "والطاقة التي ينفقها الجسم في الحركة."),
    # ── من أين وإلى أين ──
    ("io1", "الطاقة تدخل جسمنا من الأغذية والمشروبات. "
            "ويستعملها الجسم في التنفس والحركة والتفكير."),
    # ── الكفّتان ──
    ("bal1", "تخيّل ميزانًا بكفّتين: كفّة لما نأكل، وكفّة لما ننفق. "
             "إذا تساوت الكفّتان بقي الوزن ثابتًا والجسم في صحة جيدة."),
    # ── فائض / نقص ──
    ("case1", "فإذا أكلنا أكثر مما ننفق، اكتسبنا وزنًا زائدًا وقد نصاب بأمراض. "
              "وإذا أكلنا أقل مما ننفق، نقص وزننا وشعرنا بالتعب."),
    # ── مثال محلول ──
    ("ex1", "لنطبّق مثالًا من كراسك: ساعة واحدة من الرياضة تنفق ثلاثمائة سعرة حرارية."),
    ("ex2", "فكم تنفق ساعتان؟ اثنان في ثلاثمائة يساوي ستمائة سعرة حرارية!"),
    # ── انتبه ──
    ("att1", "انتبه جيدًا! الجلوس الطويل أمام الشاشات مع الأكل الكثير "
             "يكسر التوازن الطاقوي."),
    # ── السر ──
    ("astuce", "وإليك سرًّا: الجري واللعب في الساحة والسباحة والمشي إلى المدرسة، "
               "كلها أنشطة تنفق الطاقة وتحافظ على توازنك!"),
    ("outro", "والآن افتح كراسك وحلّ تمارين التوازن الطاقوي. إلى اللقاء يا أبطال!"),
]

OUT = Path(__file__).parent / "audio_sci2"


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
