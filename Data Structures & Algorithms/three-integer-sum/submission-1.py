class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if nums is None:
            return []
        nums.sort()
        l = 1
        r = len(nums)-1
        k = 0
        ret = []
        print(nums)
        while k is not len(nums)-2:
            summ = nums[k] + nums[l] + nums[r]
            combo = [nums[k], nums[l], nums[r]]
            print(summ)
            print(l)
            if l >= r:
                k+=1
                l = k+1
                r = len(nums)-1
            elif summ == 0:
                if combo not in ret:
                    ret.append(combo)
                l += 1
                r = len(nums)-1
            elif summ > 0:
                r-=1
            else:
                l+=1
        return ret