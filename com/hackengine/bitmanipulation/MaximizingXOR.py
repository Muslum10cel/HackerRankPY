L = int(input())
R = int(input())
temp = []
for i in range(L, R + 1):
    temp.append(max(map(lambda x: x ^ i, range(i, R + 1))))
print(max(temp))
