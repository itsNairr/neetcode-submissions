class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}

        def solve(i):
            if i in memo:
                return memo[i]
            if i == len(nums) - 1:
                return 0 #cause were at the end

            res = float("inf")
            end = min(len(nums), i + nums[i] + 1) #+1 and no -1 for inclusive
            for j in range(i+1, end):
                res = min(res, 1 + solve(j)) #+1 cause it costs 1 to jump
            memo[i] = res
            return memo[i]
        return solve(0)

            