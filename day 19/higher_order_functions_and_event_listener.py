from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

"""a higher order function is when one function can call another function"""

screen.listen()
screen.onkey(key="space", fun=move_forwards) # onkey is higher order function calling move_forward function
screen.exitonclick()