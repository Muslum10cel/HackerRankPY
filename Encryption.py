import math

inp = input().strip()
sentence = []
for ch in inp:
    sentence.append(ch)
length = len(sentence)
rows = math.floor(math.sqrt(length))
columns = math.ceil(math.sqrt(length))
if rows * columns < length:
    rows = columns
for i in range(columns):
    for y in range(rows):
        try:
            print(sentence[i + (y * columns)], end="")
        except:
            pass
    print("", end=" ")
