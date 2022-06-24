import turtle
import time
from ui import UI
from spaceship import Spaceship
from alienships import Aliens
from scoreboard import Score

# setting up screen
screen = turtle.Screen()
screen.setup(width=1000, height=600)
screen.bgpic('space.gif')
screen.title('Space Invaders: Shoot Those Aliens Down. Protect Mother Earth')
human_ship = 'humanship.gif'
alien_ship = 'alienship.gif'
screen.addshape(human_ship)
screen.addshape(alien_ship)
screen.tracer(0)


# creating our objects of the Games
ui = UI()
spaceship = Spaceship()
aliens = Aliens()
score = Score()

is_game_paused = False
timer = 0


def pause_game():
    global is_game_paused
    if is_game_paused:
        is_game_paused = False
    else:
        is_game_paused = True


screen.listen()
screen.onkey(key='Up', fun=spaceship.shoot)
screen.onkey(key='Left', fun=spaceship.move_left)
screen.onkey(key='Right', fun=spaceship.move_right)
screen.onkey(key='space', fun=pause_game)

playing_game = True
while playing_game:
    if not is_game_paused:
        screen.update()

        if len(aliens.alien_ships) == 0:
            ui.game_complete()
            score.write_final_score()
            break

        now = time.localtime().tm_sec
        gap = now - timer

        time.sleep(0.01)

        if gap % 5 == 0:
            for alien in aliens.alien_ships:
                alien.goto(alien.xcor(), alien.ycor()-1)
                if alien.ycor() < -200:
                    playing_game = False
                    ui.game_over()
                    score.write_final_score()
                    break

            timer = now

        for bullet in spaceship.bullets:
            bullet.move()

            for a in aliens.alien_ships:
                if bullet.distance(a) < 22:
                    a.health -= 1
                    if a.health == 0:
                        a.goto(3000, 3000)
                        aliens.alien_ships.remove(a)
                    bullet.goto(3000, 3000)
                    spaceship.bullets.remove(bullet)
                    score.inc_score()

    else:
        time.sleep(0.5)
        ui.change_color()

turtle.mainloop()
