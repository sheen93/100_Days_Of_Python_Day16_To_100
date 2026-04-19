from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from snake import Snake
import time

class GameMech:
    def __init__(self):
        #screen setup
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Snake Game")
        self.screen.tracer(0)

        self.snake = Snake()
        self.food = Food()
        self.score = Scoreboard()
        self.game_on = True

        self.setup_controls()

    def setup_controls(self):
        self.screen.onkey(self.snake.up, "Up")
        self.screen.onkey(self.snake.down, "Down")
        self.screen.onkey(self.snake.left, "Left")
        self.screen.onkey(self.snake.right, "Right")

    def update_game(self):
        self.screen.listen()
        self.screen.update()
        time.sleep(self.snake.snake_speed)
        self.snake.move()

        if self.snake.head.distance(self.food) < 15:
            self.food.refresh()
            self.score.increase_score()
            self.snake.extend()

        if abs(self.snake.head.xcor()) > 290 or abs(self.snake.head.ycor())>290:
            self.trigger_restart_menu()

        for segment in self.snake.segments[1:]:
            if self.snake.head.distance(segment) < 10:
                self.trigger_restart_menu()

    def trigger_restart_menu(self):
        self.score.game_over()
        self.screen.update()
        choice = self.screen.textinput(title="Snake died!", prompt="Do you want to:\n"
                                                             "'R' - Restart Game\n"
                                                             "'E' - Exit Game").lower()

        if choice == "r":
            self.snake.reset()
            self.score.reset()
            self.screen.listen()
        else:
            self.game_on = False
            time.sleep(3)
            self.screen.bye()

