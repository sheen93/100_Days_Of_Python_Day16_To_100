from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.snake_speed = 0.1
        self.direction_locked = False

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def reset(self):
        for seg in self.segments:
            seg.hideturtle()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.snake_speed = 0.1

    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())
        self.snake_speed *= 0.95


    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.fd(MOVE_DISTANCE)
        self.direction_locked = False

    def up(self):
        if self.head.heading() != DOWN and not self.direction_locked:
            self.head.setheading(90)
            self.direction_locked = True
    def down(self):
        if self.head.heading() != UP and not self.direction_locked:
            self.head.setheading(270)
            self.direction_locked = True
    def left(self):
        if self.head.heading() != RIGHT and not self.direction_locked:
            self.head.setheading(180)
            self.direction_locked = True
    def right(self):
        if self.head.heading() != LEFT and not self.direction_locked:
            self.head.setheading(0)
            self.direction_locked = True