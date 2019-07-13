count = [i - 1 for i in range(1000001)]
count[0], count[1], result = 0, 0, 0
for i in range(2, 1000001):
    result += count[i]
    for j in range(2, 1000000 // i + 1):
        count[i * j] -= count[i]
print(result)
