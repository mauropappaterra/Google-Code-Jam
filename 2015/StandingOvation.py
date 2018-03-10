# Google Code Jam 
# StandingOvation.py
# Created by Mauro J. Pappaterra on 10 of March 2018.
from pathlib import Path

def standingOvation (audience):
    audience = audience.split(' ')

    max_shy = int(audience[0])
    k = list(audience[1][:-1])

    #FOR TESTING PURPOSES
    #print ("Max Shyness: " + str(max_shy))
    #print(k)
    #print ("K: " +"".join(k))

    total_standing = 0
    total_friends = 0

    for index,people in enumerate (k):
        #FOR TESTING PURPOSES
        #print ("\nshyness level " + str(index) + ": " + people + " people")

        if (index == 0 or int(people) == 0):
            total_standing += int(people)
        else:
            if (index <= total_standing):
                total_standing += int(people)
            else:
                friends = 0
                while ((total_standing + friends) < index):
                    friends += 1

                total_standing += int(people) + friends
                total_friends += friends

        #FOR TESTING PURPOSES
        #print("total friends needed: " + str(total_friends))
        #print("total people standing: " + str(total_standing))

    return str(total_friends)

#PATH TO EXAMPLES, HARDCODED
#path = "Input\Standing Ovation\A-small-practice.in"
path = "Input\Standing Ovation\A-large-practice.in"

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
    print("Case #" + str(i + 1) + ": " + standingOvation(samples[i]))
    #output.write("Case #" + str(i + 1) + ": " + standingOvation(samples[i]) + "\n")
#output.close()

#FOR TESTING PURPOSES
#print(standingOvation("6 0080104"))
