#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
# get the set and then get the count of each value in the set.
# if the value of the count is odd, take one from the value and divide by two. If its even just divide by two. 
# add the values 
def sockMerchant(n, ar):
    socks = [num for num in set(ar)]
    add_these = []
    for num in socks:
        if ar.count(num) % 2 == 0:
            add_these.append(ar.count(num) // 2)
        else:
            add_these.append((ar.count(num)- 1) // 2)
    return sum(add_these)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
