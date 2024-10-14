from manim import *


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(BLUE, opacity=.1)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.rotate(PI / 2)  # rotate a certain amount

        self.play(Create(circle))  # animate the creation of the square
        self.play(Transform(circle, square))  # interpolate the square into the circle
        self.play(FadeOut(circle))  # fade out animation

class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(YELLOW, opacity=0.5)  # set the color and transparency

        circle2 = Circle()  # create a circle
        circle2.set_fill(RED, opacity=0.5)  # set the color and transparency

        square = Square()  # create a square
        square.set_fill(BLUE, opacity=0.5)  # set the color and transparency
        square.shift(LEFT * 6 + UP * 3)

        square2 = Square()  # create a square
        square2.set_fill(GRAY, opacity=0.5)  # set the color and transparency

        circle.next_to(square, DOWN, buff=4)  # set the position
        square2.next_to(circle, RIGHT, buff=10)  # set the position
        circle2.next_to(square, RIGHT, buff=10)  # set the position
        self.play(Create(square), Create(circle), Create(square2), Create(circle2))  # show the shapes on screen