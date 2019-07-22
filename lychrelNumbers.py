result = 0

for i in range(1, 10000):
    isLychrel, value = True, i
    for k in range(50):
        value += int(str(value)[::-1])
        if str(value) == str(value)[::-1]:
            isLychrel = False
            break
    if isLychrel:
        result += 1

print(result)
