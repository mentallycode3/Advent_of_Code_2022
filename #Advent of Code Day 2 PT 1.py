#Advent of Code Day 2

file = "/home/user/Downloads/day2"
file = open(file)

# A X 1 for rock
# B Y 2 for paper
# C Z 3 for scissor

# 0 if lost
# 3 if tie
# 6 if won

#Score table
A = [3, 6, 0]
B = [0, 3, 6]
C = [6, 0, 3]


totalScore = 0

#Split the two plays --> Assign the score value to my response (used to determine part of score and to use for index for score look up) --> Determine what opponent play was --> Use the opponents play to determine score lookup table using my score as the index --> Add scores

for play in file.readlines():
    currentScore = 0

    playerOne = play[0]
    playerTwo = play[2]

    if playerTwo == "X":
        playerTwo = 1
    elif playerTwo == "Y":
        playerTwo = 2
    elif playerTwo == "Z":
        playerTwo = 3

    if playerOne == "A":
        totalScore += A[playerTwo - 1]
    elif playerOne == "B":
        totalScore += B[playerTwo - 1]
    elif playerOne == "C":
        totalScore += C[playerTwo - 1]

    totalScore += playerTwo
    print(totalScore)


file.close()