class Solution:
    def tribonacci(self, n: int) -> int:
        cache = {0: 0, 1: 1, 2: 1}
        def fib(index):
            if index in cache:
                return cache[index]
            cache[index] = fib(index-1) + fib(index-2) + fib(index-3)
            return cache[index]
        
        return fib(n)