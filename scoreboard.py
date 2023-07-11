from turtle import Turtle

"""
We will save the highscore in a txt file, so that we can 
keep track of our highscore to see it later on.
Before opening it, check if it even exists. If it does,
store the data into a variable and convert it to integer type.
If it did not exist, create it, and put 0 in it.
"""
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
        """
        If the text file existed and there was some score in it, store it in the object
        as property to show the user the current highscore. Also keep track of the current
        score. Lift it up, hide the turtle itself and make it go to top left of screen.
        """
        self.score = 0
        self.highscore = data
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(-480, 260)
        self.update_score()

    def update_score(self):
        """
        First, clear the text written by the turtle. The write the new text based on new score.
        """
        self.clear()
        self.write(f'Score: {self.score} | HighScore: {self.highscore}',align='left', font=('Courier', 28, 'normal'))

    def inc_score(self):
        """
        Increase the score by 1, if it is higher than the highscore,
        update the highscore as well. Then call the update method to show
        the changed the score to the user.
        """
        self.score += 1
        if self.score > self.highscore:
            self.highscore = self.score
        self.update_score()

    def write_final_score(self):
        score = self.highscore
        open('score_keeper.txt', 'w').write(str(score))

