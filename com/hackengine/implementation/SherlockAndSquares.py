import math

test_case = int(input())

for _ in range(test_case):
    a_b = [int(x) for x in input().split()]
    print((math.floor(math.sqrt(a_b[1])) - math.ceil(math.sqrt(a_b[0])) + 1))
