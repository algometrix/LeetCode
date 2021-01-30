

def lis(nums):
    length = len(nums)
    dp = [1] * length
    for i in range(1, length):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j]+1)
    
    return dp

def minimumMountainRemovals(nums):
    print(nums,'\n')
    dp1 = lis(nums)
    print(dp1)
    dp2 = lis(nums[::-1])
    dp2 = dp2[::-1]
    print(dp2, '\n')
    dp = [ v1+v2-1 for v1,v2 in zip(dp1, dp2) ]
    print(dp)
    return len(nums) - max(dp)

nums = [9,8,1,7,6,5,4,3,2,1]
result = minimumMountainRemovals(nums)
print('Output : {}'.format((result)))