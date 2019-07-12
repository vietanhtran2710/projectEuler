from math import log10
maxResult = 0
i = 1
for i in range(1, 100000):
	# print(i)
	n, isPandigital = 1, True
	count = [False] * 9
	pandigital = 0
	while not all(count):
		value, isValid = i * n, True
		backUp = int(value)
		while value != 0:
			if value % 10 == 0 or count[value % 10 - 1]:
				isValid, isPandigital = False, False
				break
			count[value % 10 - 1] = True
			value //= 10
		if not isPandigital:
			break
		if isValid and isPandigital:
			if backUp != 0:
				pandigital = pandigital * (10 ** (int(log10(backUp)) + 1)) + backUp	
		n += 1
	if isPandigital and pandigital > maxResult:
		maxResult = pandigital
	i += 1
print(maxResult)	
