class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i,n in enumerate(nums):
            if n > 0:
                continue
                
            if i > 0 and nums[i] == nums[i-1]: 
                continue 

            l = i + 1
            r = len(nums) - 1

            while l < r:
                summ = nums[l] + n + nums[r]
                if summ == 0:
                    res.append([nums[l],n,nums[r]])
                    r -= 1
                
                if summ > 0:
                    r -= 1
                
                else:
                    while l < len(nums)-1 and nums[l] == nums[l+1]:
                        l += 1
                    l += 1

        return res