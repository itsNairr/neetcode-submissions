class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        

        def maxsub(nums):
            ccount = 0
            mcount = -float('inf')
            for num in nums:
                ccount = max(ccount, 0) + num
                mcount = max(ccount, mcount)
            return mcount

        def minsub(nums):
            ccount = 0
            mcount = float('inf')
            for num in nums:
                ccount = min(ccount, 0) + num
                mcount = min(ccount, mcount)
            return mcount

        total = sum(nums)
        minn = minsub(nums)
        maxx = maxsub(nums)

        if maxx < 0:
            return maxx

        return max(maxx, total - minn)