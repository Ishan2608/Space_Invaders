from turtle import Turtle

"""
Again, we inherit the turtle class to directly manipulates a turtle's properties 
through the object that will be created from this class.
"""


class Bullet(Turtle):
    def __init__(self):
        """
        First give it a circular shape and then stretch it vertically to give a bullet's look.
        Give it a color of your choice. Here, white is taken. And penup() method is called
        so that the turtle does not draw as it moves.
        """
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=0.25, stretch_len=2)

    def position_for_human(self, human):
        """
        It takes coordinates of the user's spacecraft, place the bullet slightly above it.
        And then turns it to left by 90 degrees. We do it to make bullet face the aliens, i.e.,
        upward direction, as by default, the turtle faces right side.
        """
        self.goto(human.xcor(), human.ycor() + 40)
        self.left(90)

    def move(self):
        """
        Simply move the turtle by 10 steps. This method will be called in game loop. This it will
        be called repetitively and thus the bullet will keep moving forward.
        """
        self.forward(10)

