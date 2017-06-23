heights = [int(x) for x in input().split(" ")]
word = input()
print(max(map(lambda x: heights[ord(x) - 97], word)) * len(word))