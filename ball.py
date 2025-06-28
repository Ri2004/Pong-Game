from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1 # move_speed attribute is used to speed up the ball

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

    def bounce_y(self):
        self.y_move *= -1
        # when ball is collided with top and bottom wall, then reverse direction of y co-ords of ball, and increase speed of ball by multiplying with 0.9. when multiply with 0.9
        # then previous speed 0.1, is decreased, when decreased then delay is also less pass in time.sleep() in main.py
        self.move_speed *= 0.9

    def bounce_x(self):
        # when ball is collided with left and right paddle, then reverse direction of y co-ords of ball, and increase speed of ball by multiplying with 0.9. when multiply with 0.9
        # then previous speed 0.1, is decreased, when decreased then delay is also less pass in time.sleep() in main.py
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        # when both paddles miss the ball, then reset the position of ball to (0, 0), and set move_speed with original speed at first i.e., 0.1, and reverse direction of x-axis
        # because when both paddles are in x-axis, so when one of paddle miss the ball, then reverse x-axis direction
        self.setposition(x=(0, 0))
        self.move_speed = 0.1
        self.bounce_x()
