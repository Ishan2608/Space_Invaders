from turtle import Turtle

try:
    f = open('score_keeper.txt', 'r')
    data = int(f.read())
except FileNotFoundError:
    f = open('score_keeper.txt', 'w')
    data = 0
    f.write(str(data))


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = data
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(-480, 260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Score: {self.score} | HighScore: {self.highscore}',align='left', font=('Courier', 28, 'normal'))

    def inc_score(self):
        self.score += 1
        if self.score > self.highscore:
            self.highscore = self.score
        self.update_score()

    def write_final_score(self):
        score = self.highscore
        open('score_keeper.txt', 'w').write(str(score))

