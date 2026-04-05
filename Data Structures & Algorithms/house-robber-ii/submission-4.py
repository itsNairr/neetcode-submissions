class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def robHouse(numss):
            cache = {}
            def robb(index):
                if index >= len(numss):
                    return 0
                if index in cache:
                    return cache[index]
                cache[index] = max(numss[index] + robb(index + 2), robb(index + 1))
                return cache[index]
            return robb(0)
            
        return max(robHouse(nums[:-1]), robHouse(nums[1:]))