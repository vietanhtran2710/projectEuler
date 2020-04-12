file_name = 'network.txt'
network, edge_sum = [], 0
with open(file_name, 'r') as f:
    data = f.readlines()
    for item in data:
        line = []
        for value in item.strip().split(','):
            if value == '-':
                line.append(0)
            else:
                line.append(int(value))
                edge_sum += int(value)
        network.append(line)
for line in network:
    for item in line:
        print("{0:3}".format(item), end = "")
    print()

chosen, result = set(), 0
min_value = 1000
first_two_node = [0, 0]
for i in range(len(network)):
    for j in range(len(network)):
        if network[i][j] != 0 and network[i][j] < min_value:
            min_value, first_two_node = network[i][j], [i, j]
chosen.add(first_two_node[0])
chosen.add(first_two_node[1])
result = min_value
while len(chosen) < len(network):
    min_val, next_node = 1000, 0
    for node in chosen:
        for i in range(len(network)):
            if i not in chosen and network[node][i] < min_val:
                if network[node][i] != 0:
                    min_val, next_node = network[node][i], i
    result += min_val
    chosen.add(next_node)
print(edge_sum // 2 - result, chosen)
