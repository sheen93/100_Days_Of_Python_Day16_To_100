from turtle import Turtle, Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from court import Court

screen = Screen()
screen.setup(width=850, height=650)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

right_paddle = Paddle(Paddle.right_x, Paddle.all_y)
left_paddle = Paddle(Paddle.left_x, Paddle.all_y)
ball = Ball()
scoreboard = Scoreboard()
court = Court()


screen.onkeypress(right_paddle.start_up, "Up")
screen.onkeyrelease(right_paddle.stop_up, "Up")
screen.onkeypress(right_paddle.start_down, "Down")
screen.onkeyrelease(right_paddle.stop_down, "Down")

screen.onkeypress(left_paddle.start_up, "w")
screen.onkeyrelease(left_paddle.stop_up, "w")
screen.onkeypress(left_paddle.start_down, "s")
screen.onkeyrelease(left_paddle.stop_down, "s")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)

    right_paddle.update_paddle()
    left_paddle.update_paddle()

    ball.move()

    #wall collision
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()

    #right paddle collision
    if ball.distance(right_paddle) < 60 and ball.xcor() > 320:
        if ball.x_move > 0:
            ball.bounce_x()
    #left paddle collision
    if ball.distance(left_paddle) < 60 and ball.xcor() < -320:
        if ball.x_move < 0:
            ball.bounce_x()

    #reset
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_pos()
        Paddle.reset_all()
        # right_paddle.reset_pos(350)
        # left_paddle.reset_pos(-350)
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_pos()
        Paddle.reset_all()
































screen.exitonclick()