# 
# app for compare files
# 

# file one
fileOne = open("./tlp.d", "r")
textOne = fileOne.read()

# file two
fileTwo = open("./tlp", "r")
textTwo = fileTwo.read()

# variable for errors
errors = 0

# loop fo checking symbols
for charNum in range(len(textTwo)):
    if textOne[charNum] != textTwo[charNum]:
        print(textTwo[charNum])
        errors += 1
        if errors == 20:
            break

# print errors
print(errors)