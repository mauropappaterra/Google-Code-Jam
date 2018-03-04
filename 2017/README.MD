<pre id="top">
   ___                  _          ___          _         __                    ____   ___  _ _____ 
  / _ \___   ___   __ _| | ___    / __\___   __| | ___    \ \  __ _ _ __ ___   |___ \ / _ \/ |___  |
 / /_\/ _ \ / _ \ / _` | |/ _ \  / /  / _ \ / _` |/ _ \    \ \/ _` | '_ ` _ \    __) | | | | |  / / 
/ /_\\ (_) | (_) | (_| | |  __/ / /__| (_) | (_| |  __/ /\_/ / (_| | | | | | |  / __/| |_| | | / /  
\____/\___/ \___/ \__, |_|\___| \____/\___/ \__,_|\___| \___/ \__,_|_| |_| |_| |_____|\___/|_|/_/   
                  |___/                                                                             
                                                                                                    
</pre>

<h1>Google Code Jam 2017</h1>
List of Solved Challenges<br>
<a href="#pancake">-Pancake Flipper</a><br>
<a href="#numbers">-Tidy Numbers</a><br>
<a href="#potty">-Bathroom Stalls</a><br>
<a href="#fashion">-Fashion Show</a><br>

<br>
More <br>
<a href="#help">Instructions to run the programs</a> <br>
<a href="https://github.com/yogurt1989/Google-Code-Jam">Go Back</a>
<br>

<hr>
<h3 id="pancake">Pancake Flipper</h3>
<i>The challenge <a href="https://code.google.com/codejam/contest/3264486/dashboard#s=p0"><b>Click here to read the full challenge at Google's Code Jam website</b></a></i> <br>
<i>Solution Script </i> <a href="https://github.com/yogurt1989/Google-Code-Jam/blob/master/2017/PancakeFlipper.py" target="_blank"><b>PancakeFlipper.py</b></a> <br>
<h4>My Solution</h4>
We first iterate the file containing all samples. We saved the first line on the file, that contains the number of samples, in a variable
no_samples, then we created a special function returnDictionary(string) that takes a line from the sample
file and returns a dictionary containing the row of pancakes as a string and the number of possible
simultaneous flips (k) as an integer. We call this function to each line of the file as we call our main
function that solves the pancake flipper problem.
Our main function pancakeFlipper(row, k) takes a row of pancakes as a string and an integer as k. We
save the length of the row in a variable length and create a counter flips, that is the returning variable for
the function. We also create a flag impossible deemed as false that will indicate if the given parameters
have a solution or not. An auxiliary function flip(char) toggles + for – and – for +. The heart of the
algorithm are two while statements that will check each character (pancake) on the row and flip it along
with the following k pancakes if the character equals –, on the right side and on the left side respectively.
A variable containing the size of the pancake row is used to avoid and index out of bounds error. Every
time a flip occurs the counter flips increases by 1. If there is a lock or an infinite loop, the flag impossible
is assigned a value True, that will determine if the final string returned by the function is the string
“IMPOSSIBLE” or the counter flips casted as a string.
<br>
<br>
<a href="#top">Back to Top</a> 
<br>

<hr>
<h3 id="numbers">Tidy Numbers</h3>
<i>The challenge <a href="https://code.google.com/codejam/contest/3264486/dashboard#s=p1"><b>Click here to read the full challenge at Google's Code Jam website</b></a></i> <br>
<i>Solution Script </i> <a href="https://github.com/yogurt1989/Google-Code-Jam/blob/master/2017/TidyNumbers.py" target="_blank"><b>TidyNumbers.py</b></a> <br>
<h4>My Solution</h4>
The first function that we call is convertToDigitList(numberAsString), this function will prepare our sample data to undergo
our algorithm by converting a number given as a string form the sample file in a list of integers containing
each digit of the number as an element of the list. We will solve this exercise using this structure,
nonetheless we have included other function to manipulate the samples and the results: the functions
convertToString(digitList) and convertToInteger(digitList) convert the list of integers back to a string or a single integer
respectively. The subfunction checkTidy(digitList) will check if a list of integers is already tidy, if it is we will just
return the same number. The subfunction findLastTidy(listOfDigits) will search for the last tidy number if the number
given is untidy: a for loop will iterate the list of integers and if an integer is smaller than its predecessor it
will be decreased by one and the following integers (digits) on its right turn into nines. This will not
always guarantee that the number will be left tidy, to solve this we call the function recursively until it
returns a tidy number, once again we use the auxiliary function checkTidy to verify this every time. <br>
<br>
<a href="#top">Back to Top</a> 
<br>

<hr>
<h3 id="potty">Bathroom Stalls</h3>
<i>The challenge <a href="https://code.google.com/codejam/contest/3264486/dashboard#s=p2"><b>Click here to read the full challenge at Google's Code Jam website</b></a></i> <br>
<i>Solution Script</i> <a href="https://github.com/yogurt1989/Google-Code-Jam/blob/master/2017/BathroomStalls.py" target="_blank"> <b>BathroomStalls.py</b></a> <br>
<h4>My Solution</h4>
This challenged seemed simple at first, but it became more complicated as I followed each step to get to a solution. Due to the intrinsic complexity of this challenge I implemented console printouts in order to aid me in the process, these have been commented out.
The main algorithm is bathroomStalls (input). The first thing we need to do is to separate n (number of stalls) and k (number of people on the stall). Since nobody ever leaves, is always true that k <= n. I used tro different lists (arrays) in order to keep track of the occupied and used toilets. The array minimum keeps track of the formula min (Ls,Rs) = maximal, whereas the array maximum keeps track of the formula max (Ls,Lr) = maximal. In order to create this two least we call the algorithm createStalls(n) that returns a list with the configuration of the bathroom stalls, both ends are occupied, all in between (n) are empty. I created two constants OCCUPIED and EMPTY and assigned the values -1 and 0 respectively.<br>
Now we arrive to the first loop of the algorithm that will repeat as long as there are people on the queue and empty bathroom stalls. For each bathroom stall that is available, we calculate the number of empty stalls to the left and to the right, using the methods calculate_ls(stalls, index) and calculate_rs(stalls, index) respectively. We then use the Python functions to calculate the minimum and maximum and save the results on their corresponding array.<br>
For the first selection, we call the method return_maximal_min (list), this method takes a list of integers, and returns the a list of all indexes of the highest integers on the list. If this list has a single element, we have our chosen stall to occupied. Otherwise we run the second selection round as specified on the challenge enunciate. If this is the case we call the method return_maximal_max (first_selection, maximum), this method takes a list of all indexes from the first selection, returns a list of all indexes where maximum is maximal. In this last case if we have more than one candidate we choose the most left bathroom stall. Last but not least, we saved the last maximal minimum and last maximal maximum variables since we will need them for the final output.<br>
Once we have our decision we mark the stall as occupied in both minimum and maximum arrays. This is done until, there are no more people in the queue or all bathroom stalls are occupied. The final output is the last recorded values for the last maximal minimum and last maximal maximum.<br>
<br>
<a href="#top">Back to Top</a> 
<br>

<hr>
<h3 id="fashion">Fashion Show</h3>
<i>The challenge <a href="https://code.google.com/codejam/contest/3264486/dashboard#s=p3"><b>Click here to read the full challenge at Google's Code Jam website</b></a></i> <br>
<i>Solution Script</i> <a href="https://github.com/yogurt1989/Google-Code-Jam/blob/master/2017/FashionShow.py" target="_blank"><b>FashionShow.py</b></a> <br>
<h4>My Solution</h4>
This was one difficult challenge! To start with, the samples are all given in multiple lines of texts. To solve this I wrote a method format_samples(samples) that formats each sample as a list containing all samples as list of their own following the format [48, 3, ['+', 1, 33], ['+', 1, 34], ['o', 1, 19]], where the first number appearing is n, the second corresponds to m, and then all given models as list, containing style, and row and column coordinate positions respectively.<br>
Once the samples are formatted we can start solving the challenge. The main algorithm fashionShow(stage_layout) takes a stage layout (sample) as an argument. First it stores the values of n and m in independent variables and deletes them from the list, leaving a full list of only models styles and coordinates (if any). For this solution I used two different matrices, the first matrix contains the stage layout, the second matrix contains a list of four booleans that keep track of the possible changes for each model on the stage. To get the first matrix we call the method getStage(n, stage_layout). This method takes a grid of size n x n, a list of m model's position coordinates on the grid (stage layout), and returns the stage as a matrix (list of lists). All empty spaces on the list are completed with the char '-'. Then we proceed to create the second matrix, the method newMatrix (n) returns a new matrix of n x n, that contains no estimations. The neutral value I chose is True, since it is neutral on the logical operator AND, that is to say it will be absorbed when the real estimations are given. Each element of the second matrix corresponds to each model on the first matrix. The second matrix keeps a list (array) of booleans of the form [True,True,True,True], corresponding respectively to the possible states '.', '+', 'x', or 'o'. Once we got our 'empty' matrix it is time to pair it with the given stage, to do this we call the method populateMatrix (n,stage,matrix). This method will iterate both matrices, and call the subroutine refreshMatrix (matrix, row_index, column_index, style) for every model on the stage. The latest method will, update the entire estimation matrix according to the set of rules given on the Fashion Challenge. Note that estimations must be updated from the coordinates of insertion of a model taking into account rows, columns and diagonal lines (which I separated in four different quadrants).
Once we got the stage and the matrix with all possible states, we called the method optimizeStage (n, stage, matrix). This method will go through the stage and now updated matrix, and try to place new models in every open position available that it finds. Obviously, every new model that is inserted must call for the refreshMatrix() method in order to update the estimations. This method conveniently returns the number of insertions that occurred. The final method getPoints (stage) calculates the total points on the stage following the specifications of the challenge. Due to the intrinsic complexity of this challenge, I had to implement methods for printing both matrices, these methods are not part of the final solution but aid me on the resolution of the challenge.
Once we got the stage and the matrix with all possible states, we called the method optimizeStage (n, stage, matrix). This method will go through the stage and now updated matrix, and try to place new models in every open position available that it finds. Obviously, every new model that is inserted must call for the refreshMatrix() method in order to update the estimations. This method conveniently returns the number of insertions that occurred. The final method getPoints (stage) calculates the total points on the stage following the specifications of the challenge. Due to the intrinsic complexity of this challenge, I had to implement methods for printing both matrices, these methods are not part of the final solution but aid me on the resolution of the challenge.
<br>
<br>
<a href="#top">Back to Top</a> 
<br>

<hr>
<h3 id="help">Instructions to run the programs</h3>
-Clone or download this repository<br>
-To run these programs in your computer you need to <a href="https://www.python.org/downloads/">download and install Python 3.</a><br>
-To execute from the command line on a Ms Windows system you need to <a href="https://docs.python.org/2/using/windows.html">add Python to the PATH environmental variable.</a><br>
-Do not hesitate to contact me if you have any problems running these programs <br>

<h4>From the command line:</h4>
1. Open a terminal <br>
2. Navigate to the folder where the files are located <br>
3. On the command line execute: <br>
&nbsp &nbsp &nbsp <code>> python3 <i>script</i>.py </code> <br>
&nbsp &nbsp &nbsp <b>Notice: Replace <i>script</i> with the name of the file you want to execute e.g. PancakeFlipper.py</b> <br>

<h4>From the Python interpreter:</h4>
1. Open Python <br>
2. On the prompt execute: <br>
&nbsp &nbsp &nbsp <code>> exec(open("<i>path</i>/<i>script</i>.py").read())</code> <br>
&nbsp &nbsp &nbsp <b>Notice: Replace <i>path</i> with the local path to the folder that contains the script you want to execute</b> <br>
&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp<b>Replace <i>script</i> with the name of the file you want to execute e.g. PancakeFlipper.py</b> <br>
<br>
<h4>To use your own input files:</h4>
All input files are hardcoded, if you want to use your own input files uncomment the following lines (excluding the first line) in all files:
<br>
<pre>
# ASK USER TO ENTER PATH TO EXAMPLE FILE ON THE COMMAND LINE
#path = input("Enter path to file containing examples: ")
#path = Path (path)
#
#while (not path.is_file()):
#    path = input("\nERROR: NOT A VALID FILE PATH! \nEnter path to file containing examples: ")
#    path = Path(path)
</pre>
For the scripts to work properly all external input files should be formated following Google's Code Jam specifications.
<br>
<br>
<a href="#top">Back to Top</a> 
<br>