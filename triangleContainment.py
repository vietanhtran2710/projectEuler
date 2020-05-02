result = 0

def length(x1, y1, x2, y2):
    from math import sqrt
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def getSize(x1, y1, x2, y2, x3, y3):
    from math import sqrt
    side1 = length(x1, y1, x2, y2)
    side2 = length(x2, y2, x3, y3)
    side3 = length(x1, y1, x3, y3)

    p = (side1 + side2 + side3) / 2

    return sqrt(p * (p - side1) * (p - side2) * (p - side3))

def doesContains(*param):
    x1, y1, x2, y2, x3, y3 = param

    print("A(", x1, ",", y1, ") B(", x2, ",", y2, "), C(", x3, ",", y3, ")")

    if length(x1, y1, 0, 0) + length(0, 0, x2, y2) == length(x1, y1, x2, y2):
        return True
    if length(x2, y2, 0, 0) + length(0, 0, x3, y3) == length(x2, y2, x3, y3):
        return True
    if length(x1, y1, 0, 0) + length(0, 0, x3, y3) == length(x1, y1, x3, y3):
        return True
    
    size1 = round(getSize(0, 0, x1, y1, x2, y2), 1)
    size2 = round(getSize(0, 0, x2, y2, x3, y3), 1)
    size3 = round(getSize(0, 0, x3, y3, x1, y1), 1)

    totalSize = round(getSize(x1, y1, x2, y2, x3, y3), 1)

    print(totalSize, size1, size2, size3)

    if abs(totalSize - (size1 + size2 + size3)) <= 0.00000000000000000000000001:
        return True
    return False

with open("triangles.txt", "r") as f:
    data = f.readlines()
    for item in data:
        param = list(map(int, item.split(",")))
        if doesContains(*param):
            print("TRUE")
            result += 1
        else:
            print("FALSE")

print(result)