import math
import os
import random
import re
import sys



# given the length of the input you need to use the methods in these libraries to determine the space between the first and last 0 while skipping 1's and 
def jumpingOnClouds(c):
    #!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    position = 0
    jumps = 0
    while position < len(c) - 2:
        if c[position + 2] != 1:
            position += 2
            jumps+= 1
    
        else:
            position +=1
            jumps += 1
    if position == len(c) - 2:
        jumps += 1

    return jumps
        



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()

