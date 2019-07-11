isPrime = [True] * 1000000
prime = []
result = 0
for i in range(2, 1000000):
	if isPrime[i]:
		prime.append(i)
		for j in range(2, 1000000 // i + 1):
			if i * j < 1000000:
				isPrime[i * j] = False
checked = [False] * 1000000
for value in prime:
	if value < 10:
		result += 1
	elif not checked[value]:
		checked[value] = True
		isValid = True
		digits = list(str(value))
		for i in range(len(digits) - 1):
			digits = [digits[-1]] + digits[:-1]
			newValue = int("".join(digits))
			checked[newValue] = True
			if not isPrime[newValue]:
				isValid = False
				break
		if isValid:
			result += len(digits)
print(result - 1) #Minus 1 because of the special case: 11

