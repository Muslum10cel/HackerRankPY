s = input()
t = len(s) // 3 * "SOS"
count = 0
for i in range(0, len(s)):
    if s[i] != t[i]:
        count += 1
print(count)