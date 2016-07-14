x1, v1, x2, v2 = map(int, input().split(" "))
t = 1
for _ in range(10001):
    if x1 + (v1 * t) == x2 + (v2 * t):
        print("YES")
        break
    t += 1
else:
    print("NO")
