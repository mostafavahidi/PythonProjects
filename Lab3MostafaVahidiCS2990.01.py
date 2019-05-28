'''
Author: Mostafa Vahidi
CS2990.01 Prof. Yang
Lab 3     9/5/18
'''

totalCost = 0

def one():
    global totalCost
    totalCost += 35
    print ("Service 1: Oil Change, $35")
def two():
    global totalCost
    totalCost += 19
    print("Service 2: Tire Rotation, $19")

def three():
    global totalCost
    totalCost += 7
    print("Service 3: Car Wash, $7")

def four():
    global totalCost
    totalCost += 12
    print("Serbice 4: Car Wax, $12")

def noChoice():
    print("No Service")

def switch_choice(firstChoice):
    switcher = {
            '1': one,
            '2': two,
            '3': three,
            '4': four,
            '-': noChoice
        }
    #Get the function from switcher dictionary
    func = switcher.get(firstChoice, lambda:"Invalid argument")
    #Execute the function
    func()

def switch_choice(secondChoice):
    switcher = {
            '1': one,
            '2': two,
            '3': three,
            '4': four,
            '-': noChoice
        }
    #Get the function from switcher dictionary
    func = switcher.get(secondChoice, lambda:"Invalid argument")
    #Execute the function
    func()

print("""Mostafa's auto shop services
        (1) Oil Change -- $35
        (2) Tire Rotation -- $19
        (3) Car Wash -- $7
        (4) Car Wax -- $12
        (-) No service
    """)

firstChoice = input("Please input the number of your first service choice.")
secondChoice = input("Please input the number of your second service choice.")


print("Mostafa's auto shop invoice")

switch_choice(firstChoice)
switch_choice(secondChoice)



print("Total: %d" %(totalCost))

'''
PROGRAM OUTPUT:
======= RESTART: C:/Users/mosta/Desktop/Lab3MostafaVahidiCS2990.01.py =======
Mostafa's auto shop services
        (1) Oil Change -- $35
        (2) Tire Rotation -- $19
        (3) Car Wash -- $7
        (4) Car Wax -- $12
        (-) No service
    
Please input the number of your first service choice.2
Please input the number of your second service choice.-
Mostafa's auto shop invoice
Service 2: Tire Rotation, $19
No Service
Total: 19


OUTPUT #2:
======= RESTART: C:/Users/mosta/Desktop/Lab3MostafaVahidiCS2990.01.py =======
Mostafa's auto shop services
        (1) Oil Change -- $35
        (2) Tire Rotation -- $19
        (3) Car Wash -- $7
        (4) Car Wax -- $12
        (-) No service
    
Please input the number of your first service choice.3
Please input the number of your second service choice.2
Mostafa's auto shop invoice
Service 3: Car Wash, $7
Service 2: Tire Rotation, $19
Total: 26
    
'''
