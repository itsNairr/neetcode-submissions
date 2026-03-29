class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        maxx = 0
        while l < r:
            w = r - l
            h = min(heights[l], heights[r])
            a = w * h
            if a > maxx:
                maxx = a
            elif heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return maxx