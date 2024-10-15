#Christopher Octavio Tellez Dominguez
from manim import *

class Figuras(Scene):
    def construct(self):

        cir = Circle()
        self.play(FadeIn(cir))
        self.wait(1)
        self.play(FadeOut(cir))
        self.wait(1)
        self.wait(1)

        rec = Rectangle()
        self.play(FadeIn(rec))
        self.wait(1)
        self.play(FadeOut(rec))
        self.wait(1)
        self.wait(1)

        # Primer cuadrado
        square1 = Square()
        square1.set_fill(RED, opacity=0.5)  
        square1.move_to(LEFT * 3 + UP * 2)  
        self.play(FadeIn(square1))  
        self.wait(1)
        self.play(FadeOut(square1))  
        self.wait(1)

        # Segundo cuadrado
        square2 = Square()
        square2.set_fill(BLUE, opacity=0.7)  
        square2.move_to(RIGHT * 3 + UP * 2)  
        self.play(FadeIn(square2))  
        self.wait(1)
        self.play(FadeOut(square2)) 
        self.wait(1)

        # Tercer cuadrado
        square3 = Square()
        square3.set_fill(GREEN, opacity=0.6)  
        square3.move_to(LEFT * 3 + DOWN * 2)  
        self.play(FadeIn(square3))  
        self.wait(1)
        self.play(FadeOut(square3)) 
        self.wait(1)

        # Cuarto cuadrado
        square4 = Square()
        square4.set_fill(YELLOW, opacity=0.8)  
        square4.move_to(RIGHT * 3 + DOWN * 2)  
        self.play(FadeIn(square4)) 
        self.wait(1)
        self.play(FadeOut(square4))  
        self.wait(1)

        # Quinto cuadrado
        square5 = Square()
        square5.set_fill(PURPLE, opacity=0.5) 
        square5.move_to(ORIGIN) 
        self.play(FadeIn(square5))  
        self.wait(1)
        self.play(FadeOut(square5))  
        self.wait(1)

        self.play(FadeIn(square4))  
        self.play(FadeIn(square3))  
        self.play(FadeIn(square2))  
        self.play(FadeIn(square1))  
        self.wait(1)
        self.play(FadeOut(square4)) 
        self.play(FadeOut(square3)) 
        self.play(FadeOut(square2)) 
        self.play(FadeOut(square1))  
        self.wait(1)



