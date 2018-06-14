import os, time
import win32clipboard

# Path to the file to monitor
PATHTOLOGFILE = r'C:\Users\Lab\James\CO2RES'

""" This program is designed to help out when running GC-TCD for CO2-Air cylinders.
If the script is running while GC samples are being done, it will automatically
calculate the nitrogen (balance) value for CO2-Air samples and copy that number
to the clipboard, so it can easily be pasted into Peaksimple to bring total gas
composition to 100%. """

def copy_str_to_clipboard(string):
    # Open the clipboard for examination, e.g. to read or write to it
    win32clipboard.OpenClipboard()
    # Set the clipboard contents to 'string'. 13 is the encoding (unicode). Can now
    # paste the data right into Peaksimple
    success = win32clipboard.SetClipboardText(string, 13)
    # Close the clipboard so other applications can work with it
    win32clipboard.CloseClipboard()


twoValues = [[],[]]
while 1:
    fileChanged = False
    # os.stat gets some info about a file. os.stat.st_mtime is the time of the
    # last edit of the file. So we check the time since last edit twice,
    # separated by 0.1 seconds. If the time changes, it was edited, and we
    # proceed.
    twoValues[0] = os.stat(PATHTOLOGFILE).st_mtime
    time.sleep(0.1)
    twoValues[1] = os.stat(PATHTOLOGFILE).st_mtime

    # If the 2 'polls' are different, set flag 'fileChanged' to True
    if twoValues[1] != twoValues[0]:
        fileChanged = True

    # If the file has changed, begin the small amt. of processing on the data
    if fileChanged:
        # Open log file, read it into 'lines'
        file = open(PATHTOLOGFILE)
        lines = file.readlines()
        # Get CO2 value as a float
        co2Line = lines[21].split()
        co2Line2 = co2Line[2].split(',')
        co2Value = float(co2Line2[3])
        # Get O2 value as a float
        o2Line = lines[22].split()
        o2Line2 = o2Line[1].split(',')
        o2Value = float(o2Line2[6])

        # Calculate what the N2 value should be
        n2Val = str(round(100.0000 - co2Value - o2Value, 4))
        print(f"Calibrate N2 to: {n2Val} \nCopied to Clipboard!")

        # Do the copying
        copy_str_to_clipboard(n2Val)

