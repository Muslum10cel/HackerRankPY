#!/bin/python3

import os
import sys

def solve(n, operations):
    total = 0
    for operation in operations:
        a = operation[0]
        b = operation[1]
        k = operation[2]
        total += ((b-a) + 1) * k
    return total // n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    operations = []

    for _ in range(m):
        operations.append(list(map(int, input().rstrip().split())))

    result = solve(n, operations)

    fptr.write(str(result) + '\n')

    fptr.close()
