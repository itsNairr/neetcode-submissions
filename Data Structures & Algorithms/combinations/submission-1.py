class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combs = []
        def helper(i, ccomb):
            if len(ccomb) == k:
                combs.append(ccomb.copy())
                return
            if i > n:
                return
            
            for j in range(i, n + 1):
                ccomb.append(j)
                helper(j+1, ccomb)
                ccomb.pop()

        helper(1, [])
        return combs