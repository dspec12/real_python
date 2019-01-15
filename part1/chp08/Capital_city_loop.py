#!/usr/bin/env python3

from capitals import capitals_dict
import random


def capital_game():
    '''Guessing game where a random state is provided and the user has to supply the capital.'''
    
    random_state = random.choice(list(capitals_dict.keys()))
    capital = capitals_dict[random_state]

    while True:
        print("State: ", random_state)
        user_input = input("What is the capital of the state? You can also type 'Exit': ")
        if user_input.lower() == "exit":
            print("The correct answer is: ",capital)
            print("Goodbye")
            break
        elif user_input.lower() == capital.lower():
            print("Correct!")
            break

def main():
    capital_game()

if __name__ == "__main__":
    main()