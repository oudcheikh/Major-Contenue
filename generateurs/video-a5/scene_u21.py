# -*- coding: utf-8 -*-
"""Vidéo U21 — التناسبية.  Rendu : venv/bin/manim -qh scene_u21.py VideoU21
Cœur de la vidéo : le جدول التناسبية se REMPLIT à l'écran — 5 خبزات = 75 أوقية,
la flèche ×15 (معامل الضرب) descend du السطر الأول au الثاني, puis 3×15=45 et
11×15=165 volent dans leurs cases ; enfin القاعدة الثلاثية sur قماش الملحفة."""
from manim import (VGroup, Rectangle, RoundedRectangle, Line, CurvedArrow,
                   SurroundingRectangle,
                   FadeIn, FadeOut, Write, Create, Transform, ReplacementTransform,
                   GrowFromCenter, Indicate, Wiggle, Flash, LaggedStart,
                   UP, DOWN, LEFT, RIGHT, PI)

from video_common import (MajorScene, ar, num, titled,
                          INK, YELL, ROSE, GREEN, BLUE, LILA, REDA, GOLD, BOUNCE, HERE)


def table(headers, cols, col_w=1.7, row_h=1.0, head_w=3.3):
    """Jadwal RTL : colonne d'en-têtes à DROITE, données vers la gauche.
    headers = [txt sطر 1, txt سطر 2] ; cols = liste de colonnes [haut, bas] (droite → gauche).
    Retourne (VGroup cadre+entêtes, positions des cellules [ligne][colonne])."""
    n = len(cols)
    w = head_w + n * col_w
    x_right = w / 2
    g = VGroup()
    # cadre + lignes
    frame = Rectangle(width=w, height=2 * row_h, stroke_color=INK, stroke_width=3,
                      fill_color="#FFFFFF", fill_opacity=0.85)
    g.add(frame)
    g.add(Line([x_right - head_w, row_h, 0], [x_right - head_w, -row_h, 0],
               color=INK, stroke_width=3))
    for i in range(1, n):
        x = x_right - head_w - i * col_w
        g.add(Line([x, row_h, 0], [x, -row_h, 0], color=INK, stroke_width=2))
    g.add(Line([x_right, 0, 0], [-x_right, 0, 0], color=INK, stroke_width=2))
    # en-têtes (fond coloré)
    h1 = Rectangle(width=head_w, height=row_h, fill_color=BLUE, fill_opacity=0.9,
                   stroke_width=0).move_to([x_right - head_w / 2, row_h / 2, 0])
    h2 = Rectangle(width=head_w, height=row_h, fill_color=GREEN, fill_opacity=0.9,
                   stroke_width=0).move_to([x_right - head_w / 2, -row_h / 2, 0])
    t1 = ar(headers[0], 24, "BOLD", "#FFFFFF").move_to(h1)
    t2 = ar(headers[1], 24, "BOLD", "#FFFFFF").move_to(h2)
    g.add(h1, h2, t1, t2)
    cells = [[], []]
    for i in range(n):
        x = x_right - head_w - i * col_w + col_w / 2 - col_w
        x = x_right - head_w - (i + 0.5) * col_w
        cells[0].append([x, row_h / 2, 0])
        cells[1].append([x, -row_h / 2, 0])
    return g, cells


class VideoU21(MajorScene):
    AUDIO = HERE / "audio_u21"
    UNIT_AR = "الوحدة 21"
    UNIT_COLOR = BLUE
    TITLE = "التناسبية"
    OUTRO_CALL = "والآن افتح كراسك وحلّ تمارين الوحدة 21"

    # ── 2. التعريف : الضرب في نفس العدد ─────────────────────────
    def s_def(self):
        d = self.seg("def1")
        head = titled("متناسبان = أضرب في نفس العدد دائمًا", 32, BLUE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        row1 = VGroup(num("2", 44), num("5", 44), num("8", 44)).arrange(LEFT, buff=1.6)
        row1.move_to([0.6, 0.8, 0])
        row2 = VGroup(num("6", 44, GREEN), num("15", 44, GREEN),
                      num("24", 44, GREEN)).arrange(LEFT, buff=1.35)
        for a, b in zip(row1, row2):
            b.move_to([a.get_center()[0], -1.0, 0])
        self.sfx("pop")
        self.play(FadeIn(row1, shift=LEFT * 0.4, rate_func=BOUNCE), run_time=0.9)
        arrows = VGroup()
        for a, b in zip(row1, row2):
            fl = CurvedArrow(a.get_bottom() + DOWN * 0.1, b.get_top() + UP * 0.1,
                             angle=-PI / 4, color=GOLD, stroke_width=4)
            arrows.add(fl)
        lab = ar("× 3", 30, "BOLD", GOLD).move_to([4.3, -0.1, 0])
        self.sfx("whoosh")
        self.play(LaggedStart(*[Create(a) for a in arrows], lag_ratio=0.25),
                  FadeIn(lab, scale=0.6), run_time=1.3)
        self.sfx("pop")
        self.play(LaggedStart(*[FadeIn(x, scale=0.4, rate_func=BOUNCE) for x in row2],
                              lag_ratio=0.25), run_time=1.2)
        self.wait(max(d - 3.4, 0.2))
        self.clear_all()

    # ── 3. جدول التناسبية : الخبزات ─────────────────────────────
    def s_tableau(self):
        d = self.seg("tab1")
        head = titled("من السوق: 5 خبزات بـ 75 أوقية", 34, GREEN)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        q = ar("ما ثمن 3 خبزات؟ وما ثمن 11 خبزة؟", 30, "BOLD", GOLD).move_to([0, 1.6, 0])
        self.sfx("pop")
        self.play(FadeIn(q, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        self.wait(max(d - 1.8, 0.2))

        d = self.seg("tab2")
        tab, cells = table(["عدد الخبزات", "الثمن بالأوقية"], [None, None, None])
        tab.move_to([0, -0.6, 0])
        off = tab.get_center() - [0, 0, 0]
        # positions absolues des cellules
        C = [[[p[0] + off[0], p[1] + off[1], 0] for p in row] for row in cells]
        self.sfx("whoosh")
        self.play(Create(tab), run_time=1.6)
        n5 = num("5", 40).move_to(C[0][0])
        n75 = num("75", 40).move_to(C[1][0])
        n3 = num("3", 40).move_to(C[0][1])
        n11 = num("11", 40).move_to(C[0][2])
        q1 = num("?", 40, REDA).move_to(C[1][1])
        q2 = num("?", 40, REDA).move_to(C[1][2])
        self.sfx("pop")
        self.play(LaggedStart(*[FadeIn(x, scale=0.4, rate_func=BOUNCE)
                                for x in (n5, n75, n3, q1, n11, q2)],
                              lag_ratio=0.15), run_time=1.6)
        self.wait(max(d - 3.2, 0.2))

        d = self.seg("tab3")
        fl = CurvedArrow(tab.get_right() + UP * 0.5 + RIGHT * 0.1,
                         tab.get_right() + DOWN * 0.5 + RIGHT * 0.1,
                         angle=-PI / 2, color=GOLD, stroke_width=5)
        self.sfx("whoosh")
        self.play(Create(fl), run_time=0.9)
        calc = VGroup(num("75", 36), ar("÷", 28, "BOLD"), num("5", 36),
                      num("=", 34), num("15", 44, GOLD)).arrange(LEFT, buff=0.25)
        calc.next_to(fl, RIGHT, buff=0.3)
        calc.shift(LEFT * 0.1)
        self.sfx("pop")
        self.play(FadeIn(calc, shift=LEFT * 0.3), run_time=0.9)
        self.wait(max(d - 1.8, 0.2))

        d = self.seg("tab4")
        lab = VGroup(ar("معامل الضرب:", 28, "BOLD", GOLD),
                     num("× 15", 36, GOLD)).arrange(LEFT, buff=0.3)
        lab.move_to([0, -2.55, 0])
        box = SurroundingRectangle(lab, color=GOLD, corner_radius=0.15, buff=0.2)
        self.sfx("ding")
        self.play(FadeIn(lab), Create(box), run_time=1.0)
        self.play(Flash(lab, color=GOLD, flash_radius=2.0), run_time=0.8)
        self.wait(max(d - 1.8, 0.2))

        d = self.seg("tab5")
        self.play(Indicate(n3, color=GREEN, scale_factor=1.5), run_time=0.9)
        r45 = num("45", 40, GREEN).move_to(C[1][1])
        self.sfx("pop")
        self.play(ReplacementTransform(q1, r45), run_time=0.9)
        self.play(Flash(r45, color=GREEN, flash_radius=0.9), run_time=0.7)
        self.wait(max(d - 2.5, 0.2))

        d = self.seg("tab6")
        self.play(Indicate(n11, color=GREEN, scale_factor=1.5), run_time=0.9)
        r165 = num("165", 40, GREEN).move_to(C[1][2])
        self.sfx("pop")
        self.play(ReplacementTransform(q2, r165), run_time=0.9)
        self.play(Flash(r165, color=GREEN, flash_radius=0.9), run_time=0.7)
        self.wait(max(d - 2.5, 0.2))
        self.clear_all()

    # ── 4. القاعدة الثلاثية : قماش الملحفة ──────────────────────
    def s_regle3(self):
        d = self.seg("regle1")
        head = titled("القاعدة الثلاثية: أضرب ثم أقسم", 34, LILA)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        steps = VGroup()
        for i, (txt, col) in enumerate([("أنظّم في جدول", BLUE),
                                        ("أضرب المتقاطعين", GREEN),
                                        ("أقسم على الثالث", ROSE)]):
            c = RoundedRectangle(corner_radius=0.22, width=4.2, height=1.0,
                                 fill_color=col, fill_opacity=0.92,
                                 stroke_color=INK).move_to([4.55 - 4.55 * i, 1.4, 0])
            ct = ar(txt, 24, "BOLD", "#FFFFFF").move_to(c)
            steps.add(VGroup(c, ct))
        self.sfx("pop")
        self.play(LaggedStart(*[GrowFromCenter(s, rate_func=BOUNCE) for s in steps],
                              lag_ratio=0.3), run_time=1.8)
        self.wait(max(d - 2.7, 0.2))

        d = self.seg("regle2")
        tab, cells = table(["الأمتار", "الثمن"], [None, None], col_w=2.0, head_w=2.4)
        tab.move_to([0.8, -1.1, 0])
        off = tab.get_center()
        C = [[[p[0] + 0.8, p[1] - 1.1, 0] for p in row] for row in cells]
        self.sfx("whoosh")
        self.play(Create(tab), run_time=1.3)
        n4 = num("4", 38).move_to(C[0][0])
        n480 = num("480", 38).move_to(C[1][0])
        n7 = num("7", 38).move_to(C[0][1])
        qq = num("?", 38, REDA).move_to(C[1][1])
        self.sfx("pop")
        self.play(LaggedStart(*[FadeIn(x, scale=0.4, rate_func=BOUNCE)
                                for x in (n4, n480, n7, qq)], lag_ratio=0.2), run_time=1.3)
        self.wait(max(d - 2.6, 0.2))

        d = self.seg("regle3")
        diag = Line(n480.get_center(), n7.get_center(), color=GOLD,
                    stroke_width=5).set_opacity(0.7)
        self.sfx("whoosh")
        self.play(Create(diag), run_time=0.8)
        self.play(Indicate(n480, color=GOLD, scale_factor=1.4),
                  Indicate(n7, color=GOLD, scale_factor=1.4), run_time=1.0)
        c1 = VGroup(num("480", 34), ar("×", 26, "BOLD", GOLD), num("7", 34),
                    num("=", 32), num("3360", 40, GOLD)).arrange(LEFT, buff=0.25)
        c1.move_to([-4.6, -0.4, 0])
        self.sfx("pop")
        self.play(FadeIn(c1, shift=UP * 0.3), run_time=0.9)
        self.wait(max(d - 2.7, 0.2))

        d = self.seg("regle4")
        self.play(Indicate(n4, color=ROSE, scale_factor=1.4), run_time=0.9)
        c2 = VGroup(num("3360", 34), ar("÷", 26, "BOLD", ROSE), num("4", 34),
                    num("=", 32), num("840", 44, GREEN)).arrange(LEFT, buff=0.25)
        c2.move_to([-4.6, -1.6, 0])
        self.sfx("pop")
        self.play(FadeIn(c2, shift=UP * 0.3), run_time=0.9)
        r840 = num("840", 38, GREEN).move_to(C[1][1])
        self.sfx("ding")
        self.play(ReplacementTransform(qq, r840), run_time=0.9)
        self.play(Flash(r840, color=GREEN, flash_radius=1.0), run_time=0.8)
        self.wait(max(d - 2.7, 0.2))
        self.clear_all()

    # ── 5. انتبه : ليس كل شيء متناسبًا ──────────────────────────
    def s_attention(self):
        d = self.seg("att1")
        head = titled("انتبه! ليس كل شيء متناسبًا", 36, REDA)
        garcon = self.boy(1.9).to_edge(LEFT, buff=0.25).shift(DOWN * 1.3)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE),
                  FadeIn(garcon, shift=RIGHT * 0.8, rate_func=BOUNCE), run_time=1.0)
        c1 = RoundedRectangle(corner_radius=0.22, width=6.8, height=1.1, fill_color=REDA,
                              fill_opacity=0.92, stroke_color=INK).move_to(RIGHT * 2.2 + UP * 0.5)
        c1t = ar("العمر والطول لا يتناسبان!", 27, "BOLD", "#FFFFFF").move_to(c1)
        c2 = RoundedRectangle(corner_radius=0.22, width=6.8, height=1.1, fill_color=GREEN,
                              fill_opacity=0.92, stroke_color=INK).move_to(RIGHT * 2.2 + DOWN * 0.9)
        c2t = ar("في 12 سنة لست ضعف طولك في 6!", 25, "BOLD", "#FFFFFF").move_to(c2)
        self.sfx("boing")
        self.play(GrowFromCenter(VGroup(c1, c1t), rate_func=BOUNCE), run_time=0.9)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(c2, c2t), rate_func=BOUNCE), run_time=0.9)
        self.play(Wiggle(garcon), run_time=1.1)
        self.wait(max(d - 3.9, 0.2))
        self.clear_all()

    # ── 6. السر : ثمن الوحدة الواحدة ────────────────────────────
    def s_astuce(self):
        d = self.seg("astuce")
        head = titled("سرّ ذهبي: ابحث عن ثمن الوحدة", 36, LILA)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=1.0)
        self.wait(1.6)
        pain = VGroup(
            RoundedRectangle(corner_radius=0.35, width=1.5, height=0.7,
                             fill_color=GOLD, fill_opacity=0.95,
                             stroke_color=INK, stroke_width=2.5),
            ar("خبزة", 22, "BOLD", "#FFFFFF"))
        pain[1].move_to(pain[0])
        pain.move_to([2.6, 0.2, 0])
        eq = VGroup(num("=", 40), num("15", 48, GOLD),
                    ar("أوقية", 28, "BOLD", GOLD)).arrange(LEFT, buff=0.3)
        eq.next_to(pain, LEFT, buff=0.5)
        self.sfx("pop")
        self.play(FadeIn(pain, scale=0.4, rate_func=BOUNCE), run_time=0.9)
        self.sfx("ding")
        self.play(FadeIn(eq, shift=LEFT * 0.3), run_time=0.9)
        lab = ar("عرفتَ ثمن الواحدة ← سهُل كل شيء!", 30, "BOLD", GREEN)
        lab.move_to([0, -1.8, 0])
        box = SurroundingRectangle(lab, color=GREEN, corner_radius=0.15, buff=0.25)
        self.sfx("pop")
        self.play(FadeIn(lab), Create(box), run_time=1.0)
        self.wait(max(d - 3.8, 0.2))
        self.clear_all()

    def construct(self):
        self.setup_common()
        self.s_intro_card("intro1")
        self.s_objectifs("intro2", [
            "أتعرّف المقدارين المتناسبين",
            "أكمل جدول التناسبية بمعامل الضرب",
            "أستعمل القاعدة الثلاثية في المسائل",
        ])
        self.s_def()
        self.s_tableau()
        self.s_regle3()
        self.s_attention()
        self.s_astuce()
        self.s_outro_end("outro")
