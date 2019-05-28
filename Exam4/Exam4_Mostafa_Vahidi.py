import math
from itertools import chain
'''
Mostafa Vahidi
CS 2990 Python Prof. Yang
Exam 4 11/20/18
'''

def problem_one():
    fileName = input(print("What file name would you like to open?"))
    try:
        file = open(fileName, "r")
        listOfNums = []
        for line in file:
            listOfNums.append([int(x) for x in line.split() if int(x) < 21])

        for i in listOfNums:
            print(sum(i))
                     
    except IOError:
        print("Incorrect file name. Let's try this again.")
        problem_one()



def up(x):
    return x + 3


def problem_three_part_one(function, value):
    return map(function, value)

def problem_three_part_two(listOfTuples):
    listOfNames = [i[0] for i in listOfTuples]
    print(listOfNames)

def main():
    print("[1] problem one \n [2] problem three part one \n [3] problem three part two \n [4] turn tuples into list \n [5] quit")
    userChoice = input(print("Your choice: "))
    if userChoice == '1':
        problem_one()
    elif userChoice == '2':
        print("Using exp")
        problem_three_part_one(math.exp, [int(2)])
    elif userChoice == '3':
        print("Using up")
        problem_three_part_one(up, [int(9)])
    elif userChoice == '4':
        listOfTuples = [("Ben", 12), ("Jake", 10)]
        problem_three_part_two(listOfTuples)
    elif userChoice == '5':
        print("Exiting")
        sys.exit()
    else:
        print("Didn't quite understand that, let's try this again.")
        main()

main()

'''
OUTPUT PROBLEM 1:

[1] problem one 
 [2] problem three part one 
 [3] problem three part two 
 [4] quit
Your choice: 
None1
What file name would you like to open?
Nonescores.txt
72
42
68
35
5


[1] problem one 
 [2] problem three part one 
 [3] problem three part two 
 [4] quit
Your choice: 
None1
What file name would you like to open?
NoneWRONG.TXT
Incorrect file name. Let's try this again.
What file name would you like to open?
None



OUTPUT PROBLEM 3 PART 1:



[1] problem one 
 [2] problem three part one 
 [3] problem three part two 
 [4] turn tuples into list 
 [5] quit
Your choice: 
None4
['Ben', 'Jake']


'''
