class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        msum = -float('inf')
        csum = 0

        for n in nums:
            csum = max(0, csum) + n
            msum = max(msum, csum)
        return msum