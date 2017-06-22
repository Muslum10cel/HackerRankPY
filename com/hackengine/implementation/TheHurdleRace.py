n, k = map(int, input().split(" "))
heights = [int(x) for x in input().split(" ")]
print(max(max(heights) - k, 0))