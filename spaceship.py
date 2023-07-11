from turtle import Turtle
from bullet import Bullet
from random import choice

# distance by which we want to move the spacecraft.
MOVE_DIST = 25

# we randomly pick from this numbers, then based on them, assign an image to turtle.
SHIPS = [1, 2, 3, 4]


class Spaceship(Turtle):
    def __init__(self):
        super().__init__()
        """
        Add an image to the turtle randomly.
        The use penup() method to make sure it does not draw as it moves.
        Create an empty list which will contain all the bullets it will have.
        """
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
        """
        Since the turtle faces right side by default, backward makes it
        look like it moves left.
        """
        self.backward(MOVE_DIST)

    def move_right(self):
        """
        Since the turtle faces right side by default, forward makes it
        look like it moves right.
        """
        self.forward(MOVE_DIST)

    def shoot(self):
        """
        Create an object from bullet class. Position it where the user's spacecraft is.
        Then add it to the list of user's bullets to keep track of them.
        """
        bullet = Bullet()
        bullet.position_for_human(self)
        self.bullets.append(bullet)
