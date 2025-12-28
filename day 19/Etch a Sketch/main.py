import turtle

tim = turtle.Turtle()
screen = turtle.Screen()

def move_forwards():
    tim.forward(10)
def reverse():
    tim.backward(10)
def turn_left():
    tim.left(10)
def turn_right():
    tim.right(10)
def screen_clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()

screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=reverse)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=screen_clear)


screen.exitonclick()