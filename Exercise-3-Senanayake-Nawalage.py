# -*- coding: utf-8 -*-
"""
Program: Assignment 03
Author: Paolo
Last date modified: 2022/09/27

"""

## question 03

### libraries ###
# import the turtle library
import turtle

# Welcome Message
welcome = 'Welcome to Turtle .'
print(welcome)

### Variables

# create the pen
pen = turtle.Pen()


# read user input & store in variables
length = 100

for side in range(4):
    pen.forward(length)
    pen.right(90)


# close window on click
turtle.exitonclick()



