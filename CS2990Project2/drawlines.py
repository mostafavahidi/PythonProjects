import turtle

t = turtle
t.pensize(2)
t.hideturtle()
t.left(90)
t.speed('fastest')
    
def long():   #draw an upward long line
    t.fd(14)
    t.up()
    t.bk(14)
    t.right(90)
    t.fd(6)
    t.left(90)
    t.down()
    
def short():  #draw an upward short line
    t.fd(6)
    t.up()
    t.bk(6)
    t.right(90)
    t.fd(6)
    t.left(90)
    t.down()

def print_start_stop():
    long()
def print_zero():
    long()
    long()
    short()
    short()
    short()
def print_one():
    short()
    short()
    short()
    long()
    long()
def print_two():
    short()
    short()
    long()
    short()
    long()
def print_three():
    short()
    short()
    long()
    long()
    short()
def print_four():
    short()
    long()
    short()
    short()
    long()
def print_five():
    short()
    long()
    short()
    long()
    short()
def print_six():
    short()
    long()
    long()
    short()
    short()
def print_seven():
    long()
    short()
    short()
    short()
    long()
def print_eight():
    long()
    short()
    short()
    long()
    short()
def print_nine():
    long()
    short()
    long()
    short()
    short()

def replaceZip(stringInput):
    stringToReturn = stringInput.replace("-", "")
    return stringToReturn

def generateCheckSum(stringInput):
    listOfNums = []
    for each in stringInput:
        listOfNums.append(int(each))

    sum = 0
    for each in listOfNums:
        sum += each

    sumModTen = sum % 10
    checkSumNum = 10 - sumModTen
    return checkSumNum

def generateFinalList(stringInput, numSum):
    listOfNums = []
    for each in stringInput:
        listOfNums.append(int(each))
    listOfNums.append(numSum)
    print(listOfNums)
    return listOfNums

def printBarCode(listOfNums):
    print_start_stop()
    for each in listOfNums:
        if each == 0: print_zero()
        elif each == 1: print_one()
        elif each == 2: print_two()
        elif each == 3: print_three()
        elif each == 4: print_four()
        elif each == 5: print_five()
        elif each == 6: print_six()
        elif each == 7: print_seven()
        elif each == 8: print_eight()
        elif each == 9: print_nine()
    print_start_stop()

    
def postalBarCodeMenu():
    print("Welcome to the US Postal Bar Code Visualizer Program.")
    print("Please put in your desired US Postal Code in the following format.\n",
                        "XXXXX-XXXX i.e.: 90025-1237 \n")
    stringInput = input("Type zipcode here: ")
    stringWithoutDash = replaceZip(stringInput)
    printBarCode(generateFinalList(stringWithoutDash, generateCheckSum(stringWithoutDash)))
                 



t.up()
t.goto(0, -50)
t.down()


postalBarCodeMenu()




 
