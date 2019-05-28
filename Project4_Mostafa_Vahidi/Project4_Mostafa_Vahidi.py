'''
Author: Mostafa Vahidi
Project 4 Prof. Yang
11/6/18
'''
import numpy as np
import matplotlib.pyplot as plt

def plot(listOfNums):
    plt.plot(listOfNums)
    plt.xlabel("Year")
    plt.ylabel("Temperature Anomaly (Celsius)")
    fig, ax = plt.subplots()
    ax.fill(listOfNums, zorder=10)
    ax.grid(True, zorder=0)
    plt.title("Temperatures")
    plt.show()
    

def writeIntoFile(newList):
    try:
        out = open("P4out.txt", 'w')
        out.writelines(str(newList))

    except FileNotFoundError:
        print("File could not be found: ")    

def readFile():
    nameOfFile = input("Type the file name you'd like to read: ")

    try:
        f = open(nameOfFile, 'r')
        listOfNums = []
        for line in f:
            try:
                listOfNums.append(float(line))
            except ValueError:
                print("not float")

        newList = [x * 100 for x in listOfNums]
        writeIntoFile(newList)

        print("Now plotting the values")
        plot(listOfNums)
            
    except FileNotFoundError:
        print("File could not be found: ")

def main():
    readFile()

main()
