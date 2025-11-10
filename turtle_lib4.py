import turtle
import time


color = input("Enter the color : ")


root = turtle.Screen()
root.bgcolor(color)


pointer = turtle.Turtle()

for i in range(200):
    pointer.forward(100)
    pointer.left(150)
    pointer.forward(120)
    pointer.left(120)
    pointer.forward(60)

time.sleep(5)
#root.exitonclick
root.mainloop
