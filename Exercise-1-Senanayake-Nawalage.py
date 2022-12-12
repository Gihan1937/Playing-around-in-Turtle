# -*- coding: utf-8 -*-
"""
Program: Assignment 03
Author: Paolo
Last date modified: 2022/09/27

"""

## question 01

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
operation_symbol = 'Please choose which type calculation you need Type 1 for addition, Type 2 for substraction, Type 3 for product, Type 4 for division, Type 5 to Quit: '


### LOOP
### set variable for the while loop
cal = True
while (cal == True):
    
    # read user input & store in variables
    opernation = input(operation_symbol)
    
    # perform the calculation: selecting the mathamatical operation to do

    if(opernation == '1'):
        number_1 = int(input(input_number_1))
        number_2 = int(input(input_number_2))
        print('Sum of 2 numbers is: ',number_1 + number_2) 

    elif(opernation == '2'):
        number_1 = int(input(input_number_1))
        number_2 = int(input(input_number_2))
        print('Difference of 2 numbers is: ',number_1 - number_2)

    elif(opernation == '3'):
        number_1 = int(input(input_number_1))
        number_2 = int(input(input_number_2))
        print('Product of 2 numbers is: ',number_1 * number_2)

    elif(opernation == '4'):
        number_1 = int(input(input_number_1))
        number_2 = int(input(input_number_2))
        print('Division of 2 numbers is: ',number_1 / number_2)

    elif(opernation == '5'):
       print('Quit')
       cal = False

    else:
        print('Invalid Insert')
        cal = False






