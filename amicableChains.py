dp = [1] * 1000001
for i in range(2, 1000001):
	for j in range(2, 1000000 // i + 1):
		if i * j <= 1000000:
			dp[i * j] += j

max_value = 0
result = 0
result_chain = []
checked = [False for i in dp]

for index in range(len(dp)):
    current_chain = []
    count, value, valid = 0, index, True
    while value not in current_chain:
        checked[value] = True
        count += 1
        current_chain.append(value)
        value = dp[value]
        if value > 1000000:
            valid = False
            break
    if valid and count > max_value and current_chain.index(value) == 0:
        max_value = count
        result = min(current_chain)
        result_chain = list(current_chain)
print(result)
