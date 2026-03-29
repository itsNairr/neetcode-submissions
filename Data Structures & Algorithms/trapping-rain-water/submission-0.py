class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l, r, a, = 0, len(height)-1, 0
        rm, lm = height[r], height[l]
        while l < r:
            if lm < rm:
                l += 1
                lm = max(lm, height[l])
                a += lm - height[l]
            else:
                r -= 1
                rm = max(rm, height[r])
                a += rm - height[r]
        return a