def getCharLen(num):
	dct = {1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 
		10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8}
	if num in dct.keys():
		return dct[num]
	if num == 1000:
		return 11
	if num >= 100:
		firstDigit = num // 10 // 10
		lastTwo = (num // 10 % 10) * 10 + (num % 10)
		if lastTwo != 0:
			return dct[firstDigit] + 10 + getCharLen(lastTwo)
		else:
			return dct[firstDigit] + 7
	else:
		firstDigit, lastDigit = num // 10, num % 10
		d = {2: 6, 3: 6, 4: 5, 5: 5, 6: 5, 7: 7, 8: 6, 9: 6}
		if lastDigit != 0:
			return d[firstDigit] + dct[lastDigit]
		else:
			return d[firstDigit]




result = 0
for i in range(1, 1001):
	print(i, getCharLen(i))
	result += getCharLen(i)
print(result)