import math

T = int(input())
for _ in range(T):
    K = int(input())
    if K % 2 == 0:
        print(K // 2 * K // 2)
    else:
        print((math.ceil(K / 2) * math.floor(K / 2)))