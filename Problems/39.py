class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(candidates, target, result,num_list = []):
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