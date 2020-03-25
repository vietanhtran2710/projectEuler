path = []
checked = [False for i in range(0, 10)]

def go(node):
    path.append(node)
    if len(path) == 8:
        print("".join(map(str,path)))
        exit()
    else:
        checked[node] = True
        for i in range(0, 10):
            if not checked[i] and graph[path[-1]][i]:
                go(i)
        checked[node] = False
        path.pop()

digits = [i for i in range(0, 10)]
with open("keylog.txt", "r") as f:
    data = f.readlines()
graph = [[False for i in range(0, 10)] for j in range(0, 10)]
for item in data:
    graph[int(item[0])][ int(item[1])] = True 
    graph[int(item[1])][ int(item[2])] = True
    graph[int(item[0])][ int(item[2])] = True
for k in range(len(graph)):
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = True
go(7)
