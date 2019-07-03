factorial = {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040, 8: 40320, 9: 362880}

result = 0
for i in range(10, 10000000):
	curious, value = 0, i
	while (value != 0):
		curious += factorial[value % 10]
		if curious > i:
			break
		value //= 10
	if curious == i:
		result += i

print(result)