# Ref : https://medium.com/100-days-of-algorithms/day-41-union-find-d0027148376d
# Git Source : https://github.com/coells/100days

def find(data, i):
    if i != data[i]:
        data[i] = find(data, data[i])
    return data[i]

def union(data, i, j):
    pi, pj = find(data, i), find(data, j)
    if pi != pj:
        data[pi] = pj

def connected(data, i, j):
    return find(data, i) == find(data, j)


if __name__ == "__main__":
    n = 10
    data = [i for i in range(n)]
    connections = [(0, 1), (1, 2), (0, 9), (5, 6), (6, 4), (5, 9)]
    # union
    for i, j in connections:
        union(data, i, j)

    # find
    for i in range(n):
        print('item', i, '-> component', find(data, i))