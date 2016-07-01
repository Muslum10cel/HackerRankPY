size = int(input().strip())
numbers = [int(x) for x in input().strip().split(" ")]
length = len(numbers)
for i in range(1, length):
    temp = numbers[i]
    index = i
    while temp < numbers[index - 1] and index - 1 >= 0:
        numbers[index - 1], numbers[index] = temp, numbers[index - 1]
        index -= 1
    print(*numbers)