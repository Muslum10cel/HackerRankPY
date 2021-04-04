#!/bin/python3

import sys

m, n = map(int, input().split(" "))
stations = [int(x) for x in input().split(" ")]
stations.sort()
if m==n:
    print(0)
else:
    maxDistance = max(stations[0],(m - stations[-1]) - 1)
    for i in range(len(stations) - 1):
        diff = abs(stations[i] - stations[i+1]) // 2
        if diff >= maxDistance:
            maxDistance = diff
    print(maxDistance)
