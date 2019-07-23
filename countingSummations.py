count = [0 for i in range(101)]
count[0] = 1
for i in range(1, 100):
    for j in range(i, 101):
        count[j] += count[j - i]
print(count[100])
