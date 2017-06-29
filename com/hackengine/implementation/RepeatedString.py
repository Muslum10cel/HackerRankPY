s = str(input())
n = int(input())
print((s[:n % len(s)].count("a")) + ((n // len(s)) * s.count("a")))