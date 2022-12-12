# -*- coding: utf-8 -*-
"""
Program: Assignment 03
Author: Paolo
Last date modified: 2022/09/27

"""

## question 04

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

for line in range(10):
    # draw
    pen.forward(length)
    pen.up()
    pen.right(90)
    pen.forward(gap)
    pen.left(90)
    pen.backward(length)
    pen.down()

# close window on click
turtle.exitonclick()



