def isPrime(value):
    from math import sqrt
    for i in range(2, int(sqrt(value)) + 1):
        if value % i == 0:
            return False
    return True


length, start, countPrime, spiralLength, sideLength = 2, 1, 0, 1, 1
while countPrime == 0 or countPrime / spiralLength >= 0.1:
    sideLength += 2
    spiralLength += 4
    for i in range(4):
        start += length
        if isPrime(start):
            countPrime += 1
    length += 2
print(sideLength)
