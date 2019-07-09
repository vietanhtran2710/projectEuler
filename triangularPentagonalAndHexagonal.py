def solve(a, b, c):
	from math import sqrt
	delta = (b ** 2) - (4 * a * c)
	if delta < 0:
		return 1.5
	else:
		return (-b + sqrt(delta)) / (2 * a)


t = 2
while True:
	# print(t)
	triangle = t ** 2 + t
	p = solve(3, -1, -triangle)
	if p != int(p):
		if t == 285:
			break
		t += 1
		continue
	h = solve(4, -2, -triangle)
	if h == int(h) and 3 * p ** 2 - p == 4 * h ** 2 - 2 * h and triangle != 81510:
		print(triangle // 2)
		break
	t += 1
