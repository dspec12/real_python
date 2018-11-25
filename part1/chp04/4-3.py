#!/usr/bin/env python3

#In onei line, display the result of trying to find() the substring "a" in the string "AAA"; the result should be -1
print("AAA".find("a"))

#Create a string object that contains the value "version 2.0"; find() the first occurrence of the number 2.0 inside of this string
#by first creating a "float" object that stores the value 2.0 as a floating-point number, then converting that object to a string using the str() function
version = "version 2.0"
v_num = 2.0
print(version.find(str(v_num)))

#Write and test a script that accepts user input using input(), then displays the result of trying to find() a particular letter in that input
input_user = input("Please type a single word with the letter 's': ")
print(input_user.find("s"))
