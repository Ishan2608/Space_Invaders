from turtle import Turtle
from bullet import Bullet

MOVE_DIST = 25


class Spaceship(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('humanship.gif')
        self.penup()
        self.goto(x=0, y=-260)
        self.bullets = []

    def move_left(self):
        self.backward(MOVE_DIST)

    def move_right(self):
        self.forward(MOVE_DIST)

    def shoot(self):
        bullet = Bullet()
        bullet.position_for_human(self)
        self.bullets.append(bullet)
