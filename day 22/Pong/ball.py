from turtle import Turtle

BALL_MOVE = 10

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.width(20)
        self.penup()
        self.goto(0,0)
        self.ball_move = 10
        self.move()

    def move(self):
        new_x = self.xcor() + BALL_MOVE
        new_y = self.ycor() + BALL_MOVE
        self.goto(new_x,new_y)

    def bounce(self):
        if self.ycor() > 290 or self.ycor() < -290:
            self.ball_move *= -1


    def game_over(self):
        pass
