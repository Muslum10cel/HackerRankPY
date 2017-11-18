def solution(s):
    count = []
    temp = set(s)
    if len(temp) == 1:
        print(0)
        return
    for num in temp:
        count.append(s.count(num))
    print(sum(count) - max(count))


if __name__ == "__main__":
    T = int(input())
    numbers = [int(x) for x in input().split(" ")]
    solution(numbers)
