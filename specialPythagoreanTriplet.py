from math import sqrt
found = False
for a in range(1, 1000):
	if found:
		break
	for b in range(1, 1000):
		if a ** 2 + b ** 2 == (1000 - a - b) ** 2:
			print(a * b * (1000 - a - b))
			found = True
