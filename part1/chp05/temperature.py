#!/usr/bin/env python3

'''
Write a script temperature.py that includes two functions. One function takes a Celsius temperature
as its input, converts that number into the equivalent Fahrenheit temperature and returns that value.
The second function takes a Fahrenheit temperature and returns the equivalent Celsius temperature.
Test your functions by passing input values to them and printing the output results.

For testing your functions, example output should look like:

72 degrees F = 22.2222222222 degrees C
37 degrees C = 98.6 degrees F”

The relevant conversion formulas are:
F = C * 9/5 + 32
C = (F - 32) * 5/9
'''

def c2f(cel):
    '''Takes a Celsius temperature, and converts that number into the equivalent Fahrenheit temperature'''
    fahrenheit = cel * 9/5 + 32
    return fahrenheit

def f2c(fah):
    '''Takes a Fahrenheit temperature and returns the equivalent Celsius temperature'''
    celsius = (fah -32)*5/9
    return celsius

print("""72 degrees F = {} degrees C
37 degrees C = {} degrees F""".format(f2c(72), c2f(37)))
