import turtle
from random import random

t = turtle.Screen()
t.bgcolor("yellow")
t.title("IMAGE GENERATOR")


cursor = turtle.Turtle()
cursor.speed(10)
#angle = int(input("enter the angle you want"))
#angle = turtle.textinput("Enter Angle", "Angle Please : ")

angle = 120
for i in range(200):
    cursor.forward(i)
    cursor.left(angle)
    cursor.forward(i)
    cursor.left(angle)
    cursor.forward(i)
    #cursor.right(120)
    #cursor.forward(100)

t.mainloop()
#t.exitonclick()