grid = []

with open("matrix.txt") as f:
    data = f.readlines()
    for item in data:
        line = list(map(int, item.split(",")))
        grid.append(list(line))

from sys import maxsize
dp = []
for item in grid:
    line = []
    for value in item:
        line.append(maxsize)
    dp.append(line)
dp[0][0] = grid[0][0]

for i in range(len(dp)):
    for j in range(len(dp[0])):
        if i + 1 < len(dp) and dp[i][j] + grid[i + 1][j] < dp[i + 1][j]:
            dp[i + 1][j] = dp[i][j] + grid[i + 1][j]
        if j + 1 < len(dp[0]) and dp[i][j] + grid[i][j + 1] < dp[i][j + 1]:
            dp[i][j + 1] = dp[i][j] + grid[i][j + 1]

print(dp[-1][-1])
