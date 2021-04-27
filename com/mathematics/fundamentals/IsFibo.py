#!/bin/python3

import math
import os
import random
import re
import sys

def isFibo(n):
    # Write your code here
    a, b , c = 0, 1, 0
    while c<=n:
        c = a+b
        a, b = b, c
        if c == n:
            return "IsFibo"
    else:
        return "IsNotFibo"
            
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = isFibo(n)

        fptr.write(result + '\n')

    fptr.close()
