n = int(input())
numbers = [int(x) for x in input().split(" ")]
left, right, equal = [], [], []
pivot = numbers[0]
for num in numbers:
    if num < pivot:
        left.append(num)
    elif num == pivot:
        equal.append(num)
    else:
        right.append(num)
print(*(left + equal + right))
