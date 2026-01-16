from turtle import Turtle
import random

COLORS = ["red", "green", "blue", "yellow", "cyan", "magenta", "black", "white"]

class Vehicle(Turtle):
    def __init__(self, lane_pos, direction, length, width = 1):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.penup()
        self.shapesize(stretch_wid=width, stretch_len=length)
        self.goto(630 if direction == 180 else -630,lane_pos)
        self.setheading(direction)
        self.half_len = int(length*20)/2
        self.half_wid = int(width*20)/2

    def collision_detected(self, t_object):
        v_left = self.xcor()-self.half_len
        v_right = self.xcor()+self.half_len
        v_top = self.ycor()+self.half_wid
        v_bottom = self.ycor()-self.half_wid

        t_radius = 10
        t_left = t_object.xcor()-t_radius
        t_right = t_object.xcor()+t_radius
        t_top = t_object.ycor()+t_radius
        t_bottom = t_object.ycor()-t_radius

        if t_right > v_left and t_left < v_right:
            if t_top > v_bottom and t_bottom < v_top:
                return True
        return False


class Sedan(Vehicle):
    def __init__(self, lane_pos, direction):
        super().__init__(lane_pos, direction, length=2, width=1)

class Bus(Vehicle):
    def __init__(self, lane_pos, direction):
        super().__init__(lane_pos, direction, length= 4, width = 2)

class BigTruck(Vehicle):
    def __init__(self, lane_pos, direction):
        super().__init__(lane_pos, direction, length= 5, width = 2)

class SUV(Vehicle):
    def __init__(self, lane_pos, direction, ):
        super().__init__(lane_pos, direction, length= 3, width = 1)

class MotorCycle(Vehicle):
    def __init__(self, lane_pos, direction):
        super().__init__(lane_pos, direction, length= 1, width = 1)