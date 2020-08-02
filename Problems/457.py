class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        mark = [1 if x % len(nums) != 0 else 0 for x in nums]
        
        def jump(site, di):
            if mark[site] == 0 or nums[site]*di < 0:
                return False
            if mark[site] == 2:
                return True
            mark[site] = 2
            if jump((site + nums[site]) % len(nums), di):
                return True
            mark[site] = 0
            return False
            
        for i in range(len(nums)):
            if jump(i, nums[i]): return True
        return False