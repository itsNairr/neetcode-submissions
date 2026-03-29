class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx = 0
        buy = None
        for i, num in enumerate(prices):
            print("price", num)
            print(i)
            if i < len(prices)-1 and num < prices[i+1]:
                if not buy:
                    buy = num
                    print(buy)
            elif buy is not None:
                print("sell", num)
                maxx += (num - buy)
                buy = None
            
        return maxx