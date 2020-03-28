dct = {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040, 8: 40320, 9: 362880}
length = {}
result = 0

for i in range(1000000):
    try:
        if length[i] == 60:
            result += 1
    except KeyError:
        count, chain, start = 0, [i], i
        while True:
            value, num = 0, start
            while num != 0:
                value += dct[num % 10]
                num //= 10
            if value in chain:
                length[value] = len(chain) - chain.index(value)
            try:
                new_value, value_index = length[value], chain.index(value)
                for j in range(value_index):
                    length[chain[j]] = value_index - j + length[value]
                for j in range(value_index + 1, len(chain)):
                    length[chain[j]] = length[value]
                if length[i] == 60:
                    result += 1
                break
            except KeyError:
                count += 1
                chain.append(value)
                start = value
            except ValueError:
                for j in range(len(chain)):
                    length[chain[j]] = len(chain) - j + length[value]
                if length[i] == 60:
                    result += 1
                break
print(result)
