n = int(input())
COLORS = [int(x) for x in input().split(" ")]
temp = list(set(COLORS))
count = 0
for item in temp:
    iCount = COLORS.count(item)
    count += (iCount // 2)
print(count)