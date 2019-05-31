#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    if len(s) == 1 and "a" in s:
        return s.count("a") * n
    else:
        the_string = ""
        a_counter = 0
        while len(the_string) < n:
            for letter in s:
                the_string += letter
                if len(the_string) == n:
                    break
        for letter in the_string:
            if letter == "a":
                a_counter += 1
        return a_counter

    #  use count("a")
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
