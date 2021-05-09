
# build snake class
from turtle import Turtle, Screen
import time

screen = Screen()



STARTING_POSITIONS = [(00, 0), (-10, 0), (-30, 0)]
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
TIME_DELAY = 0.0

class Snake:
    def __init__(self):
        self.slinky = []
        self.create_slinky()
        # print("slinky created", self.slinky)
        self.snake_head = self.slinky[0]

    def create_slinky(self):
        for position in STARTING_POSITIONS:
            if position == (0,0):
                segment = Turtle(shape="arrow")
            else:
                segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()
            segment.setposition(position)
            self.slinky.append(segment)
        return self.slinky

    def move_slinky(self):
        # print("in move slinky", self.slinky)
        # print("length of slinky", len(self.slinky))

        for each_piece_of_slinky in range(len(self.slinky) - 1, 0, -1):
            # print("in for loop", each_piece_of_slinky)
            # get position of next to last segment
            new_x = self.slinky[each_piece_of_slinky - 1].xcor()
            new_y = self.slinky[each_piece_of_slinky - 1].ycor()
            # move last segment to next to last
            self.slinky[each_piece_of_slinky].goto(new_x, new_y)
            # print("moved piece", each_piece_of_slinky)

        self.slinky[0].forward(MOVE_DISTANCE)
        return self.slinky

    def up(self):
        # print(self.snake_head.heading())
        if self.snake_head.heading() != DOWN:
            self.snake_head.seth(UP)

    def down(self):
        # print(self.snake_head.heading())
        if self.snake_head.heading() != UP:
            self.snake_head.seth(DOWN)

    def left(self):
        # print(self.snake_head.heading())
        if self.snake_head.heading() != RIGHT:
           self.snake_head.seth(LEFT)

    def right(self):
        # print(self.snake_head.heading())
        if self.snake_head.heading() != LEFT:
            self.snake_head.seth(RIGHT)

    def add_segment(self, slinky):
        # Add Segment
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        self.slinky.append(segment)
        time.sleep(TIME_DELAY)
        for each_piece_of_slinky in range(len(self.slinky) - 1, 0, -1):
            # print("in for loop", each_piece_of_slinky)
            # get position of next to last segment
            time.sleep(TIME_DELAY)
            new_x = self.slinky[each_piece_of_slinky - 1].xcor()
            new_y = self.slinky[each_piece_of_slinky - 1].ycor()
            # move last segment to next to last
            time.sleep(TIME_DELAY)
            self.slinky[each_piece_of_slinky].goto(new_x, new_y)
            # print("moved piece", each_piece_of_slinky)
        time.sleep(TIME_DELAY)
        self.slinky[0].forward(MOVE_DISTANCE)
        # print("moving forward")
        time.sleep(TIME_DELAY)
        return self.slinky

    