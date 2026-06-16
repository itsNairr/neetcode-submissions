class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True

        steps = 0
        remaining = 0

        for n in nums:
            remaining = max(remaining, n)
            if remaining == 0 and steps != len(nums)-1:
                return False
            steps += 1
            remaining -= 1
            if steps == len(nums)-1:
                return True
