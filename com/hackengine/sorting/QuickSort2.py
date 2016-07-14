left, right = [], []


def leftside(ls):
    pivot = ls[0]
    for num in ls:
        if num < pivot:
            left.append(num)
    print(*left)


def rightside(ls):
    pivot = ls[0]
    for num in ls:
        if num > pivot:
            right.append(num)
    print(*right)

size = int(input())
numbers = [int(x) for x in input().split(" ")]
leftside(numbers)
rightside(numbers)