class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True

        steps = 0
        for i, n in enumerate(nums):
            steps = max(steps, n)
            if i == len(nums)-1:
                return True
            if not steps:
                return False
            steps -= 1
