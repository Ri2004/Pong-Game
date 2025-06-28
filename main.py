from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title(titlestring = "Pong")
screen.tracer(0)

r_paddle = Paddle(x_pos = 350, y_pos = 0)
l_paddle = Paddle(x_pos = -350, y_pos = 0)


screen.listen()
screen.onkey(key = "Up", fun = r_paddle.go_up)
screen.onkey(key = "Up", fun = l_paddle.go_up)

game_is_on = True

while game_is_on:
    screen.update()









screen.exitonclick()