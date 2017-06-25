from collections import deque

n, k, q = map(int, input().split(" "))
ls = [int(x) for x in input().split(" ")]
dq = deque(ls)
dq.rotate(k)
for _ in range(q):
    print(dq[int(input())])