from manim import *

COLOR_P="#3EFC24"

class TextColor(Scene):
    def construct(self):
        text = Tex("A","B","C","D","E","F")
        text[0].set_color(RED)
        text[1].set_color(BLUE)
        text[2].set_color(GREEN)
        text[3].set_color(ORANGE)
        text[4].set_color("#DC28E2") #Hexadecimal color
        text[5].set_color(COLOR_P)
        self.play(Write(text))
        self.wait(2)

class FormulaColor1(Scene): 
    def construct(self):
        # Crear el texto matemático
        text = MathTex("x", "=", "{a", "\\over", "b}")
        # Aplicar colores a cada parte
        text[0].set_color(RED)       # x
        text[1].set_color(BLUE)      # =
        text[2].set_color(GREEN)     # {a
        text[3].set_color(ORANGE)    # \over
        text[4].set_color("#DC28E2") # b
        # Mostrar el texto en pantalla
        self.play(Write(text))
        self.wait(2)

class FormulaColor2(Scene): 
    def construct(self): 
        # Crear el texto matemático
        text = MathTex("x", "=", "\\frac{a}{b}")
        # Aplicar colores a cada parte
        text[0].set_color(RED)   # x
        text[1].set_color(BLUE)  # =
        text[2].set_color(GREEN) # \\frac{a}{b}
        # Animar el texto
        self.play(Write(text))
        self.wait(2)

class FormulaColor3(Scene): 
    def construct(self):
        # Crear el texto matemático
        text = MathTex(
            "\\sqrt{",       # Raíz cuadrada
            "\\int_{",       # Símbolo de integral con límite inferior
            "a}^",           # Límite inferior de la integral
            "{b}",           # Límite superior de la integral
            "\\left(",       # Paréntesis izquierdo
            "\\frac{x}{y}",  # Fracción x/y
            "\\right)",      # Paréntesis derecho
            "dx}"            # Diferencial dx
        )
        
        # Aplicar colores a cada componente
        text[0].set_color(RED)       # Raíz cuadrada
        text[1].set_color(BLUE)      # Símbolo de integral
        text[2].set_color(GREEN)     # Límite inferior
        text[3].set_color(YELLOW)    # Límite superior
        text[4].set_color(PINK)      # Paréntesis izquierdo
        text[5].set_color(ORANGE)    # Fracción
        text[6].set_color(PURPLE)    # Paréntesis derecho
        text[7].set_color(MAROON)    # Diferencial dx
        
        # Animar el texto
        self.play(Write(text))
        self.wait(2)

class FormulaColor3Fixed(Scene): 
    def construct(self): 
        # Crear el texto matemático
        text = MathTex(
            "\\sqrt{",       # Raíz cuadrada
            "\\int_{",       # Integral con límite inferior
            "a}^",           # Límite inferior
            "{b}",           # Límite superior
            "\\left(",       # Paréntesis izquierdo
            "\\frac{x}{y}",  # Fracción x/y
            "\\right)",      # Paréntesis derecho
            "dx."            # Diferencial dx
        )
        
        # Aplicar colores a cada segmento
        text[0].set_color(RED)       # Raíz cuadrada
        text[1].set_color(BLUE)      # Integral
        text[2].set_color(GREEN)     # Límite inferior
        text[3].set_color(YELLOW)    # Límite superior
        text[4].set_color(PINK)      # Paréntesis izquierdo
        text[5].set_color(ORANGE)    # Fracción
        text[6].set_color(PURPLE)    # Paréntesis derecho
        text[7].set_color(MAROON)    # Diferencial dx
        
        # Animar el texto
        self.play(Write(text))
        self.wait(3)

class FormulaColor3Fixed2(Scene): 
    def construct(self): 
        # Crear el texto matemático
        text = MathTex(
            "\\sqrt{",      # Raíz cuadrada
            "\\int_",       # Integral con límite inferior
            "{a}^",         # Límite inferior
            "{b}",          # Límite superior
            "\\left(",      # Paréntesis izquierdo
            "{x",           # Numerador de la fracción
            "\\over",       # División en LaTeX
            "y}",           # Denominador de la fracción
            "\\right)",     # Paréntesis derecho
            "d",            # Diferencial "d"
            "x",            # Variable "x"
            ".}"            # Punto final
        )
        
        # Aplicar colores a cada segmento
        text[0].set_color(RED)       # Raíz cuadrada
        text[1].set_color(BLUE)      # Integral
        text[2].set_color(GREEN)     # Límite inferior
        text[3].set_color(YELLOW)    # Límite superior
        text[4].set_color(PINK)      # Paréntesis izquierdo
        text[5].set_color(ORANGE)    # Numerador
        text[6].set_color(PURPLE)    # Operador de división
        text[7].set_color(MAROON)    # Denominador
        text[8].set_color(TEAL)      # Paréntesis derecho
        text[9].set_color(GOLD)      # Diferencial "d"
        text[10].set_color(GREEN)    # Variable "x"
        text[11].set_color(WHITE)    # Punto final

        # Animar el texto
        self.play(Write(text))
        self.wait(3)

class FormulaColor4(Scene): 
    def construct(self): 
        # Crear el texto matemático
        text = MathTex(
            "\\sqrt{",      # Raíz cuadrada
            "\\int_",       # Integral con límite inferior
            "{a",           # Límite inferior (parte 1)
            "+",            # Límite inferior (parte 2)
            "c}^",          # Límite inferior (parte 3) y límite superior
            "{b}",          # Límite superior
            "\\left(",      # Paréntesis izquierdo
            "{x",           # Numerador de la fracción
            "\\over",       # Operador de división
            "y}",           # Denominador de la fracción
            "\\right)",     # Paréntesis derecho
            "d",            # Diferencial "d"
            "x",            # Variable "x"
            ".}"            # Punto final
        )
        
        # Aplicar colores a cada segmento
        text[0].set_color(RED)       # Raíz cuadrada
        text[1].set_color(BLUE)      # Integral
        text[2].set_color(GREEN)     # Límite inferior (parte 1)
        text[3].set_color(YELLOW)    # Operador suma
        text[4].set_color(PINK)      # Límite inferior (parte 2)
        text[5].set_color(ORANGE)    # Límite superior
        text[6].set_color(PURPLE)    # Paréntesis izquierdo
        text[7].set_color(MAROON)    # Numerador
        text[8].set_color(TEAL)      # Operador división
        text[9].set_color(GOLD)      # Denominador
        text[10].set_color(GRAY)     # Paréntesis derecho
        text[11].set_color(RED)      # Diferencial "d"
        text[12].set_color(BLUE)     # Variable "x"
        text[13].set_color(WHITE)    # Punto final

        # Animar el texto
        self.play(Write(text))
        self.wait(3)

class FormulaColor5(Scene): 
    def construct(self): 
        # Crear el texto matemático
        text = MathTex(
            "\\sqrt{",      # Raíz cuadrada
            "\\int_",       # Integral con límite inferior
            "{a",           # Límite inferior (parte 1)
            "+",            # Operador suma
            "c}^",          # Límite inferior (parte 2) y límite superior
            "{b}",          # Límite superior
            "\\left(",      # Paréntesis izquierdo
            "{x",           # Numerador
            "\\over",       # Operador de división
            "y}",           # Denominador
            "\\right)",     # Paréntesis derecho
            "d",            # Diferencial "d"
            "x",            # Variable "x"
            ".}"            # Punto final
        )
        
        # Colores a asignar
        colors = [PURPLE, BLUE, GREEN, YELLOW, PINK, ORANGE, RED, TEAL, GOLD, MAROON, GRAY, WHITE, RED]

        # Aplicar colores a cada segmento
        for i, color in enumerate(colors):
            text[i].set_color(color)

        # Animar el texto
        self.play(Write(text))
        self.wait(3)

#################################################################################################3

class ColorByCaracter(Scene):
    def construct(self):
        # Crear el texto matemático
        text = MathTex(
            "{d", "\\over", "d", "x", "}", "\\int_", "{a}^", "{", "x", "}", "f(", "t", ")d", "t", "=", "f(", "x", ")"
        )
        # Aplicar color a todas las instancias de "x"
        text.set_color_by_tex("x", RED)
        
        # Animar el texto
        self.play(Write(text))
        self.wait(2)

class ColorByCaracterFixed(Scene): 
    def construct(self):
        # Crear el texto matemático
        text = MathTex(
            "{d", "\\over", "d", "x", "}", "\\int_", "{a}^", "{", "x", "}", "f(", "t", ")d", "t", "=", "f(", "x", ")"
        )
        
        # Aplicar color rojo a todas las instancias de "x"
        text.set_color_by_tex("x", RED)

        # Aplicar color rojo al elemento específico text[6] ("{a}^")
        text[6].set_color(RED)
        
        # Aplicar color blanco al elemento específico text[8] (abre llaves "{" para el límite superior)
        text[8].set_color(WHITE)

        # Animar la escritura del texto
        self.play(Write(text))
        self.wait(2)
	
class ListFor(Scene): 
    def construct(self): 
        # Crear el texto con elementos de la lista
        text = MathTex("[0]", "[1]", "[2]", "[3]", "[4]", "[5]", "[6]", "[7]")
        
        # Colorear los índices especificados en rojo
        indices_to_color = [0, 1, 3, 4]
        for i in indices_to_color:
            text[i].set_color(RED)
        
        # Animar la escritura del texto
        self.play(Write(text))
        self.wait(3)

class ForRange1(Scene): 
    def construct(self): 
        # Crear el texto con elementos de la lista
        text = MathTex("[0]", "[1]", "[2]", "[3]", "[4]", "[5]", "[6]", "[7]")
        
        # Colorear los primeros tres elementos en rojo
        for i in range(3):
            text[i].set_color(RED)
        
        # Animar la escritura del texto
        self.play(Write(text))
        self.wait(3)

class ForRange2(Scene): 
    def construct(self): 
        # Crear el texto con elementos de la lista
        text = MathTex("[0]", "[1]", "[2]", "[3]", "[4]", "[5]", "[6]", "[7]")
        
        # Colorear los elementos del índice 2 al 5 en rojo
        for i in range(2, 6):
            text[i].set_color(RED)
        
        # Animar la escritura del texto
        self.play(Write(text))
        self.wait(3)

class ForTwoVariables(Scene): 
    def construct(self): 
        # Crear el texto con elementos de la lista
        text = MathTex("[0]", "[1]", "[2]", "[3]", "[4]", "[5]", "[6]", "[7]")
        
        # Colorear elementos específicos según su índice y color
        for i, color in [(2, RED), (4, PINK)]:
            text[i].set_color(color)
        
        # Animar la escritura del texto
        self.play(Write(text))
        self.wait(3)

class ChangeSize(Scene):
    def construct(self):
        # Crear el texto con la fórmula
        text = MathTex("\\sum_{i=0}^n i=\\frac{n(n+1)}{2}")
        
        # Agregar el texto a la escena
        self.add(text)
        self.wait()
        
        # Escalar el texto al doble de su tamaño original
        text.scale(2)
        self.wait(2)

class AddAndRemoveText(Scene):
    def construct(self):
        # Crear el texto
        text = Tex("Text or object")
        
        # Pausa inicial
        self.wait()

        # Agregar el texto a la escena
        self.add(text)
        self.wait()

        # Eliminar el texto de la escena
        self.remove(text)
        self.wait()

class FadeText(Scene):
    def construct(self):
        # Crear el texto
        text = Tex("Text or object")
        
        # Animación de entrada (FadeIn)
        self.play(FadeIn(text))
        self.wait()
        
        # Animación de salida (FadeOut) con duración personalizada
        self.play(FadeOut(text), run_time=1)
        self.wait()

class FadeTextFromDirection(Scene):
    def construct(self):
        # Crear el texto
        text = Tex("Text or object")
        
        # Mover el texto hacia abajo y luego hacer FadeIn
        text.shift(DOWN)  # Mueve el texto hacia abajo
        self.play(FadeIn(text), run_time=1)
        self.wait()

class GrowObjectFromCenter(Scene):
    def construct(self):
        # Crear el texto
        text = Tex("Text or object")
        
        # Animación de crecimiento desde el centro
        self.play(GrowFromCenter(text), run_time=1)
        self.wait()

class ShowCreationObject(Scene):
    def construct(self):
        # Crear el texto a mostrar
        text = Tex("Text or object")
        
        # Animación de creación, mostrando el texto como si fuera "dibujado"
        self.play(Create(text), run_time=1)
        
        # Esperar después de la animación para que el texto permanezca visible
        self.wait()

class ColoringText(Scene):
    def construct(self):
        # Crear el texto a mostrar
        text = Tex("Text or object")
        self.add(text)
        
        # Esperar medio segundo antes de empezar
        self.wait(0.5)
        
        # Animar cada letra para que se coloree de amarillo
        self.play(
            LaggedStart(
                *[ApplyMethod(letter.set_color, YELLOW) for letter in text],
                lag_ratio=0.12  # El tiempo de retraso entre cada animación
            )
        )
        
        # Esperar medio segundo al final
        self.wait(0.5)

class CrossText1(Scene):
    def construct(self):
        # Corregir los delimitadores matemáticos
        text = Tex(r"$\sum_{i=1}^{\infty}i$", r"$=$", r"$-\frac{1}{2}$")
        cross = Cross(text[2])  # Marcar el último elemento
        cross.set_stroke(RED, 6)
        
        self.play(Write(text))  # Escribir el texto
        self.wait(0.5)
        self.play(FadeIn(cross))  # Mostrar el tachado
        self.wait(2)

class CrossText2(Scene):
    def construct(self):
        # Corregir los delimitadores matemáticos
        text = Tex(r"$\sum_{i=1}^{\infty}i$", r"$=$", r"$-\frac{1}{2}$")
        
        # Agrupar los elementos "=" y "-1/2"
        eq = VGroup(text[1], text[2])
        
        # Crear un tachado sobre el grupo
        cross = Cross(eq)
        cross.set_stroke(RED, 6)
        
        # Animaciones
        self.play(Write(text))
        self.wait(0.5)
        self.play(FadeIn(cross))
        self.wait(2)

class FrameBox1(Scene):
    def construct(self):
        text = MathTex(
            "\\hat{g}(", "f", ")", "=", "\\int", "{t_1}", "^{t{2}}",
            "g(", "t", ")", "e", "^{-2\\pi i", "f", "t}", "dt"
        )
        frameBox = SurroundingRectangle(text[4], buff=0.5 * SMALL_BUFF)
        self.play(Write(text))
        self.wait(0.5)
        self.play(Create(frameBox))  # ShowCreation es Create en versiones recientes
        self.wait(2)

class FrameBox2(Scene):
    def construct(self):
        text = MathTex(
            "\\hat{g}(", "f", ")", "=", "\\int", "{t_1}", "^{t{2}}",
            "g(", "t", ")", "e", "^{-2\\pi i", "f", "t}", "dt"
        )
        seleccion = VGroup(text[4], text[5], text[6])  # Agrupamos los términos seleccionados
        frameBox = SurroundingRectangle(seleccion, buff=0.5 * SMALL_BUFF)
        frameBox.set_stroke(GREEN, 9)  # Cambiamos el color y grosor del borde
        self.play(Write(text))
        self.wait(0.5)
        self.play(Create(frameBox))  # ShowCreation fue renombrado a Create
        self.wait(2)

class BraceText(Scene):
    def construct(self):
        text = Tex(
            r"$\frac{d}{dx}f(x)g(x)=$", r"$f(x)\frac{d}{dx}g(x)$", r"$+$",
            r"$g(x)\frac{d}{dx}f(x)$"
        )
        self.play(Write(text))
        brace_top = Brace(text[1], UP, buff=SMALL_BUFF)
        brace_bottom = Brace(text[3], DOWN, buff=SMALL_BUFF)
        text_top = brace_top.get_text(r"$g'f$")
        text_bottom = brace_bottom.get_text(r"$f'g$")
        self.play(
            GrowFromCenter(brace_top),
            GrowFromCenter(brace_bottom),
            FadeIn(text_top),
            FadeIn(text_bottom)
        )
        self.wait()