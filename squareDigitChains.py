def getNextNum(value):
    result = 0
    while value != 0:
        result += (value % 10) ** 2
        value //= 10
    return result


endNum = [0] * 10000000
endNum[1], endNum[89] = 1, 89
countResult = 0
for i in range(2, 10000000):
    path = [i]
    while path[-1] != 1 and path[-1] != 89 and endNum[path[-1]] == 0:
        path.append(getNextNum(path[-1]))
    if endNum[path[-1]] == 89:
        countResult += 1
    for item in path:
        endNum[item] = endNum[path[-1]]

print(countResult)
