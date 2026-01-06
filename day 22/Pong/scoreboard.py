from turtle import Turtle

FONT = ("Courier", 70, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.update_score()


    def update_score(self):
        self.clear()
        self.teleport(0,190)
        self.write(f"{self.l_score}     {self.r_score}", align="center", font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_score()
    def r_point(self):
        self.r_score += 1
        self.update_score()
