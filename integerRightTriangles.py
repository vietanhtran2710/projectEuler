pCount = [0] * 1000
from math import sqrt
for a in range(1, 1000):
	for b in range(1, 1000):
		length = sqrt(a ** 2 + b ** 2)
		if length - int(length) == 0:
			if a + b + sqrt(a ** 2 + b ** 2) < 1000:
				pCount[a + b + int(sqrt(a ** 2 + b ** 2))] += 1
maxResult, result = 0, 0
for i in range(len(pCount)):
	if pCount[i] > maxResult:
		maxResult = pCount[i]
		result = i
print(result)