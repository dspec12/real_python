#!/usr/bin/env python3

'''
1. Use a break statement to write a script that prompts the users for input repeatedly, only ending when the user types "q" 
or "Q" to quit the program; a common way of creating an infinite loop is to write while True:.
'''
while True:
    user_input = input("Press Q or q to quit: ")
    if user_input == "Q" or "q":
        break

'''
2. Combine a for loop over a range() of numbers with the continue keyword to print every number from 1 through 50 except for 
multiples of 3; you will need to use the % operator.
'''
for i in range(1, 51):
    if i % 3 == 0:
        continue
    print(i)