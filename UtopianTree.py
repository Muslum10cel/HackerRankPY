test_case = int(input())

for _ in range(test_case):
    n = int(input())
    if n == 0:
        print("1")
    elif n == 1:
        print("2")
    else:
        initial = 1
        for i in range(n):
            if (i + 1) % 2 == 0:
                initial += 1
            else:
                initial *= 2
        print(initial)
