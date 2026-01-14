from turtle import Turtle

UP = 90
DOWN = 270
SPEED = 10


class CrossingTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.goto(0, -270)
        self.speed(SPEED)
        self.setheading(UP)
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + self.speed())
    def move_down(self):
        self.goto(self.xcor(), self.ycor() - self.speed())
    def move_right(self):
        self.goto(self.xcor() + self.speed(), self.ycor())
    def move_left(self):
        self.goto(self.xcor() - self.speed(), self.ycor())

    def start_up(self):
        self.moving_up = True
    def stop_up(self):
        self.moving_up = False

    def start_down(self):
        self.moving_down = True
    def stop_down(self):
        self.moving_down = False

    def start_left(self):
        self.moving_left = True
    def stop_left(self):
        self.moving_left = False

    def start_right(self):
        self.moving_right = True
    def stop_right(self):
        self.moving_right = False

    def update(self):
        if self.moving_up:
            self.move_up()
        if self.moving_down:
            self.move_down()
        if self.moving_left:
            self.move_left()
        if self.moving_right:
            self.move_right()


