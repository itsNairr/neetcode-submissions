class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        cache = {}
        def robHouse(index, last):
            i = str(index) + "and" + str(last)
            if index > len(nums)-last:
                return 0
            if i in cache:
                return cache[i]
            cache[i] = max(nums[index] + robHouse(index + 2,last), robHouse(index + 1, last))
            return cache[i]
        return max(robHouse(0, 2), robHouse(1, 1))