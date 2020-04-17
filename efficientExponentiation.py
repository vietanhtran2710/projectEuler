max_value = 200
count = [[i, [set()]] for i in range(max_value + 1)]
count[1] = [0, [set([1])]]
result = 0

for i in range(1, max_value):
    result += count[i][0]
    if i * 2 <= max_value:
        if count[i * 2][0] > count[i][0] + 1:
            count[i * 2][0] = count[i][0] + 1
            set_lst = []
            for set_item in count[i][1]:
                set_lst.append(set_item.union(set([i])).union(set([i * 2])))
            count[i * 2][1] = list(set_lst)
        elif count[i * 2][0] == count[i][0] + 1:
            for set_item in count[i][1]:
                new_set = set_item.union(set([i])).union(set([i * 2]))
                count[i * 2][1].append(new_set)

    for j in range(1, i):
        if i + j <= max_value:
            for set1 in count[i][1]:
                for set2 in count[j][1]:
                    new_set = set1.union(set2)
                    if len(new_set) < count[i + j][0]:
                        count[i + j][0] = len(new_set) 
                        count[i + j][1] = [new_set.union(set([i + j]))]
                    elif len(new_set) == count[i + j][0]:
                        count[i + j][1].append(new_set.union(set([i + j])))

result += count[max_value][0]
print(result)


