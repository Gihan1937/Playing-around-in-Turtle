# -*- coding: utf-8 -*-
"""
Program: Assignment 03
Author: Paolo
Last date modified: 2022/09/27

"""

## question 02

### libraries ###
# import the math library
from math import *

# Welcome Message
welcome = 'Welcome to Simple Calculator.'
print(welcome)

### Variables
# Message to be displayed at the start
input_number_1 = 'Please enter number 01: '
input_number_2 = 'Please enter number 02: '
operation_symbol = 'Please enter the Operation symbol from(+,-,*,/) and $ to exit: '


### LOOP
### set variable for the while loop
cal = True
while (cal == True):
    
   # read user input & store in variables
    number_1 = input(input_number_1)
    if(number_1 == ''):
        print('Quit')
        break
    number_2 = input(input_number_2)
    if(number_2 == ''):
        print('Quit')
        break
    opernation = input(operation_symbol)
    if(opernation == ''):
        print('Quit')
        break
    
    # perform the calculation: selecting the mathamatical operation to do

    if(opernation == '+'):
        int_1 = int(number_1)
        int_2 = int(number_2)
        print('Sum of 2 numbers is: ',int_1 + int_2) 

    elif(opernation == '-'):
        int_1 = int(number_1)
        int_2 = int(number_2)
        print('Difference of 2 numbers is: ',int_1 - int_2)

    elif(opernation == '*'):
        int_1 = int(number_1)
        int_2 = int(number_2)
        print('Product of 2 numbers is: ',int_1 * int_2)

    elif(opernation == '/'):
        int_1 = int(number_1)
        int_2 = int(number_2)
        print('Division of 2 numbers is: ',int_1 / int_2)

    else:
        print('Invalid Insert')
        cal = False






