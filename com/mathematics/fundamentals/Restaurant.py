#!/bin/python3

import os
import sys

def restaurant(l, b):
    
    if l == b:
        return 1
    
    largest = max(l,b)
    gcd = 1
    for i in range(1, largest):
        if l % i == 0 and b % i == 0 and i > gcd:
            gcd = i
    return (l // gcd) * (b // gcd) 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        lb = input().split()

        l = int(lb[0])

        b = int(lb[1])

        result = restaurant(l, b)

        fptr.write(str(result) + '\n')

    fptr.close()
