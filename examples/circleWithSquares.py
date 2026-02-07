import turtle
import colorsys

# --- CONFIGURACIÓN ---
screen = turtle.Screen()
screen.setup(900, 900)
screen.bgcolor("black")
turtle.colormode(1.0)

t = turtle.Turtle()
t.speed(-20)
t.hideturtle()
t.pensize(2)

# --- PARÁMETROS ---
NUM_CUADRADOS = 120 
LADO_BASE = 180
GIRO_ENTRE_CUADRADOS = 3

def color_arcoiris(i, total):
    h = i / total
    r, g, b = colorsys.hsv_to_rgb(h, 1.0, 1.0)
    return (r, g, b)

def dibujar_cuadrado(lado):
    for _ in range(4):
        t.forward(lado)
        t.right(90)

def arte_geometrico():
    t.penup()
    t.goto(0, 0)
    t.setheading(0)
    t.pendown()

    for i in range(NUM_CUADRADOS):
        t.pencolor(color_arcoiris(i, NUM_CUADRADOS))
        dibujar_cuadrado(LADO_BASE)
        t.right(GIRO_ENTRE_CUADRADOS)
        # Pequeña traslación hacia el centro
        t.penup()
        t.forward(3)
        t.pendown()

arte_geometrico()
turtle.done()
