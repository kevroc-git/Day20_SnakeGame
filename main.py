
from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

# screen.colormode(255)


slinky = Snake.create_slinky()
print("slinky created", slinky)

game_is_on = True

while game_is_on:
    print(slinky)
    Snake.move_slinky(slinky)
    screen.update()



































screen.exitonclick()

