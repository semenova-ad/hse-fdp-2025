from turtle import *
from random import *

def square(side, color):
    pencolor(color)
    for i in range(4):
        fd(side)
        lt(90)

speed(100)
colormode(255)

colors = ["red", "green", "blue"]

for i in range(1, 1000, 4):
    square(i, choice(colors))

done()