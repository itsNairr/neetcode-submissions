from functools import lru_cache

class Solution:
    def tribonacci(self, n: int) -> int:
        @lru_cache(None)
        def fib(index):
            if index == 0:
                return 0
            if index == 1 or index == 2:
                return 1
            return fib(index-1) + fib(index-2) + fib(index-3)
        
        return fib(n)