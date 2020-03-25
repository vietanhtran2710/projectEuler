from math import log10
result = 0
for digit_count in range(1, 100):
    start_range = 10 ** (digit_count - 1)
    start_alpha = round(start_range ** (1 / digit_count))
    while start_alpha ** digit_count < 10 ** digit_count:
        if int(log10(start_alpha ** digit_count)) + 1 == digit_count:
            result += 1
            print(start_alpha, "^", digit_count, "=", start_alpha ** digit_count)
        start_alpha += 1
print(result)
