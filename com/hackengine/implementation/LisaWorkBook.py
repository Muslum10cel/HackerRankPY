count, page = 0, 1
n, k = input().strip().split(' ')
n, k = int(n), int(k)
problems = [int(x) for x in input().split()]
for prob in problems:
    for p in range(prob):
        if p + 1 == page:
            count += 1
        if p + 1 % k == 0:
            page += 1
    if p % k != 0:
        page += 1
print(count)
