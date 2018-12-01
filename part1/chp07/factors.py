#!/usr/bin/env python3

'''
“Write a script factors.py that includes a function to find all of the integers that divide evenly into an integer provided by the user.”
'''

integer = input("Enter a positive integer: ")

def factors(num, divisor):
    '''Prints if divisible'''
    if num % divisor == 0:
        print("{} is a divisor of {}".format(divisor, num))

for number in range(1, int(integer) + 1):
    (factors(int(integer), number))













