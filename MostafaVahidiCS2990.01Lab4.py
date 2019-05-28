'''
Author: Mostafa Vahidi
CS2990.01 Prof. Yang
9/12/18 Lab 4
'''
import re
p = re.compile('Regex expression')

def handleExit():
    print('''Do you want to terminate the program or keep on trying to make a new password?
            [1] Terminate
            [2] Keep on trying!''')
    userChoice = input("Type the number of your menu choice: ")
    if userChoice == '1':
        print("Thanks for using this program")
        system.exit(0)
    elif userChoice == '2':
        print("Let's try this again: ")
        getPass(1)
    else:
        handleExit()

        
def confirmPass(password):
    toConfirm = input("Please confirm the password you just chose: ")
    numOfTries = 1
    
    while toConfirm != password:
        print("The password you entered does not match the original password created.")
        if numOfTries >= 3:
            print("Sorry you ran out of tries")
            handleExit()
        else:
            numOfTries += 1
            toConfirm = input("Please confirm the password you just chose again: ")

    print("Password has been confirmed successfully!")


def getPass(numOfTries):
    password = input("Enter string to test: ")
    numOfTries = numOfTries
    
    #Matching the password with the regex expression that includes all of the criteria mentioned in part 5 (optional)
    if re.match('^(?=.{8,50}$)(?=(.*?[a-z].*?[A-Z])|(.*?[a-z].*?[0-9])|(.*?[a-z].*?[!@#$%^&*()_+])|(.*?[A-Z].*?[0-9])|(.*?[A-Z].*?[!@#$%^&*()_+])|(.*?[0-9].*?[!@#$%^&*()_+])).*$', password) and numOfTries <= 5:
        # match
        confirmPass(password)
    elif numOfTries >= 5:
        print("You ran out of tries for your password")
        handleExit() 
    else:
        # no match
        print("You did not meet the criteria for the password")
        newNumOfTries = numOfTries + 1
        getPass(newNumOfTries)


getPass(1)

'''
OUTPUT:
1)
======= RESTART: C:/Users/mosta/Desktop/MostafaVahidiCS2990.01Lab4.py =======
Enter string to test: cal
You did not meet the criteria for the password
Enter string to test: cal
You did not meet the criteria for the password
Enter string to test: cal
You did not meet the criteria for the password
Enter string to test: cal
You did not meet the criteria for the password
Enter string to test: cal
You ran out of tries for your password
Do you want to terminate the program or keep on trying to make a new password?
            [1] Terminate
            [2] Keep on trying!
Type the number of your menu choice: 1
Thanks for using this program

2)
======= RESTART: C:/Users/mosta/Desktop/MostafaVahidiCS2990.01Lab4.py =======
Enter string to test: calPolyPomona
Please confirm the password you just chose: Calpolypomona
The password you entered does not match the original password created.
Please confirm the password you just chose again: CalpolyPomona
The password you entered does not match the original password created.
Please confirm the password you just chose again: cppPomona
The password you entered does not match the original password created.
Sorry you ran out of tries
Do you want to terminate the program or keep on trying to make a new password?
            [1] Terminate
            [2] Keep on trying!
Type the number of your menu choice: 1
Thanks for using this program

3)
======= RESTART: C:/Users/mosta/Desktop/MostafaVahidiCS2990.01Lab4.py =======
Enter string to test: calPolyPomona
Please confirm the password you just chose: calpoly
The password you entered does not match the original password created.
Please confirm the password you just chose again: calPolyPomona
Password has been confirmed successfully!

4)
======= RESTART: C:/Users/mosta/Desktop/MostafaVahidiCS2990.01Lab4.py =======
Enter string to test: CalPolyPomona1$
Please confirm the password you just chose: CalpolyPomona1$
The password you entered does not match the original password created.
Please confirm the password you just chose again: CalPolyPomona1$
Password has been confirmed successfully!

5)
======= RESTART: C:/Users/mosta/Desktop/MostafaVahidiCS2990.01Lab4.py =======
Enter string to test: CalPoly&67
Please confirm the password you just chose: CalPoly$67
The password you entered does not match the original password created.
Please confirm the password you just chose again: 67&CalPoly
The password you entered does not match the original password created.
Please confirm the password you just chose again: PahulyCauhl
The password you entered does not match the original password created.
Sorry you ran out of tries
Do you want to terminate the program or keep on trying to make a new password?
            [1] Terminate
            [2] Keep on trying!
Type the number of your menu choice: 2
Let's try this again: 
Enter string to test: CalPolyPass
Please confirm the password you just chose: CalPolyPass
Password has been confirmed successfully!


'''
        
