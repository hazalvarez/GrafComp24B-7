from manim import *
import numpy as np

class Grid(VGroup):
    def __init__(self, rows=1, columns=1, width=6.0, height=6.0, **kwargs):
        super().__init__(**kwargs)

        # Asegurar que rows y columns no sean cero
        self.rows = max(1, rows)
        self.columns = max(1, columns)
        self.width = width
        self.height = height

        # Calcular el paso solo si las filas y columnas no son cero
        x_step = self.width / self.columns
        y_step = self.height / self.rows

        # Crear líneas verticales
        for x in np.arange(0, self.width + x_step, x_step):
            self.add(Line(
                [x - self.width / 2., -self.height / 2., 0],
                [x - self.width / 2., self.height / 2., 0],
            ))

        # Crear líneas horizontales
        for y in np.arange(0, self.height + y_step, y_step):
            self.add(Line(
                [-self.width / 2., y - self.height / 2., 0],
                [self.width / 2., y - self.height / 2., 0],
            ))

class ScreenGrid(VGroup):
    def __init__(self, rows=8, columns=14, width=14, height=None, grid_stroke=0.5, 
                 grid_color=WHITE, axis_color=RED, axis_stroke=2, labels_scale=0.25, 
                 labels_buff=0, number_decimals=2, **kwargs):
        super().__init__(**kwargs)

        self.rows = max(1, rows)  # Evitar cero
        self.columns = max(1, columns)  # Evitar cero
        self.width = width
        self.height = height if height is not None else config.frame_height
        self.grid_stroke = grid_stroke
        self.grid_color = grid_color
        self.axis_color = axis_color
        self.axis_stroke = axis_stroke
        self.labels_scale = labels_scale
        self.labels_buff = labels_buff
        self.number_decimals = number_decimals

        # Crear la rejilla (grid)
        grid = Grid(width=self.width, height=self.height, rows=self.rows, columns=self.columns)
        grid.set_stroke(self.grid_color, self.grid_stroke)

        # Crear los ejes
        axes_x = Line(LEFT * self.width / 2, RIGHT * self.width / 2)
        axes_y = Line(DOWN * self.height / 2, UP * self.height / 2)
        axes = VGroup(axes_x, axes_y).set_stroke(self.axis_color, self.axis_stroke)

        # Crear etiquetas para las divisiones
        divisions_x = self.width / self.columns
        divisions_y = self.height / self.rows

        labels = VGroup()

        # Crear etiquetas para cada división
        for i in range(self.columns):
            for j in range(self.rows):
                x_label = Text(f"{round((i+1) * divisions_x - self.width / 2, self.number_decimals)}").scale(self.labels_scale)
                y_label = Text(f"{round((j+1) * divisions_y - self.height / 2, self.number_decimals)}").scale(self.labels_scale)
                labels.add(x_label, y_label)

        self.add(grid, axes, labels)

class CoordScreen(Scene):
    def construct(self):
        screen_grid = ScreenGrid()
        dot = Dot([1, 1, 0])
        self.add(screen_grid)
        self.play(FadeIn(dot))
        self.wait()
