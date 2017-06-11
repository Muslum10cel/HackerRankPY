s, t = map(int, input().split(" "))
a, b = map(int, input().split(" "))
m, n = map(int, input().split(" "))
APPLES = [int(x) + a for x in input().split(" ")]
ORANGES = [int(x) + b for x in input().split(" ")]
appleCount, orangeCount = 0, 0

for apple in APPLES:
    if s <= apple <= t:
        appleCount += 1
for orange in ORANGES:
    if s <= orange <= t:
        orangeCount += 1

print(appleCount)
print(orangeCount)
