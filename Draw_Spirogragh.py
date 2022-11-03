import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("arrow")   #set turtle pointer
myScreen = Screen()    
turtle.colormode(255)   #changing color mode to rgb
timmy.speed("fastest")  # setting turtle speed as fastest


def random_color():         #function for making a random color by mixing RGB colors
    r = random.randint(0, 255)       # red color
    g = random.randint(0, 255)       # green color
    b = random.randint(0, 255)       # blue color
    color = (r, g, b)                # Mixing RGB colours as tuple
    return color


def draw_spirograph(space_between):           # passing the space between circles as integer argument
    for _ in range(360 // space_between):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + space_between)    # rotating angle of pointer


draw_spirograph(5)          # Space between circle given as sample input 

myScreen.exitonclick()     # Screen method to hold the output screen 
