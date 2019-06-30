factorial = 1
for i in range(2, 101):
	factorial *= i
print(sum(list(map(int, list(str(factorial))))))