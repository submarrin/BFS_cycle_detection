
def read_graph():
    file_in = open("file_in", 'r')
    n = file_in.readline()
    graph_matrix = []
    for i in range(int(n)):
        line = file_in.readline()
        graph_matrix.append([x == "1" for x in line.split()])
    print(*graph_matrix, sep='\n')
    file_in.close()
    return graph_matrix


def find_neighbour(s, matr, excluded=[]):
    neighbours = []
    for index, x in enumerate(matr[s]):
        if x:
            neighbours.append(index)
    neighbours = filter(lambda a: a not in excluded, neighbours)
    return [x for x in neighbours]


#print(find_neighbour(3, read_graph()))


def bfs(matr):
    queue = []
    visited = [False] * len(matr)
    queue.append(0)
    cycle = []
    current = None
    # print('Начало работы', {'queue': queue, 'visited': visited, 'current': current})
    import pdb
    pdb.set_trace()
    while len(queue) > 0:
        # print('Проверяем, что в очереди есть что-то', {'queue': queue, 'visited': visited, 'current': current})
        current = queue.pop(0)
        if visited[current]:
            return cycle
        else:
            visited[current] = True
        current_neighbours = find_neighbour(current, matr, queue)
        queue += current_neighbours
    return 0

bfs(read_graph())



