# -*- coding: utf-8 -*-
"""Vidéo U6 — قياس الأطوال.  Rendu : venv/bin/manim -qh scene_u6.py VideoU6
Cœur de la vidéo : une règle graduée mesure un crayon à l'écran, puis le tableau
de conversion (km|hm|dam|m|dm|cm|mm) où le chiffre VOLE dans sa colonne et les
zéros complètent jusqu'à l'unité demandée — comme un tableau de خانات."""
from manim import (VGroup, Rectangle, RoundedRectangle, SurroundingRectangle,
                   Line, Arrow, Cross,
                   FadeIn, FadeOut, Write, Create, GrowFromCenter,
                   Indicate, Wiggle, Flash, LaggedStart,
                   UP, DOWN, LEFT, RIGHT)

from video_common import (MajorScene, ar, num, titled,
                          INK, YELL, ROSE, GREEN, BLUE, LILA, REDA, GOLD, BOUNCE, HERE)

UNITS = ["km", "hm", "dam", "m", "dm", "cm", "mm"]     # LTR comme dans الكراس
COL_X = [-3.9 + 1.3 * i for i in range(7)]             # km à gauche → mm à droite


class VideoU6(MajorScene):
    AUDIO = HERE / "audio_u6"
    UNIT_AR = "الوحدة 6"
    UNIT_COLOR = GREEN
    TITLE = "قياس الأطوال"
    OUTRO_CALL = "والآن افتح كراسك وحلّ تمارين الوحدة 6"

    # ── 2. الوحدات الأربع : mm cm m km ─────────────────────────
    def s_unites(self):
        d = self.seg("unit1")
        head = titled("وحدات الطول", 42, GREEN)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        infos = [("mm", "المليمتر", YELL, 4.9), ("cm", "السنتيمتر", ROSE, 1.65),
                 ("m", "المتر", GREEN, -1.65), ("km", "الكيلومتر", BLUE, -4.9)]
        self.cards, self.names = {}, {}
        t = 0.9
        for sym, name, col, x in infos:          # RTL : mm apparaît à droite d'abord
            c = RoundedRectangle(corner_radius=0.22, width=2.6, height=1.0,
                                 fill_color=col, fill_opacity=0.95,
                                 stroke_color=INK, stroke_width=2).move_to([x, 1.0, 0])
            ct = num(sym, 40, "#FFFFFF").move_to(c)
            n = ar(name, 24, "BOLD", INK).move_to([x, 0.15, 0])
            self.cards[sym] = VGroup(c, ct)
            self.names[sym] = n
            self.sfx("pop")
            self.play(FadeIn(VGroup(c, ct, n), shift=DOWN * 0.3, rate_func=BOUNCE),
                      run_time=0.7)
            t += 0.7
        self.wait(max(d - t, 0.2))

        d = self.seg("unit2")                    # mm سُمك بطاقة · cm عرض إصبع
        ex_mm = ar("سُمك بطاقة", 22, color="#666666").move_to([4.9, -0.55, 0])
        ex_cm = ar("عرض إصبع", 22, color="#666666").move_to([1.65, -0.55, 0])
        self.play(Indicate(self.cards["mm"], color=GOLD, scale_factor=1.2), run_time=0.8)
        self.sfx("pop")
        self.play(FadeIn(ex_mm, shift=UP * 0.2), run_time=0.6)
        self.play(Indicate(self.cards["cm"], color=GOLD, scale_factor=1.2), run_time=0.8)
        self.sfx("pop")
        self.play(FadeIn(ex_cm, shift=UP * 0.2), run_time=0.6)
        self.wait(max(d - 2.8, 0.2))

        d = self.seg("unit3")                    # m ثلاث مساطر · km بين مدينتين
        ex_m = ar("ثلاث مساطر", 22, color="#666666").move_to([-1.65, -0.55, 0])
        ex_km = ar("بين مدينتين", 22, color="#666666").move_to([-4.9, -0.55, 0])
        self.play(Indicate(self.cards["m"], color=GOLD, scale_factor=1.2), run_time=0.8)
        self.sfx("pop")
        self.play(FadeIn(ex_m, shift=UP * 0.2), run_time=0.6)
        self.play(Indicate(self.cards["km"], color=GOLD, scale_factor=1.2), run_time=0.8)
        self.sfx("pop")
        self.play(FadeIn(ex_km, shift=UP * 0.2), run_time=0.6)
        self.wait(max(d - 2.8, 0.2))
        self.clear_all()

        # rel1 : العلاقات الثلاث
        d = self.seg("rel1")
        head = titled("أحفظ العلاقات", 42, GREEN)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.8)
        rels = [("1 m = 100 cm", GREEN, 1.0), ("1 cm = 10 mm", ROSE, 0.0),
                ("1 km = 1000 m", BLUE, -1.0)]
        t = 0.8
        for txt, col, y in rels:
            r = num(txt, 46, col).move_to([0, y, 0])
            self.sfx("pop")
            self.play(FadeIn(r, shift=UP * 0.25, rate_func=BOUNCE), run_time=0.9)
            t += 0.9
        self.wait(max(d - t, 0.2))
        self.clear_all()

    # ── 3. أقيس بالمسطرة : قلم طوله 8 cm ────────────────────────
    def s_regle(self):
        d = self.seg("mes1")
        head = titled("أقيس بالمسطرة", 42, GREEN)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        body = Rectangle(width=8.8, height=1.1, fill_color="#fdf6e4", fill_opacity=1,
                         stroke_color="#d78d33", stroke_width=3).move_to([0, -1.1, 0])
        ticks = VGroup(*[Line([-4 + 0.8 * i, -0.6, 0], [-4 + 0.8 * i, -0.95, 0],
                              color=INK, stroke_width=2.5) for i in range(11)])
        nums = VGroup(*[num(str(i), 22).move_to([-4 + 0.8 * i, -1.3, 0])
                        for i in range(11)])
        cm_lab = num("cm", 20, "#d78d33").move_to([4.15, -1.3, 0])
        self.sfx("pop")
        self.play(FadeIn(body), Create(ticks), FadeIn(nums), FadeIn(cm_lab), run_time=1.4)
        pencil = RoundedRectangle(corner_radius=0.18, width=6.4, height=0.55,
                                  fill_color=YELL, fill_opacity=1, stroke_color=INK,
                                  stroke_width=2.5).move_to([-0.8, -0.1, 0])
        self.sfx("whoosh")
        self.play(FadeIn(pencil, shift=DOWN * 0.5), run_time=0.8)
        self.play(Indicate(nums[0], color=REDA, scale_factor=1.6), run_time=0.7)
        self.play(Indicate(nums[8], color=REDA, scale_factor=1.6), run_time=0.7)
        res = num("8 cm", 48, GREEN).move_to([0, 1.2, 0])
        self.sfx("ding")
        self.play(FadeIn(res, shift=UP * 0.3, rate_func=BOUNCE), run_time=0.8)
        self.play(Flash(res, color=GREEN, flash_radius=1.6), run_time=0.8)
        self.wait(max(d - 6.1, 0.2))
        self.clear_all()

    # ── 4. جدول التحويل : 5 m = 500 cm ─────────────────────────
    def s_tableau(self):
        d = self.seg("conv1")
        head = titled("جدول تحويل وحدات الطول", 36, BLUE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        headers = VGroup()
        for i, u in enumerate(UNITS):
            cell = Rectangle(width=1.3, height=0.7, fill_color=BLUE, fill_opacity=0.92,
                             stroke_color=INK, stroke_width=2).move_to([COL_X[i], 0.9, 0])
            lab = num(u, 26, "#FFFFFF").move_to(cell)
            headers.add(VGroup(cell, lab))
        cells = VGroup(*[Rectangle(width=1.3, height=0.95, fill_color="#FFFFFF",
                                   fill_opacity=0.92, stroke_color=INK, stroke_width=2)
                        .move_to([COL_X[i], 0.05, 0]) for i in range(7)])
        self.sfx("pop")
        self.play(LaggedStart(*[FadeIn(h, shift=DOWN * 0.25, rate_func=BOUNCE)
                                for h in headers], lag_ratio=0.1), run_time=1.4)
        self.play(Create(cells), run_time=0.8)
        self.wait(max(d - 3.1, 0.2))

        # conv2 : le 5 vole dans la colonne m
        d = self.seg("conv2")
        five = num("5", 60, LILA).move_to([0, 2.0, 0])
        self.sfx("pop")
        self.play(FadeIn(five, scale=0.4, rate_func=BOUNCE), run_time=0.7)
        self.play(Indicate(headers[3], color=GOLD, scale_factor=1.2), run_time=0.7)
        self.sfx("whoosh")
        self.play(five.animate.scale(44 / 60).move_to([COL_X[3], 0.05, 0]), run_time=0.9)
        self.wait(max(d - 2.3, 0.2))

        # conv3 : les zéros dans dm et cm
        d = self.seg("conv3")
        z1 = num("0", 44).move_to([COL_X[4], 0.05, 0])
        z2 = num("0", 44).move_to([COL_X[5], 0.05, 0])
        self.sfx("pop")
        self.play(FadeIn(z1, shift=DOWN * 0.6, rate_func=BOUNCE), run_time=0.9)
        self.sfx("pop")
        self.play(FadeIn(z2, shift=DOWN * 0.6, rate_func=BOUNCE), run_time=0.9)
        self.wait(max(d - 1.8, 0.2))

        # conv4 : lire 500 → 5 m = 500 cm
        d = self.seg("conv4")
        frame = SurroundingRectangle(VGroup(five, z1, z2), color=GREEN,
                                     corner_radius=0.15, buff=0.2)
        self.sfx("ding")
        self.play(Create(frame), run_time=0.8)
        res = num("5 m = 500 cm", 48, GREEN).move_to([0, -1.7, 0])
        self.play(FadeIn(res, shift=UP * 0.3, rate_func=BOUNCE), run_time=0.9)
        self.play(Flash(res, color=GREEN, flash_radius=2.6), run_time=0.8)
        self.wait(max(d - 2.5, 0.2))
        self.clear_all()

        # ex1 : شريط 2 m و35 cm → 235 cm (نموذج الشريط)
        d = self.seg("ex1")
        head2 = titled("كم سنتيمترًا في الشريط؟", 38, GOLD)
        self.sfx("pop")
        self.play(FadeIn(head2, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        seg_m = Rectangle(width=4.0, height=0.8, fill_color=BLUE, fill_opacity=0.95,
                          stroke_color=INK, stroke_width=2.5).move_to([0.75, 0.6, 0])
        lab_m = num("2 m", 30, "#FFFFFF").move_to(seg_m)
        seg_cm = Rectangle(width=0.7, height=0.8, fill_color=YELL, fill_opacity=0.95,
                           stroke_color=INK, stroke_width=2.5).move_to([-1.6, 0.6, 0])
        lab_cm = num("35 cm", 24).next_to(seg_cm, DOWN, buff=0.25)
        self.sfx("pop")
        self.play(FadeIn(VGroup(seg_m, lab_m), shift=LEFT * 0.4, rate_func=BOUNCE),
                  run_time=0.9)
        self.sfx("pop")
        self.play(FadeIn(VGroup(seg_cm, lab_cm), shift=LEFT * 0.4, rate_func=BOUNCE),
                  run_time=0.9)
        conv = num("2 m = 200 cm", 30, BLUE).move_to([3.4, -0.7, 0])
        self.play(FadeIn(conv, shift=UP * 0.2), run_time=0.7)
        eq = num("200 + 35 = 235 cm", 48, GREEN).move_to([0, -1.8, 0])
        self.sfx("ding")
        self.play(Write(eq), run_time=1.3)
        self.play(Flash(eq, color=GREEN, flash_radius=3.0), run_time=0.8)
        self.wait(max(d - 5.5, 0.2))
        self.clear_all()

    # ── 5. انتبه : 1 m = 100 cm وليس 10 ─────────────────────────
    def s_attention(self):
        d = self.seg("att1")
        head = titled("انتبه! المتر مائة سنتيمتر", 36, REDA)
        garcon = self.boy(1.9).to_edge(LEFT, buff=0.25).shift(DOWN * 1.3)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE),
                  FadeIn(garcon, shift=RIGHT * 0.8, rate_func=BOUNCE), run_time=1.0)
        c1 = RoundedRectangle(corner_radius=0.22, width=4.4, height=1.05, fill_color=ROSE,
                              fill_opacity=0.92, stroke_color=INK).move_to([2.9, 0.7, 0])
        c1t = num("1 m = 10 cm", 36, "#FFFFFF").move_to(c1)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(c1, c1t), rate_func=BOUNCE), run_time=0.8)
        cross = Cross(VGroup(c1, c1t), stroke_color=REDA, stroke_width=6)
        self.sfx("boing")
        self.play(Create(cross), run_time=0.7)
        c2 = RoundedRectangle(corner_radius=0.22, width=4.4, height=1.05, fill_color=GREEN,
                              fill_opacity=0.92, stroke_color=INK).move_to([2.9, -1.0, 0])
        c2t = num("1 m = 100 cm", 36, "#FFFFFF").move_to(c2)
        self.sfx("ding")
        self.play(GrowFromCenter(VGroup(c2, c2t), rate_func=BOUNCE), run_time=0.8)
        c3 = num("1 cm = 10 mm", 30, BLUE).move_to([2.9, -2.2, 0])
        self.sfx("pop")
        self.play(FadeIn(c3, shift=UP * 0.25), run_time=0.7)
        self.play(Wiggle(garcon), run_time=1.1)
        self.wait(max(d - 5.1, 0.2))
        self.clear_all()

    # ── 6. السر : سلم الوحدات ×10 / ÷10 ─────────────────────────
    def s_astuce(self):
        d = self.seg("astuce")
        head = titled("سرّ صغير قبل أن نفترق", 42, LILA)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=1.0)
        steps = [("m", GREEN, 3.2, 1.2), ("dm", BLUE, 1.1, 0.45),
                 ("cm", ROSE, -1.0, -0.3), ("mm", YELL, -3.1, -1.05)]
        cards = []
        t = 1.0
        for sym, col, x, y in steps:             # l'escalier descend vers la gauche (RTL)
            c = RoundedRectangle(corner_radius=0.18, width=1.7, height=0.75,
                                 fill_color=col, fill_opacity=0.95, stroke_color=INK,
                                 stroke_width=2).move_to([x, y, 0])
            ct = num(sym, 30, "#FFFFFF").move_to(c)
            cards.append(VGroup(c, ct))
            self.sfx("pop")
            self.play(FadeIn(cards[-1], shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.5)
            t += 0.5
        arrows_down = VGroup()
        for i in range(3):
            a = Arrow(cards[i].get_bottom() + DOWN * 0.05 + LEFT * 0.3,
                      cards[i + 1].get_right() + RIGHT * 0.1,
                      color=GREEN, stroke_width=5, max_tip_length_to_length_ratio=0.25)
            arrows_down.add(a)
        lab_down = num("× 10", 30, GREEN).move_to([0.4, -1.75, 0])
        self.sfx("whoosh")
        self.play(LaggedStart(*[Create(a) for a in arrows_down], lag_ratio=0.2),
                  FadeIn(lab_down, shift=UP * 0.2), run_time=1.2)
        a_up = Arrow([-3.1, -0.5, 0], [3.2, 1.9, 0], color=ROSE, stroke_width=5,
                     max_tip_length_to_length_ratio=0.06)
        lab_up = num("÷ 10", 30, ROSE).move_to([-0.6, 1.5, 0])
        self.sfx("whoosh")
        self.play(Create(a_up), FadeIn(lab_up, shift=UP * 0.2), run_time=1.0)
        self.sfx("ding")
        self.wait(max(d - t - 2.2, 0.2))
        self.clear_all()

    def construct(self):
        self.setup_common()
        self.s_intro_card("intro1")
        self.s_objectifs("intro2", [
            "أميّز وحدات الطول وأختار المناسبة",
            "أحوّل الأطوال بجدول التحويل",
            "أحلّ مسائل بجمع الأطوال وطرحها",
        ])
        self.s_unites()
        self.s_regle()
        self.s_tableau()
        self.s_attention()
        self.s_astuce()
        self.s_outro_end("outro")
