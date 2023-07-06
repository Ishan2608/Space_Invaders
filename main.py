"""
Make the necessary imports
--- turtle: library to make graphics.
--- time: library to track time.
--- UI: class for UI elements
--- Spaceship: class for player's spaceship
--- Aliens: class for alien ships (player's enemy)
--- Score: class for maintaining scoreboard
"""

import turtle
import time
from ui import UI
from spaceship import Spaceship
from alienships import Aliens
from scoreboard import Score

# Create the screen object
screen = turtle.Screen()
# Give it desired size
screen.setup(width=1000, height=600)
# Set a background image
screen.bgpic('space.gif')
# Give a title to the game window
screen.title('Space Invaders: Shoot Those Aliens Down. Protect Mother Earth')

"""
To make the UI more attractive, we are going to have an option of spaceships
that will be randomly assigned to users. Similarly we will maintain a list
of ships for aliens with different healths. To be able to use images in turtle
(NOTE: we can use only GIF images with Turtle) we need to first add them to
screen object. Then, we can simply assign them to any turtle we want.
"""

# Adding GIFs for Player
human_ship = './gifs/humanship.gif'
human_ship2 = "./gifs/humanship2.gif"
human_ship3 = "./gifs/humanship3.gif"
human_ship4 = "./gifs/humanship4.gif"
screen.addshape(human_ship)
screen.addshape(human_ship2)
screen.addshape(human_ship3)
screen.addshape(human_ship4)

# Adding GIFs for Aliens
alien_ship = './gifs/alienship.gif'
alien_ship2 = './gifs/alienship2.gif'
alien_ship3 = './gifs/alienship3.gif'
screen.addshape(alien_ship)
screen.addshape(alien_ship2)
screen.addshape(alien_ship3)

"""
When tracer is set to 0, we kill the animation. We do it because we don't
want all the changes to be shown to user immediately, but only when they need
to be to have a smooth transition.  
"""
screen.tracer(0)

# Creating Object from the Classes we imported.
ui = UI()
spaceship = Spaceship()
aliens = Aliens()
score = Score()

# A variable to maintain pause and ongoing state of the game..
is_game_paused = False


def pause_game():
    """
    Function to change the value of our game pause checking variable.
    When the player presses SpaceBar, if the game is paused, then it
    should resume, and if it was not paused, then it should.
    """
    global is_game_paused
    if is_game_paused:
        is_game_paused = False
    else:
        is_game_paused = True


"""
Now we will set up our screen listeners, i.e., whenever user triggers
an event, such as a keypress. Then we want something to happen.
When up arrow is pressed, the user should shoot.
When left arrow is pressed, the user should move left.
When right arrow is pressed, the user should move right.
When SpaceBar is pressed, the game should pause/resume.
For each key press, a function is assigned that will do the necessary
tasks to give the effect meant for that key.
Calling screen.listen() simply tells that we want to listen to events.
"""
screen.listen()
screen.onkey(key='Up', fun=spaceship.shoot)
screen.onkey(key='Left', fun=spaceship.move_left)
screen.onkey(key='Right', fun=spaceship.move_right)
screen.onkey(key='space', fun=pause_game)

"""
We don't know how long the loop will run. It depends on the player.
Thus we run a while loop based on a boolean variable. When the game
ends, this variable will be set to False, the loop will end and Game
will get over. We could have also use while True: and then use the
break statement when needed to end the game.
"""

"""
A variable to track time elapsed. Set it to current time.
Later on in game loop, we keep calculating current time and
compare it with this timer, when the difference is 5, it means
5 seconds have elapsed, so we bring aliens down. The update this
variable to then current time. So that above functionality continues.
"""

timer = time.time()

playing_game = True
while playing_game:
    """
    NOTE: When creating a game loop, first, all the loop breaking situations
    must be assessed, and then events should be listened to. If we keep them
    to the last, then a situation will arise where the game ending condition
    was met but the user was still able to affect the game through event, once.
    First we check if the game is paused or not. If not, continue,
    If yes, just show the message of Game being paused.
    """
    if not is_game_paused:
        """
        Remember we set the screen.tracer(0) to kill the animation. We did
        it so that the user does not see the turtles being created and moving
        to their designated positions. We wanted it to happen and without the 
        user seeing the process. We wanted to show the final positions directly.
        Now that we have created our objects above and they have been placed
        and we are ready to play as we are in the game loop, we turn on the animation
        again. As now we do want the user to see his changes. 
        """
        screen.update()

        """
        Our second condition to check if whether there are any alien ships in the
        game or not, if all of them have been eliminated, then we simply break the loop.
        Since no ships exist, that means the user has won. So, we call the function that
        shows the congratulation message. And also write the final score.
        """
        if len(aliens.alien_ships) == 0:
            ui.game_complete()
            score.write_final_score()
            break

        """
        Since we passed the above condition, that means aliens do exist, and we need
        to bring them closer to the user. Calculate current time and compare it with
        timer, if the difference is greater than 5 (get integer value), then it means 5 secs
        have elapsed, so we bing the aliens down.
        """
        now = time.time()
        gap = int(now - timer)
        if gap > 5:
            """
            Traverse though aliens list, make each alien move down
            by changing its y coordinates.
            """
            for alien in aliens.alien_ships:
                alien.goto(alien.xcor(), alien.ycor() - 40)
                """
                Now that a alien ship has moved, there is a possibility
                that it may have read the user, thus we want to end the game
                and don't want to bother going to other alien ships.
                """
                if alien.ycor() < -200:
                    playing_game = False
                    ui.game_over()
                    score.write_final_score()
                    break
            """
            After all the aliends moved, we simply update the timer variable 
            to current time, cuz now we want to check for 5 seconds
            elapsed from this moment.
            """
            timer = now

        """
        Since the game is going on, there is a chance that user has shot a bullet.
        In that case, simply detect if a bullet struck an alien or not. If yes,
        reduce that alien's health by 1, if it becomes zero, remove it.
        """
        for bullet in spaceship.bullets:
            # move every bullet found in user's shot bullets forward.
            bullet.move()
            # for every ship in alien army
            for a in aliens.alien_ships:
                # check if the bullet has touched the alien ship
                if bullet.distance(a) < 22:
                    # if yes, reduce its health by 1.
                    a.health -= 1
                    # if it has become zero
                    if a.health == 0:
                        # first move the alien ship out of sight
                        a.goto(3000, 3000)
                        # then delete it.
                        aliens.alien_ships.remove(a)
                    # since the bullet hit a ship, it too needs to be removed
                    # first, move it out of sight
                    bullet.goto(3000, 3000)
                    # then remove it.
                    spaceship.bullets.remove(bullet)
                    # now increase the player's score by one.
                    score.inc_score()

    # if the game is not paused. Delay program running by 0.5 seconds
    # then change color of the text shown.
    else:
        time.sleep(0.5)
        ui.change_color()

# keep the screen running
turtle.mainloop()
