import turtle
import random

def drow_circle(r, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()

answer = ''
while answer != 'N':
    answer = turtle.textinput('Нарисовать окружность', 'Y/N')
    if answer == 'Y':
        turtle.goto(random.randrange(-200, 200), random.randrange(-200, 200))
        drow_circle(random.randrange(1, 100), 'white')
    else:
        pass