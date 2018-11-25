#!/usr/bin/env python3

'''
Write a script called exponent.py that receives two numbers from the user and displays the result of
taking the first number to the power of the second number. A sample run of the program should look
like this (with example input that has been provided by the user included below)

# Enter a base: 1.2
# Enter an exponent: 3
# 1.2 to the power of 3 = 1.728”
'''

base_num = input("Enter the base number: ")
exponent = input("Enter the exponent: ")
result = float(base_num) ** float(exponent)
print("{} to the power of {} = {}".format(base_num, exponent, result))
