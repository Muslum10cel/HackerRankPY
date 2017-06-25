def f(totalpage):
    return sum(map(lambda x, y=0: y + 1 if x % 2 == 0 else 0, range(1, totalpage + 1)))


def g(totalpage, desiredpage):
    if n % 2 == 0:
        return sum(map(lambda x, y=0: y + 1 if x % 2 == 0 else 0, range(totalpage, desiredpage, -1)))
    else:
        return sum(map(lambda x, y=0: y + 1 if x % 2 == 1 else 0, range(totalpage - 1, desiredpage - 1, -1)))


n = int(input())
p = int(input())
print(min(f(p), g(n, p)))
