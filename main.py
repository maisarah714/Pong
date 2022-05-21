import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

screen.listen()

r_paddle = Paddle((350, 0))
screen.onkeypress(key="Right", fun=r_paddle.move_up)
screen.onkeypress(key="Left", fun=r_paddle.move_down)

l_paddle = Paddle((-350, 0))
screen.onkeypress(key="a", fun=l_paddle.move_up)
screen.onkeypress(key="d", fun=l_paddle.move_down)

ball = Ball()
scoreboard = Scoreboard()

# if r_paddle.distance(screen) < 10:

game_is_on = True
while game_is_on:
    scoreboard.display_score()
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # hit right wall
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.update_score("right")
    #  hit left wall
    elif ball.xcor() < -380:
        ball.reset()
        scoreboard.update_score("left")
    # hit right paddle
    elif ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_right_paddle()
        ball.increase_speed()
    elif ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_left_paddle()
        ball.increase_speed()


screen.exitonclick()
