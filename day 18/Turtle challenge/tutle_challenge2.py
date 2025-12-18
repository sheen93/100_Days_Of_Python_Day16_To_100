import turtle
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("red")

tim.pu()
tim.setposition(-400,0)

for i in range(50):
    tim.pd()
    tim.forward(10)
    tim.pu()
    tim.forward(10)









screen = Screen()
screen.screensize(2000,2000)
screen.exitonclick()