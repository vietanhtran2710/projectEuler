from math import log10
maxResult, indexResult = 0, 0

with open("base_exp.txt", "r") as f:
    data = f.readlines()
    for index, item in enumerate(data):
        numLst = list(map(int, item.split(",")))
        value = numLst[1] * log10(numLst[0])
        if value > maxResult:
            maxResult = numLst[1] * log10(numLst[0])
            indexResult = index

print(indexResult + 1) # Base-1 index
