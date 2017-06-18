n = int(input())
s = input()
valley = seaLevel = 0
for step in s:
    if step == "U":
        seaLevel += 1
    elif step == "D":
        seaLevel -= 1
        if seaLevel == -1:
            valley += 1
print(valley)
