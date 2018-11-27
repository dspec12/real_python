#!/usr/bin/env python3

#Write a for loop that prints out the integers 2 through 10, each on a new line, by using the range() function
for n in range(2, 11):
    print("n = ", n)
print("Loop Finished")

"""
Use a while loop that prints out the integers 2 through 10 (Hint: you'll need to create a new integer first; there
isn't a good reason to use a while loop instead of a for loop in this case, but it's good practice...)
"""
n = 2
while n < 11:
    print("n = ", n)
    n = n + 1
print("Loop Finished")

'''
Write a function doubles() that takes one number as its input and doubles that number three times using a loop,
 displaying each result on a separate line; test your function by calling doubles(2) to display 4, 8, and 16
'''
def doubles(num):
    '''Takes input and doubles that number three times'''
    num = num * 2
    return(num)

number = 2
for n in range(0, 3):
    number = doubles(number)
    print(number)
