import collections

def numBusesToDestination(routes, S, T):
    if S == T:
        return 0

    neighbor_stops = collections.defaultdict(set)
    for i, route in enumerate(routes):
        for j in route:
            neighbor_stops[j].add(i)

    bfs = [(S, 0)]
    visited = set([S])
    for current_stop, bus_change in bfs:
        if current_stop == T:
            return bus_change
        for index in neighbor_stops[current_stop]:
            for neighbor in routes[index]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    bfs.append((neighbor, bus_change + 1))
            
    return -1

if __name__ == "__main__":
    routes = [[1, 2, 7], [3, 6, 7]]
    S = 1
    T = 6
    result = numBusesToDestination(routes, S, T)
    print('Minimum number of bus changes : {}'.format(result))