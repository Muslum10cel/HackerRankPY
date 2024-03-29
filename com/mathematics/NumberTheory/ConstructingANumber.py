#!/bin/python3

import math
import os
import random
import re
import sys

def canConstruct(a):
    if sum(a) % 3 == 0:
        return "Yes"
    return "No"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        a = list(map(int, input().rstrip().split()))

        result = canConstruct(a)

        fptr.write(result + '\n')

    fptr.close()
