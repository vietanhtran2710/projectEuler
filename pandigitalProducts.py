from itertools import permutations
prototype = [1, 2, 3, 4, 5, 6, 7, 8, 9]
permutationsList = permutations(prototype)
productSet = set()
for item in permutationsList:
	multiplicand = 0
	for multiplicandIndex in range(0, 7):
		multiplicand = multiplicand * 10 + item[multiplicandIndex]
		multiplier = 0
		for multiplierIndex in range(multiplicandIndex + 1, 8):
			multiplier = multiplier * 10 + item[multiplierIndex]
			product = 0
			for productIndex in range(multiplierIndex + 1, len(item)):
				product = product * 10 + item[productIndex]
			if multiplier * multiplicand == product:
				productSet.add(product)
print(sum(productSet))