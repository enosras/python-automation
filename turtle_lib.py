import turtle
import time
import math


win = turtle.Screen()  
win.bgcolor("lightblue")
win.title("Signal Reader")
win.setworldcoordinates(-180, -1.5, 720, 1.5)


cursor = turtle.Turtle()
cursor.color("blue")
cursor.penup
cursor.speed(10)

for i in range(2880) :
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
win.mainloop()
#win.exitonclick()