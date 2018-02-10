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
<i>The challenge <b><a href="https://code.google.com/codejam/contest/3264486/dashboard#s=p0">click here to read the full challenge at Google's Code Jam website</a></b></i> <br>
<i>Solution Script <b>PancakeFlipper.py</b> </i> <a href="https://github.com/yogurt1989/Google-Code-Jam/blob/master/2017/PancakeFlipper.py" target="_blank">(view)</a> <br>
<h4>My Solution</h4>
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

<h4>The Problem</h4>
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sed auctor turpis. Nullam id varius nisl. Sed mattis ullamcorper augue, quis scelerisque quam varius vel. Curabitur sit amet nulla rutrum, mollis odio id, imperdiet tortor. Curabitur euismod vehicula diam a ultricies. Pellentesque iaculis varius aliquet. Nullam vitae felis a risus imperdiet laoreet. Integer scelerisque nec nibh in vulputate. Nulla facilisi. Sed quis sapien nisl. Nam commodo leo vestibulum tellus cursus, a mollis quam egestas. Sed sodales feugiat lorem vel faucibus. In hac habitasse platea dictumst.

Pellentesque id commodo arcu. Vestibulum pharetra dui ac turpis suscipit, in iaculis velit venenatis. Fusce ut magna iaculis, varius neque in, viverra nisi. Suspendisse rutrum nibh a consequat efficitur. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Vestibulum lobortis non nunc et vulputate. Donec hendrerit dui ut dui placerat volutpat. Sed egestas a elit vitae tincidunt. Donec et elit nisl. Vivamus placerat ligula ac tellus dictum malesuada.

Phasellus ac nisl vitae ipsum condimentum convallis. Curabitur ipsum eros, aliquam sit amet posuere ac, luctus a magna. In sed hendrerit ex. Mauris faucibus velit a magna ultrices, a iaculis sem ultrices. Vestibulum fermentum tellus eu augue consectetur commodo. Quisque eget lobortis felis. In bibendum convallis nisl bibendum dignissim. Nunc eget ante in tortor porttitor maximus vel quis nunc. Curabitur neque odio, dapibus non convallis eget, placerat eu orci. Cras id porta mi. Integer condimentum mauris elit, vel consequat justo eleifend vitae. Nulla congue lorem arcu, eget ultrices dolor sollicitudin in.

<h4>My Solution</h4>
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sed auctor turpis. Nullam id varius nisl. Sed mattis ullamcorper augue, quis scelerisque quam varius vel. Curabitur sit amet nulla rutrum, mollis odio id, imperdiet tortor. Curabitur euismod vehicula diam a ultricies. Pellentesque iaculis varius aliquet. Nullam vitae felis a risus imperdiet laoreet. Integer scelerisque nec nibh in vulputate. Nulla facilisi. Sed quis sapien nisl. Nam commodo leo vestibulum tellus cursus, a mollis quam egestas. Sed sodales feugiat lorem vel faucibus. In hac habitasse platea dictumst.

Pellentesque id commodo arcu. Vestibulum pharetra dui ac turpis suscipit, in iaculis velit venenatis. Fusce ut magna iaculis, varius neque in, viverra nisi. Suspendisse rutrum nibh a consequat efficitur. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Vestibulum lobortis non nunc et vulputate. Donec hendrerit dui ut dui placerat volutpat. Sed egestas a elit vitae tincidunt. Donec et elit nisl. Vivamus placerat ligula ac tellus dictum malesuada.

Phasellus ac nisl vitae ipsum condimentum convallis. Curabitur ipsum eros, aliquam sit amet posuere ac, luctus a magna. In sed hendrerit ex. Mauris faucibus velit a magna ultrices, a iaculis sem ultrices. Vestibulum fermentum tellus eu augue consectetur commodo. Quisque eget lobortis felis. In bibendum convallis nisl bibendum dignissim. Nunc eget ante in tortor porttitor maximus vel quis nunc. Curabitur neque odio, dapibus non convallis eget, placerat eu orci. Cras id porta mi. Integer condimentum mauris elit, vel consequat justo eleifend vitae. Nulla congue lorem arcu, eget ultrices dolor sollicitudin in.<br>
<br>
<a href="#top">Back to Top</a> 
<br>
<hr>
<h3 id="potty">Bathroom Stalls</h3>
<i>Script <b>BathroomStalls.py</b></i>

<h4>The Problem</h4>
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sed auctor turpis. Nullam id varius nisl. Sed mattis ullamcorper augue, quis scelerisque quam varius vel. Curabitur sit amet nulla rutrum, mollis odio id, imperdiet tortor. Curabitur euismod vehicula diam a ultricies. Pellentesque iaculis varius aliquet. Nullam vitae felis a risus imperdiet laoreet. Integer scelerisque nec nibh in vulputate. Nulla facilisi. Sed quis sapien nisl. Nam commodo leo vestibulum tellus cursus, a mollis quam egestas. Sed sodales feugiat lorem vel faucibus. In hac habitasse platea dictumst.

Pellentesque id commodo arcu. Vestibulum pharetra dui ac turpis suscipit, in iaculis velit venenatis. Fusce ut magna iaculis, varius neque in, viverra nisi. Suspendisse rutrum nibh a consequat efficitur. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Vestibulum lobortis non nunc et vulputate. Donec hendrerit dui ut dui placerat volutpat. Sed egestas a elit vitae tincidunt. Donec et elit nisl. Vivamus placerat ligula ac tellus dictum malesuada.

Phasellus ac nisl vitae ipsum condimentum convallis. Curabitur ipsum eros, aliquam sit amet posuere ac, luctus a magna. In sed hendrerit ex. Mauris faucibus velit a magna ultrices, a iaculis sem ultrices. Vestibulum fermentum tellus eu augue consectetur commodo. Quisque eget lobortis felis. In bibendum convallis nisl bibendum dignissim. Nunc eget ante in tortor porttitor maximus vel quis nunc. Curabitur neque odio, dapibus non convallis eget, placerat eu orci. Cras id porta mi. Integer condimentum mauris elit, vel consequat justo eleifend vitae. Nulla congue lorem arcu, eget ultrices dolor sollicitudin in.

<h4>My Solution</h4>
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sed auctor turpis. Nullam id varius nisl. Sed mattis ullamcorper augue, quis scelerisque quam varius vel. Curabitur sit amet nulla rutrum, mollis odio id, imperdiet tortor. Curabitur euismod vehicula diam a ultricies. Pellentesque iaculis varius aliquet. Nullam vitae felis a risus imperdiet laoreet. Integer scelerisque nec nibh in vulputate. Nulla facilisi. Sed quis sapien nisl. Nam commodo leo vestibulum tellus cursus, a mollis quam egestas. Sed sodales feugiat lorem vel faucibus. In hac habitasse platea dictumst.

Pellentesque id commodo arcu. Vestibulum pharetra dui ac turpis suscipit, in iaculis velit venenatis. Fusce ut magna iaculis, varius neque in, viverra nisi. Suspendisse rutrum nibh a consequat efficitur. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Vestibulum lobortis non nunc et vulputate. Donec hendrerit dui ut dui placerat volutpat. Sed egestas a elit vitae tincidunt. Donec et elit nisl. Vivamus placerat ligula ac tellus dictum malesuada.

Phasellus ac nisl vitae ipsum condimentum convallis. Curabitur ipsum eros, aliquam sit amet posuere ac, luctus a magna. In sed hendrerit ex. Mauris faucibus velit a magna ultrices, a iaculis sem ultrices. Vestibulum fermentum tellus eu augue consectetur commodo. Quisque eget lobortis felis. In bibendum convallis nisl bibendum dignissim. Nunc eget ante in tortor porttitor maximus vel quis nunc. Curabitur neque odio, dapibus non convallis eget, placerat eu orci. Cras id porta mi. Integer condimentum mauris elit, vel consequat justo eleifend vitae. Nulla congue lorem arcu, eget ultrices dolor sollicitudin in.<br>
<br>
<a href="#top">Back to Top</a> 
<br>
<hr>
<h3 id="fashion">Fashion Show</h3>
<i>Script <b>FashionShow.py</b></i>

<h4>The Problem</h4>
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sed auctor turpis. Nullam id varius nisl. Sed mattis ullamcorper augue, quis scelerisque quam varius vel. Curabitur sit amet nulla rutrum, mollis odio id, imperdiet tortor. Curabitur euismod vehicula diam a ultricies. Pellentesque iaculis varius aliquet. Nullam vitae felis a risus imperdiet laoreet. Integer scelerisque nec nibh in vulputate. Nulla facilisi. Sed quis sapien nisl. Nam commodo leo vestibulum tellus cursus, a mollis quam egestas. Sed sodales feugiat lorem vel faucibus. In hac habitasse platea dictumst.

Pellentesque id commodo arcu. Vestibulum pharetra dui ac turpis suscipit, in iaculis velit venenatis. Fusce ut magna iaculis, varius neque in, viverra nisi. Suspendisse rutrum nibh a consequat efficitur. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Vestibulum lobortis non nunc et vulputate. Donec hendrerit dui ut dui placerat volutpat. Sed egestas a elit vitae tincidunt. Donec et elit nisl. Vivamus placerat ligula ac tellus dictum malesuada.

Phasellus ac nisl vitae ipsum condimentum convallis. Curabitur ipsum eros, aliquam sit amet posuere ac, luctus a magna. In sed hendrerit ex. Mauris faucibus velit a magna ultrices, a iaculis sem ultrices. Vestibulum fermentum tellus eu augue consectetur commodo. Quisque eget lobortis felis. In bibendum convallis nisl bibendum dignissim. Nunc eget ante in tortor porttitor maximus vel quis nunc. Curabitur neque odio, dapibus non convallis eget, placerat eu orci. Cras id porta mi. Integer condimentum mauris elit, vel consequat justo eleifend vitae. Nulla congue lorem arcu, eget ultrices dolor sollicitudin in.

<h4>My Solution</h4>
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sed auctor turpis. Nullam id varius nisl. Sed mattis ullamcorper augue, quis scelerisque quam varius vel. Curabitur sit amet nulla rutrum, mollis odio id, imperdiet tortor. Curabitur euismod vehicula diam a ultricies. Pellentesque iaculis varius aliquet. Nullam vitae felis a risus imperdiet laoreet. Integer scelerisque nec nibh in vulputate. Nulla facilisi. Sed quis sapien nisl. Nam commodo leo vestibulum tellus cursus, a mollis quam egestas. Sed sodales feugiat lorem vel faucibus. In hac habitasse platea dictumst.

Pellentesque id commodo arcu. Vestibulum pharetra dui ac turpis suscipit, in iaculis velit venenatis. Fusce ut magna iaculis, varius neque in, viverra nisi. Suspendisse rutrum nibh a consequat efficitur. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Vestibulum lobortis non nunc et vulputate. Donec hendrerit dui ut dui placerat volutpat. Sed egestas a elit vitae tincidunt. Donec et elit nisl. Vivamus placerat ligula ac tellus dictum malesuada.

Phasellus ac nisl vitae ipsum condimentum convallis. Curabitur ipsum eros, aliquam sit amet posuere ac, luctus a magna. In sed hendrerit ex. Mauris faucibus velit a magna ultrices, a iaculis sem ultrices. Vestibulum fermentum tellus eu augue consectetur commodo. Quisque eget lobortis felis. In bibendum convallis nisl bibendum dignissim. Nunc eget ante in tortor porttitor maximus vel quis nunc. Curabitur neque odio, dapibus non convallis eget, placerat eu orci. Cras id porta mi. Integer condimentum mauris elit, vel consequat justo eleifend vitae. Nulla congue lorem arcu, eget ultrices dolor sollicitudin in.
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