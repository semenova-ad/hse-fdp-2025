from turtle import *
from random import *
from time import *

t1 = Turtle()
t2 = Turtle()
t1.shape("turtle")
t2.shape("turtle")

LEFT_BORDER = -300
RIGHT_BORDER = 300

t1.penup()
t1.goto(LEFT_BORDER, 50)
t1.pendown()
t1.goto(LEFT_BORDER, -50)

t1.penup()
t1.goto(RIGHT_BORDER, 50)
t1.pendown()
t1.goto(RIGHT_BORDER, -50)

t1.penup()
t2.penup()
t1.goto(LEFT_BORDER, 40)
t2.goto(LEFT_BORDER, -40)

while True:
    # pause = input("Нажмите Enter, чтобы продолжить")
    sleep(0.3)
    step1 = randint(1, 3)
    step2 = randint(1, 3)
    t1.forward(step1 * 10)
    t2.forward(step2 * 10)
    if t1.pos()[0] >= RIGHT_BORDER and t2.pos()[0] >= RIGHT_BORDER:
        print("Ничья!")
        t1.circle(20)
        t2.circle(20)
        break
    elif t1.pos()[0] >= RIGHT_BORDER:
        print("Победа первой черепашки!")
        t1.circle(20)
        break
    elif t2.pos()[0] >= RIGHT_BORDER:
        print("Победа второй черепашки!")
        t2.circle(20)
        break

done()