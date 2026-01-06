from turtle import Turtle

class Court(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed('fastest')
        self.color('white')
        self.draw_court()

    def draw_court(self):
        self.teleport(0,290)
        self.setheading(0)
        self.fd(390)
        self.setheading(270)
        self.pencolor("red")
        self.fd(580)
        self.setheading(180)
        self.pencolor("white")
        self.fd(780)
        self.setheading(90)
        self.pencolor("red")
        self.fd(580)
        self.setheading(0)
        self.pencolor("white")
        self.fd(390)
        self.setheading(270)
        while self.ycor() != -290:
            self.fd(5)
            self.pu()
            self.fd(5)
            self.pd()