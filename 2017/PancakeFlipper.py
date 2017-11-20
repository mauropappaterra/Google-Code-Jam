# Google Code Jam 
# PancakeFlipper.py
# Created by Mauro J. Pappaterra & Hassan Odimi on 29 of September 2017.
from pathlib import Path

X = '+'
O = '-'

def pancakeFlipper(row, k):
    """Receives a row of pancakes as a string and a number of simultaneous flips k
    returns a string with the number of flips to have all pancakes smiley
    side up or a message if there is on solution
    e.g. '---+-++-' 3 => 3
    e.g. '+++++' 4 => 0
    e.g. '-+-+-' 4 => IMPOSSIBLE"""
    length = len (row)
    endList = length - k
    flips = 0
    impossible = False

    #FOR TESTING ONLY
    #print("number of flips: " + str(flips))
    #print(row)

    for index, x in enumerate (row):
        if ((x != X) and (endList - index >= 0)):
            aux = 0

            while (aux < k): # flips k pancakes to the right
                row[index + aux] = flip(row[index + aux])
                aux +=1

            flips += 1
            #FOR TESTING ONLY
            #print("number of flips: " + str(flips))
            #print(row)

        elif ((x != X) and (endList - index < 0) and (endList > 1)): # negative index for out of bounds
            aux = 0

            while (aux < k):  # flips k pancakes to the left
                row[index - aux] = flip(row[index - aux])
                aux += 1

            flips += 1
            #FOR TESTING ONLY
            #print("number of flips: " + str(flips))
            #print(row)

        else:
            if (x != X):
                impossible = True

    for x in row:
        if (x != X):
            impossible = True

    if (not impossible):
        return str(flips)
    else:
        return "IMPOSSIBLE"


def flip (char):
    "Toggles X to O and O to X"
    if (char == O):
        return X
    elif (char == X):
        return O

def returnDictionary (string):
    """Takes a string from the assignment sample, returns a dictionary containing
    row and number of flips (k) for each sample
    e.g. '+--+++-+- 3' => {'row':'+--+++-+-','k':3}"""
    auxList = string.split()
    k = int(auxList[1])
    row = list(auxList[0])
    return {'row': row, 'k': k}

# PATH TO EXAMPLES, HARDCODED
path = "Input\Pancake Flipper\A-large-practice.in"
#path = "Input\Pancake Flipper\A-small-practice.in"

# ASK USER TO ENTER PATH TO EXAMPLE FILE ON THE COMMAND LINE
#path = input("Enter path to file containing examples: ")
#path = Path (path)
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

#ENUMERATES ALL SAMPLES (-1 for real index)
#for i, sample in enumerate (samples):
#      print("Case #" + str(i + 1) + ":" + str(returnDictionary(samples[i])))

for i, sample in enumerate (samples):
    print("Case #" + str(i + 1) + ": " + pancakeFlipper(** returnDictionary(samples[i])))

#FOR TESTING ONLY
#test = 62
#print(samples[test])
#print(pancakeFlipper(** returnDictionary(samples[test])))

#FOR TESTING ONLY
#sample1 = {'row':['-','-','-','x','-','x','x','-'], 'k': 3} # ---+-++-
#sample2 = {'row':['x','x','x','x','x'], 'k': 4} # +++++
#sample3 = {'row':['-','x','-','x','-'], 'k': 4} # -+-+-