#!/bin/python3

import math
import os
import random
import re
import sys

#PASSED

def miniMaxSum(arr):
    # Write your code here
    min = arr[0]
    max = 0
    sum = 0
    for x in range(5):
        sum += arr[x] 
        if arr[x] <= min:
            min = arr[x]
        elif arr[x] > max:
            max = arr[x]
    
    mini = sum - max
    maxi = sum - min
    
    print(str(mini) + " " + str(maxi))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
