# -*- coding: utf-8 -*-
"""Vidéo U10 — قياس الزوايا.  Rendu : venv/bin/manim -qh scene_u10.py VideoU10
Cœur de la vidéo : la زاوية s'OUVRE à l'écran (deux ضلعين qui pivotent autour du
رأس), les quatre types défilent avec leurs mesures, la منقلة se pose sur la
زاوية étape par étape, et la mesure 90−26=64 se calcule en couleurs."""
import numpy as np
from manim import (VGroup, Line, Arc, Dot, Circle, Rectangle, RoundedRectangle,
                   AnnularSector, SurroundingRectangle, Elbow,
                   FadeIn, FadeOut, Write, Create, Transform, ReplacementTransform,
                   GrowFromCenter, Indicate, Wiggle, Flash, LaggedStart, Rotate,
                   UP, DOWN, LEFT, RIGHT, DEGREES, ORIGIN)

from video_common import (MajorScene, ar, num, titled,
                          INK, YELL, ROSE, GREEN, BLUE, LILA, REDA, GOLD, BOUNCE, HERE)


def angle_fig(deg, color, r=1.35, label=None):
    """Angle ouvert de `deg` degrés : deux côtés depuis le رأس + arc doré."""
    g = VGroup()
    c1 = Line(ORIGIN, RIGHT * r, color=INK, stroke_width=6)
    c2 = Line(ORIGIN, RIGHT * r, color=INK, stroke_width=6).rotate(
        deg * DEGREES, about_point=ORIGIN)
    arc = Arc(radius=0.45, start_angle=0, angle=deg * DEGREES,
              color=color, stroke_width=6)
    v = Dot(ORIGIN, radius=0.09, color=color)
    g.add(c1, c2, arc, v)
    if label:
        mid = (deg / 2) * DEGREES
        pos = np.array([np.cos(mid), np.sin(mid), 0]) * 0.95
        g.add(num(label, 26, color).move_to(pos))
    return g


class VideoU10(MajorScene):
    AUDIO = HERE / "audio_u10"
    UNIT_AR = "الوحدة 10"
    UNIT_COLOR = GOLD
    TITLE = "قياس الزوايا"
    OUTRO_CALL = "والآن افتح كراسك وحلّ تمارين الوحدة 10"

    # ── 2. التعريف : انفراج بين ضلعين ───────────────────────────
    def s_def(self):
        d = self.seg("def1")
        head = titled("الزاوية: انفراج بين ضلعين", 36, GOLD)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        # la زاوية s'ouvre : le second côté pivote
        c1 = Line(ORIGIN, RIGHT * 2.2, color=INK, stroke_width=7)
        c2 = Line(ORIGIN, RIGHT * 2.2, color=INK, stroke_width=7)
        v = Dot(ORIGIN, radius=0.11, color=GOLD)
        grp = VGroup(c1, c2, v).move_to([0.3, -0.4, 0])
        self.sfx("pop")
        self.play(Create(grp), run_time=0.9)
        self.sfx("whoosh")
        self.play(Rotate(c2, 60 * DEGREES, about_point=v.get_center()), run_time=1.4)
        arc = Arc(radius=0.5, start_angle=0, angle=60 * DEGREES, color=GOLD,
                  stroke_width=6, arc_center=v.get_center())
        self.play(Create(arc), run_time=0.7)
        l1 = ar("الضلع", 24, "BOLD", BLUE).move_to(v.get_center() + RIGHT * 2.0 + DOWN * 0.4)
        l2 = ar("الضلع", 24, "BOLD", BLUE).move_to(
            v.get_center() + np.array([np.cos(60 * DEGREES), np.sin(60 * DEGREES), 0]) * 2.0
            + UP * 0.35)
        l3 = ar("الرأس", 24, "BOLD", GOLD).move_to(v.get_center() + DOWN * 0.55 + LEFT * 0.5)
        self.play(LaggedStart(FadeIn(l1), FadeIn(l2), FadeIn(l3), lag_ratio=0.3),
                  run_time=1.3)
        self.wait(max(d - 4.3, 0.2))

        d = self.seg("def2")
        deg = VGroup(ar("نقيسها بالدرجات:", 30, "BOLD"), num("°", 44, ROSE),
                     ar("بالمنقلة", 30, "BOLD", ROSE)).arrange(LEFT, buff=0.3)
        deg.move_to([0, -2.6, 0])
        box = SurroundingRectangle(deg, color=ROSE, corner_radius=0.15, buff=0.2)
        self.sfx("ding")
        self.play(FadeIn(deg), Create(box), run_time=1.0)
        self.wait(max(d - 1.0, 0.2))
        self.clear_all()

    # ── 3. الأنواع الأربعة ──────────────────────────────────────
    def s_types(self):
        d = self.seg("typ1")
        head = titled("أنواع الزوايا", 40, BLUE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        qa = angle_fig(90, GREEN, label="90°").move_to([4.3, 0.3, 0])
        qa_l = ar("قائمة = 90°", 24, "BOLD", GREEN).move_to([4.6, -1.3, 0])
        self.sfx("pop")
        self.play(Create(qa), FadeIn(qa_l, shift=UP * 0.2), run_time=1.1)
        self.wait(max(d - 2.0, 0.2))

        d = self.seg("typ2")
        ha = angle_fig(40, ROSE, label="40°").move_to([1.3, 0.3, 0])
        ha_l = ar("حادة &lt; 90°", 24, "BOLD", ROSE).move_to([1.6, -1.3, 0])
        self.sfx("pop")
        self.play(Create(ha), FadeIn(ha_l, shift=UP * 0.2), run_time=1.1)
        self.wait(max(d - 1.1, 0.2))

        d = self.seg("typ3")
        mo = angle_fig(135, LILA, label="135°").move_to([-1.9, 0.3, 0])
        mo_l = ar("منفرجة &gt; 90°", 24, "BOLD", LILA).move_to([-1.6, -1.3, 0])
        self.sfx("pop")
        self.play(Create(mo), FadeIn(mo_l, shift=UP * 0.2), run_time=1.1)
        self.wait(max(d - 1.1, 0.2))

        d = self.seg("typ4")
        ms = angle_fig(180, BLUE, label="180°").move_to([-4.9, 0.3, 0])
        ms_l = ar("مستقيمة = 180°", 22, "BOLD", BLUE).move_to([-4.6, -1.3, 0])
        self.sfx("pop")
        self.play(Create(ms), FadeIn(ms_l, shift=UP * 0.2), run_time=1.1)
        refl = ar("والمنعكسة أكبر من 180°", 28, "BOLD", REDA).move_to([0, -2.6, 0])
        self.sfx("boing")
        self.play(FadeIn(refl, shift=UP * 0.3, rate_func=BOUNCE), run_time=0.9)
        self.wait(max(d - 2.0, 0.2))
        self.clear_all()

    # ── 4. الطريقة : المنقلة بثلاث خطوات ────────────────────────
    def s_methode(self):
        d = self.seg("meth1")
        head = titled("كيف أقيس بالمنقلة؟", 38, GREEN)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        # الزاوية 45°
        ang = angle_fig(45, GOLD, r=2.0).move_to([-2.8, -0.9, 0])
        self.play(Create(ang), run_time=1.0)
        self.wait(max(d - 1.9, 0.2))

        d = self.seg("meth2")
        # المنقلة : demi-disque
        vertex = ang[3].get_center()
        prot = VGroup(
            AnnularSector(inner_radius=0.6, outer_radius=1.9, angle=180 * DEGREES,
                          start_angle=0, fill_color=BLUE, fill_opacity=0.30,
                          stroke_color=BLUE, stroke_width=3),
            Line(LEFT * 1.9, RIGHT * 1.9, color=BLUE, stroke_width=3))
        for a in range(0, 181, 30):
            end = np.array([np.cos(a * DEGREES), np.sin(a * DEGREES), 0])
            prot.add(Line(end * 1.65, end * 1.9, color=BLUE, stroke_width=2.5))
        prot.move_to([3.4, 1.6, 0])
        self.sfx("pop")
        self.play(FadeIn(prot, scale=0.5, rate_func=BOUNCE), run_time=0.9)
        st1 = ar("1. مركز المنقلة على الرأس", 24, "BOLD", BLUE).move_to([3.6, -0.4, 0])
        self.play(FadeIn(st1, shift=LEFT * 0.3), run_time=0.8)
        # elle glisse sur le رأس
        self.sfx("whoosh")
        self.play(prot.animate.move_to(vertex + UP * 0.001), run_time=1.3)
        st2 = ar("2. الضلع على الصفر", 24, "BOLD", GREEN).move_to([3.6, -1.3, 0])
        self.sfx("pop")
        self.play(FadeIn(st2, shift=LEFT * 0.3), run_time=0.8)
        self.wait(max(d - 3.8, 0.2))

        d = self.seg("meth3")
        st3 = ar("3. أقرأ القياس عند الضلع الآخر", 24, "BOLD", ROSE).move_to([3.6, -2.2, 0])
        self.sfx("pop")
        self.play(FadeIn(st3, shift=LEFT * 0.3), run_time=0.8)
        mes = num("45°", 44, GOLD).move_to(vertex + np.array([1.9, 1.9, 0]) * 0.75)
        self.sfx("ding")
        self.play(GrowFromCenter(mes, rate_func=BOUNCE), run_time=0.9)
        self.play(Flash(mes, color=GOLD, flash_radius=1.2), run_time=0.8)
        self.wait(max(d - 2.5, 0.2))
        self.clear_all()

    # ── 5. مسألة : زاويتان مجموعهما 90° ─────────────────────────
    def s_comp(self):
        d = self.seg("comp1")
        head = titled("مسألة: زاويتان مجموعهما 90°", 34, LILA)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        # angle droit découpé en 26° + ?
        c1 = Line(ORIGIN, RIGHT * 2.4, color=INK, stroke_width=6)
        c2 = Line(ORIGIN, UP * 2.4, color=INK, stroke_width=6)
        mid = Line(ORIGIN, np.array([np.cos(26 * DEGREES), np.sin(26 * DEGREES), 0]) * 2.4,
                   color=GOLD, stroke_width=5)
        a1 = Arc(radius=0.75, start_angle=0, angle=26 * DEGREES, color=ROSE, stroke_width=5)
        a2 = Arc(radius=0.55, start_angle=26 * DEGREES, angle=64 * DEGREES,
                 color=GREEN, stroke_width=5)
        l26 = num("26°", 28, ROSE).move_to(
            np.array([np.cos(13 * DEGREES), np.sin(13 * DEGREES), 0]) * 1.25)
        lq = num("?", 34, GREEN).move_to(
            np.array([np.cos(58 * DEGREES), np.sin(58 * DEGREES), 0]) * 1.05)
        fig = VGroup(c1, c2, mid, a1, a2, l26, lq).move_to([3.1, -1.0, 0])
        self.sfx("whoosh")
        self.play(Create(fig), run_time=1.6)
        self.wait(max(d - 2.5, 0.2))

        d = self.seg("comp2")
        calc = VGroup(num("90", 42), num("−", 38, REDA), num("26", 42),
                      num("=", 38), num("64°", 50, GREEN)).arrange(LEFT, buff=0.3)
        calc.move_to([-2.9, -0.9, 0])
        box = SurroundingRectangle(calc, color=GREEN, corner_radius=0.15, buff=0.22)
        self.sfx("ding")
        self.play(FadeIn(calc, shift=UP * 0.3), Create(box), run_time=1.1)
        r64 = num("64°", 30, GREEN).move_to(lq)
        self.play(ReplacementTransform(lq, r64), run_time=0.8)
        self.play(Flash(calc[4], color=GREEN, flash_radius=1.2), run_time=0.8)
        self.wait(max(d - 2.7, 0.2))
        self.clear_all()

    # ── 6. انتبه : المنعكسة = 360 − الصغيرة ─────────────────────
    def s_attention(self):
        d = self.seg("att1")
        head = titled("انتبه! سرّ الزاوية المنعكسة", 34, REDA)
        garcon = self.boy(1.9).to_edge(LEFT, buff=0.25).shift(DOWN * 1.3)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE),
                  FadeIn(garcon, shift=RIGHT * 0.8, rate_func=BOUNCE), run_time=1.0)
        # petit angle 100° + le reflex 260° en arc rouge
        small = Arc(radius=0.6, start_angle=0, angle=100 * DEGREES,
                    color=BLUE, stroke_width=6)
        big = Arc(radius=0.85, start_angle=100 * DEGREES, angle=260 * DEGREES,
                  color=REDA, stroke_width=6)
        c1 = Line(ORIGIN, RIGHT * 1.9, color=INK, stroke_width=6)
        c2 = Line(ORIGIN, np.array([np.cos(100 * DEGREES), np.sin(100 * DEGREES), 0]) * 1.9,
                  color=INK, stroke_width=6)
        fig = VGroup(c1, c2, small, big).move_to([3.4, -1.0, 0])
        self.sfx("whoosh")
        self.play(Create(fig), run_time=1.4)
        calc = VGroup(num("360", 38), num("−", 34, REDA), num("100", 38),
                      num("=", 34), num("260°", 46, REDA)).arrange(LEFT, buff=0.28)
        calc.move_to([-1.4, -1.0, 0])
        box = SurroundingRectangle(calc, color=REDA, corner_radius=0.15, buff=0.2)
        self.sfx("ding")
        self.play(FadeIn(calc, shift=UP * 0.3), Create(box), run_time=1.1)
        self.play(Wiggle(garcon), run_time=1.1)
        self.wait(max(d - 4.6, 0.2))
        self.clear_all()

    # ── 7. السر : ركن الكتاب زاوية قائمة ────────────────────────
    def s_astuce(self):
        d = self.seg("astuce")
        head = titled("سرّ صغير: ركن كتابك منقلة جاهزة!", 32, LILA)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=1.0)
        self.wait(1.6)
        book = VGroup(
            RoundedRectangle(corner_radius=0.08, width=2.6, height=3.3,
                             fill_color=BLUE, fill_opacity=0.95,
                             stroke_color=INK, stroke_width=3),
            Rectangle(width=0.35, height=3.3, fill_color="#FFFFFF", fill_opacity=0.4,
                      stroke_width=0).shift(RIGHT * 1.1),
            ar("كراسي", 26, "BOLD", "#FFFFFF"))
        book[2].move_to(book[0])
        book.move_to([2.9, -0.9, 0])
        self.sfx("pop")
        self.play(FadeIn(book, scale=0.5, rate_func=BOUNCE), run_time=0.9)
        corner = Elbow(width=0.6, angle=0, color=GOLD, stroke_width=7)
        corner.move_to(book[0].get_corner(DOWN + LEFT) + np.array([0.32, 0.32, 0]))
        self.sfx("ding")
        self.play(Create(corner), run_time=0.9)
        self.play(Flash(corner, color=GOLD, flash_radius=1.0), run_time=0.8)
        rows = [("غطّتها ← قائمة", GREEN), ("ضاقت عنها ← حادة", ROSE),
                ("اتسعت ← منفرجة", LILA)]
        t = 0
        for i, (txt, col) in enumerate(rows):
            lab = ar(txt, 26, "BOLD", col).move_to([-3.2, 0.2 - 1.0 * i, 0])
            self.sfx("pop")
            self.play(FadeIn(lab, shift=LEFT * 0.4), run_time=0.7)
            t += 0.7
        self.wait(max(d - 5.0 - t, 0.2))
        self.clear_all()

    def construct(self):
        self.setup_common()
        self.s_intro_card("intro1")
        self.s_objectifs("intro2", [
            "أميّز الزوايا: حادة، قائمة، منفرجة، مستقيمة",
            "أقيس زاوية بالمنقلة بالدرجات",
            "أرسم زاوية بقياس معلوم",
        ])
        self.s_def()
        self.s_types()
        self.s_methode()
        self.s_comp()
        self.s_attention()
        self.s_astuce()
        self.s_outro_end("outro")
