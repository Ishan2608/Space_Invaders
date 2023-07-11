from turtle import Turtle
from random import choice
"""
we want our aliens to have different healths, but we want to keep the ratio biased.
We want to make sure that maximum have health 1, and minimum have health 3.
"""
qty = [1, 1, 1, 3, 1, 2, 1, 3, 1, 1, 3, 1, 1, 2, 1, 1, 1, 2, 1, 3, 1, 2, 1, 2, 1, 1, 1, 1, 2, 1, 1, 2]


class AlienShip(Turtle):
    def __init__(self, x, y):
        super().__init__()
        """
        As usual, lift the turtle using penup(). Make it go to the designated position.
        Choose a health randomly. Based on the health, give an image to the ship.
        """
        self.penup()
        self.goto(x, y)
        self.health = choice(qty)
        if self.health == 1:
            self.shape('./gifs/alienship.gif')
        elif self.health == 2:
            self.shape('./gifs/alienship2.gif')
        elif self.health == 3:
            self.shape('./gifs/alienship3.gif')


class Aliens:
    """
    This class will create several objects from the above class and position
    them according to the size of the screen. Remember that the center of the screen is
    the origin of the coordinate axes. Thus right and left boundary are half of the total width.
    Same goes for the height. We place them in the center.
    """
    def __init__(self):
        """
        We keep track of all the alien ships using a list.
        And then call the method that creates all the lanes altogether.
        """
        self.alien_ships = []
        self.create_all_lanes()

    def create_lane(self, y_cor):
        """
        Go from left most boundary to right most boundary, where you want to place the aliens.
        Change only x coordinate, keep the y coordinate same since all of them are in same lane.
        After creating the alien ship and positioning it, add it to the list.
        """
        for i in range(-350, 390, 80):
            alien_ship = AlienShip(i, y_cor)
            self.alien_ships.append(alien_ship)

    def create_all_lanes(self):
        """
        Call the above methods using a loop. The y coordinates keep changing as the above method
        that creates a single lane, uses same y coordinates. The range of x coordinates remains the
        same for all the lanes.
        """
        for i in range(20, 240, 50):
            self.create_lane(i)
