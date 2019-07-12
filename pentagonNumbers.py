def gotIntSolution(value):
	from math import sqrt
	delta = 24 * value + 1
	x1 = (1 + sqrt(delta)) / 6
	return x1 == int(x1)


pentagonNumbers = [i * (3 * i - 1) // 2 for i in range(1, 10001)]
found = False
for diff in pentagonNumbers:
	if found:
		break
	for penK in pentagonNumbers:
		if gotIntSolution(diff + penK) and gotIntSolution(2 * penK + diff):
			print(diff, diff + penK, 2 * penK + diff)
			found = True
			break