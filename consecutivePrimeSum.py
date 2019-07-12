isPrime = [True] * 1000000
prime = []
for i in range(2, 1000000):
	if isPrime[i]:
		prime.append(i)
	for j in range(2, 1000000 // i):
		isPrime[i * j] = False
maxCount, result = 0, 0
for i in range(0, len(prime)):
	sumValue, j, count = prime[i], i + 1, 0
	while sumValue < 1000000 and j < len(prime):
		sumValue += prime[j]
		count += 1
		j += 1
		if sumValue < 1000000 and isPrime[sumValue]:
			if count > maxCount:
				maxCount = count
				result = sumValue
print(result)

