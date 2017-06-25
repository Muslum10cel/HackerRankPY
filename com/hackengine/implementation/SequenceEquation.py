n = int(input())
p = dict(zip(range(1, n + 1), [int(x) for x in input().split(" ")]))
for i in range(1, n + 1):
    for value in p.values():
        if i == value:
            for key in p.keys():
                if p[p[key]] == i:
                    print(key)