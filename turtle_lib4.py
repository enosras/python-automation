import turtle
import time


color = input("Enter the color : ")


root = turtle.Screen()
root.bgcolor(color)


pointer = turtle.Turtle()
forw = 40
forb = 50
forc = 30
while forw < 120:
    for i in range(200):
        pointer.forward(forw)
        pointer.left(180-36.87)
        pointer.forward(forb)
        pointer.left(180-53.13)
        pointer.forward(forc)
        forw = forw + 40
        forb = forb + 50
        forc = forc + 30 

time.sleep(5)
#root.exitonclick
root.mainloop
