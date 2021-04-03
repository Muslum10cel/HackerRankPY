import sys

def pickingNumbers(a):
    a.sort()
    maxLen = 0
    tempLen = 0
    for i in range(len(a)):
        for j in range(i, len(a)):
            if abs(a[i] - a[j]) <= 1:
                tempLen+=1
            else:
                break
        if tempLen >= maxLen:
            maxLen = tempLen
        tempLen = 0
    return maxLen
    
if __name__ == "__main__":
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = pickingNumbers(a)
    print(result)