# -*- coding: utf-8 -*-
"""Vidéo U13 — الشراء والبيع.  Rendu : venv/bin/manim -qh scene_u13.py VideoU13
Cœur de la vidéo : le commerce se VOIT — la pièce d'or passe du تاجر à la سلعة
(ثمن الشراء) puis revient plus grosse (ثمن البيع), et le ربح apparaît sur le
نموذج الشريط : la barre du بيع dépasse la barre du شراء, le morceau en plus = الربح."""
from manim import (VGroup, Rectangle, RoundedRectangle, Circle, Line,
                   SurroundingRectangle, Brace,
                   FadeIn, FadeOut, Write, Create, Transform, ReplacementTransform,
                   GrowFromCenter, Indicate, Wiggle, Flash, LaggedStart,
                   UP, DOWN, LEFT, RIGHT)

from video_common import (MajorScene, ar, num, titled,
                          INK, YELL, ROSE, GREEN, BLUE, LILA, REDA, GOLD, BOUNCE, HERE)

X_RIGHT = 4.6          # bord droit commun des barres (RTL : elles poussent vers la gauche)
SCALE = 90.0           # 1 unité écran = 90 أوقية


def coin(value, r=0.42):
    c = Circle(radius=r, fill_color=GOLD, fill_opacity=1, stroke_color=INK, stroke_width=3)
    t = num(str(value), int(r * 60), "#FFFFFF").move_to(c)
    return VGroup(c, t)


def money_bar(value, color, label_txt, y):
    """Barre proportionnelle à `value`, alignée à droite (RTL), étiquette à droite."""
    w = value / SCALE
    r = Rectangle(width=w, height=0.85, fill_color=color, fill_opacity=0.92,
                  stroke_color=INK, stroke_width=2.5)
    r.move_to([X_RIGHT - w / 2, y, 0])
    lab = ar(label_txt, 26, "BOLD", color).next_to([X_RIGHT, y, 0], RIGHT, buff=0.25)
    val = num(str(value), 34, "#FFFFFF").move_to(r)
    return VGroup(r, lab, val)


def article(label_txt, color):
    """Une سلعة : paquet coloré avec son nom."""
    box = RoundedRectangle(corner_radius=0.18, width=1.7, height=1.25,
                           fill_color=color, fill_opacity=0.92,
                           stroke_color=INK, stroke_width=2.5)
    rib = Rectangle(width=0.3, height=1.25, fill_color="#FFFFFF", fill_opacity=0.55,
                    stroke_width=0).move_to(box)
    t = ar(label_txt, 24, "BOLD", INK).next_to(box, DOWN, buff=0.22)
    return VGroup(box, rib, t)


class VideoU13(MajorScene):
    AUDIO = HERE / "audio_u13"
    UNIT_AR = "الوحدة 13"
    UNIT_COLOR = GOLD
    TITLE = "الشراء والبيع"
    OUTRO_CALL = "والآن افتح كراسك وحلّ تمارين الوحدة 13"

    # ── 2. في السوق : ثمن الشراء / ثمن البيع ────────────────────
    def s_souk(self):
        d = self.seg("def1")
        head = titled("في السوق: أشتري ثم أبيع", 36, GOLD)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        garcon = self.boy(2.0).move_to([4.6, -1.4, 0])
        sac = article("السلعة", BLUE).move_to([-3.6, -1.2, 0])
        self.sfx("pop")
        self.play(FadeIn(garcon, scale=0.4, rate_func=BOUNCE),
                  FadeIn(sac, scale=0.4, rate_func=BOUNCE), run_time=1.0)
        # la pièce voyage du تاجر vers la سلعة = ثمن الشراء
        c = coin(180).move_to([3.6, -0.4, 0])
        self.sfx("pop")
        self.play(FadeIn(c, scale=0.4, rate_func=BOUNCE), run_time=0.7)
        self.sfx("whoosh")
        self.play(c.animate.move_to([-2.2, -0.3, 0]), run_time=1.3)
        lab1 = ar("ثمن الشراء", 30, "BOLD", ROSE).move_to([0.6, 0.9, 0])
        fl1 = SurroundingRectangle(lab1, color=ROSE, corner_radius=0.15, buff=0.2)
        self.sfx("ding")
        self.play(FadeIn(lab1), Create(fl1), run_time=0.9)
        self.wait(max(d - 4.8, 0.2))

        d = self.seg("def2")
        # la سلعة part vers le client, une pièce plus grosse revient = ثمن البيع
        self.sfx("whoosh")
        self.play(FadeOut(c), sac.animate.move_to([-5.4, -1.2, 0]), run_time=1.0)
        c2 = coin(250, 0.5).move_to([-4.2, -0.3, 0])
        self.sfx("pop")
        self.play(FadeIn(c2, scale=0.4, rate_func=BOUNCE), run_time=0.7)
        self.sfx("whoosh")
        self.play(c2.animate.move_to([3.4, -0.3, 0]), run_time=1.3)
        lab2 = ar("ثمن البيع", 30, "BOLD", GREEN).move_to([0.6, -2.6, 0])
        fl2 = SurroundingRectangle(lab2, color=GREEN, corner_radius=0.15, buff=0.2)
        self.sfx("ding")
        self.play(FadeIn(lab2), Create(fl2), run_time=0.9)
        self.wait(max(d - 3.9, 0.2))

        d = self.seg("def3")
        self.play(Indicate(VGroup(lab2, fl2), color=GREEN, scale_factor=1.15),
                  run_time=1.0)
        self.play(Indicate(VGroup(lab1, fl1), color=ROSE, scale_factor=1.15),
                  run_time=1.0)
        self.play(Wiggle(garcon), run_time=1.1)
        self.wait(max(d - 3.1, 0.2))
        self.clear_all()

    # ── 3. القاعدة الأولى ───────────────────────────────────────
    def s_formule(self):
        d = self.seg("form1")
        head = titled("القاعدة: الربح = البيع − الشراء", 34, GREEN)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        eq = VGroup(ar("الربح", 40, "BOLD", GREEN),
                    num("=", 46),
                    ar("ثمن البيع", 40, "BOLD", BLUE),
                    num("−", 46, REDA),
                    ar("ثمن الشراء", 40, "BOLD", ROSE)).arrange(LEFT, buff=0.45)
        eq.move_to([0, 0.3, 0])
        box = RoundedRectangle(corner_radius=0.25, width=eq.width + 1.2, height=1.7,
                               fill_color="#FFFFFF", fill_opacity=0.85,
                               stroke_color=GREEN, stroke_width=4).move_to(eq)
        self.sfx("ding")
        self.play(GrowFromCenter(box, rate_func=BOUNCE), Write(eq), run_time=1.6)
        self.play(Flash(eq, color=GREEN, flash_radius=2.4), run_time=0.8)
        self.wait(max(d - 2.4, 0.2))
        self.clear_all()

    # ── 4. مثال الربح : كتاب 180 → 250 (نموذج الشريط) ───────────
    def s_ribh(self):
        d = self.seg("ex1")
        head = titled("مثال: كتاب اشتُري بـ 180 وبِيع بـ 250", 32, BLUE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        livre = article("كتاب", BLUE).move_to([-5.0, 0.4, 0])
        self.sfx("pop")
        self.play(FadeIn(livre, scale=0.4, rate_func=BOUNCE), run_time=0.8)
        b_achat = money_bar(180, ROSE, "الشراء", 0.9)
        b_vente = money_bar(250, GREEN, "البيع", -0.5)
        self.sfx("pop")
        self.play(FadeIn(b_achat, shift=LEFT * 0.5, rate_func=BOUNCE), run_time=1.0)
        self.sfx("pop")
        self.play(FadeIn(b_vente, shift=LEFT * 0.5, rate_func=BOUNCE), run_time=1.0)
        self.wait(max(d - 3.7, 0.2))

        d = self.seg("ex2")
        # le morceau du بيع qui dépasse le شراء = الربح
        x_left_achat = X_RIGHT - 180 / SCALE
        x_left_vente = X_RIGHT - 250 / SCALE
        extra = Rectangle(width=70 / SCALE, height=0.85, fill_color=YELL,
                          fill_opacity=1, stroke_color=INK, stroke_width=2.5)
        extra.move_to([(x_left_achat + x_left_vente) / 2, -0.5, 0])
        guide = Line([x_left_achat, 1.45, 0], [x_left_achat, -1.05, 0],
                     color=INK, stroke_width=3).set_opacity(0.5)
        self.play(Create(guide), run_time=0.7)
        self.sfx("boing")
        self.play(FadeIn(extra, scale=0.5, rate_func=BOUNCE), run_time=0.9)
        lab = ar("الربح", 28, "BOLD", GOLD).next_to(extra, DOWN, buff=0.3)
        self.play(FadeIn(lab, shift=UP * 0.2), run_time=0.7)
        calc = VGroup(num("250", 42), num("−", 40, REDA), num("180", 42),
                      num("=", 40), num("70", 50, GREEN),
                      ar("أوقية", 28, "BOLD", GREEN)).arrange(LEFT, buff=0.3)
        calc.move_to([0.0, -2.4, 0])
        box = SurroundingRectangle(calc, color=GREEN, corner_radius=0.15, buff=0.22)
        self.sfx("ding")
        self.play(FadeIn(calc, shift=UP * 0.3), Create(box), run_time=1.1)
        self.play(Flash(calc[4], color=GREEN, flash_radius=1.3), run_time=0.8)
        self.wait(max(d - 4.3, 0.2))
        self.clear_all()

    # ── 5. مثال الخسارة : إبريق أتاي 350 → 300 ──────────────────
    def s_khasara(self):
        d = self.seg("loss1")
        head = titled("وإذا بِعتُ بثمن أقل؟ الخسارة!", 34, REDA)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        ibr = article("إبريق أتاي", LILA).move_to([-5.0, 0.4, 0])
        self.sfx("pop")
        self.play(FadeIn(ibr, scale=0.4, rate_func=BOUNCE), run_time=0.8)
        b_achat = money_bar(350, ROSE, "الشراء", 0.9)
        b_vente = money_bar(300, GREEN, "البيع", -0.5)
        self.sfx("pop")
        self.play(FadeIn(b_achat, shift=LEFT * 0.5, rate_func=BOUNCE), run_time=1.0)
        self.sfx("pop")
        self.play(FadeIn(b_vente, shift=LEFT * 0.5, rate_func=BOUNCE), run_time=1.0)
        self.wait(max(d - 3.7, 0.2))

        d = self.seg("loss2")
        # cette fois c'est le شراء qui dépasse : le morceau rouge = الخسارة
        x_left_achat = X_RIGHT - 350 / SCALE
        x_left_vente = X_RIGHT - 300 / SCALE
        manque = Rectangle(width=50 / SCALE, height=0.85, fill_color=REDA,
                           fill_opacity=1, stroke_color=INK, stroke_width=2.5)
        manque.move_to([(x_left_achat + x_left_vente) / 2, 0.9, 0])
        self.sfx("boing")
        self.play(FadeIn(manque, scale=0.5, rate_func=BOUNCE), run_time=0.9)
        lab = ar("الخسارة", 28, "BOLD", REDA).next_to(manque, UP, buff=0.25)
        self.play(FadeIn(lab, shift=DOWN * 0.2), run_time=0.7)
        calc = VGroup(num("350", 42), num("−", 40, REDA), num("300", 42),
                      num("=", 40), num("50", 50, REDA),
                      ar("أوقية", 28, "BOLD", REDA)).arrange(LEFT, buff=0.3)
        calc.move_to([0.0, -2.4, 0])
        box = SurroundingRectangle(calc, color=REDA, corner_radius=0.15, buff=0.22)
        self.sfx("ding")
        self.play(FadeIn(calc, shift=UP * 0.3), Create(box), run_time=1.1)
        rule = ar("الخسارة = الشراء − البيع", 28, "BOLD", REDA).move_to([-4.3, -1.1, 0])
        self.play(FadeIn(rule, shift=UP * 0.3), run_time=0.9)
        self.wait(max(d - 3.6, 0.2))
        self.clear_all()

    # ── 6. الكلفة : الشراء + المصاريف ───────────────────────────
    def s_kulfa(self):
        d = self.seg("cost1")
        head = titled("الكلفة = الشراء + المصاريف", 34, LILA)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        eq = VGroup(ar("الكلفة", 36, "BOLD", LILA),
                    num("=", 42),
                    ar("ثمن الشراء", 36, "BOLD", ROSE),
                    num("+", 42, GREEN),
                    ar("المصاريف", 36, "BOLD", BLUE)).arrange(LEFT, buff=0.4)
        eq.move_to([0, 1.3, 0])
        self.sfx("ding")
        self.play(Write(eq), run_time=1.4)
        self.wait(max(d - 2.3, 0.2))

        d = self.seg("cost2")
        # 500 (شراء) + 50 (نقل) côte à côte → une barre الكلفة 550
        p1 = Rectangle(width=500 / SCALE, height=0.85, fill_color=ROSE, fill_opacity=0.92,
                       stroke_color=INK, stroke_width=2.5)
        p1.move_to([X_RIGHT - 500 / SCALE / 2, -0.1, 0])
        v1 = num("500", 34, "#FFFFFF").move_to(p1)
        p2 = Rectangle(width=50 / SCALE, height=0.85, fill_color=BLUE, fill_opacity=0.92,
                       stroke_color=INK, stroke_width=2.5)
        p2.next_to(p1, LEFT, buff=0)
        v2 = num("50", 24, "#FFFFFF").move_to(p2)
        l2 = ar("النقل", 24, "BOLD", BLUE).next_to(p2, UP, buff=0.2)
        self.sfx("pop")
        self.play(FadeIn(VGroup(p1, v1), shift=LEFT * 0.5, rate_func=BOUNCE), run_time=0.9)
        self.sfx("pop")
        self.play(FadeIn(VGroup(p2, v2, l2), scale=0.5, rate_func=BOUNCE), run_time=0.9)
        br = Brace(VGroup(p1, p2), DOWN, color=LILA)
        bt = VGroup(ar("الكلفة:", 28, "BOLD", LILA), num("550", 40, LILA)
                    ).arrange(LEFT, buff=0.25).next_to(br, DOWN, buff=0.25)
        self.sfx("ding")
        self.play(GrowFromCenter(br), FadeIn(bt, shift=UP * 0.2), run_time=1.0)
        self.wait(max(d - 2.8, 0.2))

        d = self.seg("cost3")
        calc = VGroup(num("620", 42), num("−", 40, REDA), num("550", 42),
                      num("=", 40), num("70", 50, GREEN),
                      ar("أوقية ربحًا", 28, "BOLD", GREEN)).arrange(LEFT, buff=0.3)
        calc.move_to([0.0, -2.55, 0])
        box = SurroundingRectangle(calc, color=GREEN, corner_radius=0.15, buff=0.22)
        self.sfx("ding")
        self.play(FadeIn(calc, shift=UP * 0.3), Create(box), run_time=1.1)
        self.play(Flash(calc[4], color=GREEN, flash_radius=1.3), run_time=0.8)
        self.wait(max(d - 1.9, 0.2))
        self.clear_all()

    # ── 7. انتبه : الربح يُحسب من الكلفة ────────────────────────
    def s_attention(self):
        d = self.seg("att1")
        head = titled("انتبه! لا تنسَ المصاريف", 36, REDA)
        garcon = self.boy(1.9).to_edge(LEFT, buff=0.25).shift(DOWN * 1.3)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE),
                  FadeIn(garcon, shift=RIGHT * 0.8, rate_func=BOUNCE), run_time=1.0)
        c1 = RoundedRectangle(corner_radius=0.22, width=6.6, height=1.1, fill_color=GREEN,
                              fill_opacity=0.92, stroke_color=INK).move_to(RIGHT * 2.3 + UP * 0.5)
        c1t = ar("الربح الحقيقي = البيع − الكلفة", 26, "BOLD", "#FFFFFF").move_to(c1)
        c2 = RoundedRectangle(corner_radius=0.22, width=6.6, height=1.1, fill_color=REDA,
                              fill_opacity=0.92, stroke_color=INK).move_to(RIGHT * 2.3 + DOWN * 0.9)
        c2t = ar("لا أحسبه من الشراء وحده!", 26, "BOLD", "#FFFFFF").move_to(c2)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(c1, c1t), rate_func=BOUNCE), run_time=0.9)
        self.sfx("boing")
        self.play(GrowFromCenter(VGroup(c2, c2t), rate_func=BOUNCE), run_time=0.9)
        self.play(Wiggle(garcon), run_time=1.1)
        self.wait(max(d - 3.9, 0.2))
        self.clear_all()

    # ── 8. السر : قارن البيع بالشراء ────────────────────────────
    def s_astuce(self):
        d = self.seg("astuce")
        head = titled("سرّ ذهبي: قارن البيع بالشراء", 36, LILA)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=1.0)
        self.wait(1.8)
        c1 = RoundedRectangle(corner_radius=0.22, width=6.2, height=1.15, fill_color=GREEN,
                              fill_opacity=0.92, stroke_color=INK).move_to(UP * 0.55)
        c1t = ar("البيع أكبر ← ربح", 30, "BOLD", "#FFFFFF").move_to(c1)
        c2 = RoundedRectangle(corner_radius=0.22, width=6.2, height=1.15, fill_color=REDA,
                              fill_opacity=0.92, stroke_color=INK).move_to(DOWN * 0.85)
        c2t = ar("البيع أصغر ← خسارة", 30, "BOLD", "#FFFFFF").move_to(c2)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(c1, c1t), rate_func=BOUNCE), run_time=1.0)
        self.wait(2.2)
        self.sfx("boing")
        self.play(GrowFromCenter(VGroup(c2, c2t), rate_func=BOUNCE), run_time=1.0)
        self.wait(max(d - 6.0, 0.2))
        self.clear_all()

    def construct(self):
        self.setup_common()
        self.s_intro_card("intro1")
        self.s_objectifs("intro2", [
            "أفرّق بين ثمن الشراء وثمن البيع",
            "أحسب الربح والخسارة بالأوقية",
            "أحسب الكلفة: الشراء + المصاريف",
        ])
        self.s_souk()
        self.s_formule()
        self.s_ribh()
        self.s_khasara()
        self.s_kulfa()
        self.s_attention()
        self.s_astuce()
        self.s_outro_end("outro")
