
def read_graph():
    file_in = open("file_in", 'r')
    n = file_in.readline()
    graph_matrix = []
    for i in range(int(n)):
        line = file_in.readline()
        graph_matrix.append([x == "1" for x in line.split()])
    # print(*graph_matrix, sep='\n')
    file_in.close()
    return graph_matrix


def find_neighbour(s, matr, excluded=[]):
    neighbours = []
    for index, x in enumerate(matr[s]):
        if x:
            neighbours.append(index)
    neighbours = filter(lambda a: a not in excluded, neighbours)
    return [x for x in neighbours]


# print(find_neighbour(3, read_graph()))


def bfs(start, matr):
    queue = []
    visited = [False] * len(matr)
    queue.append(start)
    pred = [-1]*len(matr)
    cycle = []
    # print('Начало работы', {'queue': queue, 'visited': visited, 'current': current})
    # import pdb
    # pdb.set_trace()
    while len(queue) > 0:
        exclude_elements = queue.copy()
        current = queue.pop(0)
        if not visited[current]:
            visited[current] = True
            cycle.append(current)
        else:
            return cycle
        current_neighbours = find_neighbour(current, matr, exclude_elements)
        for y in current_neighbours:
            pred[y] = current
        queue += current_neighbours
    return "A"


def main(matr):
    for x in range(len(matr)):
        result = bfs(x, matr)
        if result != "A":
            print(x, result)
    print("A")


main(read_graph())


