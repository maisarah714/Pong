from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__(shape="square")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.setposition(position)

    def move_up(self):
        self.sety(self.ycor()+10)

    def move_down(self):
        self.sety(self.ycor()-10)
