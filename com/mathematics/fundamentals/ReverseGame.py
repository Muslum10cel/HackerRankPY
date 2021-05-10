import math
import os
import random
import re
import sys



if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n, k  = map(int, input().split(" "))
        numbers = []
        
        a = n - 1
        b = 0
        for i in range(n):
            if i % 2 == 0:
                numbers.append(a)
                a -= 1
            else:
                numbers.append(b)
                b += 1
        print(numbers.index(k))
