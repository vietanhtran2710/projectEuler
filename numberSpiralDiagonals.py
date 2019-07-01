n = 1001
result, number, length = 1, 1, 2
for i in range(n // 2):
	for j in range(4):
		number += length
		result += number
	length += 2
print(result)