import sys

def minimumDistances(a):
    minDistance = len(a) - 1
    found = False
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] == a[j] and (j-i)<=minDistance:
                minDistance = j-i
                found = True
    if not found:
        return -1
    else:
        return minDistance
         

if __name__ == "__main__":
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = minimumDistances(a)
    print(result)
