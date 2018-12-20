#!/usr/bin/env python3


'''
Create a list named desserts that holds the two string values "ice cream" and "cookies”
'''
desserts = ["ice cream", "cookies"]

'''
Sort desserts in alphabetical order, then display the contents of the list
'''
print(desserts.sort())

'''
Sort desserts in alphabetical order, then display the contents of the list
'''
print(desserts.index("ice cream"))


'''
Copy the contents of the desserts list into a new list object named food
'''
food = desserts[:]

'''
Add the strings "broccoli" and "turnips" to the food list
Display the contents of both lists to make sure that "broccoli" and "turnips" haven't been added to desserts
'''
food.extend(["broccoli", "turnips"])
print(desserts)
print(food)

'''
Remove "cookies" from the food list
'''
food.remove("cookies")

'''
Display the first two items in the food list by specifying an index range
'''
print(food[0:2])

'''
Create a list named breakfast that holds three strings, each with the value of "cookies", by splitting up the string "cookies, cookies, cookies
'''
string = "cookies, cookies, cookies"
breakfast = string.split(", ")
print(breakfast)

'''Define a function that takes a list of numbers, [2, 4, 8, 16, 32, 64], as the argument and then outputs only the numbers from the list that fall between 
1 and 20 (inclusive)”
'''
def numbers(list_of_numbers):
    for num in list_of_numbers:
        if num >= 2 and num <= 20:
            print(num)

list_of_numbers = [2, 4, 8, 16, 32, 64]
numbers(list_of_numbers)