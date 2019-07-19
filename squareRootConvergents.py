from math import log10
numerator = 1
denominator = 2
count = 0
for i in range(2, 1001):
    numerator += denominator * 2
    numerator, denominator = denominator, numerator
    if int(log10(numerator + denominator)) + 1 > int(log10(denominator)) + 1:
        count += 1
print(count)
