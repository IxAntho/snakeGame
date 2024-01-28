from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.speed("fastest")
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        # We call this method at last because we need to set
        # everything up to place our scoreboard where we want
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score = {self.score} High Score: {self.read_high_score()}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.read_high_score():
            self.write_high_score(self.score)
        self.score = 0
        self.update_scoreboard()

    def read_high_score(self):
        with open("data.txt", mode="r") as file:
            return int(file.read())

    def write_high_score(self, score):
        with open("data.txt", mode="w") as file:
            file.write(str(score))
