from manim import Scene, SVGMobject, ImageMobject, config, LEFT, RIGHT
config.background_color = "#FFF9EF"

class TestPerso(Scene):
    def construct(self):
        f = SVGMobject("assets/perso-fille.svg").scale_to_fit_height(4).shift(LEFT * 4)
        g = SVGMobject("assets/perso-garcon.svg").scale_to_fit_height(4)
        g2 = ImageMobject("assets/perso-garcon2.png").scale_to_fit_height(4).shift(RIGHT * 4)
        self.add(f, g, g2)
