#!/usr/bin/env python3

'''
Define a function, enrollment_stats(), that takes, as an input, a list of lists where each individual list contains three elements: (a) the name of a university, 
(b) the total number of enrolled students, and (c) the annual tuition fees.

Sample list:

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]
This function should return two lists: the first containing all of the student enrollment values and the second containing all of the tuition fees.

Next, define a mean() and a median() function. Both functions should take a single list as an argument and return the mean and median from the values in each 
list. Use the return values from enrollment_stats() as arguments for each function. Challenge yourself by finding a way to sum all the values in a list without using the built-in 'sum()' function for calculating the mean.

At some point you should calculate the total students enrolled and the total tuition paid.

Finally, output all values:

*************************
Total students:   77285
Total tuition:  $ 271905

Student mean:     11040
Student median:   10566

Tuition mean:   $ 38843
Tuition median: $ 39849
*************************
'''
import statistics

def enrollment_stats(lists_of_universities):
    student_enrollment = []
    tuition_fees = []
    for university in lists_of_universities:
        student_enrollment.append(university[1])
        tuition_fees.append(university[2])
    return(student_enrollment, tuition_fees)


def mean(list_of_nums):
    '''Returns the mean from a list of numbers'''
    return(int(sum(list_of_nums) / len(list_of_nums)))

def median(list_of_nums):
    '''Returns the median from a list of numbers'''
    return(statistics.median(list_of_nums))
    
def main():

    universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
    ]

    print("***************************")  
    print("Total students:   ", sum(enrollment_stats(universities)[0]))
    print("Total tuition:   $", sum(enrollment_stats(universities)[1]))
    print()
    print("Student mean:     ", mean(enrollment_stats(universities)[0]))
    print("Student median:   ", median((enrollment_stats(universities)[0])))
    print()
    print("Tuition mean:    $", mean(enrollment_stats(universities)[1]))
    print("Tuition median:  $", median((enrollment_stats(universities)[1])))
    print("***************************")

if __name__ == "__main__":
    main()