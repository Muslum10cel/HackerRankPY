N, M = map(int, input().split(" "))
teams = []
maxTopics = []
count = 0
for _ in range(N):
    teams.append(input())

for i in range(len(teams)):
    for j in range(i, len(teams)):
        maxTopics.append(str(bin(int(teams[i], 2) | int(teams[j], 2))).count("1"))

count = max(maxTopics)
print(count, maxTopics.count(count), sep="\n")