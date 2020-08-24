

def matrix_update_to_list(matrix_as_list, i, j, n, m, value):
    index  = (j * n) + i
    matrix_as_list[index] = value

def matrixQueries(n, m, queries):
    total_length = m * n
    matrix_as_list = [0] * total_length
    result = []
    for i in range(n):
        for j in range(m):
            value = (i + 1) * (j + 1)
            matrix_update_to_list(matrix_as_list, i, j, n, m, value)

    for query in queries:
        if query[0] == 0:
            result.append(min(matrix_as_list))
        elif query[0] == 1:
            for j in range(m):
                matrix_update_to_list(matrix_as_list, query[1] - 1, j, n, m, float('inf'))
        elif query[0] == 2:
            for i in range(n):
                matrix_update_to_list(matrix_as_list, i,query[1] - 1, n, m, float('inf'))

    return result



if __name__ == "__main__":
    query = [[0], [1,2], [0], [2,1], [0], [1,1], [0]]
    r = matrixQueries(3, 4, query)
    print(r)