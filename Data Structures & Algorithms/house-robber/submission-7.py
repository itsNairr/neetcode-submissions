
from functools import lru_cache


class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def torob(n):
            if n > len(nums)-1:
                return 0
            if n in cache:
                return cache[n]
            cache[n] = max(nums[n] + torob(n+2), torob(n+1))
            return cache[n]
        return max(torob(0), torob(1))