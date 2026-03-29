class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        k = 0
        while low <= high:
            res = 0
            mid = low + (high - low)// 2
            for b in piles:
                res +=  math.ceil(b/mid)
            if res <= h:
                k = mid
                high = mid -1
            else:
                low = mid + 1
        return k