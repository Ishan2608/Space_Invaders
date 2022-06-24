from turtle import Turtle
from bullet import Bullet
from random import choice

MOVE_DIST = 25

SHIPS = [1, 2, 3, 4]


class Spaceship(Turtle):
    def __init__(self):
        super().__init__()
        ship = choice(SHIPS)
        if ship == 1:
            self.shape('./gifs/humanship.gif')
        elif ship == 2:
            self.shape('./gifs/humanship2.gif')
        elif ship == 3:
            self.shape('./gifs/humanship3.gif')
        elif ship == 4:
            self.shape('./gifs/humanship4.gif')
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
