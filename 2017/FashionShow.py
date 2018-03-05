# Google Code Jam 
# FashionShow.py
# Created by Mauro J. Pappaterra on 20 of November 2017.
from pathlib import Path
from random import *

def fashionShow (stage_layout): # format [48, 3, ['+', 1, 33], ['+', 1, 34], ['o', 1, 19]]
    """Main algorithm for the fashion show challenge"""

    n = stage_layout[0] # store n
    m = stage_layout[1] # store m

    del stage_layout[0] # ... and delete both from list!
    del stage_layout[0]

    # FOR TESTING PURPOSES
    #print ("\nn: " + str (n) + "  \t\tm: " + str (m))

    #for i,models in enumerate (stage_layout):
    #    print ("pos. model " + str (i + 1) + " -> " + str(models)) # print all model positions

    stage = getStage(n, stage_layout) # format [['+', '-', '-'], ['+', '-',  '-'], [ '-',  '-', 'o']]
    #printStage(stage) # print current stage

    matrix = newMatrix(n) # format [[[False, False, True, False], [True, None, None, None], ...] for each element
    populateMatrix(n, stage, matrix)
    #printMatrix(matrix) # print outfit matrix

    models = optimizeStage (n, stage, matrix)
    points = getPoints (stage)

    # FOR TESTING PURPOSES
    #print ("Number of changes done: " + str(models) + " Total points: " + str(points))

    return str(points) + " " + str(models)

# STAGE RELATED METHODS
def getStage (n,stage_layout):
    """Takes a grid of size n x n, a list of m model's position coordinates on the grid (stage layout),
    and returns stage as a matrix (list of lists)"""
    stage = []
    k = n  # store original value of n

    while (n > 0):
        nn = k
        rows = []
        while (nn > 0):
            rows.append('-')
            nn -= 1
        stage.append(rows)
        n -= 1

    for model in stage_layout:
        style = model[0]
        row = model[1] - 1
        column = model[2] - 1

        stage[row][column] = style
    return stage

def printStage (stage):
    """Prints the contents of the stage on a more readable format. This is an auxiliary method not part of the solution"""
    print("")
    for row in stage:
        print(" ".join(row))
    print("")

# MATRIX RELATED METHODS
def newMatrix (n):
    """Returns an 'empty' matrix without any estimations"""
    new_matrix = []

    k = n  # store original value of n

    while (n > 0): #Create an empty matrix
        nn = k
        rows = []
        while (nn > 0):
            rows.append([True,True,True,True]) # booleans for . + x and o respectively, True is the neutral of the and logical operator
            nn -= 1
        new_matrix.append(rows)
        n -= 1
    return new_matrix

def populateMatrix (n, stage, matrix):
    """Pairs a matrix with a given stage layout, the values for the matrix are given
    following the rules established on the problem enunciation"""

    for i,row in enumerate (stage):
        for j, column in enumerate (row):
            #FOR TESTING PURPOSES
            #print(str(stage[i][j]) + " found at row " + str(i) + " column " + str(j))
            if (stage[i][j] == 'x'):
                refreshMatrix(matrix, i, j, 'x')

            elif (stage[i][j] == '+'):
                refreshMatrix(matrix, i, j, '+')

            elif (stage[i][j] == 'o'):
                refreshMatrix(matrix, i, j, 'o')

            elif (stage[i][j] == '.'):
                refreshMatrix(matrix, i, j, '.')

def refreshMatrix (matrix, row_index, column_index, style):
    """Takes a given matrix, a style and its coordinates, updates the matrix values
    following the rules established on the problem enunciation"""

    if (style == '.'):
        bool = 0 # for .
    elif (style == '+'):
        bool = 1 # for +
    elif (style == 'x'):
        bool = 2 # for x
    if (style == 'o'):
        bool = 3 #for o

    if (bool == 1): # for +

        size = len(matrix) - 1

        column = column_index + 1  # updates diagonal FIRST QUADRANT
        row = row_index + 1
        while (column <= size and row <= size and column >= 0 and row >= 0):
            matrix[row][column][1] = matrix[row][column][1] and False #for +
            matrix[row][column][2] = matrix[row][column][2] and True #for x
            matrix[row][column][3] = matrix[row][column][3] and False  # for o
            row += 1
            column += 1

        column = column_index + 1  # updates diagonal SECOND QUADRANT
        row = row_index - 1
        while (column <= size and row <= size and column >= 0 and row >= 0):
            matrix[row][column][1] = matrix[row][column][1] and False #for +
            matrix[row][column][2] = matrix[row][column][2] and True #for x
            matrix[row][column][3] = matrix[row][column][3] and False  # for o
            row -= 1
            column += 1

        column = column_index - 1  # updates diagonal THIRD QUADRANT
        row = row_index - 1
        while (column <= size and row <= size and column >= 0 and row >= 0):
            matrix[row][column][1] = matrix[row][column][1] and False  # for +
            matrix[row][column][2] = matrix[row][column][2] and True  # for x
            matrix[row][column][3] = matrix[row][column][3] and False  # for o
            row -= 1
            column -= 1

        column = column_index - 1  # updates diagonal FOURTH QUADRANT
        row = row_index + 1
        while (column <= size and row <= size and column >= 0 and row >= 0):
            matrix[row][column][1] = matrix[row][column][1] and False  # for +
            matrix[row][column][2] = matrix[row][column][2] and True  # for x
            matrix[row][column][3] = matrix[row][column][3] and False  # for o
            row += 1
            column -= 1

    elif (bool == 2): # for x

        column = 0
        for models in matrix: # updates row
            matrix[row_index][column][1] = matrix[row_index][column][1] and True  # for +
            matrix[row_index][column][2] = matrix[row_index][column][2] and False  # for x
            matrix[row_index][column][3] = matrix[row_index][column][3] and False  # for o
            column += 1

        row = 0
        for models in matrix: # updates column
            matrix[row][column_index][1] = matrix[row][column_index][1] and True  # for +
            matrix[row][column_index][2] = matrix[row][column_index][2] and False  # for x
            matrix[row][column_index][3] = matrix[row][column_index][3] and False  # for o
            row += 1

    elif (bool == 3): # for o

        column = 0
        for models in matrix:  # updates row
            matrix[row_index][column][1] = matrix[row_index][column][1] and True  # for +
            matrix[row_index][column][2] = matrix[row_index][column][2] and False  # for x
            matrix[row_index][column][3] = matrix[row_index][column][3] and False  # for o
            column += 1

        row = 0
        for models in matrix:  # updates column
            matrix[row][column_index][1] = matrix[row][column_index][1] and True  # for +
            matrix[row][column_index][2] = matrix[row][column_index][2] and False  # for x
            matrix[row][column_index][3] = matrix[row][column_index][3] and False  # for o
            row += 1

        size = len(matrix) - 1

        column = column_index + 1  # updates diagonal FIRST QUADRANT
        row = row_index + 1
        while (column <= size and row <= size and column >= 0 and row >= 0):
            matrix[row][column][1] = matrix[row][column][1] and False  # for +
            matrix[row][column][2] = matrix[row][column][2] and True  # for x
            matrix[row][column][3] = matrix[row][column][3] and False  # for o
            row += 1
            column += 1

        column = column_index + 1  # updates diagonal SECOND QUADRANT
        row = row_index - 1
        while (column <= size and row <= size and column >= 0 and row >= 0):
            matrix[row][column][1] = matrix[row][column][1] and False  # for +
            matrix[row][column][2] = matrix[row][column][2] and True  # for x
            matrix[row][column][3] = matrix[row][column][3] and False  # for o
            row -= 1
            column += 1

        column = column_index - 1  # updates diagonal THIRD QUADRANT
        row = row_index - 1
        while (column <= size and row <= size and column >= 0 and row >= 0):
            matrix[row][column][1] = matrix[row][column][1] and False  # for +
            matrix[row][column][2] = matrix[row][column][2] and True  # for x
            matrix[row][column][3] = matrix[row][column][3] and False  # for o
            row -= 1
            column -= 1

        column = column_index - 1  # updates diagonal FOURTH QUADRANT
        row = row_index + 1
        while (column <= size and row <= size and column >= 0 and row >= 0):
            matrix[row][column][1] = matrix[row][column][1] and False  # for +
            matrix[row][column][2] = matrix[row][column][2] and True  # for x
            matrix[row][column][3] = matrix[row][column][3] and False  # for o
            row += 1
            column -= 1

    matrix[row_index][column_index][bool] = True

def printMatrix (matrix):
    """Auxiliary method that print the content of the matrix in a more readable format.
    This is not part of the solution"""
    printout = '\n'

    for rows in matrix:
        row = ''

        for column in rows:
            col = ''

            if (column[0] == False):
                col += ' F'
            elif (column[0] == True):
                col += ' T'
            else:
                col += ' -'

            if (column[1] == False):
                col += 'F'
            elif (column[1] == True):
                col += 'T'
            else:
                col += '-'

            if (column[2] == False):
                col += 'F'
            elif (column[2] == True):
                col += 'T'
            else:
                col += '-'

            if (column[3] == False):
                col += 'F '
            elif (column[3] == True):
                col += 'T '
            else:
                col += '- '

            row += col

        printout += row + '\n'

    # FOR TESTING PURPOSES
    #print (matrix)
    print (printout)

# OTHER ALGORITHMS
def optimizeStage (n, stage, matrix):
    """Takes a stage of dimension n, and a matrix of style values, optimizes the stage while updating the matrix
    for the best possible outcome as established on the problem enunciation. It returns the number of changes done."""
    changes = 0

    for i,row in enumerate(stage):
        for j,column in enumerate(row):
            #FOR TESTING PURPOSES
            #print("matrix results for row: " + str(row) + " element -> " + str(column))

            if (column == '-'):
                if (matrix[i][j] == [True, False, False, False]):
                    stage[i][j] = '.' # update stage
                    refreshMatrix(matrix, i, j, '.')

                elif (matrix[i][j] == [True, True, False, False]):
                    stage[i][j] = '+'
                    refreshMatrix(matrix, i, j, '+')
                    changes += 1

                elif (matrix[i][j] == [True, False, True, False]):
                    stage[i][j] = 'x'
                    refreshMatrix(matrix, i, j, 'x')
                    changes += 1

                elif (matrix[i][j] == [True, False, False, True]):
                    stage[i][j] = 'o'
                    refreshMatrix(matrix, i, j, 'o')
                    changes += 1

                elif (matrix[i][j] == [True, True, False, True]):
                    stage[i][j] = 'o'
                    refreshMatrix(matrix, i, j, 'o')
                    changes += 1

                elif (matrix[i][j] == [True, True, True, False]):
                    randomize = randint(0, 1) # randomly print 1 or 0

                    if (randomize == 0):
                        stage[i][j] = '+'
                        refreshMatrix(matrix, i, j, '+')
                    else:
                        stage[i][j] = 'x'
                        refreshMatrix(matrix, i, j, 'x')

                    changes += 1

                elif (matrix[i][j] == [True, False, True, True]):
                    stage[i][j] = 'o'
                    refreshMatrix(matrix, i, j, 'o')
                    changes += 1

                elif(matrix[i][j] == [True, True, True, True]):
                    stage[i][j] = 'o'
                    refreshMatrix(matrix, i, j, 'o')
                    changes += 1

            #FOR TESTING PURPOSES
            #printStage(stage)
            #printMatrix(matrix)

    return changes

def getPoints (stage):
    """Takes an optimized stage, and returns the amount of points  calculated as follows:
    '.' = 0 points, 'x' or '+' = 1 point and 'o' = 2 points"""
    points = 0

    for row in stage:
        for style in row:
            if (style == '+'):
                points += 1
            elif (style == 'x'):
                points += 1
            if (style == 'o'):
                points += 2
    return points

def format_samples(samples):
    """Takes the sample file given as input, formats it so each example it's a different list of its own"""
    formatted_samples = []  # reformat samples for better usability

    for index, lines in enumerate(samples):

        line = samples[index][:-1]
        new_list = line.split(' ')

        new_sample = []

        if (new_list[0].isnumeric()):
            n = int(new_list[0])
            m = int(new_list[1])
            new_sample.append(n)
            new_sample.append(m)

            index += 1
            while (m > 0):
                line = samples[index][:-1]
                new_list = line.split(' ')
                model = new_list[0]
                row = int(new_list[1])
                column = int(new_list[2])
                new_sample.append([model, row, column])
                index += 1
                m -= 1

        if (len(new_sample) > 0):
            formatted_samples.append(new_sample)

    return formatted_samples

# PATH TO EXAMPLES, HARDCODED
#path = "Input\Fashion Show\D-small-practice.in"
path = "Input\Fashion Show\D-large-practice.in"

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

formatted = format_samples (samples)

# FOR TESTING PURPOSES
#for sample in formatted:
#    print (sample)

# PRINT OUTPUT OR SAVE TO EXTERNAL FILE
#path = path.replace("Input", "Output")
#output = open(path, "+w")
for i, sample in enumerate (formatted):
    print("Case #" + str(i + 1) + ": " + fashionShow(formatted[i]))
    #output.write("Case #" + str(i + 1) + ": " + fashionShow(formatted[i]) + "\n")
#output.close()

# FOR TESTING PURPOSES ONLY
#fashionShow([6, 0])
#fashionShow([3, 1, ['o', 2, 2]])
#fashionShow([10, 0])
#fashionShow([10, 3, ['+', 1, 10], ['+', 5, 5], ['o', 5, 10], ['+', 10, 5]])
#fashionShow([20, 3, ['o', 9, 9], ['+', 4, 4], ['+', 1, 11]])
#fashionShow([29, 5, ['+', 1, 22], ['+', 1, 26], ['o', 1, 5], ['+', 1, 16], ['+', 1, 23]])