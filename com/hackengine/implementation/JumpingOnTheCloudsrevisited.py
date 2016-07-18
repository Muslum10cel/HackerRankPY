n, k = map(int, input().split(" "))
clouds = [int(x) for x in input().split(" ")]
E = 100
for i in range(0, n, k):
    if clouds[i] == 0:
        E -= 1
    else:
        E -= 3
print(E)
