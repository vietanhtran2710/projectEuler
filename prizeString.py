#array for dynamic programming method 

#array counting string with 0 L
dp_0l = [[0, 0, 0] for i in range(31)]
#array counting string with 1 L
dp_1l = [[0, 0, 0] for i in range(31)]

# dp list item description
# [0]: number of last consecutive As = 0
# [1]: number of last consecutive As = 1
# [2]: number of last consecutive As = 2
dp_0l[1], dp_1l[1] = [1, 1, 0], [1, 0, 0]

for i in range(1, 30):
   #calculate dp[i + 1] from dp[i] 

   #dp_0l
    dp_0l[i + 1][0] = sum(dp_0l[i])
    dp_0l[i + 1][1] = dp_0l[i][0]
    dp_0l[i + 1][2] = dp_0l[i][1]

    #dp_1l
    dp_1l[i + 1][0] = sum(dp_0l[i]) + sum(dp_1l[i])
    dp_1l[i + 1][1] = dp_1l[i][0]
    dp_1l[i + 1][2] = dp_1l[i][1]

print(dp_0l[2])
print(dp_1l[2])

print(dp_0l[3])
print(dp_1l[3])
print(sum(dp_0l[3]) + sum(dp_1l[3]))
print(sum(dp_0l[30]) + sum(dp_1l[30]))
