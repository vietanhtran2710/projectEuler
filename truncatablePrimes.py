from math import sqrt, log10

def isPrime(value):
	for i in range(2, int(sqrt(value)) + 1):
		if value % i == 0:
			return False
	return True

count, result, index = 0, 0, 0
head = [[2, 3, 5, 7]]
tail = [[2, 3, 5, 7]]
while count < 11:
	nextHeadLine = []
	nextTailLine = []
	for item in head[index]:
		if index != 0:
			if item in tail[index]:
				count += 1
				result += item
				if count == 11:
					break
		for i in range(1, 10):
			newValue = i * (10 ** (int(log10(item)) + 1)) + item
			if isPrime(newValue):
				nextHeadLine.append(newValue)
	if count == 11:
		break
	for item in tail[index]:
		for i in range(1, 10):
			if isPrime(item * 10 + i):
				nextTailLine.append(item * 10 + i)
	head.append(list(nextHeadLine))
	tail.append(list(nextTailLine))
	index += 1
print(result)


