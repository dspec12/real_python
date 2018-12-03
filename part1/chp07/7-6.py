#!/usr/bin/env python3
'''
Write a script that uses the randint() function to simulate the toss of a die, returning a random number between 1 and 6.
'''
from random import randint

def die_roll():
    return(randint(1, 6))
print(die_roll())


'''
Write a script that simulates 10,000 throws of dice and displays the average number resulting from these tosses.
'''
total = 0
rolls = 10000
for i in range(0, rolls):
    total += die_roll()
average = total / rolls
print("After {} rolls, the average number is: {}".format(rolls, average))

