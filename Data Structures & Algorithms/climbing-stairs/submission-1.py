class Solution:
    def climbStairs(self, n: int) -> int:
        dictt = {}
        def climb(n):
            if n in dictt:
                return dictt[n]
            if n == 0:
                return 1
            if n < 0:
                return 0
            res1 = climb(n-1)
            res2 = climb(n-2)
            dictt[n] = res1 + res2
            return res1 + res2
        return climb(n-1) + climb(n-2)