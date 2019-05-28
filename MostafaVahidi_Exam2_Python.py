'''
Author: Mostafa Vahidi
Python Exam 2 Prof. Yang
'''
from random import randint

def getValues(n):
    list = [randint(1, 10) for i in range(n)]
    return list

def sumValues(L):
    sum = 0
    for i in L:
        sum += i
    return sum

def main():
    toTest = int(input("Please type in an integer: "))
    listOfVals = getValues(toTest)
    print("This is the list of values: ", listOfVals)
    sumOfVals = sumValues(listOfVals)
    print("This is the sum of those values: ", sumOfVals)

if __name__ == '__main__':
    main()


'''
Output of program:

Using n=5:

Please type in an integer: 5
This is the list of values:  [10, 8, 2, 7, 5]
This is the sum of those values:  32

Using n=10:

Please type in an integer: 10
This is the list of values:  [6, 9, 2, 7, 6, 4, 5, 10, 9, 8]
This is the sum of those values:  66
'''
