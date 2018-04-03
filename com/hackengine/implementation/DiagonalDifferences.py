a = int(input())
i = 0
j = a-1
s = 0
for _ in range(a):
	ls = [int(x) for x in input().split(" ")]
	s += (ls[i] - ls[j])
	i += 1
	j -=1

print(abs(s))
