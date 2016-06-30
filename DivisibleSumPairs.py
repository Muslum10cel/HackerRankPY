n, k = input().split(" ")
n, k = int(n), int(k)
count = 0
numbers = [int(x) for x in input().strip().split(" ")]
for x in range(0, len(numbers)):
    for y in range(0, len(numbers)):
        if x < y and (numbers[x] + numbers[y]) % k == 0:
            count += 1
print(count)
