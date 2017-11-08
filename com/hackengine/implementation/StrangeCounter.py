import math as m


def result(t):
    n = m.floor((m.log10((t + 3) / 3)) / (m.log10(2)))
    temp = 3 * (2 ** n) - 3
    if t == 1:
        return 3
    elif t == 2:
        return 2
    elif t == temp:
        return 1
    else:
        tcycbeg = temp + 1
        tvalbeg = 3 * (2 ** n)
        return tvalbeg - (abs(tcycbeg - t))


time = int(input())
print(result(time))