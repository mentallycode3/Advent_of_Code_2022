#Advent of Code Day 7

file = "/home/user/Downloads/day7"
file = open(file)

fileList = []
currentDirectory = ""

maxSize = 100000

for line in file.readlines():
    line = line[0:-1]       #Gets rid of /n

    #####Ignoring ls and dir
    if line[0] == "$":
        if line[2] == "c":
            if line[5] != ".": ##################Going deeper in to dir
                commandSplit = line.split(" ")
                currentDirectory += commandSplit[-1] + "/"

                if line[5] == "/":
                    currentDirectory = "/"
            else:      #####################Going back in dir
                cuDirectorySplit = currentDirectory.split("/")[0:-2]
                for folder in cuDirectorySplit:
                    currentDirectory = "/" + folder

                if currentDirectory != "/":
                    currentDirectory += "/"
                    
    else:
        if line[0] != "d":
            fileList.append([currentDirectory, int(line.split(" ")[0])])

fileList = sorted(fileList)

print(len(fileList))
################################################################################
compressedFiles = []

currentFolder = ""
for fileBlock in fileList:
    if fileBlock[0] != currentFolder:
        compressedFiles.append(fileBlock)
        currentFolder = fileBlock[0]
    else:
        compressedFiles[-1][1] += fileBlock[1]

print(len(compressedFiles))
################################################################################
filteredCompressed = []

for uniqueFolder in compressedFiles:
    if uniqueFolder[1] <= maxSize:
        filteredCompressed.append(uniqueFolder)
print(len(filteredCompressed))
################################################################################


sum = 0

for uniqueFolderIndex in reversed(range(len(filteredCompressed))):
    currentParent = filteredCompressed[uniqueFolderIndex][0].split("/")[1]
    nextParent = ""

    if uniqueFolderIndex != 0:
        nextParent = filteredCompressed[uniqueFolderIndex - 1][0].split("/")[1]

    if currentParent != nextParent or uniqueFolderIndex == 0:
        if filteredCompressed[uniqueFolderIndex][1] <= maxSize:
            sum += filteredCompressed[uniqueFolderIndex][1]
    else:
        filteredCompressed[uniqueFolderIndex - 1][1] += filteredCompressed[uniqueFolderIndex][1]
        sum += filteredCompressed[uniqueFolderIndex][1]



# for each in filteredCompressed:
#     print(each)

file.close()