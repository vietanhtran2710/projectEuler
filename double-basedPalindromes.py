def isDoubleBasedPalindrome(value):
	if str(value) == str(value)[::-1]:
		binary = []
		while (value != 0):
			binary = [value % 2] + binary
			value //= 2
		return binary == binary[::-1]

	else:
		return False


result = 0
for i in range(1, 1000000):
	if isDoubleBasedPalindrome(i):
		if (585 == i):
		result += i
print(result)