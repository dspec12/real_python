#!/usr/bin/env python3
'''
Write a script that prompts the user to enter a word using the input() function, stores that input in a variable, 
and then displays whether the length of that string is less than 5 characters, greater than 5 characters, or equal 
to 5 characters by using a set of if, elif and else statements.”
'''

name = input("What's your name? ")

if len(name) < 5:
    print("Your name is less than five characters.")

elif len(name) > 5:
    print("Your name is greater than five characters.")

else:
    print("Your name is equal to five characters")