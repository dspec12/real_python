#!/usr/bin/env python3

'''
Write a cube() function that takes a number and multiplies that number by itself twice over, returning
the new value; test the function by displaying the result of calling your cube() function on a few different numbers
'''
def cube(number):
    '''Returns cubed of the input number'''
    return number ** 3
print(cube(5))

'''
Write a function multiply() that takes two numbers as inputs and multiplies them together, returning the result;
test your function by saving the result of multiply(2, 5) in a new variable and printing it.
'''
def multiply(num1, num2):
    '''Returns the product of two factors supplied'''
    return num1 * num2
ten = multiply(2, 5)
print(ten)
