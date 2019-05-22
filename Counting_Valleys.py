#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
# reverse engineer 
# Every time you return to sea level (n) after n has decreased, one valley has been travelled through

def countingValleys(n, s):
    valley_counter=0
    compare_to = n
    for letter in s:
        if letter == "U":   
            compare_to += 1
            if compare_to == n:
                valley_counter +=1
        else:
            compare_to -= 1
       
            
    return valley_counter            
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
