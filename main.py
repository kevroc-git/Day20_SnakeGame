from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.colormode(255)

slinky = []

def create_slinky():
    starting_positions = [(0,0),(-20,0),(-40,0)]
    for position in starting_positions:
        segment = Turtle(shape="square")
        segment.color("white")
        segment.setposition(position)

create_slinky()

