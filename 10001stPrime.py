isPrime = [True] * 10000000
primeCount = 0
value = 2
while primeCount < 10001:
	if isPrime[value]:
		primeCount += 1
	if primeCount == 10001:
		print(value)
		break
	for j in range(2, 1000000 // value):
		isPrime[value * j] = False
	value += 1