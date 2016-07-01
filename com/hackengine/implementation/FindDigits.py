test_case = int(input())

for _ in range(test_case):
    n = int(input())
    temp = n
    count = 0
    while temp != 0:
        try:
            if (n % (temp % 10)) == 0:
                count += 1
        except:
            pass
        temp //= 10
    print(count)
