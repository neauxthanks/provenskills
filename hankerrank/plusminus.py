#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below. an 
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    
    #set up variables
    cycle = [0,0,0]
    
    #move pointer along and keep count
    for x in range(len(arr)):
        if arr[x] > 0:
            cycle[0] += 1 #pos
        elif arr[x] < 0:
            cycle[1] += 1 # neg
        else:
            cycle[2] += 1 #zero
    
    for y in range(3):
        next_value = cycle[y]/len(arr)
        formatted_string = "{:.6f}".format(next_value)
        float_value = float(formatted_string)
        print(float_value)
    
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
