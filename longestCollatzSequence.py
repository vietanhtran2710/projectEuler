maxNum = 400000000
length = [0] * maxNum
stack = [[1, 1]]

while stack:
	value, l = stack[-1][0], stack[-1][1]
	stack.pop()
	length[value] = l
	if value * 2 < maxNum and length[value * 2] == 0:
		stack.append([value * 2, l + 1])
	if (value - 1) % 3 == 0 and (value - 1) != 0 and (value - 1) // 3 != 1 and length[(value - 1) // 3] == 0 and ((value - 1) // 3 % 2) == 1:
		stack.append([(value - 1) // 3, l + 1])

print(max(length[:1000000]))
print(length[:1000000].count(0) - 1)
