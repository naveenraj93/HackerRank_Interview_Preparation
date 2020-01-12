#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    enumValue = [*enumerate(arr)]
    enumValue.sort(key = lambda t: t[1])

    count = 0
    i = 0
    while i < len(arr):
        if i == enumValue[i][0]:
            i += 1
            continue
        tmp = enumValue[i][0]
        enumValue[i], enumValue[tmp] = enumValue[tmp], enumValue[i]
        count += 1 
    
    return(count)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
