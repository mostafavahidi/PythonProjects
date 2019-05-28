'''
Author: Mostafa Vahidi
Project 1 CS2990.01
Prof. Lan Yang
9/10/18
'''
import math

#Handling the bmi message outputs for the user
def handleBMIMessage(bmi):
    if (bmi < 19):
        print("Your BMI is too low!!!")
    elif (bmi >= 19 and bmi <= 24):
        print("Your BMI shows that you are Normal!!!")
    elif (bmi >= 25 and bmi <= 29):
        print("Your BMI shows that you are Overweight!!!")
    elif (bmi >= 30 and bmi <= 39):
        print("Your BMI shows that you are Obese!!!")
    elif (bmi >= 40 and bmi <= 54):
        print("Your BMI shows that you are Extremely Obese!!!")
    else:
        print("Your BMI is abnormally large")

#Handling the american calculations for the bmi         
def american():
    try:
        weightPounds = int(input("Please put in your weight in pounds: "))
        heightInches = int(input("Please put in your height in inches: "))
    except ValueError:
        print("One of the values you input is not a valid floating number. Only type a number.")
        exit(0)
    if (weightPounds > 0 and heightInches > 0):
        bmi = int((weightPounds/(heightInches**2)) * 703)
        print("""Your weight is %d pounds, your height is %d inches, \n
             Your bmi is %d. Thank you for using this program!""" %(weightPounds, heightInches, bmi))
        handleBMIMessage(bmi)
    else:
        print("""Sorry but either your weight or height was 0 or below. Or, you did not enter proper numbers. \n
            Thus, you can't calculate your bmi. Sorry for the inconvenience. \n
            Please try again.""")

#handling the metric calculations for the bmi
def metric():
    try:
        weightKilograms = int(input("Please put in your weight in kilograms: "))
        heightMeters = float(input("Please put in your height in meters: "))
    except ValueError:
        print("One of the values you input is not a valid floating number. Only type a number.")
        exit(0)
    if (weightKilograms > 0 and heightMeters > 0):
        bmi = int(weightKilograms/(heightMeters**2))
        print("""Your weight is %d kilograms, your height is %f meters, \n
             Your bmi is %d. Thank you for using this program!""" %(weightKilograms, heightMeters, bmi))
        handleBMIMessage(bmi)
    else:
        print("""Sorry but either your weight or height was 0 or below. Or, you did not enter proper numbers. \n
            Thus, you can't calculate your bmi. Sorry for the inconvenience. \n
            Please try again.""")

#Handling the choices for the user input
def switch_choice(choice):
    switcher = {
            '1': american,
            '2': metric
        }
    #Get the function from switcher dictionary
    func = switcher.get(choice, lambda:"Invalid argument")
    #Execute the function
    func()


#initializing the menu for the program
def menu():
    print('''Welcome to Project 1 program. In this program, you can
            choose from calculating your BMI based on the American system
            or Metric system.''')

    while True:
        try:
            choice = input('''Please type a number from the options below:
                                    [1] American
                                    [2] Metric
                                    : ''')
            break
        except:
            print("That's not a valid option!")

    if choice == '1':
        return switch_choice(choice)
    elif choice == '2':
        return switch_choice(choice)
    else:
        print("That's not an option! Program will end now")
        exit(0)

menu() 
'''
OUTPUT OF PROGRAM

NORMAL TEST CASES:
Welcome to Project 1 program. In this program, you can
            choose from calculating your BMI based on the American system
            or Metric system.
Please type a number from the options below:
                                    [1] American
                                    [2] Metric
                                    : 1
Please put in your weight in pounds: 100
Please put in your height in inches: 62
Your weight is 100 pounds, your height is 62 inches, 

             Your bmi is 18. Thank you for using this program!
Your BMI is too low!!!


Welcome to Project 1 program. In this program, you can
            choose from calculating your BMI based on the American system
            or Metric system.
Please type a number from the options below:
                                    [1] American
                                    [2] Metric
                                    : 1
Please put in your weight in pounds: 147
Please put in your height in inches: 62
Your weight is 147 pounds, your height is 62 inches, 

             Your bmi is 26. Thank you for using this program!
Your BMI shows that you are Overweight!!!


Welcome to Project 1 program. In this program, you can
            choose from calculating your BMI based on the American system
            or Metric system.
Please type a number from the options below:
                                    [1] American
                                    [2] Metric
                                    : 2
Please put in your weight in kilograms: 50
Please put in your height in meters: 1.2
Your weight is 50 kilograms, your height is 1.200000 meters, 

             Your bmi is 34. Thank you for using this program!
Your BMI shows that you are Obese!!!

Welcome to Project 1 program. In this program, you can
            choose from calculating your BMI based on the American system
            or Metric system.
Please type a number from the options below:
                                    [1] American
                                    [2] Metric
                                    : 2
Please put in your weight in kilograms: 60
Please put in your height in meters: 1
Your weight is 60 kilograms, your height is 1.000000 meters, 

             Your bmi is 60. Thank you for using this program!
Your BMI is abnormally large

Welcome to Project 1 program. In this program, you can
            choose from calculating your BMI based on the American system
            or Metric system.
Please type a number from the options below:
                                    [1] American
                                    [2] Metric
                                    : 1
Please put in your weight in pounds: 250
Please put in your height in inches: 63
Your weight is 250 pounds, your height is 63 inches, 

             Your bmi is 44. Thank you for using this program!
Your BMI shows that you are Extremely Obese!!!

SPECIAL TEST CASES:

Welcome to Project 1 program. In this program, you can
            choose from calculating your BMI based on the American system
            or Metric system.
Please type a number from the options below:
                                    [1] American
                                    [2] Metric
                                    : non number
That's not an option! Program will end now



Welcome to Project 1 program. In this program, you can
            choose from calculating your BMI based on the American system
            or Metric system.
Please type a number from the options below:
                                    [1] American
                                    [2] Metric
                                    : 1
Please put in your weight in pounds: 0
Please put in your height in inches: 0
Sorry but either your weight or height was 0 or below. Or, you did not enter proper numbers. 

            Thus, you can't calculate your bmi. Sorry for the inconvenience. 

            Please try again.

            
Welcome to Project 1 program. In this program, you can
            choose from calculating your BMI based on the American system
            or Metric system.
Please type a number from the options below:
                                    [1] American
                                    [2] Metric
                                    : 2
Please put in your weight in kilograms: 50
Please put in your height in meters: 0
Sorry but either your weight or height was 0 or below. Or, you did not enter proper numbers. 

            Thus, you can't calculate your bmi. Sorry for the inconvenience. 

            Please try again.

'''


