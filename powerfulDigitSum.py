maxResult = 0
for a in range(100):
    for b in range(100):
        value = sum(list(map(int, list(str(a ** b)))))
        if value > maxResult:
            maxResult = value
print(maxResult)
