def isPrime(value):
	from math import sqrt
	for i in range(2, int(sqrt(value)) + 1):
		if value % i == 0:
			return False
	return True

from itertools import permutations
digits = [i for i in range(1, 10)]
maxResult = 0
while digits:
	permutationsList = permutations(digits)
	for item in permutationsList:
		value = int("".join(list(map(str, list(item)))))
		if isPrime(value):
			if value > maxResult:
				maxResult = value
	digits.pop()
print(maxResult)