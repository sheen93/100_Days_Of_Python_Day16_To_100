from turtle import Turtle, Screen
import time
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

left_paddle = Paddle(350)
right_paddle = Paddle(-350)
ball = Ball()

screen.onkey(left_paddle.up, "Up")
screen.onkey(left_paddle.down, "Down")
screen.onkey(right_paddle.up, "w")
screen.onkey(right_paddle.down, "s")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
































screen.exitonclick()