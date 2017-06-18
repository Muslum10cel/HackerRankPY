s, n, m = map(int, input().split(" "))
pKeyboard = [int(x) for x in input().split(" ")]
pUsb = [int(x) for x in input().split(" ")]
maxPrice = min(pKeyboard) + min(pUsb)
for keyboard in pKeyboard:
    for usb in pUsb:
        if maxPrice < keyboard + usb <= s:
            maxPrice = keyboard + usb
if maxPrice <= s:
    print(maxPrice)
else:
    print(-1)