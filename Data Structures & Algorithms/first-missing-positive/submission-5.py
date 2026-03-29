class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        for i in range(1, len(nums)+2): #Check consecutively add 1 to offset 0 and add 1 if number is not in consec
            print(i)
            if i not in nums:
                return i