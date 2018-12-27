#!/usr/bin/env python3

'''
Create a tuple named cardinal_nums that holds the strings "first", "second" and "third" in order
'''
cardinal_nums = "first", "second", "third"
'''
Display the string at position 2 in cardinal_nums by using an index number
'''
print(cardinal_nums[1])
print(type(cardinal_nums))
'''
Copy the tuple values into three new strings named pos1, pos2 and pos3 in a single line of code by 
using tuple unpacking, then print those string values
'''
pos1, pos2, pos3 = cardinal_nums
print(pos1, pos2, pos3)