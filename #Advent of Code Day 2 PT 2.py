#Advent of Code Day 2

file = "/home/user/Downloads/day2"
file = open(file)

# A 1 for rock
# B 2 for paper
# C 3 for scissor

# X if lost
# Y if tie
# Z if won

#Lose tie win
A = [3, 4, 8]
B = [1, 5, 9]
C = [2, 6, 7]

totalScore = 0

#Split the two plays --> Assign index value to my play (lose, tie, win) --> Use opponent's play to determine which list to look up --> Use index value to look up score for the game --> Add score to total score

for play in file.readlines():

    playerOne = play[0]
    playerTwo = play[2]

    if playerTwo == "X":
        playerTwo = 0
    elif playerTwo == "Y":
        playerTwo = 1
    elif playerTwo == "Z":
        playerTwo = 2

    if playerOne == "A":
        totalScore += A[playerTwo]
    elif playerOne == "B":
        totalScore += B[playerTwo]
    elif playerOne == "C":
        totalScore += C[playerTwo]


    print(totalScore)


file.close()