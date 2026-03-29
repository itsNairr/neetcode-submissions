class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        if len(nums) == 1:
            return nums
        res = [1] * len(nums)
        post = [1] * len(nums)
        ret = [1] * len(nums)
        for i in range(0, len(nums)):
            if i == 0:
                res[i] = nums[i]
            else:
                res[i] = nums[i] * res[i-1]
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                post[i] = nums[i]
            else:
                post[i] = nums[i] * post[i+1]
        for i in range(0, len(nums)):
            if i == 0:
                ret[i] = 1*post[i+1]
            elif i == len(nums)-1:
                ret[i] = res[i-1]*1
            else:
                ret[i] = res[i-1]*post[i+1]
        return ret

        

        