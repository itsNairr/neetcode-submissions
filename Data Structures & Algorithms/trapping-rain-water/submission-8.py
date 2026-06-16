class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        res = 0
        l, r = 0, len(height)-1
        lm, rm = height[l], height[r]

        while l < r:
            if lm > rm:
                r -= 1
                rm = max(rm, height[r])
                res += rm - height[r]
            else:
                l += 1
                lm = max(lm, height[l])
                res += lm - height[l]

        return res

        #Pick the smaller bound to fill up the minimum max water possible
        #HELLO UP THERE (l+1 > l)
        #HELLO DOWN THERE (l+1 < l)