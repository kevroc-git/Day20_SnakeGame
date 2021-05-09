from turtle import Turtle
print("scoreboard created")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,280)
        self.score = 0
        self.write("Score: 0", move=False, align="center", font=("Arial", 14, "normal"))
        print("scoreboard init section")


    def increase_score(self):
        self.clear()
        self.score += 1
        self.write("Score: " + str(self.score), move=False, align="center", font=("Arial", 14, "normal"))
        # return self.score





