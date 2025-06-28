from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title(titlestring = "Pong")
screen.tracer(0)

r_paddle = Paddle(position=(350.0, 0.0))
l_paddle = Paddle(position=(-350.0, 0.0))
ball = Ball()


screen.listen()
screen.onkey(key = "w", fun = l_paddle.go_up)
screen.onkey(key = "s", fun = l_paddle.go_down)
screen.onkey(key = "Up", fun = r_paddle.go_up)
screen.onkey(key = "Down", fun = r_paddle.go_down)


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()







screen.exitonclick()