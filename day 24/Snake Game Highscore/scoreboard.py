from turtle import Turtle

ALIGN ="center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt", mode = "r") as file:
            self.highscore = int(file.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.update_scoreboard()

    def update_highscore(self):
        if self.highscore < self.score:
            self.highscore = self.score
            with open("data.txt", mode = "w") as file:
                file.write(str(self.score))


    def update_scoreboard(self):
        self.clear()
        self.write(f"Highscore: {self.highscore}      Player Score: {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write("Game Over!", align=ALIGN, font=FONT)

    def reset(self):
        self.score = 0
        self.clear()
        self.goto(0,260)
        self.color("white")
        self.update_scoreboard()


    def increase_score(self):
        self.score+=1
        self.update_highscore()
        self.update_scoreboard()

