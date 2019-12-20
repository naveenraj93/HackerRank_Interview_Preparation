# Enter your code here. Read input from STDIN. Print output to STDOUT

noOfClouds = int(input())
cloudArr = input().split()
noOfJump = 0
currentCloud = 0
i = 1
twoPlaceFlag= 1


while i < noOfClouds:
    twoPlaceFlag += 1
    
    if currentCloud == i:
        pass
    elif cloudArr[i] == '0':
        if twoPlaceFlag == 2:
            noOfJump += 1
            twoPlaceFlag = 0
        currentCloud += 1
    else:
        noOfJump += 1
        currentCloud += 2
        twoPlaceFlag = 0
    #print(cloudArr[i],i,noOfJump,currentCloud)
    i+= 1

print(noOfJump)
