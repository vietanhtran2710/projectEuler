from math import sqrt
from collections import Counter

def isPrime(value):
	for i in range(2, int(sqrt(value))):
		if value % i == 0:
			return False
	return True

def getPrimeFactorList(value):
	result = []
	prime = 2
	while (value != 1):
		while not isPrime(prime) or value % prime != 0:
			prime += 1
		result.append(prime)
		value //= prime
	return result

num = 1
value = 2
while True:
	num += value
	value += 1
	lst = getPrimeFactorList(num)
	dct = Counter(lst)
	factorCount = 1
	for val in dct.values():
		factorCount *= (val + 1)
	if factorCount + 1 >= 500:
		print(num)
		break

