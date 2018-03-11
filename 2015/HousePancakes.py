# Google Code Jam 
# HousePancakes.py
# Created by Mauro J. Pappaterra on 10 of March 2018.
from pathlib import Path

def housePancakes (diners):
    diners = diners.replace('\n','').split(' ')

    D = int(diners[0])
    layout = [int(number) for number in diners[1:]]
    timers = [max(layout)]

    # FOR TESTING PURPOSES
    #print(diners)
    #print("\nD: " + str(D))
    #print("Layout: " + str(layout) + "\n")

    minutes = 0 # calculate elapsed time

    # FOR TESTING PURPOSES
    #print("current layout: " + str(layout))
    #print("updated timers: " + str(timers))

    while (not checkFinish(layout)):

        if (max(layout) > 3):
            minutes += 1
            index = returnMaxIndex(layout, max(layout))

            check_even = layout[index] % 2
            stack = int(layout[index] / 2)

            if (check_even == 0): # check if pair
                layout[index] = stack
            else: # for odd numbers
                layout[index] = stack + 1

            layout.append(stack)
            timers.append(max(layout) + minutes) # calculate total time, save in list (array)

        # FOR TESTING PURPOSES
        #print("current layout: " + str(layout))
        #print("updated timers: " + str(timers))

    return str(min(timers))

def returnMaxIndex(layout, maxi):
    for index,plate in enumerate(layout):
        if (plate == maxi):
            return index
    return -1

def checkFinish (layout):
    for plate in layout:
        if (plate > 3):
            return False
    return True


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

no_samples = int(samples[0]) # save the first line of the file containing the number of samples
del samples[0] # deletes the first line of the file, leaving only the samples

formatted_samples = [''] * no_samples
i,j = 0,0

while (j < no_samples):
    #FOR TESTING PURPOSES
    #print ("Case #" + str(j + 1) + ": " + samples[i][:-1] + " " + samples[i+1])
    formatted_samples[j] = samples[i][:-1] + " " + samples[i+1]
    i+=2
    j+=1

# PRINT OUTPUT OR SAVE TO EXTERNAL FILE
#path = path.replace("Input","Output")
#output = open(path, "+w")
for i, sample in enumerate (formatted_samples):
    print("Case #" + str(i + 1) + ": " + housePancakes(sample))
    #output.write("Case #" + str(i + 1) + ": " + housePancakes(sample) + "\n")
#output.close()

# FOR TESTING PURPOSES
#print (housePancakes("2 6 6"))
#print (housePancakes("1 20"))
#print (housePancakes("4 4 4 4 4"))