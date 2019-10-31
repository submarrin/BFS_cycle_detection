
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


def get_history(current, neigh, pred, start):
    history = [current, neigh]
    if pred[current] == pred[neigh]:
        history.append(pred[neigh])
        return sorted(history)
    while pred[neigh] != pred[current]:
        history.append(pred[neigh])
        history.append(pred[current])
        if pred[neigh] == start:
            current = pred[current]
        elif pred[current] == start:
            neigh = pred[neigh]
        else:
            current = pred[current]
            neigh = pred[neigh]
    return sorted(history)


def find_cycle(start, matr):
    queue = [start]
    pred = [-1]*len(matr)
    visited = [-1]*len(matr)
    pred[0] = -1
    # import pdb
    # pdb.set_trace()
    while queue:
        current = queue.pop(0)
        visited[current] = 1
        current_neighbours = find_neighbour(current, matr)
        for y in current_neighbours:
            if visited[y] == 1:
                continue
            elif visited[y] == -1:
                queue.append(y)
                visited[y] = 0
                pred[y] = current
            else:
                return get_history(y, current, pred, start)
    return "A"


def main(matr):
    return find_cycle(0, matr)
    # for x in range(len(matr)):
    #     result = find_cycle(x, matr)
    #     if result != "A":
    #         print(x, result)
    # print("Finished")


print(main(read_graph()))


