import turtle
import math


def law_of_cosines(angle, b):
    dif_side_squared = 2*b*b - 2*b*math.cos(angle)
    dif_side = math.sqrt(dif_side_squared)
    angle_otra = (180 - angle)/2
    print('different side : ' , dif_side)
    print("Other angles each: ", angle_otra)
    return dif_side

if __name__ == "__main__":
    ang = float(input("Enter Angle :"))
    side = float(input("Enter Symetric side :"))
    law_of_cosines(ang, side)



'''

#to have the library and its modules and classes available
screen = turtle.Screen()
screen.bgcolor("orange")
screen.title("cursor art")


cursor = turtle.Turtle()
cursor.color()
cursor.speed(20)
#cursor.penup()
fw1 = 12
fw2 = 13
fw3 = 5
fw4 = 24
fw5 = 10


for i in range(100): 
    
    cursor.forward(fw1)
    fw1*=2
    cursor.left(157.4)
    cursor.forward(fw2)
    fw1*=2
    cursor.left(112.6)
    cursor.forward(fw3)
    fw3*=2

    cursor.right(90)
    cursor.forward(fw1)
    fw1*=2
    cursor.right(157.4)
    cursor.forward(fw2)
    fw2*=2
    cursor.right(112.6)
    cursor.forward(fw5)
    fw5*=2
    cursor.left(112.6)
    cursor.forward(fw2)
    fw2*=2
    cursor.left(157.4)
    cursor.forward(fw4)
    fw4*=2
    cursor.left(157.4)
    cursor.forward(fw2)
    fw2*=2

   # fw1= fw1*2
    #fw2= fw2*2
    
    '''

'''
    cursor.forward(10)
    cursor.left()
    cursor.forward(24)
    cursor.left()
    cursor.forward(26)'''



#cursor.pendown
#screen.exitonclick()