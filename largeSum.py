with open("data.txt", "r") as f:
	data = list(map(int, f.readlines()))
	print(str(sum(data))[:10])
