with open("names.txt", "r") as f:
	data = f.read().split(",")
	for i in range(len(data)):
		data[i] = data[i][1:-1]
data.sort()

result = 0
for i in range(len(data)):
	score = 0
	for char in data[i]:
		score += ord(char) - ord("A") + 1
	result += score * (i + 1)

print(result)