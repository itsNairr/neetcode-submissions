class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combs = []

        def helper(i, ccomb):
            if sum(ccomb) == target:
                combs.append(ccomb.copy())
                return
            if i >= len(nums) or sum(ccomb) > target:
                return

            ccomb.append(nums[i])   
            helper(i, ccomb)
            ccomb.pop()
            helper(i + 1, ccomb)
            
        helper(0, [])
        return combs     