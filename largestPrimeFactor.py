from math import sqrt

def isPrime(value):
	for i in range(2, int(sqrt(value))):
		if value % i == 0:
			return False
	return True

num = 600851475143
prime_factor = int(sqrt(num))	
while not isPrime(prime_factor) or num % prime_factor != 0:
	prime_factor -= 1
	
print(prime_factor)
