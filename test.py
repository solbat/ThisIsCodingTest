graph = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3]]

num = 0

def change():
    graph[0][1] = 1
    num = 1

change()
print(graph)
print(num)