def isValid(i):
	s, value = 0, i
	while value != 0:
		s += (value % 10) ** 5
		value //= 10
	return s == i


result = 0

for i in range(11, 1000000):
	if isValid(i):
		result += i

print(result)