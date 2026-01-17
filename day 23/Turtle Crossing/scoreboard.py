from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.teleport(500, 280)
        self.show_score()

    def increase_score(self):
        self.score += 1

    def show_score(self):
        self.clear()
        self.write(f"Point: {self.score}", align="center", font=("Courier", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("Game Over", align="center", font=("Courier", 50, "bold"))