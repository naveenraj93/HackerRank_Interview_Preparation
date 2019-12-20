#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    in_valley = False
    current_level = 0
    no_of_valley = 0
    for i in s:
        if i == 'U':
            current_level += 1
        else:
            current_level -= 1
        
        if current_level < 0:
            in_valley = True
        
        if in_valley and current_level == 0:
            no_of_valley += 1
            in_valley = False
    
    return(no_of_valley)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
