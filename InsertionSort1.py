size = int(input().strip())
numbers = [int(x) for x in input().strip().split(" ")]
length = len(numbers)
last = numbers[length - 1]
for i in range(2, length + 2):
    if numbers[length - i] > last and length - i >= 0:
        numbers[length - (i - 1)] = numbers[length - i]
        print(*numbers)
    else:
        numbers[length - (i - 1)] = last
        break
print(*numbers)
