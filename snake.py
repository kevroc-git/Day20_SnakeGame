
# build snake class

class Snake:

    def __init__(self):
        slinky = []

    def create_slinky(self):
        slinky = []
        starting_positions = [(-10,0),(-20,0),(-40,0)]
        from turtle import Turtle

        for position in starting_positions:
            if position == (-10,0):
                segment = Turtle(shape="arrow")
            else:
                segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()
            segment.setposition(position)
            slinky.append(segment)
            snake_head = slinky[0]
        return slinky


    def move_slinky(slinky):
        print("in move slinky", slinky)
        import time
        print("length of slinky", len(slinky))
        for each_piece_of_slinky in range(len(slinky) - 1, 0, -1):

            print("in for loop", each_piece_of_slinky)
            # get position of next to last segment
            new_x = slinky[each_piece_of_slinky - 1].xcor()
            new_y = slinky[each_piece_of_slinky - 1].ycor()
            # move last segment to next to last
            slinky[each_piece_of_slinky].goto(new_x, new_y)
            print("moved piece", each_piece_of_slinky)
            time.sleep(5)
            # screen.update()

        slinky[0].forward(20)
        slinky[0].left(90)
        return slinky
