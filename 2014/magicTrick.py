# Google Code Jam 
# magicTrick.py
# Created by Mauro J. Pappaterra on 13 of March 2018.
from pathlib import Path

def magicTrick(sample):

    sample = [int(x) for x in sample.split(' ') if True]

    first_selected = sample[0]
    first_layout = [sample[1:5],sample[5:9],sample[9:13],sample[13:17]]

    second_selected = sample[17]
    second_layout = [sample[18:22],sample[22:26],sample[26:30], sample[30:34]]

    # FOR TESTING PURPOSES
    #print(first_layout)
    #print(second_layout)

    first = first_layout[first_selected - 1]
    second = second_layout[second_selected - 1]

    # FOR TESTING PURPOSES
    #print(first)
    #print(second)

    lucky_guess = []

    for card_a in first:
        for card_b in second:
            if (card_a == card_b):
                lucky_guess.append(card_a)
                continue

    if (len(lucky_guess) > 1):
        return "Bad magician!"
    elif (len(lucky_guess) == 0):
        return "Volunteer cheated!"
    else:
        return str(lucky_guess[0])


#PATH TO EXAMPLES, HARDCODED
path = "Input\Magic Trick\A-small-practice.in"

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
    formatted_samples[j] = samples[i][:-1] + " " + samples[i+1][:-1] + " " + samples[i+2][:-1]+ " " + samples[i+3][:-1]+ " " + samples[i+4][:-1] +\
    " " + samples[i+5][:-1] + " " + samples[i+6][:-1]+ " " + samples[i+7][:-1]+ " " + samples[i+8][:-1]+ " " + samples[i+9][:-1]
    i+=10
    j+=1

# PRINT OUTPUT OR SAVE TO EXTERNAL FILE
path = path.replace("Input","Output")
output = open(path, "+w")
for i, sample in enumerate (formatted_samples):
    #print("Case #" + str(i + 1) + ": " + magicTrick(sample))
    output.write("Case #" + str(i + 1) + ": " + magicTrick(sample) + "\n")
output.close()

