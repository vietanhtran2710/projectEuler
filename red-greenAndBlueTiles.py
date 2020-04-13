length = 50

dp = [0 for i in range(length + 1)]
dp[0] = 1

for i in range(length):
    #add 1 grey
    if i + 1 <= length:
        dp[i + 1] += dp[i]

    #calculate from red
    if i + 2 <= length:
        dp[i + 2] += dp[i]

    #calculate from green
    if i + 3 <= length:
        dp[i + 3] += dp[i]

    #calculate from blue
    if i + 4 <= length:
        dp[i + 4] += dp[i]

print(dp[length])
