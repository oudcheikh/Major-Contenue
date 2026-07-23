# -*- coding: utf-8 -*-
"""Vidéo U14 — الأعداد العشرية.  Rendu : venv/bin/manim -qh scene_u14.py VideoU14
Cœur de la vidéo : 3,75 se DÉCOUPE à l'écran (جزء صحيح / فاصلة / جزء عشري), les
chiffres volent dans جدول الخانات (الوحدات، الأعشار، الأجزاء من المئة), la
comparaison 6,4 ↔ 6,09 se fait خانة بخانة, et l'addition posée : الفاصلة تحت الفاصلة."""
from manim import (VGroup, Rectangle, RoundedRectangle, Line, DashedLine,
                   SurroundingRectangle,
                   FadeIn, FadeOut, Write, Create, Transform, ReplacementTransform,
                   GrowFromCenter, Indicate, Wiggle, Flash, LaggedStart,
                   UP, DOWN, LEFT, RIGHT)

from video_common import (MajorScene, ar, num, titled,
                          INK, YELL, ROSE, GREEN, BLUE, LILA, REDA, GOLD, BOUNCE, HERE)


class VideoU14(MajorScene):
    AUDIO = HERE / "audio_u14"
    UNIT_AR = "الوحدة 14"
    UNIT_COLOR = BLUE
    TITLE = "الأعداد العشرية"
    OUTRO_CALL = "والآن افتح كراسك وحلّ تمارين الوحدة 14"

    # ── 2. التعريف : الفاصلة والجزءان ───────────────────────────
    def s_def(self):
        d = self.seg("def1")
        head = titled("عدد بفاصلة: جزء صحيح وجزء عشري", 32, BLUE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        ent = num("3", 88, GREEN).move_to([1.6, 0.4, 0])
        virg = num(",", 88, GOLD).move_to([1.0, 0.15, 0])
        dec = num("75", 88, ROSE).move_to([-0.1, 0.4, 0])
        self.sfx("pop")
        self.play(LaggedStart(FadeIn(ent, scale=0.4, rate_func=BOUNCE),
                              FadeIn(virg, scale=0.4, rate_func=BOUNCE),
                              FadeIn(dec, scale=0.4, rate_func=BOUNCE),
                              lag_ratio=0.3), run_time=1.6)
        l1 = ar("الجزء الصحيح", 26, "BOLD", GREEN).move_to([2.6, -1.1, 0])
        l2 = ar("الفاصلة", 26, "BOLD", GOLD).move_to([0.9, -1.7, 0])
        l3 = ar("الجزء العشري", 26, "BOLD", ROSE).move_to([-1.1, -1.1, 0])
        self.play(LaggedStart(FadeIn(l1, shift=UP * 0.3), FadeIn(l2, shift=UP * 0.3),
                              FadeIn(l3, shift=UP * 0.3), lag_ratio=0.3), run_time=1.5)
        self.wait(max(d - 4.0, 0.2))

        d = self.seg("def2")
        lect = ar("ثلاثة فاصلة خمسة وسبعون", 34, "BOLD", LILA).move_to([0.6, -2.4, 0])
        box = SurroundingRectangle(lect, color=LILA, corner_radius=0.15, buff=0.22)
        self.play(Indicate(ent, color=GREEN, scale_factor=1.3), run_time=0.9)
        self.play(Indicate(virg, color=GOLD, scale_factor=1.3), run_time=0.8)
        self.play(Indicate(dec, color=ROSE, scale_factor=1.3), run_time=0.9)
        self.sfx("ding")
        self.play(FadeIn(lect), Create(box), run_time=1.0)
        self.wait(max(d - 3.6, 0.2))
        self.clear_all()

    # ── 3. جدول الخانات ─────────────────────────────────────────
    def s_tab(self):
        d = self.seg("tab1")
        head = titled("لكل رقم خانته!", 38, GREEN)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        # colonnes RTL : الوحدات à droite, puis الفاصلة, الأعشار, الأجزاء من المئة
        cols = [("الوحدات", GREEN, 2.4), (",", GOLD, 0.9),
                ("الأعشار", ROSE, 2.4), ("الأجزاء من المئة", LILA, 3.0)]
        x = 4.4
        headers, cells_x = VGroup(), []
        for txt, col, w in cols:
            hbox = Rectangle(width=w, height=0.95, fill_color=col, fill_opacity=0.92,
                             stroke_color=INK, stroke_width=2.5).move_to([x - w / 2, 0.9, 0])
            ht = (num(txt, 40, "#FFFFFF") if txt == ","
                  else ar(txt, 21, "BOLD", "#FFFFFF")).move_to(hbox)
            cbox = Rectangle(width=w, height=1.15, fill_color="#FFFFFF", fill_opacity=0.9,
                             stroke_color=INK, stroke_width=2.5).move_to([x - w / 2, -0.15, 0])
            headers.add(VGroup(hbox, ht, cbox))
            cells_x.append(x - w / 2)
            x -= w
        self.sfx("whoosh")
        self.play(LaggedStart(*[FadeIn(h, shift=DOWN * 0.3, rate_func=BOUNCE)
                                for h in headers], lag_ratio=0.2), run_time=1.8)
        self.wait(max(d - 2.7, 0.2))

        d = self.seg("tab2")
        # 3 , 7 5 volent dans leurs cases
        digits = [num("3", 54, GREEN), num(",", 54, GOLD),
                  num("7", 54, ROSE), num("5", 54, LILA)]
        start = VGroup(*[dg.copy() for dg in digits])
        for i, dg in enumerate(digits):
            dg.move_to([cells_x[i], -0.15, 0])
        src = VGroup(*start).arrange(LEFT, buff=0.15).move_to([0, -2.1, 0])
        self.sfx("pop")
        self.play(FadeIn(src, scale=0.5, rate_func=BOUNCE), run_time=0.8)
        for s, dg in zip(start, digits):
            self.sfx("whoosh")
            self.play(ReplacementTransform(s, dg), run_time=0.7)
        self.play(Flash(VGroup(*digits), color=GOLD, flash_radius=2.6), run_time=0.8)
        self.wait(max(d - 4.4, 0.2))
        self.clear_all()

    # ── 4. المقارنة : 6,4 و 6,09 ────────────────────────────────
    def s_comp(self):
        d = self.seg("comp1")
        head = titled("أقارن: 6,4 أم 6,09؟", 36, GOLD)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        a = num("6,4", 64).move_to([2.4, 0.6, 0])
        b = num("6,09", 64).move_to([-2.2, 0.6, 0])
        vs = ar("أم", 30, "BOLD", GOLD).move_to([0.1, 0.6, 0])
        self.sfx("pop")
        self.play(FadeIn(a, scale=0.5, rate_func=BOUNCE), FadeIn(vs),
                  FadeIn(b, scale=0.5, rate_func=BOUNCE), run_time=1.0)
        self.wait(max(d - 1.9, 0.2))

        d = self.seg("comp2")
        a2 = num("6,40", 64).move_to([2.4, 0.6, 0])
        a2[-1].set_color(GOLD)
        self.sfx("boing")
        self.play(ReplacementTransform(a, a2), run_time=1.0)
        note = ar("أضيف صفرًا لأساوي عدد الأرقام", 26, "BOLD", GOLD).move_to([2.4, -0.6, 0])
        self.play(FadeIn(note, shift=UP * 0.3), run_time=0.9)
        self.wait(max(d - 1.9, 0.2))

        d = self.seg("comp3")
        # je compare خانة بخانة : le 4 gagne contre le 0
        c4 = SurroundingRectangle(a2[2], color=GREEN, corner_radius=0.1, buff=0.08)
        c0 = SurroundingRectangle(b[2], color=REDA, corner_radius=0.1, buff=0.08)
        self.sfx("pop")
        self.play(Create(c4), Create(c0), run_time=0.9)
        self.play(Indicate(a2[2], color=GREEN, scale_factor=1.5),
                  Indicate(b[2], color=REDA, scale_factor=1.5), run_time=1.1)
        res = VGroup(num("6,4", 48, GREEN), num(">", 44, GOLD),
                     num("6,09", 48)).arrange(LEFT, buff=0.35)
        res.move_to([0.1, -2.2, 0])
        box = SurroundingRectangle(res, color=GREEN, corner_radius=0.15, buff=0.22)
        self.sfx("ding")
        self.play(FadeIn(res, shift=UP * 0.3), Create(box), run_time=1.0)
        self.play(Flash(res, color=GREEN, flash_radius=2.2), run_time=0.8)
        self.wait(max(d - 3.8, 0.2))
        self.clear_all()

    # ── 5. الجمع عموديًا : 1,5 + 2,3 ────────────────────────────
    def s_op(self):
        d = self.seg("op1")
        head = titled("القاعدة الذهبية: الفاصلة تحت الفاصلة!", 30, ROSE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        self.wait(max(d - 0.9, 0.2))

        d = self.seg("op2")
        n1 = num("1,5", 60).move_to([0.6, 0.9, 0])
        n2 = num("2,3", 60).move_to([0.6, -0.1, 0])
        plus = num("+", 52, GREEN).next_to(n2, RIGHT, buff=0.5)
        bar = Line([1.9, -0.75, 0], [-0.9, -0.75, 0], color=INK, stroke_width=4)
        self.sfx("pop")
        self.play(FadeIn(n1, scale=0.5, rate_func=BOUNCE), run_time=0.8)
        self.sfx("pop")
        self.play(FadeIn(n2, scale=0.5, rate_func=BOUNCE), FadeIn(plus), run_time=0.8)
        self.play(Create(bar), run_time=0.6)
        # ligne pointillée qui traverse les فاصلة alignées
        vline = DashedLine([0.6, 1.5, 0], [0.6, -1.9, 0], color=GOLD, stroke_width=4)
        self.sfx("whoosh")
        self.play(Create(vline), run_time=0.9)
        lab = ar("الفاصلة تحت الفاصلة", 24, "BOLD", GOLD).move_to([-2.6, 0.4, 0])
        self.play(FadeIn(lab, shift=RIGHT * 0.3), run_time=0.8)
        self.wait(max(d - 3.9, 0.2))

        d = self.seg("op3")
        # أعشار : 5+3=8 puis وحدات : 1+2=3 puis la virgule descend
        self.play(Indicate(n1[2], color=ROSE, scale_factor=1.5),
                  Indicate(n2[2], color=ROSE, scale_factor=1.5), run_time=1.0)
        r8 = num("8", 60, ROSE).move_to([-0.1, -1.4, 0])
        self.sfx("pop")
        self.play(FadeIn(r8, scale=0.4, rate_func=BOUNCE), run_time=0.8)
        self.play(Indicate(n1[0], color=GREEN, scale_factor=1.5),
                  Indicate(n2[0], color=GREEN, scale_factor=1.5), run_time=1.0)
        r3 = num("3", 60, GREEN).move_to([1.2, -1.4, 0])
        self.sfx("pop")
        self.play(FadeIn(r3, scale=0.4, rate_func=BOUNCE), run_time=0.8)
        virg = num(",", 60, GOLD).move_to([0.62, -1.65, 0])
        self.sfx("whoosh")
        self.play(ReplacementTransform(n2[1].copy(), virg), run_time=0.9)
        frame = SurroundingRectangle(VGroup(r3, virg, r8), color=GREEN,
                                     corner_radius=0.12, buff=0.2)
        self.sfx("ding")
        self.play(Create(frame), run_time=0.8)
        self.play(Flash(VGroup(r3, virg, r8), color=GREEN, flash_radius=1.6), run_time=0.8)
        self.wait(max(d - 5.3, 0.2))
        self.clear_all()

    # ── 6. انتبه : لا تنسَ الفاصلة ──────────────────────────────
    def s_attention(self):
        d = self.seg("att1")
        head = titled("انتبه! لا تنسَ الفاصلة في الناتج", 32, REDA)
        garcon = self.boy(1.9).to_edge(LEFT, buff=0.25).shift(DOWN * 1.3)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE),
                  FadeIn(garcon, shift=RIGHT * 0.8, rate_func=BOUNCE), run_time=1.0)
        c1 = RoundedRectangle(corner_radius=0.22, width=6.4, height=1.1, fill_color=REDA,
                              fill_opacity=0.92, stroke_color=INK).move_to(RIGHT * 2.4 + UP * 0.5)
        c1t = VGroup(num("38", 34, "#FFFFFF"), ar("خطأ!", 26, "BOLD", "#FFFFFF")
                     ).arrange(LEFT, buff=0.5).move_to(c1)
        c2 = RoundedRectangle(corner_radius=0.22, width=6.4, height=1.1, fill_color=GREEN,
                              fill_opacity=0.92, stroke_color=INK).move_to(RIGHT * 2.4 + DOWN * 0.9)
        c2t = VGroup(num("3,8", 34, "#FFFFFF"), ar("صحيح!", 26, "BOLD", "#FFFFFF")
                     ).arrange(LEFT, buff=0.5).move_to(c2)
        self.sfx("boing")
        self.play(GrowFromCenter(VGroup(c1, c1t), rate_func=BOUNCE), run_time=0.9)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(c2, c2t), rate_func=BOUNCE), run_time=0.9)
        self.play(Wiggle(garcon), run_time=1.1)
        self.wait(max(d - 3.9, 0.2))
        self.clear_all()

    # ── 7. السر : 3,5 = 3,50 ────────────────────────────────────
    def s_astuce(self):
        d = self.seg("astuce")
        head = titled("سرّ ذهبي: الصفر في الآخر لا يغيّر شيئًا", 30, LILA)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=1.0)
        self.wait(1.8)
        a = num("3,5", 66).move_to([2.2, -0.2, 0])
        eq = num("=", 56, GOLD).move_to([0.1, -0.2, 0])
        b = num("3,50", 66).move_to([-2.1, -0.2, 0])
        b[-1].set_color(GOLD)
        self.sfx("pop")
        self.play(FadeIn(a, scale=0.5, rate_func=BOUNCE), run_time=0.8)
        self.sfx("ding")
        self.play(FadeIn(eq), FadeIn(b, scale=0.5, rate_func=BOUNCE), run_time=1.0)
        self.play(Flash(VGroup(a, eq, b), color=LILA, flash_radius=2.6), run_time=0.9)
        self.wait(max(d - 4.5, 0.2))
        self.clear_all()

    def construct(self):
        self.setup_common()
        self.s_intro_card("intro1")
        self.s_objectifs("intro2", [
            "أقرأ الأعداد العشرية وأكتبها بالفاصلة",
            "أقارن الأعداد العشرية وأرتّبها",
            "أجمع وأطرح: الفاصلة تحت الفاصلة",
        ])
        self.s_def()
        self.s_tab()
        self.s_comp()
        self.s_op()
        self.s_attention()
        self.s_astuce()
        self.s_outro_end("outro")
