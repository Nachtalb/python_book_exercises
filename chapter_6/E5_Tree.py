from turtle import *


def drawTree(length):
    if length < 5:
        return
    else:
        forward(length)
        left(90)
        drawTree(length / 2)
        right(180)
        drawTree(length / 2)
        left(90)
        back(length)


speed(3)
left(90)
drawTree(200)
hideturtle()
