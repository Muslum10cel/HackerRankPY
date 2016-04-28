sentence = input().split(" ")
ss = ""
for s in sentence:
    for ch in s:
        if ch.isupper():
            ss += ch.lower()
        else:
            ss += ch
if len(set(ss)) == 26:
    print("pangram")
else:
    print("not pangram")
