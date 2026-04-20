class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subset = []
        nums.sort()
        def helper(i, cset):
            if i >= len(nums):
                subset.append(cset.copy())
                return

            cset.append(nums[i])
            helper(i + 1, cset)
            cset.pop()

            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            
            helper(i + 1, cset)
        
        helper(0, [])

        return subset
