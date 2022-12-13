#Advent of Code Day 3

file = "/home/user/Downloads/day3"
file = open(file)

group = ["","",""]

lineCounter = 0
sum = 0

for rucksack in file.readlines():
    group[lineCounter] = rucksack[0:-1]
    lineCounter += 1

    if lineCounter == 3:
        threeFound = False

        for firstLetter in group[0]:
            for secondLetter in group[1]:
                if firstLetter == secondLetter:
                    for thirdLetter in group[2]:
                        if firstLetter == thirdLetter:
                            threeFound = True
                            frontUnicode = ord(firstLetter)
                            if frontUnicode > 96:
                                sum += frontUnicode - 96
                            else:
                                sum += frontUnicode - 38
                            break
                if threeFound == True:
                    break
            if threeFound == True:
                break
        
        lineCounter = 0
        group = ["","",""]

print(sum)
file.close()