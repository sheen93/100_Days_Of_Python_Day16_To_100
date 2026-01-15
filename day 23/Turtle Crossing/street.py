from turtle import Turtle

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Street(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.teleport(-650,250)

    def draw_street(self):
        self.color("white")
        self.pensize(5)
        self.setheading(RIGHT)
        self.fd(1300)
        self.setheading(DOWN)
        self.fd(500)
        self.setheading(LEFT)
        self.fd(1300)
        self.setheading(UP)
        self.fd(500)
        self.teleport(-650, 280)
        self.setheading(RIGHT)
        self.fd(1300)
        self.teleport(-650, -280)
        self.fd(1300)
        #middle yellow
        self.teleport(self.xcor(),0)
        self.pencolor("yellow")
        self.pensize(10)
        self.setheading(LEFT)
        self.fd(1300)

