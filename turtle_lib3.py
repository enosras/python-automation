import turtle
from random import random

t = turtle.Screen()
t.bgcolor("yellow")


cursor = turtle.Turtle()
cursor.speed(1)

cursor.forward(100)
cursor.left(120)
cursor.forward(100)
cursor.left(120)
cursor.forward(100)
#cursor.right(120)
#cursor.forward(100)

t.exitonclick()