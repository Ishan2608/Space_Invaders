from turtle import Turtle
from random import choice

qty = [1, 1, 1, 1, 1, 2, 1, 3, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2]


class AlienShip(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape('alienship.gif')
        self.penup()
        self.goto(x, y)
        self.health = choice(qty)


class Aliens:
    def __init__(self):
        self.y_start = 0
        self.y_end = 240
        self.alien_ships = []
        self.alien_bullets = []
        self.create_all_lanes()

    def create_lane(self, y_cor):
        for i in range(-350, 390, 80):
            alien_ship = AlienShip(i, y_cor)
            self.alien_ships.append(alien_ship)

    def create_all_lanes(self):
        for i in range(self.y_start, self.y_end, 50):
            self.create_lane(i)
