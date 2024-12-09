from manim import *
class Ecuacion(Scene):
    def construct(self):
        text = MathTex(r"x = \frac {-b \pm \sqrt{b^2 -4ac}}{2a}")
        self.add(text)

#Revisado
