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
<br>
More <br>
<a href="#help">Instructions to run the programs</a> <br>
<a href="https://github.com/yogurt1989/Google-Code-Jam">Go Back</a>

<br>
<hr>
<h3 id="pancake">Pancake Flipper</h3>
<i>Script <b>PancakeFlipper.py</b></i>

<h5>The Problem</h5>
The first exercise we chose was the Pancake Flipper. We used Python library to iterate the file containing
all samples. We saved the first line on the file, that contains the number of samples, in a variable
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
A variable containing the size of the pancake row is used to avoid and index out of bound error. Every
time a flip occurs the counter flips increases by 1. If there is a lock or an infinite loop, the flag impossible
is assigned a value True, that will determine if the final string returned by the function is the string
“IMPOSSIBLE” or the counter flips casted as a string.


<h5>My Solution</h5>
The first exercise we chose was the Pancake Flipper. We used Python library to iterate the file containing
all samples. We saved the first line on the file, that contains the number of samples, in a variable
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
A variable containing the size of the pancake row is used to avoid and index out of bound error. Every
time a flip occurs the counter flips increases by 1. If there is a lock or an infinite loop, the flag impossible
is assigned a value True, that will determine if the final string returned by the function is the string
“IMPOSSIBLE” or the counter flips casted as a string.
<br>
<br>
<a href="#top">Back to Top</a> 
<br>
<hr>
<h3 id="numbers">Tidy Numbers</h3>
<i>Script <b>TidyNumbers.py</b></i>

<h5>The Problem</h5>
The first exercise we chose was the Pancake Flipper. We used Python library to iterate the file containing
all samples. We saved the first line on the file, that contains the number of samples, in a variable
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
A variable containing the size of the pancake row is used to avoid and index out of bound error. Every
time a flip occurs the counter flips increases by 1. If there is a lock or an infinite loop, the flag impossible
is assigned a value True, that will determine if the final string returned by the function is the string
“IMPOSSIBLE” or the counter flips casted as a string.


<h5>My Solution</h5>
The first exercise we chose was the Pancake Flipper. We used Python library to iterate the file containing
all samples. We saved the first line on the file, that contains the number of samples, in a variable
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
A variable containing the size of the pancake row is used to avoid and index out of bound error. Every
time a flip occurs the counter flips increases by 1. If there is a lock or an infinite loop, the flag impossible
is assigned a value True, that will determine if the final string returned by the function is the string
“IMPOSSIBLE” or the counter flips casted as a string.
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

<h5>From the command line:</h5>
1. Open a terminal <br>
2. Navigate to the folder where the files are located <br>
3. On the command line execute: <br>
&nbsp &nbsp &nbsp <code>> python3 <i>script</i>.py </code> <br>
&nbsp &nbsp &nbsp <b>Notice: Replace <i>script</i> with the name of the file you want to execute e.g. PancakeFlipper.py</b> <br>

<h5>From the Python interpreter:</h5>
1. Open Python <br>
2. On the prompt execute: <br>
&nbsp &nbsp &nbsp <code>> exec(open("<i>path</i>/<i>script</i>.py").read())</code> <br>
&nbsp &nbsp &nbsp <b>Notice: Replace <i>path</i> with the local path to the folder that contains the script you want to ezecute</b> <br>
&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp<b>Replace <i>script</i> with the name of the file you want to execute e.g. PancakeFlipper.py</b> <br>

<br>
<a href="#top">Back to Top</a> 
<br>