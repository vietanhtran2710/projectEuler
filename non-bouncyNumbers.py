single = [[0 for j in range(10)] for i in range(101)]
decrease  = [[0 for j in range(10)] for i in range(101)]
increase = [[0 for j in range(10)] for i in range(101)]
single[1] = [1 for i in range(10)]
single[1][0] = 0
result = 0
for i in range(1, 100):
    result += sum(single[i]) + sum(increase[i]) + sum(decrease[i])
    for digit in range(10):
        single[i + 1][digit] += single[i][digit]
        for upper in range(digit + 1, 10):
            increase[i + 1][upper] += single[i][digit]
        for lower in range(digit):
            decrease[i + 1][lower] += single[i][digit]
        for upper in range(digit, 10):
            increase[i + 1][upper] += increase[i][digit]
        for lower in range(digit + 1):
            decrease[i + 1][lower] += decrease[i][digit]
result += sum(single[100]) + sum(increase[100]) + sum(decrease[100])
print(result)
