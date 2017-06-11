IDS = [1, 2, 3, 4, 5]
n = int(input())
BIRDS = [int(x) for x in input().split(" ")]
counters = []
for ids in IDS:
    counters.append(BIRDS.count(ids))
print(counters.index(max(counters)) + 1)
