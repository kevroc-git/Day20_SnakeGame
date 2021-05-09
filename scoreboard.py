from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,280)
        self.score = 0
        self.write_score()



    def increase_score(self):
        self.clear()
        self.score += 1
        self.write_score()

    def write_score(self):
        self.write("Score: " + str(self.score), move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

