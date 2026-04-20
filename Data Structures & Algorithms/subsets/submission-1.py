class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets, curset = [], []

        def helper(i, cset):
            if i >= len(nums):
                subsets.append(cset.copy())
                return
            
            cset.append(nums[i])
            helper(i + 1, cset)
            cset.pop()

            helper(i + 1, cset)
        
        helper(0, curset)
        return subsets
