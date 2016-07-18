n = int(input())
clouds = [int(x) for x in input().split(" ")]
step, nxt = 0, 0
while nxt < n - 1:
    if nxt + 2 > n - 1:
        nxt += 1
        step += 1
        break
    if clouds[nxt + 2] == 0:
        nxt += 2
    else:
        nxt += 1
    step += 1
print(step)
