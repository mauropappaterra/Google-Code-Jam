# Google Code Jam 
# CookieClicker.py
# Created by Mauro J. Pappaterra on 13 of March 2018.
from pathlib import Path

def cookieClicker (sample):
    sample = [float(x) for x in sample.split(' ') if True]

    C = sample[0] # cost for a farm
    F = sample[1] # farm cookie production per second
    X = sample[2] # cookies needed to win

    #FOR TESTING PURPOSES
    #print("C:" + str(C) + " F:" + str(F) + " X:" + str(X))
    time = 0.0 # seconds past
    cookies = 0.0 # no. of cookies
    production = 2.0 # cookie production per second

    factories = 0

    while (True):
        time += 1
        cookies += production

        if (cookies >= C ):

            if (factory_strategy(C, F, X, cookies, production)): # check if it's worth it to buy a cookie farm
                # buy a cookie farm
                cookies -= C # deduct cookies
                production += F # update production per second
                factories += 1
            else: # calculate remaining time needed, add time and exit
                missing_cookies = X - cookies
                missing_time = missing_cookies / production

                time += missing_time
                cookies += missing_cookies
                break # exit

        if (cookies >= X):
            break

    # FOR TESTING PURPOSES
    #print("You won! Total Time " + str(time) +" Cookies: " + str(cookies) + " Factories: " + str(factories))
    return str(time)

def factory_strategy (C, F, X, cookies, production):
    "Returns True if it is worth it to buy a factory"

    costInSeconds = C/F #seconds needed to buy a farm
    timeWithoutFactory = (X-cookies) / production
    timeWithNewFactory = (X / (production + F))

    if (timeWithoutFactory < timeWithNewFactory):
        return False

    return True


#PATH TO EXAMPLES, HARDCODED
path = "Input\Cookie Clicker Alpha\B-small-practice.in"
#path = "Input\Cookie Clicker Alpha\B-large-practice.in"

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

no_samples = int(samples[0]) # save the first line of the file containing the number of samples
del samples[0] # deletes the first line of the file, leaving only the samples

# PRINT OUTPUT OR SAVE TO EXTERNAL FILE
#path = path.replace("Input","Output")
#output = open(path, "+w")
for i, sample in enumerate (samples):
    print("Case #" + str(i + 1) + ": " + cookieClicker(sample))
    #output.write("Case #" + str(i + 1) + ": " + cookieClicker(sample) + "\n")
#output.close()