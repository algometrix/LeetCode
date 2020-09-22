

def subgridSum(matrix, subgrid_size):
    row, col = len(matrix), len(matrix[0])
    if subgrid_size == row:
        return sum([ sum(val) for val in matrix])
    elif subgrid_size == 1:
        return max([ max(val) for val in matrix])
    else:
        result = []
       
        for i in range(row - subgrid_size + 1):
            for j in range(row - subgrid_size + 1):
                _sum = 0
                for p in range(i, subgrid_size + i): 
                    for q in range(j, subgrid_size + j): 
                        _sum += matrix[p][q] 
                
                result.append(_sum)
    
    return max(result)
                 

def largestSubgrid(matrix, maxSum):
    row, col = len(matrix), len(matrix[0])
    search_space_min = 1
    search_space_max = row
    result = []
    while search_space_min < search_space_max:
        mid_search_space = (search_space_min + search_space_max) // 2
        subgrid_sum = subgridSum(matrix, mid_search_space)
        if subgrid_sum > maxSum:
            search_space_min = mid_search_space
        else:
            search_space_max = mid_search_space
            result.append(mid_search_space)

    return max(result)

if __name__ == "__main__":
    matrix = [
                [1, 1, 1],
                [1, 1, 1],
                [1, 1, 1],
            ]   
    maxSum = 4
    result = largestSubgrid(matrix, maxSum)
    print('Output : {}'.format(result))
