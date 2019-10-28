
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


def get_history(start, y, pred):
    history = [y]
    while y != start:
        y = pred[y]
        history.append(y)
    return history


print(get_history(0, 3, [-1, 0, 1, 2]))




def bfs(start, matr):
    queue = []
    visited = [False] * len(matr)
    queue.append(start)
    visited[start] = True
    pred = [-1]*len(matr)
    cycle = []
    # print('Начало работы', {'queue': queue, 'visited': visited, 'current': current})
    # import pdb
    # pdb.set_trace()
    while len(queue) > 0:
        current = queue.pop(0)
        current_neighbours = find_neighbour(current, matr)
        for y in current_neighbours:
            pred[y] = current
            if not visited[y]:
                visited[y] = True
                queue.append(y)
            else:
                if y not in queue:
                    return get_history(start, y, pred)
    return "A"


def main(matr):
    for x in range(len(matr)):
        result = bfs(x, matr)
        if result != "A":
            print(x, result)
    print("A")


main(read_graph())


