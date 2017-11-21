def solution(loaves):
    bread = 0
    length = len(loaves)
    for i in range(length - 1):
        if loaves[i] % 2 != 0:
            loaves[i + 1] += 1
            loaves[i] += 1
            bread += 2
    if sum(loaves) % 2 == 0:
        print(bread)
    else:
        print("NO")


if __name__ == "__main__":
    br = int(input())
    loaf = [int(x) for x in input().split(" ")]
    solution(loaf)
