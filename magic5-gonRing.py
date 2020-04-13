from itertools import permutations

max_value = 0
a = [i for i in range(1, 11)]

for item in permutations(a):
    if 10 in (item[0], item[3], item[5], item[8], item[9]):
        s = []
        s.append([item[0], item[1], item[2]])
        s.append([item[3], item[2], item[4]])
        s.append([item[5], item[4], item[6]])
        s.append([item[8], item[6], item[7]])
        s.append([item[9], item[7], item[1]])
        if len(set([sum(item) for item in s])) == 1:
            min_val, index = 11, 0
            for i in range(len(s)):
                if min_val > s[i][0]:
                    min_val, index = s[i][0], i
            string, ind = "".join(map(str, s[index])), (index + 1) % len(s)
            while ind != index:
                string += "".join(map(str, s[ind]))
                ind = (ind + 1) % len(s)
            max_value = max(max_value, int(string))
print(max_value)
