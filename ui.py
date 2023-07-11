import time
from turtle import Turtle
import random

"""
We show two texts: one is the title, and the other is a paragraph.
We want to place them in the center of the screen. Initial color si white.
We will keep changing the color of the text whenever the game is paused or resumes.
For that we will keep a list of colors to choose from.
"""

FONT = ("Courier", 52, "normal")
FONT2 = ("Courier", 32, "normal")
ALIGNMENT = 'center'
COLOR = "white"
COLOR_LIST = ['light blue', 'royal blue', 'light steel blue', 'steel blue',
              'light cyan', 'light sky blue', 'violet', 'salmon', 'tomato',
              'sandy brown', 'purple', 'deep pink', 'medium sea green', 'khaki']


class UI(Turtle):
    def __init__(self):
        """
        Since it will only write, hide the turtle, lift it up and 
        add a randomly assigned color.
        """
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color(random.choice(COLOR_LIST))
        self.header()

    def header(self):
        """
        Clear the previous text, position it at the center. And write the title & paragraph.
        """
        self.clear()
        self.goto(x=0, y=-150)
        self.write('Space Invaders', align=ALIGNMENT, font=FONT)
        self.goto(x=0, y=-180)
        self.write('Press Space to PAUSE or RESUME the Game', align=ALIGNMENT, font=('Calibri', 14, 'normal'))

    def change_color(self):
        """
        Clear previous text, change the color property by randomly selecting from the list of colors.
        Then call the header function to re-display the text.
        """
        self.clear()
        self.color(random.choice(COLOR_LIST))
        self.header()

    def paused_status(self):
        """
        Clear the screen and change the color of the text to use.
        Since the color will keep changing when the game is paused,
        We want to keep changing the color every 0.5 seconds. Thus,
        when we changed the color. we make the program stop for 0.5s.
        We do this because while loop will keep running and keep entering the else
        block where we update the color. This method will be used repetitively.
        """
        self.clear()
        self.change_color()
        time.sleep(0.5)

    def game_over(self):
        """
        If the game was cleared by the user, then show the regretful message.
        """
        self.clear()
        self.write("Game is Over", align='center', font=FONT)

    def game_complete(self):
         """
         If the game was cleared by the user, then show the congratulately message.
         """
        self.clear()
        self.write('Hooray!! You Completed the Game', align='center', font=FONT2)
