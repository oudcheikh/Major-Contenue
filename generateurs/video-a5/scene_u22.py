# -*- coding: utf-8 -*-
"""Vidéo U22 — الحركة المنتظمة.  Rendu : venv/bin/manim -qh scene_u22.py VideoU22
Cœur de la vidéo : la voiture ROULE sur la route et laisse des bornes égales chaque
heure (حركة منتظمة), puis le مثلث السرعة : le doigt couvre المطلوب et le قانون
apparaît ; enfin قطار الحديد : 1h40 → 100 دقيقة → 70 km."""
from manim import (VGroup, Rectangle, RoundedRectangle, Circle, Line, Polygon,
                   SurroundingRectangle,
                   FadeIn, FadeOut, Write, Create, Transform, ReplacementTransform,
                   GrowFromCenter, Indicate, Wiggle, Flash, LaggedStart,
                   UP, DOWN, LEFT, RIGHT)

from video_common import (MajorScene, ar, num, titled, strip,
                          INK, YELL, ROSE, GREEN, BLUE, LILA, REDA, GOLD, BOUNCE, HERE)


def voiture(color=BLUE, w=1.6):
    corps = RoundedRectangle(corner_radius=0.15, width=w, height=0.5,
                             fill_color=color, fill_opacity=1,
                             stroke_color=INK, stroke_width=2.5)
    toit = RoundedRectangle(corner_radius=0.12, width=w * 0.55, height=0.35,
                            fill_color=color, fill_opacity=1,
                            stroke_color=INK, stroke_width=2.5)
    toit.next_to(corps, UP, buff=-0.08)
    r1 = Circle(radius=0.14, fill_color=INK, fill_opacity=1,
                stroke_width=0).move_to(corps.get_center() + LEFT * w * 0.28 + DOWN * 0.28)
    r2 = Circle(radius=0.14, fill_color=INK, fill_opacity=1,
                stroke_width=0).move_to(corps.get_center() + RIGHT * w * 0.28 + DOWN * 0.28)
    return VGroup(corps, toit, r1, r2)


def triangle_svt():
    """مثلث السرعة : المسافة في الأعلى، السرعة × الزمن في الأسفل."""
    tri = Polygon([0, 1.7, 0], [2.1, -1.3, 0], [-2.1, -1.3, 0],
                  stroke_color=INK, stroke_width=4,
                  fill_color="#FFFFFF", fill_opacity=0.9)
    mid = Line([-1.05, 0.2, 0], [1.05, 0.2, 0], color=INK, stroke_width=3)
    sep = Line([0, 0.2, 0], [0, -1.3, 0], color=INK, stroke_width=3)
    t_d = ar("المسافة", 28, "BOLD", GREEN).move_to([0, 0.8, 0])
    t_v = ar("السرعة", 24, "BOLD", BLUE).move_to([0.85, -0.55, 0])
    t_t = ar("الزمن", 24, "BOLD", ROSE).move_to([-0.85, -0.55, 0])
    return VGroup(tri, mid, sep, t_d, t_v, t_t)


class VideoU22(MajorScene):
    AUDIO = HERE / "audio_u22"
    UNIT_AR = "الوحدة 22"
    UNIT_COLOR = GREEN
    TITLE = "الحركة المنتظمة"
    OUTRO_CALL = "والآن افتح كراسك وحلّ تمارين الوحدة 22"

    # ── 2. المفهوم : نفس المسافة كل ساعة ────────────────────────
    def s_concept(self):
        d = self.seg("conc1")
        head = titled("حركة منتظمة: نفس المسافة كل ساعة", 32, GREEN)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        route = Line([6.2, -0.9, 0], [-6.2, -0.9, 0], color=INK, stroke_width=5)
        self.play(Create(route), run_time=0.8)
        car = voiture().move_to([5.0, -0.35, 0])
        self.sfx("pop")
        self.play(FadeIn(car, scale=0.5, rate_func=BOUNCE), run_time=0.8)
        # la voiture roule (RTL : droite → gauche), une borne à chaque heure
        bornes = VGroup()
        for i, x in enumerate([1.6, -1.8, -5.2]):
            self.sfx("whoosh")
            self.play(car.animate.move_to([x, -0.35, 0]), run_time=1.0)
            b = Line([x, -0.9, 0], [x, -1.35, 0], color=GOLD, stroke_width=5)
            lb = ar(f"ساعة {i + 1}", 22, "BOLD", GOLD).next_to(b, DOWN, buff=0.15)
            bornes.add(VGroup(b, lb))
            self.sfx("pop")
            self.play(FadeIn(bornes[-1], scale=0.5), run_time=0.4)
        self.wait(max(d - 5.0, 0.2))

        d = self.seg("conc2")
        box = RoundedRectangle(corner_radius=0.25, width=10.6, height=1.25,
                               fill_color=GREEN, fill_opacity=0.92,
                               stroke_color=INK, stroke_width=2).move_to([0, 1.55, 0])
        boxt = ar("السرعة المتوسطة = المسافة في ساعة واحدة (km/h)", 28,
                  "BOLD", "#FFFFFF").move_to(box)
        self.sfx("ding")
        self.play(GrowFromCenter(VGroup(box, boxt), rate_func=BOUNCE), run_time=1.1)
        self.wait(max(d - 1.1, 0.2))
        self.clear_all()

    # ── 3. مثال الدراجة : 40 km في ساعتين ───────────────────────
    def s_velo(self):
        d = self.seg("ex1")
        head = titled("دراجة: 40 km في ساعتين", 36, BLUE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        s = strip(2, 2, width=6.4, height=0.95, fill=BLUE).move_to([0.2, 0.5, 0])
        lab = VGroup(num("40", 40), ar("كيلومترًا", 26, "BOLD")).arrange(LEFT, buff=0.3)
        lab.next_to(s, UP, buff=0.3)
        h1 = ar("ساعة 1", 24, "BOLD", GOLD).move_to(s[0].get_center() + DOWN * 1.0)
        h2 = ar("ساعة 2", 24, "BOLD", GOLD).move_to(s[1].get_center() + DOWN * 1.0)
        self.sfx("pop")
        self.play(FadeIn(VGroup(s, lab), scale=0.7, rate_func=BOUNCE), run_time=1.0)
        self.play(FadeIn(h1, shift=UP * 0.2), FadeIn(h2, shift=UP * 0.2), run_time=0.8)
        self.wait(max(d - 2.8, 0.2))

        d = self.seg("ex2")
        n1 = num("20", 36, "#FFFFFF").move_to(s[0].get_center())
        n2 = num("20", 36, "#FFFFFF").move_to(s[1].get_center())
        self.sfx("pop")
        self.play(FadeIn(n1, scale=0.4, rate_func=BOUNCE),
                  FadeIn(n2, scale=0.4, rate_func=BOUNCE), run_time=0.9)
        calc = VGroup(num("40", 40), ar("÷", 30, "BOLD"), num("2", 40),
                      num("=", 38), num("20", 48, GREEN),
                      ar("km/h", 30, "BOLD", GREEN)).arrange(LEFT, buff=0.3)
        calc.move_to([0.2, -2.2, 0])
        box = SurroundingRectangle(calc, color=GREEN, corner_radius=0.15, buff=0.22)
        self.sfx("ding")
        self.play(FadeIn(calc, shift=UP * 0.3), Create(box), run_time=1.1)
        self.play(Flash(calc[4], color=GREEN, flash_radius=1.2), run_time=0.8)
        self.wait(max(d - 2.8, 0.2))
        self.clear_all()

    # ── 4. مثلث السرعة والمسافة والزمن ──────────────────────────
    def s_triangle(self):
        d = self.seg("tri1")
        head = titled("مثلث السرعة: ارسمه واحفظه", 36, LILA)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        tri = triangle_svt().move_to([3.4, -0.7, 0])
        self.sfx("whoosh")
        self.play(Create(tri[0]), run_time=1.0)
        self.play(Create(tri[1]), Create(tri[2]), run_time=0.8)
        self.sfx("pop")
        self.play(LaggedStart(FadeIn(tri[3], scale=0.4, rate_func=BOUNCE),
                              FadeIn(tri[4], scale=0.4, rate_func=BOUNCE),
                              FadeIn(tri[5], scale=0.4, rate_func=BOUNCE),
                              lag_ratio=0.3), run_time=1.5)
        self.wait(max(d - 4.2, 0.2))

        # tri2 : le doigt couvre المسافة → المسافة = السرعة × الزمن
        d = self.seg("tri2")
        doigt = Circle(radius=0.55, fill_color=YELL, fill_opacity=0.85,
                       stroke_color=GOLD, stroke_width=4).move_to(tri[3].get_center())
        self.sfx("boing")
        self.play(GrowFromCenter(doigt, rate_func=BOUNCE), run_time=0.8)
        law1 = VGroup(ar("المسافة", 30, "BOLD", GREEN), num("=", 36),
                      ar("السرعة", 30, "BOLD", BLUE), ar("×", 26, "BOLD", GOLD),
                      ar("الزمن", 30, "BOLD", ROSE)).arrange(LEFT, buff=0.3)
        law1.move_to([-3.3, 0.3, 0])
        box1 = SurroundingRectangle(law1, color=GREEN, corner_radius=0.15, buff=0.2)
        self.sfx("ding")
        self.play(FadeIn(law1, shift=LEFT * 0.4), Create(box1), run_time=1.0)
        self.wait(max(d - 1.8, 0.2))

        d = self.seg("tri3")
        self.play(FadeOut(doigt), run_time=0.5)
        law2 = VGroup(ar("السرعة", 26, "BOLD", BLUE), num("=", 32),
                      ar("المسافة ÷ الزمن", 26, "BOLD", INK)).arrange(LEFT, buff=0.25)
        law2.move_to([-3.3, -0.8, 0])
        law3 = VGroup(ar("الزمن", 26, "BOLD", ROSE), num("=", 32),
                      ar("المسافة ÷ السرعة", 26, "BOLD", INK)).arrange(LEFT, buff=0.25)
        law3.move_to([-3.3, -1.8, 0])
        self.sfx("pop")
        self.play(FadeIn(law2, shift=LEFT * 0.4), run_time=0.9)
        self.sfx("pop")
        self.play(FadeIn(law3, shift=LEFT * 0.4), run_time=0.9)
        self.wait(max(d - 2.3, 0.2))
        self.clear_all()

    # ── 5. قطار الحديد : 42 km/h في 1h40 ────────────────────────
    def s_train(self):
        d = self.seg("train1")
        head = titled("قطار الحديد: 42 km/h — كم يقطع في 1h40؟", 30, GOLD)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        loco = VGroup(voiture(GOLD, 2.0),
                      voiture(LILA, 1.6).shift(RIGHT * 2.0),
                      voiture(LILA, 1.6).shift(RIGHT * 3.8))
        loco.move_to([0.2, 0.6, 0])
        rail = Line([6.0, 0.05, 0], [-6.0, 0.05, 0], color=INK, stroke_width=4)
        self.play(Create(rail), run_time=0.7)
        self.sfx("whoosh")
        self.play(FadeIn(loco, shift=LEFT * 1.2), run_time=1.2)
        self.wait(max(d - 2.8, 0.2))

        d = self.seg("train2")
        conv = VGroup(ar("ساعة و40 دقيقة", 28, "BOLD"), num("=", 34),
                      num("60", 36, BLUE), num("+", 32, GREEN), num("40", 36, BLUE),
                      num("=", 34), num("100", 44, GOLD),
                      ar("دقيقة", 28, "BOLD", GOLD)).arrange(LEFT, buff=0.28)
        conv.move_to([0, -1.2, 0])
        box = SurroundingRectangle(conv, color=GOLD, corner_radius=0.15, buff=0.22)
        self.sfx("ding")
        self.play(FadeIn(conv, shift=UP * 0.3), Create(box), run_time=1.2)
        self.wait(max(d - 1.2, 0.2))

        d = self.seg("train3")
        calc = VGroup(num("42", 38), ar("×", 28, "BOLD", GOLD), num("100", 38),
                      ar("÷", 28, "BOLD", ROSE), num("60", 38),
                      num("=", 36), num("70", 48, GREEN),
                      ar("كيلومترًا", 28, "BOLD", GREEN)).arrange(LEFT, buff=0.28)
        calc.move_to([0, -2.5, 0])
        box2 = SurroundingRectangle(calc, color=GREEN, corner_radius=0.15, buff=0.22)
        self.sfx("ding")
        self.play(FadeIn(calc, shift=UP * 0.3), Create(box2), run_time=1.2)
        self.play(Flash(calc[6], color=GREEN, flash_radius=1.2), run_time=0.8)
        self.wait(max(d - 2.0, 0.2))
        self.clear_all()

    # ── 6. انتبه : حوّل الوحدات قبل الحساب ──────────────────────
    def s_attention(self):
        d = self.seg("att1")
        head = titled("انتبه! حوّل الوحدات قبل الحساب", 34, REDA)
        garcon = self.boy(1.9).to_edge(LEFT, buff=0.25).shift(DOWN * 1.3)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE),
                  FadeIn(garcon, shift=RIGHT * 0.8, rate_func=BOUNCE), run_time=1.0)
        c1 = RoundedRectangle(corner_radius=0.22, width=6.6, height=1.1, fill_color=REDA,
                              fill_opacity=0.92, stroke_color=INK).move_to(RIGHT * 2.3 + UP * 0.5)
        c1t = VGroup(ar("ساعة و40 دقيقة ≠", 26, "BOLD", "#FFFFFF"),
                     num("140", 32, "#FFFFFF")).arrange(LEFT, buff=0.25).move_to(c1)
        c2 = RoundedRectangle(corner_radius=0.22, width=6.6, height=1.1, fill_color=GREEN,
                              fill_opacity=0.92, stroke_color=INK).move_to(RIGHT * 2.3 + DOWN * 0.9)
        c2t = VGroup(ar("بل =", 26, "BOLD", "#FFFFFF"),
                     num("100", 32, "#FFFFFF"),
                     ar("دقيقة", 26, "BOLD", "#FFFFFF")).arrange(LEFT, buff=0.25).move_to(c2)
        self.sfx("boing")
        self.play(GrowFromCenter(VGroup(c1, c1t), rate_func=BOUNCE), run_time=0.9)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(c2, c2t), rate_func=BOUNCE), run_time=0.9)
        self.play(Wiggle(garcon), run_time=1.1)
        self.wait(max(d - 3.9, 0.2))
        self.clear_all()

    # ── 7. السر : 60 km/h = 1 km في الدقيقة ─────────────────────
    def s_astuce(self):
        d = self.seg("astuce")
        head = titled("سرّ ذهبي: 60 km/h = كيلومتر في الدقيقة", 30, LILA)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=1.0)
        self.wait(1.6)
        rows = [("في ساعة كاملة", "60 km", BLUE),
                ("في نصف ساعة", "30 km", GREEN),
                ("في دقيقة واحدة", "1 km", GOLD)]
        t = 0
        for i, (txt, val, col) in enumerate(rows):
            c = RoundedRectangle(corner_radius=0.22, width=7.4, height=1.05,
                                 fill_color=col, fill_opacity=0.92,
                                 stroke_color=INK).move_to([0, 0.65 - 1.3 * i, 0])
            ct = ar(txt, 27, "BOLD", "#FFFFFF").move_to(c.get_center() + RIGHT * 1.7)
            cv = num(val, 34, "#FFFFFF").move_to(c.get_center() + LEFT * 2.2)
            self.sfx("pop")
            self.play(GrowFromCenter(VGroup(c, ct, cv), rate_func=BOUNCE), run_time=0.9)
            t += 0.9
        self.wait(max(d - 1.6 - t, 0.2))
        self.clear_all()

    def construct(self):
        self.setup_common()
        self.s_intro_card("intro1")
        self.s_objectifs("intro2", [
            "أفهم السرعة المتوسطة (km/h)",
            "أحفظ مثلث السرعة والمسافة والزمن",
            "أحوّل الوحدات قبل الحساب",
        ])
        self.s_concept()
        self.s_velo()
        self.s_triangle()
        self.s_train()
        self.s_attention()
        self.s_astuce()
        self.s_outro_end("outro")
