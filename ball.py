from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_right_paddle(self):
        self.x_move = -(abs(self.x_move))

    def bounce_left_paddle(self):
        self.x_move = abs(self.x_move)

    def reset(self):
        self.goto(0, 0)
        self.x_move *= -1
        self.move_speed = 0.1

    def increase_speed(self):
        # if self.speed() < 10:
        #     self.speed(self.speed() + 1)
        self.move_speed *= 0.9
