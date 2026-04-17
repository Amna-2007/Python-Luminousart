import turtle
import colorsys

def draw_luminous_art():
    screen = turtle.Screen()
    screen.bgcolor("black")

    t = turtle.Turtle()
    t.speed(0)
    turtle.tracer(3)   # 👈 speed boost
    t.hideturtle()
    t.pensize(4)

    hue = 0.6

    for i in range(400):
        color = colorsys.hsv_to_rgb(hue, 0.9, 1)
        t.pencolor(color)
        hue += 0.005

        t.penup()
        t.goto(0, 0)
        t.setheading(i * 10)
        t.pendown()
        t.forward(i * 0.8)
        t.right(20)

    turtle.done()

draw_luminous_art()