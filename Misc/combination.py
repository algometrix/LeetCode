


def combinations(array):
    def dfs(k, temp, result):
        if k == len(array):
            result.append(temp[::])
        else:
            temp.append(k)
            dfs(k+1, temp, result)
            temp.pop()
            dfs(k+1, temp, result)
    
    result = []
    temp = []
    dfs(0, temp, result)
    return result


array = [1,2,3]
print(combinations((array)))


