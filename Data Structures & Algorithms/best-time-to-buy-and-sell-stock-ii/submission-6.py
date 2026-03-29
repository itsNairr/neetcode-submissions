class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx = 0
        buy = None
        for i, num in enumerate(prices):
            if i < len(prices)-1 and num < prices[i+1]:
                if not buy:
                    buy = num
            elif buy is not None:
                maxx += (num - buy)
                buy = None
        return maxx