# Google Code Jam 
# FashionShow.py
# Created by Mauro J. Pappaterra on 20 of November 2017.
from pathlib import Path
from random import *

def fashionShow (stage_layout):
    """Main algorithm for the fashion show challenge"""

    n = stage_layout[0] # store n
    m = stage_layout[1] # store m

    del stage_layout[0] # ... and delete both from list!
    del stage_layout[0]

    #FOR TESTING PURPOSES
    print ("\nn: " + str (n) + "  \t\tm: " + str (m))

    #if (len(formatted_sample) > 0):
    for i,models in enumerate (stage_layout):
        print ("pos. model " + str (i + 1) + " -> " + str(models)) # print all model positions

    stage = getStage(n, stage_layout)
    printStage(stage) # print current stage


    matrix = newMatrix(n)
    updateMatrix(n,stage,matrix)
    printMatrix(matrix) # print outfit matrix

    optimizeStage (n, stage, matrix)

    return ''

# STAGE RELATED METHODS
def getStage (n,stage_layout):
    """Takes a grid of size n x n, a list of m model's position coordenates on the grid (stage layout),
    and returns stage as a matrix"""
    stage = getEmptyStage(n)

    for model in stage_layout:
        style = model[0]
        row = model[1] - 1
        column = model[2] - 1

        stage[row][column] = style

    return stage

def getEmptyStage (n):
    """Takes an integer n and returns a matrix of n x n"""
    emptyStage = []

    k = n # store original value of n

    while (n > 0):
        nn = k
        rows = []
        while (nn > 0):
            rows.append('-')
            nn -= 1
        emptyStage.append(rows)
        n -= 1

    return emptyStage

def printStage (stage):
    """Prints the contents of the stage, auxiliary method not part of the solution"""
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
            rows.append([None,None,None,None]) # booleans for . + x and o respectively
            nn -= 1
        new_matrix.append(rows)
        n -= 1
    return new_matrix

def updateMatrix (n, stage, new_matrix):
    """Pairs a matrix with a stage"""

    for i,row in enumerate (stage):
        for j, column in enumerate (row):
            #print("This is a: " + str(stage[i][j]))
            if (stage[i][j] == 'x'):
                #print ("x found at row " + str(i + 1) + " column " + str(j + 1))
                refreshMatrix(new_matrix, i, j, 'x')

            elif (stage[i][j] == '+'):
                #print("+ found at row " + str(i + 1) + " column " + str(j + 1))
                refreshMatrix(new_matrix, i, j, '+')

            elif (stage[i][j] == 'o'):
                #print("o found at row " + str(i + 1) + " column " + str(j + 1))
                refreshMatrix(new_matrix, i, j, 'o')

            elif (stage[i][j] == '.'):
                #print(". found at row " + str(i + 1) + " column " + str(j + 1))
                refreshMatrix(new_matrix, i, j, '.')

def refreshMatrix (matrix, row_index, column_index, style):

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
            matrix[row][column][1] = False #for +
            matrix[row][column][2] = True #for x
            matrix[row][column][3] = False #for o
            row += 1
            column += 1

        column = column_index + 1  # updates diagonal SECOND QUADRANT
        row = row_index - 1
        while (column <= size and row <= size and column >= 0 and row >= 0):
            matrix[row][column][1] = False #for +
            matrix[row][column][2] = True #for x
            matrix[row][column][3] = False #for o
            row -= 1
            column += 1

        column = column_index - 1  # updates diagonal THIRD QUADRANT
        row = row_index - 1
        while (column <= size and row <= size and column >= 0 and row >= 0):
            matrix[row][column][1] = False #for +
            matrix[row][column][2] = True #for x
            matrix[row][column][3] = False #for o
            row -= 1
            column -= 1

        column = column_index - 1  # updates diagonal FOURTH QUADRANT
        row = row_index + 1
        while (column <= size and row <= size and column >= 0 and row >= 0):
            matrix[row][column][1] = False #for +
            matrix[row][column][2] = True #for x
            matrix[row][column][3] = False #for o
            row += 1
            column -= 1

        matrix[row_index][column_index][0] = False
        matrix[row_index][column_index][2] = False
        matrix[row_index][column_index][3] = False

    elif (bool == 2): # for x

        column = 0
        for models in matrix: # updates row
            matrix[row_index][column][1] = True  # for +
            matrix[row_index][column][2] = False  # for x
            matrix[row_index][column][3] = False  # for o
            column += 1

        row = 0
        for models in matrix: # updates column
            matrix[row][column_index][1] = True  # for +
            matrix[row][column_index][2] = False  # for x
            matrix[row][column_index][3] = False  # for o
            row += 1

        matrix[row_index][column_index][0] = False
        matrix[row_index][column_index][1] = False
        matrix[row_index][column_index][3] = False

    elif (bool == 3):

        column = 0
        for models in matrix:  # updates row
            matrix[row_index][column][1] = True  # for +
            matrix[row_index][column][2] = False  # for x
            matrix[row_index][column][3] = False  # for o
            column += 1

        row = 0
        for models in matrix:  # updates column
            matrix[row][column_index][1] = True  # for +
            matrix[row][column_index][2] = False  # for x
            matrix[row][column_index][3] = False  # for o
            row += 1

        size = len(matrix) - 1

        column = column_index + 1  # updates diagonal FIRST QUADRANT
        row = row_index + 1
        while (column <= size and row <= size and column >= 0 and row >= 0):
            matrix[row][column][1] = False  # for +
            matrix[row][column][2] = True  # for x
            matrix[row][column][3] = False  # for o
            row += 1
            column += 1

        column = column_index + 1  # updates diagonal SECOND QUADRANT
        row = row_index - 1
        while (column <= size and row <= size and column >= 0 and row >= 0):
            matrix[row][column][1] = False  # for +
            matrix[row][column][2] = True  # for x
            matrix[row][column][3] = False  # for o
            row -= 1
            column += 1

        column = column_index - 1  # updates diagonal THIRD QUADRANT
        row = row_index - 1
        while (column <= size and row <= size and column >= 0 and row >= 0):
            matrix[row][column][1] = False  # for +
            matrix[row][column][2] = True  # for x
            matrix[row][column][3] = False  # for o
            row -= 1
            column -= 1

        column = column_index - 1  # updates diagonal FOURTH QUADRANT
        row = row_index + 1
        while (column <= size and row <= size and column >= 0 and row >= 0):
            matrix[row][column][1] = False  # for +
            matrix[row][column][2] = True  # for x
            matrix[row][column][3] = False  # for o
            row += 1
            column -= 1

        matrix[row_index][column_index][0] = False
        matrix[row_index][column_index][1] = False
        matrix[row_index][column_index][2] = False

    matrix[row_index][column_index][bool] = True

def printMatrix (matrix):
    """Auxiliary method that print the content of the matrix, not part of the solution"""
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
    print (printout)

# OPTIMIZATION ALGORITHM
def optimizeStage (n, stage, matrix):

    changes = 0

    for i,row in enumerate(stage):
        for j,column in enumerate(row):
            #print (column)
            if (column == '-'):
                print ("optimize that shit")
                if (matrix[i][j] == [True, False, False, False] or matrix[i][j] == [False, False, False, False]):

                    stage[i][j] = '.' # update stage
                    changes += 1 # counter for changes made

                    updateMatrix(n, stage, matrix) # update matrix, this method calls refresh too!

                    printStage(stage)
                    printMatrix(matrix)

                elif (matrix[i][j] == [True, True, False, False] or matrix[i][j] == [False, True, False, False]):
                    stage[i][j] = '+'
                    changes += 1

                    updateMatrix(n, stage, matrix)

                    printStage(stage)
                    printMatrix(matrix)

                elif (matrix[i][j] == [True, False, True, False] or matrix[i][j] == [False, False, True, False]):
                    stage[i][j] = 'x'
                    changes += 1

                    updateMatrix(n, stage, matrix)

                    printStage(stage)
                    printMatrix(matrix)

                elif (matrix[i][j] == [True, False, False, True] or matrix[i][j] == [False, False, False, True]):
                    stage[i][j] = 'o'
                    changes += 1

                    updateMatrix(n, stage, matrix)

                    printStage(stage)
                    printMatrix(matrix)

                elif (matrix[i][j] == [True, True, False, True] or matrix[i][j] == [False, True, False, True]):
                    stage[i][j] = 'o'
                    changes += 1

                    updateMatrix(n, stage, matrix)

                    printStage(stage)
                    printMatrix(matrix)

                elif (matrix[i][j] == [True, True, True, False] or matrix[i][j] == [False, True, True, False]):


                    randomize = randint(0, 1) # randomly print 1 or 0

                    if (randomize == 0):
                        stage[i][j] = '+'
                    else:
                        stage[i][j] = 'x'

                    changes += 1

                    updateMatrix(n, stage, matrix)

                    printStage(stage)
                    printMatrix(matrix)

                elif (matrix[i][j] == [True, False, True, True] or matrix[i][j] == [False, False, True, True]):

                    stage[i][j] = 'o'
                    changes += 1

                    updateMatrix(n, stage, matrix)

                    printStage(stage)
                    printMatrix(matrix)

                elif(matrix[i][j] == [True, True, True, True] or matrix[i][j] == [False, True, True, True]):
                    stage[i][j] = 'o'
                    changes += 1

                    updateMatrix(n, stage, matrix)

                    printStage(stage)
                    printMatrix(matrix)

    return ''



#PATH TO EXAMPLES, HARDCODED
path = "Input\Fashion Show\D-small-practice.in"
#path = "Input\Fashion Show\D-large-practice.in"

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


formatted_samples = [] # reformat samples for better usability
for index,lines in enumerate (samples):

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

    if (len(new_sample)>0):
        formatted_samples.append(new_sample)
#FOR TESTING PURPOSES
#for sample in formatted_samples:
#    print (sample)


#for i, sample in enumerate (formatted_samples):
#    print("Case #" + str(i + 1) + ": " + fashionShow(formatted_samples[i]))

#FOR TESTING PURPOSES

#FOR TESTING PURPOSES ONLY
fashionShow([3, 1, ['o', 1, 1]])
#fashionShow([20, 3, ['o', 9, 9], ['+', 4, 4], ['+', 1, 11]])
#fashionShow([29, 5, ['+', 1, 22], ['+', 1, 26], ['o', 1, 5], ['+', 1, 16], ['+', 1, 23]])
#fashionShow([6, 0])

