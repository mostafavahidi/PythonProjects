'''
Author: Mostafa Vahidi
CS2990 Lab 7
10/24/18
'''
import sys

listOfNames = ["John", "Tam", "Ken", "Jesse"]
playerDict = {"John": 5, "Tam": 4, "Ken": 3, "Jesse": 2}
global newRating

def getRating(listOfNames, playerDict):

    for name in listOfNames:
        score = int(input("Enter " + name + "'s rating: "))
        playerDict[name] = score


def outputRating(listOfNames, playerDict):

    print("ROSTER")
    for name in sorted(playerDict):
        print(name + ", Rating: " + str(playerDict[name]))

def menu():
    print("MENU")
    userInp = input("\n f - Do Part (1) of the Lab assignment" +
                    "\n a - Add a player" +
                    "\n d - Remove a player" +
                    "\n u - Update player rating" +
                    "\n r - Output players above a rating" +
                    "\n o - Output roster in order of rating" +
                    "\n q - Quit" +
                    "\n Choose an option: ")
    if userInp == 'f':
        getRating(listOfNames, playerDict)
        outputRating(listOfNames, playerDict)
        print("Done")
        menu()

    elif userInp == 'a':
        nameOfPlayer = input("What is the name of the player you want to add?")
        ratingOfPlayer = int(input("What is the rating of the player you want to add?"))
        playerDict[nameOfPlayer] = ratingOfPlayer
        print("Done")
        menu()

    elif userInp == 'd':
        nameOfPlayer = input("What is the name of the player you want to remove?")
        del playerDict[nameOfPlayer]
        print("Done")
        menu()
        
    elif userInp == 'u':

        nameOfPlayer = input("What is the name of the player, whos rating you want to update?")
        newRating = int(input("What is his or her new rating?"))
        playerDict[nameOfPlayer] = newRating
        print("Done")
        menu()
        
    elif userInp == 'r':

        ratingOfPlayer = int(input("What's the rating you want to base the output off of?"))
        for name in playerDict:
            if playerDict[name] > ratingOfPlayer:
                print(name + ", Rating: " + str(playerDict[name]))
        print("Done")
        menu()
        
    elif userInp == 'o':
        sorted_by_value = sorted(playerDict.items(), reverse=True, key=lambda kv: kv[1])
        teams_sort_by_value = dict(sorted_by_value)
        print("ROSTER")
        for name in teams_sort_by_value :
            print(name + ", Rating: " + str(playerDict[name]))
        print("Done")
        menu()
        
    elif userInp == 'q':

        print("Goodbye")
        sys.exit()

    else:

        print("Wrong input, let's try this again.")
        menu()


menu()

'''
OUTPUT for PART 1:

MENU

 f - Do Part (1) of the Lab assignment
 a - Add a player
 d - Remove a player
 u - Update player rating
 r - Output players above a rating
 o - Output roster in order of rating
 q - Quit
 Choose an option: f
Enter John's rating: 5
Enter Tam's rating: 4
Enter Ken's rating: 3
Enter Jesse's rating: 6
ROSTER
Jesse, Rating: 6
John, Rating: 5
Ken, Rating: 3
Tam, Rating: 4


OUTPUT for A:
MENU

 f - Do Part (1) of the Lab assignment
 a - Add a player
 d - Remove a player
 u - Update player rating
 r - Output players above a rating
 o - Output roster in order of rating
 q - Quit
 Choose an option: a
What is the name of the player you want to add?Matthew
What is the rating of the player you want to add?7
Done
MENU

 f - Do Part (1) of the Lab assignment
 a - Add a player
 d - Remove a player
 u - Update player rating
 r - Output players above a rating
 o - Output roster in order of rating
 q - Quit
 Choose an option: o
ROSTER
Matthew, Rating: 7
Done



OUTPUT for D:
MENU

 f - Do Part (1) of the Lab assignment
 a - Add a player
 d - Remove a player
 u - Update player rating
 r - Output players above a rating
 o - Output roster in order of rating
 q - Quit
 Choose an option: d
What is the name of the player you want to remove?Jesse
Done
MENU

 f - Do Part (1) of the Lab assignment
 a - Add a player
 d - Remove a player
 u - Update player rating
 r - Output players above a rating
 o - Output roster in order of rating
 q - Quit
 Choose an option: o
ROSTER
John, Rating: 5
Tam, Rating: 4
Ken, Rating: 3
Done



OUTPUT for U:
MENU

 f - Do Part (1) of the Lab assignment
 a - Add a player
 d - Remove a player
 u - Update player rating
 r - Output players above a rating
 o - Output roster in order of rating
 q - Quit
 Choose an option: u
What is the name of the player, whos rating you want to update?Jesse
What is his or her new rating?7
Done
MENU

 f - Do Part (1) of the Lab assignment
 a - Add a player
 d - Remove a player
 u - Update player rating
 r - Output players above a rating
 o - Output roster in order of rating
 q - Quit
 Choose an option: o
ROSTER
Jesse, Rating: 7
John, Rating: 5
Tam, Rating: 4
Ken, Rating: 3
Done



OUTPUT for R:
MENU

 f - Do Part (1) of the Lab assignment
 a - Add a player
 d - Remove a player
 u - Update player rating
 r - Output players above a rating
 o - Output roster in order of rating
 q - Quit
 Choose an option: f
Enter John's rating: 5
Enter Tam's rating: 4
Enter Ken's rating: 3
Enter Jesse's rating: 2
ROSTER
Jesse, Rating: 2
John, Rating: 5
Ken, Rating: 3
Tam, Rating: 4
Done
MENU

 f - Do Part (1) of the Lab assignment
 a - Add a player
 d - Remove a player
 u - Update player rating
 r - Output players above a rating
 o - Output roster in order of rating
 q - Quit
 Choose an option: r
What's the rating you want to base the output off of?3
John, Rating: 5
Tam, Rating: 4
Done




OUTPUT for O:
MENU

 f - Do Part (1) of the Lab assignment
 a - Add a player
 d - Remove a player
 u - Update player rating
 r - Output players above a rating
 o - Output roster in order of rating
 q - Quit
 Choose an option: f
Enter John's rating: 5
Enter Tam's rating: 4
Enter Ken's rating: 3
Enter Jesse's rating: 2
ROSTER
Jesse, Rating: 2
John, Rating: 5
Ken, Rating: 3
Tam, Rating: 4
Done
MENU

 f - Do Part (1) of the Lab assignment
 a - Add a player
 d - Remove a player
 u - Update player rating
 r - Output players above a rating
 o - Output roster in order of rating
 q - Quit
 Choose an option: o
ROSTER
John, Rating: 5
Tam, Rating: 4
Ken, Rating: 3
Jesse, Rating: 2
Done



'''



                             
