t = int(input())
first, count = 2, 0
for _ in range(1, t + 1):
    count += first
    first = first * 3 // 2
print(count)
