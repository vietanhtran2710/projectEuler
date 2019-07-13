def factorial(value):
    result = 1
    for i in range(2, value + 1):
        result *= i
    return result


def combination(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


count = 0
for n in range(1, 101):
    for r in range(n + 1):
        if combination(n, r) > 1000000:
            count += 1
print(count)
