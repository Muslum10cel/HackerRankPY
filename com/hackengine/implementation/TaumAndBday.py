for _ in range(int(input().strip())):
    BW = [int(a) for a in input().strip().split(" ")]
    XYZ = [int(a) for a in input().strip().split(" ")]
    forB = min(XYZ[0], (XYZ[1] + XYZ[2]))
    forW = min(XYZ[1], (XYZ[0] + XYZ[2]))
    print((BW[0] * forB) + (BW[1] * forW))
