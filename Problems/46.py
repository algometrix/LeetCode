class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(numbers, result, new_nums):
            if len(numbers) == len(nums):
                result.append(numbers)
            else:
                for index, num in enumerate(new_nums):
                    dfs(numbers + [num], result, new_nums[:index]+new_nums[index+1:])
        
        result = []
        for index, num in enumerate(nums):
            dfs([num], result, nums[:index] + nums[index+1:])
            
        return result