result = 0
for i in range(100, 1000):
	for j in range(100, 1000):
		value = i * j
		if str(value) == str(value)[::-1] and value > result:
			result = value
print(result)