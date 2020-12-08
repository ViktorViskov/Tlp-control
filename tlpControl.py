# 
# Variables
# 

# path to file
filePath = "/etc/default/tlp"

# 
# Libs
# 

import os, sys

# 
# Functions
# 

# fistTimeStart copy and rename file to "file.d"
def firstTimeStart(fileName):
    try:
        open("%s.d" % fileName)
    except FileNotFoundError:
        os.system("cp %s %s.d" % (fileName, fileName))

# backup function
def fileBackup(fileName):
    os.system("cp %s %s.backup" % (fileName, fileName))

# take argument
def getArguments():
    # default value
    defaultValue = "800M"

    try:
        # get convert and return argument
        return toHz(sys.argv[1])
    except IndexError:
        # if not return default value
        print("You did not give argument. %s used by default." % defaultValue)
        return toHz(defaultValue)

# convertation to Hz
# for example "1.6G" = 1600000, "800M" = 800000, "200H" = 200 another type is error
def toHz(strHz):
    # default value
    defaultValue = 800000
    # if last char is G
    if strHz[len(strHz) - 1] == "G":
        hz = float(strHz[:-1]) * 1000000
    # else if last M
    elif strHz[len(strHz) - 1] == "M":
        hz = float(strHz[:-1]) * 1000
    # else if last H
    elif strHz[len(strHz) - 1] == "H":
        hz = float(strHz[:-1])
    # if incorect input
    else:
        print("Not correct format string to convertation Hz. Used default value %s hz" % defaultValue)
        hz = defaultValue
    # return value
    return int(hz)

# 
# App start
# 

# check for firststart
firstTimeStart(filePath)

# file backup
fileBackup(filePath)

# open file by line and set in arr
openedFile = open(filePath,"r")
linesFile = openedFile.readlines()

# file to write
fileToWrite = open(filePath,"w")
# new str
newStr = "%s\n" % getArguments()


# Loop for proccesing linesfile
for lineNum in range(len(linesFile)):
    # define first symb
    if linesFile[lineNum][0] != "#":
        #divide by =
        linesFile[lineNum] = linesFile[lineNum].split("=")

        # check for parametr
        if linesFile[lineNum][0] == "CPU_SCALING_MAX_FREQ_ON_BAT":
            linesFile[lineNum][1] = newStr
        
        # make again one line
        if len(linesFile[lineNum]) > 1:
            newLine = "=".join(linesFile[lineNum])
            linesFile[lineNum] = newLine

    # write file
    fileToWrite.writelines(linesFile[lineNum])

# restart tlp
os.system("tlp start")
