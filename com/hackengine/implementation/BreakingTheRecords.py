n = int(input())
SCORES = [int(x) for x in input().split(" ")]
highestScore = lowestScore = SCORES[0]
highestCount = lowestCount = 0

for score in SCORES:
    if score > highestScore:
        highestScore = score
        highestCount += 1
    elif score < lowestScore:
        lowestScore = score
        lowestCount += 1

print(highestCount, lowestCount, end="\n")
