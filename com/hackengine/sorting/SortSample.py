V = int(input().strip())
n = int(input().strip())
list = [x for x in input().split(" ")]
for i in range(len(list)):
    if int(list[i]) == V:
        print(i)
        break
