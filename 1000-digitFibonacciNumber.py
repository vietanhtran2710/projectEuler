x, y, z = 1, 1, 0
index = 2
while len(str(z)) < 1000:
	index += 1
	z = x + y
	x = y
	y = z
print(index)