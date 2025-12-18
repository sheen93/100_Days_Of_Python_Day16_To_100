from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.shape("turtle")
tim.speed("fastest")
tim.pensize(10)
turn_angle = [0,90,180,270]
distance = [10,20,30,40,50]

def random_color():
    color1 = random.randint(0, 255)
    color2 = random.randint(0, 255)
    color3 = random.randint(0, 255)
    tim.color(color1,color2,color3)

def check_border(t):
    # Check if the turtle has hit the borders (e.g., at 300 or -300)
    if t.xcor() > 290 or t.xcor() < -290 or t.ycor() > 290 or t.ycor() < -290:
        t.undo() # Undo the move that crossed the border

def random_walk():
    random_color()
    random_turns = random.randint(0,4)
    for i in range(random_turns):
        tim.setheading(random.choice(turn_angle))
    tim.forward(random.choice(distance))
    check_border(tim)
    tim.setheading(random.choice(turn_angle))


for i in range(200):
    random_walk()








screen.exitonclick()