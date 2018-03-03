# Google Code Jam 
# RevengePancakes.py
# Created by Mauro J. Pappaterra on 03 of March 2018.
from pathlib import Path

X = '+'
O = '-'

def pancakeRevenge (stack):
    # FOR TESTING PURPOSES
    #print ("Original pancake stack:\n" + stack)
    y = 0
    while (not ready(stack)):
        i = 0

        while (stack[i] == X and not (i == len(stack))):
            i += 1

        if (i == 0):
            while (stack[i] == O and not (i == len(stack))):
                i+= 1

        # FOR TESTING PURPOSES
        #print ("After flippin' the top " + str(i) + " pancake(s):")
        stack = lift_n_flip(stack,i)
        y += 1

    return str(y)

def lift_n_flip(stack, i):

    flipped_stack = ""

    for pancake in stack [0:i]:
        flipped_stack += flip(pancake)

    flipped_stack = flipped_stack[::-1] + stack[i:]
    # FOR TESTING PURPOSES
    #print(flipped_stack)
    return flipped_stack

def flip (char):
    "Toggles X to O and O to X"
    if (char == O):
        return X
    elif (char == X):
        return O

def ready (stack):
    for pancake in stack:
        if (pancake == O):
            return False
    return True

# PATH TO EXAMPLES, HARDCODED
#path = "Input\Revenge Pancakes\B-small-practice.in"
path = "Input\Revenge Pancakes\B-large-practice.in"

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
path = path.replace("Input","Output")
output = open(path, "+w")
for i, sample in enumerate (samples):
    #print("Case #" + str(i + 1) + ": " + pancakeRevenge(sample))
    output.write("Case #" + str(i + 1) + ": " + pancakeRevenge(sample) + "\n") # OR saved to external file
output.close()

# FOR TESTING PURPOSES
#print(pancakeRevenge("+-++-+--+-"))
