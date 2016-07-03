def find(m, n, s):
    if (m + s) <= n:
        return m + s
    return (m + s) - n


T = int(input().strip())
while T > 0:
    N, M, S = map(int, input().strip().split(" "))
    M -= 1
    if M > N:
        M %= N
        print(find(M, N, S))
    else:
        print(find(M, N, S))
    T -= 1
