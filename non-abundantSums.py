dp = [0] * 28124
abundant = []
for i in range(2, 28124):
	if dp[i] > i:
		abundant.append(i)
	for j in range(2, 28124 // i + 1):
		if i * j < 28124:
			dp[i * j] += j

result = [False for i in range(28124)] 
for i in range(len(abundant) - 1):
	for j in range(i, len(abundant)):
		if abundant[i] + abundant[j] <= 28123:
			result[abundant[i] + abundant[j]] = True

s = 0
for i in range(1, 28124):
	if not result[i]:
		s += i

print(s)