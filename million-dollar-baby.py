colour_list=[(78, 179, 237), (221, 138, 116), (224, 75, 50), (165, 211, 234), (194, 55, 37), (45, 132, 197), 
             (127,255,212),(0,0,255),(138,43,226),(255,97,3),(118,238,0),(0,238,238),(162,205,90),(178,58,238),(255,20,147),
             (0,191,255),(0,154,205),(255,48,48),(255,215,0),(238,180,34),(31,31,31),(255,105,180),(132,112,255)]

from turtle import Turtle,Screen
import random
tim=Turtle()
myscreen=Screen()
myscreen.colormode(255)
tim.speed('fast')
tim.penup()
x=-250
y=-200
tim.setpos(x,y)
tim.pendown()
for i in range (10):
    for i in range (10):
        color=random.choice(colour_list)
        tim.dot(20,color)
        tim.penup()
        tim.forward(50)
        tim.pendown()
    tim.penup()
    y+=50
    tim.setpos(x,y)

myscreen.exitonclick()
