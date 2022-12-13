#Advent of Code Day 1

file = "/home/user/Downloads/day1"
file = open(file)

highestTotal = 0
currentTotal = 0

for calories in file.readlines():
    if calories != '\n':
        currentTotal += int(calories)
    else:
        if currentTotal > highestTotal:
            highestTotal = currentTotal
        currentTotal = 0

print(highestTotal)

file.close()