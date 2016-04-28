strt = int(input().strip())
end = int(input().strip())
found = 0
for i in range(strt, end + 1):
    if i == 1:
        print(1, end=" ")
    temp = str(i ** 2)
    try:
        if int(temp[:len(temp) // 2]) + int(temp[len(temp) // 2:]) == i:
            print(i, end=" ")
            found = 1
    except:
        pass
if not found:
    print("INVALID RANGE")
