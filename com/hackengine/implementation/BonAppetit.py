n, k = map(int, input().split(" "))
COSTS = [int(x) for x in input().split(" ")]
c = int(input())
del COSTS[k]
if sum(COSTS) // 2 != c:
    print(c - sum(COSTS) // 2)
else:
    print("Bon Appetit")