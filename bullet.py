from turtle import Turtle


class Bullet(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=0.25, stretch_len=2)

    def position_for_human(self, human):
        self.goto(human.xcor(), human.ycor() + 40)
        self.left(90)

    def move(self):
        self.forward(10)

