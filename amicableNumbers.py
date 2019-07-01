dp = [1] * 10000
for i in range(2, 10000):
	for j in range(2, 10000 // i + 1):
		if i * j < 10000:
			dp[i * j] += j

result = 0
for i in range(10000):
	if dp[i] < 10000 and i == dp[dp[i]] and i != dp[i]:
		result += i
print(result)