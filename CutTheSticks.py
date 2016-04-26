n = int(input().strip())
sticks = sorted([int(stc) for stc in input().strip().split(" ")])
for st in sticks:
    count = 0
    if st:
        for s in range(len(sticks)):
            if sticks[s]:
                sticks[s] -= st
                count += 1
    if count:
        print(count)
