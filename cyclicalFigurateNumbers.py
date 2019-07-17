firstTwoDigit = [{}, {}, {}, {}, {}, {}]
path = []
checked = [False] * 6
triangleFormula = lambda x: x * (x + 1) // 2
squareFormula = lambda x: x * x
pentaFormula = lambda x: x * (3 * x - 1) // 2
hexaFormula = lambda x: x * (2 * x - 1)
heptaFormula = lambda x: x * (5 * x - 3) // 2
octaFormula = lambda x: x * (3 * x - 2)

def getLastTwoDigit(value):
    return (value // 10 % 10) * 10 + (value % 10)

def getFirstTwoDigit(value):
    return (value // 1000 * 10) + (value // 100 % 10)

def getNumberDict(dctIndex, indexRange, formula):
    global firstTwoDigit
    for i in indexRange:
        value = formula(i)
        twoDigit = getFirstTwoDigit(value)
        try:
            firstTwoDigit[dctIndex][twoDigit].append(value)
        except KeyError:
            firstTwoDigit[dctIndex][twoDigit] = [value]

def go(digits):
    global path, checked
    if len(path) == 6:
        if digits == getFirstTwoDigit(path[0]):
            print(path, sum(path))
    else:
        for i in range(6):
            if not checked[i] and digits in firstTwoDigit[i].keys():
                for value in firstTwoDigit[i][digits]:
                    path.append(value)
                    checked[i] = True
                    go(getLastTwoDigit(value))
                    path.pop()
                    checked[i] = False

getNumberDict(0, range(45, 141), triangleFormula)
getNumberDict(1, range(32, 100), squareFormula)
getNumberDict(2, range(26, 82), pentaFormula)
getNumberDict(3, range(23, 71), hexaFormula)
getNumberDict(4, range(21, 64), heptaFormula)
getNumberDict(5, range(19, 59), octaFormula)

for item in firstTwoDigit[0].values():
    for number in item:
        path, checked[0] = [number], True
        go(getLastTwoDigit(number))
