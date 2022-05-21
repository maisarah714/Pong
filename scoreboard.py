from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Courier", 30, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.color("white")
        self.penup()
        self.hideturtle()

    def display_score(self):
        self.clear()
        self.goto(-100, 250)
        self.write(f"{self.score_left}", align=ALIGNMENT, font=FONT)
        self.goto(100, 250)
        self.write(f"{self.score_right}", align=ALIGNMENT, font=FONT)

    def update_score(self, hit):
        if hit == "left":
            self.score_right += 1
        else:
            self.score_left += 1
        self.display_score()
