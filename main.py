from turtle import Screen
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

    # Detect collision with wall
    if slinky.snake_head.xcor() > 280 \
            or slinky.snake_head.xcor() < -280 \
            or slinky.snake_head.ycor() > 280 \
            or slinky.snake_head.ycor() < -280:
        scoreboard.game_over()
        game_is_on = False

    # Detect collision with tail
    # if head collides with any segment in tail
    for segment in slinky.slinky:
        if segment == slinky.snake_head:
            pass  # nothing to do here

        elif slinky.snake_head.distance(segment) < 5:
            game_is_on = False
            scoreboard.game_over()

# done
screen.exitonclick()
