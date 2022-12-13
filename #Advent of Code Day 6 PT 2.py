#Advent of Code Day 6

file = "/home/user/Downloads/day6"
file = open(file)
text = file.readlines()[0][0:-1]

markerFound = False
currentLetter = 0
marker = ["","","",""]

scannerStep = len(text) - 3

for step in range(scannerStep):
    scanningBlock = text[step:step + 14]
    sortedBlock = []

    for letter in scanningBlock:
        sortedBlock.append(letter)

    sortedBlock.sort()
    
    sameFound = False

    for index in range(1,len(sortedBlock)):
        if sortedBlock[index] == sortedBlock[index - 1]:
            sameFound = True

    if sameFound == False:
        print("Step: " + str(step + 14))
        break

    marker = ["","","",""]


file.close()