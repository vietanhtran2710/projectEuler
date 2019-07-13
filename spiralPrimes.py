def isPrime(value):
    from math import sqrt
    for i in range(2, int(sqrt(value)) + 1):
        if value % i == 0:
            return False
    return True


length, start, countPrime, spiralLength, sideLength = 2, 1, 1, 1, 1
while countPrime / spiralLength >= 0.1:
    sideLength += 2
    for i in range(4):
        spiralLength += 1
        start += length
        if isPrime(start):
            countPrime += 1
        if countPrime / spiralLength < 0.1:
            print(sideLength,"--")
            break
    if countPrime / spiralLength < 0.1:
        break
    length += 2
