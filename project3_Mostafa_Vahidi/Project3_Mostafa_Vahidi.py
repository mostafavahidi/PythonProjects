'''
Author: Mostafa Vahidi
CS 2990 Project 3
Prof. Yang
'''

import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

def getNumShells():
    listOfNames = ['Alex', 'Bay', 'Dana', 'Max', 'Terry', 'Wes']
    listOfTuples = []

    for i in range(6):
        print("Hello", listOfNames[i], "! Please tell me how many different shells you collected.")
        
        pukaAmount = int(input("Puka: "))
        coneAmount = int(input("Cone: "))
        driftWoodAmount = int(input("Driftwood: "))
        seaGlassAmount = int(input("Sea Glass: "))
        starFishAmount = int(input("Star Fish Amount: "))

        pukaT = ("Puka", pukaAmount)
        coneT = ("Cone", coneAmount)
        driftWoodT = ("Driftwood", driftWoodAmount)
        seaGlassT = ("Seaglass", seaGlassAmount)
        starFishT = ("Starfish", starFishAmount)

        listOfTuples.append(pukaT)
        listOfTuples.append(coneT)
        listOfTuples.append(driftWoodT)
        listOfTuples.append(seaGlassT)
        listOfTuples.append(starFishT)


    print("Printing all of the shells for all students: ")
    for x in listOfTuples:
        print (x[0], x[1])

    print("DEBUGGINGGGGGGG")
    print(listOfTuples)
    
    return listOfTuples



def getCount(listOfTuples):
    newTuplesList = []
    
    pukaCount = 0
    coneCount = 0
    driftWoodCount = 0
    seaGlassCount = 0
    starFishCount = 0

    for i in range(len(listOfTuples)):
        if listOfTuples[i][0] == "Puka":
            pukaCount += listOfTuples[i][1]
        elif listOfTuples[i][0] == "Cone":
            coneCount += listOfTuples[i][1]
        elif listOfTuples[i][0] == "Driftwood":
            driftWoodCount += listOfTuples[i][1]
        elif listOfTuples[i][0] == "Seaglass":
            seaGlassCount += listOfTuples[i][1]
        elif listOfTuples[i][0] == "Starfish":
            starFishCount += listOfTuples[i][1]

    pukaT = ("Puka", pukaCount)
    coneT = ("Cone", coneCount)
    driftWoodT = ("Driftwood", driftWoodCount)
    seaGlassT = ("Seaglass", seaGlassCount)
    starFishT = ("Starfish", starFishCount)

    newTuplesList.append(pukaT)
    newTuplesList.append(coneT)
    newTuplesList.append(driftWoodT)
    newTuplesList.append(seaGlassT)
    newTuplesList.append(starFishT)

    print("Printing Total Count of each shell")
    for x in newTuplesList:
        print (x[0], x[1])

    return newTuplesList


def getPrices(newTuplesList):
    pukaPrice = 0
    conePrice = 0
    driftWoodPrice = 0
    seaGlassPrice = 0
    starFishPrice = 0
    

    for i in newTuplesList:
        if i[0] == "Puka":
            pukaPrice = i[1] * 1.00
        elif i[0] == "Cone":
            conePrice = i[1] * 1.50
        elif i[0] == "Driftwood":
            driftWoodPrice = i[1] * 0.50
        elif i[0] == "Seaglass":
            seaGlassPrice = i[1] * 2.00
        elif i[0] == "Starfish":
            starFishPrice = i[1] * 2.50

    print("Price of each type of shell gathered: ")
    print("Puka Price: ", pukaPrice)
    print("Cone Price: ", conePrice)
    print("Driftwood Price: ", driftWoodPrice)
    print("Sea Glass Price: ", seaGlassPrice)
    print("Star Fish Price: ", starFishPrice)
    
def drawBarGraph(popularity_data):

    # save the names and their respective scores separately 
    # reverse the tuples to go from most frequent to least frequent 
    shell = list(zip(*popularity_data))[0]
    score = list(zip(*popularity_data))[1]
    x_pos = np.arange(len(shell)) 

    # calculate slope and intercept for the linear trend line
    slope, intercept = np.polyfit(x_pos, score, 1)
    trendline = intercept + (slope * x_pos)

    #plt.plot(x_pos, trendline, color='red', linestyle='--')    
    plt.bar(x_pos, score,align='center')
    plt.xticks(x_pos, shell) 
    plt.ylabel('Frequency of Each Kind')
    plt.xlabel('Types of Shells Found')
    plt.show()

def main():
    listOfTuples = getNumShells()

    countOfTuplesList = getCount(listOfTuples)

    getPrices(countOfTuplesList)

    drawBarGraph(countOfTuplesList)

main()



'''
OUTPUT

Hello Alex ! Please tell me how many different shells you collected.
Puka: 1
Cone: 2
Driftwood: 3
Sea Glass: 4
Star Fish Amount: 5
Hello Bay ! Please tell me how many different shells you collected.
Puka: 1
Cone: 2
Driftwood: 3
Sea Glass: 4
Star Fish Amount: 5
Hello Dana ! Please tell me how many different shells you collected.
Puka: 1
Cone: 2
Driftwood: 3
Sea Glass: 4
Star Fish Amount: 5
Hello Max ! Please tell me how many different shells you collected.
Puka: 1
Cone: 2
Driftwood: 3
Sea Glass: 4
Star Fish Amount: 5
Hello Terry ! Please tell me how many different shells you collected.
Puka: 1
Cone: 2
Driftwood: 3
Sea Glass: 4
Star Fish Amount: 5
Hello Wes ! Please tell me how many different shells you collected.
Puka: 1
Cone: 2
Driftwood: 3
Sea Glass: 4
Star Fish Amount: 5
Printing all of the shells for all students: 
Puka 1
Cone 2
Driftwood 3
Seaglass 4
Starfish 5
Puka 1
Cone 2
Driftwood 3
Seaglass 4
Starfish 5
Puka 1
Cone 2
Driftwood 3
Seaglass 4
Starfish 5
Puka 1
Cone 2
Driftwood 3
Seaglass 4
Starfish 5
Puka 1
Cone 2
Driftwood 3
Seaglass 4
Starfish 5
Puka 1
Cone 2
Driftwood 3
Seaglass 4
Starfish 5
DEBUGGINGGGGGGG
[('Puka', 1), ('Cone', 2), ('Driftwood', 3), ('Seaglass', 4), ('Starfish', 5), ('Puka', 1), ('Cone', 2), ('Driftwood', 3), ('Seaglass', 4), ('Starfish', 5), ('Puka', 1), ('Cone', 2), ('Driftwood', 3), ('Seaglass', 4), ('Starfish', 5), ('Puka', 1), ('Cone', 2), ('Driftwood', 3), ('Seaglass', 4), ('Starfish', 5), ('Puka', 1), ('Cone', 2), ('Driftwood', 3), ('Seaglass', 4), ('Starfish', 5), ('Puka', 1), ('Cone', 2), ('Driftwood', 3), ('Seaglass', 4), ('Starfish', 5)]
Printing Total Count of each shell
Puka 6
Cone 12
Driftwood 18
Seaglass 24
Starfish 30
Price of each type of shell gathered: 
Puka Price:  6.0
Cone Price:  18.0
Driftwood Price:  9.0
Sea Glass Price:  48.0
Star Fish Price:  75.0

'''










    
