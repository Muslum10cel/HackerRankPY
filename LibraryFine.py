da, ma, ya = input().split(" ")
de, me, ye = input().split(" ")
D = int(da) - int(de)
M = int(ma) - int(me)
Y = int(ya) - int(ye)

if Y < 0:
    print(0)
elif Y == 0:
    if M < 0:
        print(0)
    elif M == 0:
        if D <= 0:
            print(0)
        else:
            print(15 * D)
    else:
        print(500 * M)
else:
    print(10000)
