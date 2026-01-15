from turtle import Turtle
import random

COLORS = ["red", "green", "blue", "yellow", "cyan", "magenta", "black", "white"]

class Vehicle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)