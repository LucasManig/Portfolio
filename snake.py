from turtle import Turtle

START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
DISTANZ = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segmente = []
        self.create_snake()
        self.head = self.segmente[0]

    def create_snake(self):
        for position in START_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        neues_segment = Turtle("square")
        neues_segment.color("white")
        neues_segment.penup()
        neues_segment.goto(position)
        self.segmente.append(neues_segment)

    def erweitern(self):
        self.add_segment(self.segmente[-1].position())

    def bewegen(self):
        for seg_num in range(len(self.segmente) - 1, 0, -1):
            neu_x = self.segmente[seg_num - 1].xcor()
            neu_y = self.segmente[seg_num - 1].ycor()
            self.segmente[seg_num].goto(neu_x, neu_y)
        self.segmente[0].forward(DISTANZ)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)