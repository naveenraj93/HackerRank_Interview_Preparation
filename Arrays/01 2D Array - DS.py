#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    sumList = []

    for i in range(0,4):
        
        for j in range(0,4):
            sum = 0
    #        print( (i,j), (i,(j + 1)),(i,(j + 2)))
    #        print( i + 1,(j + 1))
    #        print( (i + 2,j), (i + 2,(j + 1)),((i + 2),(j + 2)))
    #        print(arr[i][j],arr[i][j + 1],arr[i][j + 2])
    #        print(' ',arr[i + 1][j + 1],' ')
    #        print(arr[i + 2][j ],arr[i + 2][j + 1],arr[i + 2][j + 2])
            sum += arr[i][j]  + arr[i][j + 1] + arr[i][j + 2]
            sum += arr[i + 1][j + 1]
            sum +=  arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2 ][j + 2]
    #        print(sum)
            sumList.append(sum)

    return(max(sumList))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
