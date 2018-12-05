#!/usr/bin/env python3

''' 
I keep flipping a fair coin until I've seen it land on both heads and tails at least once each - in other words, after I flip 
the coin the first time, I continue to flip it until I get a different result. On average, how many times will I have to flip the coin total?

You will need to use a for loop over a range of trials.
For each trial, first you should check the outcome of the first flip.
Make sure you add the first flip to the total number of flips.
After the first toss, you'll need another loop to keep flipping while you get the same result as the first flip.
'''

from random import randint

def coin_flip():
    return randint(0,1)

trials = 10000
flips = 0

for i in range(0, trials):
    first_flip = coin_flip()
    flips += 1
    while coin_flip() == first_flip:
        flips += 1
    flips += 1
print("Average:", flips / trials)
    

    





