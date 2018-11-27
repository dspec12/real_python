#!/usr/bin/env python3

'''
Write a script invest.py that will track the growing amount of an investment over time. This script includes an invest()
 function that takes three inputs: the initial investment amount, the annual compounding rate, and the total number of years
  to invest. So, the first line of the function will look like this:

def invest(amount, rate, time):
The function then prints out the amount of the investment for every year of the time period.

In the main body of the script (after defining the function), use the following code to test your function:

invest(100, .05, 8)
invest(2000, .025, 5)
'''

def invest(amount, rate, time):
    print("principal amount: ${}".format(amount))
    print("annual rate of return:", rate)
    for t in range(1, time + 1):
        amount = amount * (1 + rate)
        print("year {}: ${}".format(t, amount))
    print()

invest(100, .05, 8)
invest(2000, .025, 5)
