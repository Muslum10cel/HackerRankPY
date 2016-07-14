aliceCount, bobCount = 0, 0
ALICE = [int(x) for x in input().split(" ")]
BOB = [int(x) for x in input().split(" ")]
for i in range(len(ALICE)):
    if ALICE[i] > BOB[i]:
        aliceCount += 1
    elif BOB[i] > ALICE[i]:
        bobCount += 1
print(aliceCount, bobCount)
