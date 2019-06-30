triangle = []

with open("data.txt", "r") as f:
	data = f.readlines()
	for item in data:
		line = list(map(int, item.split()))
		triangle.append(list(line))

result = []
for line in triangle:
	newLine = []
	for item in line:
		newLine.append(item)
	result.append(newLine)
result[1][0] += result[0][0]
result[1][1] += result[0][0]
for i in range(1, len(triangle) - 1):
	for j in range(len(triangle[i])):
		if result[i + 1][j] < result[i][j] + triangle[i + 1][j]:
			result[i + 1][j] = result[i][j] + triangle[i + 1][j]
		if result[i + 1][j + 1] < result[i][j] + triangle[i + 1][j + 1]:
			result[i + 1][j + 1] = result[i][j] + triangle[i + 1][j + 1]
print(max(result[-1]))