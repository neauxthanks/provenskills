#!/bin/python3

import math
import os
import random
import re
import sys

#PASSED

def timeConversion(s):
    # Write your code here
    # Detect if AM or PM

    twentyfour = ""
    if s[8] == 'P':
        day = False
        hour = s[0:2]
        calculation = (int)(hour)
        calculation += 12
        if calculation == 24:
            hour == "00"
        else:
            hour = str(calculation)
        twentyfour = hour + s[2:8]
    else: 
        if (s[0] =='1'):
            twentyfour = "00" + s[2:8]
        else:
            twentyfour = s[0:8]
    return twentyfour[0:8]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
