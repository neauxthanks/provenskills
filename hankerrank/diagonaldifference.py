#!/bin/python3

import math
import os
import random
import re
import sys

# PASSED

def diagonalDifference(arr):
    # Write your code here
    # tried this recursively but that was overkill tbh
    up = 0
    down = 0
    
    for x in range(len(arr)):
        up += arr[x][x]
        down += arr[len(arr)-1-x][x]
    
    return abs(up-down)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
