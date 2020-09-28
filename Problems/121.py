class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        if not prices:
            return 0
        dp = []
        for i in range(len(prices)):
            minPrice = min(minPrice, prices[i])
            dp.append(prices[i] - minPrice)
        
        #print(dp)
        return max(dp)