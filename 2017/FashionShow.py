# Google Code Jam 
# FashionShow.py
# Created by Mauro J. Pappaterra on 20 of November 2017.
from pathlib import Path

#PATH TO EXAMPLES, HARDCODED
path = "Input\Bathroom Stalls\D-small-practice.in"
#path = "Input\Bathroom Stalls\D-large-practice.in"

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

for i, sample in enumerate (samples):
    print("Case #" + str(i + 1) + ": " + tidyNumbers(samples[i]))