class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l,r = 0, len(height) - 1
        lm, rm = height[l], height[r]
        res = 0

        while l < r:
            if lm < rm:  #Pick the smaller bound to fill up the minimum max water possible
                l += 1
                lm = max(lm, height[l])
                res += lm - height[l]
            else:
                r -= 1
                rm = max(rm, height[r])
                res += rm - height[r]
        return res

        #HELLO UP THERE (l+1 > l)
        #HELLO DOWN THERE (l+1 < l)