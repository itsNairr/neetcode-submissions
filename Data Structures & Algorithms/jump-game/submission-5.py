class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump = nums[0]
        if not jump and len(nums) > 1:
            return False
        for i in range(1, len(nums)-1):
            jump -= 1
            jump = max(jump, nums[i])
            if not jump:
                return False
        
        return True
