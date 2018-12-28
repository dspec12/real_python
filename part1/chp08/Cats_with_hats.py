#!/usr/bin/env python3
'''
You have 100 cats.

One day you decide to arrange all your cats in a giant circle. Initially, none of your cats have any hats on. You walk around the circle 100 times, 
always starting at the same spot, with the first cat (cat # 1). Every time you stop at a cat, you either put a hat on it if it doesn't have one on, 
or you take its hat off if it has one on.

The first round, you stop at every cat, placing a hat on each one.
The second round, you only stop at every second cat (#2, #4, #6, #8, etc.).
The third round, you only stop at every third cat (#3, #6, #9, #12, etc.).
You continue this process until you've made 100 rounds around the cats (e.g., you only visit the 100th cat).
Write a program that simply outputs which cats have hats at the end
'''

CWH = []
CWNH = []

def place_hat(cat):
    '''Takes or removes hat from a cat's head'''
    if cat in CWH:
         CWH.remove(cat)
    else:
        CWH.append(cat)
        
for round in range(1,101):
    for cat in range(1,101):
        if cat % round:
            pass
        else:
            place_hat(cat)

print("Total number of cat with hats: ", len(CWH))
print("Specific cats with hats: ", CWH)