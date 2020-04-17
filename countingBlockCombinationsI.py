max_length = 50
dp = [[0, 0] for i in range(max_length + 1)]
dp[0] = [1, 1]

# dp[0]: ways count
# dp[1]: ways count ended with gray square
for i in range(max_length):
    dp[i + 1][0] += dp[i][0]
    dp[i + 1][1] += dp[i][0]

    for j in range(i + 3, max_length + 1):
        dp[j][0] += dp[i][1]

print(dp[max_length])
