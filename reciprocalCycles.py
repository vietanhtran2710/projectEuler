def getReciproCyclesLength(num):
	modulo = [10 % num]
	div = [10 // num]
	while modulo[-1] != 0:
		d = modulo[-1] * 10
		modulo.append(d % num)
		div.append(d // num)
		if modulo.index(modulo[-1]) != len(modulo) - 1:
			return len(modulo) - modulo.index(modulo[-1]) - 1

	return 0


result, maxLength = 0, 0
for d in range(1, 1000):
	value = getReciproCyclesLength(d)
	if maxLength < value:
		result, maxLength = d, value

print(result)