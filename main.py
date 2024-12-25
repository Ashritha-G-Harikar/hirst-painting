import turtle as t
import random
distance = 10
tim = t.Turtle()
tim.ht()
screen = t.Screen()
screen.colormode(255)
tim.penup()
tim.goto(-300, 300)


def color_dots():
    y = 300
    i = 0
    for color in range(100):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        tim.color(r, g, b)
        if i % 10 == 0:
            tim.penup()
            tim.goto(-150, y)
        tim.dot(15)
        tim.penup()
        tim.forward(40)
        i += 1
        y -= 5


color_dots()


screen.exitonclick()
