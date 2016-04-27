T = int(input().strip())
while T > 0:
    B, W = input().strip().split(" ")
    X, Y, Z = input().strip().split(" ")
    B, W, X, Y, Z = int(B), int(W), int(X), int(Y), int(Z)
    if Z >= Y and Z >= X:
        print((B * X) + (W * Y))
    elif Y >= X:
        if X + Z >= Y:
            print((B * X) + (W * Y))
        else:
            print((B * X) + W * (X + Z))
    elif X >= Y:
        if Y + Z >= X:
            print((B * X) + (W * Y))
        else:
            print(B * (Y + Z) + (W * Y))
    T -= 1
