isPrime = [True] * 1000000
prime = []
isPrime[0], isPrime[1] = False, False
for i in range(2, 1000000):
	if isPrime[i]:
		prime.append(i)
		for j in range(2, 1000000 // i + 1):
			if i * j < 1000000:
				isPrime[i * j] = False


def getDistinctPrimesFactors(value):
	count, primeIndex = 0, 0
	while value != 1:
		while primeIndex < len(prime) and value % prime[primeIndex] != 0:
			primeIndex += 1
		count += 1
		while value % prime[primeIndex] == 0:
			value //= prime[primeIndex]
	return count


num = 210
while True:
	found = True
	for i in range(4):
		if getDistinctPrimesFactors(num + i) != 4:
			found = False
			break
	if found:
		print(num)
		break
	num += 1