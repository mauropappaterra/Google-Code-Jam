# Google Code Jam 
# Fractiles.py
# Created by Mauro J. Pappaterra on 09 of March 2018.
from pathlib import Path

GOLD = 'G'
LEAD = 'L'

def fractiles (sample):
    sample = sample.split(' ')

    K = int(sample[0]) # number of tiles
    C = int(sample[1]) # complexity: number of transformations
    S = int(sample[2]) # students: number of tiles that can be turned over


    if (S == K): # TIME SAVER: save some time discarding sequences we can see entirely
        i = 1
        results = ""
        while (i <= K):
            results += str(i) + " "
            i += 1
        return results

    #FOR TESTING PURPOSES
    #print("\nK = " + str(K) + "\nC = " + str(C) + "\nS = " + str(S) + "\n")
    possible_sequences = createSequences(K)
    art_sequences = []

    #FOR TESTING PURPOSES
    #print("All possible sequences")
    for sequence in possible_sequences:
        #printSequence(sequence)
        art_sequences.append(createArtwork(sequence, "".join(sequence), GOLD * (C + 1), C))

    #FOR TESTING PURPOSES
    #print("\nAll transformed sequences")
    #for sequence in art_sequences:
    #    printSequence(sequence)

    results = findIndex(art_sequences,S)

    if (checkImpossible(art_sequences, results)):
        return "IMPOSSIBLE"

    return " ".join(results)

def checkImpossible (art_sequence, results):
    no_indexes = len(results)
    check = []

    for sequence in art_sequence:
        flag = True
        i = 0

        while (i < no_indexes):
            if (sequence[i] == GOLD):
                flag = False
            i += 1

        if (flag):
            check.append(sequence)
    #FOR TESTING PURPOSES
    #print(check)
    if (len(check) > 1):
        return True

    return False

def findIndex(art_sequences, S):
    all_counters = []

    for sequence in art_sequences[0]:
        all_counters.append(0)

    length = len(all_counters) - 1
    index = 0

    #FOR TESTING PURPOSES
    #print(all_counters)
    #print (str(length))

    while (index <= length):
        for sequence in art_sequences[1:-1]:
            if (sequence[index] == LEAD):
                all_counters[index] += 1
        index += 1

    #FOR TESTING PURPOSES
    #print(all_counters)
    return returnMinimal (all_counters, S)

def returnMinimal (all_counters, S):

    minimal = []
    minimun = min(all_counters)

    for index,counter in enumerate (all_counters):
        if (S > 0):
            if (counter == minimun):
                minimal.append(str(index + 1))
                S -= 1

    #FOR TESTING PURPOSES
    #print(minimal)
    return minimal

def createArtwork (sequence, original, gold, complexity):

    complexity -= 1

    if (complexity > 0):

        for index,tile in enumerate(sequence):

            if (tile == GOLD):
                sequence[index] = gold
            elif (tile == LEAD):
                sequence[index] = original

        new_sequence = list("".join(sequence))

        #FOR TESTING PURPOSES
        #printSequence(new_sequence)
        return createArtwork(new_sequence, original, gold, complexity)

    else:
        #FOR TESTING PURPOSES
        #printSequence(sequence)
        return sequence

def createSequences (k):
    all_sequences = []
    sequence = emptySequence(k)

    gold_tiles = 0

    while (gold_tiles <= k):
        all_sequences += completeSequence(sequence,gold_tiles,0)
        gold_tiles += 1

    return all_sequences

def completeSequence (sequence, gold_tiles, index):

    if (gold_tiles > 0):
        gold_tiles -= 1
        return_sequences = []

        while (index < len(sequence)):

            new_sequence = sequence[:]

            if (sequence[index] != GOLD):
                new_sequence[index] = GOLD
                return_sequences += completeSequence(new_sequence, gold_tiles, index + 1)

            index += 1

        return return_sequences

    else:
        return [sequence]

def emptySequence (k):
    sequence = []

    while (k > 0):
        sequence.append(LEAD)
        k -= 1
    #FOR TESTING PURPOSES
    #print(sequence)
    return sequence

def printSequence (sequence):
    printout = ""
    for tile in sequence:
        printout += tile + ' '
    print(printout)

# PATH TO EXAMPLES, HARDCODED
path = "Input\Fractiles\D-small-practice.in"
#path = "Input\Fractiles\D-large-practice.in"

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
    print("Case #" + str(i + 1) + ": " + fractiles(sample))
    #output.write("Case #" + str(i + 1) + ": " + fractiles(sample) + "\n")
#output.close()

# FOR TESTING PURPOSES

#emptySequence(10)

#print(completeSequence([LEAD,LEAD,LEAD,LEAD],0,0))
#print(completeSequence([LEAD,LEAD,LEAD,LEAD],1,0))
#print(completeSequence([LEAD,LEAD,LEAD,LEAD],2,0))
#print(completeSequence([LEAD,LEAD,LEAD,LEAD],3,0))
#print(completeSequence([LEAD,LEAD,LEAD,LEAD],4,0))

#print(createSequences(3))

#print(fractiles("2 3 2"))
#print(fractiles("1 1 1"))
#print(fractiles("2 1 1"))
#print(fractiles("2 1 2"))
#print(fractiles("3 2 3"))