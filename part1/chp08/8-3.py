#!/usr/bin/env python3

'''
Create an empty dictionary named birthdays
'''
birthdays = {}

'''
Enter the following data into the dictionary:

 'Luke Skywalker': '5/24/19'
 'Obi-Wan Kenobi': '3/11/57'
 'Darth Vader': '4/1/41'
'''
birthdays["Luke Skywalker"] = "5/24/19"
birthdays["Obi-Wan Kenobi"] = "3/11/57"
birthdays["Darth Vader"] = "4/1/41"
'''
Write if statements that test to check if 'Yoda' and 'Darth Vader' exist as keys in the dictionary, 
then enter each of them with birthday value 'unknown' if their name does not exist as a key
'''
if "Yoda" not in birthdays:
    birthdays["Yoda"] = "unkown"

if "Darth Vader" not in birthdays:
    birthdays["Darth Vader"] = "unkown"

'''
Display all the key-value pairs in the dictionary, one per line with a space between the name and the birthday, 
by looping over the dictionary's keys
'''
for x in birthdays:
    print(x, birthdays[x])

'''
Delete 'Darth Vader' from the dictionary
'''
del(birthdays["Darth Vader"])

'''
Bonus: Make the same dictionary by using dict() and passing in the initial values when you first create the dictionary
'''
starwars_bdays = dict([("Luke Skywalker","5/24/19"), 
                       ("Obi-WanKenobi","3/11/57"), 
                       ("Darth Vader","4/1/41"), 
                       ("Yoda","unknown")])
print(starwars_bdays)