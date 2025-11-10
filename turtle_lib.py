import turtle
import time
import math


win = turtle.Screen()  
win.bgcolor("purple")
win.title("My Turtle Drawing")
win.setworldcoordinates(-180, -2, 360, 2)


cursor = turtle.Turtle()
cursor.color("blue")
cursor.forward

for i in range(360) :
    rad = math.radians(i)
    y = math.sin(rad)
    #cursor.forward(i)
    cursor.goto(rad, y)
    



cursor.pendown
'''for _ in range(4):
        main_turtle.forward(100)
        main_turtle.right(90)
'''

#time.sleep(2)
#win.mainloop()
win.exitonclick()