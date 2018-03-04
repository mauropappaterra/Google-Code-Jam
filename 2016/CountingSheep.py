# Google Code Jam 
# CountingSheep.py
# Created by Mauro J. Pappaterra on 04 of March 2018.
from pathlib import Path
def countingSheep(n):
    seen_digits = [False,False,False,False,False,False,False,False,False,False] # 0 to 9
    n = int(n)
    i = 1

    if (n == 0):
        return "INSOMNIA"

    while (not sleep_time(seen_digits)):
        seen_digits = check_number(n * i, seen_digits)
        #print(seen_digits)
        i += 1

    return str(n * (i - 1))

def check_number (n, seen_digits):
    number = list(str(n))
    # FOR TESTING PURPOSES
    #print (number)

    for digit in number:
        d = int(digit)
        seen_digits[d] = True

    return seen_digits

def sleep_time (seen_digits):
    if (False in seen_digits):
        return False
    else:
        return True

# PATH TO EXAMPLES, HARDCODED
#path = "Input\Counting Sheep\A-small-practice.in"
path = "Input\Counting Sheep\A-large-practice.in"

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
    print("Case #" + str(i + 1) + ": " + countingSheep(sample))
    #output.write("Case #" + str(i + 1) + ": " + countingSheep(sample) + "\n")
#output.close()

# FOR TESTING PURPOSES
#print(countingSheep("1234567890"))
#print(countingSheep("1234"))
#print(countingSheep("199"))
#print(countingSheep("0"))