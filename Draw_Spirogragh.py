import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("arrow")
myScreen = Screen()
turtle.colormode(255)
timmy.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(space_between):
    for _ in range(360 // space_between):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + space_between)


draw_spirograph(5)

myScreen.exitonclick()
