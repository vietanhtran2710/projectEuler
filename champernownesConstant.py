def getDigit(index):
	from math import log10
	length, num = 0, 0
	while length < index:
		num += 1
		length += int(log10(num)) + 1
		if length >= index:
			return int(str(num)[len(str(num)) - (length - index) - 1])

print(getDigit(1) * getDigit(10) * getDigit(100) * getDigit(1000) * getDigit(10000) * getDigit(100000) * getDigit(1000000))