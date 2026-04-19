import time
from game_mechanics import GameMech

game = GameMech()

while game.game_on:
    game.update_game()













# import turtle
# from snake import Snake
# import time
# from food import Food
# import scoreboard
#
# screen = turtle.Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor("black")
# screen.title("Snake Game Highscore")
# screen.tracer(0)
#
# food = Food()
# snake = Snake()
# screen.listen()
#
# screen.onkey(snake.up, "Up")
# screen.onkey(snake.down, "Down")
# screen.onkey(snake.left, "Left")
# screen.onkey(snake.right, "Right")
#
# score_turtle = scoreboard.Scoreboard()
# game_on = True
#
# while game_on:
#     screen.update()
#     time.sleep(snake.snake_speed)
#
#     snake.move()
#
#     #detect collision with food
#     if snake.head.distance(food) < 15:
#         food.refresh()
#         score_turtle.increase_score()
#         snake.extend()
#
#     #detect collision with wall
#     if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
#         reset = screen.textinput(title="Snake died!", prompt="Do you want to:\n"
#                                                              "'R' - Restart Game\n"
#                                                              "'E' - Exit Game").lower()
#         if reset == "r":
#             snake.reset()
#             score_turtle.reset()
#             continue
#         else:
#             game_on = False
#             score_turtle.game_over()
#             break
#
#     #detect collision with tail
#     for segment in snake.segments[1:]:
#         if snake.head.distance(segment) < 10:
#             reset = screen.textinput(title="Snake died!", prompt="Do you want to:\n"
#                                                                  "'R' - Restart Game\n"
#                                                                  "'E' - Exit Game").lower()
#             if reset == "r":
#                 snake.reset()
#                 score_turtle.reset()
#                 continue
#             else:
#                 game_on = False
#                 score_turtle.game_over()
#                 break
#
#
# screen.exitonclick()