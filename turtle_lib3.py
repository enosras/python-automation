import turtle
from random import random

t = turtle.Screen()
t.bgcolor("orange")
t.title("image-GENERATOR")


cursor = turtle.Turtle()
cursor.speed(10)
#cursor.color("blue")
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