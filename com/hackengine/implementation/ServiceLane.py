N, T = input().strip().split(" ")
N, T = int(N), int(T)
width = [int(x) for x in input().split(" ")]

for _ in range(T):
    x, y = input().strip().split(" ")
    len = int(y) - int(x) + 1
    bikecount, carcount, truckcount = 0, 0, 0
    for i in range(int(x), int(y) + 1):
        if width[i] >= 1:
            bikecount += 1
        if width[i] >= 2:
            carcount += 1
        if width[i] >= 3:
            truckcount += 1
    if len == bikecount:
        if len == carcount:
            if len == truckcount:
                print(3)
            else:
                print(2)
        else:
            print(1)
