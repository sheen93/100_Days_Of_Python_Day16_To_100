from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)

tim = Turtle()
tim.shape("turtle")
tim.color("red")

tom = Turtle()
tom.shape("turtle")
tom.color("blue")
tom.teleport(-200,200)

"""tim's way to make different shapes"""
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

"""tom's way to make different shapes"""
def draw_shapes(num_of_sides):
    angle = 360/num_of_sides
    for _ in range(num_of_sides):
        tom.forward(100)
        tom.right(angle)
for shape_side_n in range(3,11):
    draw_shapes(shape_side_n)




screen.exitonclick()