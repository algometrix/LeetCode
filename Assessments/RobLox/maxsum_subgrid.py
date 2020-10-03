

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
    while search_space_min <= search_space_max:
        #print(search_space_min, search_space_max)
        mid_search_space = (search_space_min + search_space_max) // 2
        subgrid_sum = subgridSum(matrix, mid_search_space)
        #print("Sum ", mid_search_space, subgrid_sum)
        if subgrid_sum > maxSum:
            search_space_max = mid_search_space - 1
        else:
            search_space_min = mid_search_space + 1
            result.append(mid_search_space)

    #print(result)
    return max(result)

if __name__ == "__main__":
    matrix = [
                [1, 1, 1,1],
                [2, 2, 2, 2],
                [3, 3, 3, 3],
                [4, 4, 4, 4]
            ]   
    
    maxSum = 39
    result = largestSubgrid(matrix, maxSum)
    print('Output : {}'.format(result))
