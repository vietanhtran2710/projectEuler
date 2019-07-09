triangleNumbers = []
countResult = 0
for n in range(1, 10000):
	triangleNumbers.append((n * (n + 1)) // 2)
with open("words.txt", "r") as f:
	data = f.read()
	words = data.split(",")
	for word in words:
		value = 0
		for char in word[1:-1]:
			value += ord(char) - ord("A") + 1
		if value in triangleNumbers:
			countResult += 1
			print(word)
			if word == "SKY":
				print("found")
print(countResult) 