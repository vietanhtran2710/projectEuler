data = []

def transform(value, num1, num2):
    from math import sqrt
    dct = {}
    checked = [False] * 10
    for i in range(len(value)):
        if num1[i] in dct.keys():
            return 0
        if checked[int(value[i])]:
            return 0
        dct[num1[i]] = value[i]
        checked[int(value[i])] = True
    if dct[num2[0]] == "0":
        return 0
    result = 0
    for char in num2:
        result = result * 10 + int(dct[char])
    if int(sqrt(result)) == sqrt(result):
        return result
    else:
        return 0


with open("anagramList.txt", "r") as f:
    data = f.readlines()
    for i in range(len(data)):
        data[i] = data[i].split()

maxResult, result1, result2 = 0, 0, 0
from math import log10
square = []
for i in range(10):
	square.append([])
for i in range(1, 31623):
	square[int(log10(i * i)) + 1].append(i * i)

for item in data:
    for firstValue in square[len(item[0])]:
        secondValue1 = transform(str(firstValue), str(item[0]), str(item[1]))
        secondValue2 = transform(str(firstValue), str(item[1]), str(item[0]))

        if secondValue1 != 0:
            if max(firstValue, secondValue1) > maxResult:
                maxResult = max(firstValue, secondValue1)
                result1 = firstValue
                result2 = secondValue1
        if secondValue2 != 0:
            if max(firstValue, secondValue2) > maxResult:
                maxResult = max(firstValue, secondValue2)
                result1 = firstValue
                result2 = secondValue2

print(maxResult)
