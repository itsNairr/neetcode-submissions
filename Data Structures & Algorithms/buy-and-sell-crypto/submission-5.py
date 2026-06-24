class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx, B = 0, 0
        for i in range(len(prices)):
            if prices[i] < prices[B]:
                B = i
            maxx = max(maxx, prices[i]-prices[B])
        
        return maxx
        