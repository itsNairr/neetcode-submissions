class Solution:
    def climbStairs(self, n: int) -> int:
        dictt = {}
        def climb(num):
            if num <= 2:
                return num
            if num in dictt:
                return dictt[num]
            dictt[num] = climb(num-1) + climb(num-2)
            return dictt[num]
        return climb(n)
        