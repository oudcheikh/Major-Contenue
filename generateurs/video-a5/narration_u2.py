# -*- coding: utf-8 -*-
"""Narration U2 — الكسور. Contenu fidèle à la page U2 du cahier :
البسط/المقام · حصص متساوية · نصف/ثلث/ربع · مقارنة (نفس المقام) · piège du grand مقام."""
import asyncio, json, subprocess
from pathlib import Path

import edge_tts
import imageio_ffmpeg

VOICE = "ar-SA-HamedNeural"
RATE = "-3%"

SEGMENTS = [
    ("intro1", "أهلًا بكم من جديد يا أبطال الرياضيات! درسُ اليوم من الوحدة الثانية: الكسور."),
    ("intro2", "في هذا الدرس سنتعرف على البسط والمقام، وسنمثل الكسور بالرسم، ونقارنها."),
    # ── المفهوم ──
    ("conc1", "الكسر هو جزء من كلٍّ كامل. انظروا إلى هذا القرص الكامل."),
    ("conc2", "قسمناه إلى أربع حصص متساوية، وأخذنا حصة واحدة. هذا هو الكسر: رُبع."),
    ("conc3", "كيف يُكتب الكسر؟ في الأعلى نكتب البسط: عدد الحصص المأخوذة. "
              "وفي الأسفل نكتب المقام: عدد الحصص الكلية."),
    ("conc4", "إليكم سرًّا لطيفًا: البسط يسكن فوق الخط ويعدّ الحصص المأخوذة، "
              "والمقام يسكن تحت الخط ويعدّ الحصص كلها!"),
    # ── أشهر الكسور ──
    ("rep1", "لنتعرف الآن على أشهر الكسور: النصف، ثم الثلث، ثم الربع."),
    ("rep2", "وإذا أخذنا ثلاث حصص من أربع، حصلنا على ثلاثة أرباع."),
    ("rep3", "وإذا أخذنا الحصص كلها، أربعًا من أربع، حصلنا على الكلِّ الكامل: واحد."),
    # ── المقارنة ──
    ("comp1", "والآن، كيف نقارن كسرين لهما نفس المقام؟ أتأكد أولًا أن المقامين متساويان، "
              "ثم أقارن البسطين: صاحب البسط الأكبر هو الكسر الأكبر."),
    ("comp2", "مثال: خمسة أسباع أكبر من سُبُعَين، لأن المقامين متساويان، "
              "والبسط خمسة أكبر من البسط اثنين."),
    # ── انتبه ──
    ("att1", "انتبه جيدًا! المقام الأكبر لا يعني كسرًا أكبر."),
    ("att2", "الثُّمُن أصغر من النصف، لأننا عندما نقسم الكل إلى ثماني حصص، "
             "تصبح كل حصة صغيرة جدًا."),
    # ── السر + الختام ──
    ("astuce", "وقبل أن نفترق، إليك سرًّا صغيرًا: إذا تساوى البسطان فانظر إلى المقام: "
               "كلما كبر المقام، صغرت الحصة!"),
    ("outro", "والآن افتح كراسك وحلّ تمارين الوحدة الثانية. إلى اللقاء يا أبطال!"),
]

OUT = Path(__file__).parent / "audio_u2"


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
