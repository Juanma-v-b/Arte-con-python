import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)
t.hideturtle()

layers = 24
petals = 12
h = 0.0

for i in range(layers):
    color = colorsys.hsv_to_rgb(h, 0.9, 1)
    t.pencolor(color)

    for _ in range(petals):
        t.pensize(2)
        t.circle(80 + i * 10, 60)
        t.left(120)
        t.circle(80 + i * 10, 60)
        t.left(120)


        t.pensize(1)
        t.forward(100 + i * 10)
        t.backward(100 + i * 10)
        t.right(360 / petals)

    h += 0.8 / layers
    t.right(360 / layers)

h = 0
for i in range(36):
    color = colorsys.hsv_to_rgb(h, 0.9, 1)
    t.pencolor(color)
    t.circle(40, 90)
    t.left(90)
    t.circle(40, 90)
    t.left(10)

    h += 0.03 

turtle.done()
