# Google Code Jam 
# TidyNumbers.py
# Created by Mauro J. Pappaterra & Hassan Odimi on 30 of September 2017.

from pathlib import Path

def tidyNumbers (number):
    "Takes a number (as a string) and returns the last tidy number counted"
    'e.g. "12645" => "12599"'
    'e.g. "345" => "345"'
    listOfDigits = convertToDigitList(number)
    #FOR TESTING PURPOSES
    #print(listOfDigits)

    if (not checkTidy(listOfDigits)):  # calls findLastTidy algorithm only for untidy numbers
        lastTidy = findLastTidy(listOfDigits)
    else:
        lastTidy = listOfDigits  # returns the same number if its already tidy

    while (lastTidy[0] == 0): # this loop deletes all zeroes to the left
        del lastTidy[0]

    return convertToString(lastTidy) # returns result as a string

def findLastTidy (listOfDigits):
    "This recursive algorithm takes a number as a list of digits"
    "and returns the last tidy number as a list of digits"
    'e.g. [9,8,7,6] => [8,9,9,9]'
    noDigits = len(listOfDigits)  # number of digits
    noLoops = noDigits - 1  # number of loop iterations

    for index, digit in enumerate(listOfDigits):
        if (noLoops > 0):
            if (digit > listOfDigits[index + 1]):
                listOfDigits[index] = digit - 1;
                index += 1
                while (index < noDigits):
                    listOfDigits[index] = 9;
                    index += 1
            noLoops -= 1

    if (checkTidy(listOfDigits)):
        listOfDigits = listOfDigits
    else:
        listOfDigits = findLastTidy(listOfDigits) # recursive call

    return listOfDigits;

def convertToDigitList (numberAsString):
    "Takes a single number as a string, returns a list of integers for each digit"
    "e.g. '12345' => [1,2,3,4,5]"
    digitList = list(str(numberAsString))  # converts string into a list of char
    del digitList[-1]  # deletes last char on list that is always '\n'

    for i, digit in enumerate(digitList):
        digitList[i] = (int(digit)) # converts all digits from char to integers
    return digitList

def convertToString (digitList):
    "Takes a list of digits and returns its concatenation as a single string"
    'e.g. [1,2,3,4,5] => "12345"'
    for index, digit in enumerate(digitList):
        digitList[index] = str(digit)

    asString = "".join(digitList)
    return asString

def convertToInteger (digitList):
    "Takes a list of digits and returns its concatenation as a single integer"
    "e.g. [1,9,9,8] => 1998"
    asInteger = int(convertToString(digitList))
    return asInteger

def checkTidy (digitList):
    "Takes list of integers returns True if the numbers are 'tidy'"
    "e.g. 123456 => True"
    "e.g. 912345 => False"
    tidy = True
    noDigits = len(digitList) # number of digits
    noLoops = noDigits - 1 # number of loop iterations

    if (noDigits > 1): # all 1 digit numbers are already sorted
        for index, digit in enumerate(digitList):
            if (noLoops > 0):
             if (digit > digitList[index + 1]):
                 tidy = False
            noLoops -= 1
    return tidy

# PATH TO EXAMPLES, HARDCODED
#path = "C:\Input Files\Tidy Numbers\B-large-practice.in"
#mode = "r"

# ASK USER TO ENTER PATH TO EXAMPLE FILE ON THE COMMAND LINE
path = input("Enter path to file containing examples: ")
path = Path(path)

mode = "r"
while (not path.is_file()):
    path = input("\nERROR: NOT A VALID FILE PATH! \nEnter path to file containing examples: ")
    path = Path(path)

with open (path, mode) as reader:
    samples = (reader.readlines())
    reader.close()

no_samples = samples[0] # save the first line of the file containing the number of samples
del samples[0] # deletes the first line of the file, leaving only the samples

for i, sample in enumerate (samples):
    print("Case #" + str(i + 1) + ": " + tidyNumbers(samples[i]))