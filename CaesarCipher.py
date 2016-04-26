N = int(input().strip())
sentence = input().strip()
K = int(input().strip())
message = []
for char in sentence:
    temp = int(ord(char))
    temp1 = K
    if 64 < ord(char) < 91 or 96 < ord(char) < 123:
        while temp1 > 0:
            temp += 1
            if temp == 91:
                temp = 65
            if temp == 123:
                temp = 97
            temp1 -= 1
        message.append(chr(temp))
    else:
        message.append(char)
for i in message:
    print(i, end="")
