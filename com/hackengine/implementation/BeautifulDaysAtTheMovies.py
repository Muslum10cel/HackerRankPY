i, j, k = map(int, input().split(" "))
print(sum(map(lambda x, y=0: y + 1 if abs(x - (int((str(x)[::-1])))) % k == 0 else 0, range(i, j + 1))))
