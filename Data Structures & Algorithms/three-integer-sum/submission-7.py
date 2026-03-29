class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        check = set()
        print(nums)
        for index, val in enumerate(nums):
            print(val)
            l, r = index+1, len(nums)-1
            while l < r:
                summ = val + nums[l] + nums[r]
                if summ == 0:
                    if (val, nums[l], nums[r]) not in check:
                        check.add((val, nums[l], nums[r]))
                        res.append([val, nums[l], nums[r]])
                    r -= 1
                    l += 1
                elif summ > 0:
                    r -= 1
                else:
                    l += 1

        return res