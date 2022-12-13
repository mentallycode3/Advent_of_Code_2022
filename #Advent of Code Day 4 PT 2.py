#Advent of Code Day 4

file = "/home/user/Downloads/day4"
file = open(file)

sum = 0

for pair in file.readlines():
    splitPair = pair[0:-1].split(",") #[0,-1] gets rid of /n on each line
    
    setOne = [0, 0]
    setTwo = [0, 0]

    setOneComplete = False

    for strRange in splitPair:
        strNumbers = strRange.split("-")
        
        if setOneComplete == False:
            setOne[0] = int(strNumbers[0])
            setOne[1] = int(strNumbers[1])
            setOneComplete = True
        else:
            setTwo[0] = int(strNumbers[0])
            setTwo[1] = int(strNumbers[1])

    if setOne[0] >= setTwo[0] and setOne[0] <= setTwo[1] or setOne[1] >= setTwo[0] and setOne[1] <= setTwo[1]:
        sum += 1
    elif setTwo[0] >= setOne[0] and setTwo[0] <= setOne[1] or setTwo[1] >= setOne[0] and setTwo[1] <= setOne[1]:
        sum += 1

print(sum)

file.close()