import os
import sys
import functools as fc

def connectingTowns(n, routes):
    return fc.reduce(lambda x,y:x*y, routes) % 1234567

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        routes = list(map(int, input().rstrip().split()))

        result = connectingTowns(n, routes)

        fptr.write(str(result) + '\n')

    fptr.close()
