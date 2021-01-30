def combinationSum(candidates, target):
    def backtrack(candidates, target, result,num_list = []):
        print(num_list)
        if sum(num_list) == target:
            result.append(num_list)
        elif sum(num_list) > target:
            return
            
        for index, candidate in enumerate(candidates):
            backtrack(candidates[index:], target, result, num_list + [candidate])
            
    result = []
    if len(candidates) == 0:
        return result
    
    backtrack(candidates, target, result)
    return result


candidates = [2,3,6,7]
target = 7
print(combinationSum(candidates, target))