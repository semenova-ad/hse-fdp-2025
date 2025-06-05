from turtle import *

shape("turtle")
colormode(255)
speed(100)
bgcolor("black")

for i in range(360):
    pencolor(i % 256, (i*2) % 256, (i*4) % 256)
    rt(1)
    circle(i + 5)

done()
