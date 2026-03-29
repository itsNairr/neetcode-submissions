class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        print(nums)
        for i, a in enumerate(nums):
            if a > target:
                break
            if i > 0 and nums[i] == nums[i-1]:
                    continue
            for j in range(i+1, len(nums)):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                l = j + 1
                r = len(nums) -1
                while l < r:
                    ans = a + nums[j] + nums[l] + nums[r]
                    if ans == target:
                        res.append([a, nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]:
                            l+=1
                    elif ans > target:
                        r -= 1
                    else:
                        l += 1
        return res
