
# build snake class
from turtle import Turtle
STARTING_POSITIONS = [(-10, 0), (-20, 0), (-40, 0)]

class Snake:

    def __init__(self):
        self.slinky = []
        self.create_slinky()

    def create_slinky(self):
        for position in STARTING_POSITIONS:
            if position == (-10,0):
                segment = Turtle(shape="arrow")
            else:
                segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()
            segment.setposition(position)
            self.slinky.append(segment)
            snake_head = slinky[0]
        return slinky


    def move_slinky(slinky):
        print("in move slinky", slinky)
        import time
        from turtle import Screen
        Screen().tracer(0)
        print("length of slinky", len(slinky))
        for each_piece_of_slinky in range(len(slinky) - 1, 0, -1):

            print("in for loop", each_piece_of_slinky)
            # get position of next to last segment
            new_x = slinky[each_piece_of_slinky - 1].xcor()
            new_y = slinky[each_piece_of_slinky - 1].ycor()
            # move last segment to next to last
            slinky[each_piece_of_slinky].goto(new_x, new_y)
            print("moved piece", each_piece_of_slinky)
            time.sleep(1)


        slinky[0].forward(20)
        slinky[0].left(90)
        return slinky
