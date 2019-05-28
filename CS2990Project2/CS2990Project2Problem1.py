

def get_num_characters(stringInput): #Get number of chars in string
    countLetters = 0
    for each in stringInput:
        countLetters += 1
    return countLetters

def output_without_whitespace(stringInput): #replaces all whitespaces of string with nothing
    newString = stringInput.replace(" ", "")
    newString = newString.replace("\t", "")
    return newString

def textAnalyzerMenu():
    stringInput = input("Welcome to the Text Analyzer and Modifier program.\n Please type in the sentence of your choice: ")
    print("The string you entered was: ", stringInput)
    print("Number of characters: ", get_num_characters(stringInput))
    print("String with no whitespace: ", output_without_whitespace(stringInput))


textAnalyzerMenu()


'''
****************
PROBLEM 1 OUTPUT
****************

Welcome to the Text Analyzer and Modifier program.
 Please type in the sentence of your choice: The only thing we have to fear is fear itself.
The string you entered was:  The only thing we have to fear is fear itself.
Number of characters:  46
String with no whitespace:  Theonlythingwehavetofearisfearitself.


Welcome to the Text Analyzer and Modifier program.
 Please type in the sentence of your choice: This is a text string
The string you entered was:  This is a text string
Number of characters:  21
String with no whitespace:  Thisisatextstring



Welcome to the Text Analyzer and Modifier program.
 Please type in the sentence of your choice: This is example with     multiple spaces
The string you entered was:  This is example with     multiple spaces
Number of characters:  40
String with no whitespace:  Thisisexamplewithmultiplespaces
'''
