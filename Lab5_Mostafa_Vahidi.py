'''
Author: Mostafa Vahidi
CS2990.01 Prof. Yang
Lab 5
9/24/18
'''
from random import *

#Problem 1
def superLotto():
    luckyNumList = []
    for i in range(5):
        luckyNumToAdd = randint(1, 47)       
        luckyNumList.append(luckyNumToAdd)

    megaNum = randint(1,27)
    print ("Your Super Lotto number is: " + ", ".join(str(x) for x in luckyNumList) + ", " + str(megaNum))
    


#Problem 2
def arrowPrint():
    baseHeight = int(input("Enter arrow base height: "))
    baseWidth = int(input("Enter arrow base width: "))
    headWidth = int(input("Enter arrow head width: "))

    for heightLine in range(baseHeight):
        print(baseWidth * "*")
    for headLine in range(headWidth):
        print((headWidth - headLine) * "*")


#Menu
def menu():
    choice = input("Welcome to Lab 5 \n Please enter your choice: \n [1]superLotto \n [2]arrowPrint \n : ")
    if choice == '1':
        superLotto()
    elif choice == '2':
        arrowPrint()
    else:
        print("Your choice was not valid. Let's try this again.")
        menu()
        
menu()


'''

OUTPUT FOR PROBLEM 1 (LOTTO NUMBER):
===== RESTART: C:/workspaceSchool/CS299.01_Python/Lab5_Mostafa_Vahidi.py =====
Welcome to Lab 5 
 Please enter your choice: 
 [1]superLotto 
 [2]arrowPrint 
 : 1
Your Super Lotto number is: 14, 17, 23, 26, 14, 13


===== RESTART: C:/workspaceSchool/CS299.01_Python/Lab5_Mostafa_Vahidi.py =====
Welcome to Lab 5 
 Please enter your choice: 
 [1]superLotto 
 [2]arrowPrint 
 : 1
Your Super Lotto number is: 9, 36, 11, 14, 27, 20

===== RESTART: C:/workspaceSchool/CS299.01_Python/Lab5_Mostafa_Vahidi.py =====
Welcome to Lab 5 
 Please enter your choice: 
 [1]superLotto 
 [2]arrowPrint 
 : 1
Your Super Lotto number is: 41, 9, 1, 13, 25, 16


OUTPUT FOR PROBLEM 2 (ARROW PRINT):
===== RESTART: C:/workspaceSchool/CS299.01_Python/Lab5_Mostafa_Vahidi.py =====
Welcome to Lab 5 
 Please enter your choice: 
 [1]superLotto 
 [2]arrowPrint 
 : 2
Enter arrow base height: 5
Enter arrow base width: 2
Enter arrow head width: 4
**
**
**
**
**
****
***
**
*


===== RESTART: C:/workspaceSchool/CS299.01_Python/Lab5_Mostafa_Vahidi.py =====
Welcome to Lab 5 
 Please enter your choice: 
 [1]superLotto 
 [2]arrowPrint 
 : 2
Enter arrow base height: 6
Enter arrow base width: 3
Enter arrow head width: 7
***
***
***
***
***
***
*******
******
*****
****
***
**
*


===== RESTART: C:/workspaceSchool/CS299.01_Python/Lab5_Mostafa_Vahidi.py =====
Welcome to Lab 5 
 Please enter your choice: 
 [1]superLotto 
 [2]arrowPrint 
 : 2
Enter arrow base height: 5
Enter arrow base width: 3
Enter arrow head width: 6
***
***
***
***
***
******
*****
****
***
**
*

'''
