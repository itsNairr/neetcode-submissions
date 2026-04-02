
from functools import lru_cache


class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache(None)
        def torob(n):
            if n > len(nums)-1:
                return 0
            return max(nums[n] + torob(n+2), torob(n+1))
        return max(torob(0), torob(1))