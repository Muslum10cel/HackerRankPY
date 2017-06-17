n = int(input())
s = [int(x) for x in input().split(" ")]
d, m = map(int, input().split(" "))
count = i = 0
while i + m <= len(s):
    if sum(s[i:i + m]) == d:
        count += 1
    i += 1
print(count)
