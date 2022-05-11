"""
GAME: Cannon.
AUTHOR 1: Carla Onate Gardella.
AUTHOR 2: Octavio Augusto Aleman Esparza.

DATE: May - 11 - 2022.

"""

from random import randrange
from turtle import *

from freegames import vector

import time # Time library has been imported in order to take time measures within the compilation of the code.

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []


def tap(x, y):
    """Respond to screen tap."""
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25


def inside(xy):
    """Return True if xy within screen."""
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw():
    """Draw ball and targets."""
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

def takeTime(): # The takeTime() function has been added. This function declares and sets the initial values of the global variables necessary to take time measures.
    global start # The variable start is declared as global.
    start = time.time() # The variable start is given the initial value of the current time.

    global speedTargets # The variable speedTargets is declared as global.
    speedTargets = 0.5 # The variable speedTargets is given its initial value.

    global speedBall # The variable speedBall is declared as global.
    speedBall = 0.35 # The variable speedBall is given its initial value.

    global currentTime # The variable currentTime is declared as global.
    currentTime = 0.0 # The variable currentTime is given its initial value.

def adjustSpeed(): # The function adjustSpeed() has been added. Its purpose is to increase both the target and ball's speed every time a 20 second interval passes. 

    global currentTime, speedTargets, speedBall, start # The necessary variables are declared as global. 

    currentTime = time.time() # The current time measure is saved in the currentTime variable.

    dif = (currentTime - start) # The difference between the saved start time measure and current time measure is calculated.

    if dif >= 20.0: # If the difference between both time measures is equal or greater than 20 (seconds), the function will run the following code.
        speedTargets = speedTargets + 0.5 # The speed of the targets is increased in 0.5. 
        speedBall = speedBall - 0.05 # The speed of the Ball is increased in 0.05.

        start = time.time() # The start variable is given a new value, now measuring the time passed since the last time the speed was increased.


def move():
    """Move ball and targets."""
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    adjustSpeed() # The adjustSpeed() function is called.

    for target in targets:
        target.x -= speedTargets # The Targets speed contained in the speedTargets variable is asigned.
        
    if inside(ball):
        speed.y -= speedBall # The Ball's speed contained in the speedBall variable is asigned.
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    for target in targets:
        if not inside(target): # if dot not inside canvas
            target.x = 250 # reset x to initial position
            target.y = randrange(-150, 150) # set y to random position in canvas
            # remove return so that the game doesn't end

    ontimer(move, 50)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
takeTime() # The takeTime() function is called.
move()
done()
