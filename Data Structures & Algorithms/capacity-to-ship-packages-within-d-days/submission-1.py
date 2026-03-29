class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low, high = max(weights), sum(weights)
        res = high
        while low <= high:
            mid = low + (high - low)//2
            d = 1
            dw = mid
            for w in weights:
                if dw >= w:
                    dw -= w
                else:
                    d += 1
                    dw = mid - w
            if d <= days:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res