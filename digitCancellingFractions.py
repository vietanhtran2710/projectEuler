numerator = []
denominator = []

for a in range(1, 10):
	for b in range(1, 10):
		for c in range(1, 10):
			if a != b and b != c and c != a:
				if (a * 10 + b) / (b * 10 + c) == a/c:
					numerator.append(a * 10 + b)
					denominator.append(b * 10 + c)
numeratorProduct, denominatorProduct = 1, 1
for i in range(len(numerator)):
	numeratorProduct *= numerator[i]
	denominatorProduct *= denominator[i]
from math import gcd
print(denominatorProduct // gcd(numeratorProduct, denominatorProduct))