class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        low, high = 0, x
        while low <= high:
            mid = low + (high - low)//2
            if mid*mid <= x < (mid+1)*(mid+1):
                return mid
            elif x//mid > mid:
                low = mid + 1
            else:
                high = mid - 1 

        