#!/usr/bin/env python3
'''
1.)
'''
poem = open("poem.txt", "r")

for line in poem.readlines():
    print(line, end="")

poem.close()

print()
print()
'''
2.)
'''
with open("poem.txt", "r") as f:
    line = f.readline()
    while line != "":
        print(line, end=""),
        line = f.readline()
 
'''
3.) A
'''
output = open("output.txt", "w")
poem = open("poem.txt", "r")

for line in poem.readlines():
    output.write(line)

output.close()
poem.close()
'''
3.) B
'''
with open("poem.txt", "r") as poem, open("output.txt", "w") as output:
    for line in poem.readlines():
        output.write(line)
'''
4.)
'''
with open("output.txt", "a") as output:
    output.write("\nLast MF line!")