#Advent of Code Day 1

file = "/home/user/Downloads/day1"
file = open(file)

highest = [0, 0, 0]
currentTotal = 0

#If not an empty line then add calories to currentTotal --> once an empty line is reached if the current Value is higher than the first value in the list then replace it and then sort list from highest to lowest --> Reset currentTotal to 0 --> loop

for calories in file.readlines():
    if calories != '\n':
        currentTotal += int(calories)
    else:
        if currentTotal > highest[0]:
            highest[0] = currentTotal

        highest = sorted(highest)
        currentTotal = 0

print(highest[0] + highest[1] + highest[2])

file.close()