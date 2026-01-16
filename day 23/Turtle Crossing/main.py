from turtle import Turtle, Screen
import time
from car_manager import CarManager
from crossing_turtle import CrossingTurtle
from scoreboard import Scoreboard
from street import Street


screen = Screen()
screen.setup(width=1200, height=650)
screen.bgcolor("grey")
screen.title("Turtle Crossing")
screen.tracer(0)
screen.listen()

cTurtle = CrossingTurtle()
street = Street()
car = CarManager()
scoreboard = Scoreboard()
street.draw_street()

screen.onkeypress(cTurtle.start_up, "Up")
screen.onkeyrelease(cTurtle.stop_up, "Up")

screen.onkeypress(cTurtle.start_down, "Down")
screen.onkeyrelease(cTurtle.stop_down, "Down")

screen.onkeypress(cTurtle.start_right, "Right")
screen.onkeyrelease(cTurtle.stop_right, "Right")

screen.onkeypress(cTurtle.start_left, "Left")
screen.onkeyrelease(cTurtle.stop_left, "Left")



game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.08)

    cTurtle.update()
    cTurtle.border_check()

    car.create_cars()
    car.move_cars()

    if cTurtle.change_direction():
        scoreboard.increase_score()
        car.speed_up()
        cTurtle.speed_up()


    scoreboard.show_score()



    for cars in car.all_cars:
        if cars.collision_detected(cTurtle):
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()