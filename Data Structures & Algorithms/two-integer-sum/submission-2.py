class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums or len(nums) <= 1:
            return None
        dict = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in dict.keys():
                return [dict[diff], index]  
            else:
                dict[num] = index
        return None
