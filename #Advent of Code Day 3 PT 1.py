#Advent of Code Day 3

file = "/home/user/Downloads/day3"
file = open(file)

sum = 0

for rucksack in file.readlines():
    containerLen = int(len(rucksack)/2)
    frontHalf = rucksack[0:containerLen]
    backHalf = rucksack[containerLen:-1]

    letterFound = False

    for frontLetter in frontHalf:
        for backLetter in backHalf:
            if frontLetter == backLetter:
                letterFound = True
                
                frontUnicode = ord(frontLetter)

                if frontUnicode > 96:
                    sum += frontUnicode - 96
                else:
                    sum += frontUnicode - 38
                break

        if letterFound == True:
            break

print(sum)
file.close()