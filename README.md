# quick-script
Using the win32clipboard module to automate a boring task.

A task I have to do at work involves getting 2 numeric values from a program (Peaksimple), and subtracting them from 100 to get a 
third value, which then has to be entered back into Peaksimple. This has to be done over and over again. Originally, I'd have to 
do it manually by opening up the calculator for each run and calculating the value, then typing it into Peaksimple. So instead of 
all that nonsense, I wrote this script.

Peaksimple dumps the generated data into a log file when it's done with the run. This script polls the file's directory every 0.1 seconds. The polling is done using os.stat(), which returns the time of the last edit of the file.
If the file was updated, some processing is done on the data (100 - x - y = z). Z is then copied to the Windows clipboard using 
win32clipboard.SetClipboardText(). I can then paste the value into Peaksimple without having to do anything. Little time savers like this is one of the main reasons why I love python so much.
