last_ten_digits = [0 for i in range(10)]
last_ten_digits[0] = 2
for i in range(2, 7830457 + 1):
    rem = 0
    for index in range(len(last_ten_digits)):
        value = last_ten_digits[index] * 2 + rem
        last_ten_digits[index] = value % 10
        rem = value // 10
rem = 0
for index in range(len(last_ten_digits)):
    value = last_ten_digits[index] * 28433 + rem
    last_ten_digits[index] = value % 10
    rem = value // 10
last_ten_digits[0] += 1
print("".join(map(str, last_ten_digits[::-1])))
