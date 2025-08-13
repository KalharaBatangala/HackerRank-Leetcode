#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    valleys = 0 # no. of valleys
    
    altitude = 0   # begin at sea level
    for i in range(steps):
        if(path[i] == 'U'):
            altitude += 1   # U step up
            if(altitude == 0):
                valleys  += 1
        elif(path[i] == 'D'): 
            altitude -= 1   # D step down
    return valleys

if __name__ == '__main__':
    steps = int(input("Enter number of steps: ").strip())
    path = input("Enter path (U/D): ").strip()
    
    result = countingValleys(steps, path)
    print("Number of valleys:", result)
