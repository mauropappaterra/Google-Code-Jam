# Google Code Jam 
# HousePancakes.py
# Created by Mauro J. Pappaterra on 10 of March 2018.
from pathlib import Path

def housePancakes (sample):

    return sample

#PATH TO EXAMPLES, HARDCODED
path = "Input\House Pancakes\B-small-practice.in"
#path = "Input\House Pancakes\B-large-practice.in"

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

# PRINT OUTPUT OR SAVE TO EXTERNAL FILE
#path = path.replace("Input","Output")
#output = open(path, "+w")
for i, sample in enumerate (samples):
    print("Case #" + str(i + 1) + ": " + housePancakes(samples[i]))
    #output.write("Case #" + str(i + 1) + ": " + housePancakes(samples[i]) + "\n")
#output.close()