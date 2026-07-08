class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m = -float('inf')
        cmax = 1
        cmin = 1

        for n in nums:
            if n < 0:
                cmax, cmin = cmin, cmax
            cmax = max(cmax * n, n)
            cmin = min(cmin * n, n)
            print(cmax, cmin)
            m = max(m, cmax, cmin)
        return m