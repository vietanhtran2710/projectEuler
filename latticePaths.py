def factorial(value):
	result = 1
	for i in range(2, value + 1):
		result *= i
	return result


print(factorial(40) // (factorial(20) * factorial(20)))