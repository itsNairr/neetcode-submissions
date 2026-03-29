class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                if nums[-1] == val:
                    nums.pop()
                    continue
                nums[i] = nums[-1]
                nums.pop()
            i+=1
        return len(nums)