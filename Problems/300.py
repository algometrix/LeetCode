from bisect import bisect_left
def lengthOfLIS(nums):
    dp = []
    for elem in nums:
        ind = bisect_left(dp, elem)
        if ind == len(dp):
            dp.append(elem)
        else:
            dp[ind] = elem
    return len(dp)


nums = [8,7,6,2,3,4,5]
print(lengthOfLIS(nums))