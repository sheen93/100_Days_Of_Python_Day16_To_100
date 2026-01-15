from turtle import Turtle

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Street(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.teleport(-500,250)

    def draw_street(self):
        self.color("white")
        self.pensize(5)
        self.setheading(RIGHT)
        self.fd(1000)
        self.setheading(DOWN)
        self.fd(500)
        self.setheading(LEFT)
        self.fd(1000)
        self.setheading(UP)
        self.fd(500)
