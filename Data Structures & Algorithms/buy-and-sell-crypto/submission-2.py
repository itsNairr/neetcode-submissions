class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        B = 0
        for S in range(len(prices)):
            while prices[S] < prices[B]:
                B += 1
            profit = max(profit, prices[S]-prices[B])
        return profit

        