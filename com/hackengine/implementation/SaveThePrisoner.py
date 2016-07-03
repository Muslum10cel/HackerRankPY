def find(m, n, s):
    if (m + s) <= n:
        return m + s
    else:
        return (m + s) - n


T = int(input().strip())
while T > 0:
    NMS = input().split(" ")
    N, M, S = int(NMS[0]), int(NMS[1]) - 1, int(NMS[2])
    if M > N:
        M %= N
        print(find(M, N, S))
    else:
        print(find(M, N, S))
    T -= 1
