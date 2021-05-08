
# build snake class
from turtle import Turtle, Screen
import time
screen = Screen()



STARTING_POSITIONS = [(00, 0), (-10, 0), (-30, 0)]

class Snake:
    def __init__(self):
        self.slinky = []
        self.create_slinky()
        print("slinky created", self.slinky)
        screen.update()

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
        print("in move slinky", self.slinky)
        print("length of slinky", len(self.slinky))
        time.sleep(2)

        for each_piece_of_slinky in range(len(self.slinky) - 1, 0, -1):
            print("in for loop", each_piece_of_slinky)
            # get position of next to last segment
            new_x = self.slinky[each_piece_of_slinky - 1].xcor()
            new_y = self.slinky[each_piece_of_slinky - 1].ycor()
            # move last segment to next to last
            self.slinky[each_piece_of_slinky].goto(new_x, new_y)
            print("moved piece", each_piece_of_slinky)
            time.sleep(2)

        self.slinky[0].forward(10)
        # self.slinky[0].left(90)
        return self.slinky
