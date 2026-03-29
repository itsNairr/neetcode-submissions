class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        
        # Pass 1: Calculate Prefix products and store in res
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i] #Calculate second so it doesnt use current number
            
        # Pass 2: Calculate Suffix products on the fly and multiply into res
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
            
        return res