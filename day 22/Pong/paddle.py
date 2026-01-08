from turtle import Turtle

UP = 90
DOWN = 270
PADDLE_LIMIT = 240



class Paddle(Turtle):

    right_x = 350
    left_x = -350
    all_y = 0
    all_paddles = []
    def __init__(self, x,y):
        super().__init__()
        self.initial_x = x
        self.initial_y = y
        self.x = x
        self.y = y
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.teleport(self.initial_x, self.initial_y)
        Paddle.all_paddles.append(self)
        self.paddle_speed = 10
        self.moving_up = False
        self.moving_down = False


    def up(self):
        if self.ycor() < PADDLE_LIMIT:
            new_y = self.ycor() + self.paddle_speed
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() > -PADDLE_LIMIT:
            new_y = self.ycor() - self.paddle_speed
            self.goto(self.xcor(), new_y)

    def start_up(self):
        self.moving_up = True
    def stop_up(self):
        self.moving_up = False
    def start_down(self):
        self.moving_down = True
    def stop_down(self):
        self.moving_down = False

    def update_paddle(self):
        if self.moving_up:
            self.up()
        if self.moving_down:
            self.down()

    def reset_pos(self):
        self.x = self.initial_x
        self.y = self.initial_y
        self.goto(self.initial_x, self.initial_y)

    @classmethod
    def reset_all(cls):
        for paddle in cls.all_paddles:
            paddle.reset_pos()
    @classmethod
    def update_all_paddles(cls):
        for paddle in cls.all_paddles:
            paddle.update_paddle()


