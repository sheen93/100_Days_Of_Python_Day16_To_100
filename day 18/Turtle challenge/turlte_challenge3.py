from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)

tim = Turtle()
tim.shape("turtle")

sides = 3

while sides != 11:
    color1 = random.randint(0, 255)
    color2 = random.randint(0, 255)
    color3 = random.randint(0, 255)
    tim.pencolor(color1,color2,color3)
    for i in range(sides):
        tim.forward(100)
        tim.right(360/sides)
    sides += 1


screen.exitonclick()