# -*- coding: utf-8 -*-
"""
Program: Assignment 03
Author: Paolo
Last date modified: 2022/09/27

"""

## question 06

### libraries ###
# import the turtle library
import turtle

# Welcome Message
welcome = 'Welcome to Turtle .'
print(welcome)

### Variables

# create the pen
pen = turtle.Pen()

# length and the gap
length = 150
gap = 20
angle = 20

for line in range(10):
    # draw
    pen.left(angle)
    pen.forward(length)
    pen.up()
    pen.backward(length)
    pen.right(angle)
    pen.forward(gap)
    pen.down()
    

# close window on click
turtle.exitonclick()



