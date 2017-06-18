q = int(input())
for _ in range(q):
    A, B, C = map(int, input().split(" "))
    locA = C - A
    locB = C - B
    if abs(locA) < abs(locB):
        print("Cat A")
    elif abs(locB) < abs(locA):
        print("Cat B")
    else:
        print("Mouse C")
