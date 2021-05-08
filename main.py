
from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

SPEED = 0.0
slinky = Snake()


screen.listen()
screen.onkey(slinky.up, "Up")
screen.onkey(slinky.down, "Down")
screen.onkey(slinky.left, "Left")
screen.onkey(slinky.right, "Right")


game_is_on = True
while game_is_on:
    time.sleep(SPEED)
    slinky.move_slinky()




































screen.exitonclick()

