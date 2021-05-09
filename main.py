
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

slinky = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(slinky.up, "Up")
screen.onkey(slinky.down, "Down")
screen.onkey(slinky.left, "Left")
screen.onkey(slinky.right, "Right")


game_is_on = True

while game_is_on:
    slinky.move_slinky()

    # detect collision with food
    if slinky.snake_head.distance(food) < 15:
        food.refresh()
        slinky.add_segment(slinky)
        scoreboard.increase_score()


































screen.exitonclick()

