class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums or len(nums) <= 1:
            return None
        dictt = {}

        for i, num in enumerate(nums):
            second = target - num
            if second in dictt:
                return [dictt[second], i]
            else:
                dictt[num] = i