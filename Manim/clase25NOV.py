from manim import *

class WriteText(Scene):
    def construct(self):
        text = Text("This is a regular Text")
        self.play(Write(text))
        self.wait(3)

class AddText(Scene):
    def construct(self):
        text = Text("This is a regular text")
        self.add(text)
        self.wait(3)

class Formula(Scene):
    def construct(self):
        formula = MathTex("x^2 + y^2 = z^2")
        self.play(Write(formula))
        self.wait(3)

class TypesOfText(Scene):
    def construct(self):
        types_of_text = Tex(
            "This is a regular text,\\ $\\frac{x}{y}$,\\ $$x^2 + y^2 = a^2$$"
        )
        self.play(Write(types_of_text))
        self.wait(3)

class TextInCenter(Scene):
    def construct(self):
        text = Text("Text")
        self.play(Write(text))
        self.wait(3)

class TextOnEdges(Scene):
    def construct(self):
        top_text = Text("Top").to_edge(UP)
        bottom_text = Text("Bottom").to_edge(DOWN)
        right_text = Text("Right").to_edge(RIGHT)
        left_text = Text("Left").to_edge(LEFT)
        self.play(Write(top_text), Write(bottom_text), Write(right_text), Write(left_text))
        self.wait(3)

class TextInCorners(Scene):
    def construct(self):
        upper_right = Text("Upper Right").to_corner(UP + RIGHT)
        lower_left = Text("Lower Left").to_corner(DOWN + LEFT)
        self.play(Write(upper_right), Write(lower_left))
        self.wait(3)

class CustomPosition(Scene):
    def construct(self):
        text1 = Text("Text at custom position").move_to(UP + RIGHT)
        text2 = Text("Central Text")
        self.play(Write(text1), Write(text2))
        self.wait(3)

class RotateObject(Scene):
    def construct(self):
        text = Text("Rotating Text").shift(UP)
        self.play(Write(text))
        for _ in range(4):
            self.play(Rotate(text, PI / 4))
        self.wait(3)

class MirrorObject(Scene):
    def construct(self):
        text = Text("Mirrored Text")
        text.flip(UP)
        self.play(Write(text))
        self.wait(3)

class TextSizes(Scene):
    def construct(self):
        sizes = ["\Huge Huge", "\huge huge", "\LARGE LARGE", "\Large Large", "\large large", 
                 "\normalsize normal", "\small small", "\footnotesize footnotesize", 
                 "\scriptsize scriptsize", "\tiny tiny"]
        texts = [Tex(size) for size in sizes]
        for i, text in enumerate(texts):
            if i == 0:
                text.to_edge(UP)
            else:
                text.next_to(texts[i-1], DOWN, buff=0.2)
            self.add(text)
        self.wait(3)

class TextFonts(Scene):
    def construct(self):
        fonts = [
            "{\rmfamily Roman serif}", "\textit{Italic}", "\texttt{Typewriter}", 
            "\textbf{Bold}", "\textsl{Slanted}", "\textsc{Small Caps}"
        ]
        texts = [Tex(font) for font in fonts]
        for i, text in enumerate(texts):
            if i == 0:
                text.to_edge(UP)
            else:
                text.next_to(texts[i-1], DOWN, buff=0.2)
            self.add(text)
        self.wait(3)
