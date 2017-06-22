def f(fruits, s, t):
    return sum(map(lambda x, y=0: y + 1 if s <= x <= t else y, fruits))


s, t = map(int, input().split(" "))
a, b = map(int, input().split(" "))
m, n = map(int, input().split(" "))
APPLES = [int(x) + a for x in input().split(" ")]
ORANGES = [int(x) + b for x in input().split(" ")]
print(f(APPLES, s, t), f(ORANGES, s, t), sep="\n")