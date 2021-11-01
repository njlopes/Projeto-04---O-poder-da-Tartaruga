from turtle import *


speed(11)
shape('turtle')
pensize(7)
color('Blue')


for count in range(6):
    forward(40)
    right(60)
    for count in range(3):
        forward(20)
        backward(20)
        left(60)
    right(120)
    backward(40)
    left(60)


done()
