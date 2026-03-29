class Solution:
    def climbStairs(self, n: int) -> int:
        dictt = {}
        def climb(n):
            if n <= 2:
                return n
            if n in dictt:
                return dictt[n]
            dictt[n] = climb(n-2) + climb(n-1)
            return dictt[n]
        return climb(n)