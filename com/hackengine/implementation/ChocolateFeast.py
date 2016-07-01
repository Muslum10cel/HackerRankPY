list = []
test_case = int(input())

for _ in range(test_case):
    n, c, m = input().strip().split(' ')
    n, c, m = int(n), int(c), int(m)
    if n / c < m:
        list.append(n / c)
    elif n / c == m:
        list.append(n / c + 1)
    else:
        count = 0
        temp = n / c
        while temp >= m:
            temp -= m
            temp += 1
            count += 1
        list.append(n / c + count)

for item in list:
    print(int(item))
