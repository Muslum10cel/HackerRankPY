def solution(n, k):
    if k == 0:
        print(*range(1, n + 1))
    elif n % 2 * k != 0:
        print(-1)
    else:
        for i in range(1, n + 1, 2 * k):
            print(*list(map(lambda x: x + k, range(i, i + k))), *list(map(lambda y: y - k, range(i + k, 2 * k + i))),
                  end=" ")
        print()


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split(" "))
        solution(N, K)
