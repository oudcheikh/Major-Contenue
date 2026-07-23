# -*- coding: utf-8 -*-
"""Vidéo Sciences 5 — الماء والصحة.  Rendu : ./build_science.sh 5
Cœur : الماء ضروري للحياة · الجسم 60% ماء (بيشر) · أدوار الماء الثلاثة ·
من المصدر إلى الكوب (سلسلة) · خطر الماء الملوّث · مثال: توفير 10% من 20 لتر = 2 ·
سرّ موريتاني: بئر نظيفة صالحة مقابل مياه نهر السنغال تحتاج تصفية."""
import numpy as np
from manim import (VGroup, Rectangle, RoundedRectangle, Circle, Ellipse, Polygon,
                   AnnularSector, SurroundingRectangle, Dot, Line,
                   FadeIn, FadeOut, Write, Create, GrowFromCenter, Flash, Indicate,
                   Wiggle, LaggedStart, UP, DOWN, LEFT, RIGHT, DEGREES)

from video_common import (MajorScene, ar, num, titled, chip,
                          INK, YELL, ROSE, GREEN, BLUE, LILA, REDA, GOLD, BOUNCE, HERE)


def water_drop(scale=1.0, col=BLUE, opacity=0.6):
    """قطرة ماء : دائرة + مثلث علوي."""
    return VGroup(
        Circle(radius=0.45 * scale, fill_color=col, fill_opacity=opacity,
               stroke_color=INK, stroke_width=2.5),
        Polygon([-0.28 * scale, 0.32 * scale, 0], [0.28 * scale, 0.32 * scale, 0],
                [0, 0.95 * scale, 0], fill_color=col, fill_opacity=opacity,
                stroke_color=INK, stroke_width=2.5),
    )


def flow_card(label, col, w=2.85, h=1.35):
    """بطاقة مستديرة لسلسلة المعالجة."""
    box = RoundedRectangle(corner_radius=0.2, width=w, height=h,
                           fill_color=col, fill_opacity=0.92,
                           stroke_color=INK, stroke_width=2.5)
    t = ar(label, 24, "BOLD", "#FFFFFF")
    if t.width > w - 0.4:
        t.scale_to_fit_width(w - 0.4)
    t.move_to(box)
    return VGroup(box, t)


class VideoSci5(MajorScene):
    AUDIO = HERE / "audio_sci5"
    UNIT_AR = "علوم · درس 5"
    UNIT_COLOR = LILA
    TITLE = "الماء والصحة"
    OUTRO_CALL = "والآن افتح كراسك وحلّ تمارين درس الماء والصحة"

    # ── 2. التعريف ──────────────────────────────────────────────
    def s_def(self):
        d = self.seg("def1")
        box = RoundedRectangle(corner_radius=0.28, width=11.4, height=2.0,
                               fill_color=BLUE, fill_opacity=0.14,
                               stroke_color=BLUE, stroke_width=3).move_to(UP * 0.35)
        head = titled("لماذا الماء مهمّ؟", 34, BLUE)
        t = ar("الماء ضروري للحياة", 34, "BOLD", INK).move_to(box.get_center() + UP * 0.35)
        t2 = ar("ولعمل الجسم الجيّد", 34, "BOLD", BLUE).move_to(box.get_center() + DOWN * 0.4)
        drop = water_drop(0.8).move_to([-4.9, 0.35, 0])
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        self.sfx("ding")
        self.play(GrowFromCenter(box, rate_func=BOUNCE), Write(t), run_time=1.3)
        self.play(FadeIn(t2, shift=UP * 0.3),
                  FadeIn(drop, scale=0.4, rate_func=BOUNCE), run_time=0.9)
        self.wait(max(d - 3.1, 0.2))
        self.clear_all()

    # ── 3. الجسم 60% ماء ────────────────────────────────────────
    def s_body(self):
        d = self.seg("body1")
        head = titled("جسمنا ماء في معظمه", 34, BLUE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        # بيشر / كأس مدرّج
        bw, bh = 2.4, 3.2
        cx, cy = 3.4, -0.55
        glass = Rectangle(width=bw, height=bh, stroke_color=INK, stroke_width=3.5,
                          fill_opacity=0).move_to([cx, cy, 0])
        fillh = bh * 0.60
        water = Rectangle(width=bw - 0.12, height=fillh, fill_color=BLUE, fill_opacity=0.55,
                          stroke_width=0)
        water.move_to([cx, cy - bh / 2 + fillh / 2, 0])
        pct = num("60%", 46, "#1c5a8f")
        pct.move_to([cx, cy - bh / 2 + fillh / 2, 0])
        line60 = Line([cx - bw / 2 - 0.35, cy - bh / 2 + fillh, 0],
                      [cx + bw / 2 + 0.35, cy - bh / 2 + fillh, 0],
                      color=REDA, stroke_width=3)
        self.sfx("ding")
        self.play(Create(glass), run_time=0.8)
        self.sfx("whoosh")
        self.play(GrowFromCenter(water, rate_func=BOUNCE), FadeIn(pct),
                  Create(line60), run_time=1.2)
        # texte
        info = ar("جسم الإنسان حوالي 60% ماء", 30, "BOLD", INK).move_to([-2.6, 0.85, 0])
        drop = water_drop(0.7).move_to([-4.9, -1.3, 0])
        lab = ar("نشرب 1,5 لتر يوميًا", 30, "BOLD", BLUE).move_to([-2.2, -1.3, 0])
        self.sfx("pop")
        self.play(FadeIn(info, shift=LEFT * 0.3, rate_func=BOUNCE), run_time=0.9)
        self.sfx("pop")
        self.play(FadeIn(drop, scale=0.4, rate_func=BOUNCE),
                  FadeIn(lab, shift=LEFT * 0.3), run_time=0.9)
        self.wait(max(d - 4.7, 0.2))
        self.clear_all()

    # ── 4. أدوار الماء الثلاثة ──────────────────────────────────
    def s_roles(self):
        d = self.seg("role1")
        head = titled("للماء أدوار في الجسم", 34, GREEN)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        roles = [("يرطّب الجسم ويزيل النفايات", BLUE),
                 ("الكلية تصفّي الدم", ROSE),
                 ("المعدة تهضم الطعام", GREEN)]
        cards = VGroup()
        for i, (lab, col) in enumerate(roles):
            box = RoundedRectangle(corner_radius=0.22, width=8.4, height=1.15,
                                   fill_color=col, fill_opacity=0.92,
                                   stroke_color=INK, stroke_width=2.5)
            dot = Circle(radius=0.2, fill_color="#FFFFFF", fill_opacity=1,
                         stroke_color=INK, stroke_width=1.5).move_to(box.get_right() + LEFT * 0.5)
            n = num(str(i + 1), 26, col).move_to(dot)
            t = ar(lab, 28, "BOLD", "#FFFFFF")
            if t.width > 6.6:
                t.scale_to_fit_width(6.6)
            t.move_to(box.get_center() + LEFT * 0.4)
            cards.add(VGroup(box, t, dot, n).move_to([-0.4, 1.35 - i * 1.4, 0]))
        t = 0
        for c in cards:
            self.sfx("ding")
            self.play(GrowFromCenter(c, rate_func=BOUNCE), run_time=0.8)
            t += 0.8
        self.wait(max(d - t - 0.9, 0.2))
        self.clear_all()

    # ── 5. من المصدر إلى الكوب ──────────────────────────────────
    def s_clean(self):
        d = self.seg("clean1")
        head = titled("من المصدر إلى الكوب", 34, LILA)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        steps = [("ماء البئر", REDA),
                 ("أغليه أو أضف الجافيل", YELL),
                 ("وعاء نظيف مغطّى", BLUE),
                 ("ماء صالح للشرب", GREEN)]
        # 2 rangées de 2, sens RTL : بئر en haut-droite → معالجة → وعاء → صالح
        pos = [(2.4, 0.85), (-1.7, 0.85), (-1.7, -1.5), (2.4, -1.5)]
        cards = [flow_card(lab, col).move_to([x, y, 0])
                 for (lab, col), (x, y) in zip(steps, pos)]
        arrows = [
            num("←", 48, INK).move_to([0.35, 0.85, 0]),   # بئر → معالجة
            num("↓", 48, INK).move_to([-1.7, -0.32, 0]),  # معالجة → وعاء
            num("→", 48, INK).move_to([0.35, -1.5, 0]),   # وعاء → صالح
        ]
        seq = [cards[0], arrows[0], cards[1], arrows[1], cards[2], arrows[2], cards[3]]
        t = 0
        for m in seq:
            self.sfx("pop")
            self.play(FadeIn(m, scale=0.6, rate_func=BOUNCE), run_time=0.7)
            t += 0.7
        self.play(Indicate(cards[3], color=GREEN, scale_factor=1.15), run_time=0.9)
        t += 0.9
        self.wait(max(d - t - 0.9, 0.2))
        self.clear_all()

    # ── 6. خطر الماء الملوث ─────────────────────────────────────
    def s_risk(self):
        d = self.seg("risk1")
        head = titled("انتبه! الماء الملوّث", 34, REDA)
        garcon = self.boy(1.9).to_edge(LEFT, buff=0.3).shift(DOWN * 1.3)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE),
                  FadeIn(garcon, shift=RIGHT * 0.8, rate_func=BOUNCE), run_time=1.0)
        # panneau d'avertissement (triangle)
        tri = Polygon([0, 1.15, 0], [-1.0, -0.6, 0], [1.0, -0.6, 0],
                      fill_color=REDA, fill_opacity=0.92, stroke_color=INK,
                      stroke_width=3).move_to([2.4, 0.55, 0])
        bang = num("!", 60, "#FFFFFF").move_to(tri.get_center() + DOWN * 0.05)
        card = RoundedRectangle(corner_radius=0.22, width=8.0, height=1.25, fill_color=ROSE,
                                fill_opacity=0.92, stroke_color=INK,
                                stroke_width=2.5).move_to([0.9, -1.6, 0])
        ct = ar("الماء الملوّث ينقل أمراضًا خطيرة", 30, "BOLD", "#FFFFFF").move_to(card)
        self.sfx("boing")
        self.play(GrowFromCenter(VGroup(tri, bang), rate_func=BOUNCE), run_time=1.0)
        self.sfx("ding")
        self.play(GrowFromCenter(VGroup(card, ct), rate_func=BOUNCE), run_time=0.9)
        self.play(Wiggle(garcon), run_time=1.1)
        self.wait(max(d - 4.0, 0.2))
        self.clear_all()

    # ── 7. مثال محلول : توفير 10% ───────────────────────────────
    def s_example(self):
        d = self.seg("ex1")
        head = titled("مثال محلول: نوفّر الماء", 32, GOLD)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        drop = water_drop(1.3, BLUE, 0.5).move_to([-3.8, 0.35, 0])
        v20 = VGroup(num("20", 46, BLUE), ar("لترًا", 26, "BOLD", BLUE)
                     ).arrange(LEFT, buff=0.25).next_to(drop, DOWN, buff=0.4)
        cap = ar("عائلة تستعمل كل يوم", 28, "BOLD", INK).next_to(drop, UP, buff=0.5)
        save = ar("وتريد أن توفّر 10%", 30, "BOLD", GREEN).move_to([2.4, -0.2, 0])
        sbox = SurroundingRectangle(save, color=GREEN, corner_radius=0.15, buff=0.28)
        self.sfx("pop")
        self.play(FadeIn(drop, scale=0.5, rate_func=BOUNCE), FadeIn(v20),
                  FadeIn(cap, shift=DOWN * 0.2), run_time=1.0)
        self.sfx("ding")
        self.play(Create(sbox), FadeIn(save), run_time=1.0)
        self.wait(max(d - 2.9, 0.2))

        d = self.seg("ex2")
        self.clear_all()
        head2 = titled("كم لترًا نوفّر؟", 32, GOLD)
        self.sfx("pop")
        self.play(FadeIn(head2, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        calc = VGroup(num("20", 46, BLUE), num("×", 34, GOLD), num("10", 46),
                      num("÷", 34, GOLD), num("100", 46), num("=", 38),
                      num("2", 54, GREEN)).arrange(LEFT, buff=0.28)
        unit = ar("لتر", 30, "BOLD", GREEN)
        row = VGroup(calc, unit).arrange(LEFT, buff=0.4).move_to([0, 0.3, 0])
        box = SurroundingRectangle(row, color=GREEN, corner_radius=0.15, buff=0.28)
        self.sfx("ding")
        self.play(FadeIn(row, shift=UP * 0.3), Create(box), run_time=1.1)
        self.play(Flash(calc[6], color=GREEN, flash_radius=1.2), run_time=0.8)
        tag = ar("نوفّر لترين كل يوم!", 30, "BOLD", ROSE).move_to([0, -2.2, 0])
        self.sfx("tada")
        self.play(FadeIn(tag, scale=0.6, rate_func=BOUNCE), run_time=0.9)
        self.wait(max(d - 3.7, 0.2))
        self.clear_all()

    # ── 8. سرّ من بلادنا ────────────────────────────────────────
    def s_astuce(self):
        d = self.seg("astuce")
        head = titled("سرّ من بلادنا", 32, LILA)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        # carte verte : صالح
        g = RoundedRectangle(corner_radius=0.26, width=6.0, height=2.5, fill_color=GREEN,
                             fill_opacity=0.16, stroke_color=GREEN,
                             stroke_width=3).move_to([-3.15, -0.35, 0])
        g_h = ar("صالح مباشرة", 30, "BOLD", GREEN).move_to(g.get_center() + UP * 0.75)
        g_t = ar("بئر نظيفة أو خزان محمي", 27, "BOLD", INK).move_to(g.get_center() + DOWN * 0.1)
        gdrop = water_drop(0.6, GREEN, 0.7).move_to(g.get_center() + DOWN * 0.85)
        # carte bleue : يحتاج معالجة
        b = RoundedRectangle(corner_radius=0.26, width=6.0, height=2.5, fill_color=BLUE,
                             fill_opacity=0.16, stroke_color=BLUE,
                             stroke_width=3).move_to([3.15, -0.35, 0])
        b_h = ar("يحتاج معالجة", 30, "BOLD", BLUE).move_to(b.get_center() + UP * 0.75)
        b_t = ar("مياه نهر السنغال", 27, "BOLD", INK).move_to(b.get_center() + DOWN * 0.05)
        b_t2 = ar("تصفية وتعقيم قبل الشرب", 24, "BOLD", REDA).move_to(b.get_center() + DOWN * 0.75)
        self.sfx("ding")
        self.play(GrowFromCenter(VGroup(g, g_h, g_t), rate_func=BOUNCE),
                  FadeIn(gdrop, scale=0.4), run_time=1.2)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(b, b_h, b_t, b_t2), rate_func=BOUNCE), run_time=1.2)
        self.wait(max(d - 3.3, 0.2))
        self.clear_all()

    def construct(self):
        self.setup_common()
        self.s_intro_card("intro1")
        self.s_objectifs("intro2", [
            "أشرح أهمية الماء للحياة",
            "أميّز الماء الصالح من الملوّث",
            "أقترح وسائل للحفاظ على الماء",
        ])
        self.s_def()
        self.s_body()
        self.s_roles()
        self.s_clean()
        self.s_risk()
        self.s_example()
        self.s_astuce()
        self.s_outro_end("outro")
