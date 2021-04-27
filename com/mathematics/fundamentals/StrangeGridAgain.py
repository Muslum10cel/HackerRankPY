#!/bin/python3

import os
import sys

def strangeGrid(r, c):
    if r % 2 == 0:
        return (((r // 2) - 1) * 10) + [1,3,5,7,9][c-1]
    else:
        return ((r // 2) * 10) + [0,2,4,6,8][c-1] 
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    rc = input().split()

    r = int(rc[0])

    c = int(rc[1])

    result = strangeGrid(r, c)

    fptr.write(str(result) + '\n')

    fptr.close()
