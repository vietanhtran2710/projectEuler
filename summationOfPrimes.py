n = 2000000
isPrime = [True] * (n + 1)
result = 0
for i in range(2, n):
	if isPrime[i]:
		result += i
		for j in range(2, n // i + 1):
			isPrime[i * j] = False
print(isPrime)
print(result)