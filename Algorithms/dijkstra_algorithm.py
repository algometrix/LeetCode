import heapq


def shortest_path(graph, source, destination):
    num_nodes = len(graph)
    for i in range(num_nodes):
        for j in range(num_nodes):
            if graph[i][j] == -1:
                graph[i][j] = float('inf')

    fringe = []
    heapq.heappush(fringe, (0, source, [source]))
    while fringe:
        cost, node, path = heapq.heappop(fringe)
        if node is destination:
            return cost, path
        for index in range(num_nodes):
            if index != node:
                heapq.heappush(fringe, (cost + graph[node][index], index, path + [index]))

    return None


if __name__ == '__main__':
    graph = [
        # 0,  1,  2,  3
        [-1,  1, -1,  9],  # 0
        [-1, -1,  2, -1],  # 1
        [-1, -1, -1,  3],  # 2
        [-1, -1, -1, -1],  # 3
    ]
    print(shortest_path(graph, 0, 3))
