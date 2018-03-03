# Google Code Jam 
# BathroomStalls.py
# Created by Mauro J. Pappaterra on 16 of November 2017.
from pathlib import Path

OCCUPIED = -1 # integer flag for occupied toilets
EMPTY = 0

def bathroomStalls (input):
    input = input.split(' ')

    n = int((input[0]))
    k = int (min (input)) # since nobody ever leaves, is always true that k <= n

    minimum = createStalls(n) # an array to keep track of formula: min (Ls,Rs) = maximal
    maximum = createStalls(n) # an array to keep track of formula: max (Ls,Rs) = maximal

    last_min = 0  # store last maximal minimum for retrieval
    last_max = 0  # store last maximal maximum for retrieval

    # FOR TESTING PURPOSES
    #print ("N = " + str(n) + "\tK = " + str(k) +"\n")
    #print (minimum)
    #print (maximum)

    while (k > 0): # repeat as long as there are people on the queue
        # FOR TESTING PURPOSES
        #print ("\nk = " + str(k) + " \nRecalculating stall distances:\n")

        for index, toilet in enumerate(minimum):
            if (toilet != OCCUPIED):  # Only calculate empty potties
                ls = calculate_ls(minimum, index)
                rs = calculate_rs(minimum, index)
                minimum[index] = min(ls, rs)
                maximum[index] = max(ls, rs)

                # FOR TESTING PURPOSES
                #print("index: " + str(index)+ " Ls: " + str(ls) + " Rs: " + str(rs) + "\t\tmin(Ls,Rs) = " + str(minimum[index]) + "\t\tmax(Ls,Rs) = " + str(maximum[index]))

        # FOR TESTING PURPOSES
        #print("\nMINIMUM: " + str(minimum))
        #print("MAXIMUM: " + str(maximum))

        first_selection = return_maximal_min(minimum)

        if (len(first_selection) == 1):
            choose = first_selection[0] # retrieve index for toilet
        else:
            second_selection = return_maximal_max (first_selection, maximum) # choose left-most from second selection
            choose = second_selection

        last_min = str(minimum[choose])  # get last maximal minimum
        last_max = str(maximum[choose])  # get last maximal maximum

        # FOR TESTING PURPOSES
        #print("\nA potty has been occupied..!")
        #print ("\nLast min: " + str(last_min))
        #print ("Last max: " + str(last_max))

        minimum[choose] = OCCUPIED  # mark as occupied in both arrays
        maximum[choose] = OCCUPIED

        k -= 1 # counter one off
        # FOR TESTING PURPOSES
        #print("Insertion at index " + str(choose) + "(DENOTED BY -1): " + str(minimum))
        #print("Insertion at index " + str(choose) + "(DENOTED BY -1): "+ str(maximum))

    return last_max + " " + last_min

def createStalls(n):
    """Returns a list with the configuration of the bathroom stalls, both ends
    are occupied, all in between (n) are empty"""
    stalls = [OCCUPIED,OCCUPIED] # toilets in both ends are always occupied

    while (n > 0):
        stalls.insert(1, EMPTY)
        n-=1
    return stalls

def calculate_ls (stalls, index):
    """Calculates the distance to the closest occupied toilet to the left"""
    index -= 1
    ls = 0

    while (index > 0):
        if stalls[index] != OCCUPIED:
            ls += 1 # increase counter for every empty toilet found
            index -= 1
        else:
            break # break when an occupied toilet is found
    return ls

def calculate_rs(stalls, index):
    """Calculates the distance to the closest occupied toilet to the right"""
    index += 1
    rs = 0

    while (index < len(stalls)):
        if stalls[index] != OCCUPIED:
            rs += 1  # increase counter for every empty toilet found
            index += 1
        else:
            break  # break when an occupied toilet is found
    return rs

def return_maximal_min (list): # for first selection
    """Takes a list of integers, returns the a list of all indexes of the highest integers on the list"""
    highest = max (list)
    maximal = []
    for index,integer in enumerate (list):
        if (integer == highest):
            maximal.append(index)
    # FOR TESTING PURPOSES
    #print("First selection results " + str(maximal))
    return maximal

def return_maximal_max (first_selection, maximum): # for second selection
    """Takes a list of all indexes from the first selection, returns a list of all indexes where maximum is maximal"""
    maximal = []
    second_selection = -1

    for index in first_selection:
        maximal.append(maximum[index]) # return the max (Sl,Sr) value for the given indexes only

    maximal_value = max (maximal) # find the maximal among max (Sl,Sr)

    for index in first_selection:
        if (maximum[index] == maximal_value):
            second_selection = index # retrieve the index from the first selection list,
            break # only the leftmost is important, break after first is found

    # FOR TESTING PURPOSES
    #print ("Second selection results " + str(second_selection))
    return second_selection

# PATH TO EXAMPLES, HARDCODED
#path = "Input\Bathroom Stalls\C-small-practice-1.in"
#path = "Input\Bathroom Stalls\C-small-practice-2.in"
path = "Input\Bathroom Stalls\C-large-practice.in"

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
for i, sample in enumerate (samples): # print to console OR save to external file
    print("Case #" + str(i + 1) + ": " + bathroomStalls(samples[i]))
    #output.write("Case #" + str(i + 1) + ": " + bathroomStalls(samples[i]) + "\n")
#output.close()

# FOR TESTING PURPOSES
#sample = "10 5"
#print(bathroomStalls(sample))