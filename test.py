import turtle
from turtle import *
t = Turtle()
print("test")
Turtle.speed('fastest')

def mysisterGOONS():
    for i in range(200):
        t.forward(i * 3)
        t.right(90)
Turtle.done()

mysisterGOONS()
Turtle.done()