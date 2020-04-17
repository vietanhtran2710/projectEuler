max_length = 1000000
dp = [[0, 0] for i in range(max_length + 1)]
dp[0] = [1, 1]

# dp[0]: ways count
# dp[1]: ways count ended with gray square
for i in range(max_length):
    if dp[i][0] > 1000000:
        print(i)
        break
    dp[i + 1][0] += dp[i][0]
    dp[i + 1][1] += dp[i][0]

    for j in range(i + 50, max_length + 1):
        dp[j][0] += dp[i][1]
