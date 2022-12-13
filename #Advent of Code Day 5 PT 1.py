#Advent of Code Day 5

file = "/home/user/Downloads/day5"
file = open(file)

lineBuffer = []
stack = []

instructionBuffer = []

result = ""

#Loads stack and instructions in lists
for line in file.readlines():
    lineBuffer.append(line[0:-1])

foundEnd = False

for instruction in reversed(lineBuffer):
    if instruction != "" and instruction[1] != "1" and foundEnd == False:
        instructionBuffer.insert(0, instruction)
        lineBuffer.pop()
    else:
        foundEnd = True

lineBuffer.pop()
lineBuffer.pop()

#Initialize each block to correct stack
for line in reversed(lineBuffer):
    currentPosition = 0

    #Establish the list
    if stack == []:
        for letter in line:
            if ord(letter) < 91 and ord(letter) > 34:
                stack.append([])

    for index in range(len(line)):
        if ord(line[index]) < 91 and ord(line[index]) > 34:
            stack[int(index/4)].append(line[index])


#Interprets instructions
for instruction in instructionBuffer:
    breakdown = instruction.split(" ") #numbers are in one three and five

    times = int(breakdown[1])
    start = int(breakdown[3])
    end = int(breakdown[5])

    for x in range(times):
        stack[end - 1].append(stack[start - 1][-1])
        stack[start - 1].pop()

for indStack in stack:
    result += indStack[-1]

print(result)
    
file.close()