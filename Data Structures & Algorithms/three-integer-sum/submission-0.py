class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = []
        nums.sort()
        a, r = 0, len(nums)-1
        l = a + 1
        while a < len(nums)-1:
            ans = nums[r] + nums[l] + nums[a]
            if ans == 0:
                if([nums[r], nums[l], nums[a]]) not in sol:
                    sol.append([nums[r], nums[l], nums[a]])
            if ans < 0:
                l+=1
            else: 
                r-=1
            if l >= r:
                a+= 1
                l = a + 1
                r = len(nums)-1
        return sol
            