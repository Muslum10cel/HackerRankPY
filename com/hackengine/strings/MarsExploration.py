s = input()
t = len(s) // 3 * "SOS"
print(len(list(filter(lambda x: x > 0, [ord(a) ^ ord(b) for a, b in zip(s, t)]))))