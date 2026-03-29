class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        L = 0
        res = []
        for R in range(k-1, len(nums)):
            res.append(max(nums[L:R+1]))
            L+=1
        return res