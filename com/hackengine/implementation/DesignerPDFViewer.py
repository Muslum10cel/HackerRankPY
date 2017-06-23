heights = [int(x) for x in input().split(" ")]
word = input()
ls = []
for char in word:
    ls.append(heights[ord(char) - 97])
print(max(ls) * len(word))