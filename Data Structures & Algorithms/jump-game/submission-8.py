class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump = nums[0]
        if not jump and len(nums) > 1:
            return False
        for i in range(1, len(nums)-1):
            jump = max(jump-1, nums[i])
            if not jump:
                return False
        
        return True
