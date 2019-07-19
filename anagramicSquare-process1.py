with open("p098_words.txt", "r") as f:
	data = f.read().split(",")
	for i in range(len(data)):
		data[i] = data[i][1:-1]

from collections import Counter
checked = [False] * len(data)
line = []

with open("anagramList.txt", "w") as f:
    for i in range(len(data) - 1):
    	if not checked[i]:
    		checked[i] = True
    		iCount, anargram = Counter(data[i]), [data[i]]
    		for j in range(i + 1, len(data)):
    			if not checked[j]:
    				if iCount == Counter(data[j]):
    					checked[j] = True
    					anargram.append(data[j])
    		if len(anargram) > 1:
    			line.append(" ".join(anargram) + "\n")
    f.writelines(line)
