import turtle
import colorsys

# --- CONFIGURACIÓN ---
screen = turtle.Screen()
screen.setup(900, 900)
screen.bgcolor("black")
turtle.colormode(1.0)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.pensize(2) # Grosor del trazo
# t.circle(100) # Pinta un circulo de 100 de tamaño

# Hace un giro hacia la derecha de 10 grados y pinta otro circulo de 100 de tamaño, repitiendo esto 36 veces para completar un giro completo (360 grados).
for i in range(36):
    h = i / 36.0
    color = colorsys.hsv_to_rgb(h, 0.9, 1)
    t.pencolor(color)
    t.right(10)
    t.circle(100)

    
for i in range(36*2):
    h = i / (36.0 * 2)
    color = colorsys.hsv_to_rgb(h, 0.9, 1)
    t.pencolor(color)
    t.left(5)
    t.circle(100)


turtle.done()
