from itertools import permutations
lst = [i for i in range(10)]
permutationsList = permutations(lst)
primeList = [2, 3, 5, 7, 11, 13, 17]
result = 0
for item in permutationsList:
	valid = True
	for i in range(len(primeList)):
		value = item[i + 1] * 100 + item[i + 2] * 10 + item[i + 3]
		if value % primeList[i] != 0:
			valid = False
			break
	if valid:
		result += int("".join(map(str, item)))
print(result)

