# -*- coding: utf-8 -*-
"""Vidéo Sciences 6 — التطعيم (la vaccination).  Rendu : ./build_science.sh 6
Cœur : le vaccin = entraînement de l'armée de défense (bouclier + microbe),
le corps prêt bloque la maladie, la variole éradiquée, l'immunité collective,
le carnet de vaccination, puis l'exemple 200 × 50 ÷ 100 = 100 تلميذ."""
import numpy as np
from manim import (VGroup, Rectangle, RoundedRectangle, Circle, Ellipse, Polygon,
                   AnnularSector, SurroundingRectangle, Dot, Line, Arrow,
                   FadeIn, FadeOut, Write, Create, GrowFromCenter, Flash, Indicate,
                   Wiggle, LaggedStart, UP, DOWN, LEFT, RIGHT, DEGREES)

from video_common import (MajorScene, ar, num, titled, chip,
                          INK, YELL, ROSE, GREEN, BLUE, LILA, REDA, GOLD, BOUNCE, HERE)


def shield(h=2.4, col=GREEN, fill=0.9):
    """Bouclier de défense : Polygon symétrique + trait vertical + barre horizontale (croix)."""
    pts = [(-1, 1), (1, 1), (1, -0.05), (0.6, -0.85), (0, -1.35),
           (-0.6, -0.85), (-1, -0.05)]
    body = Polygon(*[[x, y, 0] for x, y in pts], fill_color=col, fill_opacity=fill,
                   stroke_color=INK, stroke_width=3)
    v = Line([0, 0.75, 0], [0, -1.0, 0], color="#FFFFFF", stroke_width=5)
    hbar = Line([-0.55, 0.2, 0], [0.55, 0.2, 0], color="#FFFFFF", stroke_width=5)
    g = VGroup(body, v, hbar)
    g.scale_to_fit_height(h)
    return g


def microbe(r=0.55, col=LILA):
    """Microbe : disque + pointes radiales + deux yeux menaçants."""
    body = Circle(radius=r, fill_color=col, fill_opacity=0.92, stroke_color=INK,
                  stroke_width=2.5)
    spikes = VGroup()
    for k in range(10):
        a = k * 36 * DEGREES
        d = np.array([np.cos(a), np.sin(a), 0])
        sp = Line(d * r, d * (r + 0.22), color=INK, stroke_width=3)
        tip = Dot(d * (r + 0.24), radius=0.05, color=col)
        spikes.add(sp, tip)
    eyes = VGroup(
        Dot([-0.18 * r / 0.55, 0.12, 0], radius=0.07, color=INK),
        Dot([0.18 * r / 0.55, 0.12, 0], radius=0.07, color=INK),
    )
    mouth = Line([-0.16, -0.16, 0], [0.16, -0.16, 0], color=INK, stroke_width=3)
    return VGroup(body, spikes, eyes, mouth)


def check(col=GREEN, s=1.0):
    """Coche verte."""
    g = VGroup(
        Line([-0.18, 0.02, 0], [-0.04, -0.16, 0], color=col, stroke_width=6),
        Line([-0.04, -0.16, 0], [0.22, 0.22, 0], color=col, stroke_width=6),
    )
    return g.scale(s)


def person(col=BLUE, h=1.2):
    """Petite silhouette : tête + corps."""
    head = Circle(radius=0.22, fill_color=col, fill_opacity=1, stroke_color=INK,
                  stroke_width=2)
    body = Polygon([-0.28, -0.15, 0], [0.28, -0.15, 0], [0.2, -0.9, 0], [-0.2, -0.9, 0],
                   fill_color=col, fill_opacity=1, stroke_color=INK, stroke_width=2)
    head.move_to([0, 0.15, 0])
    g = VGroup(body, head)
    g.scale_to_fit_height(h)
    return g


class VideoSci6(MajorScene):
    AUDIO = HERE / "audio_sci6"
    UNIT_AR = "علوم · درس 6"
    UNIT_COLOR = GREEN
    TITLE = "التطعيم"
    OUTRO_CALL = "والآن افتح كراسك وحلّ تمارين درس التطعيم"

    # ── 2. التعريف ──────────────────────────────────────────────
    def s_def(self):
        d = self.seg("def1")
        head = titled("ما هو التطعيم؟", 34, GREEN)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        box = RoundedRectangle(corner_radius=0.28, width=11.6, height=2.2,
                               fill_color=GREEN, fill_opacity=0.14,
                               stroke_color=GREEN, stroke_width=3).move_to(UP * 0.35)
        t = ar("حماية الجسم من الأمراض بواسطة اللقاحات", 32, "BOLD", INK
               ).move_to(box.get_center() + UP * 0.42)
        t2 = ar("واللقاح يهيّئ الجهاز المناعي للدفاع", 32, "BOLD", GREEN
                ).move_to(box.get_center() + DOWN * 0.42)
        self.sfx("ding")
        self.play(GrowFromCenter(box, rate_func=BOUNCE), Write(t), run_time=1.4)
        self.play(FadeIn(t2, shift=UP * 0.3), run_time=1.0)
        self.wait(max(d - 3.3, 0.2))
        self.clear_all()

    # ── 3. اللقاح = تدريب لجيش الدفاع ────────────────────────────
    def s_train(self):
        d = self.seg("train1")
        head = titled("اللقاح تدريبٌ لجيش الدفاع", 34, GREEN)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        sh = shield(2.6, GREEN).move_to([3.3, 0.4, 0])
        mi = microbe(0.55, LILA).move_to([-3.6, 0.7, 0])
        mlab = ar("جزء ضعيف من الميكروب", 24, "BOLD", LILA).next_to(mi, DOWN, buff=0.35)
        self.sfx("pop")
        self.play(FadeIn(mi, scale=0.4, rate_func=BOUNCE), FadeIn(mlab), run_time=0.9)
        arrow = Arrow([-1.9, 0.5, 0], [1.4, 0.5, 0], color=INK, stroke_width=6,
                      max_tip_length_to_length_ratio=0.12)
        self.sfx("whoosh")
        self.play(Create(arrow), run_time=0.7)
        self.sfx("ding")
        self.play(GrowFromCenter(sh, rate_func=BOUNCE), run_time=1.0)
        made = RoundedRectangle(corner_radius=0.22, width=8.6, height=1.05,
                                fill_color=GREEN, fill_opacity=0.92, stroke_color=INK,
                                stroke_width=2.5).move_to(DOWN * 2.35)
        made_t = ar("فيصنع الجسم أجسامًا مضادة للدفاع", 28, "BOLD", "#FFFFFF").move_to(made)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(made, made_t), rate_func=BOUNCE), run_time=1.0)
        self.wait(max(d - 5.4, 0.2))
        self.clear_all()

    # ── 4. الجسم مستعدّ ─────────────────────────────────────────
    def s_ready(self):
        d = self.seg("train2")
        head = titled("إذا جاء المرض، الجسم مستعدّ!", 34, ROSE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        sh = shield(2.7, GREEN).move_to([1.6, -0.2, 0])
        self.play(FadeIn(sh, shift=LEFT * 0.3, rate_func=BOUNCE), run_time=0.7)
        mi = microbe(0.55, REDA).move_to([-4.6, -0.1, 0])
        self.sfx("pop")
        self.play(FadeIn(mi, scale=0.4), run_time=0.5)
        # le microbe fonce sur le bouclier
        self.sfx("whoosh")
        self.play(mi.animate.move_to([-0.5, -0.15, 0]), run_time=0.8)
        # le bouclier bloque : Flash + microbe repoussé
        self.sfx("boing")
        self.play(Flash(sh, color=GREEN, flash_radius=2.1, line_length=0.5), run_time=0.7)
        self.play(mi.animate.move_to([-5.3, 1.4, 0]).scale(0.7).set_opacity(0.5),
                  Wiggle(sh), run_time=0.8)
        tag = ar("الجسم محميّ!", 32, "BOLD", GREEN).move_to(DOWN * 2.5)
        self.sfx("tada")
        self.play(FadeIn(tag, scale=0.6, rate_func=BOUNCE), run_time=0.7)
        self.wait(max(d - 5.1, 0.2))
        self.clear_all()

    # ── 5. الفائدة : أمراض خطيرة + الجدري ───────────────────────
    def s_use(self):
        d = self.seg("use1")
        head = titled("اللقاح يقينا أمراضًا خطيرة", 34, BLUE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        maladies = [("الحصبة", ROSE), ("شلل الأطفال", BLUE)]
        pills = VGroup()
        for lab, col in maladies:
            p = RoundedRectangle(corner_radius=0.35, width=4.2, height=1.2,
                                 fill_color=col, fill_opacity=0.92,
                                 stroke_color=INK, stroke_width=2.5)
            pt = ar(lab, 30, "BOLD", "#FFFFFF").move_to(p)
            pills.add(VGroup(p, pt))
        pills.arrange(LEFT, buff=0.7).move_to(UP * 1.1)
        for p in pills:
            self.sfx("pop")
            self.play(FadeIn(p, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.7)
        # carte الجدري éradiquée
        card = RoundedRectangle(corner_radius=0.25, width=6.4, height=1.7,
                                fill_color=GREEN, fill_opacity=0.16,
                                stroke_color=GREEN, stroke_width=3).move_to(DOWN * 1.35)
        cname = ar("الجدري", 40, "BOLD", INK).move_to(card.get_center() + LEFT * 1.7)
        cross = VGroup(
            Line([-0.9, 0.35, 0], [0.9, -0.35, 0], color=REDA, stroke_width=7),
        ).move_to(cname)
        ck = check(GREEN, 1.6).move_to(card.get_center() + RIGHT * 1.8)
        sub = ar("قُضي عليه نهائيًا", 26, "BOLD", GREEN).move_to(DOWN * 2.6)
        self.sfx("ding")
        self.play(GrowFromCenter(card, rate_func=BOUNCE), FadeIn(cname), run_time=1.0)
        self.sfx("boing")
        self.play(Create(cross), Create(ck), run_time=0.8)
        self.play(FadeIn(sub, shift=UP * 0.3), run_time=0.7)
        self.wait(max(d - 5.5, 0.2))
        self.clear_all()

    # ── 6. يحمي الآخرين (المناعة الجماعية) ──────────────────────
    def s_others(self):
        d = self.seg("others1")
        head = titled("التطعيم يحمي الآخرين أيضًا", 34, LILA)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        cols = [BLUE, ROSE, YELL, GREEN, REDA]
        people = VGroup(*[person(c, 1.25) for c in cols]).arrange(LEFT, buff=0.55)
        people.move_to(DOWN * 1.4)
        # grand bouclier / dôme protecteur au-dessus
        dome = AnnularSector(inner_radius=3.05, outer_radius=3.35, angle=180 * DEGREES,
                             start_angle=0, fill_color=GREEN, fill_opacity=0.9,
                             stroke_color=INK, stroke_width=2.5)
        dome.move_to([0, -0.45, 0])       # bbox-centre → arche au-dessus des silhouettes
        for p in people:
            self.sfx("pop")
            self.play(FadeIn(p, shift=UP * 0.3, rate_func=BOUNCE), run_time=0.45)
        self.sfx("whoosh")
        self.play(Create(dome), run_time=1.1)
        tag = ar("مناعة جماعية تحمي الجميع", 28, "BOLD", GREEN).move_to(UP * 1.55)
        self.sfx("ding")
        self.play(FadeIn(tag, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.8)
        self.wait(max(d - 5.2, 0.2))
        self.clear_all()

    # ── 7. دفتر التطعيم ─────────────────────────────────────────
    def s_card(self):
        d = self.seg("card1")
        head = titled("دفتر التطعيم", 34, BLUE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        book = RoundedRectangle(corner_radius=0.2, width=6.6, height=4.2,
                                fill_color="#FFFFFF", fill_opacity=1,
                                stroke_color=BLUE, stroke_width=4).move_to([-1.4, -0.25, 0])
        band = Rectangle(width=6.6, height=0.85, fill_color=BLUE, fill_opacity=0.92,
                         stroke_width=0).move_to(book.get_top() + DOWN * 0.42)
        band_t = ar("مواعيد اللقاحات", 26, "BOLD", "#FFFFFF").move_to(band)
        self.sfx("ding")
        self.play(GrowFromCenter(VGroup(book, band, band_t), rate_func=BOUNCE), run_time=1.1)
        dates = ["الشهر ٢", "الشهر ٤", "الشهر ٩", "السنة ١"]
        rows = VGroup()
        for i, dt in enumerate(dates):
            y = 0.7 - i * 0.78
            line = Line([-4.3, y - 0.28, 0], [1.5, y - 0.28, 0], color="#D8D8D8",
                        stroke_width=2)
            dtx = ar(dt, 24, "BOLD", INK).move_to([0.4, y, 0])
            ck = check(GREEN, 1.2).move_to([-3.7, y, 0])
            rows.add(VGroup(line, dtx, ck))
        t = 0
        for r in rows:
            self.sfx("pop")
            self.play(FadeIn(r, shift=LEFT * 0.3, rate_func=BOUNCE), run_time=0.6)
            t += 0.6
        note = RoundedRectangle(corner_radius=0.22, width=3.9, height=1.5,
                                fill_color=GOLD, fill_opacity=0.95, stroke_color=INK,
                                stroke_width=2.5).move_to([4.2, -0.3, 0])
        note_t = ar("احتفظ به\nدائمًا", 30, "BOLD", "#FFFFFF").move_to(note)
        self.sfx("boing")
        self.play(GrowFromCenter(VGroup(note, note_t), rate_func=BOUNCE), run_time=0.9)
        self.wait(max(d - t - 2.9, 0.2))
        self.clear_all()

    # ── 8. مثال محلول ───────────────────────────────────────────
    def s_example(self):
        d = self.seg("ex1")
        head = titled("مثال محلول من كراسك", 32, GOLD)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        # école
        school = VGroup(
            Rectangle(width=3.0, height=1.7, fill_color=YELL, fill_opacity=0.9,
                      stroke_color=INK, stroke_width=2.5),
            Polygon([-1.7, 0.85, 0], [1.7, 0.85, 0], [0, 1.9, 0],
                    fill_color=ROSE, fill_opacity=0.9, stroke_color=INK, stroke_width=2.5),
            Rectangle(width=0.7, height=0.9, fill_color=BLUE, fill_opacity=0.85,
                      stroke_color=INK, stroke_width=2).shift(DOWN * 0.4),
        ).move_to([-3.6, 0.3, 0])
        s_val = VGroup(num("200", 44, INK), ar("تلميذ", 26, "BOLD", INK)
                       ).arrange(LEFT, buff=0.25).next_to(school, DOWN, buff=0.4)
        self.sfx("pop")
        self.play(FadeIn(school, scale=0.5, rate_func=BOUNCE), FadeIn(s_val), run_time=1.0)
        pctbox = RoundedRectangle(corner_radius=0.25, width=5.2, height=1.7, fill_color=GREEN,
                                  fill_opacity=0.16, stroke_color=GREEN, stroke_width=3)
        pt = VGroup(ar("طُعّم منهم", 30, "BOLD", INK), num("50%", 48, GREEN)
                    ).arrange(LEFT, buff=0.35).move_to(pctbox)
        pct = VGroup(pctbox, pt).move_to([2.6, 0.3, 0])
        self.sfx("ding")
        self.play(GrowFromCenter(pct, rate_func=BOUNCE), run_time=1.0)
        givens = VGroup(school, s_val, pct)
        self.wait(max(d - 2.9, 0.2))

        d = self.seg("ex2")
        self.play(FadeOut(givens, shift=DOWN * 0.3), run_time=0.6)
        q = ar("كم تلميذًا طُعّم؟", 30, "BOLD", GOLD).move_to(UP * 1.6)
        self.play(FadeIn(q, shift=DOWN * 0.2), run_time=0.6)
        calc = VGroup(num("200", 44), num("×", 36, GOLD), num("50", 44),
                      num("÷", 36, GOLD), num("100", 44),
                      num("=", 40), num("100", 56, GREEN)).arrange(LEFT, buff=0.28)
        calc.move_to(DOWN * 0.1)
        box = SurroundingRectangle(calc, color=GREEN, corner_radius=0.15, buff=0.3)
        self.sfx("ding")
        self.play(FadeIn(calc, shift=UP * 0.3), Create(box), run_time=1.1)
        self.play(Flash(calc[6], color=GREEN, flash_radius=1.3), run_time=0.8)
        res = VGroup(num("100", 44, GREEN), ar("تلميذ مُطعَّم", 30, "BOLD", ROSE)
                     ).arrange(LEFT, buff=0.3).move_to(DOWN * 2.2)
        self.sfx("tada")
        self.play(FadeIn(res, scale=0.6, rate_func=BOUNCE), run_time=0.9)
        self.wait(max(d - 4.0, 0.2))
        self.clear_all()

    # ── 9. سرّ : الوقاية خير من العلاج ──────────────────────────
    def s_astuce(self):
        d = self.seg("astuce")
        head = titled("الوقاية خير من العلاج", 34, GOLD)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        box = RoundedRectangle(corner_radius=0.28, width=11.0, height=1.7,
                               fill_color=GOLD, fill_opacity=0.16,
                               stroke_color=GOLD, stroke_width=3).move_to(UP * 0.55)
        t = ar("اللقاح يقي قبل المرض، ولا يعالج بعده", 32, "BOLD", INK).move_to(box)
        self.sfx("ding")
        self.play(GrowFromCenter(box, rate_func=BOUNCE), Write(t), run_time=1.4)
        chips_row = VGroup()
        for lab, col in [("يقي قبله", GREEN), ("لا يعالج بعده", REDA)]:
            p = RoundedRectangle(corner_radius=0.3, width=4.4, height=1.15,
                                 fill_color=col, fill_opacity=0.92, stroke_color=INK,
                                 stroke_width=2.5)
            pt = ar(lab, 28, "BOLD", "#FFFFFF").move_to(p)
            chips_row.add(VGroup(p, pt))
        chips_row.arrange(LEFT, buff=0.7).move_to(DOWN * 1.5)
        for c in chips_row:
            self.sfx("pop")
            self.play(FadeIn(c, shift=UP * 0.3, rate_func=BOUNCE), run_time=0.7)
        self.wait(max(d - 3.8, 0.2))
        self.clear_all()

    def construct(self):
        self.setup_common()
        self.s_intro_card("intro1")
        self.s_objectifs("intro2", [
            "أعرّف التطعيم واللقاح",
            "أشرح كيف يحمي اللقاح الجسم",
            "أعرف أهمية جدول التطعيم",
        ])
        self.s_def()
        self.s_train()
        self.s_ready()
        self.s_use()
        self.s_others()
        self.s_card()
        self.s_example()
        self.s_astuce()
        self.s_outro_end("outro")
