from math import sqrt
isPrime = [True] * 10000
primeNumber = []
for i in range(2, len(isPrime)):
	if not isPrime[i]:
		if i % 2 != 0:
			canBeWritten = False
			for value in primeNumber:
				if int(sqrt((i - value) // 2)) == sqrt((i - value) // 2):
					canBeWritten = True
					break
			if not canBeWritten:
				print(i)
				break
	else:
		primeNumber.append(i)
		for j in range(2, 10000 // i + 1):
			if i * j < 10000:
				isPrime[i * j] = False
