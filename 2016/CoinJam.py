# Google Code Jam 
# CoinJam.py
# Created by Mauro J. Pappaterra on 04 of March 2018.
from pathlib import Path
import math

def coinJam(nj):
    nj = nj.split(' ')

    n = int(nj[0])
    j = int(nj[1])

    # FOR TESTING PURPOSES
    #print("N: " + str(n))
    #print("J: " + str(j))

    # create the first coin
    coin = "1"
    zeros = n - 2

    while zeros > 0:
        coin += "0"
        zeros -= 1

    coin += "1"

    all_validations = "" # validation string for output

    while (j > 0):
        # FOR TESTING PURPOSES
        # print(coin)

        is_jamcoin = True
        validation_string = "\n" + coin

        base = 2
        while (base <= 10):
            validate = convert_base(coin, base) #Try a really high prime number -> 205891132153789

            if (check_composite(validate)):
                if (base != 10):
                    validation_string += " " + str(validate) # print all validations but base 10
            else:
                # FOR TESTING PURPOSES
                #print("Discarded. This coin would be a prime on base " + str(base) + " = " + str(validate))
                is_jamcoin = False
                break # immediately discard the jamcoin as soon as any prime number is found
            base += 1

        if (is_jamcoin):
            all_validations += validation_string
            j -= 1 # only decrease the counter whenever a valid jamcoin is found!

        coin = next_coin(coin)

    return all_validations


def convert_base (coin, base):
    """Takes a number as coin, interpretes its on the base given. Returns convertion to decimal on the given base"""
    number = 0
    exponent = len(coin) - 1

    for digit in coin:
        number += int(digit) * base ** exponent
        exponent -= 1
    # FOR TESTING PURPOSES
    #print (str(coin) + " interpreted as base " + str(base) + " -> would equal to " + str(number) + " in decimal")
    return number

def check_composite (number):
    """Returns True if the number is composite (or NOT prime)."""
    top = int(math.sqrt(number))
    check = 2

    while (check < top):
        if (number % check == 0):
            return True
        check += 1

    return False

def next_coin (coin):
    current_value = convert_base(coin[1:-1],2)
    coin_value = make_binary(current_value + 1) # add 1 by 1 return as binary string

    # FOR TESTING PURPOSES
    #print("Current Coin Value: " + make_binary(current_value))
    #print("Next Coin Value: " + coin_value)

    zeroes = len(coin[1:-1]) - len(coin_value)
    new_coin = "1"

    while zeroes > 0:
        new_coin += "0"
        zeroes-= 1

    new_coin += coin_value + "1"

    # FOR TESTING PURPOSES
    #print("Next Coin is: " + str(new_coin))

    return new_coin

def make_binary (decimal):
    "Converts a decimal integer into binary, returns as string"
    binary = ""

    while (decimal != 0):
        binary += str(decimal % 2)
        decimal = int(decimal / 2)

    return binary[::-1]

# PATH TO EXAMPLES, HARDCODED
#path = "Input\Coin Jam\C-small-practice.in"
path = "Input\Coin Jam\C-large-practice.in"

# ASK USER TO ENTER PATH TO EXAMPLE FILE ON THE COMMAND LINE
#path = input("Enter path to file containing examples: ")
#path = Path(path)
#
#while (not path.is_file()):
#    path = input("\nERROR: NOT A VALID FILE PATH! \nEnter path to file containing examples: ")
#    path = Path(path)

mode = "r"
with open (path, mode) as reader:
    samples = (reader.readlines())
    reader.close()

no_samples = samples[0] # save the first line of the file containing the number of samples
del samples[0] # deletes the first line of the file, leaving only the samples

# SAVE OUTPUT TO EXTERNAL FILE
#path = path.replace("Input","Output")
#output = open(path, "+w")
for i, sample in enumerate (samples): # print to console OR saved to external file
    print("Case #" + str(i + 1) + ": " + coinJam(sample))
    #output.write("Case #" + str(i + 1) + ": " + coinJam(sample) + "\n")
#output.close()

# FOR TESTING PURPOSES
#coinJam("4 10\n")
#print(make_binary(9999))