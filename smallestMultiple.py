from math import gcd

def lcm(a, b):
	return (a * b) // gcd(a, b)

a = [i for i in range(1, 21)]
result = 1
for i in range(1, len(a)):
	result = lcm(result, a[i])
print(result)