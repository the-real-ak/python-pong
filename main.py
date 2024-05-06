from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

import time

screen = Screen()
screen.setup(width=800, height=500)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

player1 = Paddle(position=-350)
player2 = Paddle(position=350)
ball = Ball()
scoreboard = Scoreboard()
screen.update()

screen.onkey(player1.up, "w")
screen.onkey(player1.down, "s")

screen.onkey(player2.up, "Up")
screen.onkey(player2.down, "Down")
screen.listen()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 230 or ball.ycor() < -230:
        ball.bounce_y()

    # Detect collision with right paddle.
    if ball.distance(player2) < 50 and ball.xcor() > 330:
        ball.bounce_x()
    if ball.distance(player1) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    if ball.xcor() > 350:
        scoreboard.increment_player1()
        ball.reset_position()
    if ball.xcor() < -350:
        scoreboard.increment_player2()
        ball.reset_position()

screen.exitonclick()
