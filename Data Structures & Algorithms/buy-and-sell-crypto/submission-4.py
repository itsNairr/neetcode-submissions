class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, B = 0, 0
        for S in range(len(prices)):
            if prices[S] < prices[B]:
                B = S
            profit = max(profit, prices[S]-prices[B])
        return profit

        