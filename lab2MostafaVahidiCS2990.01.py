'''
Author: Mostafa Vahidi
Lab 2 CS2990.01
Prof. Lan Yang
9/4/18
'''
import math
try:
    weightPounds = float(input("Please put in your weight in pounds: "))
    heightInches = float(input("Please put in your height in inches: "))
except ValueError:
    print("One of the values you input is not a valid floating number. Only type a number.")
    exit(0)
if (weightPounds > 0 and heightInches > 0):
    bmi = float((weightPounds/math.sqrt(heightInches)**2) * 703)
    print("""Your weight is %f pounds, your height is %f inches, \n
             Your bmi is %f. Thank you for using this program!""" %(weightPounds, heightInches, bmi))
else:
    print("""Sorry but either your weight or height was 0 or below. Or, you did not enter proper numbers. \n
            Thus, you can't calculate your bmi. Sorry for the inconvenience. \n
            Please try again.""")
     
'''
OUTPUT OF PROGRAM

NORMAL TEST CASES:

Test Case: Weight: 102 lbs, height: 56 inches
======= RESTART: C:/Users/mosta/Desktop/lab2MostafaVahidiCS2990.01.py =======
Please put in your weight in pounds102
Please put in your height in inches56
Your weight is 102.000000 pounds, your height is 56.000000 inches, 

             Your bmi is 1280.464286. Thank you for using this program!

Test Case: Weight: 160.5 lbs, height: 71 inches
======= RESTART: C:/Users/mosta/Desktop/lab2MostafaVahidiCS2990.01.py =======
Please put in your weight in pounds: 160.5
Please put in your height in inches: 71
Your weight is 160.500000 pounds, your height is 71.000000 inches, 

             Your bmi is 1589.176056. Thank you for using this program!


Test Case: Weight: 250 lbs, height: 67.5 inches
======= RESTART: C:/Users/mosta/Desktop/lab2MostafaVahidiCS2990.01.py =======
Please put in your weight in pounds: 250
Please put in your height in inches: 67.5
Your weight is 250.000000 pounds, your height is 67.500000 inches, 

             Your bmi is 2603.703704. Thank you for using this program!

Test Case: My choice of data: Weight: 300 lbs, height: 20 inches
======= RESTART: C:/Users/mosta/Desktop/lab2MostafaVahidiCS2990.01.py =======
Please put in your weight in pounds: 300
Please put in your height in inches: 20
Your weight is 300.000000 pounds, your height is 20.000000 inches, 

             Your bmi is 10545.000000. Thank you for using this program!


SPECIAL TEST CASES:

Test Case: Weight: 0 lbs, height: 50 inches
======= RESTART: C:/Users/mosta/Desktop/lab2MostafaVahidiCS2990.01.py =======
Please put in your weight in pounds: 0
Please put in your height in inches: 50
Sorry but either your weight or height was 0 or below. Or, you did not enter proper numbers. 

            Thus, you can't calculate your bmi. Sorry for the inconvenience. 

            Please try again.


Test Case: Weight: 200 lbs, height: 0 inches
======= RESTART: C:/Users/mosta/Desktop/lab2MostafaVahidiCS2990.01.py =======
Please put in your weight in pounds: 200
Please put in your height in inches: 0
Sorry but either your weight or height was 0 or below. Or, you did not enter proper numbers. 

            Thus, you can't calculate your bmi. Sorry for the inconvenience. 

            Please try again.


Test Case: Weight: 0 lbs, height: 0 inches
======= RESTART: C:/Users/mosta/Desktop/lab2MostafaVahidiCS2990.01.py =======
Please put in your weight in pounds: 0
Please put in your height in inches: 0
Sorry but either your weight or height was 0 or below. Or, you did not enter proper numbers. 

            Thus, you can't calculate your bmi. Sorry for the inconvenience. 

            Please try again.


Test Case: Weight: -50 lbs, height: 50 inches
======= RESTART: C:/Users/mosta/Desktop/lab2MostafaVahidiCS2990.01.py =======
Please put in your weight in pounds: -50
Please put in your height in inches: 50
Sorry but either your weight or height was 0 or below. Or, you did not enter proper numbers. 

            Thus, you can't calculate your bmi. Sorry for the inconvenience. 

            Please try again.


Test Case: Weight: "56 lbs" String, height: 46 inches
======= RESTART: C:/Users/mosta/Desktop/lab2MostafaVahidiCS2990.01.py =======
Please put in your weight in pounds: 56 lbs
One of the values you input is not a valid floating number. Only type a number.



'''


